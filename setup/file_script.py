import os

folders = [
    "exchange/binance",
    "strategies",
    "tests",
    "utils",
]

files = {
    "exchange/__init__.py": "",
    "exchange/binance/__init__.py": "",
    "exchange/binance/binance.py": "",
    "exchange/binance/config.py": "",
    "exchange/binance/abstract.py": "",
    "exchange/binance/backtest.py": "",
    "exchange/binance/" "strategies/__init__.py": "",
    "strategies/futures_trading.py": "",
    "strategies/spot_trading.py": "",
    ".gitignore": "",
    ".env": "",
    "Dockerfile": "",
    ".dockerignore": "",
    "requirements.txt": "",
}


def run():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for path, content in files.items():
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

    print("successful")


if __name__ == "__main__":
    run()
