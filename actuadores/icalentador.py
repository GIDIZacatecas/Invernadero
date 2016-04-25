#!/usr/bin/python

import logging
import mraa

class iCalentador(object):

    def __init__(self):
        logging.info('Invernadero Calentador')
        self.calentador = mraa.Gpio(3)
        self.estado = 0

    def iCalentadorPrender(self, estado):
        self.calentador.dir(mraa.DIR_OUT)
        self.calentador.write(estado)

    def iCalentadorEstado(self):
        return self.calentador.read()
