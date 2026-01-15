from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Basic_C:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        
    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def a(self) -> int:
        return self.__a

    @a.setter
    def a(self, a: int):
        self.__a = a
