import requests
import pandas as pd

BASE_URL = "https://api.binance.com/api/v3/klines"


def fetch_ohlcv(symbol, interval="5m", limit=100):
    url = BASE_URL
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params, timeout=5)
    data = response.json()

    df = pd.DataFrame(
        data,
        columns=[
            "open_time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "qav",
            "num_trades",
            "taker_base_vol",
            "taker_quote_vol",
            "ignore"
        ],
    )

    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df

