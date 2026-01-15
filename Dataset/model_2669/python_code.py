from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class B:

    pass
class conts_Named:

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
class conts_F(Named):

    pass
class conts_C(Named):

    pass
class conts_E(Named, B):

    pass
class conts_G(Named):

    pass
class conts_B(Named):

    pass
class conts_H(Named):

    pass
class conts_A(Named):

    pass