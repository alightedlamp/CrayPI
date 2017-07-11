import flask

from flask import flash, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app
from ..forms import GetShipmentsForm, MoveShipmentForm, AddTrackingForm

import handlers.shipments_handler


@app.route('/shipments')
@app.route('/shipments', methods=['GET'])
def shipments():
    user = flask.g.user
    form = GetShipmentsForm()
    return flask.render_template('shipments.html',
                                 title='Shipments',
                                 form=form,
                                 user=user)


@app.route('/shipments/move', methods=['GET', 'POST'])
def move_shipments():
    user = flask.g.user
    form = MoveShipmentForm()

    if form.validate_on_submit():
        shipment_id = form.shipment_id.data
        date = str(form.shipment_date.data)
        response = handlers.shipments_handler.adjust_date(shipment_id, date)

        if response.status_code == '200':
            message_success = u'Shipment ' + shipment_id + u' moved to ' + date
            flash(message_success, 'success')
        else:
            flash('Shipment could not be moved', 'error')

        return redirect(url_for('shipments'))

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

