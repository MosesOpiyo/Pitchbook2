from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from config import config_options

db = SQLAlchemy()

# Initializing application
# app = Flask(__name__)

#Setting up configuration
# app.config.from_object(DevConfig)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):

    app = Flask(__name__)

    db.init_app(app)

    app.config.from_object(config_options[config_name])

    #registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    return app