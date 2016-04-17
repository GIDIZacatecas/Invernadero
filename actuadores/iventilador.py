#!/usr/bin/python

import logging
import time

from random import randint
from threading import Thread

class iVentilador(object):

    def __init__(self):

        logging.info('Invernadero Ventilador')

    def iVentiladorPrender(self, estado):
        self.estado = ~ estado

    def iVentiladorEstado(self):
        return self.estado

# End of File
