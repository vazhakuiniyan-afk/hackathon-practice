import requests

print("--- The AI Age Guesser ---")

# 1. Get input from the user
user_name = input("Type a first name and press Enter: ")

# 2. Add their name to the API URL
url = f"https://api.agify.io?name={user_name}"

# 3. Talk to the waiter and get the data
response = requests.get(url)
data = response.json()

# 4. Print the custom result safely
if data['age'] is None:
    print(f"Wow! The AI has never heard of the name {user_name} before! You broke the matrix.")
else:
    print(f"The AI guesses that {user_name} is {data['age']} years old!")