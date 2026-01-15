from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mydsl_W:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class W:

    pass
class mydsl_C(W):

    pass
class mydsl_B(W):

    pass
class mydsl_D(W):

    pass
class mydsl_L(W):

    pass
class mydsl_A(W):

    pass