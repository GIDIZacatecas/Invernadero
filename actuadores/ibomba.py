#!/usr/bin/python

import logging
import time

from random import randint
from threading import Thread

class iBomba(object):

    def __init__(self):

        logging.info('Invernadero Bomba de Agua')

    def iBombaPrender(self, estado):
        self.estado = ~ estado

    def iBombaEstado(self):
        return self.estado
