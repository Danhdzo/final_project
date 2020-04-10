from INIT import db
from INIT.models import Hotel, Rooms, RoomType, BookingStatus, Agents, RateType, Rates, PaymentStatus, PaymentType, \
    Bookings

# hotel
Name = ['Anaheim', 'Tokyo']
Address = ['1150 West, Magic Way', '29-1 Maihama, Urayasu, Chiba 279-0031']
City = ['Anaheim city 123', 'Tokyo city 123']
State = ['California', 'Kanto']
Zip = ['54321', '98765']
Phone = ['1714-778-6600', '8147-305-3333']
Website = ['https://disneyland.disney.go.com/es-us/hotels/disneyland-hotel/',
           'https://www.tokyodisneyresort.jp/en/info/']

for nam, hadrss, hct, hstat, hz, hphon, site in zip(Name, Address, City, State, Zip, Phone, Website):
    db.session.add(Hotel(name=nam, address=hadrss, city=hct, state=hstat, zip=hz, phone=hphon, website=site,
                         rooms_avail=210))
    db.session.commit()

# Booking Status
Status = ['Occupied', 'Free', 'Cleaning', 'Repairing', 'Closed']
Description = ['Guests on the room', 'Free of guests', 'Maid in the room', 'Plumber or else', 'Ghost or other']
for bstat, bdesc in zip(Status, Description):
    db.session.add(BookingStatus(status=bstat, description=bdesc, active=0))
    db.session.commit()

# Agents
Code = ['MILITAR', 'UTE', 'AMIGUIS']
for cody in Code:
    db.session.add(Agents(code=cody))
    db.session.commit()

# Bookings

# RoomType
RType = ['single', 'double', 'junior', 'master']
RTDescription = ['single bed', 'couple of beds', 'single and queen size bed', '2 queen size beds']
for rtaip, rtdesc in zip(RType, RTDescription):
    db.session.add(RoomType(type=rtaip, description=rtdesc, active=0))
    db.session.commit()

# Rooms
Floor = []
RoomNum = []
hotel = []
for f in range(1, 8):
    for r in range(1, 31):
        # Description
        db.session.add(Rooms(floor=str(f), room_num=str(r), description='Room Ready', hotel_id=1))
        db.session.add(Rooms(floor=str(f), room_num=str(r), description='Room Ready', hotel_id=2))
        db.session.commit()

# RoomsBooked

# RateType
RType = ['Regular', 'High Season', 'Low Season']
RaTDescription = ['Regular Rate', 'Higher Rate due to low vacancy',
                  'Lower rate due to high vacancy']
for rtaip, ratdesc in zip(RType, RaTDescription):
    db.session.add(RateType(rate_type=rtaip, description=ratdesc, active=0))
    db.session.commit()

# Rates
for month in range(1, 13):
    if month <= 3 or month >= 11:
        rate = 800
    elif month == 4 or month >= 9:
        rate = 1000
    else:
        rate = 1200
    db.session.add(Rates(rate=rate, month=month))

# Payment Type
PaymentTypes = ['Debit', 'Credit', 'Paypal', 'Cash']
for payment in PaymentTypes:
    PaymentT_data = PaymentType(payment_type=payment, active=0)

# Payment Status
PaymentStat = ['Completed', 'Cancelled', 'In Progress']
Description = ['Transaction Successful', 'Transaction Aborted', 'Making Transaction']
for paystat, desc in zip(PaymentStat, Description): PaymentStatus(status=paystat, description=desc, active=0)

# Payments
