import os
import os
from typing import List
from PyPDF2 import PdfReader

def load_pdfs(directory: str) -> List[str]:
    documents = []

    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            path = os.path.join(directory, file)
            reader = PdfReader(path)

            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""

            documents.append(text)

    return documents
