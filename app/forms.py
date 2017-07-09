from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class GetShipmentsForm(Form):
    subscription_id = StringField(u'Subscription ID', validators=[DataRequired()])


class MoveShipmentForm(Form):
    shipment_id = StringField(u'Shipment ID', validators=[DataRequired()])
    shipment_date = DateField(u'Shipment Date', validators=[DataRequired()])
    submit = SubmitField()


class AddTrackingForm(Form):
    shipment_ids = TextAreaField(u'Shipment IDs', validators=[DataRequired()])
    tracking_numbers = TextAreaField(u'Tracking Numbers', validators=[DataRequired()])
    submit = SubmitField()