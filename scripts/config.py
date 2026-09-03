"""
This file stores the configuration of the API, database settings 
"""
# dotenv is a library that allows me to load the variables needed for this environment.

import os
from dotenv import load_dotenv

# Method that loads the environment:
load_dotenv()       

# API configuration setup:


API_KEY = os.getenv('OPENWEATHER_API_KEY') 
# os.getenv allows me to call or get a certain variable from the environment


BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

CITIES = ["Johannesburg", "East London", "Mossel Bay", 
        "George", "Cape Town", "Pretoria", "Durban"]

# Database setup:
DB_PATH = "weather_data.db"


# Ensure the API key works / is created:

if not API_KEY:
    raise ValueError("Please add generated API key for Weather in .env file")

