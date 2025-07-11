from unittest.mock import patch, MagicMock
import pytest
from exchange.binance.futures import BinanceFutures


@patch.object(BinanceFutures, "_get_api")
def test_raw_buy_market(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "ok"}
    mock_get_api.return_value = mock

    api = BinanceFutures()
    res = api.buy_market("ETH/USDT", 0.05)

    mock.create_order.assert_called_once_with(
        "ETH/USDT", "market", "buy", 0.05, params=None
    )
    assert res["status"] == "ok"


@patch.object(BinanceFutures, "_get_api")
def test_raw_sell_market(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "ok"}
    mock_get_api.return_value = mock

    api = BinanceFutures()
    res = api.sell_market("BTC/USDT", 0.02)

    mock.create_order.assert_called_once_with(
        "BTC/USDT", "market", "sell", 0.02, params=None
    )
    assert res["status"] == "ok"


@patch.object(BinanceFutures, "_get_api")
def test_set_leverage(mock_get_api):
    mock = MagicMock()
    mock.fapiprivate_post_leverage.return_value = {"leverage": 10}
    mock_get_api.return_value = mock

    api = BinanceFutures()
    res = api.set_leverage("BTC/USDT", 10)

    mock.fapiprivate_post_leverage.assert_called_once_with(
        {"symbol": "BTCUSDT", "leverage": 10}
    )
    assert res["leverage"] == 10
