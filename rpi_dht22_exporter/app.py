from flask import Flask
from rpi_dht22_exporter import metrics


def create_app(users=None):
    app = Flask(__name__)
    app.register_blueprint(metrics.API)
    return app
