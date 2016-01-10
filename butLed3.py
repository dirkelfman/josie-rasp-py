import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
import ultrasonic_2 as Sonic

    
from gpiozero import Button
from gpiozero import LED
from time import sleep
from pygame import mixer

Sonic.init()
#duck = mixer.Sound("/usr/share/scratch/Media/Sounds/Animal/Duck.wav")

button = Button(22)
button.wait_for_press();
#duck.play()
print('im so awesome')

led = LED(17)

def food():
    print (' ')
    print ('measuring')
    dist = Sonic.measureDistance()
    print(' measured ' , dist)
    print (' ')
    
while True:
    food()
    led.on()
    sleep(1)
    led.off()
    sleep(1)




