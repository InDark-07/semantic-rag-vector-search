# Installation

## Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

# Run Application

```bash
python3 main.py
```

This runs:
- Strategy A → Raw Vector Search
- Strategy B → AI-Enhanced Retrieval

---

# Run Benchmark

```bash
python3 benchmark.py
```

This generates a structured comparison report between:
- Raw Vector Search
- Query Expansion Retrieval

---

# Run Tests

```bash
python3 -m pytest
```

Expected Output:

```bash
================== test session starts ==================
collected 4 items

tests/test_embedding_service.py .
tests/test_query_expander.py .
tests/test_retriever.py .
tests/test_vector_store.py .

================== 4 passed ==================
```

---

# Similarity Metric Choice

This implementation uses **Cosine Similarity**.

## Why Cosine Similarity?

- Sentence embeddings depend more on angular similarity than vector magnitude.
- Cosine similarity performs better for semantic retrieval tasks.
- FAISS `IndexFlatIP` combined with vector normalization effectively computes cosine similarity.

## Why Not Euclidean Distance?

Euclidean distance becomes less effective in high-dimensional embedding spaces because:

- Semantically similar vectors may still have large Euclidean distances.
- Embedding magnitude can distort similarity calculations.

Cosine similarity is therefore preferred for NLP embedding systems.
