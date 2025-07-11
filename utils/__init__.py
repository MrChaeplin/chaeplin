import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/trading.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
