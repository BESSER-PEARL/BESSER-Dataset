from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class multiview_Named:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Named:

    pass
class multiview_F(Named):

    pass
class multiview_C(Named):

    pass
class multiview_B(Named):

    pass
class multiview_E(Named):

    pass
class multiview_A(Named):

    pass