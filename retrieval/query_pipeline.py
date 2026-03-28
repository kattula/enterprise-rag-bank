# query_pipeline.py
def handle_query(query):
    query_emb = get_embedding(query)
    docs = retrieve(query_emb)
    reranked = rerank(query, docs)
    prompt = build_prompt(query, reranked)
    response = call_llm(prompt)
    return response
