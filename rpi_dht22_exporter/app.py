import prometheus_client
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from rpi_dht22_exporter import metrics


def create_app(pin_number: int):
    app = Flask(__name__)
    metrics_collector_registry = prometheus_client.CollectorRegistry(auto_describe=True)
    metrics_collector_registry.register(metrics.DHT22Collector(pin_number))
    app.wsgi_app = DispatcherMiddleware(  # type: ignore
        app.wsgi_app,
        {"/metrics": prometheus_client.make_wsgi_app(metrics_collector_registry)},
    )
    return app
