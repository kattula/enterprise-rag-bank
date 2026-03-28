import json

def log_feedback(query, response, rating):
    data = {
        "query": query,
        "response": response,
        "rating": rating
    }

    with open("feedback.json", "a") as f:
        f.write(json.dumps(data) + "\n")
