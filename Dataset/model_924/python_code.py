from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArcKind(Enum):
    normal = "normal"
    read_arc = "read_arc"


############################################
# Definition of Classes
############################################

class Place:

    pass
class Node_dynamic:

    pass
class petrinetsemantics_SDMMPetriNet_Place_dynamic(Node_dynamic):

    def __init__(self, marking: int, petrinetsemantics_SDMMPetriNet_Place_dynamic: "Place" = None, Node_dynamic: "petrinetsemantics_SDMMPetriNet_PetriNet_dynamic"):
        self.marking = marking
        self.petrinetsemantics_SDMMPetriNet_Place_dynamic = petrinetsemantics_SDMMPetriNet_Place_dynamic
        
    @property
    def marking(self) -> int:
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
class petrinetsemantics_TM3PetriNet_PNSimEvent:

    def __init__(self, internal: bool, date: int, name: str):
        self.internal = internal
        self.date = date
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def date(self) -> int:
        return self.__date

    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def internal(self) -> bool:
        return self.__internal

    @internal.setter
    def internal(self, internal: bool):
        self.__internal = internal

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
        
    @property
    def time(self) -> float:
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
class petrinetsemantics_SDMMPetriNet_PetriNet_dynamic:

    pass
class Node:

    pass
class petrinetsemantics_DDMMPetriNet_PetriNet:

    def __init__(self, name: str, Arc: set["Arc"] = None, Node: set["Node"] = None):
        self.name = name
        self.Arc = Arc if Arc is not None else set()
        self.Node = Node if Node is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_PetriNet__Arc", None)
        self.__Arc = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDMMPetriNet2"):
                    opp_val = getattr(item, "DDMMPetriNet2", None)
                    
                    if opp_val == self:
                        setattr(item, "DDMMPetriNet2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDMMPetriNet2"):
                    opp_val = getattr(item, "DDMMPetriNet2", None)
                    
                    setattr(item, "DDMMPetriNet2", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_PetriNet__Node", None)
        self.__Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDMMPetriNet"):
                    opp_val = getattr(item, "DDMMPetriNet", None)
                    
                    if opp_val == self:
                        setattr(item, "DDMMPetriNet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDMMPetriNet"):
                    opp_val = getattr(item, "DDMMPetriNet", None)
                    
                    setattr(item, "DDMMPetriNet", self)
                    

class petrinetsemantics_DDMMPetriNet_Arc:

    def __init__(self, kind: str, weight: int, Node12: "Node" = None, Node15: "Node" = None, PetriNet18: "PetriNet" = None):
        self.kind = kind
        self.weight = weight
        self.Node12 = Node12
        self.Node15 = Node15
        self.PetriNet18 = PetriNet18
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Node12(self):
        return self.__Node12

    @Node12.setter
    def Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Arc__Node12", None)
        self.__Node12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDMMPetriNet13"):
                opp_val = getattr(old_value, "DDMMPetriNet13", None)
                if opp_val == self:
                    setattr(old_value, "DDMMPetriNet13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDMMPetriNet13"):
                opp_val = getattr(value, "DDMMPetriNet13", None)
                setattr(value, "DDMMPetriNet13", self)

    @property
    def Node15(self):
        return self.__Node15

    @Node15.setter
    def Node15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Arc__Node15", None)
        self.__Node15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDMMPetriNet16"):
                opp_val = getattr(old_value, "DDMMPetriNet16", None)
                if opp_val == self:
                    setattr(old_value, "DDMMPetriNet16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDMMPetriNet16"):
                opp_val = getattr(value, "DDMMPetriNet16", None)
                setattr(value, "DDMMPetriNet16", self)

    @property
    def PetriNet18(self):
        return self.__PetriNet18

    @PetriNet18.setter
    def PetriNet18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Arc__PetriNet18", None)
        self.__PetriNet18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDMMPetriNet19"):
                opp_val = getattr(old_value, "DDMMPetriNet19", None)
                if opp_val == self:
                    setattr(old_value, "DDMMPetriNet19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDMMPetriNet19"):
                opp_val = getattr(value, "DDMMPetriNet19", None)
                setattr(value, "DDMMPetriNet19", self)

class petrinetsemantics_DDMMPetriNet_Place(Node):

    def __init__(self, initialMarking: int, DDMMPetriNet16: "petrinetsemantics_DDMMPetriNet_Arc", DDMMPetriNet13: "petrinetsemantics_DDMMPetriNet_Arc", Node21: "petrinetsemantics_SDMMPetriNet_Node_dynamic", DDMMPetriNet: "petrinetsemantics_DDMMPetriNet_PetriNet"):
        self.initialMarking = initialMarking
        
    @property
    def initialMarking(self) -> int:
        return self.__initialMarking

    @initialMarking.setter
    def initialMarking(self, initialMarking: int):
        self.__initialMarking = initialMarking

class PetriNet:

    pass
class petrinetsemantics_DDMMPetriNet_Node(ABC):

    def __init__(self, name: str, PetriNet: "PetriNet" = None, Arc6: set["Arc"] = None, Arc9: set["Arc"] = None):
        self.name = name
        self.PetriNet = PetriNet
        self.Arc6 = Arc6 if Arc6 is not None else set()
        self.Arc9 = Arc9 if Arc9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arc9(self):
        return self.__Arc9

    @Arc9.setter
    def Arc9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Node__Arc9", None)
        self.__Arc9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDMMPetriNet10"):
                    opp_val = getattr(item, "DDMMPetriNet10", None)
                    
                    if opp_val == self:
                        setattr(item, "DDMMPetriNet10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDMMPetriNet10"):
                    opp_val = getattr(item, "DDMMPetriNet10", None)
                    
                    setattr(item, "DDMMPetriNet10", self)
                    

    @property
    def PetriNet(self):
        return self.__PetriNet

    @PetriNet.setter
    def PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Node__PetriNet", None)
        self.__PetriNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDMMPetriNet4"):
                opp_val = getattr(old_value, "DDMMPetriNet4", None)
                if opp_val == self:
                    setattr(old_value, "DDMMPetriNet4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDMMPetriNet4"):
                opp_val = getattr(value, "DDMMPetriNet4", None)
                setattr(value, "DDMMPetriNet4", self)

    @property
    def Arc6(self):
        return self.__Arc6

    @Arc6.setter
    def Arc6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinetsemantics_DDMMPetriNet_Node__Arc6", None)
        self.__Arc6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDMMPetriNet7"):
                    opp_val = getattr(item, "DDMMPetriNet7", None)
                    
                    if opp_val == self:
                        setattr(item, "DDMMPetriNet7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDMMPetriNet7"):
                    opp_val = getattr(item, "DDMMPetriNet7", None)
                    
                    setattr(item, "DDMMPetriNet7", self)
                    

class petrinetsemantics_DDMMPetriNet_Transition(Node):

    def __init__(self, min_time: int, max_time: int, DDMMPetriNet16: "petrinetsemantics_DDMMPetriNet_Arc", DDMMPetriNet13: "petrinetsemantics_DDMMPetriNet_Arc", Node21: "petrinetsemantics_SDMMPetriNet_Node_dynamic", DDMMPetriNet: "petrinetsemantics_DDMMPetriNet_PetriNet"):
        self.min_time = min_time
        self.max_time = max_time
        
    @property
    def min_time(self) -> int:
        return self.__min_time

    @min_time.setter
    def min_time(self, min_time: int):
        self.__min_time = min_time

    @property
    def max_time(self) -> int:
        return self.__max_time

    @max_time.setter
    def max_time(self, max_time: int):
        self.__max_time = max_time

class Arc:

    pass