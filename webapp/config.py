"""Flask config."""
import os
from os import environ, path

BASE_DIR = path.abspath(path.dirname(__file__))


class Config:
    """Flask configuration variables."""

    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT")
    FLASK_APP = "main.py"
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SECRET_KEY = environ.get("SECRET_KEY") or 'very-secret-key'

    # Assets
    LESS_BIN = environ.get("LESS_BIN")
    ASSETS_DEBUG = environ.get("ASSETS_DEBUG")
    LESS_RUN_IN_DEBUG = environ.get("LESS_RUN_IN_DEBUG")

    # Static Assets
    STATIC_FOLDER = "app/static"
    TEMPLATES_FOLDER = "app/templates"
    COMPRESSOR_DEBUG = environ.get("COMPRESSOR_DEBUG")

    #SQL
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
