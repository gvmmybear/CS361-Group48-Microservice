from colorama import *
import json
import random


# loads the config file for 'random' animal bank
# source of config values: https://gist.github.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54
def load_config_file(config_file):
    pet_config = []
    with open(config_file, 'r') as config:
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


def pick_random_config_value():
    values = load_config_file('./pet_config.txt')
    random_index = random.randint(1, 999_999_999) % len(values)
    print(random_index)
    print(values[random_index])
    random_value = values[random_index]
    return random_value


def remove_svgs_from_list(list_of_urls):
    for url in list_of_urls:
        if url[-4:] == '.svg':
            list_of_urls.remove(url)
            # print(url[-4:])
    return list_of_urls