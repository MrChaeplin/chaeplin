from exchange.binance.api import BinanceAPI
from exchange.base.base_trader import BaseTrader
from utils import errors
import ccxt
import logging


logger = logging.getLogger(__name__)


class BinanceFutures(BinanceAPI):  # raw wrapper

    def __init__(self):
        super().__init__("future")

    def fetch_ohlcv(self, symbol: str, timeframe="1m", limit=60):
        """Fetch OHLCV data for a futures symbol"""
        return self._get_api().fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

    def get_position(self, symbol: str):
        """Get current position info for a symbol"""
        return self._get_api().fapiPrivateGetPositionRisk(
            params={"symbol": symbol.replace("/", "")}
        )

    def get_wallet_balance(self):
        """Get futures account wallet balance"""
        return self._get_api().fetch_balance()

    def get_order_history(self, symbol: str):
        """Get all order history for a symbol"""
        return self._get_api().fapiPrivateGetAllOrders(
            {"symbol": symbol.replace("/", "")}
        )

    def set_leverage(self, symbol: str, leverage: int):
        """Set leverage for symbol // 레버리지 설정"""
        try:
            return self._get_api().fapiprivate_post_leverage(
                {
                    "symbol": symbol.replace("/", ""),
                    "leverage": leverage,
                }
            )
        except ccxt.BaseError as e:
            logger.error(f"[Leverage Error] symbol={symbol} leverage={leverage} → {e}")
            raise

    def set_margin_type(self, symbol: str, margin_mode: str):
        """Set margin type: 'ISOLATED' or 'CROSSED'"""
        try:
            return self._get_api().fapiPrivate_post_marginType(
                {
                    "symbol": symbol.replace("/", ""),
                    "marginType": margin_mode.upper(),
                }
            )
        except ccxt.BaseError as e:
            logger.error(
                f"[Margin Error] symbol={symbol} marginType={margin_mode} → {e}"
            )
            raise

    def set_position_mode(self, hedge: bool):
        """
        Set position mode for the entire futures account
        hedge=True  -> Hedge Mode (롱/숏 동시 보유)
        hedge=False -> One-Way Mode (단일 방향)
        """
        try:
            return self._get_api().fapiPrivate_post_positionSideDual(
                {
                    "dualSidePosition": str(hedge).lower(),
                }
            )
        except ccxt.BaseError as e:
            logger.error(f"[Margin Type Error] hedge={hedge} → {e}")
            raise

    def close_position_market(self, symbol: str, side: str, amount: float):
        """Close position at market price"""
        return errors.safe_create_order(self._get_api(), symbol, "market", side, amount)

    def buy_market(self, symbol: str, amount: float):
        """Long position at market price // 시장가 롱 진입"""
        return errors.safe_create_order(
            self._get_api(), symbol, "market", "buy", amount
        )

    def buy_limit(self, symbol: str, amount: float, price: float):
        """Long position at limit price // 지정가 롱 진입"""
        return errors.safe_create_order(
            self._get_api(), symbol, "limit", "buy", amount, price=price
        )

    def sell_market(self, symbol: str, amount: float):
        """Short position at market price // 시장가 숏 진입"""
        return errors.safe_create_order(
            self._get_api(), symbol, "market", "sell", amount
        )

    def sell_limit(self, symbol: str, amount: float, price: float):
        """Short position at limit price // 지정가 숏 진입"""
        return errors.safe_create_order(
            self._get_api(), symbol, "limit", "sell", amount, price=price
        )

    def stop_loss_market(self, symbol: str, amount: float, price: float):
        """Stop loss order at market price"""
        params = {
            "stopPrice": price,
            "reduceOnly": True,
            "closePosition": False,
        }
        return errors.safe_create_order(
            self._get_api(),
            symbol=symbol,
            order_type="stop_market",
            side="sell",
            amount=amount,
            price=price,
            params=params,
        )

    def take_profit(self, symbol: str, amount: float, price: float):
        """Take profit order at limit price // 익절 주문"""
        params = {
            "stopPrice": price,
            "reduceOnly": True,
            "closePosition": False,
        }
        return errors.safe_create_order(
            self._get_api(),
            symbol=symbol,
            order_type="take_profit_market",
            side="sell",
            amount=amount,
            price=price,
            params=params,
        )


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class FuturesTrader(BaseTrader):
    """Convenience wrapper for a single futures symbol"""

    def __init__(self, api: BinanceFutures, symbol: str):
        super().__init__(api, symbol)

    def set_leverage(self, leverage: int):
        return self.api.set_leverage(self.symbol, leverage)

    def set_margin_type(self, mode: str):
        return self.api.set_margin_type(self.symbol, mode)

    def set_position_mode(self, hedge: bool):
        return self.api.set_position_mode(hedge)
