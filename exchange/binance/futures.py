from exchange.binance.api import BinanceAPI


class BinanceFutures(BinanceAPI):  # raw wrapper

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

    def set_margin_type(self, symbol: str, margin_mode: str):
        """
        Set margin type for a futures symbol
        margin_mode: 'ISOLATED' or 'CROSSED'
        """
        return self._get_api().fapiPrivate_post_marginType(
            {
                "symbol": symbol.replace("/", ""),
                "marginType": margin_mode.upper(),
            }
        )

    def set_position_mode(self, hedge: bool):
        """
        Set position mode for the entire futures account
        hedge=True  -> Hedge Mode (롱/숏 동시 보유)
        hedge=False -> One-Way Mode (단일 방향)
        """
        return self._get_api().fapiPrivate_post_positionSideDual(
            {
                "dualSidePosition": str(hedge).lower(),
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


class FuturesTrader:
    def __init__(self, api: BinanceFutures, symbol: str):
        """
        :param api: BinanceFutures instance
        :param symbol: Trading Symbol (e.g. "BTC/USDT")
        """
        self.api = api
        self.symbol = symbol

    def fetch_ohlcv(self, timeframe="1m", limit=60):
        """
        Fetch OHLCV for this symbol
        :param timeframe: "1m", "5m", "1h", "4h" . . .
        :param limit: 불러올 캔들 개수
        """
        return self.api._get_api().fetch_ohlcv(
            self.symbol, timeframe=timeframe, limit=limit
        )

    def set_margin_type(self, mode: str):
        """
        Switch margin mode for this symbol
        :param mode: "isolated" 또는 "crossed"
        """
        return self.api.set_margin_type(self.symbol, mode)

    def buy_market(self, amount: float):
        """
        Convenience method: buy long market price
        :param amount: buying amount
        """
        return self.api.buy_market(self.symbol, amount)


class BTCFutures(FuturesTrader):
    """FuturesTrader for BTC/USDT only"""

    def __init__(self, api: BinanceFutures):
        super().__init__(api, "BTC/USDT")


class ETHFutures(FuturesTrader):
    """FuturesTrader for ETH/USDT only"""

    def __init__(self, api: BinanceFutures):
        super().__init__(api, "ETH/USDT")
