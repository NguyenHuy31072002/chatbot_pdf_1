import streamlit as st
from utils.session import get_session_id, clear_chat_history
from services.file_processing import get_pdf_text, get_docx_text
from services.text_processing import get_text_chunks
from services.vector_store import get_vector_store
from services.chatbot import user_input

def main():
    session_id = get_session_id()
    st.set_page_config(page_title="Gemini PDF & DOC Chatbot", page_icon="🤖")

    # Sidebar for uploading PDF and DOCX files
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files", type=["pdf"], accept_multiple_files=True)
        docx_docs = st.file_uploader("Upload your DOCX Files", type=["docx"], accept_multiple_files=True)

        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                raw_text += get_docx_text(docx_docs)  # Combine text from PDF and DOCX
                if raw_text:
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success(f"Processed {len(pdf_docs)} PDFs and {len(docx_docs)} DOCs.")
                else:
                    st.error("No text extracted from the PDFs or DOCX files.")

    # Main content area for displaying chat messages
    st.title("Chat with PDF and DOCX files using Gemini🤖")
    st.write("Welcome to the chat!")
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    if session_id not in st.session_state:
        st.session_state[session_id] = {"messages": [{"role": "assistant", "content": "Upload some PDFs or DOCs and ask me a question."}]}

    for message in st.session_state[session_id]['messages']:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input():
        st.session_state[session_id]['messages'].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        if st.session_state[session_id]['messages'][-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = user_input(prompt)
                    full_response = ''.join(response['output_text'])
                    st.write(full_response)

                    st.session_state[session_id]['messages'].append({"role": "assistant", "content": full_response})

if __name__ == "__main__":
    main()
