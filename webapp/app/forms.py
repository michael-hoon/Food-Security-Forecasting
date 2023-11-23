from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired, ValidationError
import pandas as pd

class InputVariables(FlaskForm):
    data = 'data/2Ddataset.xlsx'
    df = pd.read_excel(data)
    population = FloatField('Population', validators=[DataRequired()])
    infant_mortality = FloatField('Infant Mortality (in %)', validators=[DataRequired()])
    hdi = FloatField('Human Development Index (from 0 to 1)', validators=[DataRequired()])
    gini_index = FloatField("Gini's Index (from 0 to 100)", validators=[DataRequired()])
    temperature = FloatField('Temperature (in °C)', validators=[DataRequired()])
    submit = SubmitField('Calculate Food Insecurity')
