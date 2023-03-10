from flask import Flask, jsonify, make_response, request
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


@app.route('/users', methods=["GET", "POST"])
def users():
    if request.method == 'GET':
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
            200,
            {"Content-Type": "application/json"}
        )

        return response
    elif request.method == 'POST':
        new_user = User(
            username=request.form.get("username"),
            email=request.form.get("email"),
            password_hash=request.form.get("password_hash")
        )
        db.session.add(new_user)
        db.session.commit()



        response = make_response(
            "user created",
            201,
         {"Content-Type": "application/json"}
         )


        return response


@app.route('/users/<int:id>')
def user_by_id(id):
        user = User.query.filter(User.id == id).first()

        user_dict = user.to_dict()

        response = make_response(
            jsonify(user_dict),
            200
            )


        return response




if __name__ == '__main__':
    app.run(port=5555, debug=False)

# LOGIN EXAMPLE
#     @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))