from flask import render_template
from . import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/sign-up')
def SignUp():
    return render_template('sign-up.html')

@app.route('/pitchbook')
def home():
    return render_template('home.html')



@app.route('/account')
def account():
    return render_template('account.html')
