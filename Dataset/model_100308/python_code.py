from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArcKind(Enum):
    read_arc = "read_arc"
    normal = "normal"


############################################
# Definition of Classes
############################################

class petrinetsemantics_SDMMPetriNet_PetriNet_dynamic:

    pass
class Place:

    pass
class Node_dynamic:

    pass
class petrinetsemantics_SDMMPetriNet_Place_dynamic(Node_dynamic):

    def __init__(self, marking: int, petrinetsemantics_SDMMPetriNet_Place_dynamic: "Place" = None, Node_dynamic: "petrinetsemantics_SDMMPetriNet_PetriNet_dynamic" = None):
        self.marking = marking
        self.petrinetsemantics_SDMMPetriNet_Place_dynamic = petrinetsemantics_SDMMPetriNet_Place_dynamic
        
        pass
    @property
    def marking(self):
        return self.__marking

    @marking.setter
    def marking(self, marking: int):
        self.__marking = marking


    @property
    def petrinetsemantics_SDMMPetriNet_Place_dynamic(self):
        return self.__petrinetsemantics_SDMMPetriNet_Place_dynamic

    @petrinetsemantics_SDMMPetriNet_Place_dynamic.setter
    def petrinetsemantics_SDMMPetriNet_Place_dynamic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_SDMMPetriNet_Place_dynamic__petrinetsemantics_SDMMPetriNet_Place_dynamic", None)
        self.__petrinetsemantics_SDMMPetriNet_Place_dynamic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Place"):
                opp_val = getattr(old_value, "Place", None)
                if opp_val == self:
                    setattr(old_value, "Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Place"):
                opp_val = getattr(value, "Place", None)
                setattr(value, "Place", self)

class petrinetsemantics_SDMMPetriNet_Node_dynamic(ABC):

    pass
