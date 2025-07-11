from unittest.mock import patch, MagicMock
import pytest
from exchange.binance.spot import BinanceSpot


@patch.object(BinanceSpot, "_get_api")
def test_raw_buy_market(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock

    api = BinanceSpot()
    res = api.buy_market("BTC/USDT", 0.01)

    mock.create_order.assert_called_once_with(
        "BTC/USDT", "market", "buy", 0.01, params=None
    )
    assert res["status"] == "success"


@patch.object(BinanceSpot, "_get_api")
def test_raw_buy_limit(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock

    api = BinanceSpot()
    res = api.buy_limit("BTC/USDT", 0.01, price=30000)

    mock.create_order.assert_called_once_with(
        "BTC/USDT", "limit", "buy", 0.01, price=30000, params=None
    )
    assert res["status"] == "success"


@patch.object(BinanceSpot, "_get_api")
def test_raw_sell_market(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock

    api = BinanceSpot()
    res = api.sell_market("BTC/USDT", 0.01)

    mock.create_order.assert_called_once_with(
        "BTC/USDT", "market", "sell", 0.01, params=None
    )
    assert res["status"] == "success"


@patch.object(BinanceSpot, "_get_api")
def test_raw_sell_limit(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock

    api = BinanceSpot()
    res = api.sell_limit("BTC/USDT", 0.01, price=35000)

    mock.create_order.assert_called_once_with(
        "BTC/USDT", "limit", "sell", 0.01, price=35000, params=None
    )
    assert res["status"] == "success"
