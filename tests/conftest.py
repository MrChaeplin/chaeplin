# Test for: pytest shared fixtures/configuration
# Description: Shared pytest fixtures for tests
import logging
from datetime import datetime
import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    today = datetime.now().strftime("%Y-%m-%d")
    log_dir = "tests/logs"
    os.makedirs(log_dir, exist_ok=True)

    log_filename = os.path.join(log_dir, f"test_result_{today}.log")

    if not logging.getLogger().hasHandlers():
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] %(levelname)s - %(message)s",
            encoding="utf-8",
            handlers=[
                logging.FileHandler(log_filename, encoding="utf-8"),
                logging.StreamHandler(),
            ],
        )

    logging.getLogger().info("=== test log start ===")
