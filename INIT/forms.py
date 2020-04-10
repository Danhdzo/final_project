from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, Email

from INIT.models import Hotel, RoomType, Bookings


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Persona_form(FlaskForm):
    name = StringField('First Name',
                       validators=[DataRequired()])
    last_name = StringField('last_name',
                            validators=[DataRequired()])
    age = StringField('Age',
                      validators=[DataRequired()])
    address = StringField('Address',
                          validators=[DataRequired()])
    city = StringField('City',
                       validators=[DataRequired()])
    state = StringField('State',
                        validators=[DataRequired()])
    zip = StringField('ZIP',
                      validators=[DataRequired()])
    country = StringField('Country',
                          validators=[DataRequired()])
    phone = StringField('Phone',
                        validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Create Guest')


class Booking_form(FlaskForm):
    # hotel dropdown
    hotel_list = []
    for h in Hotel.query.all():
        hotel_list.append((h.id, h.name))
    name = SelectField('Hotel Name', choices=hotel_list)
    # date_from field
    date_from = DateField('Date From (dd-mm-yyyy)', validators=[DataRequired()], format='%d-%m-%Y')
    # date_to field
    date_to = DateField('Date To (dd-mm-yyyy)', validators=[DataRequired()], format='%d-%m-%Y')
    # adults dropdown
    adult_list = []
    for i in range(1, 11):
        adult_list.append((i, i))
    adults = SelectField('Adults', choices=adult_list)
    # children dropdown
    child_list = []
    for i in range(0, 11):
        child_list.append((i, i))
    children = SelectField('Children', choices=child_list)
    # room type dropdown
    type_list = []
    for rt in RoomType.query.all():
        type_list.append((rt.id, rt.type))
    room_type = SelectField('RoomType', choices=type_list)
    # agent field
    agent = StringField('Code')
    # room count dropdown
    count_list = []
    for i in range(1, 11):
        count_list.append((i, i))
    room_count = SelectField('Amount of rooms to reserve',
                             choices=count_list)
    # submit
    submit = SubmitField('Submit')


class Payments(FlaskForm):
    paid = BooleanField('Paid')
    payment_type = SelectField('Payment Type', PaymentType=['Debit', 'Credit', 'PayPal', 'Cash'])


class Confirmation_form(FlaskForm):
    Submit = SubmitField('Submit')
# class Bookings(FlaskForm):
