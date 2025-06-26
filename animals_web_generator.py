import json
import requests


def fetch_fox_data_and_save():
    """
    Fetch data about the animal 'Fox' from the API and save it to animals_data.json.
    """
    api_url = 'https://api.api-ninjas.com/v1/animals?name=fox'
    headers = {'X-Api-Key': 'g13wiSJKuuqKKeZVSTj5PA==v0bQqQNgDXk5EG3w'}

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            with open('animals_data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print("✔️ Fox data saved to animals_data.json.")
        else:
            print(f"❌ API Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Request failed: {e}")


def load_animals(file_path):
    """Load the animal data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def serialize_animal(animal):
    """Convert a single animal dictionary into a formatted HTML string."""
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    locations = animal.get("locations")
    location = locations[0] if locations else None
    animal_type = animal.get("characteristics", {}).get("type")

    html = '<li class="cards__item">\n'

    if name:
        html += f'  <div class="card__title">{name}</div>\n'

    html += '  <p class="card__text">\n'
    if diet:
        html += f'    <strong>Diet:</strong> {diet}<br/>\n'
    if location:
        html += f'    <strong>Location:</strong> {location}<br/>\n'
    if animal_type:
        html += f'    <strong>Type:</strong> {animal_type}<br/>\n'
    html += '  </p>\n'
    html += '</li>\n\n'

    return html


def build_html(animal_list):
    """Generate the full HTML string for all animals."""
    output = ""
    for animal in animal_list:
        output += serialize_animal(animal)
    return output


def insert_into_template(template_path, output_html, output_file):
    """Replace placeholder in HTML template and write final HTML to file."""
    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", output_html)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_html)


def main():
    # Fetch and save API data for "Fox"
    fetch_fox_data_and_save()

    # Load saved animal data from JSON file
    animals = load_animals("animals_data.json")

    # Generate HTML and insert it into the template
    html_output = build_html(animals)
    insert_into_template("animals_template.html", html_output, "animals.html")


if __name__ == "__main__":
    main()