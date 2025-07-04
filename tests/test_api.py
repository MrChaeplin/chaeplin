# Test for: exchange/binance/api.py
# Description: Unit tests for core BinanceAPI methods (fetch_ticker, create_order, fetch_balance)
from unittest.mock import patch, MagicMock
from exchange.binance.api import BinanceAPI


@patch("exchange.binance.api.ccxt.binance")
def test_fetch_ticker(mock_binance):
    mock_instance = MagicMock()
    mock_instance.fetch_ticker.return_value = {"symbol": "BTC/USDT", "last": 30000}
    mock_binance.return_value = mock_instance

    api = BinanceAPI("spot")
    result = api.fetch_ticker("BTC/USDT")

    assert result["last"] == 30000


@patch("exchange.binance.api.ccxt.binance")
def test_create_order(mock_binance):
    mock_instance = MagicMock()
    mock_instance.create_order.return_value = {
        "id": "chaeplin",
        "status": "open",
        "symbol": "BTC/USDT",
    }
    mock_binance.return_value = mock_instance

    api = BinanceAPI("spot")
    result = api.create_order("BTC/USDT", "market", "buy", 0.01)

    assert result["status"] == "open"


@patch("exchange.binance.api.ccxt.binance")
def test_fetch_balance(mock_binance):
    mock_instance = MagicMock()
    mock_instance.fetch_balance.return_value = {"total": {"BTC": 0.5, "USDT": 1000}}
    mock_binance.return_value = mock_instance

    api = BinanceAPI("spot")
    result = api.fetch_balance()

    assert result["total"]["BTC"] == 0.5
