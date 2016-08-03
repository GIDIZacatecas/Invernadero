
#!/usr/bin/python

import logging
import mraa
import time

from random import randint
from threading import Thread

class iHumedad(object):

    def __init__(self):

        logging.info('Invernadero Humedad')
        self.humedad = 0
        self.humedadumbral = 2

        self.grovehumedad = mraa.Aio(0)

        thread = Thread(target=self.iHumedadActualizar)
        thread.start()

    def iHumedadActualizar(self):
        while True:
            self.humedad = self.grovehumedad.read()
            #self.humedad = randint(20,40)

    def iHumedadLectura(self):
        return self.humedad

    def iHumedadUmbralEscritura(self, valor):
        self.humedadumbral = valor

    def iHumedadUmbralLectura(self):
        return self.humedadumbral

# Connect the Grove Moisture Sensor to analog port A1
# SIG,NC,VCC,GND
sensor = 0
 #posible codigo grove 
#while True:
 #   try:
        #print grovepi.analogRead(sensor)
        #time.sleep(.5)
    #except KeyboardInterrupt:
        #break
    #except IOError:
        #print "Error"
# End of File
