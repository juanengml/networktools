import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import netools

DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))
disp.begin(contrast=40)
disp.clear()
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
font = ImageFont.load_default()
 

def msg(name,ip):
 disp.clear()
 disp.display()
 draw.text((1,10), name, font=font)
 draw.text((1,20), ip, font=font)
 disp.image(image)
 disp.display()


while  True:
 print('Press Ctrl-C to quit.')
 ip = netools.local_ip()
 iot1 = netools.ping("Edson","192.168.100.13")
 msg("Pi0",ip)
 time.sleep(2)
 msg(iot1[0],iot1[1])
 time.sleep(2)
 

 
