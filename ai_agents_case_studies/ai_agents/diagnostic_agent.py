import time
import random

def simulate_diagnosis():
    processing_time = random.uniform(1.0, 2.5)
    time.sleep(processing_time)
    return processing_time

if __name__ == "__main__":
    t = simulate_diagnosis()
    print(f"AI diagnosis completed in {t:.2f} seconds.")
