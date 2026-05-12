from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class:

    pass


class CuentaBancaria:

    def __init__(self, saldo: int):
        self.saldo = saldo
        
        pass
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo: int):
        self.__saldo = saldo



class Gato:

    def __init__(self, nombre: str, raza: str, color: str):
        self.nombre = nombre
        self.raza = raza
        self.color = color
        
        pass
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

