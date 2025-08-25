import streamlit as st
import google.generativeai as genai
import os

# Load your website knowledge (Teslaberry content)
with open("teslaberry_content_final.txt", "r", encoding="utf-8") as f:
    website_knowledge = f.read()

# API Key setup
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")

st.set_page_config(page_title="🤖 Teslaberry Chatbot", layout="centered")
st.title("🤖 Chat with Teslaberry Bot")

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me anything about Teslaberry...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    # Add website context to user query
    prompt = f"""
    You are an AI assistant for Teslaberry. 
    Here is some knowledge about Teslaberry:
    {website_knowledge}

    Based on this, answer the user's question clearly and concisely.
    Question: {user_input}
    """

    response = model.generate_content(prompt)

    # ✅ Safely extract reply text
    if response.candidates:
        reply = "".join(part.text for part in response.candidates[0].content.parts if part.text)
    else:
        reply = "⚠️ Sorry, I couldn't generate a response."

    st.session_state.chat_history.append({"role": "assistant", "text": reply})

# Show chat history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["text"])
