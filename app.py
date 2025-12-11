# app.py
import streamlit as st
from dublin_rag import rag_answer  # import your function

st.set_page_config(page_title="Dublin Regulation RAG", page_icon="📘")

st.title("Migrants Rights & Guidance Platform")
st.write("Ask a question and get an answer based on the Dublin Regulation PDF (local Llama 3 via Ollama).")

# Optional: simple chat history
if "history" not in st.session_state:
    st.session_state.history = []

for role, content in st.session_state.history:
    with st.chat_message(role):
        st.markdown(content)

user_question = st.chat_input("Type your question about the Dublin Regulation...")
if user_question:
    # show user message
    st.session_state.history.append(("user", user_question))
    with st.chat_message("user"):
        st.markdown(user_question)

    # get model answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = rag_answer(user_question)
        st.markdown(answer)
    st.session_state.history.append(("assistant", answer))
