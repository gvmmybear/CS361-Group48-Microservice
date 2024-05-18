from colorama import *
from . import my_tools as tools
import os
import requests


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
        'gsrsearch': search_for,
        'filemime': 'image/jpeg|image/png'
    }

    print(Fore.BLUE + 'Sending request to wikimedia commons...')
    response = requests.get(wikimedia, params=parameters)
    if response.status_code == 200:
        return tools.url_payload_parser(response)
    else:
        print(Fore.RED + f'ERROR! Urls could not be fetched. Response Code: {response.status_code}')
        return []


# sends a req to wikimedia using an image url and then saves the image to local microservice folder /images
def save_image_from_url(url):
    try:
        # https://foundation.wikimedia.org/wiki/Policy:User-Agent_policy
        headers = {'User-Agent': 'CoolBot/0.0 (https://example.org/coolbot/; coolbot@example.org)'}
        response = requests.get(url, headers=headers)

        # clean up url and use string for unique file name
        file_name = ''.join(url.split('/'))[13:]
        download_path = f'./images/{file_name}'

        # save the file using byte chunks
        with open(download_path, 'wb') as file:
            for byte_chunk in response.iter_content():
                file.write(byte_chunk)
        
        # log output to console and return the absolute path of the downloaded image
        print(f'Image downloaded successsfully! File saved as: {file_name}')
        return os.path.abspath(download_path)
    except Exception as e:
        print(Fore.RED + f"Error downloading image from {url}: {e}")
        return
