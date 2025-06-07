import streamlit as st
from groq import Groq

# 👉 Replace with your actual Groq API key
GROQ_API_KEY = ""

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Page config
st.set_page_config(page_title="Chatbot with Groq", page_icon="🤖")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🤖 Groq Chatbot (LLaMA 3)")

# Chat display
for user_msg, bot_msg in st.session_state.chat_history:
    st.chat_message("user").markdown(user_msg)
    st.chat_message("assistant").markdown(bot_msg)

# User input box
user_input = st.chat_input("Say something...")

def get_response(prompt, history):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for u, a in history:
        messages.append({"role": "user", "content": u})
        messages.append({"role": "assistant", "content": a})
    messages.append({"role": "user", "content": prompt})

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {e}"

# Process input
if user_input:
    bot_reply = get_response(user_input, st.session_state.chat_history)
    st.session_state.chat_history.append((user_input, bot_reply))
    st.rerun()
