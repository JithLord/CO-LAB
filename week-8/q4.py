import time
import sys
import RPi.GPIO as GPIO

def bin_led(b1,b2,b3):
    if b3:
        GPIO.output(11, GPIO.HIGH)
    else:
        GPIO.output(11, GPIO.LOW)
    if b2:
        GPIO.output(13, GPIO.HIGH)
    else:
        GPIO.output(13, GPIO.LOW)
    if b1:
        GPIO.output(15, GPIO.HIGH)
    else:
        GPIO.output(15, GPIO.LOW)
    time.sleep(1)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setwarnings(False)

print("Binary counter")
for i in itertools.product([0,1],repeat=3):
    b1,b2,b3 = i
    bin_led(b1,b2,b3)
print("Binary counter done, Now\n")
print("Ring counter")
N=8
