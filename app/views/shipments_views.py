import flask

from flask import flash, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app
from ..forms import MoveShipmentForm, AddTrackingForm

import handlers.shipments_handler


@app.route('/shipments')
@app.route('/shipments', methods=['GET'])
def shipments_page():
    user = flask.g.user
    return flask.render_template('shipments.html',
                                 title='Shipments',
                                 user=user)


@app.route('/shipments/move', methods=['GET', 'POST'])
def move_shipments():
    user = flask.g.user

    form = MoveShipmentForm()
    form.shipments_month_change.choices = [(i, i) for i in range(-6, 7) if i != 0]
    options = list(form.options)

    print form.shipment_id.data
    print form.shipments_month_change.data
    print form.validate_on_submit() # why you return false when there IS shipment ID data??

    if form.is_submitted():
        shipments = form.shipment_id.data
        if form.options.data == 'by-date':
            date = form.shipment_date.data
            failed = handlers.shipments_handler.adjust_by_date(shipments, date)
        elif form.options.data == 'by-month':
            month = form.shipments_month_change.data
            failed = handlers.shipments_handler.adjust_by_month(shipments, month)

        if failed:
            flash('Shipments could not be moved: ' + str(failed), 'error')
        else:
            flash('Shipments moved!', 'success')

        return redirect(url_for('shipments_page'))

    return flask.render_template('shipments_move.html',
                                 title='Shipments - Adjust Dates',
                                 form=form,
                                 options=options,
                                 user=user)


@app.route('/shipments/tracking', methods=['GET', 'POST'])
def add_tracking():
    user = flask.g.user
    form = AddTrackingForm()

    if form.is_submitted():
        shipments = form.shipment_ids.data
        tracking_numbers = form.tracking_numbers.data
        response = add_tracking(shipments, tracking_numbers)

        if response:
            flash('Tracking could not be added to shipments: ' + response, 'error')
        else:
            flash('Tracking added!')

    return flask.render_template('shipments_tracking.html',
                                 title='Shipments - Add Tracking',
                                 form=form,
                                 user=user)


@app.route('/shipments/change-product', methods=['GET', 'POST'])
def change_product():
    user = flask.g.user
    form = ChangeProductForm()