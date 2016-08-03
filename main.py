#!/usr/bin/python

import time

from flask import Flask
from flask_restful import Resource, Api

from sensores.ihumedad import iHumedad
from sensores.itemperatura import iTemperatura
from actuadores.ibomba import iBomba
from actuadores.icalentador import iCalentador
from actuadores.iventilador import iVentilador

from threading import Thread

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

ihumedad = iHumedad()
itemperatura = iTemperatura()
ibomba = iBomba()
icalentador = iCalentador()
iventilador = iVentilador()
ifuncion = 1

app = Flask(__name__)
api = Api(app)

class Funcion(Resource):

    def __init__(self):
        pass

    def get(self, valor):
        global ifuncion
        if valor == 1:
            ifuncion = valor
        else:
            ifuncion = 0
        return valor
        
class FuncionEstado(Resource):

    def __init__(self):
        pass

    def get(self):
        global ifuncion
        return ifuncion

class Humedad(Resource):

    def __init__(self):
        super(Humedad, self).__init__()

    def get(self):
        humedad = ihumedad.iHumedadLectura()
        return humedad

class HumedadUmbral(Resource):

    def __init__(self):
        pass

    def get(self, valor):
        ihumedad.iHumedadUmbralEscritura(valor)
        return valor

class HumedadUmbralEstado(Resource):

    def __init__(self):
        pass

    def get(self):
        return ihumedad.iHumedadUmbralLectura()

class Temperatura(Resource):

    def __init__(self):
        super(Temperatura, self).__init__()

    def get(self):
        temperatura = itemperatura.iTemperaturaLectura()
        return temperatura

class TemperaturaMaxima(Resource):

    def __init__(self):
        pass

    def get(self, valor):
        itemperatura.iTemperaturaMaximaEscritura(valor)
        return valor

class TemperaturaMaximaEstado(Resource):

    def __init__(self):
        pass

    def get(self):
        return itemperatura.iTemperaturaMaximaLectura()

class TemperaturaMinima(Resource):

    def __init__(self):
        pass

    def get(self, valor):
        itemperatura.iTemperaturaMinimaEscritura(valor)
        return valor

class TemperaturaMinimaEstado(Resource):

    def __init__(self):
        pass

    def get(self):
        return itemperatura.iTemperaturaMinimaLectura()

class Bomba(Resource):

    def __init__(self):
        self.ibomba = iBomba()

    def get(self, valor):
        if valor != 2:
            self.ibomba.iBombaPrender(valor)
        return valor

class BombaEstado(Resource):

    def __init__(self):
        self.ibomba = iBomba()

    def get(self):
        valor = self.ibomba.iBombaEstado()
        return valor

class Calentador(Resource):

    def __init__(self):
        self.icalentador = iCalentador()

    def get(self, valor):
        if valor != 2:
            self.icalentador.iCalentadorPrender(valor)
        return valor

class CalentadorEstado(Resource):

    def __init__(self):
        self.icalentador = iCalentador()

    def get(self):
        valor = self.icalentador.iCalentadorEstado()
        return valor
        
class Ventilador(Resource):

    def __init__(self):
        self.iventilador = iVentilador()

    def get(self, valor):
        if valor != 2:
            self.iventilador.iVentiladorPrender(valor)
        return valor
        
class VentiladorEstado(Resource):

    def __init__(self):
        self.iventilador = iVentilador()

    def get(self):
        valor = self.iventilador.iVentiladorEstado()
        return valor

def funcionHumedad(bot, update):
    humedad = ihumedad.iHumedadLectura()
    bot.sendMessage(update.message.chat_id, text='Humedad ' + str(humedad))

def funcionTemperatura(bot, update):
    temperatura = itemperatura.iTemperaturaLectura()
    bot.sendMessage(update.message.chat_id, text='Temperatura ' + str(temperatura))

def funcionEcho(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def functionMain():
    while True:
        temperatura = itemperatura.iTemperaturaLectura()
        humedad = ihumedad.iHumedadLectura()
        print temperatura, humedad

        maxima = itemperatura.iTemperaturaMaximaLectura()
        minima = itemperatura.iTemperaturaMinimaLectura()
        print "Temperatura Maxima " + str(maxima)
        print "Temperatura Minima " + str(minima)

        if humedad == 0 and temperatura != 100:
            print "Dispositivos Prendidos"
            ibomba.iBombaPrender(1)
            icalentador.iCalentadorPrender(1)
            iventilador.iVentiladorPrender(1)
        elif humedad > 0 and temperatura != 100:
            print "Dispositivos Apagados"
            ibomba.iBombaPrender(0)
            icalentador.iCalentadorPrender(0)
            iventilador.iVentiladorPrender(0)
        
        time.sleep(1)

'''
http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html
http://learnpythonthehardway.org/book/ex28.html
'''

api.add_resource(Funcion, '/funcion/<int:valor>', endpoint = 'funcion')
api.add_resource(FuncionEstado, '/funcion/estado')

api.add_resource(Humedad, '/humedad')
api.add_resource(HumedadUmbral, '/humedad/umbral/<int:valor>', endpoint = 'humedadumbral')
api.add_resource(HumedadUmbralEstado, '/humedad/umbral/estado')
api.add_resource(Temperatura, '/temperatura')
api.add_resource(TemperaturaMaxima, '/temperatura/maxima/<int:valor>', endpoint = 'temperaturamaxima')
api.add_resource(TemperaturaMaximaEstado, '/temperatura/maxima/estado')
api.add_resource(TemperaturaMinima, '/temperatura/minima/<int:valor>', endpoint = 'temperaturaminima')
api.add_resource(TemperaturaMinimaEstado, '/temperatura/minima/estado')

api.add_resource(Bomba, '/bomba/<int:valor>', endpoint = 'bomba')
api.add_resource(BombaEstado, '/bomba/estado')
api.add_resource(Calentador, '/calentador/<int:valor>', endpoint = 'calentador')
api.add_resource(CalentadorEstado, '/calentador/estado')
api.add_resource(Ventilador, '/ventilador/<int:valor>', endpoint = 'ventilador')
api.add_resource(VentiladorEstado, '/ventilador/estado')

if __name__ == '__main__':

    threadmain = Thread(target=functionMain)
    threadmain.start()

    updater = Updater("216787884:AAHv_6IIlANC-yuFJnyWBXPNUQJ9Nm0pRcY")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("humedad", funcionHumedad))
    dp.add_handler(CommandHandler("temperatura", funcionTemperatura))
    dp.add_handler(MessageHandler([Filters.text], funcionEcho))

    updater.start_polling()

    #app.run(host='0.0.0.0', debug=True, threaded=True)
    app.run(host='0.0.0.0', debug=False)

    updater.idle()
