from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class errormanypov_Named:

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
class errormanypov_M(Named):

    pass
class errormanypov_B(Named):

    pass
class errormanypov_E(Named):

    pass
class errormanypov_F(Named):

    pass
class errormanypov_C(Named):

    pass
class errormanypov_J(Named):

    pass
class errormanypov_JK(Named):

    pass
class errormanypov_K(Named):

    pass
class errormanypov_A(Named):

    pass