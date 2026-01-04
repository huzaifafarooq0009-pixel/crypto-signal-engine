# data/binance_client.py

import requests
import pandas as pd
from config.settings import BINANCE_KLINES_API

def fetch_klines(symbol: str, interval: str = "5m", limit: int = 100) -> pd.DataFrame:
    """
    Fetch klines (candlestick data) from Binance API for a given symbol.
    Returns a pandas DataFrame.
    """
    url = f"{BINANCE_KLINES_API}?symbol={symbol}&interval={interval}&limit={limit}"
    data = requests.get(url, timeout=5).json()

    df = pd.DataFrame(data, columns=[
        "time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])

    # Convert numeric columns to float
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df
