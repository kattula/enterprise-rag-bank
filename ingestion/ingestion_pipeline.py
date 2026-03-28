# ingestion_pipeline.py
from langchain.text_splitter import RecursiveCharacterTextSplitter

def process_document(doc):
    chunks = splitter.split_text(doc)
    return chunks
