import requests
import datetime
import json

from auth_handler import get_cj_api_auth

auth = get_cj_api_auth()
auth = (auth[0], auth[1])

base_url = 'http://api.cratejoy.com/v1/shipments'


def adjust_date(id, date):
    date = date
    url = base_url + id

    response = requests.put(url, data=json.dumps({\
        'adjusted_ordered_at': date
        }), auth=auth)

    return response


def add_tracking(ids):
    date = str(datetime.datetime.now().isoformat())

    print date

    for id in ids:
        id = str(id)
        url = base_url + id
        response = requests.put(url, data=json.dumps({\
            'status': 'shipped',\
            'shipped_at': date\
            }), auth=auth)

    # check responses, if failures build up array of failed IDs to return

    return response
