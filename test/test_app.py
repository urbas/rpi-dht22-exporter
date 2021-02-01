import logging
from unittest import mock

from rpi_dht22_exporter import app


@mock.patch("rpi_dht22_exporter.metrics.get_dht22_reading", return_value=(53.4, 22.4))
def test_metrics(mock_get_dht22_reading):
    """metrics endpoint produces the expected metrics"""
    test_client = app.create_app(pin_number=5).test_client()
    mock_get_dht22_reading.assert_called_once_with(pin_number=5)
    response = test_client.get("/metrics")
    assert b"dht22_humidity 53.4\n" in response.data
    assert b"dht22_temperature 22.4\n" in response.data
    assert b"Humidity percentage." in response.data
    mock_get_dht22_reading.assert_has_calls(
        [mock.call(pin_number=5), mock.call(pin_number=5)]
    )


@mock.patch("rpi_dht22_exporter.metrics.get_dht22_reading", side_effect=Exception)
def test_reading_error(mock_get_dht22_reading, caplog):
    """metrics includes an error counter and logs at error level"""
    caplog.set_level(logging.ERROR)
    test_client = app.create_app(pin_number=5).test_client()
    response = test_client.get("/metrics")
    assert b"dht22_sampling_error_total 2.0\n" in response.data
    assert "Failed to get a reading from DHT22 at pin number 5." in caplog.text


@mock.patch("rpi_dht22_exporter.metrics.get_dht22_reading", return_value=(None, None))
def test_no_reading(mock_get_dht22_reading, caplog):
    """
    error counter should be increased when the dht22 returns non-numerical readings
    """
    caplog.set_level(logging.ERROR)
    test_client = app.create_app(pin_number=5).test_client()
    response = test_client.get("/metrics")
    assert b"dht22_sampling_error_total 2.0\n" in response.data
    assert "DHT22 produced invalid readings" in caplog.text
    assert "None and None respectively" in caplog.text
