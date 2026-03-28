from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

def chunk_documents(documents: List[str]) -> List[str]:
    chunks = []
    for doc in documents:
        chunks.extend(splitter.split_text(doc))
    return chunks
