from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class SelectInputOutput(FlaskForm):
    input = SelectMultipleField(choices=[])
    output = SelectMultipleField(choices=[])
    submit = SubmitField('Visualize!')
