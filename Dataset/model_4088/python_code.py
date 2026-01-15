from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Behavior_NamedElement(ABC):

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
class Behavior_State(NamedElement):

    pass
class Behavior_Event(NamedElement):

    pass
class Behavior_Transition(NamedElement):

    pass
class Behavior_Component(NamedElement):

    pass
class Behavior_System(NamedElement):

    pass