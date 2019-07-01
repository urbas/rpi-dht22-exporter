from flask import Flask
from rpi_dht22_exporter import metrics


def create_app(users=None):
    app = Flask(__name__)
    app.register_blueprint(metrics.API)
    return app


def main():
  # import Adafruit_DHT
  # temperature, humidity = Adafruit_DHT.read_retry(sensor=Adafruit_DHT.DHT22, pin=14) 
  # print(f"Temperature: {temperature}")
  # print(f"Humidity: {humidity}")
  pass


if __name__ == "__main__":
    main()