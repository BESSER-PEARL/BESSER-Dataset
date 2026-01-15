from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class B:

    pass
class kref_Named:

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
class kref_G(Named):

    pass
class kref_H(Named):

    pass
class kref_F(Named):

    pass
class kref_C(Named):

    pass
class kref_B(Named):

    pass
class kref_K(Named):

    pass
class kref_J(Named):

    pass
class kref_E(Named, B):

    pass
class kref_A(Named):

    pass