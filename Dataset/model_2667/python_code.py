from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class semlink_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class semlink_A(NamedElement):

    pass
class semlink_B(NamedElement):

    pass
class semlink_C(NamedElement):

    pass
class semlink_G(NamedElement):

    pass