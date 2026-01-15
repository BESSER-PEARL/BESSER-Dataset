from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class manypov_Named:

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
class manypov_M(Named):

    pass
class manypov_F(Named):

    pass
class manypov_K(Named):

    pass
class manypov_J(Named):

    pass
class manypov_E(Named):

    pass
class manypov_B(Named):

    pass
class manypov_C(Named):

    pass
class manypov_JK(Named):

    pass
class manypov_A(Named):

    pass