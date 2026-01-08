# Crypto Signal Engine

Live Cryptocurrency Signal Dashboard with Real-Time Indicators and Alerts

A Python-based real-time crypto signal engine that fetches live market data from Binance, calculates key technical indicators (RSI, MACD), generates trading signals (LONG/SHORT/HOLD), and displays them on a professional, scrollable dashboard with audio/visual alerts.

Key Features

Real-Time Data Ingestion: Fetches live candlestick data from Binance API for top 100 USDT trading pairs.

Technical Analysis Indicators:

RSI (Relative Strength Index) – identifies overbought/oversold conditions.

MACD (Moving Average Convergence Divergence) – identifies trend strength and reversals.

Trading Signals: Generates LONG, SHORT, and HOLD signals based on combined RSI & MACD strategy.

Interactive GUI Dashboard:

Scrollable, responsive display of symbols, prices, indicators, and signals.

Ocean-blue theme with professional typography.

Header row for clear data visualization.

Alerts & Notifications: Pop-up windows and beep sounds for signal changes.

Multi-Threaded Pipeline: Handles all symbols concurrently with threading to ensure real-time performance.

Extensible & Modular: Project structured into modules for data ingestion, indicators, strategy, alerts, GUI, and pipeline, allowing easy extension and maintenance.

Project Structure
crypto-signal-engine/
│
├── main.py                 # Entry point to start engine and GUI
├── requirements.txt        # Project dependencies
├── README.md
│
├── config/
│   └── settings.py         # Symbols, API URLs, refresh intervals
│
├── app/
│   └── dashboard.py        # GUI creation and label updates
│
├── indicators/
│   ├── rsi.py
│   └── macd.py             # Indicator calculations
│
├── services/
│   └── binance_api.py      # Data fetching from Binance API
│
├── alerts/
│   └── notifier.py         # Pop-up and sound alerts
│
└── pipeline/
    └── scheduler.py        # Scheduler for updating symbols continuously

Tech Stack

Python 3.x

Tkinter – GUI framework

Pandas & NumPy – Data manipulation and indicator calculations

Requests – API calls to Binance

Winsound – Audio notifications

Threading – Real-time concurrent execution

Installation & Setup

Clone the repository:

git clone https://github.com/<your-username>/crypto-signal-engine.git
cd crypto-signal-engine


Install dependencies:

pip install -r requirements.txt


Run the dashboard:

python main.py
