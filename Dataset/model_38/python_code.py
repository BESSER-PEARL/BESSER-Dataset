from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet_Arc:

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class TransToPlaceArc:

    pass
class PlaceToTransArc:

    pass
class Place:

    pass
class Element:

    pass
class PetriNet_Transition(Element):

    pass
class PetriNet_PetriNet(Element):

    pass
class PetriNet_Place(Element):

    pass
class Arc:

    pass
class PetriNet_PlaceToTransArc(Arc):

    pass
class PetriNet_TransToPlaceArc(Arc):

    pass
class Transition:

    pass
class PetriNet_Element(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
