from random import choice as rc
from faker import Faker
from app import app
from models import db, User

db.init_app(app)

fake = Faker()

with app.app_context():
    User.query.delete()

    users = []

    for i in range(10):
        user = User(name=faker.name())
        users.append(user)

        db.session.add_all(users)
        db.session.commit()
