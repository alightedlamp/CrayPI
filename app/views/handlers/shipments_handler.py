import requests
import datetime
from dateutil.relativedelta import relativedelta
import json

from auth_handler import get_cj_api_auth

auth = get_cj_api_auth()
auth = (auth[0], auth[1])

base_url = 'http://api.cratejoy.com/v1/shipments/'


def check_response(response):
    if response > 200:
        return 'failed'


def get_shipments():
    response = requests.get(base_url)
    return response


def adjust_shipment_date(shipment, date):
    url = base_url + shipment + '/'
    date = str(date)
    response = requests.put(url, data=json.dumps({
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
        # why is this get returning entire shipment json blob?
        url = base_url + shipment + '?adjusted_ordered_at'
        response = requests.get(url, auth=auth)
        if response.status_code > 200:
            failed_shipments.append(shipment)
        elif response.status_code == 200:
            resp_dict = json.loads(response.content)
            date = resp_dict['adjusted_ordered_at']
            date = date.split("T")[0]
            date = datetime.datetime.strptime(date, "%Y-%m-%d")\
                + relativedelta(months=month)
            date = str(date)

            response = adjust_shipment_date(shipment, date)
            if response.status_code > 200:
                failed_shipments.append(shipment)

    return failed_shipments


def add_tracking(shipment_ids, tracking_numbers):
    shipment_ids = shipment_ids.split(',')
    tracking_numbers = tracking_numbers.split(',')
    failed_shipments = []

    date = str(datetime.datetime.now().isoformat())

    if shipment_ids.len != tracking_numbers.len:
        return 'Number of shipment IDs and tracking numbers do not match'
    else:
        for shipment_id in shipment_ids:
            for tracking_number in tracking_numbers:
                shipment_id = str(shipment_id)
                url = base_url + shipment_id
                response = requests.put(url, data=json.dumps({
                    'status': 'shipped',
                    'shipped_at': date,
                    'tracking_number': tracking_number
                    }), auth=auth)
                if response > 200:
                    failed_shipments.append(shipment_id)
            return failed_shipments


def change_product_request(shipment, product):
    url = base_url + shipment
    response = requests.put(url, data=json.dumps({

        }), auth=auth)
