from dotenv import load_dotenv
import os
from pathlib import Path


def load_binance_config():
    env_path = Path(__file__).parents[2] / ".env"
    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError('Values Error: Check your ".env" file')
    return api_key, api_secret


class Binance:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Binance, cls).__new__(cls)
            try:
                api_key, api_secret = load_binance_config()
                cls._instance.__api_key = api_key
                cls._instance.__api_secret = api_secret

            except ValueError as e:
                raise ValueError(f"Binance failed: {e}")
        return cls._instance

    def get_api_key(self):
        return self.__api_key

    def get_api_secret(self):
        return self.__api_secret


binance_instance = Binance()
