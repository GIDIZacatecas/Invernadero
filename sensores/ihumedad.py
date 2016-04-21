
#!/usr/bin/python

import logging
import time

from random import randint
from threading import Thread

class iHumedad(object):

    def __init__(self):

        logging.info('Invernadero Humedad')
        self.humedad = 0

        thread = Thread(target=self.iHumedadActualizar)
        thread.start()

    def iHumedadActualizar(self):
        while True:
            self.humedad = randint(20,40)

    def iHumedadLectura(self):
        return self.humedad

# End of File
