import requests

print("=== 🤖 Hackathon AI Identity Predictor ===")

name = input("Enter a first name: ")

# API 1: Age Prediction
age_url = f"https://api.agify.io?name={name}"
age_data = requests.get(age_url).json()

# API 2: Country Prediction
country_url = f"https://api.nationalize.io?name={name}"
country_data = requests.get(country_url).json()

print("\n--- RESULTS ---")

# Handle Age Result
if age_data.get('age') is None:
    print(f"- Age: Unknown (Name not found in database)")
else:
    print(f"- Age: ~{age_data['age']} years old")

# Handle Country Result
if country_data.get('country') and len(country_data['country']) > 0:
    top_country = country_data['country'][0]['country_id']
    probability = round(country_data['country'][0]['probability'] * 100, 1)
    print(f"- Nationality: Most likely {top_country} ({probability}% confidence)")
else:
    print("- Nationality: Unknown")