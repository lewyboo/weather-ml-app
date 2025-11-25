import unittest
import numpy as np
from app import classify_weather

class TestUnit(unittest.TestCase):
    def test_classify_weather_output(self):
        # create dummy input with 10 numerical features
        features = np.array([[20, 1013, 50, 5, 180, 0, 0, 0, 0]])
        prediction, latency = classify_weather(features)

        # check that prediction is a string from weather_classes
        self.assertIsInstance(prediction, str)
        self.assertIn(prediction, [
            'clear', 'cloudy', 'drizzly', 'foggy', 'hazey',
            'misty', 'rainy', 'smokey', 'thunderstorm'
        ])

        # check that latency is a float
        self.assertIsInstance(latency, float)

if __name__ == '__main__':
    unittest.main()
