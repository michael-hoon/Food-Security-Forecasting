from flask import render_template
from flask import current_app as app
from app.forms import InputVariables
from flask import render_template, flash, redirect, url_for
from learning_model import model
# from app.models import Variables 
# from app import db

@app.route('/', methods=['GET', 'POST'])
def home():
    '''landing page'''
    form = InputVariables()
    if form.validate_on_submit():
        temperature = form.temperature.data
        hdi = form.hdi
        gini_index = form.gini_index
        population = form.population
        infant_mortality = form.infant_mortality
        '''
        db.session.add(variables)
        db.session.commit()
        '''
        prediction = model.predict([])
        flash('Settings Applied')
        return render_template(
            'index.jinja2',
            title = 'FSP-inator by the JKYM Group',
            description='Discover poverty all around the world!',
            template = 'home-template',
            body="",
            form = form,
            predicted_val = prediction
        )
    return render_template(
        'index.jinja2',
        title = 'FSP-inator by the JKYM Group',
        description='Discover poverty all around the world!',
        template = 'home-template',
        body="",
        form = form
    )
