from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Ventana:

    def __init__(self, c1: Cuadrado, c2: Cuadrado, c3: Cuadrado, fig: Figura, l1: int, l2: int, etiqueta: str):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.fig = fig
        self.l1 = l1
        self.l2 = l2
        self.etiqueta = etiqueta
        
        pass
    @property
    def fig(self):
        return self.__fig
    @fig.setter
    def fig(self, fig: Figura):
        self.__fig = fig

    @property
    def l2(self):
        return self.__l2
    @l2.setter
    def l2(self, l2: int):
        self.__l2 = l2

    @property
    def c3(self):
        return self.__c3
    @c3.setter
    def c3(self, c3: Cuadrado):
        self.__c3 = c3

    @property
    def etiqueta(self):
        return self.__etiqueta
    @etiqueta.setter
    def etiqueta(self, etiqueta: str):
        self.__etiqueta = etiqueta

    @property
    def l1(self):
        return self.__l1
    @l1.setter
    def l1(self, l1: int):
        self.__l1 = l1

    @property
    def c1(self):
        return self.__c1
    @c1.setter
    def c1(self, c1: Cuadrado):
        self.__c1 = c1

    @property
    def c2(self):
        return self.__c2
    @c2.setter
    def c2(self, c2: Cuadrado):
        self.__c2 = c2



class JFrame:

    pass


class Cuadrado:

    def __init__(self, v1: int, v2: int, img: str):
        self.v1 = v1
        self.v2 = v2
        self.img = img
        
        pass
    @property
    def v2(self):
        return self.__v2
    @v2.setter
    def v2(self, v2: int):
        self.__v2 = v2

    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, img: str):
        self.__img = img

    @property
    def v1(self):
        return self.__v1
    @v1.setter
    def v1(self, v1: int):
        self.__v1 = v1



class Canvas:

    pass


class Figura:

    def __init__(self, estado: bool, valor: int):
        self.estado = estado
        self.valor = valor
        
        pass
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor: int):
        self.__valor = valor

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado: bool):
        self.__estado = estado

