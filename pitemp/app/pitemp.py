#!/bin/python
#rpi based temp monitoring and alerting
import time
import datetime
#import multiprocessing
#mport subprocess
import Adafruit_DHT
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import settings
import schedule
import pitemp_lib as plib


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


'''
def temp_sensor():
    #get the sensor
    #sensor = 'Adafruit_DHT.'+settings.SENSORTYPE
    sensor = Adafruit_DHT.DHT11
    #Pins where DHT11 sensors connected
    pins = settings.PINS

    #lets print the output of the sensors
    self.output = {}
    for pin in pins:
        try:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            temp_scale = 'C'
            if(settings.SCALE == 'Fahrenheit'):
                temperature = temperature * 9/5.0 + 32
                temp_scale = 'F'
            self.output['temp_pin%s'%(pin)] = temperature
            self.output['temp_scale'] = temp_scale
            self.output['humidity_pin%s'%(pin)] = humidity
            #print( "Temp: {:.1f} {} Humidity: {}% ".format(temperature, temp_scale, humidity))
        except RuntimeError as error:
            print(error.args[0])
    print(self.output)
    return self.output
'''


def screen_output():
    #get the pins
    PIN = settings.PINS
    sensor = Adafruit_DHT.DHT11
    ip_addr = plib.get_nic_ip_info(settings.PHYSNET)
    
    if(settings.SCALE=='Fahrenheit'):
        temp_scale = 'F'
    else:
        temp_scale = 'C'
    
    # 128x32 display with hardware I2C:
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=settings.RST)

    # Initialize library.
    disp.begin()

    # Clear display.
    disp.clear()
    disp.display()

    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = -2
    top = padding
    bottom = height-padding
    # Move left to right keeping track of the current x position for drawing shapes.
    x = 0

    # Load default font.
    font = ImageFont.load_default()

    while True:
        #lets print the output of the sensors
        output = {}
        for pin in PIN:
            try:
                humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
                temp_scale = 'C'
                if(settings.SCALE == 'Fahrenheit'):
                    temperature = temperature * 9/5.0 + 32
                    temp_scale = 'F'
                output['temp_pin%s'%(pin)] = temperature
                output['temp_scale'] = temp_scale
                output['humidity_pin%s'%(pin)] = humidity
                #print( "Temp: {:.1f} {} Humidity: {}% ".format(temperature, temp_scale, humidity))
            except RuntimeError as error:
                print(error.args[0])
        
        dt = datetime.datetime.now()
        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        draw.text((x, top),       "Time: "+dt.strftime('%H:%M:%S'), font=font, fill=255)
        draw.text((x, top+8),     "IP: "+ip_addr, font=font, fill=255)
        draw.text((x, top+16),    "Temp: "+str(output['temp_pin%s'%(str(PIN[0]))])+""+output['temp_scale']+" Hum "+str(output['humidity_pin%s'%(str(PIN[0]))]), font=font, fill=255)
        draw.text((x, top+25),    "Sensor Two", font=font, fill=255)
        draw.text((x, top+33),    "Temp: "+str(output['temp_pin%s'%(str(PIN[1]))])+""+output['temp_scale']+" Hum "+str(output['humidity_pin%s'%(str(PIN[1]))]), font=font, fill=255)
        draw.text((x, top+41),    "Sensor Three", font=font, fill=255)
        draw.text((x, top+49),    "Temp: "+str(output['temp_pin%s'%(str(PIN[2]))])+""+output['temp_scale']+" Hum "+str(output['humidity_pin%s'%(str(PIN[2]))]), font=font, fill=255)
        
        # Display image.
        disp.image(image)
        disp.display()

if __name__=='__main__':
    #Run the function
    schedule.every(settings.INTERVAL).seconds.do(screen_output())

