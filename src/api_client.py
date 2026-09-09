"""
- This is a Weather API client that fetches weather data from OpenWeatherMAP API.
- This file handles the interaction / communication with the external data source this project uses.
"""

import requests
import time
from dataclasses import dataclass
from datetime import datetime
