import random
import time
from datetime import datetime

pairs = [
    "EUR/USD",
    "USD/JPY",
    "GBP/USD",
    "AUD/USD",
    "USD/CAD"
]

print("=== ABBASIXBOT STARTED ===")

while True:
    pair = random.choice(pairs)
    signal = random.choice(["🟢 CALL", "🔴 PUT"])
    confidence = random.randint(70, 95)

    print("\n--------------------------")
    print("Pair:", pair)
    print("Signal:", signal)
    print("Confidence:", str(confidence) + "%")
    print("Time:", datetime.now().strftime("%H:%M:%S"))

    time.sleep(15)
