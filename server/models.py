from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, func
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rule = ('-spreadsheets.user','-columns.user')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(128))
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    spreadsheets = db.relationship('Spreadsheet', backref='user')
    def __repr__(self):
        return f'< User {self.username}>'




class Spreadsheet(db.Model, SerializerMixin):
    __tablename__ = 'spreadsheets'

    serialize_rules = ('-user.spreadsheets','-columns.spreadsheets')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    columns = db.relationship('Column', backref='spreadsheet')

    def __repr__(self):
        return f'<Spreadsheet {self.name} >,' + \
            f'<Spreadsheet {self.user_id}'

#


class Column(db.Model, SerializerMixin):
    __tablename__ = 'columns'

    serialize_rules = ('-spreadsheets.columns','-user.columns',)

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=True)
    value = db.Column(db.Integer, nullable=True)
    # created_at = Column(DateTime(), server_default=func.now())
    # updated_at = Column(DateTime(), onupdate=func.now())

    spreadsheet_id = db.Column(db.Integer, db.ForeignKey('spreadsheets.id'))
    def __repr__(self):
        return f'<Column {self.text} >, ' + \
                f'<Column {self.id} >,' + \
                f'<Column {self.value} >,'