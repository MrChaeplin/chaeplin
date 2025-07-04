# Test for: exchange/binance/spot.py
# Description: Unit tests for BinanceSpot (market/limit order)
from unittest.mock import patch, MagicMock
from exchange.binance.spot import BinanceSpot


@patch("exchange.binance.spot.BinanceSpot.get_api")
def test_buy_market(mock_get_api):
    mock_api = MagicMock()
    mock_api.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock_api

    api = BinanceSpot()
    result = api.buy_market("BTC/USDT", 0.01)

    mock_api.create_order.assert_called_with("BTC/USDT", "market", "buy", 0.01)
    assert result["status"] == "success"


@patch("exchange.binance.spot.BinanceSpot.get_api")
def test_buy_limit(mock_get_api):
    mock_api = MagicMock()
    mock_api.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock_api

    api = BinanceSpot()
    result = api.buy_limit("BTC/USDT", 0.01, 30000)

    mock_api.create_order.assert_called_with(
        "BTC/USDT", "limit", "buy", 0.01, price=30000
    )
    assert result["status"] == "success"


@patch("exchange.binance.spot.BinanceSpot.get_api")
def test_sell_market(mock_get_api):
    mock_api = MagicMock()
    mock_api.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock_api

    api = BinanceSpot()
    result = api.sell_market("BTC/USDT", 0.01)

    mock_api.create_order.assert_called_with("BTC/USDT", "market", "sell", 0.01)
    assert result["status"] == "success"


@patch("exchange.binance.spot.BinanceSpot.get_api")
def test_sell_limit(mock_get_api):
    mock_api = MagicMock()
    mock_api.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock_api

    api = BinanceSpot()
    result = api.sell_limit("BTC/USDT", 0.01, 35000)

    mock_api.create_order.assert_called_with(
        "BTC/USDT", "limit", "sell", 0.01, price=35000
    )
    assert result["status"] == "success"
