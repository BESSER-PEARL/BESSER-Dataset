from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class containment_Named:

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
class containment_B(Named):

    pass
class containment_E(Named):

    pass
class containment_H(Named):

    pass
class containment_C(Named):

    pass
class containment_G(Named):

    pass
class containment_F(Named):

    pass
class containment_A(Named):

    pass