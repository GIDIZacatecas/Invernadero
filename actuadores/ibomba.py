#!/usr/bin/python

import logging
import mraa

from flask_restful import Resource

class iBomba():

    def __init__(self):
        logging.info('Invernadero Bomba de Agua')
        self.bomba = mraa.Gpio(2)
        self.bomba.dir(mraa.DIR_OUT)
        self.estado = 0

    def iBombaPrender(self, estado):
        self.bomba.write(estado)

    def iBombaEstado(self):
        return self.estado
