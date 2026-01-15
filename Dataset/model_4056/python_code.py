from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class classdiagram_Attribute(NamedElement):

    pass
class classdiagram_Class(NamedElement):

    pass
class classdiagram_Method(NamedElement):

    pass
class classdiagram_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
