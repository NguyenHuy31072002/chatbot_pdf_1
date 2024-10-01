from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
from utils.session import get_session_id
import streamlit as st
import openai
from langchain.vectorstores import FAISS

# Tạo và lưu vector store
def get_vector_store(chunks):
    session_id = get_session_id()
    embeddings = SentenceTransformerEmbeddings(model_name="keepitreal/vietnamese-sbert", model_kwargs={"trust_remote_code": True})
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local(f"faiss_index_{session_id}")
    st.session_state[session_id]['vector_store'] = vector_store

# Hàm lấy embeddings từ OpenAI
def get_embeddings(text):
    # Đặt API key của bạn
    openai.api_key = 'YOUR_API_KEY'
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"  # Hoặc một model khác mà bạn muốn
    )
    return response['data'][0]['embedding']


# Tạo và lưu vector store
def get_vector_store_openai(chunks):
    session_id = get_session_id()
    
    # Tạo embeddings cho từng chunk
    embeddings = [get_embeddings(chunk) for chunk in chunks]
    
    # Tạo vector store từ embeddings
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    
    # Lưu vector store vào file
    vector_store.save_local(f"faiss_index_{session_id}")
    
    # Lưu vào session state
    st.session_state[session_id]['vector_store'] = vector_store