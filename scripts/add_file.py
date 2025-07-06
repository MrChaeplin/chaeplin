import os

folders = [
    "backtesting",
    "backtesting/data",
    "cli",
    "exchange",
    "exchange/binance",
    "logs",
    "passed_strategies",
    "risk",
    "scripts",
    "strategies/futures",
    "strategies/spot",
    "tests",
    "tests/logs",
    "utils",
]

files = {
    # backtesting
    "backtesting/__init__.py": "",
    "backtesting/data_handler.py": "# TODO: implement data loading & saving logic\n",
    "backtesting/engine.py": "# TODO: implement backtesting engine\n",
    # CLI
    "cli/__init__.py": "",
    "cli/main.py": (
        "#!/usr/bin/env python3\n"
        "# CLI entrypoint (to be implemented)\n\n"
        "def main():\n"
        "    pass\n\n"
        "if __name__ == '__main__':\n"
        "    main()\n"
    ),
    # exchange/binance
    "exchange/__init__.py": "",
    "exchange/binance/__init__.py": "",
    "exchange/binance/api.py": "# TODO: implement BinanceAPI subclass\n",
    "exchange/binance/config.py": (
        "# Loads API keys from .env and exposes them via a singleton\n"
    ),
    "exchange/binance/futures.py": "# TODO: implement BinanceFutures methods\n",
    "exchange/binance/spot.py": "# TODO: implement BinanceSpot methods\n",
    "exchange/binance/symbols.py": "# TODO: implement SymbolTrader, BTC, ETH classes\n",
    "exchange/binance/ws_listener.py": "# TODO: implement WebSocket listener for live data\n",
    # logs (keep the folder in git via .gitkeep)
    "logs/.gitkeep": "",
    # passed_strategies
    "passed_strategies/__init__.py": "",
    # rist (manager module)
    "rist/__init__.py": "",
    "rist/manager.py": "# TODO: implement strategy manager\n",
    # scripts
    "scripts/add_file.py": "",  # this file itself
    "scripts/save_data.py": "# TODO: script to fetch and save OHLCV data\n",
    # strategies
    "strategies/futures/__init__.py": "",
    "strategies/futures/strategy.py": "# TODO: implement futures strategy\n",
    "strategies/spot/__init__.py": "",
    "strategies/spot/strategy.py": "# TODO: implement spot strategy\n",
    # tests
    "tests/__init__.py": "",
    "tests/conftest.py": "# TODO: add pytest fixtures\n",
    "tests/test_api.py": "# TODO: unit tests for BinanceAPI\n",
    "tests/test_config.py": "# TODO: unit tests for config loader\n",
    "tests/test_futures.py": "# TODO: unit tests for BinanceFutures\n",
    "tests/test_spot.py": "# TODO: unit tests for BinanceSpot\n",
    "tests/logs/.gitkeep": "",
    # utils
    "utils/__init__.py": "",
    "utils/file_utils.py": "# TODO: implement file utilities\n",
    "utils/logger.py": "# TODO: implement logging setup\n",
    "utils/time_utils.py": "# TODO: implement time helper functions\n",
}


def run():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for path, content in files.items():
        dirpath = os.path.dirname(path)

        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)

        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

    print("successful")


if __name__ == "__main__":
    run()
