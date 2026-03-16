import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import asyncio
import uuid
import streamlit as st

from app.router_agent import build_router_agent, ask_router_agent


st.set_page_config(
    page_title="Personal Multi-Agent Assistant",
    page_icon="🤖",
    layout="centered",
)

st.title("Personal Multi-Agent Assistant")
st.caption("Self-help + Software Engineering mentor")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hey — ask me about self-help books, software engineering books, "
                "project structure, clean code, habits, or mindset."
            ),
        }
    ]

if "agent" not in st.session_state:
    with st.spinner("Starting assistant..."):
        st.session_state.agent = asyncio.run(
            build_router_agent(st.session_state.thread_id)
        )

with st.sidebar:
    st.subheader("Session")
    st.write(f"Thread ID: `{st.session_state.thread_id[:8]}`")

    if st.button("Reset chat"):
        st.session_state.thread_id = str(uuid.uuid4())
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "New chat started. Ask me about self-help or software engineering."
                ),
            }
        ]
        st.session_state.agent = asyncio.run(
            build_router_agent(st.session_state.thread_id)
        )
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = asyncio.run(
                ask_router_agent(
                    st.session_state.agent,
                    st.session_state.thread_id,
                    prompt,
                )
            )
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})