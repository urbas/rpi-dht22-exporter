from flask import Blueprint
from flask.json import jsonify

API = Blueprint("metrics", __name__, url_prefix="/metrics")


@API.route("")
def get():
    return jsonify(temperature=42, humidity=95)
