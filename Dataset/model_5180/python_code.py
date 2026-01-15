from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class manypov2_Named:

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
class manypov2_M(Named):

    pass
class manypov2_C(Named):

    pass
class manypov2_N(Named):

    pass
class manypov2_F(Named):

    pass
class manypov2_B(Named):

    pass
class manypov2_K(Named):

    pass
class manypov2_J(Named):

    pass
class manypov2_E(Named):

    pass
class manypov2_JK(Named):

    pass
class manypov2_A(Named):

    pass