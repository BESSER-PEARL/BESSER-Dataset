from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class D:

    pass
class case4_Named:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Named:

    pass
class case4_B(Named):

    pass
class case4_T(Named):

    pass
class case4_E(D, Named):

    pass
class case4_A(Named):

    pass
class case4_N(Named):

    pass
class T:

    pass
class case4_D(T):

    pass