import json
from app.rag_pipeline import RAGPipeline


pipeline = RAGPipeline()

queries = [
    "How does the system handle peak load?",
    "How is reliability maintained during failures?",
    "How does the platform optimize performance?"
]

benchmark_results = []

for query in queries:
    raw_results = pipeline.raw_vector_search(query)
    enhanced_results = pipeline.enhanced_retrieval(query)

    benchmark_results.append({
        "query": query,
        "strategy_a_raw_vector_search": raw_results,
        "strategy_b_enhanced_retrieval": enhanced_results
    })

print(json.dumps(benchmark_results, indent=4))