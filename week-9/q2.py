import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(11, GPIO.HIGH)

buzzStatus = 1
def swLed(ev=None):
    global buzzStatus
    buzzStatus = not buzzStatus
    GPIO.output(11, buzzStatus)
    if buzzStatus == 1:
        print('Switch status: OFF')
    else:
        print('Switch status: ON')
try:
    GPIO.add_event_detect(12, GPIO.FALLING, callback=swLed, bouncetime=200)
    while 1:
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.output(11, GPIO.HIGH)
    print("Done")
    GPIO.cleanup()          
