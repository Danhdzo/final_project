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
    FirstName = db.Column(db.String(50), unique=False, nullable=False)
    LastName = db.Column(db.String(50), unique=False, nullable=False)
    Age = db.Column(db.String(50), unique=False, nullable=False)
    Address = db.Column(db.String(50), unique=False, nullable=False)
    City = db.Column(db.String(20), unique=False, nullable=False)
    State = db.Column(db.String(20), unique=False, nullable=False)
    ZIP = db.Column(db.String(20), unique=False, nullable=False)
    Country = db.Column(db.String(20), unique=False, nullable=False)
    PhoneNum = db.Column(db.String(20), unique=False, nullable=False)
    Email = db.Column(db.String(30), unique=False, nullable=False)
    # bookings = db.relationship('Bookings', backref='Bookings.Persona', lazy='joined')


class Hotel(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Name = db.Column(db.String(50), unique=False, nullable=False)
    hAddress = db.Column(db.String(50), unique=False, nullable=False)
    hCity = db.Column(db.String(20), unique=False, nullable=False)
    hState = db.Column(db.String(20), unique=False, nullable=False)
    hZIP = db.Column(db.String(20), unique=False, nullable=False)
    hPhoneNum = db.Column(db.String(20), unique=False, nullable=False)
    Website = db.Column(db.String(40), unique=False, nullable=False)
    Room_avail = db.Column(db.Integer, unique=False, nullable=False)
    # bookings = db.relationship('Bookings', backref='Bookings.Hotel', lazy='joined')
    # rooms = db.relationship('Rooms', backref='Rooms.Hotel', lazy='joined')


class BookingStatus(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Status = db.Column(db.String(10), unique=False, nullable=False)
    Description = db.Column(db.String(150), unique=False, nullable=False)
    Active = db.Column(db.Boolean, unique=False, nullable=False)

class Agents(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Code = db.Column(db.String(10), unique=False, nullable=False)
    # bookings = db.relationship('Bookings', backref='Bookings.Agents', lazy='joined')

class Bookings(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    DateFrom = db.Column(db.Date, unique=False, nullable=False)
    DateTo = db.Column(db.Date, unique=False, nullable=False)
    RoomCount = db.Column(db.Integer, unique=False, nullable=False)
    Adults = db.Column(db.Integer, unique=False, nullable=False)
    Children = db.Column(db.Integer, unique=False, nullable=False)
    hotelID = db.Column(db.Integer, ForeignKey(Hotel.id))
    agentID = db.Column(db.Integer, ForeignKey(Agents.id))
    personaID = db.Column(db.Integer, ForeignKey(Persona.id))
    BookingStatusID = db.Column(db.Integer, ForeignKey(BookingStatus.id))
    H_id = db.relationship('Hotel', foreign_keys=[hotelID])
    A_id = db.relationship('Agents', foreign_keys=[agentID])
    P_id = db.relationship('Persona', foreign_keys=[personaID])
    BS_id = db.relationship('BookingStatus', foreign_keys=[BookingStatusID])
    # roomsBooked = db.relationship('RoomsBooked', backref='RoomsBooked.Booking', lazy='joined')

class RoomType(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    RType = db.Column(db.String(10), unique=False, nullable=False)
    RTDescription = db.Column(db.String(120), unique=False, nullable=False)
    RTActive = db.Column(db.Boolean, unique=False, nullable=False)
    # rooms = db.relationship('Rooms', backref='Rooms.RoomType', lazy='joined')

class Rooms(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Floor = db.Column(db.String(2), unique=False, nullable=False)
    RoomNum = db.Column(db.String(3), unique=False, nullable=False)
    Description = db.Column(db.String(150), unique=False, nullable=False)
    hotelID = db.Column(db.Integer, ForeignKey(Hotel.id))
    roomTypeID = db.Column(db.Integer, ForeignKey(RoomType.id))
    H_id = db.relationship('Hotel', foreign_keys=[hotelID])
    # rates = db.relationship('Rates', backref='Rates.Rooms', lazy='joined')
    # roomsBooked = db.relationship('RoomsBooked', backref='RoomsBooked.Rooms', lazy='joined')
    # payments = db.relationship('Payments', backref='Payments.Rooms', lazy='joined')


class RateType(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    RType = db.Column(db.String(10), unique=False, nullable=True)
    RaTDescription = db.Column(db.String(150), unique=False, nullable=True)
    RaTActive = db.Column(db.Boolean, unique=False, nullable=False)
    # rates = db.relationship('Rates', backref='Rate.RateType', lazy='joined')


class Rates(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Rate = db.Column(db.Integer, unique=False, primary_key=False)
    Month = db.Column(db.Integer, unique=False, primary_key=False)
    RoomsID = db.Column(db.Integer, ForeignKey(Rooms.id))
    RateTypeID = db.Column(db.Integer, ForeignKey(RateType.id))



class RoomsBooked(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    BookingsID = db.Column(db.Integer, ForeignKey(Bookings.id))
    RoomID = db.Column(db.Integer, ForeignKey(Rooms.id))
    RateID = db.Column(db.Integer, ForeignKey(Rates.id))
    Ro_id = db.relationship('Hotel', foreign_keys=[RoomID])
    Ra_id = db.relationship('Hotel', foreign_keys=[RateID])

class PaymentStatus(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    Status = db.Column(db.Boolean, unique=False, nullable=False)
    Description = db.Column(db.String(150), unique=False, nullable=False)
    Active = db.Column(db.Boolean, unique=False, nullable=False)
    # payments = db.relationship('Payments', backref='Payments.PaymentStatus', lazy='joined')


class PaymentType(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    PaymentType = db.Column(db.String(10), unique=True, nullable=False)
    Active = db.Column(db.Boolean, unique=False, nullable=False)
    # payments = db.relationship('Payments', backref='Payments.PaymentType', lazy='joined')


class Payments(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    RoomID = db.Column(db.Integer, ForeignKey(Rooms.id))
    Date = db.Column(db.Date, unique=True, nullable=False)
    ServicePaid = db.Column(db.Boolean, nullable=False)
    PaymentStatusID = db.Column(db.Integer, ForeignKey(PaymentStatus.id))
    PaymentTypeID = db.Column(db.Integer, ForeignKey(PaymentType.id))
    PS_id = db.relationship('Hotel', foreign_keys=[PaymentStatusID])
    PT_id = db.relationship('Hotel', foreign_keys=[PaymentTypeID])


def __repr__(self):
    return f"User('{self.username}')"
