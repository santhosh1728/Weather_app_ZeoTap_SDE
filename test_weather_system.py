# test_weather_system.py

import unittest
from unittest.mock import patch, MagicMock
from weather import fetch_and_process_weather_data, kelvin_to_celsius_fahrenheit
from email_alerts import send_email_alert

class TestWeatherSystem(unittest.TestCase):

    @patch('requests.get')
    def test_system_setup(self, mock_get):
        # Mock API response
        mock_get.return_value.json.return_value = {
            'main': {'temp': 300.0, 'feels_like': 298.0, 'humidity': 80},
            'wind': {'speed': 5.0},
            'weather': [{'description': 'clear sky'}],
            'sys': {'sunrise': 1629820500, 'sunset': 1629870100},
            'timezone': 19800
        }
        fetch_and_process_weather_data()
        self.assertTrue(mock_get.called)

    @patch('requests.get')
    def test_data_retrieval(self, mock_get):
        # Mock API response
        mock_get.return_value.json.return_value = {
            'main': {'temp': 300.0, 'feels_like': 298.0, 'humidity': 80},
            'wind': {'speed': 5.0},
            'weather': [{'description': 'clear sky'}],
            'sys': {'sunrise': 1629820500, 'sunset': 1629870100},
            'timezone': 19800
        }
        fetch_and_process_weather_data()
        self.assertTrue(mock_get.called)

    def test_kelvin_to_celsius_fahrenheit(self):
        kelvin = 300
        celsius, fahrenheit = kelvin_to_celsius_fahrenheit(kelvin)
        self.assertAlmostEqual(celsius, 26.85, places=2)
        self.assertAlmostEqual(fahrenheit, 80.33, places=2)

    @patch('requests.get')
    @patch('pymongo.MongoClient')
    def test_database_insertion(self, mock_client, mock_get):
        # Mock API response
        mock_get.return_value.json.return_value = {
            'main': {'temp': 300.0, 'feels_like': 298.0, 'humidity': 80},
            'wind': {'speed': 5.0},
            'weather': [{'description': 'clear sky'}],
            'sys': {'sunrise': 1629820500, 'sunset': 1629870100},
            'timezone': 19800
        }
        mock_client.return_value = MagicMock()
        fetch_and_process_weather_data()
        # Check if data is inserted into daily_weather_summary collection
        mock_client.return_value.weather_data.daily_weather_summary.insert_one.assert_called()

    @patch('requests.get')
    @patch('pymongo.MongoClient')
    def test_forecast_insertion(self, mock_client, mock_get):
        # Mock API response for forecast
        mock_get.return_value.json.return_value = {
            'list': [
                {'main': {'temp': 300.0, 'humidity': 80},
                 'wind': {'speed': 5.0},
                 'weather': [{'description': 'clear sky'}],
                 'dt': 1629820500}
            ]
        }
        mock_client.return_value = MagicMock()
        fetch_and_process_weather_data()
        # Check if data is inserted into weather_forecast collection
        mock_client.return_value.weather_data.weather_forecast.insert_one.assert_called()

if __name__ == '__main__':
    unittest.main()
