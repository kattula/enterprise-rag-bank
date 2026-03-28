from fastapi import FastAPI
import time

from retrieval.retriever import Retriever
from retrieval.reranker import Reranker
from llm.prompt import build_prompt
from llm.generator import LLMGenerator
from cache.redis_cache import RedisCache
from monitoring.logging import log_request

app = FastAPI()

# Initialize components (singleton style)
vector_store = None  # load your FAISS index
retriever = Retriever(vector_store)
reranker = Reranker()
llm = LLMGenerator()
cache = RedisCache()

@app.post("/query")
def query_api(q: str):
    start = time.time()

    cached = cache.get(q)
    if cached:
        return {"response": cached, "cached": True}

    docs = retriever.retrieve(q)
    docs = reranker.rerank(q, docs)

    prompt = build_prompt(q, docs[:3])
    response = llm.generate(prompt)

    cache.set(q, response)

    latency = time.time() - start
    log_request(q, latency)

    return {"response": response, "latency": latency}
