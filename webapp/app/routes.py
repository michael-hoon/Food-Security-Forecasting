from flask import render_template
from flask import current_app as app

@app.route('/')
def home():
    '''landing page'''
    return render_template(
        'index.jinja2',
        title = 'FSP-inator by the JKYM Group',
        description='Discover poverty all around the world!',
        template = 'home-template',
        body=""
    )
