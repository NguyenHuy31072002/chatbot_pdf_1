from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from utils.embeddings import get_embeddings
from utils.session import get_session_id
import google.generativeai as genai
import os

# Load biến môi trường từ file .env
load_dotenv()

# Lấy API key từ biến môi trường và cấu hình Google Gemini API
api_key = os.getenv("GOOGLE_API_KEY")

# Load API key từ .env
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Tạo chuỗi hỏi đáp
def create_qa_chain(prompt, db):
    def custom_llm(query, context):
        full_prompt = prompt.format(context=context, question=query)
        response = model.generate_content(full_prompt)
        if "Câu trả lời không có trong ngữ cảnh" in response.text:
            response = model.generate_content(query)
        return response.text

    class CustomRetrievalQA:
        def __init__(self, retriever, prompt):
            self.retriever = retriever
            self.prompt = prompt

        def invoke(self, inputs):
            query = inputs["query"]
            docs = self.retriever.get_relevant_documents(query)
            context = " ".join([doc.page_content for doc in docs])
            return {"answer": custom_llm(query, context)}

    retriever = db.as_retriever(search_kwargs={"k": 3}, max_tokens_limit=6000)
    return CustomRetrievalQA(retriever, prompt)

# Xử lý đầu vào của người dùng
def user_input(user_question):
    session_id = get_session_id()
    embeddings = get_embeddings()
    new_db = FAISS.load_local(f"faiss_index_{session_id}", embeddings, allow_dangerous_deserialization=True)
    retriever = new_db.as_retriever()

    prompt_template = """
    Trả lời câu hỏi chi tiết nhất có thể từ ngữ cảnh được cung cấp. Nếu câu trả lời không nằm trong ngữ cảnh được cung cấp, hãy nói, "câu trả lời không có trong ngữ cảnh".

    Context:\n {context}\n
    Question: \n{question}\n

    Trả lời:
    """
    qa_chain = create_qa_chain(prompt_template, new_db)

    response = qa_chain.invoke({"query": user_question})
    return {"output_text": [response["answer"]]}
