"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment
#from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from app.middleware import PrefixMiddleware


def init_app():
    """Construct core Flask application with embedded Dash app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)
    #db = SQLAlchemy(app)
    #migrate = Migrate(app, db)
    bootstrap = Bootstrap5(app)
    # set voc=False if you run on local computer
    app.wsgi_app = PrefixMiddleware(app.wsgi_app, voc=False)

    with app.app_context():
        # Import parts of our core Flask app
        from . import routes
        from .assets import compile_static_assets

        # Import Dash application
        from .dashboard import init_dashboard

        app = init_dashboard(app)

        # Compile static assets
        compile_static_assets(assets)

        return app
