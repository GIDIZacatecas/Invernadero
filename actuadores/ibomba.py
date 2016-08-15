#!/usr/bin/python

import logging
import mraa

from flask_restful import Resource

class iBomba(object):

    def __init__(self):
        logging.info('Invernadero Bomba de Agua')
        self.bomba = mraa.Gpio(2)
        self.estado = 0
        self.bombaduracionmin = 0
        self.bombaduracionhor = 0
        self.bombaduraciondia = 0

    def iBombaPrender(self, estado):
        self.bomba.dir(mraa.DIR_OUT)
        self.bomba.write(estado)

    def iBombaEstado(self):
        return self.bomba.read()

    def iBombaDuracionMinEscritura(self, valor):
        self.bombaduracionmin = valor

    def iBombaDuracionMinLectura(self):
        return self.bombaduracionmin

    def iBombaDuracionHorEscritura(self, valor):
        self.bombaduracionhor = valor

    def iBombaDuracionHorLectura(self):
        return self.bombaduracionhor

    def iBombaDuracionDiaEscritura(self, valor):
        self.bombaduraciondia = valor

    def iBombaDuracionDiaLectura(self):
        return self.bombaduraciondia
