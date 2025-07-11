import ccxt
from exchange.binance.config import binance_instance
from exchange.base.abstract_api import AbstractAPI


class BinanceAPI(AbstractAPI):
    def __init__(self, market_type):
        if market_type not in ("spot", "future"):
            raise ValueError(f"Invalid market_type: {market_type}")

        self.__api_key = binance_instance.get_api_key()
        self.__api_secret = binance_instance.get_api_secret()
        self.market_type = market_type

        self._api = self._create_api()

    def _create_api(self):
        options = {
            "defaultType": self.market_type,
            "quoteOrderQty": True,
        }

        return ccxt.binance(
            {
                "apiKey": self.__api_key,
                "secret": self.__api_secret,
                "enableRateLimit": True,
                "adjustForTimeDifference": True,
                "verbose": False,  # HTTP log
                "options": options,
            }
        )

    @classmethod
    def binance_spot(cls):
        return cls("spot")._get_api()

    @classmethod
    def binance_futures(cls):
        return cls("future")._get_api()

    def _get_api(self):
        return self._api

    def fetch_ticker(self, symbol: str):
        return self._get_api().fetch_ticker(symbol)

    def create_order(
        self,
        symbol: str,
        order_type: str,
        side: str,
        amount: float,
        price: float = None,
        params: dict = None,
    ):
        return self._get_api().create_order(
            symbol, order_type, side, amount, price=price, params=params
        )

    def fetch_balance(self):
        return self._get_api().fetch_balance()

    def cancel_order(self, order_id: str, symbol: str = None):
        return self._get_api().cancel_order(order_id, symbol)
