from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class B:

    pass
class comps_Named:

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
class comps_C(Named):

    pass
class comps_B(Named):

    pass
class comps_E(Named, B):

    pass
class comps_G(Named):

    pass
class comps_H(Named):

    pass
class comps_F(Named):

    pass
class comps_A(Named):

    pass