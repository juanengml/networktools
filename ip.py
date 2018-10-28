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
 

def msg(name1,name2,ip1,ip2):
 disp.clear()
 disp.clear()
 disp.display()
 draw.text((1,5), "  "+name1, font=font)
 draw.text((1,15), ip1, font=font)
 draw.text((1,27), "  "+name2, font=font)
 draw.text((1,37), ip2, font=font)
 disp.image(image)
 disp.display()


while  True:
 print('Press Ctrl-C to quit.')
 ip = netools.local_ip()
 iot1 = netools.ping("Edson","192.168.100.13")
 time.sleep(0.5)
 msg("Pi0",iot1[0],ip,iot1[1])
 time.sleep(0.5)
# msg(iot1[0],iot1[1])
# time.sleep(0.5)
 

 
