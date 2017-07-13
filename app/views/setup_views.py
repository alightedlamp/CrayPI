import flask

from flask import flash, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app


@app.route('/setup', methods=['POST'])
def first_time_setup():
    # where user will input their API creds


@app.route('/setup/user', methods=['GET', 'POST'])
def user_setup():
    # where admin can set up a main admin