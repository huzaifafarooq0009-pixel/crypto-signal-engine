import tkinter as tk
import winsound


def show_signal_popup(root, symbol, signal):
    popup = tk.Toplevel(root)
    popup.configure(bg="black")
    popup.geometry("260x120+600+300")

    color = "green" if signal == "LONG" else "red"
    text = f"{symbol} → {signal}"

    label = tk.Label(
        popup,
        text=text,
        font=("Courier", 16, "bold"),
        fg=color,
        bg="black"
    )
    label.pack(expand=True)

    winsound.Beep(1000, 300)
    winsound.Beep(1300, 300)

    popup.after(5000, popup.destroy)
