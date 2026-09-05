import unittest
from unittest.mock import patch, Mock
import sys 
sys.path.append('.')
from extract import extract_weather_for_city


# each test case has a layout of AAA (Act Assert Arrange):
class TestWeatherAPI(unittest.TestCase):
    # Test 1: Does the API parse a good response correcyly?
    @patch('extract.request.get')       # this fakes the requests.get
    def test_fetch_api_success(self, mock_get):





    # Test 2: What if API fails?
    # Test 3: Integration of API, how it work within the system.
