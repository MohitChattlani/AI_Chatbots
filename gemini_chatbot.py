import streamlit as st
import google.generativeai as genai
import os

# Paste your API key here or use an environment variable
GOOGLE_API_KEY = "XXXX"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

st.set_page_config(page_title="🤖 Gemini Chatbot", layout="centered")
st.title("🤖 Chat with Google Gemini")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    # Generate Gemini response
    response = model.generate_content(user_input)
    reply = response.text
    st.session_state.chat_history.append({"role": "assistant", "text": reply})

# Show chat history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["text"])
