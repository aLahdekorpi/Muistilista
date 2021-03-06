from flask_wtf import FlaskForm
from wtforms import PasswordField, TextField
  
class LoginForm(FlaskForm):
    username = TextField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = TextField("Name")
    username = TextField("Username")
    password = PasswordField("Password")        