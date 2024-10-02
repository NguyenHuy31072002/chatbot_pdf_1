from PyPDF2 import PdfReader
from docx import Document
import streamlit as st
from utils.session import get_session_id
from pdf2image import convert_from_path
import os
from pdf_img.extract_text import extract_text_with_prompt_from_image
from pdf_img.pdf_to_img import pdf_to_images_and_upload

# # Đọc file PDF
# def get_pdf_text(pdf_docs):
#     session_id = get_session_id()
#     text = ""
#     for pdf in pdf_docs:
#         pdf_reader = PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text += page.extract_text() or ""
#     st.session_state[session_id]['pdf_text'] = text
#     return text





def get_pdf_text(pdf_docs):
    
    text = ""

    # Check if pdf_docs is a list or a string
    if not isinstance(pdf_docs, list):
        pdf_docs = [pdf_docs] # Convert to a list if it's a string

    # Thử đọc từng file PDF trong danh sách
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)  # pdf là đường dẫn của từng file PDF
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
        except IsADirectoryError: # Handle the case where the input is a directory
            print(f"Error: {pdf} is a directory, not a PDF file.")
        except FileNotFoundError: # Handle the case where the file doesn't exist
            print(f"Error: {pdf} not found.")
        except PyPDF2.errors.PdfReadError: # Handle the case where the file is not a valid PDF
            print(f"Error: {pdf} is not a valid PDF file.")

        # Nếu văn bản trả về rỗng, chuyển file PDF thành ảnh và trích xuất văn bản từ ảnh
        if not text.strip():
            image_urls = pdf_to_images_and_upload(pdf)  # Chuyển đổi từng file PDF thành ảnh
            prompt = """Trích xuất văn bản từ hình ảnh. Chỉ trả về văn bản, không cần giải thích."""
            for image_url in image_urls:
                response = extract_text_with_prompt_from_image(image_url, prompt)
                text += response.strip() + "\n\n"
    
    return text


# Đọc file DOCX
def get_docx_text(docx_docs):
    session_id = get_session_id()
    text = ""
    for doc in docx_docs:
        document = Document(doc)
        for paragraph in document.paragraphs:
            text += paragraph.text
    st.session_state[session_id]['docx_text'] = text
    return text
