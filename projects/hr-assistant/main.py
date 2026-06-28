"""
HR Assistant — answers employee questions from YOUR company policies.

How it works: it reads every document in the "policies" folder, then answers
an employee's question using ONLY those documents. If the answer isn't in your
policies, it says so and points them to a human — it never guesses about HR.

You don't need to understand every line. The comments explain each step in
plain English, like a recipe.
"""

# --- Step 1: Bring in the tools we need ---
import os                          # helps us find the policy files on disk
import glob                        # finds all the policy documents in the folder
from anthropic import Anthropic    # the official kit for talking to the Claude AI
from dotenv import load_dotenv     # loads your secret key from the private .env file

# --- Step 2: Open the line to the AI ---
load_dotenv()
client = Anthropic()

# The folder where your policy documents live (sits right next to this script).
POLICIES_FOLDER = os.path.join(os.path.dirname(__file__), "policies")


# --- Step 3: Read all your policy documents ---
def load_policies() -> str:
    """Read every document in the policies folder and stitch them together."""
    files = sorted(glob.glob(os.path.join(POLICIES_FOLDER, "*.md")))
    if not files:
        return ""
    pieces = []
    for path in files:
        name = os.path.basename(path)
        with open(path, "r") as f:
            pieces.append(f"--- Document: {name} ---\n{f.read()}")
    return "\n\n".join(pieces)


# --- Step 4: Answer one question, grounded in the policies ---
def ask_hr(question: str, policies: str) -> str:
    """Answer an employee question using only the company policies."""

    # These are the AI's standing instructions — its job description and its rules.
    # The guardrails (rules 1 and 2) are what make this safe to use for HR.
    instructions = (
        "You are a warm, helpful HR assistant for a small company. "
        "Answer the employee's question using ONLY the company policies below.\n\n"
        "Rules you must always follow:\n"
        "1. If the answer is not clearly in the policies, say you don't have that "
        "information and suggest they contact the HR team. NEVER guess.\n"
        "2. For sensitive or personal matters — complaints, disputes, pay, "
        "performance, health, or anything about a specific individual — do not try "
        "to resolve it. Kindly point the employee to a human in HR.\n"
        "3. Point to the relevant policy when you can, so your answer is trustworthy.\n"
        "4. Be concise and kind.\n\n"
        "=== COMPANY POLICIES ===\n"
        f"{policies}"
    )

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        system=instructions,                # the AI's job description + the policies
        messages=[{"role": "user", "content": question}],   # the employee's question
    )
    return response.content[0].text


# --- Step 5: What runs when you start the program ---
if __name__ == "__main__":
    print("\n💼  HR Assistant\n")

    policies = load_policies()
    if not policies:
        print("No policy documents found in the 'policies' folder.")
        print("Add your handbook there and try again.\n")
    else:
        question = input("Ask an HR question, then press Enter:\n> ").strip()
        if not question:
            print("\nNo question entered. Run it again and type one in.\n")
        else:
            print("\nChecking the policies...\n")
            try:
                print(ask_hr(question, policies))
                print()
            except Exception as error:
                print("Something went wrong — most often a missing AI key.")
                print(f"(Technical detail for your assistant: {error})\n")
