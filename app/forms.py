from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class GetShipmentsForm(Form):
    search_term = StringField(u'Subscription ID', validators=[DataRequired()])


class MoveShipmentForm(Form):
    shipment_id = TextAreaField(u'Shipment ID(s)', validators=[DataRequired()], id='shipment-id')

    options = RadioField(u'Type', choices=[('by-date', 'By date'), ('by-month', 'By month')], coerce=unicode)

    shipment_date = DateField(u'Shipment Date', id='shipment-date')
    shipments_month_change = SelectField(u'Month Adjustment', coerce=int, id='shipment-month-choice')

    submit = SubmitField(id='submit-btn')


class AddTrackingForm(Form):
    shipment_ids = TextAreaField(u'Shipment IDs', validators=[DataRequired()])
    tracking_numbers = TextAreaField(u'Tracking Numbers', validators=[DataRequired()])
    submit = SubmitField()