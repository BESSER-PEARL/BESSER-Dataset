from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class petriNetEMF_Identification(ABC):

    def __init__(self, ID: str, name: str):
        self.ID = ID
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class Identification:

    pass
class petriNetEMF_Arc(Identification):

    pass
class petriNetEMF_Transition(Identification):

    pass
class petriNetEMF_Place(Identification):

    pass
class petriNetEMF_PetriNet(Identification):

    pass
class petriNetEMF_TransitionToPlaceArc(Arc):

    pass
class petriNetEMF_PlaceToTransitionArc(Arc):

    pass