from langchain_community.embeddings import SentenceTransformerEmbeddings

# Trả về Embeddings
def get_embeddings():
    return SentenceTransformerEmbeddings(model_name="keepitreal/vietnamese-sbert", model_kwargs={"trust_remote_code": True})
