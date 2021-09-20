from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Initializing application
# app = Flask(__name__)

#Setting up configuration
# app.config.from_object(DevConfig)

app = Flask(__name__)

from . import views