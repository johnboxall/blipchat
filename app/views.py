import time
import datetime

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
    if year is None:
        date = datetime.date.today()
    if year is not None:
        try:
            date = datetime.date(year=year, month=month, day=day)
        except ValueError:
            raise

    client = hipchat.get_client()
    messages = client.history(room_id=current_app.config["HIPCHAT_ROOM_ID"],
                             date=date)

    return render_template("index.html",
                           messages=messages,
                           date=date,
                           prev=date - datetime.timedelta(days=1),
                           next=date + datetime.timedelta(days=1))