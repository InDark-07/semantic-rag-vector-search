class Retriever:
    def __init__(self, embedding_service, vector_store):
        self.embedding_service = embedding_service
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k=3):
        query_embedding = self.embedding_service.embed_query(query)
        results = self.vector_store.search(query_embedding, top_k)
        return results