#!/bin/python
#rpi based temp monitoring and alerting
import time
#import board
import Adafruit_DHT
import settings

#get the sensor
sensor = settings.SENSORTYPE

#Pins where DHT11 sensors connected
pins = ['22','23','4']

#lets print the output of the sensors
while True:
    for pin in pins:
        try:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            temp_scale = 'C'
            if(settings.SCALE == 'Fahrenheit'):
                temperature = temperature * 9/5.0 + 32
                temp_scale = 'F'
            humidity = dhtDevice.humidity
            print( "Temp: {:.1f} {}   Humidity: {}% ".format(temperature, temp_scale, humidity))
        except RuntimeError as error:
            print(error.args[0])
    time.sleep(2)


#if there is an overheat situation blink the led

#lets keep an eye on the button and change output from stats to temps

