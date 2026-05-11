# Semantic RAG & Vector Search Assessment

## Overview

This project implements a local Retrieval-Augmented Generation (RAG)
pipeline focused on:

- Embeddings
- Vector databases
- Retrieval logic
- Benchmarking
- Query expansion

---

# Architecture

User Query
    ↓
Embedding Generation
    ↓
FAISS Vector Search
    ↓
Top-K Retrieved Chunks

Enhanced Retrieval adds:

User Query
    ↓
Query Expansion Model
    ↓
Embedding Generation
    ↓
FAISS Search
    ↓
Improved Semantic Results

---

# Installation
bash pip install -r requirements.txt
`

---

# Run Application
bash python main.py
---

# Run Benchmark
bash python benchmark.py
---

# Run Tests
bash pytest
---

# Similarity Metric Choice

This implementation uses Cosine Similarity.

Reason:

* Sentence embeddings rely more on angular similarity than raw magnitude.
* Cosine similarity works better for semantic retrieval.
* FAISS IndexFlatIP combined with vector normalization effectively computes cosine similarity.

Why not Euclidean Distance?

* Euclidean distance becomes less effective in high-dimensional embedding spaces.
* Two semantically similar vectors may still have large Euclidean distances.

---

# Migration to Vertex AI Vector Search

In production, this system can migrate to:

* Vertex AI Embeddings API
* Vertex AI Matching Engine
* Gemini models for query rewriting

Migration Steps:

1. Replace local embedding model with:
python from vertexai.language_models import TextEmbeddingModel
2. Replace FAISS with:

* Vertex AI Matching Engine Index
* Matching Engine Endpoint

3. Store embeddings in:

* GCS
* BigQuery
* Vertex AI Vector Search Index

4. Replace mocked query expansion with:
python from vertexai.generative_models import GenerativeModel
5. Add:

* Hybrid search
* Metadata filtering
* Re-ranking
* Streaming updates
* Monitoring and observability

---

# Key Features

* Modular architecture
* Local semantic search
* Query expansion pipeline
* Benchmark comparison
* Mocked Vertex AI SDK
* Production-ready structure
* Unit tested
--- # Expected Benchmark Output
json
[
    {
        "query": "How does the system handle peak load?",
        "strategy_a_raw_vector_search": [
            {
                "score": 0.82,
                "document": "The distributed backend system handles peak load..."
            }
        ],
        "strategy_b_enhanced_retrieval": [
            {
                "score": 0.91,
                "document": "Container orchestration is handled using Kubernetes..."
            }
        ]
    }
]