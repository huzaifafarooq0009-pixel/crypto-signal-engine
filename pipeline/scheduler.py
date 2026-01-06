import threading
import time

from data.binance_client import fetch_klines
from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd
from strategy.momentum import decide_signal
from alerts.notifier import show_signal_popup


def process_symbol(root, symbol, update_ui):
    df = fetch_klines(symbol)

    if df is None or len(df) < 30:
        return

    rsi = calculate_rsi(df)
    macd, signal_line, hist = calculate_macd(df)

    decision = decide_signal(rsi, macd, signal_line, hist)

    price = df["close"].iloc[-1]
    volume = df["volume"].iloc[-1]

    update_ui(symbol, price, rsi, macd, volume, decision)

    if decision in ["LONG", "SHORT"]:
        root.after(0, show_signal_popup, root, symbol, decision)


def start_scheduler(root, symbols, update_ui, interval):
    def loop():
        while True:
            for symbol in symbols:
                threading.Thread(
                    target=process_symbol,
                    args=(root, symbol, update_ui),
                    daemon=True
                ).start()

            time.sleep(interval)

    threading.Thread(target=loop, daemon=True).start()
