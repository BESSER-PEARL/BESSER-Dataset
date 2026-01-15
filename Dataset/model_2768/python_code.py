from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class v125case5_Named:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class D:

    pass
class Named:

    pass
class v125case5_E(D, Named):

    pass
class v125case5_B(Named):

    pass
class v125case5_A(Named):

    pass
class v125case5_T(Named):

    pass
class v125case5_N(Named):

    pass
class T:

    pass
class v125case5_D(T):

    pass