import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime

DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
disp.begin(contrast=40)
disp.clear()

def msg(text):
 disp.clear()
 disp.display()
 image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
 draw = ImageDraw.Draw(image)
 draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
 font = ImageFont.load_default()
 draw.text((1,10), text, font=font)
# draw.text((2,20), "Quero Caldo",font=font)
# draw.text((3,30), "De Mocoto", font=font)
 disp.image(image)
 disp.display()


while  True:
 print('Press Ctrl-C to quit.')
 relogio = "%.8s" % str(datetime.now()).split()[1]
 msg(relogio)
 time.sleep(1) 
