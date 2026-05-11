from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class refact_Named:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class refact_A:

    pass
class Named:

    pass
class refact_E(Named):

    pass
class refact_B(Named):

    pass
class refact_C(Named):

    pass
class refact_D(Named):

    pass