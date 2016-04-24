#!/usr/bin/python

import logging
import mraa

class iVentilador(object):

    def __init__(self):
        logging.info('Invernadero Ventilador')
        self.ventilador = mraa.Gpio(4)
        self.ventilador.dir(mraa.DIR_OUT)
        self.estado = 0

    def iVentiladorPrender(self, estado):
        self.ventilador.write(estado)

    def iVentiladorEstado(self):
        return self.estado

# End of File
