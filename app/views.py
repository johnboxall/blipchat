import time
import datetime

import pytz

from flask import Blueprint, render_template, current_app

from . import hipchat


blueprint = Blueprint("blipchat", __name__)


@blueprint.app_errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

@blueprint.app_errorhandler(500)
def not_found(error):
    return render_template("500.html"), 500

@blueprint.route("/")
@blueprint.route("/<int:year>-<int:month>-<int:day>/")
def history(year=None, month=None, day=None):
    tz = pytz.timezone("Canada/Pacific")

    if year is None:
        dt = datetime.datetime.now(tz)
    else:
        try:
            dt = datetime.datetime(year=year, month=month, day=day, tzinfo=tz)
        except ValueError:
            raise

    client = hipchat.get_client()
    messages = client.history(room_id=current_app.config["HIPCHAT_ROOM_ID"],
                              dt=dt)

    return render_template("index.html",
                           messages=messages,
                           dt=dt,
                           prev=dt - datetime.timedelta(days=1),
                           next=dt + datetime.timedelta(days=1))