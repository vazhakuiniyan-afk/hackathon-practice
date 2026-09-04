import requests

print("Fetching a random joke for your hackathon...")

# 1. Talk to the waiter (API)
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

# 2. Get the food (Data) on a plate (JSON)
data = response.json()

# 3. Serve it nicely to the user
print("- " + data['setup'])
print("- " + data['punchline'])