from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Union


class BertEncoder:
    """
    BERT-based sentence encoder using MiniLM.

    Responsibility:
    - Convert text into dense vector embeddings
    - Ensure embeddings are normalized for cosine similarity
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(
        self,
        texts: Union[str, List[str]],
        normalize: bool = True
    ) -> np.ndarray:
        """
        Encode text(s) into vector embeddings.

        Args:
            texts: A string or list of strings to encode
            normalize: Whether to L2-normalize embeddings

        Returns:
            NumPy array of embeddings
        """

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=normalize
        )

        return embeddings
