#!/usr/bin/python

import time

from flask import Flask
from flask_restful import Resource, Api

from sensores.ihumedad import iHumedad
from sensores.itemperatura import iTemperatura
from sensores.iproximidad import iProximidad
from actuadores.ibomba import iBomba
from actuadores.icalentador import iCalentador
from actuadores.iventilador import iVentilador
from actuadores.ifoco import iFoco
from threading import Thread

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

ihumedad = iHumedad()
itemperatura = iTemperatura()
iproximidad = iProximidad()
ibomba = iBomba()
icalentador = iCalentador()
iventilador = iVentilador()
ifoco = iFoco()
ifuncion = 1
segundos = 60
duracionfoco = 0
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

class Proximidad(Resource):

    def __init__(self):
        super(Proximidad, self).__init__()

    def get(self):
        proximidad = iproximidad.iProximidadLectura()
        return proximidad

class Bomba(Resource):
    def __init__(self):
        super(Bomba, self).__init__()
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

class BombaDuracionMin(Resource):

     def __init__(self):
         pass

     def get(self, valor):
         ibomba.iBombaDuracionMinEscritura(valor)
         return valor

class BombaDuracionMinEstado(Resource):

    def __init__(self):
        pass

    def get(self):
        return ibomba.iBombaDuracionMinLectura()

class BombaDuracionHor(Resource):

     def __init__(self):
         pass

     def get(self, valor):
         ibomba.iBombaDuracionHorEscritura(valor)
         return valor

class BombaDuracionHorEstado(Resource):

    def __init__(self):
        pass

    def get(self):
        return ibomba.iBombaDuracionHorLectura()

class BombaDuracionDia(Resource):

     def __init__(self):
         pass

     def get(self, valor):
         ibomba.iBombaDuracionDiaEscritura(valor)
         return valor

class BombaDuracionDiaEstado(Resource):

    def __init__(self):
        pass

    def get(self):
         return ibomba.iBombaDuracionDiaLectura()

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

class Foco(Resource):

    def __init__(self):
        self.ifoco = iFoco()

    def get(self, valor):
        if valor != 2:
            self.ifoco.iFocoPrender(valor)
        return valor

class FocoEstado(Resource):

    def __init__(self):
        self.ifoco = iFoco()

    def get(self):
        valor = self.ifoco.iFocoEstado()
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

def funcionProximidad(bot, update):
    proximidad = iproximidad.iProximidadLectura()
    bot.sendMessage(update.message.chat_id, text='Humedad ' + str(proximidad))

