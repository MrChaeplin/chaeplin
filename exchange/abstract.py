from abc import ABC, abstractmethod


class AbstractAPI(ABC):

    @abstractmethod
    def fetch_ticker(self, symbol: str):
        pass

    @abstractmethod
    def create_order(self, symbol: str, order_type: str, side: str, amount: float):
        pass

    @abstractmethod
    def fetch_balance(self):
        pass
