import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("rag-system")

def log_request(query, latency):
    logger.info(f"Query: {query} | Latency: {latency}")
