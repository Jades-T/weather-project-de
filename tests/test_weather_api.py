import unittest
from unittest.mock import patch, Mock
import sys 
sys.path.append('.')
from extract import extract_weather_for_city



class TestWeatherAPI(unittest.TestCase):
    # Test 1: Does the API parse correctly?
    
    # fakes the real call for requests.get 
    @patch('extract.request.get')
    def test_fetch_api_success(self, mock_get):

        # Arrange : create fake API response
        fake_response = Mock()
        fake_response.json.return_value = {"humidity": 70}, "weather":[{"main": "Clear"}]
            "name": "Cape Town", "main": {"temp": 25.5, ""}



        }
        # Act
        # Assert