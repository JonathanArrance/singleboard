#!/bin/python
#rpi based temp monitoring and alerting
import time
#import board
import Adafruit_DHT
import settings

#get the sensor
#sensor = 'Adafruit_DHT.'+settings.SENSORTYPE
sensor = Adafruit_DHT.DHT11
#Pins where DHT11 sensors connected
pins = ['24','23','4']

#lets print the output of the sensors
while True:
    print("------")
    for pin in pins:
        try:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            temp_scale = 'C'
            if(settings.SCALE == 'Fahrenheit'):
                temperature = temperature * 9/5.0 + 32
                temp_scale = 'F'
            print( "Temp: {:.1f} {}   Humidity: {}% ".format(temperature, temp_scale, humidity))
        except RuntimeError as error:
            print(error.args[0])
    print("---------")
    time.sleep(1)

#if there is an overheat situation blink the led

#lets keep an eye on the button and change output from stats to temps

