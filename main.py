#!/usr/bin/python

from flask import Flask
from flask_restful import Resource, Api

from sensores.itemperatura import iTemperatura
from actuadores.iventilador import iVentilador

app = Flask(__name__)
api = Api(app)

class Temperatura(Resource):

    def __init__(self):
        self.itemperatura = iTemperatura()
        super(Temperatura, self).__init__()

    def get(self):
        temperatura = self.itemperatura.iTemperaturaLectura()
        return {'temperatura': temperatura}

class Ventilador(Resource):

    def __init__(self):
        self.iventilador = iVentilador()

    def get(self, valor):
        self.iventilador.iVentiladorPrender(valor)
        estado = self.iventilador.iVentiladorEstado()
        return {'ventilador': estado}

api.add_resource(Temperatura, '/temperatura')
api.add_resource(Ventilador, '/ventilador/<int:valor>', endpoint = 'ventilador')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
