import redis
import json
import hashlib

class RedisCache:
    def __init__(self, host="localhost", port=6379):
        self.client = redis.Redis(host=host, port=port, decode_responses=True)

    def _key(self, query):
        return hashlib.md5(query.encode()).hexdigest()

    def get(self, query):
        key = self._key(query)
        value = self.client.get(key)
        return json.loads(value) if value else None

    def set(self, query, response):
        key = self._key(query)
        self.client.set(key, json.dumps(response), ex=3600)
