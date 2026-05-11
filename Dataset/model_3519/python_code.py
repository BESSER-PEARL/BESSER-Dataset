from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class modelA_B:

    def __init__(self, b: bool):
        self.b = b
        
        pass
    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: bool):
        self.__b = b


class modelA_A:

    def __init__(self, a: int):
        self.a = a
        
        pass
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: int):
        self.__a = a

