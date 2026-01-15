from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FaultyUMLmodel3_A:

    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    @property
    def d(self) -> int:
        return self.__d

    @d.setter
    def d(self, d: int):
        self.__d = d

    @property
    def a(self) -> int:
        return self.__a

    @a.setter
    def a(self, a: int):
        self.__a = a

    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def c(self) -> int:
        return self.__c

    @c.setter
    def c(self, c: int):
        self.__c = c
