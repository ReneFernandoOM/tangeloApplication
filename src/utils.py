import requests
import hashlib
from typing import List, Dict, Tuple

from config import API_URL, API_RESOURCE
from errors import HandledError

def get_all_countries() -> List:
    api_response = requests.get(f"{API_URL}/{API_RESOURCE}")

    if api_response.ok:
        all_countries = api_response.json()
        return all_countries

    raise HandledError('API is not responding as expected')

def get_country_info(country: Dict) -> Tuple[str, str, List]:
    country_name_info = country.get('name', {})
    country_name = country_name_info.get('common')
    
    # in case it doesn't have a 'common' name
    if not country_name:
        country_name = country_name_info.get('official')

    region = country.get('region')
    languages = country.get('languages')

    if country_name and region and languages:
        return country_name, region, list(languages.values())

def encrypt_string(string: str) -> str:
    encrypted_string = hashlib.sha1(string.encode()).hexdigest()
    return encrypted_string

# def save_json(df):