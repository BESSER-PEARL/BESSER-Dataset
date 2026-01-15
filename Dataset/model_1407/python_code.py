from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hfsm_NamedElement:

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
class hfsm_Transition(NamedElement):

    pass
class hfsm_Region(NamedElement):

    pass
class AbstractState:

    pass
class hfsm_State(AbstractState):

    pass
class hfsm_AbstractState(NamedElement):

    pass