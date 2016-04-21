#!/usr/bin/python

from flask import Flask
from flask_restful import Resource, Api

from sensores.itemperatura import iTemperatura
from sensores.iHumedad import iHumedad
from actuadores.iventilador import iVentilador

app = Flask(__name__)
api = Api(app)

class Humedad(Resource):

    def __init__(self):
        self.iHumedad = iHumedad()
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

class Ventilador(Resource):

    def __init__(self):
        self.iventilador = iVentilador()

    def get(self, valor):
        self.iventilador.iVentiladorPrender(valor)
        estado = self.iventilador.iVentiladorEstado()
        return {'ventilador': estado}
        
class Calentador(Resource):

    def __init__(self):
        self.icalentador = iCalentador()

    def get(self, valor):
        self.icalentador.iCalentadorPrender(valor)
        estado = self.icalentador.iCalentadorEstado()
        return {'calentador': estado}
        
class Bomba(Resource):

    def __init__(self):
        self.ibomba = iBomba()

    def get(self, valor):
        self.ibomba.iBombaPrender(valor)
        estado = self.ibomba.iBombaEstado()
        return {'bomba': estado}
        
api.add_resource(Temperatura, '/temperatura')
api.add_resource(Humedad, '/humedad')
api.add_resource(Ventilador, '/ventilador/<int:valor>', endpoint = 'ventilador')
api.add_resource(Calentador, '/calentador/<int:valor>', endpoint = 'calentador')
api.add_resource(Bomba, '/bomba/<int:valor>', endpoint = 'bomba')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
