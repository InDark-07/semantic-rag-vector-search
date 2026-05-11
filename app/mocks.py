class MockTextEmbeddingModel:
    """
    Mock implementation of Vertex AI TextEmbeddingModel.
    """

    @classmethod
    def from_pretrained(cls, model_name: str):
        return cls()

    def get_embeddings(self, texts):
        return texts


class MockGenerativeModel:
    """
    Mock implementation of Vertex AI GenerativeModel.
    Used for query expansion.
    """

    def __init__(self, model_name: str):
        self.model_name = model_name

    def generate_content(self, prompt: str):
        expansions = {
            "How does the system handle peak load?": (
                "Explain horizontal scaling, load balancing, autoscaling, "
                "traffic spikes, Kubernetes scaling, and high throughput systems"
            ),

            "How is reliability maintained during failures?": (
                "Explain replication, failover systems, disaster recovery, "
                "redundancy, and node crash handling"
            ),

            "How does the platform optimize performance?": (
                "Explain caching, Redis, indexing, database optimization, "
                "monitoring, and latency reduction"
            )
        }

        return expansions.get(prompt, prompt)