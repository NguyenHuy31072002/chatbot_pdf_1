from langchain_community.embeddings import SentenceTransformerEmbeddings
import openai
# Trả về Embeddings
def get_embeddings():
    return SentenceTransformerEmbeddings(model_name="keepitreal/vietnamese-sbert", model_kwargs={"trust_remote_code": True})


# Trả về Embeddings
def get_embeddings_OpenAI(text):
    # Đặt API key của bạn
    openai.api_key = 'YOUR_API_KEY'
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"  # Hoặc một model khác mà bạn muốn
    )
    return response['data'][0]['embedding']