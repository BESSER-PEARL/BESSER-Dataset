from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Cliente:

    def __init__(self, numeroDeCliente: str, nombre: str, listaMascotas: str):
        self.numeroDeCliente = numeroDeCliente
        self.nombre = nombre
        self.listaMascotas = listaMascotas
        
        pass
    @property
    def numeroDeCliente(self):
        return self.__numeroDeCliente
    @numeroDeCliente.setter
    def numeroDeCliente(self, numeroDeCliente: str):
        self.__numeroDeCliente = numeroDeCliente

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def listaMascotas(self):
        return self.__listaMascotas
    @listaMascotas.setter
    def listaMascotas(self, listaMascotas: str):
        self.__listaMascotas = listaMascotas



class Perro:

    def __init__(self, fechaCastracion: str):
        self.fechaCastracion = fechaCastracion
        
        pass
    @property
    def fechaCastracion(self):
        return self.__fechaCastracion
    @fechaCastracion.setter
    def fechaCastracion(self, fechaCastracion: str):
        self.__fechaCastracion = fechaCastracion



class Gato:

    def __init__(self, ultimaDesparasitacion: str, MESES_ENTRE_DESPARASITACIONES: str):
        self.ultimaDesparasitacion = ultimaDesparasitacion
        self.MESES_ENTRE_DESPARASITACIONES = MESES_ENTRE_DESPARASITACIONES
        
        pass
    @property
    def ultimaDesparasitacion(self):
        return self.__ultimaDesparasitacion
    @ultimaDesparasitacion.setter
    def ultimaDesparasitacion(self, ultimaDesparasitacion: str):
        self.__ultimaDesparasitacion = ultimaDesparasitacion

    @property
    def MESES_ENTRE_DESPARASITACIONES(self):
        return self.__MESES_ENTRE_DESPARASITACIONES
    @MESES_ENTRE_DESPARASITACIONES.setter
    def MESES_ENTRE_DESPARASITACIONES(self, MESES_ENTRE_DESPARASITACIONES: str):
        self.__MESES_ENTRE_DESPARASITACIONES = MESES_ENTRE_DESPARASITACIONES



class Animal(ABC):

    def __init__(self, identificador: str, raza: str, nombre: str):
        self.identificador = identificador
        self.raza = raza
        self.nombre = nombre
        
        pass
    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def identificador(self):
        return self.__identificador
    @identificador.setter
    def identificador(self, identificador: str):
        self.__identificador = identificador

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre



class ILocalizable_Interface:

    pass


class CoordenadaGPS:

    def __init__(self, latitud: str, longitud: str):
        self.latitud = latitud
        self.longitud = longitud
        
        pass
    @property
    def longitud(self):
        return self.__longitud
    @longitud.setter
    def longitud(self, longitud: str):
        self.__longitud = longitud

    @property
    def latitud(self):
        return self.__latitud
    @latitud.setter
    def latitud(self, latitud: str):
        self.__latitud = latitud

