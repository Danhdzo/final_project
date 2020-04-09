from flask import flash, render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from INIT.forms import LoginForm, Persona_form, Hotel_form, Booking_form
from INIT.__init__ import app, db, bcrypt
from INIT.models import User, Persona, Hotel, Bookings, Rooms, RoomType, Agents


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/booking")
def booking():
    # Get hotel data from DB
    #
    Hotelform = Hotel_form()
    Hotelform.Name.hotels = [(hotel.Name) for hotel in Hotel.query.all()]
    # # Get if rooms available
    # Bookingform = Booking_form()
    #
    # if Booking_form.validate_on_submit():
    #     booking = Bookings(DateFrom=Booking_form.DateFrom.data, DateTo=Booking_form.DateTo.data,
    #                        Adults=Booking_form.Adults.data,
    #                        Children=Booking_form.Children.data, RoomType=Booking_form.RoomType.data,
    #                        AgentID=Booking_form.Agent.data,
    #                        RoomCount=Booking_form.RoomCount.data)
    # vacancy = db.query(Rooms, Bookings, Hotel, RoomType) \
    #     .join(Bookings) \
    #     .join(Hotel) \
    #     .filter_by(Booking_form.RoomType.data) \
    #     .filter_by(hotel) \
    #     .filter_by(Rooms.Room_avail).first()
    #
    # if Booking_form.RoomCount <= vacancy:
    #     vacancy -= Booking_form.RoomCount
    #     next_page = request.args.get('next')
    #     return redirect(next_page) if next_page else redirect(url_for('confirmation'))
    #
    # else:
    #     flash('Rooms not available, please choose another type of room or select a different hotel', 'danger')

    return render_template('booking.html', title='Booking', form=Hotel_form)


@app.route("/persona", methods=['GET', 'POST'])
# @login_required
def persona():
    form = Persona_form()
    if form.validate_on_submit():
        client = Persona(FirstName=form.FirstName.data, LastName=form.LastName.data, Age=form.Age.data,
                         Address=form.Address.data,
                         City=form.City.data, State=form.State.data, ZIP=form.ZIP.data, Country=form.Country.data,
                         PhoneNum=form.PhoneNum.data,
                         Email=form.Email.data)

        check_client = Persona.query.filter_by(Email=form.Email.data).first()
        print(check_client)
        if check_client is None:
            db.session.add(client)
            db.session.commit()

            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect(url_for('booking'))
        else:
            flash('Client data already exist, please enter different data', 'danger')
    return render_template('persona.html', title='Client', form=form)


# return redirect(url_for('login'))

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('persona'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('persona'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


# @app.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
