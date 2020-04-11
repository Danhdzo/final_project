from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, Email

from INIT.models import Hotel, RoomType, Bookings, PaymentType, Rates


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
    name = SelectField('Hotel Name',  validators=[DataRequired()] ,choices=hotel_list)
    # date_from field
    date_from = DateField('Date From (dd-mm-yyyy)', validators=[DataRequired()], format='%d-%m-%Y')
    # date_to field
    date_to = DateField('Date To (dd-mm-yyyy)', validators=[DataRequired()], format='%d-%m-%Y')
    # adults dropdown
    adult_list = []
    for i in range(1, 11):
        adult_list.append((i, i))
    adults = SelectField('Adults',validators=[DataRequired()] , choices=adult_list)
    # children dropdown
    child_list = []
    for i in range(0, 11):
        child_list.append((i, i))
    children = SelectField('Children', validators=[DataRequired()] ,choices=child_list)
    # room type dropdown
    type_list = []
    for rt in RoomType.query.all():
        type_list.append((rt.id, rt.type))
    room_type = SelectField('RoomType',validators=[DataRequired()] , choices=type_list)
    # agent field
    agent = StringField('Code')
    # room count dropdown
    count_list = []
    for i in range(1, 11):
        count_list.append((i, i))
    room_count = SelectField('Amount of rooms to reserve',validators=[DataRequired()] ,
                             choices=count_list)
    # submit
    submit = SubmitField('Reserve')


class Payments_form(FlaskForm):
    #count of days
    global c
    #count of months
    global r
    #sum of rates of monthly
    global rates_times_days
    #dicount applied
    global disc_rates
    desc = Booking_form.agent.data
    for date in range(Booking_form.date_from.data,Booking_form.date_to.data):
        month = date.month
        if month==month[date+1]:
            c+=1
        else:
            rates_times_days = []
            r+=1
            for row in Rates.query.filter_by(month).with_entities(Rates.rate).first():
                rates_times_days[r] = (c + 1) * int(row)
                if desc == "MILITAR" or desc == "AMIGUIS" or desc == "UTE":
                    rates_times_days[r]=rates_times_days[r]*(1-(1/10))
                c = 0
    #sum of rates
    total_rate=0
    for rate in rates_times_days:
        total_rate=total_rate+rates_times_days[r]





    #payments
    pay_type_list=[]
    for p in range(0,2):
        pay_type_list.append((p,p))
    payment_type = SelectField('Payment Type', validators=[DataRequired], choices=pay_type_list)
    card_number = StringField('Card Number',validators=[DataRequired])
    sec_num= PasswordField('CVV', validators=[DataRequired])
    submit = SubmitField('Submit')


