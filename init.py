from flask import Flask
import flask_sqlalchemy
from config import DB_CONNECTION_URI
from dotenv import load_dotenv

load_dotenv()

db = flask_sqlalchemy.SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    db.create_all
    return app
