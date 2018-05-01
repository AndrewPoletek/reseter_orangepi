l# -*- coding: utf-8
import os
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep

#definiuje klase lacze
class router():
    def start(self):
        gpio.setcfg(port.PG7, gpio.OUTPUT)
        gpio.output(port.PG7, gpio.HIGH)

    def restart(self):
        gpio.output(port.PG7, gpio.LOW)
        sleep(5)
        gpio.output(port.PG7, gpio.HIGH)
        

    def sprawdz_lacze(self):
#przypisuje serwery do slownika
        serwery = ['google.pl', 'wp.pl', 'onet.pl', 'amazon.com', 'ebay.com', 'ovh.org', '8.8.8.8', 'orange.pl', 'play.pl', 'upc.pl']
        #serwery = 192.168.0.10
        i = 0
        connect = 0
#zaczynam sprawdzać czy jest polaczenie z internetem
        while i < 10:
            hostname = serwery[i]
            response = os.system("ping -c 1 " + hostname)
            temperature = str(os.popen("cat /sys/devices/virtual/thermal/thermal_zone1/temp").read())
            if response == 0:
                print("Internety działają!")
		print("Temperatura procesora:" +temperature)
                if int(temperature) > 80 :
                    os.system('shutdown -h now')
                connect = 1
                break
#9 ptla oznacza brak poczenia wic resetujemy routery
            elif i == 9:
                print('Brak połączenia')
                router.restart()
                break
            i = i+1

#uruchamiam router
gpio.init()
router = router()
router.start()
a=int(1)
#sprawdzamy cze co 4 minuty
while a < 10 :
    router.sprawdz_lacze()
    sleep(10)
