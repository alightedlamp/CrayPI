import requests
import datetime
from dateutil.relativedelta import relativedelta
import json

from auth_handler import get_cj_api_auth

auth = get_cj_api_auth()
auth = (auth[0], auth[1])

base_url = 'http://api.cratejoy.com/v1/shipments/'


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

