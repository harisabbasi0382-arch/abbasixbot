import yfinance as yf
import pandas as pd
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator

# Get market data
data = yf.download("EURUSD=X", period="5d", interval="5m")

# Indicators
data["EMA9"] = EMAIndicator(data["Close"], window=9).ema_indicator()
data["EMA21"] = EMAIndicator(data["Close"], window=21).ema_indicator()
data["RSI"] = RSIIndicator(data["Close"], window=14).rsi()

last = data.iloc[-1]

if last["EMA9"] > last["EMA21"] and last["RSI"] < 70:
    print("🟢 BUY SIGNAL")
elif last["EMA9"] < last["EMA21"] and last["RSI"] > 30:
    print("🔴 SELL SIGNAL")
else:
    print("⚪ WAIT")
