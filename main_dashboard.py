import requests

def fetch_crypto_price(symbol="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd,inr"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            data = res.json()
            if symbol in data:
                return data[symbol]
    except Exception as e:
        print(f"  [Crypto Error]: {e}")
    return None

def fetch_city_weather(city_name):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    try:
        geo_res = requests.get(geo_url, timeout=5)
        if geo_res.status_code == 200:
            geo_data = geo_res.json()
            if "results" in geo_data and len(geo_data["results"]) > 0:
                loc = geo_data["results"][0]
                lat, lon = loc["latitude"], loc["longitude"]
                country = loc.get("country", "Unknown")
                
                weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
                w_res = requests.get(weather_url, timeout=5)
                if w_res.status_code == 200:
                    w_data = w_res.json()["current_weather"]
                    return country, w_data["temperature"], w_data["windspeed"]
    except Exception as e:
        print(f"  [Weather Error]: {e}")
    return None, None, None

def display_menu():
    print("\n==========================================")
    print("   🌐 HACKATHON MULTI-TOOL CLI ENGINE    ")
    print("==========================================")
    print("1. Check Live Cryptocurrency Price")
    print("2. Check Live Weather by City")
    print("3. Exit")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            coin = input("Enter coin name (e.g., bitcoin, ethereum, cardano): ").strip().lower()
            if coin:
                data = fetch_crypto_price(coin)
                if data:
                    print(f"\n📊 {coin.upper()} Market Rates:")
                    print(f"  • USD: ${data.get('usd', 'N/A'):,}")
                    print(f"  • INR: ₹{data.get('inr', 'N/A'):,}")
                else:
                    print(f"\n❌ Could not fetch price data for '{coin}'.")
                    
        elif choice == "2":
            city = input("Enter city name: ").strip()
            if city:
                country, temp, wind = fetch_city_weather(city)
                if temp is not None:
                    print(f"\n🌤️ Weather for {city.title()}, {country}:")
                    print(f"  • Temperature: {temp}°C")
                    print(f"  • Wind Speed: {wind} km/h")
                else:
                    print(f"\n❌ Could not fetch weather data for '{city}'.")
                    
        elif choice == "3":
            print("\nShutting down engine. Happy hacking!")
            break
        else:
            print("\n⚠️ Invalid selection. Please enter 1, 2, or 3.")