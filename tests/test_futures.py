# Test for: exchange/binance/futures.py
# Description: Unit tests for BinanceFutures (market order, leverage)
from unittest.mock import patch, MagicMock
from exchange.binance.futures import BinanceFutures


@patch("exchange.binance.futures.BinanceFutures._get_api")
def test_long_market(mock_get_api):
    mock_api = MagicMock()
    mock_api.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock_api

    api = BinanceFutures()
    result = api.buy_market("BTC/USDT", 0.01)

    assert result["status"] == "success"
    mock_api.create_order.assert_called_with("BTC/USDT", "market", "buy", 0.01)


@patch("exchange.binance.futures.BinanceFutures._get_api")
def test_sell_market(mock_get_api):
    mock_api = MagicMock()
    mock_api.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock_api

    api = BinanceFutures()
    result = api.sell_market("BTC/USDT", 0.02)
    assert result["status"] == "success"
    mock_api.create_order.assert_called_with("BTC/USDT", "market", "sell", 0.02)


@patch("exchange.binance.futures.BinanceFutures._get_api")
def test_set_leverage(mock_get_api):
    mock_api = MagicMock()
    mock_api.fapiprivate_post_leverage.return_value = {"leverage": 10}
    mock_get_api.return_value = mock_api

    api = BinanceFutures()
    result = api.set_leverage("BTC/USDT", 10)

    mock_api.fapiprivate_post_leverage.assert_called_with(
        {"symbol": "BTCUSDT", "leverage": 10}
    )
    assert result["leverage"] == 10
