from flask import render_template
from flask import current_app as app
from app.forms import SelectInputOutput
from flask import render_template, flash, redirect, url_for

@app.route('/')
def home():
    '''landing page'''
    form = SelectInputOutput()
    if form.validate_on_submit():
        input = form.input.data
        output = form.output.data
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
