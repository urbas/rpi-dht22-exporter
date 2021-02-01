import click

from rpi_dht22_exporter import app


@click.command()
@click.option(
    "--listen-address",
    default="0.0.0.0",
    help="The address on which to listen for HTTP requests.",
    show_default=True,
)
@click.option(
    "--listen-port",
    default=9894,
    help="The port on which to listen for HTTP requests.",
    show_default=True,
)
@click.option(
    "--pin-number",
    default=14,
    help="The number of the GPIO pin on which the DHT22 sensor is attached.",
    show_default=True,
)
def main(listen_address, listen_port, pin_number):
    app.create_app(pin_number=pin_number).run(host=listen_address, port=listen_port)
