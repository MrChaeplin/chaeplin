# tests/test_spot.py
# Test for: exchange/binance/spot.py
# Description: Unit tests for BinanceSpot and SpotTrader
from unittest.mock import patch, MagicMock
import pytest
from exchange.binance.spot import BinanceSpot, SpotTrader, BTCSpot


@patch.object(BinanceSpot, "_get_api")
def test_raw_buy_market(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock

    api = BinanceSpot()
    res = api.buy_market("BTC/USDT", 0.01)

    mock.create_order.assert_called_once_with("BTC/USDT", "market", "buy", 0.01)
    assert res["status"] == "success"


@patch.object(BinanceSpot, "_get_api")
def test_raw_buy_limit(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock

    api = BinanceSpot()
    res = api.buy_limit("BTC/USDT", 0.01, price=30000)

    mock.create_order.assert_called_once_with(
        "BTC/USDT", "limit", "buy", 0.01, price=30000
    )
    assert res["status"] == "success"


@patch.object(BinanceSpot, "_get_api")
def test_raw_sell_market(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock

    api = BinanceSpot()
    res = api.sell_market("BTC/USDT", 0.01)

    mock.create_order.assert_called_once_with("BTC/USDT", "market", "sell", 0.01)
    assert res["status"] == "success"


@patch.object(BinanceSpot, "_get_api")
def test_raw_sell_limit(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "success"}
    mock_get_api.return_value = mock

    api = BinanceSpot()
    res = api.sell_limit("BTC/USDT", 0.01, price=35000)

    mock.create_order.assert_called_once_with(
        "BTC/USDT", "limit", "sell", 0.01, price=35000
    )
    assert res["status"] == "success"


@patch.object(BinanceSpot, "_get_api")
def test_spot_trader_fetch_ohlcv(mock_get_api):
    mock = MagicMock()
    mock.fetch_ohlcv.return_value = [[1, 2, 3, 4, 5, 6]]
    mock_get_api.return_value = mock

    api = BinanceSpot()
    btc_tr = BTCSpot(api)
    data = btc_tr.fetch_ohlcv("5m", limit=1)

    mock.fetch_ohlcv.assert_called_once_with("BTC/USDT", timeframe="5m", limit=1)
    assert data == [[1, 2, 3, 4, 5, 6]]


@patch.object(BinanceSpot, "_get_api")
def test_spot_trader_delegation(mock_get_api):
    mock = MagicMock()
    mock.fetch_ohlcv.return_value = [[0, 1, 2, 3, 4, 5]]
    mock_get_api.return_value = mock

    api = BinanceSpot()
    spot_t = SpotTrader(api, "ETH/USDT")
    data = spot_t.fetch_ohlcv("1h", limit=1)

    mock.fetch_ohlcv.assert_called_once_with("ETH/USDT", timeframe="1h", limit=1)
    assert data == [[0, 1, 2, 3, 4, 5]]
