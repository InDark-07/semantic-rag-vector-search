import numpy as np
from app.vector_store import VectorStore


def test_vector_store_search():
    dimension = 4

    store = VectorStore(dimension)

    embeddings = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0]
    ]).astype("float32")

    docs = ["doc1", "doc2"]

    store.add_embeddings(embeddings, docs)

    query = np.array([1, 0, 0, 0]).astype("float32")

    results = store.search(query, top_k=1)

    assert results[0]["document"] == "doc1"