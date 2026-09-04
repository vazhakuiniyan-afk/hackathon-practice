import requests

def get_crypto_price(coin_id="bitcoin"):
    """Fetch live cryptocurrency prices using CoinGecko's open API."""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd,inr"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            data = res.json()
            if coin_id in data:
                return data[coin_id]
    except Exception as e:
        print(f"[Crypto API Error]: {e}")
    return None

def get_iss_location():
    """Fetch real-time location of the International Space Station."""
    url = "http://api.open-notify.org/iss-now.json"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            data = res.json()
            if data.get("message") == "success":
                pos = data["iss_position"]
                return pos["latitude"], pos["longitude"]
    except Exception as e:
        print(f"[ISS API Error]: {e}")
    return None, None

def run_dashboard():
    print("==========================================")
    print("   🚀 HACKATHON REAL-TIME DATA ENGINE    ")
    print("==========================================")
    
    # 1. Fetch Crypto Rates
    print("\n[1/2] Querying Global Financial Market Data...")
    crypto_data = get_crypto_price("bitcoin")
    if crypto_data:
        print(f"  • Bitcoin (USD): ${crypto_data['usd']:,}")
        print(f"  • Bitcoin (INR): ₹{crypto_data['inr']:,}")
    else:
        print("  • Crypto Data: Service unavailable.")

    # 2. Fetch ISS Telemetry
    print("\n[2/2] Fetching Live ISS Space Coordinates...")
    lat, lon = get_iss_location()
    if lat and lon:
        print(f"  • Current ISS Latitude : {lat}")
        print(f"  • Current ISS Longitude: {lon}")
    else:
        print("  • Space Telemetry: Service unavailable.")
        
    print("\n==========================================")

if __name__ == "__main__":
    run_dashboard()