from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
import pandas as pd

class InputVariables(FlaskForm):
    data = 'data/2Ddataset.xlsx'
    df = pd.read_excel(data)
    population = StringField('Population', validators=[DataRequired()])
    infant_mortality = StringField('Infant Mortality', validators=[DataRequired()])
    hdi = StringField('hdi', validators=[DataRequired()])
    gini_index = StringField("Gini's Index", validators=[DataRequired()])
    temperature = StringField('temperature', validators=[DataRequired()])
    submit = SubmitField('Apply Parameters')
