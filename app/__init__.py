from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('404.html'),404

def create_app(config_name):
    """This is the app factory function
    """
    app = Flask(__name__)

    #setting up the configurations
    app.config.from_object(config_options[config_name])

    #initializing the extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    configure_uploads(app,photos)

    #registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authentication')

    app.register_error_handler(404,four_Ow_four)

    return app