\[12:20 pm, 04/09/2026] Azhaku Iniyan: import requests



def get\_age\_prediction(name):

&#x20;   """Fetch age prediction from Agify API."""

&#x20;   try:

&#x20;       res = requests.get(f"https://api.agify.io?name={name}", timeout=5)

&#x20;       if res.status\_code == 200:

&#x20;           return res.json().get('age')

&#x20;   except Exception:

&#x20;       pass

&#x20;   return None



def get\_country\_prediction(name):

&#x20;   """Fetch country prediction from Nationalize API."""

&#x20;   try:

&#x20;       res = requests.get(f"https://api.nationalize.io?name={name}", timeout=5)

&#x20;       if res.status\_code == 200:

&#x20;           data = res.json()

&#x20;           if data.get('country') and len(data\['country']) > 0:

&#x20;               top = data\['country']\[0]

&#x20;               return top\['country\_id'], round(top\['probability'] \* 100, 1)

&#x20;   except Exception:

&#x20;       pas…

\[12:47 pm, 04/09/2026] Azhaku Iniyan: import requests



def get\_crypto\_price(coin\_id="bitcoin"):

&#x20;   """Fetch live cryptocurrency prices using CoinGecko's open API."""

&#x20;   url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin\_id}\&vs\_currencies=usd,inr"

&#x20;   try:

&#x20;       res = requests.get(url, timeout=5)

&#x20;       if res.status\_code == 200:

&#x20;           data = res.json()

&#x20;           if coin\_id in data:

&#x20;               return data\[coin\_id]

&#x20;   except Exception as e:

&#x20;       print(f"\[Crypto API Error]: {e}")

&#x20;   return None



def get\_iss\_location():

&#x20;   """Fetch real-time location of the International Space Station."""

&#x20;   url = "http://api.open-notify.org/iss-now.json"

&#x20;   try:

&#x20;       res = requests.get(url, timeout=5)

&#x20;       if res.status\_code == 200:

&#x20;           data = res.json()

&#x20;       …

\[12:58 pm, 04/09/2026] Azhaku Iniyan: import requests



def fetch\_crypto\_price(symbol="bitcoin"):

&#x20;   url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}\&vs\_currencies=usd,inr"

&#x20;   try:

&#x20;       res = requests.get(url, timeout=5)

&#x20;       if res.status\_code == 200:

&#x20;           data = res.json()

&#x20;           if symbol in data:

&#x20;               return data\[symbol]

&#x20;   except Exception as e:

&#x20;       print(f"  \[Crypto Error]: {e}")

&#x20;   return None



def fetch\_city\_weather(city\_name):

&#x20;   geo\_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city\_name}\&count=1"

&#x20;   try:

&#x20;       geo\_res = requests.get(geo\_url, timeout=5)

&#x20;       if geo\_res.status\_code == 200:

&#x20;           geo\_data = geo\_res.json()

&#x20;           if "results" in geo\_data and len(geo\_data\["results"]) > 0:

&#x20;              …

\[1:12 pm, 04/09/2026] Azhaku Iniyan: # 🌐 Hackathon Multi-Tool CLI Engine



A modular Python command-line interface (CLI) built for rapid API integration, error resilience, and real-time data aggregation. Developed as a technical portfolio project for hackathon development setups.



\## 🚀 Key Features



\* \*Real-Time Data Aggregation\*: Fetches live cryptocurrency market rates and geocoded weather forecasts.

\* \*Resilient Architecture\*: Built-in HTTP status code verification, 5-second request timeouts, and global try/except fallback logic.

\* \*Interactive CLI\*: Menu-driven interface supporting repeated queries without session crashes.

\* \*Modular Codebase\*: Functional separation (def) and \_\_main\_\_ entry point execution.



\## 🛠️ Tech Stack



\* \*Language\*: Python 3.x

\* \*Libraries\*: requests

\* \*Version Control\*: Git / GitHub

\* \*APIs Integrated\*:

&#x20; \* \[CoinGecko API](https://www.coingecko.com/en/api) (Financial Data)

&#x20; \* \[Open-Meteo API](https://open-meteo.com/) (Geocoding \& Weather Data)

&#x20; \* \[Agify \& Nationalize APIs](https://agify.io/) (Demographic Predictions)



\## 📦 Project Structure



```text

hackathon-practice/

├── main\_dashboard.py      # Capstone interactive CLI engine

├── hackathon\_engine.py    # Multi-source data aggregator

├── portfolio\_builder.py  # Modular identity predictor engine

├── weather\_app.py        # Geocoding \& weather pipeline

├── checker.py            # API status code \& error checker

├── .gitignore            # Security exclusions

└── README.md             # Project documentation