class petrinetsemantics_DDMMPetriNet_Arc:

    def __init__(self, kind: str, weight: int, incomings: "Node" = None, outgoings: "Node" = None, arcs: "PetriNet" = None):
        self.kind = kind
        self.weight = weight
        self.incomings = incomings
        self.outgoings = outgoings
        self.arcs = arcs
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight


    @property
    def outgoings(self):
        return self.__outgoings

    @outgoings.setter
    def outgoings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Arc__outgoings", None)
        self.__outgoings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node11"):
                opp_val = getattr(old_value, "Node11", None)
                if opp_val == self:
                    setattr(old_value, "Node11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node11"):
                opp_val = getattr(value, "Node11", None)
                setattr(value, "Node11", self)

    @property
    def arcs(self):
        return self.__arcs

    @arcs.setter
    def arcs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Arc__arcs", None)
        self.__arcs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet13"):
                opp_val = getattr(old_value, "PetriNet13", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet13"):
                opp_val = getattr(value, "PetriNet13", None)
                setattr(value, "PetriNet13", self)

    @property
    def incomings(self):
        return self.__incomings

    @incomings.setter
    def incomings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Arc__incomings", None)
        self.__incomings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node9"):
                opp_val = getattr(old_value, "Node9", None)
                if opp_val == self:
                    setattr(old_value, "Node9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node9"):
                opp_val = getattr(value, "Node9", None)
                setattr(value, "Node9", self)

class PetriNet:

    pass
class petrinetsemantics_DDMMPetriNet_Node(ABC):

    def __init__(self, name: str, nodes: "PetriNet" = None, source: set["Arc"] = None, target: set["Arc"] = None):
        self.name = name
        self.nodes = nodes
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc5"):
                    opp_val = getattr(item, "Arc5", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc5"):
                    opp_val = getattr(item, "Arc5", None)
                    
                    setattr(item, "Arc5", self)
                    

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet"):
                opp_val = getattr(old_value, "PetriNet", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet"):
                opp_val = getattr(value, "PetriNet", None)
                setattr(value, "PetriNet", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc7"):
                    opp_val = getattr(item, "Arc7", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc7"):
                    opp_val = getattr(item, "Arc7", None)
                    
                    setattr(item, "Arc7", self)
                    

class Arc:

    pass
class petrinetsemantics_DDMMPetriNet_PetriNet:

    def __init__(self, name: str, net: set["Node"] = None, net2: set["Arc"] = None):
        self.name = name
        self.net = net if net is not None else set()
        self.net2 = net2 if net2 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def net2(self):
        return self.__net2

    @net2.setter
    def net2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_PetriNet__net2", None)
        self.__net2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    setattr(item, "Arc", self)
                    

    @property
    def net(self):
        return self.__net

    @net.setter
    def net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_PetriNet__net", None)
        self.__net = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

class Node:

    pass
class petrinetsemantics_DDMMPetriNet_Place(Node):

    def __init__(self, initialMarking: int, Node9: "petrinetsemantics_DDMMPetriNet_Arc" = None, Node11: "petrinetsemantics_DDMMPetriNet_Arc" = None, Node: "petrinetsemantics_DDMMPetriNet_PetriNet" = None, Node15: "petrinetsemantics_SDMMPetriNet_Node_dynamic" = None):
        self.initialMarking = initialMarking
        
        pass
    @property
    def initialMarking(self):
        return self.__initialMarking

    @initialMarking.setter
    def initialMarking(self, initialMarking: int):
        self.__initialMarking = initialMarking


class petrinetsemantics_DDMMPetriNet_Transition(Node):

    def __init__(self, min_time: int, max_time: int, Node9: "petrinetsemantics_DDMMPetriNet_Arc" = None, Node11: "petrinetsemantics_DDMMPetriNet_Arc" = None, Node: "petrinetsemantics_DDMMPetriNet_PetriNet" = None, Node15: "petrinetsemantics_SDMMPetriNet_Node_dynamic" = None):
        self.min_time = min_time
        self.max_time = max_time
        
        pass
    @property
    def max_time(self):
        return self.__max_time

    @max_time.setter
    def max_time(self, max_time: int):
        self.__max_time = max_time


    @property
    def min_time(self):
        return self.__min_time

    @min_time.setter
    def min_time(self, min_time: int):
        self.__min_time = min_time


class petrinetsemantics_TM3PetriNet_PNSimEvent:

    def __init__(self, internal: bool, date: int, name: str):
        self.internal = internal
        self.date = date
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def internal(self):
        return self.__internal

    @internal.setter
    def internal(self, internal: bool):
        self.__internal = internal


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: int):
        self.__date = date


class PNScenario:

    pass
class petrinetsemantics_TM3PetriNet_PNTrace:

    pass
class PNTrace:

    pass
class petrinetsemantics_TM3PetriNet_PNScenario:

    pass
class Transition:

    pass
class PetriNetEvent:

    pass
class petrinetsemantics_EDMMPetriNet_FireTransitionEvent(PetriNetEvent):

    def __init__(self, time: float, petrinetsemantics_EDMMPetriNet_FireTransitionEvent: "Transition" = None):
        self.time = time
        self.petrinetsemantics_EDMMPetriNet_FireTransitionEvent = petrinetsemantics_EDMMPetriNet_FireTransitionEvent
        
        pass
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: float):
        self.__time = time


    @property
    def petrinetsemantics_EDMMPetriNet_FireTransitionEvent(self):
        return self.__petrinetsemantics_EDMMPetriNet_FireTransitionEvent

    @petrinetsemantics_EDMMPetriNet_FireTransitionEvent.setter
    def petrinetsemantics_EDMMPetriNet_FireTransitionEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_EDMMPetriNet_FireTransitionEvent__petrinetsemantics_EDMMPetriNet_FireTransitionEvent", None)
        self.__petrinetsemantics_EDMMPetriNet_FireTransitionEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition"):
                opp_val = getattr(old_value, "Transition", None)
                if opp_val == self:
                    setattr(old_value, "Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition"):
                opp_val = getattr(value, "Transition", None)
                setattr(value, "Transition", self)

class PNSimEvent:

    pass
class petrinetsemantics_EDMMPetriNet_PetriNetEvent(PNSimEvent):

    pass