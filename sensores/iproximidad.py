import logging 
import time
import mraa
import datetime
from threading import Thread


class iProximidad(object):

    def __init__(self):
        logging.info('Invernadero Proximidad')
        self.proximidad = 0
        
        self.pin = mraa.Gpio(7)

        self.pin.dir(mraa.DIR_IN)
        thread = Thread(target=self.iProximidadActualizar)
        thread.start()


    def iProximidadActualizar(self):
        while True:
            self.proximidad = self.pin.read()    
    
    def iProximidadLectura(self):
        return self.proximidad
  























