import numpy as np
from index.category_index import CategoryIndex
from models.encoder import BertEncoder


SHIFT_KEYWORDS = {"shift", "shifting", "move", "moving", "relocate"}
REPAIR_KEYWORDS = {
    "repair",
    "fix",
    "service",
    "not cooling",
    "not working",
    "issue",
    "problem"
}


def extract_brand(category_name: str):
    """
    Extract brand or variant from category name if present.
    Example:
      'AC Repair & Services-Voltas' -> 'voltas'
    """
    if "-" not in category_name:
        return None
    return category_name.split("-", 1)[1].lower().strip()


class SemanticCategorySearch:
    """
    Semantic category search using BERT embeddings + lightweight re-ranking.
    """

    def __init__(self):
        self.index = CategoryIndex()
        self.encoder = BertEncoder()

    def _contains_any(self, text: str, keywords: set) -> bool:
        text = text.lower()
        return any(k in text for k in keywords)

    def _rerank(self, query: str, results: list):
        q = query.lower()

        for r in results:
            name = r["category"]
            name_lower = name.lower()

            # -------------------------------
            # 1. Brand penalty (GENERIC RULE)
            # -------------------------------
            brand = extract_brand(name)

            if brand:
                # Penalise brand-specific category
                # unless brand explicitly mentioned in query
                if brand not in q:
                    r["score"] -= 0.25

            # -------------------------------
            # 2. Shift intent handling
            # -------------------------------
            if self._contains_any(q, SHIFT_KEYWORDS):
                if "packers" in name_lower or "movers" in name_lower:
                    r["score"] += 0.4
                if (
                    "rent" in name_lower
                    or "room" in name_lower
                    or "guest house" in name_lower
                ):
                    r["score"] -= 0.3

            # -------------------------------
            # 3. Repair intent handling
            # -------------------------------
            if self._contains_any(q, REPAIR_KEYWORDS):
                if "ac repair" in name_lower:
                    r["score"] += 0.3
                if "air cooler" in name_lower:
                    r["score"] -= 0.2

        return sorted(results, key=lambda x: x["score"], reverse=True)

    def search(self, query: str, top_k: int = 5):
        # Encode query
        query_embedding = self.encoder.encode(query)

        # Vector similarity
        scores = np.dot(self.index.embeddings, query_embedding)

        results = [
            {"category": cat["name"], "score": float(score)}
            for cat, score in zip(self.index.categories, scores)
        ]

        # Re-rank with business-safe logic
        reranked = self._rerank(query, results)

        return [
            {
                "category": r["category"],
                "score": round(r["score"], 4)
            }
            for r in reranked[:top_k]
        ]
