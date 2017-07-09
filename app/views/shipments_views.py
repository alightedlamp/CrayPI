import flask

from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app
from ..forms import GetShipmentsForm, MoveShipmentForm, AddTrackingForm


@app.route('/shipments')
def shipments():
    user = flask.g.user
    return flask.render_template('shipments.html',
                                 title='Shipments',
                                 user=user)


@app.route('/shipments/move')
def move_shipments():
    user = flask.g.user
    form = MoveShipmentForm()
    return flask.render_template('shipments_move.html',
                                 title='Shipments - Adjust Dates',
                                 form=form,
                                 user=user)

@app.route('/shipments/tracking')
def add_tracking():
    user = flask.g.user
    form = AddTrackingForm()
    return flask.render_template('shipments_tracking.html',
                                 title='Shipments - Add Tracking',
                                 form=form,
                                 user=user)

