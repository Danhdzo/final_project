import asyncio
import random
from faker import Faker
from pyppeteer import launch


asyncio.set_event_loop(asyncio.new_event_loop())

def disable_timeout_pyppeteer():
    import pyppeteer.connection
    original_method = pyppeteer.connection.websockets.client.connect

    def new_method(*args, **kwargs):
        kwargs['ping_interval'] = None
        kwargs['ping_timeout'] = None
        return original_method(*args, **kwargs)

    pyppeteer.connection.websockets.client.connect = new_method


def create_users():
    faker = Faker('es_MX')
    seed = random.randint(1, 100)
    Faker.seed(seed)
    name = faker.first_name()
    last_name = faker.last_name()
    age = random.randint(1, 100)
    address = faker.address()
    city = 'Monterrey'
    state = 'Nuevo Leon'
    zip = random.randint(64000, 64968)
    country = 'Mexico'
    phone = random.randint(8100000000, 8199999999)
    email = faker.ascii_free_email()
    return {"name": name,
            "last_name": last_name,
            "age": age,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip,
            "country": country,
            "phone": phone,
            "email": email}


def create_booking():
    faker = Faker('es_MX')
    seed = random.randint(1, 100)
    Faker.seed(seed)
    hotel_name = ['Anaheim', 'Tokyo']
    room_type = ['single', 'double', 'junior', 'master']
    hotel_name_choice = random.choice(hotel_name)
    from_day = random.randint(1, 28)
    from_month = random.randint(1, 12)
    from_year = '2020'
    to_day = random.randint(1, 28)
    if from_month == 12:
        to_month = 12
    else:
        to_month = from_month + 1
    to_year = '2020'
    adults = random.randint(1, 10)
    children = random.randint(0, 10)
    room_count = random.randint(1, 10)
    agents = random.randint(1, 1000)
    type = random.choice(room_type)
    return {"hotel_name": hotel_name_choice, "from_day": from_day, "from_month": from_month, "from_year": from_year,
            "to_day": to_day, "to_month": to_month, "to_year": to_year,
            "adults": adults, "children": children, "room_count": room_count, "agents": agents, "type": type}


async def insert_user():
    u = create_users()
    await page.waitFor(2000)
    await page.type('#name', u.get("name"))
    await page.type('#last_name', u.get("last_name"))
    await page.type('#age', u.get("age"))
    await page.type('#address', u.get("address"))
    await page.type('#city', u.get("city"))
    await page.type('#state', u.get("state"))
    await page.type('#zip', u.get("zip"))
    await page.type('#country', u.get("country"))
    await page.type('#phone', u.get("phone"))
    await page.type('#email', u.get("email"))
    await page.click('#create')


async def insert_booking():
    b = create_booking()
    await page.waitFor(2000)
    await page.type('#hotel_name', b.get("hotel_name_choice"))
    await page.type('#from_day', b.get("from_day"))
    await page.type('#from_month', b.get("from_month"))
    await page.type('#from_year', b.get("from_year"))
    await page.type('#to_day', b.get("to_day"))
    await page.type('#to_month', b.get("to_month"))
    await page.type('#to_year', b.get("to_year"))
    await page.type('#adults', b.get("adults"))
    await page.type('#children', b.get("children"))
    await page.type('#room_count', b.get("room_count"))
    await page.type('#agents', b.get("agents"))
    await page.type('#room_type', b.get("type"))
    await page.click('#book')
    await page.waitFor(3000)


async def login(email,password,num_of_users):
    await page.goto('http://127.0.0.1:5000/', timeout=100000)
    await page.click('#login')
    await page.waitFor('#email')
    await page.type('#email', email)
    await page.type('#password', password)
    await page.type('#number_of_users', num_of_users)
    await page.click('#create')


async def logout():
    await page.click('#logout')
    await page.waitFor(3000)



async def var_receiver(email,password,num_of_users):
    disable_timeout_pyppeteer()
    browser = await launch(headless=False)
    context = await browser.createIncogniteBrowserContext()
    global page
    page = await context.newPage()
    await login(email=email,password=password,num_of_users=num_of_users)
    await insert_user()
    await insert_booking()
    await logout()


def run_main(email,password,num_of_users):
    asyncio.get_event_loop().run_until_complete(var_receiver(email,password,num_of_users))
