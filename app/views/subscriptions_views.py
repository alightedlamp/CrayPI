import flask

from flask import flash, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app
from ..forms import ChangeRenewal

import handlers.subscriptions_hander


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
            response = handlers.subscriptions_handler.adjust_by_date(subscriptions, date)
        elif form.options.data == 'by-month':
            month = form.renewal_month_change.data
            response = handlers.subscriptions_handler.adjust_by_month(subscriptions, month)

        if response:
            flash('Renewal dates could not be changed: ' + str(response), 'error')
        else:
            flash('Renewals changed!', 'success')

        return redirect(url_for('change_renewal'))

    return flask.render_template('move_renewals.html',
                                 title='Subscriptionss - Adjust Renewals',
                                 form=form,
                                 options=options,
                                 user=user)
