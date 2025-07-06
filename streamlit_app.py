import streamlit as st
import requests

st.set_page_config(page_title="Healthcare RAG Chatbot", layout="centered")
st.title("Healthcare RAG Chatbot")

st.write("Ask a question related to our healthcare documents:")
user_input = st.text_area("Your question:", height=100)

if st.button("Ask") and user_input.strip():
    with st.spinner("Getting answer..."):
        response = requests.post(
            "http://localhost:8000/chat/", json={"message": user_input}
        )
        if response.status_code == 200:
            answer = response.json().get("answer", "No answer returned.")
            # Render answer with newlines and references
            for para in answer.split("\n"):
                st.markdown(para)
        else:
            st.error(f"Error: {response.text}")
