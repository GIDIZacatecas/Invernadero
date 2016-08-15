import time
import logging
import mraa

from flask_restful import Resource

class iFoco():

    def __init__(self):
        logging.info('Invernadero Focos')
        self.foco = mraa.Gpio(6)

        self.estado = 0

    def iFocoPrender(self, estado):
        self.foco.dir(mraa.DIR_OUT)
        self.foco.write(estado)
        

    def iFocoEstado(self):
        return self.foco.read()
