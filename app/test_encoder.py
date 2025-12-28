from models.encoder import BertEncoder

encoder = BertEncoder()

texts = [
    "need someone to click photos at my wedding",
    "wedding photography services"
]

embeddings = encoder.encode(texts)

print(embeddings.shape)
