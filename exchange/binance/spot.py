from exchange.binance.api import BinanceAPI
from utils import errors
from exchange.base.base_trader import BaseTrader


class BinanceSpot(BinanceAPI):  # raw wrapper
    def __init__(self):
        super().__init__("spot")

    def fetch_ohlcv(self, symbol: str, timeframe="1m", limit=60):
        return self._get_api().fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

    def get_wallet_balance(self):
        """Fetch spot wallet balance"""
        return self._get_api().fetch_balance()

    def get_order_history(self, symbol: str):
        return self._get_api().private_get_allorders(
            {"symbol": symbol.replace("/", "")}
        )

    def buy_market(self, symbol: str, amount: float):
        """Buy at market price // 시장가 매수"""
        return errors.safe_create_order(
            self._get_api(), symbol, "market", "buy", amount
        )

    def buy_limit(self, symbol: str, amount: float, price: float):
        """Buy position at limit price // 지정가 매수"""
        return errors.safe_create_order(
            self._get_api(), symbol, "limit", "buy", amount, price=price
        )

    def sell_market(self, symbol: str, amount: float):
        """Sell position at market price // 시장가 매도"""
        return errors.safe_create_order(
            self._get_api(), symbol, "market", "sell", amount
        )

    def sell_limit(self, symbol: str, amount: float, price: float):
        """Sell position at limit price // 지정가 매도"""
        return errors.safe_create_order(
            self._get_api(), symbol, "limit", "sell", amount, price=price
        )


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class SpotTrader(BaseTrader):

    def __init__(self, api: BinanceSpot, symbol: str):
        super().__init__(api, symbol)
