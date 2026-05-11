from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Basic2_C:

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        
        pass
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: int):
        self.__a = a


    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b


    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c: int):
        self.__c = c

