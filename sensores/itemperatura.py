#!/usr/bin/python

import logging
import time

import pyupm_grove as grove

from random import randint
from threading import Thread

class iTemperatura(object):

    def __init__(self):

        logging.info('Invernadero Temperatura')
        self.temperatura = 0

        self.grovetemperature = grove.GroveTemp(0)

        thread = Thread(target=self.iTemperaturaActualizar)
        thread.start()

    def iTemperaturaActualizar(self):
        while True:
            self.temperature = self.grovetemperature.value()
            #self.temperatura = randint(20,40)

    def iTemperaturaLectura(self):
        return self.temperatura

# End of File
