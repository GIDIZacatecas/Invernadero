#!/usr/bin/python

import logging
import mraa

class iVentilador(object):

    def __init__(self):
        logging.info('Invernadero Ventilador')
        self.ventilador = mraa.Gpio(4)
        self.estado = 0

    def iVentiladorPrender(self, estado):
        self.ventilador.dir(mraa.DIR_OUT)
        self.ventilador.write(estado)

    def iVentiladorEstado(self):
        return self.ventilador.read()

# End of File
