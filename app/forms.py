from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired 

class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired()])     #-----> Datarequired valida la data enviada por el usuario
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Send")