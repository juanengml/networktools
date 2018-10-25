from os import popen,system
import pyping

def local_ip():
   ip = popen("ifconfig | grep 'inet '").read().split(" ")[9]
   return ip

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
 
