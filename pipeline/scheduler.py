import threading
import winsound
from services.binance_api import fetch_and_analyze
from alerts.notifier import show_popup

def start_scheduler(root, symbols, labels, update_gui, interval):
    def loop():
        for sym in symbols:
            threading.Thread(
                target=process_symbol,
                args=(root, sym, labels, update_gui),
                daemon=True
            ).start()

        root.after(interval, loop)

    loop()

def process_symbol(root, symbol, labels, update_gui):
    data = fetch_and_analyze(symbol)

    decision = "HOLD"
    color = "white"

    if 30 <= data['rsi'] < 40 and data['macd'] > data['signal_line'] and data['hist'] > 0:
        decision = "LONG"
        color = "green"
        root.after(0, show_popup, root, symbol, decision)

    elif 60 < data['rsi'] <= 70 and data['macd'] < data['signal_line'] and data['hist'] < 0:
        decision = "SHORT"
        color = "red"
        root.after(0, show_popup, root, symbol, decision)

    root.after(0, update_gui, labels, symbol, data, decision, color)




