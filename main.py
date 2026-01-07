import tkinter as tk
from config.settings import TOP_SYMBOLS, REFRESH_INTERVAL
from app.dashboard import create_dashboard, update_gui
from pipeline.scheduler import start_scheduler

def main():
    root = tk.Tk()
    root.title("Crypto Signal Engine")
    root.configure(bg="black")
    root.geometry("950x800")

    labels = create_dashboard(root, TOP_SYMBOLS)

    start_scheduler(
        root=root,
        symbols=TOP_SYMBOLS,
        labels=labels,
        update_gui=update_gui,
        interval=REFRESH_INTERVAL
    )

    root.mainloop()

if __name__ == "__main__":
    main()


