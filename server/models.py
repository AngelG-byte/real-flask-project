from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128))

    spreadsheets = db.relationship('Spreadsheet', backref='users')

    def __repr__(self):
        return f'<Spreadsheet User {self.username}>'

#
class Spreadsheet(db.Model):
    __tablename__ = 'spreadsheets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    columns = db.relationship('Column', backref='spreadsheets')

    def __repr__(self):
        return f'<Spreadsheet {self.name} >'

#
class Column(db.Model):
    __tablename__ = 'columns'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=True)
    value = db.Column(db.Integer, nullable=True)

    spreadsheet_id = db.Column(db.Integer, db.ForeignKey('spreadsheets.id'))
