from os import popen,system
import pyping

def local_ip():
   data = popen("sudo ifconfig wlan0").read().split("\n")[1].split(" ")[9]
   return data

def ping(name,ip):
   checar = pyping.ping(ip)
   print checar.avg_rtt
   if checar.avg_rtt:
       return name,ip
   else:
       return "Not","Connect"

def test_cloud():
 status = False
 b1 = "broker.mqttdashboard.com"
 b2 = "192.168.0.1"
 porta = 1883
 try:
     r = pyping.ping(b1)    # But it's udp, not real icmp
     print  (r.max_rtt,r.avg_rtt,r.min_rtt)
     status = [b1,True]
 except Exception, e:
     localnet = pyping.ping(b2)
     print (localnet.max_rtt,localnet.avg_rtt,localnet.min_rtt)
     status = [b2,True]

 return  status
 
