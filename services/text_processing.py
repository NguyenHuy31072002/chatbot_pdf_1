from langchain.text_splitter import RecursiveCharacterTextSplitter

# Tách văn bản thành các đoạn
def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = splitter.split_text(text)
    return chunks
