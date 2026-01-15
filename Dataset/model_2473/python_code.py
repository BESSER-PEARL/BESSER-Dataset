from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class railway2stochasticpetrinet_RailwayElement:

    pass
class railway2stochasticpetrinet_PetriNet:

    pass
class railway2stochasticpetrinet_TraceLink(ABC):

    pass
class railway2stochasticpetrinet_ImmediateTransition:

    pass
class railway2stochasticpetrinet_Place:

    pass
class railway2stochasticpetrinet_Route:

    pass
class PetriNetModuleTraceLink:

    pass
class railway2stochasticpetrinet_RequiredElement2Connection(PetriNetModuleTraceLink):

    pass
class railway2stochasticpetrinet_RequiredElement2FailureModel(PetriNetModuleTraceLink):

    pass
class railway2stochasticpetrinet_Route2FailureModel(PetriNetModuleTraceLink):

    pass
class railway2stochasticpetrinet_Arc:

    pass
class railway2stochasticpetrinet_Node:

    pass
class TraceLink:

    pass
class railway2stochasticpetrinet_RailwayContainer2PetriNet(TraceLink):

    pass
class railway2stochasticpetrinet_PetriNetModuleTraceLink(TraceLink):

    pass
class railway2stochasticpetrinet_RailwayContainer:

    pass
class railway2stochasticpetrinet_Railway2StochasticPetriNetTrace:

    pass