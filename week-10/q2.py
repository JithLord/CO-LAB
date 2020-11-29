import sys
import board
import digitalio
from PIL import Image
import adafruit_ssd1306

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C, reset=RESET_PIN)

# Clear display.
oled.fill(0)
oled.show()

# Open, resize, and convert image to Black and White
image = (
    Image.open(sys.argv[1])
    .resize((oled.width, oled.height), Image.BICUBIC)
    .convert("1")
)

# Display the converted image
oled.image(image)
oled.show()
