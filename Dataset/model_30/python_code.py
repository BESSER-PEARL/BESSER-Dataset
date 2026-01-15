from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Transition:

    pass
class Place:

    pass
class PetriNet_Arc(ABC):

    def __init__(self, weight: str):
        self.weight = weight
        
    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

class Element:

    pass
class PetriNet_PetriNet(Element):

    pass
class PetriNet_Transition(Element):

    pass
class PetriNet:

    pass
class PlaceToTransArc:

    pass
class TransToPlaceArc:

    pass
class PetriNet_Place(Element):

    pass
class Arc:

    pass
class PetriNet_TransToPlaceArc(Arc):

    pass
class PetriNet_PlaceToTransArc(Arc):

    pass
class PetriNet_Element(ABC):

    pass