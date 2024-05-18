import random
from flask import Flask
from . import my_tools as tools
from . import wikimedia_commons_api as wiki_api

app = Flask(__name__)

def start_flask():
    app.run(host='localhost', port=2024, debug=True)


@app.route("/")
def home():
    return "Microservice Status: UP"


@app.route("/generateRandomPet")
def generate_random_pet():
    
    random_url = wiki_api.fetch_wikimedia_urls(search_for=tools.pick_random_config_value(), number_of_urls=10)
    image_path = wiki_api.save_image_from_url(random.choice(random_url))
    return image_path
