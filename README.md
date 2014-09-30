# Blipchat

A service for exposing Hipchat room convos to folks who aren't users.

## Installation and Usage

    git clone ...
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    make run

## Config

The following environment variables can be configured:

* `HIPCHAT_AUTH_TOKEN` required for accessing the Hipchat history API.
* `HIPCHAT_ROOM_ID` the room who's history should be displayed.
* `BASIC_AUTH_USERNAME` and `BASIC_AUTH_PASSWORD`


## TODO

- [ ] Cache Hipchat responses
- [ ] Add styling / html stuff
- [ ] Allow selecting which room you want
- [ ] Allow other forms of auth
- [ ] App.json / deploy to Heroku button