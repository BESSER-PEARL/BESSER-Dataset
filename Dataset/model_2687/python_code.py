from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class multiview2_Named:

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
class multiview2_F(Named):

    pass
class multiview2_B(Named):

    pass
class multiview2_E(Named):

    pass
class multiview2_C(Named):

    pass
class multiview2_A(Named):

    pass