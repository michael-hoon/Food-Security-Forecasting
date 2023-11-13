from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
import pandas as pd

class SelectInputOutput(FlaskForm):
    data = 'data/2Ddataset.xlsx'
    df = pd.read_excel(data)
    input = SelectMultipleField(choices=df.keys())
    output = SelectField(choices=df.keys())
    submit = SubmitField('Apply Parameters')
