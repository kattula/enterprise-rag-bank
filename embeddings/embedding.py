# embedding.py
from vertexai.language_models import TextEmbeddingModel

model = TextEmbeddingModel.from_pretrained("textembedding-gecko")

def get_embedding(text):
    return model.get_embeddings([text])[0].values
