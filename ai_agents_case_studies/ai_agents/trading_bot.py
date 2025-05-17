import time
import random

def simulate_trading_bot():
    latency = random.uniform(0.01, 0.1)
    time.sleep(latency)  # Simulate real-time market reaction
    return latency

if __name__ == "__main__":
    latency = simulate_trading_bot()
    print(f"Trading bot executed trade with simulated latency of {latency:.3f} seconds.")
