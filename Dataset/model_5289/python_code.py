from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class minimalB_B:

    def __init__(self, b: int):
        self.b = b
        
        pass
    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

