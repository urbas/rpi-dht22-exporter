# Raspberry Pi DHT22 Prometheus Exporter
An HTTP server that serves DHT22 temperature and humidity readings in a format readable by Prometheus.

## Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Running
```bash
FLASK_ENV=development FLASK_APP=rpi_dht22_exporter/app.py flask run --host 0.0.0.0
```
This will serve metrics at `http://localhost:5000/metrics`.

You can make Prometheus scrape these with this scrape config:
```yaml
scrape_configs:
  - job_name: 'dht22@<the IP of your Raspberry Pi>'
    static_configs:
      - targets: ['<the IP of your Raspberry Pi>:5000']
        labels:
          location: 'bedroom'
```