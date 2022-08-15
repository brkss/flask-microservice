from flask import Flask
import flask_sqlalchemy
from config import DB_CONNECTION_URI
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION_URI
    app.app_context().push()
    return app
