from flask import Flask
from flask_bootstrap import Bootstrap as BT
from .config import Config

def create_app():
    app = Flask(__name__)
    bootstrap = BT(app)

    app.config.from_object(Config)

    return app