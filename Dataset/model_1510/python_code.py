from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Transition:

    pass
class PetriNetSim_Transition(Transition):

    def __init__(self):
        
    def outWeight(self, p: Place) -> int:
        # TODO: Implement outWeight method
        pass

    def inWeight(self, p: Place) -> int:
        # TODO: Implement inWeight method
        pass

    def enabled(self) -> bool:
        # TODO: Implement enabled method
        pass

    def fire(self) -> bool:
        # TODO: Implement fire method
        pass

class PetriNet:

    pass
class PetriNetSim_PetriNet(PetriNet):

    def __init__(self):
        
    def step(self) -> bool:
        # TODO: Implement step method
        pass

    def simulate(self):
        # TODO: Implement simulate method
        pass

    def pick(self, s: str) -> str:
        # TODO: Implement pick method
        pass

class Place:

    pass
class PetriNetSim_Place(Place):

    def __init__(self):
        
    def modify(self, t: str) -> bool:
        # TODO: Implement modify method
        pass
