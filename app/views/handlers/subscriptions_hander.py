import requests
import datetime
import json

from auth_handler import get_cj_api_auth

auth = get_cj_api_auth()
auth = (auth[0], auth[1])

base_url = 'http://api.cratejoy.com/v1/subscriptions/'


def adjust_renewal(subscription, date):
    # do a thing


def reactivate(subscription):
    # do a thing


def add_coupons(subscription, coupon):
    # do a thing


def adjust_gift_info(subscription, options):
    # do a thing


def create_order():
    # do a thing
