import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

API_KEY = os.getenv("API_KEY")

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ API error {response.status_code}: {response.text}")
            return []
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return []