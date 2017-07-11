import requests
import datetime
import json

from auth_handler import get_cj_api_auth

auth = get_cj_api_auth()
auth = (auth[0], auth[1])

base_url = 'http://api.cratejoy.com/v1/shipments/'


def adjust_date(shipment_id, date):
    url = base_url + shipment_id + '/'
    date = date

    response = requests.put(url, data=json.dumps({\
        'adjusted_ordered_at': date
        }), auth=auth)

    return response


def add_tracking(shipment_ids, tracking_numbers):
    date = str(datetime.datetime.now().isoformat())

    for shipment_id in shipment_ids:
        shipment_id = str(shipment_id)
        url = base_url + shipment_id
        response = requests.put(url, data=json.dumps({\
            'status': 'shipped',\
            'shipped_at': date\
            }), auth=auth)

    # check responses, if failures build up array of failed IDs to return

    return response
