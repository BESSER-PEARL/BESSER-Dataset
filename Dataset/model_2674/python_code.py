from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class refs_Named:

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
class refs_G(Named):

    pass
class refs_C(Named):

    pass
class refs_F(Named):

    pass
class refs_B(Named):

    pass
class refs_E(Named):

    pass
class refs_H(Named):

    pass
class refs_A(Named):

    pass