import time
import sys
import RPi.GPIO as GPIO
import itertools

def bin_led(b4,b3,b2,b1):
    if b4:
        GPIO.output(31, GPIO.HIGH)
    else:
        GPIO.output(31, GPIO.LOW)
    if b3:
        GPIO.output(33, GPIO.HIGH)
    else:
        GPIO.output(33, GPIO.LOW)
    if b2:
        GPIO.output(35, GPIO.HIGH)
    else:
        GPIO.output(35, GPIO.LOW)
    if b1:
        GPIO.output(37, GPIO.HIGH)
    else:
        GPIO.output(37, GPIO.LOW)
    time.sleep(1)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setwarnings(False)

print("Ring Counter")
count = 0
b1,b2,b3,b4 = 0,0,0,1
while (1):
    b1,b2,b3,b4 = b4,b1,b2,b3
    print(b1,b2,b3,b4)
    if ((b1,b2,b3,b4)==(1,0,0,0)):
        count+=1
    if count==2:
        break
    bin_led(b1,b2,b3,b4)

print("Twisted Ring counter")
b1,b2,b3,b4 = 0,0,0,0

while ((b1,b2,b3,b4)!=(0,0,0,1)):
    b1,b2,b3,b4 = 1-b4,b1,b2,b3
    print(b1,b2,b3,b4)
    bin_led(b1,b2,b3,b4)
    
GPIO.output(37, GPIO.LOW)
GPIO.output(35, GPIO.LOW)
GPIO.output(33, GPIO.LOW)
GPIO.output(31, GPIO.LOW)
