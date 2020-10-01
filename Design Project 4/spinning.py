#Spins a servo when a button is pressed using a raspberry pi

from gpiozero import Servo
from gpiozero import Button
from time import sleep

button = Button()#insert pin number
correction = None #default angle movement of servo (may not always be 90 degrees)
servoPin = None #insert pin number
#Assumed that the pulse width for max and min rotation is 2.0 and 1.0 ms respectively. 
#Could be different depending on what is specified 
maxPw = (2.0 + correction)/1000 
minPw = (1.0 - correction)/1000
#Initializing servo
servo = Servo(servoPin, min_pulse_width=minPw, max_pulse_width=maxPw)
if button.is_held:
    servo.mid() #This is another check to ensure that the motor is in neutral position 
    servo.max() 
    #Turns servo +90 degrees 
if button.ispressed:
    servo.mid()
    #Reset the position of motor after it has rotated the door handle
    
