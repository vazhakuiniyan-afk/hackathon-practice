import json
import requests
from datetime import datetime

LOG_FILE = "search_history.json"

def fetch_and_log_crypto(coin_id="bitcoin"):
    """Fetch live crypto rates and append the result to a local JSON file."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd,inr"
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if coin_id in data:
                record = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "asset": coin_id,
                    "usd_price": data[coin_id]["usd"],
                    "inr_price": data[coin_id]["inr"]
                }
                
                # Load existing log file if it exists, otherwise create a new list
                try:
                    with open(LOG_FILE, "r") as f:
                        logs = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    logs = []
                
                # Append new query record
                logs.append(record)
                
                # Write updated log back to file
                with open(LOG_FILE, "w") as f:
                    json.dump(logs, f, indent=4)
                
                print(f"✅ Successfully exported report for '{coin_id}' to {LOG_FILE}:")
                print(json.dumps(record, indent=2))
                return
        print(f"❌ Failed to retrieve data for '{coin_id}'.")
    except Exception as e:
        print(f"❌ Logging error: {e}")

if __name__ == "__main__":
    coin = input("Enter cryptocurrency to fetch & log (e.g., bitcoin, ethereum): ").strip().lower()
    if coin:
        fetch_and_log_crypto(coin)