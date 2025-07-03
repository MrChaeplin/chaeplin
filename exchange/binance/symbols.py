from .binance import BinanceAPI


class SymbolTrader:
    def __init__(self, api: BinanceAPI, symbol: str):
        self.api = api
        self.symbol = symbol


class BTC(SymbolTrader):
    def __init__(self, api):
        super().__init__(api, "BTC/USDT")


class ETH(SymbolTrader):
    def __init__(self, api):
        super().__init__(api, "ETH/USDT")
