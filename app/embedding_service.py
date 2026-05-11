from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents):
        embeddings = self.model.encode(documents, convert_to_numpy=True)
        return embeddings

    def embed_query(self, query: str):
        embedding = self.model.encode([query], convert_to_numpy=True)
        return embedding[0]