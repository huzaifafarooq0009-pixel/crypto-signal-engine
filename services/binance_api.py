import requests
import pandas as pd
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd

def fetch_and_analyze(symbol):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=5m&limit=100"
    data = requests.get(url, timeout=5).json()

    df = pd.DataFrame(
        data,
        columns=['time','open','high','low','close','volume',
                 'ct','qav','trades','tb','tq','ignore']
    )

    df['close'] = df['close'].astype(float)
    df['volume'] = df['volume'].astype(float)

    rsi = calculate_rsi(df)
    macd, signal, hist = calculate_macd(df)

    return {
        "price": df['close'].iloc[-1],
        "volume": df['volume'].iloc[-1],
        "rsi": rsi.iloc[-1],
        "macd": macd.iloc[-1],
        "signal_line": signal.iloc[-1],
        "hist": hist.iloc[-1]
    }
