import json
import requests


def fetch_animal_data(animal_name):
    """
    Fetches animal data from the API for the given animal name.
    Returns a list of results (can be empty if not found).
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {'X-Api-Key': 'g13wiSJKuuqKKeZVSTj5PA==v0bQqQNgDXk5EG3w'}

    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"API error: {response.status_code}")
            return []
    except Exception as e:
        print(f"Request failed: {e}")
        return []


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


def build_error_html(animal_name):
    """Return styled error message as an HTML element."""
    return f'''
<li class="cards__item">
  <div class="card__title" style="color: red; font-weight: bold;">
    The animal "{animal_name}" doesn't exist.
  </div>
</li>
'''


def insert_into_template(template_path, output_html, output_file):
    """Replace placeholder in HTML template and write final HTML to file."""
    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", output_html)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_html)


def main():
    animal_name = input("Enter a name of an animal: ").strip()
    results = fetch_animal_data(animal_name)

    if results:
        html_output = build_html(results)
    else:
        html_output = build_error_html(animal_name)

    insert_into_template("animals_template.html", html_output, "animals.html")
    print("✔️ Website was successfully generated to animals.html")


if __name__ == "__main__":
    main()