import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatIP(dimension)
        self.documents = []

    def add_embeddings(self, embeddings, documents):
        normalized = self._normalize(embeddings)
        self.index.add(normalized)
        self.documents.extend(documents)

    def search(self, query_embedding, top_k=3):
        query_embedding = self._normalize(
            np.array([query_embedding])
        )

        scores, indices = self.index.search(query_embedding, top_k)

        results = []

        for idx, score in zip(indices[0], scores[0]):
            results.append({
                "document": self.documents[idx],
                "score": float(score)
            })

        return results

    @staticmethod
    def _normalize(vectors):
        norms = np.linalg.norm(vectors, axis=1, keepdims=True)
        return vectors / norms