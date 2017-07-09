import flask

from flask import render_template, flash, redirect, session, url_for, request, g, session as flask_session
from flask.ext.login import login_user, logout_user, current_user, login_required

from app import app
from app.views.handlers.auth_handler import get_google_authorization_url


@app.route('/')
@app.route('/index')
def index():
    user = flask.g.user
    return flask.render_template('index.html',
                                 title='Home',
                                 user=user,
                                 auth_url=get_google_authorization_url())
