from colorama import *
import json


# loads the config file for 'random' animal bank
# source of config values: https://gist.github.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54
def load_config_file():
    pet_config = []
    with open('pet_config.txt', 'r') as config:
        for line in config:
            pet_config.append(line.strip())

    # print(pet_config)
    return pet_config


# function to parse and cleanup the payload and return list of urls
def url_payload_parser(response):
    # grab the response data
    json_payload = response.json()
    payload_values = json_payload.get('query', {}).get('pages', {}).values()
    
    # console logging
    print(Fore.GREEN + 'WIKIMEDIA RESPONSE: ' + str(response.status_code))
    print(Fore.WHITE + 'PAYLOAD:')
    print(json.dumps(json_payload, indent=2))

    # grab the url values from each search result
    image_urls = []
    for value in payload_values:
        image_urls.append(value['imageinfo'][0]['url'])
    print(f'URLS:{image_urls}')
    return image_urls
