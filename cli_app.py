import argparse
import requests

def fetch_weather(city_name):
    """Fetch live weather details for a given city."""
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
                    print(f"\n🌤️ Weather Report for {city_name.title()}, {country}:")
                    print(f"  • Temperature: {w_data['temperature']}°C")
                    print(f"  • Wind Speed:  {w_data['windspeed']} km/h")
                    return
        print(f"\n❌ City '{city_name}' not found.")
    except Exception as e:
        print(f"\n❌ Request failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="🚀 Hackathon Weather CLI Tool")
    parser.add_argument("--city", "-c", type=str, required=True, help="Name of the city to query weather for")
    
    args = parser.parse_args()
    fetch_weather(args.city)

if __name__ == "__main__":
    main()