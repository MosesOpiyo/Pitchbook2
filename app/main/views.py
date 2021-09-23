from flask import render_template
from app.auth import auth
from flask_login import login_required
from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import User

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@main.route('/sign-up')
def SignUp():
    return render_template('sign-up.html')

@main.route('/pitchbook')
def home():
    return render_template('home.html')



@main.route('/account')
def account():
    return render_template('account.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


