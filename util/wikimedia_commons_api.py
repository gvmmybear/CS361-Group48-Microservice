from colorama import *#init, Fore
import requests
import json


# Function makes a request to wikimedia commons for urls with an input param for search topic 
# and number of urls desired. Default it set to 3 urls per request.
def fetch_wikimedia_urls(search_for, number_of_urls=3):
    init() # colorama for color text console print
    wikimedia = 'https://commons.wikimedia.org/w/api.php'
    parameters = {
        'action': 'query',
        'generator': 'search',
        'prop': 'imageinfo',
        'format': 'json',
        'iiprop': 'url', # Image Information Properties (IIPROP)
        'gsrnamespace': 6, # Global Shared Repository (GSR) namespace: 6 is the value for file namespace
        'gsrlimit': number_of_urls,
        'gsrsearch': search_for
    }

    print(Fore.BLUE + 'Sending request to wikimedia commons...')
    response = requests.get(wikimedia, params=parameters)
    if response.status_code == 200:
        return url_payload_parser(response)
    else:
        print(Fore.RED + f'ERROR! Urls could not be fetched. Response Code: {response.status_code}')
        return []


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

