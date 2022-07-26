from unicodedata import name
from app.forms import LoginForm
from . import auth
from flask import render_template

@auth.route('/login')
def login():
    context = {
        'login_form': LoginForm()
    }
    return render_template('login.html', **context)