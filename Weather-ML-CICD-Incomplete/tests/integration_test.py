import unittest
import sys
import os

# Ensure app.py is discoverable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app  # Import your Flask app instance

class TestModelAppIntegration(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_model_app_integration(self):
        # Valid test input that should work with the trained model
        form_data = {
            'temperature': '275.15',   # Kelvin
            'pressure': '1013',        # hPa
            'humidity': '85',          # %
            'wind_speed': '3.6',       # m/s
            'wind_deg': '180',         # degrees
            'rain_1h': '0',            # mm
            'rain_3h': '0',            # mm
            'snow': '0',               # mm
            'clouds': '20'             # %
        }

        response = self.client.post('/', data=form_data)

        # Ensure the response is successful
        self.assertEqual(response.status_code, 200)

        # Decode HTML and check for valid prediction class
        html_text = response.data.decode('utf-8').lower()
        print("Response HTML:", html_text)  # Helpful for debugging

        valid_classes = [
            'clear', 'cloudy', 'drizzly', 'foggy', 'hazey',
            'misty', 'rainy', 'smokey', 'thunderstorm'
        ]
        found_class = any(weather in html_text for weather in valid_classes)
        self.assertTrue(found_class, "No valid weather class found in response.")

        # Check that latency is displayed
        self.assertIn('ms', html_text, "Latency not displayed in milliseconds.")

if __name__ == '__main__':
    unittest.main()
