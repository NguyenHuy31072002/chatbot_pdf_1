from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from utils.session import get_session_id
import streamlit as st

# Tạo và lưu vector store
def get_vector_store(chunks):
    session_id = get_session_id()
    embeddings = SentenceTransformerEmbeddings(model_name="keepitreal/vietnamese-sbert", model_kwargs={"trust_remote_code": True})
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local(f"faiss_index_{session_id}")
    st.session_state[session_id]['vector_store'] = vector_store
