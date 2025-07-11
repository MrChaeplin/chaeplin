from abc import ABC, abstractmethod


class AbstractAPI(ABC):

    @abstractmethod
    def fetch_ticker(self, symbol: str):
        pass

    @abstractmethod
    def create_order(
        self,
        symbol: str,
        order_type: str,
        side: str,
        amount: float,
        price: float = None,
        params: dict = None,
    ):
        pass

    @abstractmethod
    def fetch_balance(self):
        pass

    def cancel_order(self, order_id: str, symbol: str = None):
        pass
