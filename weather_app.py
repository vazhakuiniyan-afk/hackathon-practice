import requests

print("=== 🌤️ Real-Time City Weather Lookup ===")

city_name = input("Enter a city name: ")

# Stage 1: Convert City Name to Coordinates (Geocoding API)
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
geo_data = requests.get(geo_url).json()

if "results" not in geo_data or len(geo_data["results"]) == 0:
    print(f"Error: Could not find coordinates for '{city_name}'. Check spelling.")
else:
    # Extract coordinates from nested JSON list
    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    country = location.get("country", "Unknown")

    # Stage 2: Fetch Live Weather using Latitude & Longitude
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_data = requests.get(weather_url).json()

    # Extract current weather properties
    current = weather_data["current_weather"]
    temp = current["temperature"]
    wind = current["windspeed"]

    print(f"\n--- WEATHER REPORT: {city_name.title()}, {country} ---")
    print(f"- Temperature: {temp}°C")
    print(f"- Wind Speed: {wind} km/h")