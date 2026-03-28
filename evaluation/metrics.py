def recall_at_k(retrieved, relevant):
    return len(set(retrieved) & set(relevant)) / len(relevant)

def precision_at_k(retrieved, relevant):
    return len(set(retrieved) & set(relevant)) / len(retrieved)
