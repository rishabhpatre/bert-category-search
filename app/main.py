from search.semantic_search import SemanticCategorySearch


if __name__ == "__main__":
    searcher = SemanticCategorySearch()

    queries = [
        "need someone to click photos at my wedding",
        "ac not cooling need urgent repair",
        "looking for a doctor for heart problem",
        "want to shift my house next week",
        "need a hotel near airport for one night"
    ]

    for q in queries:
        print(f"\nQuery: {q}")
        results = searcher.search(q, top_k=5)
        for r in results:
            print(r)
