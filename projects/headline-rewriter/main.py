"""
Headline Rewriter — your first AI tool.

What it does: you type in one marketing headline, and the AI gives you
5 fresh rewrites in different styles. That's it.

You don't need to understand every line. The comments explain what each part
does in plain English. When you're curious, read them top to bottom like a recipe.
"""

# --- Step 1: Bring in the tools we need ---
# "import" means "let me use this pre-built code someone else wrote."
import os                          # lets us read the secret key from the environment
from anthropic import Anthropic    # the official kit for talking to the Claude AI
from dotenv import load_dotenv     # loads your secret key from the private .env file


# --- Step 2: Load your secret key ---
# This reads the .env file two folders up (the one in your Agent-Lab).
load_dotenv()

# Create the "client" — think of it as opening a phone line to the AI.
# It automatically finds your key from the environment.
client = Anthropic()


# --- Step 3: The function that does the actual work ---
def rewrite_headline(headline: str) -> str:
    """Send one headline to the AI and ask for 5 rewrites."""

    # This is the instruction we send to the AI, written in plain English.
    instructions = (
        f'You are a sharp marketing copywriter.\n'
        f'Rewrite this headline 5 different ways. Make each one a distinct '
        f'style: one punchy, one curiosity-driven, one benefit-focused, '
        f'one bold/contrarian, and one elegant/premium.\n'
        f'Return them as a simple numbered list, nothing else.\n\n'
        f'Headline: "{headline}"'
    )

    # Here's the actual call to the AI. We tell it:
    #   - which AI brain to use (model)
    #   - how long the answer can be (max_tokens)
    #   - what we want (our instructions)
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        messages=[{"role": "user", "content": instructions}],
    )

    # The AI's reply comes back in pieces; this grabs the text part.
    return response.content[0].text


# --- Step 4: The part that runs when you start the program ---
if __name__ == "__main__":
    print("\n✍️  Headline Rewriter\n")

    # Ask you to type a headline.
    headline = input("Type a headline to rewrite, then press Enter:\n> ").strip()

    if not headline:
        print("\nNo headline entered — nothing to do. Run it again and type one in.\n")
    else:
        print("\nThinking...\n")
        try:
            result = rewrite_headline(headline)
            print("Here are 5 rewrites:\n")
            print(result)
            print()
        except Exception as error:
            # If something goes wrong (usually a missing key), explain it kindly.
            print("Something went wrong. Most often this means your AI key isn't set up yet.")
            print("Ask your assistant to help you check the .env file.\n")
            print(f"(Technical detail, for your assistant: {error})\n")
