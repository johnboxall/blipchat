# Blipchat

A service for exposing Hipchat room convos to folks who aren't users.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/johnboxall/blipchat)

## Installation and Usage

Blipchat is simple Flask application. To develop locally:

    git clone git@github.com:johnboxall/blipchat.git
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    # Configure the settings below in your local `.env` file and..!
    make run

## Config

The following environment variables can be configured:

* `BLIPCHAT_CONFIG` the module to import that contains the settings. Defaults to
  `config.ProductionConfig` if being run on a Heroku dyno or `config.DevelopmentConfig`.
* `HIPCHAT_AUTH_TOKEN` required for accessing the Hipchat history API.
* `HIPCHAT_ROOM_ID` the room who's history should be displayed.
* `BASIC_AUTH_USERNAME` and `BASIC_AUTH_PASSWORD` provide HTTP Authentication
  when `config.ProductionConfig` is used.

In development, set in a `.env` at the root for much happiness.

## TODO

- [ ] Cache Hipchat responses
- [ ] Add styling / html stuff
- [ ] Allow selecting which room you want
- [ ] Secret header based auth.
- [ ] Allow timezone configuration