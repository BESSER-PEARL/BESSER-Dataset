from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Basic4_C:

    def __init__(self, d: bool, a: bool, b: bool, c: bool):
        self.d = d
        self.a = a
        self.b = b
        self.c = c
        
        pass
    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: bool):
        self.__b = b


    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, d: bool):
        self.__d = d


    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c: bool):
        self.__c = c


    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: bool):
        self.__a = a

