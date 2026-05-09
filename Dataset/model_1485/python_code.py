from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class petriNetEMF_TransitionToPlaceArc(Arc):

    pass
class petriNetEMF_PlaceToTransitionArc(Arc):

    pass
class petriNetEMF_Identification(ABC):

    def __init__(self, ID: str, name: str):
        self.ID = ID
        self.name = name
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Identification:

    pass
class petriNetEMF_Transition(Identification):

    pass
class petriNetEMF_Place(Identification):

    pass
class petriNetEMF_Arc(Identification):

    pass
class petriNetEMF_PetriNet(Identification):

    pass