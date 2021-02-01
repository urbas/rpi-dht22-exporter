import sys
from unittest import mock

import pytest

from rpi_dht22_exporter import app
from rpi_dht22_exporter.main import main


def test_help(monkeypatch, capfd):
    monkeypatch.setattr(sys, "argv", ["app-name", "--help"])
    with pytest.raises(SystemExit) as ex_info:
        main()
    assert ex_info.value.code == 0
    assert "Usage: app-name" in capfd.readouterr().out


def test_main(mock_app, monkeypatch):
    """check that the exporter is created with all the given parameters"""
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "app-name",
            "--listen-address",
            "1.2.3.4",
            "--listen-port",
            "12345",
            "--pin-number",
            "5",
        ],
    )
    with pytest.raises(SystemExit) as ex_info:
        main()
    assert ex_info.value.code == 0
    app.create_app.assert_called_once_with(pin_number=5)
    mock_app.run.assert_called_once_with(host="1.2.3.4", port=12345)


def test_default_parameters(mock_app, monkeypatch):
    """check that the exporter is created with default parameters"""
    monkeypatch.setattr(sys, "argv", ["app-name"])
    with pytest.raises(SystemExit) as ex_info:
        main()
    assert ex_info.value.code == 0
    app.create_app.assert_called_once_with(pin_number=14)
    mock_app.run.assert_called_once_with(host="0.0.0.0", port=9894)


@pytest.fixture(name="mock_app")
def _mock_app():
    with mock.patch("rpi_dht22_exporter.app.create_app") as mock_create_app:
        mock_create_app.return_value = mock.Mock()
        yield mock_create_app.return_value
