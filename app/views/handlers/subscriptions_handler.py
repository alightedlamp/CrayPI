import requests
import datetime
import json

from general_handlers import get_msg
from auth_handler import get_cj_api_auth

auth = get_cj_api_auth()
auth = (auth[0], auth[1])

base_url = 'http://api.cratejoy.com/v1/subscriptions/'


def reactivate_subscriptions(subscriptions):
    subscriptions = subscriptions.split(',')
    failures = []

    for subscription in subscriptions:
        url = base_url + subscription + '/reactivate/'
        response = requests.put(url, auth=auth)

        if response > 200:
            failures.append(subscription)

    return get_msg(failures, 'subscription')


def adjust_gift_info(order_id, is_gift, gift_msg):
    url = 'http://api.cratejoy.com/v1/orders/' + order_id
    data = {}

    if is_gift:
        data['is_gift'] = is_gift
    if gift_msg:
        data['gift_message'] = gift_msg

    response = requests.put(url, data=data, auth=auth)

    if response > 200 | response < 200:
        return 'Order could not be updated'
    elif response == 200:
        return 'Order updated'


def change_autorenew(subscription, autorenew_status):
    url = base_url + subscription

    response = requests.post(url, data=json.dumps({
        'autorenew': autorenew_status
    }), auth=auth)


def add_coupons(subscriptions, coupon):
    subscriptions = subscriptions.split(',')
    failures = []

    for subscription in subscriptions:
        url = base_url + subscription + '/coupons/'
        response = requests.post(url, data=json.dumps({
            'coupon_id': coupon
        }), auth=auth)

        if response.status_code > 200:
            failures.append(subscription)

    return get_msg(failures, 'subscription coupon')
