import tkinter as tk

def create_dashboard(root, symbols):
    labels = {}

    # Heading at the top
    heading = tk.Label(
        root,
        text="🔵 Live Crypto Signals (5m Interval)",
        font=("Segoe UI", 28, "bold"),
        fg="#00BFFF",  # Ocean blue
        bg="black"
    )
    heading.pack(pady=20)

    # Canvas + Scrollbar
    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Frame inside canvas
    frame = tk.Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Update scroll region automatically
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame.bind("<Configure>", on_frame_configure)

    # Column headers (optional, like a table)
    headers = ["Symbol", "Signal", "Price", "RSI", "MACD", "Volume"]
    header_text = " | ".join(headers)
    header_label = tk.Label(
        frame,
        text=header_text,
        font=("Segoe UI", 15, "bold"),
        fg="#00BFFF",
        bg="black",
        anchor="w"
    )
    header_label.pack(pady=(0, 10), fill="x")

    # Labels for each symbol
    for sym in symbols:
        lbl = tk.Label(
            frame,
            text=f"{sym} → WAITING | Price: -- | RSI: -- | MACD: -- | Vol: --",
            font=("Segoe UI", 10, "bold"),
            fg="#00BFFF",
            bg="black",
            anchor="w"  # Align from left
        )
        lbl.pack(pady=6, fill="x")
        labels[sym] = lbl

    return labels

def update_gui(labels, symbol, data, decision, color="#00BFFF"):
    """
    Updates the label of a given symbol with new signal & values.
    """
    text = f"{symbol:<8} → {decision:<5} | Price: ${data['price']:<10.2f} | RSI: {data['rsi']:<5.1f} | MACD: {data['macd']:<6.2f} | Vol: {data['volume']:<10.1f}"
    labels[symbol].config(
        text=text,
        fg=color
    )






