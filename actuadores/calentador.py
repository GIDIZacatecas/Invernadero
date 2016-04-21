#!/usr/bin/python

import logging
import time

from random import randint
from threading import Thread

class icalentador(object):

    def __init__(self):

        logging.info('Invernadero Calentador')

    def iVentiladorPrender(self, estado):
        self.estado = ~ estado

    def iCalentadorEstado(self):
        return self.estado
