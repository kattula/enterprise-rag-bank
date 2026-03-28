from rank_bm25 import BM25Okapi

class HybridSearch:
    def __init__(self, corpus: list):
        self.tokenized = [doc.split() for doc in corpus]
        self.bm25 = BM25Okapi(self.tokenized)

    def keyword_search(self, query: str, top_k=5):
        tokens = query.split()
        scores = self.bm25.get_scores(tokens)
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return ranked[:top_k]
