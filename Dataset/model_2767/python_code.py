from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class D:

    pass
class ref3_Named:

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
class ref3_A(Named):

    pass
class ref3_T(Named):

    pass
class ref3_E(D, Named):

    pass
class ref3_B(Named):

    pass
class ref3_N(Named):

    pass
class T:

    pass
class ref3_D(T):

    pass