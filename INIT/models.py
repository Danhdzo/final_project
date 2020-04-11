from INIT.__init__ import db, login_manager
from flask_login import UserMixin
from sqlalchemy import ForeignKey


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)


class Persona(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    age = db.Column(db.String(50), unique=False, nullable=False)
    address = db.Column(db.String(50), unique=False, nullable=False)
    city = db.Column(db.String(20), unique=False, nullable=False)
    state = db.Column(db.String(20), unique=False, nullable=False)
    zip = db.Column(db.String(20), unique=False, nullable=False)
    country = db.Column(db.String(20), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=False, nullable=False)
    bookings = db.relationship('Bookings', backref='persona')


class Hotel(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    address = db.Column(db.String(50), unique=False, nullable=False)
    city = db.Column(db.String(20), unique=False, nullable=False)
    state = db.Column(db.String(20), unique=False, nullable=False)
    zip = db.Column(db.String(20), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=False)
    website = db.Column(db.String(40), unique=False, nullable=False)
    rooms_avail = db.Column(db.Integer, unique=False, nullable=False)
    bookings = db.relationship('Bookings', backref='hotel')
    rooms = db.relationship('Rooms', backref='hotel')


class BookingStatus(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    status = db.Column(db.String(10), unique=False, nullable=False)
    description = db.Column(db.String(150), unique=False, nullable=False)
    active = db.Column(db.Boolean, unique=False, nullable=False)
    bookings = db.relationship('Bookings', backref='booking_status')


class Agents(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    code = db.Column(db.String(10), unique=False, nullable=False)
    bookings = db.relationship('Bookings', backref='agents')


class Bookings(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    date_from = db.Column(db.Date, unique=False, nullable=False)
    date_to = db.Column(db.Date, unique=False, nullable=False)
    room_count = db.Column(db.Integer, unique=False, nullable=False)
    adults = db.Column(db.Integer, unique=False, nullable=False)
    children = db.Column(db.Integer, unique=False, nullable=False)
    hotel_id = db.Column(db.Integer, ForeignKey(Hotel.id))
    agent_id = db.Column(db.Integer, ForeignKey(Agents.id))
    persona_id = db.Column(db.Integer, ForeignKey(Persona.id))
    booking_status_id = db.Column(db.Integer, ForeignKey(BookingStatus.id))
    rooms_booked = db.relationship('RoomsBooked', backref='bookings')


class RoomType(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    type = db.Column(db.String(10), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    active = db.Column(db.Boolean, unique=False, nullable=False)
    rooms = db.relationship('Rooms', backref='Rooms')


class Rooms(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    floor = db.Column(db.String(2), unique=False, nullable=False)
    room_num = db.Column(db.String(3), unique=False, nullable=False)
    description = db.Column(db.String(150), unique=False, nullable=False)
    hotel_id = db.Column(db.Integer, ForeignKey(Hotel.id))
    room_type_id = db.Column(db.Integer, ForeignKey(RoomType.id))
    rooms_booked = db.relationship('RoomsBooked', backref='rooms')
    payments = db.relationship('Payments', backref='rooms')
    rates = db.relationship('Rates', backref='rooms')


class PaymentType(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    payment_type = db.Column(db.String(10), unique=True, nullable=False)
    active = db.Column(db.Boolean, unique=False, nullable=False)
    card_num = db.Column(db.String(12), unique=True, nullable=False)
    card_cvv = db.Column(db.String(3), unique=False, nullable=False)
    payments = db.relationship('Payments', backref='payment_type')


class PaymentStatus(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    status = db.Column(db.Boolean, unique=False, nullable=False)
    description = db.Column(db.String(150), unique=False, nullable=False)
    active = db.Column(db.Boolean, unique=False, nullable=False)
    payments = db.relationship('Payments', backref='payment_status')


class Payments(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Date = db.Column(db.Date, unique=True, nullable=False)
    pay_status_id = db.Column(db.Integer, ForeignKey(PaymentStatus.id))
    pay_type_id = db.Column(db.Integer, ForeignKey(PaymentType.id))
    rooms_id = db.Column(db.Integer, ForeignKey(Rooms.id))


class RateType(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    rate_type = db.Column(db.String(10), unique=False, nullable=True)
    description = db.Column(db.String(150), unique=False, nullable=True)
    active = db.Column(db.Boolean, unique=False, nullable=False)
    rates = db.relationship('Rates', backref='rate_type')


class Rates(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    rate = db.Column(db.Integer, unique=False, primary_key=False)
    month = db.Column(db.Integer, unique=False, primary_key=False)
    rooms_id = db.Column(db.Integer, ForeignKey(Rooms.id))
    rate_type_id = db.Column(db.Integer, ForeignKey(RateType.id))


class RoomsBooked(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    bookings_id = db.Column(db.Integer, ForeignKey(Bookings.id))
    rooms_id = db.Column(db.Integer, ForeignKey(Rooms.id))


def __repr__(self):
    return f"User('{self.username}')"
