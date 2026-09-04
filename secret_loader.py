import os

def load_env_file(filepath=".env"):
    """Parse a local .env file and set values into environment variables."""
    if not os.path.exists(filepath):
        print(f"⚠️ Configuration file '{filepath}' not found.")
        return
    
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip().strip("'\"")

def main():
    print("=== 🔐 Environment Variable Loader ===")
    load_env_file()
    
    weather_key = os.environ.get("WEATHER_API_KEY", "NOT_FOUND")
    finance_key = os.environ.get("FINANCE_API_KEY", "NOT_FOUND")
    debug = os.environ.get("DEBUG_MODE", "False")
    
    print(f"\nLoaded Credentials:")
    print(f"  • Weather API Key: {weather_key}")
    print(f"  • Finance API Key: {finance_key}")
    print(f"  • Debug Mode     : {debug}")

if __name__ == "__main__":
    main()