import os


class Config(object):
    # Flask Debug setting.
    DEBUG = False
    # Flag for running unit tests.
    TESTING = False

    # Used by `flask_sslify` to redirect HTTP traffic to HTTPS.
    SSL_ONLY = False

    # Used by `flask.ext.basicauth` to add HTTP Authentication.
    BASIC_AUTH_FORCE = False
    BASIC_AUTH_USERNAME = None
    BASIC_AUTH_PASSWORD = None

    # Hipchat settings.
    HIPCHAT_AUTH_TOKEN = os.environ["HIPCHAT_AUTH_TOKEN"]
    HIPCHAT_ROOM_ID = os.environ["HIPCHAT_ROOM_ID"]

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    SSL_ONLY = True

    # TODO: Raise if these aren't not correctly configured.
    BASIC_AUTH_FORCE = True
    BASIC_AUTH_REALM = "Ask John"
    BASIC_AUTH_USERNAME = os.environ.get("BASIC_AUTH_USERNAME", None)
    BASIC_AUTH_PASSWORD = os.environ.get("BASIC_AUTH_PASSWORD", None)