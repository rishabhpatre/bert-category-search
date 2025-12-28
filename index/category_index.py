from index.build_index import build_category_index


class CategoryIndex:
    """
    Holds category metadata and embeddings in memory.
    """

    def __init__(self):
        self.categories, self.embeddings = build_category_index()
