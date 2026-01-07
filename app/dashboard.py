import tkinter as tk

def create_dashboard(root, symbols):
    labels = {}

    headers = ["Symbol", "Price", "RSI", "MACD", "Volume", "Signal"]
    frame = tk.Frame(root, bg="black")
    frame.pack(fill="both", expand=True)

    for col, h in enumerate(headers):
        tk.Label(frame, text=h, fg="cyan", bg="black",
                 font=("Courier", 12, "bold")).grid(row=0, column=col)

    for row, sym in enumerate(symbols, start=1):
        labels[sym] = {}
        for col, h in enumerate(headers):
            lbl = tk.Label(frame, text="Loading...", fg="white", bg="black")
            lbl.grid(row=row, column=col)
            labels[sym][h] = lbl

    return labels

def update_gui(labels, symbol, data, decision, color):
    labels[symbol]["Price"].config(text=f"${data['price']:.2f}")
    labels[symbol]["RSI"].config(text=f"{data['rsi']:.1f}")
    labels[symbol]["MACD"].config(text=f"{data['macd']:.2f}")
    labels[symbol]["Volume"].config(text=f"{data['volume']:.1f}")
    labels[symbol]["Signal"].config(text=decision, fg=color)


