#Program that calculates temperature using a temperature sensor and a raspberry pi
#Unless specified the code was written by team members

from sensor_library import *
from gpiozero import LED
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import time
import pyrebase

#Firebase initialization (Written by me)
config = {
    "apiKey": "AIzaSyA4fFc50MbroRk0YgUGuYcci7YKl2rM_-I",
    "authDomain": "baby-temperature.firebaseapp.com",
    "databaseURL": "https://baby-temperature.firebaseio.com",
    "projectID": "baby-temperature",
    "storageBucket": "baby-temperature.appspot.com",
    "messagingSenderId": "333367061666"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# OLED Screen Initialization
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = 2
shape_width = 500
top = padding
bottom = height-padding

x = padding

#Font is imported from the font file in the same folder as the program
font = ImageFont.truetype('LiberationMono-Bold.ttf',30)

#All LEDs are defined and the temperature sensor
blueled = LED(8)
greenled = LED(12)
yellowled = LED(9)
redled = LED(5)

sensor = Temp_Sensor()

#Turns off all LEDs
def LED_off(LED1,LED2,LED3,LED4):
    LED1.off()
    LED2.off()
    LED3.off()
    LED4.off()
    
#This function swaps which LEDs are turned on and off
def LED_swap(led_off1 , led_off2 , led_off3 , led_on):
    
    led_off1.off()
    led_off2.off()
    led_off3.off()

    led_on.on()

#This function flashes an LED when turned on
def LED_flash(led):

    time.sleep(0.25)
 
    led.off()

    time.sleep(0.25)

#This function measures the average temperature from 5 most recent measurements  
def measure_avgtemp():

    count = 0
    temp = 0
    
    for i in range(5):

        temp += sensor.avg_temp()

        count += 1
        time.sleep (0.1)

    avg_temp = temp / count

    avg_temp = round(avg_temp,2)
    
    return avg_temp

#Displays any output on the screen
def screen_display(output):

    draw.text((x, top),    str(output),  font=font, fill=1900)

    disp.image(image)
    disp.display()

    time.sleep(0.5)

    #clears the screen    
    draw.rectangle((0,0,width,height), outline=0, fill=0)

#Causes the LEDs to flash in a sequence if there is error in the measured temperature
def LED_Error(LED1,LED2,LED3,LED4):

    LED2.off()
    LED3.off()
    LED4.off()


    LED1.on()

    time.sleep(0.1)

    LED1.off()
    LED2.on()

    time.sleep(0.2)

    LED2.off()
    LED3.on()

    time.sleep(0.2)

    LED3.off()
    LED4.on()

    time.sleep(0.1)

def main():    
    while True:
        
        temp = measure_avgtemp()

        #Finding local time (written by me)
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        #Uploading sensor data to Firebase (written by me)
        data= {
            "temperature": temp
        }
        tdata={
            "time": current_time
        }
        db.child("Temp").update(data)
        db.child("T").update(tdata)
        print("Data Updated")

    
        if temp >= 20 and temp < 35.5:

            LED_swap(yellowled, redled, greenled, blueled)
            screen_display(temp)
            print ('The temperature is ' + str(temp) + ' the blue LED is on')

        elif temp >= 35.5 and temp < 37.5:

            LED_swap(yellowled, redled, blueled, greenled)
            screen_display(temp)
            print ('The temperature is ' + str(temp) + ' the green LED is on')

        elif temp >= 37.5 and temp < 40:

            LED_swap(blueled, redled, greenled, yellowled)
            screen_display(temp)
            print ('The temperature is ' + str(temp) + ' the yellow LED is on')

        elif temp >= 40 and temp <= 50:

            screen_display(temp)
            LED_swap(yellowled, blueled, greenled, redled)
            LED_flash(redled)
            print ('The temperature is ' + str(temp) + ' the red LED is on')

        elif temp > 50:

            LED_off(redled,yellowled,greenled,blueled) 

            LED_Error (redled,yellowled,greenled,blueled)
            LED_Error (blueled,greenled,yellowled,redled)

            screen_display('HOT!!')

            print ('The temperature is ' + str(temp) + ' AAAHHH TOO HOT')

        else:

            LED_off(redled,yellowled,greenled,blueled) 

            LED_Error (redled,yellowled,greenled,blueled)
            LED_Error (blueled,greenled,yellowled,redled)

            screen_display('COLD!!')

            print ('The temperature is ' + str(temp) + ' AAAHHH TOO COLD')

            time.sleep(0.1)

LED_off(redled,yellowled,greenled,blueled)    
main()        
