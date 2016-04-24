#!/usr/bin/python

from flask import Flask
from flask_restful import Resource, Api

from sensores.ihumedad import iHumedad
from sensores.itemperatura import iTemperatura
from actuadores.ibomba import iBomba
from actuadores.icalentador import iCalentador
from actuadores.iventilador import iVentilador

app = Flask(__name__)
api = Api(app)

class Humedad(Resource):

    def __init__(self):
        self.ihumedad = iHumedad()
        super(Humedad, self).__init__()

    def get(self):
        humedad = self.ihumedad.iHumedadLectura()
        return {'Humedad': humedad}

class Temperatura(Resource):

    def __init__(self):
        self.itemperatura = iTemperatura()
        super(Temperatura, self).__init__()

    def get(self):
        temperatura = self.itemperatura.iTemperaturaLectura()
        return {'temperatura': temperatura}

class Bomba(Resource):

    def __init__(self):
        self.ibomba = iBomba()

    def get(self, valor):
        if valor != 2:
            self.ibomba.iBombaPrender(valor)
        return {'bomba': valor}

class Calentador(Resource):

    def __init__(self):
        self.icalentador = iCalentador()

    def get(self, valor):
        if valor != 2:
            self.icalentador.iCalentadorPrender(valor)
        return {'calentador': valor}
        
class Ventilador(Resource):

    def __init__(self):
        self.iventilador = iVentilador()

    def get(self, valor):
        if valor != 2:
            self.iventilador.iVentiladorPrender(valor)
        return {'ventilador': valor}
        
api.add_resource(Humedad, '/humedad')
api.add_resource(Temperatura, '/temperatura')
api.add_resource(Bomba, '/bomba/<int:valor>', endpoint = 'bomba')
api.add_resource(Calentador, '/calentador/<int:valor>', endpoint = 'calentador')
api.add_resource(Ventilador, '/ventilador/<int:valor>', endpoint = 'ventilador')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
