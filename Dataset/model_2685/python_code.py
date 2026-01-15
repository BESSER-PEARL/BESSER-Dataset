from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Named:

    pass
class multiview_F(Named):

    pass
class multiview_A(Named):

    pass
class multiview_Named:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class multiview_C(Named):

    pass
class multiview_E(Named):

    pass
class multiview_B(Named):

    pass