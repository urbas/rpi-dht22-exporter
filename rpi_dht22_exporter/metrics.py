import logging
from typing import Tuple

import prometheus_client.core


class DHT22Collector:
    def __init__(self, pin_number: int):
        self._pin_number = pin_number
        self._error_counter = 0

    def collect(self):
        try:
            humidity, temperature = get_dht22_reading(pin_number=self._pin_number)
            if not isinstance(humidity, float) or not isinstance(temperature, float):
                raise RuntimeError(
                    "DHT22 produced invalid readings for humidity and temperature: "
                    f"{humidity} and {temperature} respectively."
                )
            logging.debug(
                "Got a reading of humidity %s\\% and temperature %s°C from DHT22 on "
                "pin number %s.",
                humidity,
                temperature,
                self._pin_number,
            )
            return [
                prometheus_client.core.GaugeMetricFamily(
                    "dht22_humidity", "Humidity percentage.", value=humidity
                ),
                prometheus_client.core.GaugeMetricFamily(
                    "dht22_temperature", "Temperature in °C.", value=temperature
                ),
            ]
        except Exception as ex:
            logging.error(
                "Failed to get a reading from DHT22 at pin number %s. Error: %s",
                self._pin_number,
                ex,
            )
            return self._sampling_error()

    def _sampling_error(self):
        self._error_counter += 1
        return [
            prometheus_client.core.CounterMetricFamily(
                "dht22_sampling_error",
                "Counts the number of times sampling DHT22 metrics failed.",
                value=self._error_counter,
            )
        ]


def get_dht22_reading(pin_number: int) -> Tuple[float, float]:
    import Adafruit_DHT

    return Adafruit_DHT.read_retry(sensor=Adafruit_DHT.DHT22, pin=pin_number)
