from flask import render_template
from flask import current_app as app
from app.forms import InputVariables
from flask import render_template, flash, redirect, url_for
from app.learning_model import Model
# from app.models import Variables 
# from app import db

@app.route('/', methods=['GET', 'POST'])
def home():
    '''landing page'''
    form = InputVariables()
    if form.validate_on_submit():
        temperature = form.temperature.data
        hdi = form.hdi.data
        gini_index = form.gini_index.data
        population = form.population.data
        infant_mortality = form.infant_mortality.data
        '''
        db.session.add(variables)
        db.session.commit()
        '''
        model = Model()
        prediction = model.prediction(population, infant_mortality, temperature, gini_index, hdi)
        flash('Settings Applied')
        return render_template(
            'index.jinja2',
            title = 'FIP-inator by the JKYM Group',
            description='Discover poverty all around the world!',
            template = 'home-template',
            body="",
            form = form,
            predicted_val = prediction
        )
    return render_template(
        'index.jinja2',
        title = 'FIP-inator by the JKYM Group',
        description='Discover poverty all around the world!',
        template = 'home-template',
        body="",
        form = form
    )

@app.route('/data', methods = ['GET'])
def data():
    return render_template(
        'final_report.html'
    )
