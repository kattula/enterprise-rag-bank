def build_prompt(query: str, docs: list) -> str:
    context = "\n\n".join(docs)

    return f"""
You are a banking assistant.
Answer ONLY from the provided context.
If unsure, say "I don't know".

Context:
{context}

Question:
{query}
"""
