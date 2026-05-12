from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Gato:

    def __init__(self, Nombre: str, Raza: str, Color: str):
        self.Nombre = Nombre
        self.Raza = Raza
        self.Color = Color
        
        pass
    @property
    def Raza(self):
        return self.__Raza
    @Raza.setter
    def Raza(self, Raza: str):
        self.__Raza = Raza

    @property
    def Color(self):
        return self.__Color
    @Color.setter
    def Color(self, Color: str):
        self.__Color = Color

    @property
    def Nombre(self):
        return self.__Nombre
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self.__Nombre = Nombre

