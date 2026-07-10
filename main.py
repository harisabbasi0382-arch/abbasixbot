import time
from datetime import datetime

print("=== ABBASIXBOT STARTED ===")

for i in range(20):
    print("------------------------")
    print("Time:", datetime.now().strftime("%H:%M:%S"))
    print("Bot is running...")
    time.sleep(5)

print("=== ABBASIXBOT FINISHED ===")
