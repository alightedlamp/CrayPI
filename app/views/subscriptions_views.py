import flask

from flask import flash, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app
from ..forms import ChangeRenewal, ReactivateSubscription, AdjustGiftInfo
from handlers import subscriptions_handler

import handlers.general_handlers


@app.route('/subscriptions/renewal', methods=['GET', 'POST'])
def change_renewal():
    user = flask.g.user
    form = ChangeRenewal()

    form.renewal_month_change.choices = [(i, i) for i in range(-6, 7) if i != 0]
    options = list(form.options)

    if form.is_submitted():
        subscriptions = form.subscription_ids.data
        if form.options.data == 'by-date':
            date = form.renewal_date.data
            response = handlers.general_handlers.adjust_dates(subscriptions, date, 'subscriptions')
        elif form.options.data == 'by-month':
            month = form.renewal_month_change.data
            response = handlers.general_handlers.adjust_months(subscriptions, month,'subscriptions')

        flash(response)

        return redirect(url_for('change_renewal'))

    return flask.render_template('move_renewals.html',
                                 title='Subscriptions - Adjust Renewals',
                                 form=form,
                                 options=options,
                                 user=user)


@app.route('/subscriptions/reactivate', methods=['GET', 'POST'])
def reactivate_subscriptions():
    user = flask.g.user
    form = ReactivateSubscription()

    if form.is_submitted():
        subscriptions = form.subscription_ids.data
        response = subscriptions_handler.reactivate_subscriptions(subscriptions)

        flash(response)

        return redirect(url_for('reactivate_subscriptions'))

    return flask.render_template('reactivate_subscriptions.html',
                                 title='Subscriptions - Reactivate',
                                 form=form,
                                 user=user)


@app.route('/subscriptions/adjust_gift_info', methods=['GET', 'POST'])
def adjust_gift_info():
    user = flask.g.user
    form = AdjustGiftInfo()
    form.gift_status.choices = [('t', 'True'), ('f', 'False')]

    if form.is_submitted():
        order_id = form.order_id.data
        gift_status = form.gift_status.data
        gift_message = form.gift_message.data

        response = subscriptions_handler.adjust_gift_info(order_id, gift_status, gift_message)

        flash(response)

        return redirect(url_for('adjust_gift_info'))

    return flask.render_template('adjust_gift_info.html',
                                 title='Subscriptions - Adjust Gift Info',
                                 form=form,
                                 user=user)
