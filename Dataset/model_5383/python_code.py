from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class p_B:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class p_A:

    pass