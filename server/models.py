from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, func

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128))
    spreadsheets = db.relationship('Spreadsheet', backref='user')

    def __repr__(self):
        return f'<Spreadsheet User {self.username}>'

#
class Spreadsheet(db.Model):
    __tablename__ = 'spreadsheets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    columns = db.relationship('Column', backref='spreadsheet')

    def __repr__(self):
        return f'<Spreadsheet {self.name} >,' + \
            f'<Spreadsheet {self.user_id}'

#
class Column(db.Model):
    __tablename__ = 'columns'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=True)
    value = db.Column(db.Integer, nullable=True)
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    spreadsheet_id = db.Column(db.Integer, db.ForeignKey('spreadsheets.id'))
    def __repr__(self):
        return f'<Column {self.text} >, ' + \
                f'<Column {self.id} >,' + \
                f'<Column {self.value} >,'