"""
Positioning Teardown Agent — your first REAL agent.

The big difference from your earlier tools: those asked the AI one question and
got one answer. THIS one runs in a LOOP — you give it a goal and a tool, and the
AI decides for itself what to do next: which pages to read, when it has enough,
and what to conclude. You get to WATCH it choose.

What it does: you give it a brand or competitor's website. It reads the site
(fetching extra pages if it wants), then returns a positioning teardown plus a
pitch angle for how your agency could help them.
"""

import sys
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

MODEL = "claude-opus-4-8"


# ---------------------------------------------------------------------------
# THE TOOL: fetch a web page — the agent's "hands" on the web.
# The AI can't browse on its own. It ASKS us to run this; we hand back the
# result. That request-and-return is the heart of how agents use tools.
# ---------------------------------------------------------------------------
def fetch_url(url: str) -> str:
    """Download a web page and return its visible text + the links on it."""
    try:
        resp = requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0 (teardown-agent)"},
        )
        resp.raise_for_status()
    except Exception as error:
        return f"ERROR fetching {url}: {error}"

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):   # drop code, keep words
        tag.decompose()

    title = soup.title.get_text(strip=True) if soup.title else "(no title)"
    text = " ".join(soup.get_text(separator=" ").split())[:5000]

    # Collect same-site links so the AI can choose to read more pages.
    base = urlparse(url).netloc
    links = []
    for a in soup.find_all("a", href=True):
        full = urljoin(url, a["href"])
        if urlparse(full).netloc == base and full not in links:
            links.append(full)
        if len(links) >= 15:
            break

    return (
        f"TITLE: {title}\n\n"
        f"TEXT (first 5000 chars):\n{text}\n\n"
        f"LINKS ON THIS PAGE:\n" + "\n".join(links)
    )


# How we describe the tool TO the AI, so it knows when and how to use it.
TOOLS = [
    {
        "name": "fetch_url",
        "description": (
            "Fetch a web page and get back its visible text and the links on it. "
            "Use this to read a company's website — start with their homepage, then "
            "follow links like 'About' or 'Services' if you need more to understand "
            "their positioning."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "The full URL to fetch"}
            },
            "required": ["url"],
        },
    }
]


def run_agent(start_url: str) -> None:
    """Give the AI a goal + the fetch tool, then let it drive in a loop."""

    goal = (
        f"You are a sharp brand strategist at a marketing agency. "
        f"Do a positioning teardown of the company at this website: {start_url}\n\n"
        f"Use the fetch_url tool to read their site — begin with the homepage, and "
        f"follow a couple of relevant links (About, Services) if it helps you "
        f"understand their messaging, audience, and positioning. When you have "
        f"enough, stop fetching and give your final answer with two sections:\n"
        f"1. POSITIONING TEARDOWN — how they position themselves, their messaging, "
        f"audience, strengths, and gaps.\n"
        f"2. PITCH ANGLE — one sharp angle our agency could use to win them."
    )

    messages = [{"role": "user", "content": goal}]

    # THE AGENTIC LOOP. Each time around, the AI either asks for the tool or finishes.
    for step in range(1, 7):
        print(f"\n──────── Step {step}: the AI is thinking… ────────")
        response = client.messages.create(
            model=MODEL,
            max_tokens=2500,
            tools=TOOLS,
            messages=messages,
        )

        # Show what the AI said and/or decided to do this turn.
        tool_results = []
        for block in response.content:
            if block.type == "text" and block.text.strip():
                print(f"\n💬 AI: {block.text.strip()}")
            elif block.type == "tool_use":
                url = block.input.get("url", "")
                print(f"\n🔧 The AI decided to FETCH: {url}")
                result = fetch_url(url)
                first_line = result.splitlines()[0] if result else ""
                print(f"   📄 got it ({len(result)} chars) — {first_line}")
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })

        # Save the AI's turn to the running conversation.
        messages.append({"role": "assistant", "content": response.content})

        # If it asked for the tool, hand back the results and loop again.
        if response.stop_reason == "tool_use":
            messages.append({"role": "user", "content": tool_results})
            continue

        # Otherwise it's done.
        print("\n════════ ✅ The AI finished — final teardown is above. ════════\n")
        return

    print("\n(Reached the step limit — stopping so it can't loop forever.)\n")


if __name__ == "__main__":
    print("\n🔍  Positioning Teardown Agent\n")
    url = sys.argv[1] if len(sys.argv) > 1 else input("Enter a brand's website URL:\n> ").strip()
    if not url:
        print("No URL entered. Run it again with a website address.\n")
    elif not url.startswith("http"):
        print("Please include the full address, starting with http:// or https://\n")
    else:
        run_agent(url)
