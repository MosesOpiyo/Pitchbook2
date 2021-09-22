from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config_options

db = SQLAlchemy()

# Initializing application
# app = Flask(__name__)

#Setting up configuration
# app.config.from_object(DevConfig)


def create_app(config_name):

    app = Flask(__name__)

    db.init_app(app)

    app.config.from_object(config_options[config_name])

    #registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app