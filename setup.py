#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

REQUIREMENTS = ["Adafruit_Python_DHT==1.4.0", "Flask==1.0.3"]

SETUP_REQUIREMENTS = ["pytest-runner"]

TEST_REQUIREMENTS = ["pytest"]

setup(
    author="Matej Urbas",
    author_email="matej.urbas@gmail.com",
    entry_points={
        "console_scripts": [
            "rpi-dht22-exporter=rpi_dht22_exporter.app:main",
        ]
    },
    install_requires=REQUIREMENTS,
    include_package_data=True,
    keywords="rpi_dht22_exporter",
    name="rpi_dht22_exporter",
    packages=find_packages(include=["rpi_dht22_exporter"]),
    setup_requires=SETUP_REQUIREMENTS,
    test_suite="tests",
    tests_require=TEST_REQUIREMENTS,
)