from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class output_B:

    def __init__(self, b: str):
        self.b = b
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b
