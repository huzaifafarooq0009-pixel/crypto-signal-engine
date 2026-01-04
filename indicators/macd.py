# indicators/macd.py

import pandas as pd

def calculate_macd(df: pd.DataFrame, fast_period: int = 12, slow_period: int = 26, signal_period: int = 9):
    """
    Calculate MACD line and signal line for a given DataFrame with 'close' column.
    Returns a tuple of Pandas Series: (macd_line, signal_line, macd_histogram)
    """
    # Exponential moving averages
    ema_fast = df['close'].ewm(span=fast_period, adjust=False).mean()
    ema_slow = df['close'].ewm(span=slow_period, adjust=False).mean()

    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    macd_histogram = macd_line - signal_line

    return macd_line, signal_line, macd_histogram
