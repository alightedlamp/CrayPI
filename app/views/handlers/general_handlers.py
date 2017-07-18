import requests
import datetime
from dateutil.relativedelta import relativedelta
import json

from auth_handler import get_cj_api_auth

auth = get_cj_api_auth()
auth = (auth[0], auth[1])

base_url = 'http://api.cratejoy.com/v1/'


def get_date_key(endpoint):
    if endpoint == 'shipments':
        return 'adjusted_ordered_at'
    elif endpoint == 'subscriptions':
        return 'end_date'


def get_msg(failures, endpoint):
    if failures:
        failures = str(failures)
        return 'Some ' + endpoint + ' adjustments failed: ' + failures
    else:
        return 'Success!'


def adjust_dates(ids, date, endpoint):
    date_key = get_date_key(endpoint)
    ids = ids.split(',')
    date = str(date)
    failures = []

    for _id in ids:
        url = base_url + endpoint + '/' + _id + '/'
        response = requests.put(url, data=json.dumps({
            date_key: date
        }), auth=auth)

        if response.status_code > 200:
            failures.append(_id)

    return get_msg(failures, endpoint)


def adjust_months(ids, months, endpoint):
    date_key = get_date_key(endpoint)
    ids = ids.split(',')
    failures = []

    for _id in ids:
        url = base_url + endpoint + '/' + _id + '/'
        response = requests.get(url, auth=auth)

        if response.status_code > 200:
            failures.append(_id)
        elif response.status_code == 200:
            response = json.loads(response.content)
            date = response[date_key]
            date = date.split('T')[0]
            date = datetime.datetime.strptime(date, '%Y-%m-%d') + relativedelta(months=months)
            date = str(date)

            response = requests.put(url, data=json.dumps({
                date_key: date
                }), auth=auth)

            if response.status_code > 200:
                failures.append(_id)

    return get_msg(failures, endpoint)
