from exchange.binance.api import BinanceAPI


class BinanceFutures(BinanceAPI):
    def __init__(self):
        super().__init__("future")

    def set_leverage(self, symbol, leverage):
        """Set leverage for symbol // 레버리지 설정"""
        return self._get_api().fapiprivate_post_leverage(
            {
                "symbol": symbol.replace("/", ""),
                "leverage": leverage,
            }
        )

    def get_wallet_balance(self):
        """Get futures account wallet balance // 선물 계정 잔고 조회"""
        return self._get_api().fetch_balance()

    def close_position_market(self, symbol, side, amount):
        return self._get_api().create_order(symbol, "market", side, amount)

    def get_account_info(self):
        """Get full account info // 전체 계정 정보 조회"""
        return self._get_api().fapiprivate_get_account()

    def get_order_history(self, symbol):
        """Get all order history for a symbol // 종목별 주문 조회"""
        return self._get_api().fapiprivate_get_allorders(
            {"symbol": symbol.replace("/", "")}
        )

    def get_position(self, symbol):
        """Get current position info for a symbol // 종목별 포지션 조회"""
        return self._get_api().fapiprivate_get_positionrisk(
            params={"symbol": symbol.replace("/", "")}
        )

    def buy_market(self, symbol, amount):
        """Long position at market price // 시장가 롱 진입"""
        return self._get_api().create_order(symbol, "market", "buy", amount)

    def buy_limit(self, symbol, amount, price):
        """Long position at limit price // 지정가 롱 진입"""
        return self._get_api().create_order(symbol, "limit", "buy", amount, price=price)

    def sell_market(self, symbol, amount):
        """Short position at market price // 시장가 숏 진입"""
        return self._get_api().create_order(symbol, "market", "sell", amount)

    def sell_limit(self, symbol, amount, price):
        """Short position at limit price // 지정가 숏 진입"""
        return self._get_api().create_order(
            symbol, "limit", "sell", amount, price=price
        )

    def stop_loss_market(self, symbol, amount, price):
        """Stop loss order at market price // 시장가 스탑로스"""
        return self._get_api().create_order(
            symbol, "stop_market", "sell", amount, price=price
        )

    def take_profit(self):
        """Take profit order (Not implemented) // 익절 주문 (미구현)"""
        pass
