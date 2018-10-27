import pyupm_i2clcd as lcd  # importa biblioteca para i2c 
import netools
import time,os # importa biblioteca de tempo e os para sistema operacional

Lcd = lcd.Jhd1313m1(0, 0x3E, 0x62) # Cria uma variavel para usar o display
Lcd.clear()  # Limpa tela
Lcd.setColor(255, 255, 0)  # Seta cor verde

def msg(name,ip):
    Lcd.clear()
    Lcd.setCursor(0,0) # Inicia o Cursor na posicao x = 0,y = 0
    Lcd.write(name)
    Lcd.setCursor(0,1) # Inicia o Cursor na posicao x = 0,y = 0
    Lcd.write(ip)

while True:
 ip = netools.local_ip()
 iot0 = netools.ping("Pi0: ","192.168.100.10")
 msg("Edson: ",ip)
 time.sleep(2)
 msg(iot0[0],iot0[1])
 time.sleep(2)




