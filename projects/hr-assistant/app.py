"""
HR Assistant — WEB version.

Same assistant as main.py, but as a web page your colleagues open in a browser
and chat with, instead of a terminal. We reuse the exact same brain (the
policy-loading and answering logic) from main.py — this file is just the
"front desk" that people see and type into.
"""

import streamlit as st                    # the kit that turns Python into a web page
from main import load_policies, ask_hr    # reuse the logic we already built

# --- Set up the page (title, icon) ---
st.set_page_config(page_title="HR Assistant", page_icon="💼")
st.title("💼 HR Assistant")
st.caption(
    "Ask a question about company policies. "
    "For anything sensitive, I'll point you to a human in HR."
)

# Load the company policies once when the page opens.
policies = load_policies()

# Remember the conversation so it stays on screen as you chat.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show everything said so far.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# The box at the bottom where the employee types their question.
question = st.chat_input("Ask an HR question…")

if question:
    # Show the employee's question.
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Get and show the assistant's answer.
    with st.chat_message("assistant"):
        with st.spinner("Checking the policies…"):
            answer = ask_hr(question, policies)
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
