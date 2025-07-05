import ccxt
from exchange.binance.config import binance_instance
from exchange.abstract import AbstractAPI


class BinanceAPI(AbstractAPI):
    def __init__(self, market_type):
        if market_type not in ("spot", "future"):
            raise ValueError(f"Invalid market_type: {market_type}")

        self.api_key = binance_instance.api_key
        self.api_secret = binance_instance.api_secret
        self.market_type = market_type

        self.api = self._create_api()

    def _create_api(self):
        options = {
            "defaultType": self.market_type,
            "quoteOrderQty": True,
        }

        return ccxt.binance(
            {
                "apiKey": self.api_key,
                "secret": self.api_secret,
                "enableRateLimit": True,
                "adjustForTimeDifference": True,
                "verbose": False,  # HTTP log
                "options": options,
            }
        )

    @classmethod
    def binance_spot(cls):
        return cls("spot").get_api()

    @classmethod
    def binance_futures(cls):
        return cls("future").get_api()

    def get_api(self):
        return self.api

    def fetch_ticker(self, symbol: str):
        return self.get_api().fetch_ticker(symbol)

    def create_order(self, symbol: str, order_type: str, side: str, amount: float):
        return self.get_api().create_order(symbol, order_type, side, amount)

    def fetch_balance(self):
        return self.get_api().fetch_balance()
