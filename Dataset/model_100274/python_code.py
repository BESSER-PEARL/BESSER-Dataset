from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class PetriNet_TPArc(Arc):

    pass
class PetriNet_PTArc(Arc):

    pass
class PetriNet_Arc(ABC):

    def __init__(self, weight: str):
        self.weight = weight
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


class Transition:

    pass
class Place:

    pass
class PetriNet_Net:

    pass
class PetriNet_Transition:

    pass
class TPArc:

    pass
class PTArc:

    pass
class Net:

    pass
class PetriNet_Place:

    pass