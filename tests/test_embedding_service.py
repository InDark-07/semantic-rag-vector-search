from app.embedding_service import EmbeddingService


def test_embedding_generation():
    service = EmbeddingService()

    embedding = service.embed_query("hello world")

    assert embedding is not None
    assert len(embedding) > 0