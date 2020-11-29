import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)  #Output
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Input 1
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Input 2
GPIO.output(11, GPIO.HIGH)

try:
    while(1):
        a,b = GPIO.input(35),GPIO.input(37)
        c = a or b
        if c:
            GPIO.output(11, GPIO.HIGH)
        else:
            GPIO.output(11, GPIO.LOW)        
except KeyboardInterrupt:
    GPIO.output(11, GPIO.HIGH)
    
try:
    while(1):
        a,b = GPIO.input(35),GPIO.input(37)
        c = a or b
        if c:
            GPIO.output(11, GPIO.HIGH)
        else:
            GPIO.output(11, GPIO.LOW)
        
except KeyboardInterrupt:
    GPIO.output(11, GPIO.HIGH)