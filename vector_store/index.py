import faiss
import numpy as np
from typing import List

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, embeddings: List[List[float]], texts: List[str]):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.texts.extend(texts)

    def search(self, query_vector, k=5):
        D, I = self.index.search(query_vector, k)
        return [self.texts[i] for i in I[0]]
