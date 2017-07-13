import requests
import datetime
from dateutil.relativedelta import relativedelta
import json

from auth_handler import get_cj_api_auth

auth = get_cj_api_auth()
auth = (auth[0], auth[1])

base_url = 'http://api.cratejoy.com/v1/shipments/'


def adjust_shipment_date(shipment, date):
    url = base_url + shipment + '/'
    print url
    date = str(date)
    response = requests.put(url, data=json.dumps({\
        'adjusted_ordered_at': date
    }), auth=auth)
    return response


def adjust_by_date(shipments, date):
    shipments = shipments.split(',')
    failed_shipments = []
    for shipment in shipments:
        response = adjust_shipment_date(shipment, date)
        if response.status_code != 200:
            failed_shipments.append(shipment)
    return failed_shipments


def adjust_by_month(shipments, month):
    shipments = shipments.split(',')
    failed_shipments = []
    for shipment in shipments:
        url = base_url + shipment + '/?adjusted_ordered_at'
        date = requests.get(url) + relativedelta(months=month)
        response = adjust_shipment_date(shipment, date)
        if response.status_code != 200:
            failed_shipments.append(shipment)
    return failed_shipments


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
