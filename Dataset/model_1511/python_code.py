from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Transition:

    pass
class PetriNetSim_Transition(Transition):

    def __init__(self):
        
        pass
    def outWeight(self, PetriNetSim_p) :
        # TODO: Implement outWeight method
        pass

    def inWeight(self, PetriNetSim_p) :
        # TODO: Implement inWeight method
        pass

    def fire(self) :
        # TODO: Implement fire method
        pass

    def enabled(self) :
        # TODO: Implement enabled method
        pass

class Place:

    pass
class PetriNetSim_Place(Place):

    def __init__(self):
        
        pass
    def modify(self, PetriNetSim_t) :
        # TODO: Implement modify method
        pass

class PetriNet:

    pass
class PetriNetSim_PetriNet(PetriNet):

    def __init__(self):
        
        pass
    def simulate(self):
        # TODO: Implement simulate method
        pass

    def pick(self, PetriNetSim_s) :
        # TODO: Implement pick method
        pass

    def step(self) :
        # TODO: Implement step method
        pass
