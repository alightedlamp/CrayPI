import requests
import json

from auth_handler import get_cj_api_auth

auth = get_cj_api_auth()
auth = (auth[0], auth[1])

base_url = 'http://api.cratejoy.com/v1/products/'


def get_products():
    response = requests.get(base_url)
    return response
