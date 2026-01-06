# strategy/momentum.py

def generate_signal(rsi, macd, macd_signal, macd_hist):
    """
    Decide LONG / SHORT / HOLD based on indicator values
    """

    if 30 <= rsi < 40 and macd > macd_signal and macd_hist > 0:
        return "LONG", "green"

    elif 60 < rsi <= 70 and macd < macd_signal and macd_hist < 0:
        return "SHORT", "red"

    return "HOLD", "white"
