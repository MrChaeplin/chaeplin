from exchange.binance.api import BinanceAPI


class BinanceSpot(BinanceAPI):  # raw wrapper
    def __init__(self):
        super().__init__("spot")

    def get_wallet_balance(self):
        """Fetch spot wallet balance"""
        return self._get_api().fetch_balance()

    def buy_market(self, symbol, amount):
        """Buy at market price // 시장가 매수"""
        return self._get_api().create_order(symbol, "market", "buy", amount)

    def buy_limit(self, symbol, amount, price):
        """Buy position at limit price // 지정가 매수"""
        return self._get_api().create_order(symbol, "limit", "buy", amount, price=price)

    def sell_market(self, symbol, amount):
        """Sell position at market price // 시장가 매도"""
        return self._get_api().create_order(symbol, "market", "sell", amount)

    def sell_limit(self, symbol, amount, price):
        """Sell position at limit price // 지정가 매도"""
        return self._get_api().create_order(
            symbol, "limit", "sell", amount, price=price
        )


class SpotTrader:
    def __init__(self, api: BinanceSpot, symbol: str):
        self.api = api
        self.symbol = symbol

    def fetch_ohlcv(self, timeframe="1m", limit=60):
        return self.api._get_api().fetch_ohlcv(
            self.symbol, timeframe=timeframe, limit=limit
        )


class BTCSpot(SpotTrader):
    """SpotTrader for BTC/USDT only"""

    def __init__(self, api: BinanceSpot):
        super().__init__(api, "BTC/USDT")


class ETHSpot(SpotTrader):
    """SpotTrader for ETH/USDT only"""

    def __init__(self, api: BinanceSpot):
        super().__init__(api, "ETH/USDT")
