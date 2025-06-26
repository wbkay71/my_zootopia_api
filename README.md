# 🦊 Zootopia API – Dynamic Animal Info Website

Zootopia API is a Python-based application that dynamically generates a website displaying information about animals, using data fetched from a public API. Users can enter the name of any animal and receive a nicely styled HTML page with information such as habitat, diet, and type.

---

## 🚀 Features

- Retrieves animal data dynamically from the [API Ninjas Animal API](https://api-ninjas.com/api/animals)
- Generates a custom HTML website for the animal entered
- Displays structured cards with styling (name, diet, location, type)
- Includes an error message in the same design if the animal does not exist

---

## 🧠 Technologies Used

- Python 3
- Requests library (for API interaction)
- HTML/CSS (for styled output)
- Environment variables with `.env` file (to protect your API key)

---

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/zootopia_api.git
cd zootopia_api

zootopia_api/
│
├── animals_web_generator.py      # Main script (UI and HTML generation)
├── data_fetcher.py               # Fetches data from API
├── animals_template.html         # HTML template with placeholder
├── requirements.txt              # Python dependencies
├── .env                          # API key (not tracked by Git)
├── .gitignore                    # Ignoring .env and other local files
└── README.md                     # Project documentation

