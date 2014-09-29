from flask import Blueprint, render_template

from . import hipchat


blueprint = Blueprint("blipchat", __name__)


@blueprint.app_errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404

@blueprint.app_errorhandler(500)
def not_found(error):
    return render_template("500.html"), 500

@blueprint.route("/")
def index():
    client = hipchat.get_client()
    messages = client.history(room_id=764056)
    return render_template("index.html", messages=messages)