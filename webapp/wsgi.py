from app import init_app
from flask_bootstrap import Bootstrap5

app = init_app()
bootstrap = Bootstrap5(app)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
