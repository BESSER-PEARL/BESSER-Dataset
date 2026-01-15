from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class petrinet_Place(NamedElement):

    pass
class petrinet_Net(NamedElement):

    pass
class petrinet_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class petrinet_Transition(NamedElement):

    pass