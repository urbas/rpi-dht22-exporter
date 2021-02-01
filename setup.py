#!/usr/bin/env python

"""The setup script."""

import os
import re
from pathlib import Path
from setuptools import setup

REQUIREMENTS = ["click>=7.0.0", "Flask>=1.0.0", "prometheus_client>=0.8.0"]

if re.search(r"^(aarch64|arm)", os.uname().machine):
    REQUIREMENTS.append("Adafruit_Python_DHT==1.4.0")

SETUP_REQUIREMENTS = ["pytest-runner"]

TEST_REQUIREMENTS = ["pytest"]

CHANGELOG = Path("CHANGELOG.md").read_text()

setup(
    author_email="matej.urbas@gmail.com",
    author="Matej Urbas",
    entry_points={
        "console_scripts": ["rpi-dht22-exporter=rpi_dht22_exporter.main:main"]
    },
    include_package_data=True,
    install_requires=REQUIREMENTS,
    keywords=["rpi-dht22-exporter", "dht22", "prometheus", "exporter"],
    license="MIT license",
    long_description_content_type="text/markdown",
    long_description=f"{Path('README.md').read_text()}\n\n{CHANGELOG}",
    name="rpi-dht22-exporter",
    packages=["rpi_dht22_exporter"],
    setup_requires=SETUP_REQUIREMENTS,
    test_suite="test",
    tests_require=TEST_REQUIREMENTS,
    url="https://github.com/urbas/rpi-dht22-exporter",
    version="2.0.1",
)
