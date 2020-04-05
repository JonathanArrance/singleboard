#!/bin/python
#rpi based temp monitoring and alerting
import time
import board
import adafruit_dht

#Pins where DHT11 sensors connected
pins = ['22','23','24']

#lets print the output of the sensors
while True:
    for pin in pins:
        dhtDevice = adafruit_dht.DHT11(board.D%s)%(pin)
        try:
            temperature_c = dhtDevice.emperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )
        except RuntimeError as error:
            print(error.args[0])
    time.sleep(2)


#if there is an overheat situation blink the led

#lets keep an eye on the button and change output from stats to temps

