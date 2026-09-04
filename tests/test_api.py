import unittest
from app.crypto import get_crypto_price
from app.weather import get_city_weather

class TestAPIEngine(unittest.TestCase):

    def test_crypto_bitcoin_response(self):
        """Test that the crypto module returns valid numeric rates for Bitcoin."""
        data = get_crypto_price("bitcoin")
        self.assertIsNotNone(data, "Crypto API returned None")
        self.assertIn("usd", data, "USD key missing from crypto response")
        self.assertIsInstance(data["usd"], (int, float), "USD rate is not numeric")

    def test_weather_erode_response(self):
        """Test that the weather module returns valid coordinates and country data for Erode."""
        country, temp, wind = get_city_weather("Erode")
        self.assertIsNotNone(temp, "Temperature returned None")
        self.assertEqual(country, "India", f"Expected 'India', got '{country}'")

if __name__ == "__main__":
    unittest.main()