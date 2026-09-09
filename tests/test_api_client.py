import pytest
from unittest.mock import Mock, patch
from src.api_client import *

def get_mock_response_data():
    """
    - Create sample API response data for testing:
    - This function returns the API sample response data in a dictionary.
    - Return: dict
    """
    return {
        'main': {
            'temp': 22,
            'humidity': 70,
            'feels_like': 20.5
        },
        'weather': [{
            'description': 'partly sunny'
        }],
        'wind': {
            'speed': 5.5,
            'direction': 'E'
        }
    }
def test_get_parse_weather_response():
    """
    Test if the sample API response is correct
    """
    mock_data = get_mock_response_data()
    result = get_mock_response_data(mock_data, "Cape Town")

    # Check that the response data is the same as WeatherData:
    assert isinstance(result, WeatherData)
    assert result.temperature == 22
    assert result.humidity == 70
    assert result.wind_speed == 5.5
    assert result.direction == 'E'
    assert result.feels_like == 20.5
    assert result.description == "partly sunny"
    assert result.location == "Cape Town"
    assert isinstance(result.timestamp, float)
