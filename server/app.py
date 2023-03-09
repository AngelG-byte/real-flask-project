from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Spreadsheet, Column

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)


@app.route('/')
def index():
    return "Hello World"

@app.route('/users/<int:id>')
def user_by_id(id):
    user = User.query.filter(User.id == id).first()
    response_body = f'''
        <h2>id is {user.id}</h2>
        <h2>Information for {user.username}</h2>
        <h2>email is {user.email}</h2>
    '''

    response = make_response(response_body, 200)

    return response

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=False)
