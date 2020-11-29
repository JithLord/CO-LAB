import RPi.GPIO as GPIO
import time
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)   
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(11, GPIO.HIGH)

ledStatus = 1
RESET_PIN = digitalio.DigitalInOut(board.D4)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, reset=RESET_PIN)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)
def swLed(ev=None):
    global ledStatus
    ledStatus = not ledStatus
    GPIO.output(11, ledStatus)
    if ledStatus == 1:
        print('Switch status: OFF','Led OFF')
        draw.text((0, 0), "Switch status: OFF", font=font, fill=255)
        oled.image(image)
        oled.show()
    else:
        print('Switch status: ON','Led ON')
        draw.text((0, 0), "Switch status: ON", font=font, fill=255)
        oled.image(image)
        oled.show()
try:
    GPIO.add_event_detect(12, GPIO.FALLING, callback=swLed, bouncetime=200)
    while 1:
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.output(11, GPIO.HIGH)
    print("Done")
    GPIO.cleanup()      