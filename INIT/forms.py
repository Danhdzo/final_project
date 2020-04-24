from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class Automate(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    number_of_users = StringField('Users to be created', validators=[DataRequired()])
    create= SubmitField('Create Users')

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
    name = StringField('Hotel Name', validators=[DataRequired()])
    # date_from field
    date_from_day = StringField('Day', validators=[DataRequired()])
    # date_from field
    date_from_month = StringField('Month', validators=[DataRequired()])
    # date_from field
    date_from_year = StringField('Year', validators=[DataRequired()])
    # date_to field
    date_to_day = StringField('Day', validators=[DataRequired()])
    # date_to field
    date_to_month = StringField('Month', validators=[DataRequired()])
    # date_to field
    date_to_year = StringField('Year', validators=[DataRequired()])
    # adults dropdown
    adults = StringField('Adults', validators=[DataRequired()])
    # children dropdown
    children = StringField('Children', validators=[DataRequired()])
    # room type dropdown
    room_type = StringField('RoomType', validators=[DataRequired()])
    # agent field
    agent = StringField('Code')
    # room count dropdown
    room_count = StringField('Amount of rooms to reserve',
                             validators=[DataRequired()])
    # submit
    submit = SubmitField('Reserve')
