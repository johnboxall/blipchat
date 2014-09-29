import os

from flask import Flask
from flask.ext.basicauth import BasicAuth
from flask_sslify import SSLify

from . import views


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or get_config())
    return app

def create_web_app(config=None):
    app = create_app(config=config)

    # Order is important here, because we must redirect to SSL before asking for
    # auth.
    SSLify(app)
    BasicAuth(app)

    app.register_blueprint(views.blueprint)
    return app


def get_config():
    config = os.environ.get("BLIPCHAT_CONFIG", None)
    if config is not None:
        return config

    # Heroku
    if "DYNO" in os.environ:
        config = "config.ProductionConfig"
    else:
        config = "config.DevelopmentConfig"

    return config