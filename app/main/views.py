from flask import render_template
from . import main

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
