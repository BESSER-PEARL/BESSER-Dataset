from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class E(Enum):


############################################
# Definition of Classes
############################################

class a_C2:

    pass
class a_Zug:

    pass
class a_C:

    def __init__(self, a: str):
        self.a = a
        
        pass
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a


    def o(self, a_p):
        # TODO: Implement o method
        pass
