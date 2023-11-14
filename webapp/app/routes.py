from flask import render_template
from flask import current_app as app
from app.forms import SelectInputOutput
from flask import render_template, flash, redirect, url_for
import app.model as model

@app.route('/', methods=['GET', 'POST'])
def home():
    '''landing page'''
    form = SelectInputOutput()
    if form.validate_on_submit():
        model.country = form.output.data
        flash('Settings Applied')
        return render_template(
            'index.jinja2',
            title = 'FSP-inator by the JKYM Group',
            description='Discover poverty all around the world!',
            template = 'home-template',
            body="",
            form = form
        )
    return render_template(
        'index.jinja2',
        title = 'FSP-inator by the JKYM Group',
        description='Discover poverty all around the world!',
        template = 'home-template',
        body="",
        form = form
    )
