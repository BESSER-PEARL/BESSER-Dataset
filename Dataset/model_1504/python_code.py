from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class PetriNet_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class PetriNet_Transition(NamedElement):

    pass
class PetriNet_Place(NamedElement):

    pass
class PetriNet_Net:

    pass