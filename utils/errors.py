import ccxt
import logging
from ccxt.base.exchange import Exchange

logger = logging.getLogger(__name__)


def safe_create_order(
    api: Exchange, symbol, order_type, side, amount, price=None, params=None
):
    try:
        if order_type == "limit" and price is not None:
            return api.create_order(
                symbol, order_type, side, amount, price=price, params=params
            )
        elif price is not None:
            return api.create_order(
                symbol, order_type, side, amount, price=price, params=params
            )
        else:
            return api.create_order(symbol, order_type, side, amount, params=params)

    except ccxt.InsufficientFunds as e:
        logger.error(f"Insufficient balance: {e}")
        raise

    except ccxt.AuthenticationError as e:
        logger.critical(
            "API key authentication failed: .env file or environment variables need to be checked"
        )
        raise

    except ccxt.NetworkError as e:
        logger.warning(f"Network error: {e}")
        raise

    except ccxt.InvalidOrder as e:
        logger.error(f"Invalid order: {e}")
        raise

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        raise
