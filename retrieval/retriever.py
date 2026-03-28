from embeddings.embedding_model import EmbeddingModel

class Retriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.embedder = EmbeddingModel()

    def retrieve(self, query: str, k=5):
        query_vec = self.embedder.embed([query])
        docs = self.vector_store.search(query_vec, k)
        return docs
