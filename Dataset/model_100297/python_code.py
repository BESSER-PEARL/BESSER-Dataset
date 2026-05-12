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

    def __init__(self, weight: str, name: str):
        self.weight = weight
        self.name = name
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class PetriNet_Element(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Arc:

    pass
class PetriNet_TransitionToPlace(Arc):

    pass
class PetriNet_PlaceToTransition(Arc):

    pass
class Element:

    pass
class PetriNet_Place(Element):

    pass
class PetriNet_Transition(Element):

    pass
class EObject:

    pass
class PetriNet_PetriNet(EObject):

    pass