def funcionEcho(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def functionMain():
    while True:
        global segundos
        temperatura = itemperatura.iTemperaturaLectura()
        humedad = ihumedad.iHumedadLectura()
        print temperatura, humedad
        proximidad = iproximidad.iProximidadLectura()
        print proximidad
        maxima = itemperatura.iTemperaturaMaximaLectura()
        minima = itemperatura.iTemperaturaMinimaLectura()
        umbral = ihumedad.iHumedadUmbralLectura()
        global duracionfoco 
        minutos = ibomba.iBombaDuracionMinLectura()
        horas = ibomba.iBombaDuracionHorLectura()
        dias = ibomba.iBombaDuracionDiaLectura()
        auxmin = minutos
        auxhor = horas
        auxdia = dias
        print "Temperatura Maxima " + str(maxima)
        print "Temperatura Minima " + str(minima)

        if temperatura > maxima:
            iventilador.iVentiladorPrender(1)
            icalentador.iCalentadorPrender(0)
            print "Ventilador  Prendido \n"
        if temperatura < minima:
            print "Calentador Prendido \n"
            icalentador.iCalentadorPrender(1)
            iventilador.iVentiladorPrender(0)

        if humedad <= umbral :
            ibomba.iBombaPrender(0)         
        if humedad >= umbral:
            if segundos >= 1 and segundos <= 60 :
                 ibomba.iBombaPrender(1)
                 print "Bomba Prendida \n"
                 segundos = segundos-1
                 print "Segundos : "
                 print segundos
                 print " Minutos : "
                 print minutos
                 print "Horas : "
                 print horas
                 print "Dias : "
                 print dias
            elif segundos == 0 :
                 if minutos >= 1 and minutos <= 60 :
                      minutos = minutos-1
                      ibomba.iBombaDuracionMinEscritura(minutos)
                      segundos = 60
                 elif minutos == 0 :
                       if horas >= 1 and horas <= 24 :
                           horas = horas-1
                           minutos = 59
                           segundos = 60
                           ibomba.iBombaDuracionHorEscritura(horas)
                           ibomba.iBombaDuracionMinEscritura(minutos)
                       elif horas == 0 :
                           if dias >=1 and dias <=15 :
                               dias = dias - 1
                               ibomba.iBombaDuracionDiaEscritura(dias)
                               horas = 24
                               segundos = 60
                               ibomba.iBombaDuracionHorEscritura(horas)
                           elif dias == 0 :
                                if horas == 0 and minutos == 0 :
                                     print "Riego Finalizado \n"
                                     ibomba.iBombaPrender(0)
                                     if humedad >= umbral :
                                           segundos = 60
                                           minutos = auxmin
                                           horas = auxhor
                                           dias = auxdia
           
        if proximidad >= 1 and duracionfoco == 0 :
             ifoco.iFocoPrender(1)
             duracionfoco = 30  
             print " Movimiento Detectado "
             print " Luces Encendidas "
        elif proximidad >= 1 and duracionfoco > 0 :
             print "Luces Encendidas"
             duracionfoco = duracionfoco -1 
        elif proximidad == 0 and duracionfoco > 0 :
             duracionfoco = duracionfoco -1
             print "Luces Encendidas"
        elif proximidad == 0 and duracionfoco == 0 :
             ifoco.iFocoPrender(0)
             print "Luces Apagadas "
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
api.add_resource(Proximidad, '/proximidad')
api.add_resource(BombaDuracionDia, '/bomba/duracion/dias/<int:valor>', endpoint = 'bombaduraciondia')
api.add_resource(BombaDuracionDiaEstado, '/bomba/duracion/dias/estado')
api.add_resource(Bomba, '/bomba/<int:valor>', endpoint = 'bomba')
api.add_resource(BombaEstado, '/bomba/estado')
api.add_resource(Foco, '/foco/<int:valor>', endpoint = 'foco')
api.add_resource(FocoEstado, '/foco/estado')


api.add_resource(Calentador, '/calentador/<int:valor>', endpoint = 'calentador')
api.add_resource(CalentadorEstado, '/calentador/estado')

api.add_resource(Ventilador, '/ventilador/<int:valor>', endpoint = 'ventilador')
api.add_resource(VentiladorEstado, '/ventilador/estado')

api.add_resource(BombaDuracionMin, '/bomba/duracion/minutos/<int:valor>', endpoint = 'bombaduracionmin')
api.add_resource(BombaDuracionMinEstado, '/bomba/duracion/minutos/estado')
api.add_resource(BombaDuracionHor, '/bomba/duracion/horas/<int:valor>', endpoint = 'bombaduracionhor')
api.add_resource(BombaDuracionHorEstado, '/bomba/duracion/horas/estado')

if __name__ == '__main__':

    threadmain = Thread(target=functionMain)
    threadmain.start()

    updater = Updater("216787884:AAHv_6IIlANC-yuFJnyWBXPNUQJ9Nm0pRcY")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("humedad", funcionHumedad))
    dp.add_handler(CommandHandler("temperatura", funcionTemperatura))
    dp.add_handler(CommandHandler("proximidad", funcionProximidad))
    dp.add_handler(MessageHandler([Filters.text], funcionEcho))

    updater.start_polling()

    app.run(host='0.0.0.0', debug=False, threaded=True)
    #app.run(host='0.0.0.0', debug=False)

    updater.idle()
#                                                                                                                                                                                                                                                                                                                                                                                m1íˆíí÷¼>œu8tì4ÿ¸Þ©ß9ÿIãÓD—b×ÐgéÏ½ÝÝŸz„{>ôò÷¶öñô5õsõ7pÔaÿR7È>X7Ä1T?Ì9Ü8Â=Ò<Ê7Ú>&8öq\l¼{Bjb`RnrtJujfZgzeÆdf{ÖfödÎmîfÞf
