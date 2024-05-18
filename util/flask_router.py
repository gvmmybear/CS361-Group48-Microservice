import random
import json
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
    random_pet = tools.pick_random_config_value()
    random_urls = wiki_api.fetch_wikimedia_urls(search_for=random_pet, number_of_urls=10)
    image_path = wiki_api.save_image_from_url(random.choice(tools.remove_svgs_from_list(random_urls)))
    payload = {
        'entity_type': random_pet,
        'image_path': image_path
    }

    return json.dumps(payload)


@app.route("/generateImage/<entity_type>")
def generate_image(entity_type):
    image_urls = wiki_api.fetch_wikimedia_urls(search_for=entity_type, number_of_urls=10)
    image_path = wiki_api.save_image_from_url(random.choice(tools.remove_svgs_from_list(image_urls)))
    payload = {
        'entity_type': entity_type,
        'image_path': image_path
    }

    return json.dumps(payload)
