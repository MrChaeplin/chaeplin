# Test for: exchange/binance/config.py
# Description: Unit tests for Binance config loader (.env environment variable loading)
from exchange.binance.config import binance_instance


def test_binance_instance_has_api_key_and_secret():
    assert binance_instance.api_key is not None, "API Key is missing"
    assert binance_instance.api_secret is not None, "API Secret is missing"
