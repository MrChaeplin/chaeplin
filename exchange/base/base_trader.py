from exchange.base.abstract_trader import AbstractTrader


class BaseTrader(AbstractTrader):
    def __init__(self, api, symbol):
        self.api = api
        self.symbol = symbol

    def fetch_ohlcv(self, timeframe="1m", limit=60):
        return self.api.fetch_ohlcv(self.symbol, timeframe, limit)

    def get_position(self):
        return self.api.get_position(self.symbol)

    def get_order_history(self):
        return self.api.get_order_history(self.symbol)

    def get_balance(self):
        return self.api.get_wallet_balance()

    def buy_market(self, amount):
        return self.api.buy_market(self.symbol, amount)

    def sell_market(self, amount):
        return self.api.sell_market(self.symbol, amount)

    def buy_limit(self, amount, price):
        return self.api.buy_limit(self.symbol, amount, price)

    def sell_limit(self, amount, price):
        return self.api.sell_limit(self.symbol, amount, price)

    def stop_loss_market(self, amount, price):
        return self.api.stop_loss_market(self.symbol, amount, price)

    def close_position_market(self, side, amount):
        return self.api.close_position_market(self.symbol, side, amount)

    def take_profit(self, amount, price):
        return self.api.take_profit_market(self.symbol, amount, price)
