from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class F:

    pass
class namd_I(F):

    pass
class D:

    pass
class namd_F(D):

    pass
class B:

    pass
class namd_D(B):

    pass
class namd_Named:

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
class namd_C(Named):

    pass
class namd_E(Named):

    pass
class namd_H(Named):

    pass
class namd_G(Named):

    pass
class namd_B(Named):

    pass
class namd_A:

    pass