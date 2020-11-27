import time
import sys
import RPi.GPIO as GPIO
import itertools

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setwarnings(False)

N=int(input("Enter the number of times: "))
while N:
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(11,GPIO.LOW)
    N-=1
