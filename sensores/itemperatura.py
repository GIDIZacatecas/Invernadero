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
        self.temperaturamaxima = 27
        self.temperaturaminima = 13

        self.grovetemperatura = grove.GroveTemp(0)

        thread = Thread(target=self.iTemperaturaActualizar)
        thread.start()

    def iTemperaturaActualizar(self):
        while True:
            self.temperatura = self.grovetemperatura.value()
            #self.temperatura = randint(20,40)

    def iTemperaturaLectura(self):
        return self.temperatura

    def iTemperaturaMaximaEscritura(self, valor):
        self.temperaturamaxima = valor

    def iTemperaturaMaximaLectura(self):
        return self.temperaturamaxima

    def iTemperaturaMinimaEscritura(self, valor):
        self.temperaturaminima = valor

    def iTemperaturaMinimaLectura(self):
        return self.temperaturaminima

# End of File
