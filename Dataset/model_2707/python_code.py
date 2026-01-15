from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tbase_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class tbase_TRoot:

    pass
class tbase_C:

    pass
class NamedElement:

    pass
class tbase_A(NamedElement):

    pass
class tbase_B(NamedElement):

    pass