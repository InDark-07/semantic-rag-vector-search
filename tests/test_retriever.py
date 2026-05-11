from app.rag_pipeline import RAGPipeline


def test_retrieval_pipeline():
    pipeline = RAGPipeline()

    results = pipeline.raw_vector_search(
        "How does the system handle peak load?"
    )

    assert len(results) > 0