l# -*- coding: utf-8
import os
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

#define class lacze
class router():
    def start(self):
        gpio.setcfg(port.PG7, gpio.OUTPUT)
        gpio.output(port.PG7, gpio.HIGH)

    def restart(self):
        gpio.output(port.PG7, gpio.LOW)
        sleep(5)
        gpio.output(port.PG7, gpio.HIGH)
        

    def sprawdz_lacze(self):
#add server adress to dictionary
        serwery = ['google.pl', 'wp.pl', 'onet.pl', 'amazon.com', 'ebay.com', 'ovh.org', '8.8.8.8', 'orange.pl', 'play.pl', 'upc.pl']
        i = 0
        connect = 0
#im start check internet connection
        while i < 10:
            hostname = serwery[i]
#check via ping
            response = os.system("ping -c 1 " + hostname)
#here i check temperautre processor
            temperature = str(os.popen("cat /sys/devices/virtual/thermal/thermal_zone1/temp").read())
            if response == 0:
                print("Internety działają!")
#here i will shutdown system if temperature of processor is to high
		print("Temperatura procesora:" +temperature)
                if int(temperature) > 80 :
                    os.system('shutdown -h now')
                connect = 1
                break
#9 loop mean problem with connect to internet and i restart router
            elif i == 9:
                print('Brak połączenia')
                router.restart()
                break
            i = i+1

#im starting router
gpio.init()
router = router()
router.start()
a=int(1)
#im checking connection every 4 minutes
while a < 10 :
    router.sprawdz_lacze()
    sleep(10)
