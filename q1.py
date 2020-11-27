import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(11, GPIO.OUT)   # Set 11's mode is output
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set 12's mode is input, and pull up to high level(3.3V)
GPIO.output(11, GPIO.HIGH)

Led_status = 1
def swLed(ev=None):
    global Led_status
    Led_status = not Led_status
    GPIO.output(11, Led_status)  # switch led status(on-->off; off-->on)
    if Led_status == 1:
        print('Switch status: OFF')
    else:
        print('Switch status: ON')
try:
    GPIO.add_event_detect(12, GPIO.FALLING, callback=swLed, bouncetime=200) # wait for falling and set bouncetime to prevent the callback function from being called multiple times when the button is pressed
    while 1:
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.output(11, GPIO.HIGH)
    print("Done")
    GPIO.cleanup()          