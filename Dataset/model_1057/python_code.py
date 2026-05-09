from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet:

    pass
class PlaceToTransArc:

    pass
class TransToPlaceArc:

    pass
class Arc:

    pass
class PetriNet_WeightedArc(Arc):

    pass
class PetriNet_TransToPlaceArc(Arc):

    pass
class Transition:

    pass
class Place:

    pass
class Element:

    pass
class PetriNet_Place(Element):

    pass
class PetriNet_Transition(Element):

    pass
class PetriNet_PetriNet(Element):

    pass
class PetriNet_Element(ABC):

    pass
class PetriNet_PlaceToTransArc(Arc):

    pass
class PetriNet_Arc:

    def __init__(self, weight: str):
        self.weight = weight
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

