#!/bin/python
#rpi based temp monitoring and alerting
import time
import multiprocessing
import subprocess
import Adafruit_DHT
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import settings

#get the sensor
#sensor = 'Adafruit_DHT.'+settings.SENSORTYPE
sensor = Adafruit_DHT.+settings.SENSORTYPE
#Pins where DHT11 sensors connected
pins = settings.PINS

#lets print the output of the sensors
while True:
    print("------")
    out = {}
    for pin in pins:
        try:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            temp_scale = 'C'
            if(settings.SCALE == 'Fahrenheit'):
                temperature = temperature * 9/5.0 + 32
                temp_scale = 'F'
            out['temp_%s_%s']%(pin,temp_scale) = temperature
            out['humidity_%s_%s']%(pin,humidity) = humidity
            print(out)
            #print( "Temp: {:.1f} {} Humidity: {}% ".format(temperature, temp_scale, humidity))
        except RuntimeError as error:
            print(error.args[0])
    print("---------")
    #time.sleep(settings.SLEEP)

    #if there is an overheat situation blink the led

    #lets keep an eye on the button and change output from stats to temps
    '''
    #disply the to the screen
    # 128x32 display with hardware I2C:
    disp = Adafruit_SSD1306.SSD1306_128_32(rst=settings.RST)

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

        # Draw a black filled box to clear the image.
        draw.rectangle((0,0,width,height), outline=0, fill=0)

        # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
        th = "hostname -I | cut -d\' \' -f1"
        IP = subprocess.check_output(cmd, shell = True )
        cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
        CPU = subprocess.check_output(cmd, shell = True )
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell = True )
        cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
        Disk = subprocess.check_output(cmd, shell = True )

    # Write two lines of text.

    draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)
    draw.text((x, top+8),     str(CPU), font=font, fill=255)
    draw.text((x, top+16),    str(MemUsage),  font=font, fill=255)
    draw.text((x, top+25),    str(Disk),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    '''
    time.sleep(2)
    