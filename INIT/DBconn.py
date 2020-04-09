from INIT import db
from INIT.models import Hotel, Rooms, RoomType, BookingStatus, Agents, RateType, Rates, PaymentStatus, PaymentType

# hotel
Name = ['Anaheim', 'Tokyo']
hAddress = ['1150 West, Magic Way', '29-1 Maihama, Urayasu, Chiba 279-0031']
hCity = ['Anaheim city 123', 'Tokyo city 123']
hState = ['California', 'Kanto']
hZIP = ['54321', '98765']
hPhoneNum = ['1714-778-6600', '8147-305-3333']
Website = ['https://disneyland.disney.go.com/es-us/hotels/disneyland-hotel/',
           'https://www.tokyodisneyresort.jp/en/info/']

for nam, hadrss, hct, hstat, hz, hphon, site in zip(Name, hAddress, hCity, hState, hZIP, hPhoneNum, Website):
    db.session.add(Hotel(Name=nam, hAddress=hadrss, hCity=hct, hState=hstat, hZIP=hz, hPhoneNum=hphon, Website=site,
                         Room_avail=210))
    db.session.commit()

# Booking Status
Status = ['Occupied', 'Free', 'Cleaning', 'Repairing', 'Closed']
Description = ['Guests on the room', 'Free of guests', 'Maid in the room', 'Plumber or else', 'Ghost or other']
for bstat, bdesc in zip(Status, Description):
    db.session.add(BookingStatus(Status=bstat, Description=bdesc, Active=0))
    db.session.commit()

# Agents
Code = ['MILITAR', 'UTE', 'AMIGUIS']
for cody in Code:
    db.session.add(Agents(Code=cody))
    db.session.commit()

# Bookings

# RoomType
RType = ['single', 'double,', 'junior', 'master']
RTDescription = ['single bed', 'couple of beds', 'single and queen size bed', '2 queen size beds']
for rtaip, rtdesc in zip(RType, RTDescription):
    db.session.add(RoomType(RType=rtaip, RTDescription=rtdesc, RTActive=0))
    db.session.commit()

# Rooms
Floor = []
RoomNum = []
hotel = []
for f in range(1, 8):
    for r in range(1, 31):
        # Description
        db.session.add(Rooms(Floor=str(f), RoomNum=str(r), Description='Room Ready', hotelID=1))
        db.session.add(Rooms(Floor=str(f), RoomNum=str(r), Description='Room Ready', hotelID=2))
        db.session.commit()

# RoomsBooked

# RateType
RType = ['Regular', 'High Season', 'Low Season']
RaTDescription = ['Ragular Rate', 'Higher Rate due to low vacancy',
                  'Lower rate due to high vacancy']
for rtaip, ratdesc in zip(RType, RaTDescription):
    db.session.add(RateType(RType=rtaip, RaTDescription=ratdesc, RaTActive=0))
    db.session.commit()

# Rates
for month in range(1, 13):
    if month <= 3 or month >= 11:
        rate = 800
    elif month == 4 or month >= 9:
        rate = 1000
    else:
        rate = 1200
    db.session.add(Rates(Rate=rate, Month=month))

# Payment Type
PaymentTypes = ['Debit', 'Credit', 'Paypal', 'Cash']
for payment in PaymentTypes:
    PaymentT_data = PaymentType(PaymentType=payment, Active=0)

# Payment Status
PaymentStat = ['Completed', 'Cancelled', 'In Progress']
Description = ['Transaction Successful', 'Transaction Aborted', 'Making Transaction']
for paystat, desc in zip(PaymentStat, Description): PaymentStatus(Status=paystat, Description=desc, Active=0)

# Payments
