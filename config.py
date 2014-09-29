import os


class Config(object):
    DEBUG = False
    TESTING = False

    SSL_ONLY = False

    BASIC_AUTH_FORCE = False
    BASIC_AUTH_USERNAME = None
    BASIC_AUTH_PASSWORD = None

    HIPCHAT_AUTH_TOKEN = os.environ.get("HIPCHAT_AUTH_TOKEN", None)
    HIPCHAT_ROOM_ID = os.environ.get("HIPCHAT_ROOM_ID", None)


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