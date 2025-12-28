from models.encoder import BertEncoder
from data.categories import CATEGORIES


def build_category_index():
    encoder = BertEncoder()

    texts = [
        f"{cat['name']}. {cat['description']}"
        for cat in CATEGORIES
    ]

    embeddings = encoder.encode(texts)

    return CATEGORIES, embeddings
