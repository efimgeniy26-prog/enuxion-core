import time
import random

# ENUXION LAB - Network Utility Tool
# Purpose: Simulating real-time liquidity scan for ENU pairs

class EnuxionScanner:
    def __init__(self):
        self.version = "1.0.2"
        self.active = True

    def scan_liquidity(self):
        print(f"--- Enuxion Scanner v{self.version} ---")
        print("[INFO] Initializing RPC connection...")
        
        pairs = ["SOL/ENU", "USDC/ENU", "SOL/USDC"]
        
        try:
            while self.active:
                target = random.choice(pairs)
                depth = round(random.uniform(10.5, 500.0), 2)
                print(f"[SCAN] Analyzing pair: {target} | Pool Depth: {depth} SOL")
                time.sleep(3)
        except KeyboardInterrupt:
            print("\n[STOP] Scanner paused by operator.")

if __name__ == "__main__":
    scanner = EnuxionScanner()
    scanner.scan_liquidity()
