from INIT import db, bcrypt
from INIT.models import *

db.drop_all()
db.create_all()
user = User(username="luis_hdzo@hotmail.com",password=bcrypt.generate_password_hash("password"))
db.session.add(user)
db.session.commit()
import INIT.DBconn