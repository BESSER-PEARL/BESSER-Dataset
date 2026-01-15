from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class multiview4_Named:

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
class multiview4_F(Named):

    pass
class multiview4_B(Named):

    pass
class multiview4_E(Named):

    pass
class multiview4_C(Named):

    pass
class multiview4_A(Named):

    pass