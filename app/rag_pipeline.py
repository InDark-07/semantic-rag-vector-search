from app.embedding_service import EmbeddingService
from app.vector_store import VectorStore
from app.retriever import Retriever
from app.query_expander import QueryExpander
from app.dataset import TECHNICAL_DOCUMENTS


class RAGPipeline:
    def __init__(self):
        self.embedding_service = EmbeddingService()

        sample_embedding = self.embedding_service.embed_query("sample")

        self.vector_store = VectorStore(
            dimension=len(sample_embedding)
        )

        self.query_expander = QueryExpander()

        self._ingest_documents()

        self.retriever = Retriever(
            self.embedding_service,
            self.vector_store
        )

    def _ingest_documents(self):
        embeddings = self.embedding_service.embed_documents(
            TECHNICAL_DOCUMENTS
        )

        self.vector_store.add_embeddings(
            embeddings,
            TECHNICAL_DOCUMENTS
        )

    def raw_vector_search(self, query: str):
        return self.retriever.retrieve(query)

    def enhanced_retrieval(self, query: str):
        expanded_query = self.query_expander.expand_query(query)
        return self.retriever.retrieve(expanded_query)