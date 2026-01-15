from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Named:

    pass
class refact_D(Named):

    pass
class refact_C(Named):

    pass
class refact_Named:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class refact_E(Named):

    pass
class refact_B(Named):

    pass
class refact_A:

    pass