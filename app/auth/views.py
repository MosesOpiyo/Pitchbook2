from flask import render_template
from app.auth import auth


@auth.route('/')
def login():
    return render_template('templates/index.html')