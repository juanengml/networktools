import pyupm_i2clcd as lcd  # importa biblioteca para i2c 
import netools
import time,os # importa biblioteca de tempo e os para sistema operacional

Lcd = lcd.Jhd1313m1(0, 0x3E, 0x62) # Cria uma variavel para usar o display
Lcd.clear()  # Limpa tela
Lcd.setColor(255, 255, 0)  # Seta cor verde
Lcd.setCursor(0,0) # Inicia o Cursor na posicao x = 0,y = 0

while True:
 ip = netools.local_ip()
 Lcd.write(ip)  # escreve no LCD o IP
 time.sleep(0.5) # Espera d