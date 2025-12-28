# BERT-Based Semantic Category Search

This repository implements a **BERT-based semantic category retrieval system** that maps free-text user queries to relevant business categories from a large, fixed taxonomy (JD-scale).

The goal of this project is to **showcase correct, production-oriented usage of BERT embeddings** for semantic search, while **intentionally avoiding LLM embeddings** where they are not required.

---

## Problem Statement

Users express intent in **natural language**, while platforms operate on a **predefined category taxonomy**.

Examples:
- “want to shift my house next week”
- “ac not cooling need urgent repair”
- “voltas ac service”

The challenge is to bridge this gap **reliably and at scale**, without:
- brittle keyword matching
- hard-to-debug classification models
- unnecessary reliance on large language models

---

## Solution Overview

The system follows a layered retrieval design:

User Query
↓
BERT Embedding (Semantic Understanding)
↓
Vector Similarity Search (High Recall)
↓
Lightweight Re-ranking (Business Correctness)
↓
Top-K Relevant Categories


BERT is used strictly for **semantic retrieval**, not for final decision-making.

---

## Why BERT Embeddings?

BERT (via `sentence-transformers`) converts:
- user queries
- category names with descriptions

into dense vector embeddings in a shared semantic space.

This enables:
- understanding of synonyms and paraphrases
- handling of long, conversational queries
- retrieval even when keywords do not exactly match

BERT is used **only as an encoder**, which is its strongest and most reliable use case.

---

## Why LLM Embeddings Were Not Used

LLM embeddings (e.g. OpenAI embeddings) were **intentionally not used** in this project.

### Reasons

**1. Control & Determinism**  
BERT runs locally, with predictable and reproducible behaviour and no external API dependency.

**2. Cost & Scalability**  
Category embeddings are computed once, and query embeddings are fast and free at scale, with no per-request token cost.

**3. Clear Separation of Responsibilities**  
Embeddings are used only for retrieval, while business correctness is handled via ranking logic. LLMs are unnecessary for deterministic category lookup over a fixed taxonomy.

**4. Correct Use of LLMs**  
LLMs are better suited for conversational flows, attribute extraction, and follow-up questioning — not for basic category retrieval.

---

## Why Not Pure BERT Classification?

Pure classification was deliberately avoided because:
- large taxonomies require extensive labelled data
- categories evolve frequently
- misclassifications are hard to debug and control

Semantic retrieval + ranking is more robust, interpretable, and extensible.

---

## Handling Real-World Search Issues

**Brand Over-Ranking**  
Brand-specific categories (e.g. `AC Repair & Services-Voltas`) are penalised by default and surfaced only when the brand is explicitly mentioned in the query.

**Action vs Object Intent**  
Queries such as “want to shift my house” are correctly mapped to **services** (Packers & Movers) rather than **accommodation**, using intent-aware re-ranking.

These corrections are implemented as **lightweight, explainable ranking signals**, not hardcoded category rules.

---

## Project Structure

bert_category_search/
│
├── data/ # Category data & generation
├── models/ # BERT encoder abstraction
├── index/ # In-memory embedding index
├── search/ # Semantic search + re-ranking
├── app/ # Entry point
└── README.md



---

## Tech Stack

- Python 3
- sentence-transformers (MiniLM, BERT-based)
- NumPy
- Cosine similarity (vector search)

---

## What This Project Demonstrates

- Correct usage of BERT embeddings
- Clear separation between retrieval and ranking
- Practical handling of real-world taxonomy noise
- Production-aligned semantic search design
- Conscious decision not to overuse LLMs

---

## Non-Goals

- Fine-tuning BERT
- Training deep ML models
- Replacing business logic with LLMs
- Learning ranking weights from user traffic

These exclusions are intentional.

---

## Key Takeaway

**BERT embeddings are used where semantic understanding is required,  
and simple, explainable logic is used where business correctness matters.**

This balance is deliberate and production-oriented.
