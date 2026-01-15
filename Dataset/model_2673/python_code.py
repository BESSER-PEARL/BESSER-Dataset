from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class reference_Named:

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
class reference_G(Named):

    pass
class reference_H(Named):

    pass
class reference_E(Named):

    pass
class reference_B(Named):

    pass
class reference_C(Named):

    pass
class reference_F(Named):

    pass
class reference_A(Named):

    pass