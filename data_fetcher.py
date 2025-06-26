import requests

API_KEY = 'g13wiSJKuuqKKeZVSTj5PA==v0bQqQNgDXk5EG3w'
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': { ... },
        'locations': [ ... ],
        'characteristics': { ... }
    }
    """
    url = API_URL.format(animal_name)
    headers = {'X-Api-Key': API_KEY}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API Error {response.status_code}: {response.text}")
            return []
    except Exception as e:
        print(f"Request failed: {e}")
        return []
