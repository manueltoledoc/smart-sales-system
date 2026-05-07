import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(
    page_title="Smart Sales System",
    page_icon="🤖"
)

st.title("Smart Sales System")
st.write("Chatbot comercial inicial")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "Eres un asistente comercial profesional."
        }
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

user_input = st.chat_input("Escribe tu mensaje")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    response = client.responses.create(
        model="gpt-4o-mini",
        input=st.session_state.messages
    )

    assistant_reply = response.output_text

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    with st.chat_message("assistant"):
        st.write(assistant_reply)
