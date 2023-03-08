from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Spreadsheet, Column

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def index():
    return "Index for User/Spreadheet/Columns API"


@app.route('/users')
def users():

    users = []
    for user in User.query.all():
        user_dict = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "password_hash": user.password_hash,

        }
        users.append(user_dict)

    response = make_response(
        jsonify(users),
        200
    )

    return response

@app.route('/users/<int:id>')
def user_by_id(id):
        user = User.query.filter(User.id == id).first()

        user_dict = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
        response = make_response(
            user_dict,
            200
            )


        return response

if __name__ == '__main__':
    app.run(port=5555, debug=False)
