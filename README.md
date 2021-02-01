# Raspberry Pi DHT22 Prometheus Exporter [![build-badge]](https://travis-ci.com/github/urbas/rpi-dht22-exporter) [![pypi-badge]](https://pypi.org/project/rpi-dht22-exporter/)

Exports DHT22 temperature and humidity readings in a format readable by Prometheus.

## Installation

```bash
pip install rpi-dht-22-exporter
```

## Running
```bash
rpi-dht22-exporter --pin <gpio pin number>
```

This will serve metrics at `http://0.0.0.0:9894/metrics`.

You can make Prometheus scrape these with this scrape config:
```yaml
scrape_configs:
  - job_name: 'dht22@<the IP of your Raspberry Pi>'
    static_configs:
      - targets: ['<the IP of your Raspberry Pi>:9894']
        labels:
          location: 'bedroom'
```

[build-badge]: https://travis-ci.com/urbas/rpi-dht22-exporter.svg?branch=master
[pypi-badge]: https://badge.fury.io/py/rpi-dht22-exporter.svg
