from app.rag_pipeline import RAGPipeline


pipeline = RAGPipeline()

query = "How does the system handle peak load?"

print("\n===== Strategy A: Raw Vector Search =====\n")

raw_results = pipeline.raw_vector_search(query)

for idx, result in enumerate(raw_results, start=1):
    print(f"Result {idx}:")
    print(result["document"])
    print(f"Score: {result['score']}")
    print()


print("\n===== Strategy B: Enhanced Retrieval =====\n")

expanded_results = pipeline.enhanced_retrieval(query)

for idx, result in enumerate(expanded_results, start=1):
    print(f"Result {idx}:")
    print(result["document"])
    print(f"Score: {result['score']}")
    print()