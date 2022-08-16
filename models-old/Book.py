#from init import db
import flask_sqlalchemy
from app import app

db = flask_sqlalchemy.SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    # parms
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    author = db.Column(db.String(255))
    price = db.Column(db.Integer)
