from abc import ABC, abstractmethod


class AbstractTrader(ABC):
    def __init__(self, api, symbol: str):
        self.api = api
        self.symbol = symbol

    @abstractmethod
    def fetch_ohlcv(self, timeframe="1m", limit=60):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def get_order_history(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def buy_market(self, amount: float):
        pass

    @abstractmethod
    def buy_limit(self, amount: float, price: float):
        pass

    @abstractmethod
    def sell_market(self, amount: float):
        pass

    @abstractmethod
    def sell_limit(self, amount: float, price: float):
        pass

    @abstractmethod
    def stop_loss_market(self, amount: float, price: float):
        pass

    @abstractmethod
    def close_position_market(self, side: str, amount: float):
        pass

    @abstractmethod
    def take_profit(self, amount: float, price: float):
        pass
