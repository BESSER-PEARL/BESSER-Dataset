from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class TPagarPorEdificios1:

    pass


class TPagarJugadores1:

    def __init__(self, monto: int):
        self.monto = monto
        
        pass
    @property
    def monto(self):
        return self.__monto
    @monto.setter
    def monto(self, monto: int):
        self.__monto = monto



class TCobrarBanco1:

    pass


class TIrACarcel1:

    pass


class TAvanzarPagarDoble1:

    pass


class TAvanzar1:

    pass


class TCobrarJugadores1:

    def __init__(self, monto: int):
        self.monto = monto
        
        pass
    @property
    def monto(self):
        return self.__monto
    @monto.setter
    def monto(self, monto: int):
        self.__monto = monto



class TPagarPorEdificios:

    pass


class TPagarBanco1:

    def __init__(self, monto: int):
        self.monto = monto
        
        pass
    @property
    def monto(self):
        return self.__monto
    @monto.setter
    def monto(self, monto: int):
        self.__monto = monto



class Tarjeta1:

    def __init__(self, tipoDeCarta: str, descripcion: str):
        self.tipoDeCarta = tipoDeCarta
        self.descripcion = descripcion
        
        pass
    @property
    def tipoDeCarta(self):
        return self.__tipoDeCarta
    @tipoDeCarta.setter
    def tipoDeCarta(self, tipoDeCarta: str):
        self.__tipoDeCarta = tipoDeCarta

    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, descripcion: str):
        self.__descripcion = descripcion



class TSalirCarcel:

    pass


class Impuestos:

    pass


class CasillaTarjeta:

    pass


class Salida:

    pass


class Carcel:

    pass


class IrACarcel:

    pass


class ParqueoLibre:

    pass


class Ferrocarril:

    pass


class Propiedad:

    pass


class Servicio:

    pass


class TituloServicio:

    pass


class TituloFerrocarril:

    pass


class TituloPropiedad:

    pass


class Titulo:

    pass


class Casilla:

    pass


class Dados:

    pass


class Jugador:

    pass


class TCobrarJugadores:

    pass


class TIrACarcel:

    pass


class Monopoly1:

    def __init__(self, attribute: str):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class TAvanzarPagarDoble:

    pass


class TAvanzar:

    pass


class TCobrarBanco:

    pass


class TPagarJugadores:

    pass


class TPagarBanco:

    pass


class Tarjeta:

    pass


class Monopoly:

    pass
