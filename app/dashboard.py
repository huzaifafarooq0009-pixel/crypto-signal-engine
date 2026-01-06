import tkinter as tk


class Dashboard:
    def __init__(self, root, symbols):
        self.root = root
        self.symbols = symbols
        self.labels = {}

        root.title("Live Crypto Signal Engine")
        root.geometry("950x800")
        root.configure(bg="black")

        title = tk.Label(
            root,
            text="🔵 Live Crypto Signals (5m)",
            font=("Courier", 16, "bold"),
            fg="cyan",
            bg="black"
        )
        title.pack(pady=10)

        container = tk.Frame(root, bg="black")
        container.pack(fill="both", expand=True)

        headers = ["Symbol", "Price", "RSI", "MACD", "Volume", "Signal"]
        widths = [12, 14, 12, 14, 14, 14]

        header_row = tk.Frame(container, bg="black")
        header_row.pack()

        for i, h in enumerate(headers):
            tk.Label(
                header_row,
                text=h,
                font=("Courier", 12, "bold"),
                fg="cyan",
                bg="black",
                width=widths[i]
            ).grid(row=0, column=i)

        for symbol in symbols:
            row = tk.Frame(container, bg="black")
            row.pack()

            self.labels[symbol] = {}

            for i, col in enumerate(headers):
                lbl = tk.Label(
                    row,
                    text="Loading...",
                    font=("Courier", 11),
                    fg="white",
                    bg="black",
                    width=widths[i]
                )
                lbl.grid(row=0, column=i)
                self.labels[symbol][col] = lbl

    def update_ui(self, symbol, price, rsi, macd, volume, decision):
        if symbol not in self.labels:
            return

        self.labels[symbol]["Price"].config(text=f"${price:,.2f}")
        self.labels[symbol]["RSI"].config(text=f"{rsi:.1f}")
        self.labels[symbol]["MACD"].config(text=f"{macd:.2f}")
        self.labels[symbol]["Volume"].config(text=f"{volume:,.1f}")

        color = "green" if decision == "LONG" else "red" if decision == "SHORT" else "white"
        self.labels[symbol]["Signal"].config(text=decision, fg=color)
