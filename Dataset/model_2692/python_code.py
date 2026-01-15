from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class multiview3_Named:

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
class multiview3_K(Named):

    pass
class multiview3_F(Named):

    pass
class multiview3_B(Named):

    pass
class multiview3_C(Named):

    pass
class multiview3_W(Named):

    pass
class multiview3_M(Named):

    pass
class multiview3_H(Named):

    pass
class multiview3_E(Named):

    pass
class multiview3_A(Named):

    pass