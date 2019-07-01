import logging
from os import environ

from flask import Blueprint, abort
from flask.json import jsonify

API = Blueprint("metrics", __name__, url_prefix="/metrics")


@API.route("")
def get():
    try:
        # pylint: disable=import-error
        import Adafruit_DHT

        humidity, temperature = Adafruit_DHT.read_retry(
            sensor=Adafruit_DHT.DHT22, pin=int(environ.get("DHT22_PIN", "14"))
        )
        return f"humidity {humidity}\ntemperature {temperature}\n"
    except Exception as ex:
        logging.error("Could not read values from DHT22. Error: %s", ex)
        return abort(501)
