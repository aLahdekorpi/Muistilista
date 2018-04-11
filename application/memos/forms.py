from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, validators

class MemoForm(FlaskForm):
    name = TextField("Memo name" ,[validators.Length(min=2)])
    class Meta:
        csrf = False