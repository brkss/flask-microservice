#from init import db
import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    author = db.Column(db.String(255))
    price = db.Column(db.Integer)
