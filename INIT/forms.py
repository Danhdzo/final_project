from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Persona_form(FlaskForm):
    FirstName = StringField('FirstName',
                            validators=[DataRequired()])
    LastName = StringField('LastName',
                           validators=[DataRequired()])
    Age = StringField('Age',
                      validators=[DataRequired()])
    Address = StringField('Address',
                          validators=[DataRequired()])
    City = StringField('City',
                       validators=[DataRequired()])
    State = StringField('State',
                        validators=[DataRequired()])
    ZIP = StringField('ZIP',
                      validators=[DataRequired()])
    Country = StringField('Country',
                          validators=[DataRequired()])
    PhoneNum = StringField('PhoneNum',
                           validators=[DataRequired()])
    Email = StringField('Email',
                        validators=[DataRequired(), Email()])
    Submit = SubmitField('Create Client')


class Hotel_form(FlaskForm):
    Name = SelectField(u'Hotel Name', hotels=['Anaheim', 'Tokyo'])
    # if Name == "Anaheim":
    #     hAddress = "1150 West, Magic Way"
    #     hCity = "Anaheim"
    #     hState = "California"
    #     hZIP = "54321"
    #     hPhoneNum = "17147786600"
    #     Website = "https://disneyland.disney.go.com/es-us/hotels/disneyland-hotel/"
    #
    # elif Name == "Tokyo":
    #     hAddress = "29-1 Maihama, Urayasu, Chiba 279-0031"
    #     hCity = "Tokyo"
    #     hState = "Kanto"
    #     hZIP = "98765"
    #     hPhoneNum = "81473053333"
    #     Website = "https://www.tokyodisneyresort.jp/en/info/"

    Submit = SubmitField('Submit')


class Booking_form(FlaskForm):
    DateFrom = DateField(u'DateFrom', validators=[DataRequired()], format='%d-%m-%Y')
    DateTo = DateField(u'DateTo', validators=[DataRequired()], format='%d-%m-%Y')
    Adults = StringField(u'Adults', validators=[DataRequired()])
    Children = StringField(u'Children', validators=[DataRequired()])
    RoomType = SelectField(u'RoomType', RoomType=['single', 'double', 'triple', 'suit', 'master'])
    Agent = StringField('Code', validators=[DataRequired()])
    RoomCount= SelectField(u'Amount of rooms to reserve', RoomCount=['1','2','3','4','5','6','7','8','9','10'])
    Submit = SubmitField('Submit')

class Payments(FlaskForm):
    ServicePaid=BooleanField('Paid')
    paymentType=SelectField(u'Payment Type', PaymentType=['Debit', 'Credit'])

class Confirmation_form(FlaskForm):
    Submit = SubmitField('Submit')
# class Bookings(FlaskForm):
