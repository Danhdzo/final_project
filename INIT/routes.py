from flask import flash, render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from INIT.forms import LoginForm, Persona_form, Booking_form, Automate
from INIT.__init__ import app, db, bcrypt
from INIT.models import User, Persona, Hotel, Bookings, Rooms, RoomType, Agents, RoomsBooked, PaymentType, BookingStatus

global booking_data


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/automate", methods=['GET', 'POST'])
def automate():
    form = Automate()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            for user in form.number_of_users.data:
                import INIT.Automation

            return redirect(url_for('automate'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('automation.html', title='Automating Tool', form=form)


@app.route("/persona", methods=['GET', 'POST'])
# @login_required
def persona():
    form = Persona_form()
    if form.validate_on_submit():
        client = Persona(name=form.name.data, last_name=form.last_name.data, age=form.age.data,
                         address=form.address.data,
                         city=form.city.data, state=form.state.data, zip=form.zip.data, country=form.country.data,
                         phone=form.phone.data,
                         email=form.email.data)

        check_client = Persona.query.filter_by(email=form.email.data).first()
        if check_client is None:
            db.session.add(client)
            db.session.commit()
            next_page = request.args.get('submit')
            return redirect(next_page) if next_page else redirect(url_for('booking'))
        else:
            flash('Client data already exist, please enter different data', 'danger')
    return render_template('persona.html', title='Client', form=form)


@app.route("/booking", methods=['GET', 'POST'])
def booking():
    form = Booking_form()
    c = 0
    if form.validate_on_submit():
        full_room = []
        for h in Hotel.query.all():
            if form.name.data == h.name:
                Bookings(hotel_id=h.id)
            else:
                flash('No hotel with that name', 'danger')
        for a in Agents.query.all():
            if form.agent.data == a.code:
                Bookings(agent_id=a.id)
        p = Persona.query.order_by(Persona.id.desc()).first()
        Bookings(persona_id=p.id)

        booking = Bookings(date_from_day=form.date_from_day.data,
                           date_from_month=form.date_from_month.data, date_from_year=form.date_from_year.data,
                           date_to_day=form.date_to_day.data, date_to_month=form.date_to_month.data,
                           date_to_year=form.date_to_year.data,
                           adults=form.adults.data, children=form.children.data, room_count=form.room_count.data)

        # date validation
        if int(form.date_to_year.data) >= int(form.date_from_year.data) and int(form.date_to_month.data) >= int(
                form.date_from_month.data):
            # room vacancy per date
            for room in Bookings.query.all():
                if room.rooms_booked == True:
                    full_room.append(room.id)
                    for full in full_room:
                        if full.room_avail >= form.room_count.data:

                            db.session.add(booking)
                            db.session.commit()
        else:
            flash('Date not valid, please try again', 'danger')
    #             flash('There\'s not enough vacancy', 'danger')
    # else:
    #     db.session.add(booking)
    #     db.session.add(agent)
    #     db.session.add(room_type)
    #     db.session.commit()
    flash('Added correctly', 'danger')
    return redirect(url_for('persona'))


    return render_template('booking.html', title='Booking', form=form)


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
