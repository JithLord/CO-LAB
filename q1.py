import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)   
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(11, GPIO.HIGH)

ledStatus = 1
def swLed(ev=None):
    global ledStatus
    ledStatus = not ledStatus
    GPIO.output(11, ledStatus)
    if ledStatus == 1:
        print('Switch status: OFF','Led OFF')
    else:
        print('Switch status: ON','Led ON')
try:
    GPIO.add_event_detect(12, GPIO.FALLING, callback=swLed, bouncetime=200)
    while 1:
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.output(11, GPIO.HIGH)
    print("Done")
    GPIO.cleanup()          
