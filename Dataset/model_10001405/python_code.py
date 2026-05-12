from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class mundo_Ratite:

    def __init__(self, quilla: bool):
        self.quilla = quilla
        
        pass
    @property
    def quilla(self):
        return self.__quilla
    @quilla.setter
    def quilla(self, quilla: bool):
        self.__quilla = quilla



class mundo_Tinamues:

    def __init__(self, velocidadTierra: str):
        self.velocidadTierra = velocidadTierra
        
        pass
    @property
    def velocidadTierra(self):
        return self.__velocidadTierra
    @velocidadTierra.setter
    def velocidadTierra(self, velocidadTierra: str):
        self.__velocidadTierra = velocidadTierra



class mundo_Neoaves:

    def __init__(self, longitudPatas: str, numeroDedosPatas: str):
        self.longitudPatas = longitudPatas
        self.numeroDedosPatas = numeroDedosPatas
        
        pass
    @property
    def longitudPatas(self):
        return self.__longitudPatas
    @longitudPatas.setter
    def longitudPatas(self, longitudPatas: str):
        self.__longitudPatas = longitudPatas

    @property
    def numeroDedosPatas(self):
        return self.__numeroDedosPatas
    @numeroDedosPatas.setter
    def numeroDedosPatas(self, numeroDedosPatas: str):
        self.__numeroDedosPatas = numeroDedosPatas



class mundo_Galloanserae:

    def __init__(self, tipo: str, reproduccion: str, DOMESTICA: str, CAZA: str, POLIGAMA: str, MONOGAMA: str):
        self.tipo = tipo
        self.reproduccion = reproduccion
        self.DOMESTICA = DOMESTICA
        self.CAZA = CAZA
        self.POLIGAMA = POLIGAMA
        self.MONOGAMA = MONOGAMA
        
        pass
    @property
    def CAZA(self):
        return self.__CAZA
    @CAZA.setter
    def CAZA(self, CAZA: str):
        self.__CAZA = CAZA

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def POLIGAMA(self):
        return self.__POLIGAMA
    @POLIGAMA.setter
    def POLIGAMA(self, POLIGAMA: str):
        self.__POLIGAMA = POLIGAMA

    @property
    def DOMESTICA(self):
        return self.__DOMESTICA
    @DOMESTICA.setter
    def DOMESTICA(self, DOMESTICA: str):
        self.__DOMESTICA = DOMESTICA

    @property
    def MONOGAMA(self):
        return self.__MONOGAMA
    @MONOGAMA.setter
    def MONOGAMA(self, MONOGAMA: str):
        self.__MONOGAMA = MONOGAMA

    @property
    def reproduccion(self):
        return self.__reproduccion
    @reproduccion.setter
    def reproduccion(self, reproduccion: str):
        self.__reproduccion = reproduccion



class mundo_Paleognato:

    def __init__(self, numeroHuesosPaladar: str):
        self.numeroHuesosPaladar = numeroHuesosPaladar
        
        pass
    @property
    def numeroHuesosPaladar(self):
        return self.__numeroHuesosPaladar
    @numeroHuesosPaladar.setter
    def numeroHuesosPaladar(self, numeroHuesosPaladar: str):
        self.__numeroHuesosPaladar = numeroHuesosPaladar



class mundo_Neognato:

    def __init__(self, numeroHuesosPata: str, longitudTercerDedo: str):
        self.numeroHuesosPata = numeroHuesosPata
        self.longitudTercerDedo = longitudTercerDedo
        
        pass
    @property
    def longitudTercerDedo(self):
        return self.__longitudTercerDedo
    @longitudTercerDedo.setter
    def longitudTercerDedo(self, longitudTercerDedo: str):
        self.__longitudTercerDedo = longitudTercerDedo

    @property
    def numeroHuesosPata(self):
        return self.__numeroHuesosPata
    @numeroHuesosPata.setter
    def numeroHuesosPata(self, numeroHuesosPata: str):
        self.__numeroHuesosPata = numeroHuesosPata



class mundo_Neornithe:

    def __init__(self, rangoMetabolico: str, ALTO: str, BAJO: str, MEDIO: str, longitudCola: str, densidadOsea: str):
        self.rangoMetabolico = rangoMetabolico
        self.ALTO = ALTO
        self.BAJO = BAJO
        self.MEDIO = MEDIO
        self.longitudCola = longitudCola
        self.densidadOsea = densidadOsea
        
        pass
    @property
    def BAJO(self):
        return self.__BAJO
    @BAJO.setter
    def BAJO(self, BAJO: str):
        self.__BAJO = BAJO

    @property
    def densidadOsea(self):
        return self.__densidadOsea
    @densidadOsea.setter
    def densidadOsea(self, densidadOsea: str):
        self.__densidadOsea = densidadOsea

    @property
    def rangoMetabolico(self):
        return self.__rangoMetabolico
    @rangoMetabolico.setter
    def rangoMetabolico(self, rangoMetabolico: str):
        self.__rangoMetabolico = rangoMetabolico

    @property
    def MEDIO(self):
        return self.__MEDIO
    @MEDIO.setter
    def MEDIO(self, MEDIO: str):
        self.__MEDIO = MEDIO

    @property
    def longitudCola(self):
        return self.__longitudCola
    @longitudCola.setter
    def longitudCola(self, longitudCola: str):
        self.__longitudCola = longitudCola

    @property
    def ALTO(self):
        return self.__ALTO
    @ALTO.setter
    def ALTO(self, ALTO: str):
        self.__ALTO = ALTO



class mundo_Ave:

    def __init__(self, color: str, altura: str, factorPeso: str):
        self.color = color
        self.altura = altura
        self.factorPeso = factorPeso
        
        pass
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: str):
        self.__altura = altura

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def factorPeso(self):
        return self.__factorPeso
    @factorPeso.setter
    def factorPeso(self, factorPeso: str):
        self.__factorPeso = factorPeso

