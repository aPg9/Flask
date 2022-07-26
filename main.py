from flask import Flask, make_response, redirect, request, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired     
import unittest

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ["Buy coffee", "Send buy apply", "Send video to productor"]

class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired()])     #-----> Datarequired valida la data enviada por el usuario
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Send")


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests') 
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', error=error)


@app.route("/index")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))     
    session["user_ip"] = user_ip
    return response


@app.route('/hello',
 methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm() 
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data 
        session["username"] = username
        flash('Username registered successfully!!! ')

        return redirect(url_for('index'))

    return render_template('hello.html', **context)     