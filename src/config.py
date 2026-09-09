"""
- Config sets up the environment for the weather project.
- This allows me to use the API, Database and other variables inside an environment.

"""
import os
from dotenv import load_dotenv

def load_config() -> dict:
    """
    - This function loads the configuration settings for the project.
    - The API key, API url, Database Path will be configured.
    - Return: dict
    """

    load_dotenv()
    # Allows me to load the variables in the environment 


    config = {
    # config settings will be returned as a dictionary
        'weather_api_key': os.getenv('WEATHER_API_KEY', ''),
        'weather_api_url': os.getenv('WEATHER_API_URL','https://api.openweathermap.org/data/2.5/weather'),
        'database_path': os.getenv('DATABASE_PATH', 'data/weather.db'),
        'update_interval': int(os.getenv('UPDATE_INTERVAL', '60')) ,
        'max_retries': int(os.getenv('MAX_RETRIES', '3')),
        'retry_delay': int(os.getenv('RETRY_DELAY', '1')),
        # 'log_level':,               # check what this does?
        # 'log_file':    
    }

    return config



def validate_config(config: dict) -> bool:
    """
    - This functions validates that the configuration settings are correct and actually exists.
    - Args: The dictionary config, will be used and also loaded using from load_config()
    - Returns: True if the configuration is valid and exists
    - Raises: Should give a ValueError if the config is invalid and does nort exist.
    """

    if not config.get('weather_api_key') and not config.get('weather_api_url'):
        raise ValueError("WEATHER_API_KEY and WEATHER_API_URL is required to proceed.")
    
    
    if not config.get('update_interval', 0)<=0:
        raise ValueError("UPDATE_INTERNAL must be in minutes and must be positive.")
    
    if not config.get('max_entries', 0) < 0:
        raise ValueError("MAX ENTRIES cannot be negative.")
    
    if not config.get('retry_delay'):
        raise ValueError("RETRY_DELAY must be in seconds and must be positive.")

    # See if you should add the log_levels information.
    # Is the log level data needed?
    return True

def get_config() -> dict:
    """
    - This function combines the loading and validation of the configuration settings for the project.    
    - Returns: Indicates if the validation of the configuration file is correctly setup.
    - Raises: A value error is raised if the configuration validation failed.
    """

    # load the configuration from the environment variables.
    config = load_config()

    # Validate the configuration, ensures it works. Should raise value error if something is wrong.
    validate_config(config)

    # returns the validate configuration.
    return config