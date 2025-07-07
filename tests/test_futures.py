# tests/test_futures.py
# Test for: exchange/binance/futures.py
# Description: Unit tests for BinanceFutures and FuturesTrader
from unittest.mock import patch, MagicMock
import pytest
from exchange.binance.futures import BinanceFutures, ETHFutures


@patch.object(BinanceFutures, "_get_api")
def test_raw_buy_market(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "ok"}
    mock_get_api.return_value = mock

    api = BinanceFutures()
    res = api.buy_market("ETH/USDT", 0.05)

    mock.create_order.assert_called_once_with("ETH/USDT", "market", "buy", 0.05)
    assert res["status"] == "ok"


@patch.object(BinanceFutures, "_get_api")
def test_raw_sell_market(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "ok"}
    mock_get_api.return_value = mock

    api = BinanceFutures()
    res = api.sell_market("BTC/USDT", 0.02)

    mock.create_order.assert_called_once_with("BTC/USDT", "market", "sell", 0.02)
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


@patch.object(BinanceFutures, "_get_api")
@pytest.mark.parametrize(
    "mode, symbol, expected",
    [
        ("isolated", "BTC/USDT", {"symbol": "BTCUSDT", "marginType": "ISOLATED"}),
        ("CROSSED", "ETH/USDT", {"symbol": "ETHUSDT", "marginType": "CROSSED"}),
    ],
)
def test_set_margin_type_raw(mock_get_api, mode, symbol, expected):
    mock = MagicMock()
    mock.fapiPrivate_post_marginType.return_value = {
        "marginType": expected["marginType"]
    }
    mock_get_api.return_value = mock

    api = BinanceFutures()
    res = api.set_margin_type(symbol, mode)

    mock.fapiPrivate_post_marginType.assert_called_once_with(expected)
    assert res["marginType"] == expected["marginType"]


@patch.object(BinanceFutures, "_get_api")
@pytest.mark.parametrize(
    "hedge, expected",
    [
        (True, {"dualSidePosition": "true"}),
        (False, {"dualSidePosition": "false"}),
    ],
)
def test_set_position_mode(mock_get_api, hedge, expected):
    mock = MagicMock()
    mock.fapiPrivate_post_positionSideDual.return_value = expected
    mock_get_api.return_value = mock

    api = BinanceFutures()
    res = api.set_position_mode(hedge)

    mock.fapiPrivate_post_positionSideDual.assert_called_once_with(expected)
    assert res == expected


@patch.object(BinanceFutures, "_get_api")
def test_futures_trader_buy(mock_get_api):
    mock = MagicMock()
    mock.create_order.return_value = {"status": "ok"}
    mock_get_api.return_value = mock

    api = BinanceFutures()
    eth_t = ETHFutures(api)
    res = eth_t.buy_market(0.1)

    mock.create_order.assert_called_once_with("ETH/USDT", "market", "buy", 0.1)
    assert res["status"] == "ok"
