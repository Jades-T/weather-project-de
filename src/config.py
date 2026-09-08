"""
Config sets up the environment for the weather project.
This allows me to use the API, Database and other variables inside an environment.

"""
import os
from dotenv import load_dotenv

def load_config() -> dict:
    """
    This function loads the configuration settings for the project.
    The API key, API url, Database Path will be configured.
    """
    load_dotenv()
    #  Allows me to load the variables in the environment

    # config settings will be returned as a dictionary:
    """
    weather_api_key
    weather_api_url
    database_path
    update_interval (Minutes)
    maximum amount of retries (Integer)
    retry_delay (Seconds)
    log_level (Still need to find out what is cooking here?)
    """
    config = {
        'weather_api_key': os.getenv('WEATHER_API_KEY', ''),
        'weather_api_url': os.getenv('WEATHER_API_URL','https://api.openweathermap.org/data/2.5/weather'),
        'database_path': os.getenv('DATABASE_PATH', 'data/weather.db'),
        'update_interval': int(os.getenv('UPDATE_INTERVAL_MINUTES', '60')) ,        # minutes
        'max_retries': int(os.getenv('MAX_RETRIES', '3')),
        'retry_delay': int(os.getenv('RETRY_DELAY', '1')),             # seconds
        'log_level':,               # check what this does?
        'log_file':    
    }

    return config









def validate_config(config: dict) -> bool:
    pass


def get_config() -> dict:
    pass