import streamlit as st
import google.generativeai as genai
import os

# Load knowledge base
with open("teslaberry_content_final.txt", "r", encoding="utf-8") as f:
    website_knowledge = f.read()

# --- Simple chunking function ---
def split_text(text, chunk_size=2000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

chunks = split_text(website_knowledge)

# API key setup
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Correct model name
model = genai.GenerativeModel("gemini-1.5-pro")

st.set_page_config(page_title="🤖 Teslaberry Chatbot", layout="centered")
st.title("🤖 Chat with Teslaberry Bot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_relevant_context(query, k=2):
    """Simple keyword search to pick relevant chunks."""
    query_lower = query.lower()
    scored = [(chunk, chunk.lower().count(query_lower)) for chunk in chunks]
    scored.sort(key=lambda x: x[1], reverse=True)
    return " ".join([chunk for chunk, score in scored[:k] if score > 0]) or chunks[0]

user_input = st.chat_input("Ask me anything about Teslaberry...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    # Fetch only relevant knowledge
    relevant_context = get_relevant_context(user_input)

    prompt = f"""
    You are an AI assistant for Teslaberry. 
    Here is some knowledge about Teslaberry:
    {relevant_context}

    Based on this, answer the user's question clearly and concisely.
    Question: {user_input}
    """

    try:
        response = model.generate_content(prompt)
        reply = response.text if hasattr(response, "text") else "⚠️ No response received."
    except Exception as e:
        reply = f"⚠️ API error: {str(e)}"

        reply=reply + prompt

    st.session_state.chat_history.append({"role": "assistant", "text": reply})

# Show chat history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["text"])
