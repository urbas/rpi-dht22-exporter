import Adafruit_DHT


def main():
  temperature, humidity = Adafruit_DHT.read_retry(sensor=Adafruit_DHT.DHT22, pin=14) 
  print(f"Temperature: {temperature}")
  print(f"Humidity: {humidity}")


if __name__ == "__main__":
    main()