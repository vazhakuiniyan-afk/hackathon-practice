import requests

url = input("Enter an API URL to test: ")

try:
    # Set a 5-second timeout so the app doesn't freeze forever if offline
    response = requests.get(url, timeout=5)
    
    print(f"\nHTTP Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print("✅ Connection Successful!")
        print("Response Data:", response.json())
    elif response.status_code == 404:
        print("❌ Error 404: Resource or endpoint not found.")
    elif response.status_code == 429:
        print("⚠️ Error 429: Rate limit exceeded. Slow down your requests.")
    else:
        print(f"⚠️ Server returned unhandled status code: {response.status_code}")

except requests.exceptions.Timeout:
    print("❌ Error: Request timed out. The server took too long to answer.")
except requests.exceptions.ConnectionError:
    print("❌ Error: Failed to connect. Check your internet connection.")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")