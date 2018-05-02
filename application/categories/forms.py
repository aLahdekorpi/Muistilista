from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, validators

class CategoryForm(FlaskForm):
    name = TextField("Name" ,[validators.Length(min=2)])
    class Meta:
        csrf = False
    