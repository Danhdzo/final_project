from flask import flash, render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from INIT.forms import LoginForm, Persona_form, Booking_form, Payments_form
from INIT.__init__ import app, db, bcrypt
from INIT.models import User, Persona, Hotel, Bookings, Rooms, RoomType, Agents, RoomsBooked, PaymentType


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


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
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('booking'))
        else:
            flash('Client data already exist, please enter different data', 'danger')
    return render_template('persona.html', title='Client', form=form)


@app.route("/booking", methods=['GET', 'POST'])
def booking():
    form = Booking_form()
    if form.validate_on_submit():
        booking = Bookings(date_from=form.date_from.data, date_to=form.date_to.data, adults=form.adults.data,
                           children=form.children.data, room_count=form.room_count.data)
        type = RoomType(type=form.room_type)
        agent = Agents(code=form.agent)
        for row in Rooms.query.with_entities(Rooms.id):
            for rooms_booked in RoomsBooked.query.with_entities(RoomsBooked.rooms_id):
                if row != rooms_booked:
                    c = +1
                    x = c - form.room_count.data
                    if x >= 0:
                        next_page = request.args.get('next')
                        return redirect(next_page) if next_page else redirect(url_for('confirmation'))
                    else:
                        flash('Rooms not available, please choose a different hotel or different dates', 'danger')
    return render_template('booking.html', title='Booking', form=form)


@app.route("/confirmation", methods=['GET', 'POST'])
def confirmation():
    form = Payments_form()
    if form.validate_on_submit():
        form = PaymentType(payment_type=form.payment_type.data,
                           card_num=bcrypt.generate_password_hash(form.card_number.data),
                           card_cvv=bcrypt.generate_password_hash(form.sec_num.data))
        if form is True:
            return redirect(url_for('persona'))
        else:
               flash('Rooms not available, please choose a different hotel or different dates', 'danger')
    return render_template('confirmation.html', title='Confirmation', form=form)


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
