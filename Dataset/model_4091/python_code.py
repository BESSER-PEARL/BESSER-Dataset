from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudostateKind(Enum):
    initial = "initial"
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"


############################################
# Definition of Classes
############################################

class statemachines_almostuml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class statemachines_almostuml_Constraint(ABC):

    pass
class Constraint:

    pass
class Trigger:

    pass
class Behavior:

    pass
class almostuml_Vertex:

    pass
class almostuml_NamedElement:

    pass
class statemachines_almostuml_State(almostuml_NamedElement, almostuml_Vertex):

    def __init__(self, statemachines_almostuml_State: "Behavior" = None, statemachines_almostuml_State15: "Behavior" = None, statemachines_almostuml_State18: "Behavior" = None, statemachines_almostuml_State21: set["Region"] = None):
        self.statemachines_almostuml_State = statemachines_almostuml_State
        self.statemachines_almostuml_State15 = statemachines_almostuml_State15
        self.statemachines_almostuml_State18 = statemachines_almostuml_State18
        self.statemachines_almostuml_State21 = statemachines_almostuml_State21 if statemachines_almostuml_State21 is not None else set()
        
        pass
    @property
    def statemachines_almostuml_State15(self):
        return self.__statemachines_almostuml_State15

    @statemachines_almostuml_State15.setter
    def statemachines_almostuml_State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_State__statemachines_almostuml_State15", None)
        self.__statemachines_almostuml_State15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior16"):
                opp_val = getattr(old_value, "Behavior16", None)
                if opp_val == self:
                    setattr(old_value, "Behavior16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior16"):
                opp_val = getattr(value, "Behavior16", None)
                setattr(value, "Behavior16", self)

    @property
    def statemachines_almostuml_State21(self):
        return self.__statemachines_almostuml_State21

    @statemachines_almostuml_State21.setter
    def statemachines_almostuml_State21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_State__statemachines_almostuml_State21", None)
        self.__statemachines_almostuml_State21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region22"):
                    opp_val = getattr(item, "Region22", None)
                    
                    if opp_val == self:
                        setattr(item, "Region22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region22"):
                    opp_val = getattr(item, "Region22", None)
                    
                    setattr(item, "Region22", self)
                    

    @property
    def statemachines_almostuml_State18(self):
        return self.__statemachines_almostuml_State18

    @statemachines_almostuml_State18.setter
    def statemachines_almostuml_State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_State__statemachines_almostuml_State18", None)
        self.__statemachines_almostuml_State18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior19"):
                opp_val = getattr(old_value, "Behavior19", None)
                if opp_val == self:
                    setattr(old_value, "Behavior19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior19"):
                opp_val = getattr(value, "Behavior19", None)
                setattr(value, "Behavior19", self)

    @property
    def statemachines_almostuml_State(self):
        return self.__statemachines_almostuml_State

    @statemachines_almostuml_State.setter
    def statemachines_almostuml_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_State__statemachines_almostuml_State", None)
        self.__statemachines_almostuml_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior"):
                opp_val = getattr(old_value, "Behavior", None)
                if opp_val == self:
                    setattr(old_value, "Behavior", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior"):
                opp_val = getattr(value, "Behavior", None)
                setattr(value, "Behavior", self)

    def handle(self, statemachines_eventOccurrence):
        # TODO: Implement handle method
        pass

    def setAsCurrent(self):
        # TODO: Implement setAsCurrent method
        pass

class State:

    pass
class statemachines_almostuml_Pseudostate(State):

    def __init__(self, kind: str, State: "statemachines_almostuml_Region" = None):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class statemachines_almostuml_FinalState(State):

    def __init__(self, State: "statemachines_almostuml_Region" = None):
        
        pass
    def handle(self, statemachines_eventOccurrence):
        # TODO: Implement handle method
        pass

class Transition:

    pass
class Vertex:

    pass
class almostuml_statemachines_EventOccurrence:

    pass
class Region:

    pass
class NamedElement:

    pass
class statemachines_almostuml_Region(NamedElement):

    def __init__(self, container: set["Vertex"] = None, statemachines_almostuml_Region: set["Transition"] = None, region: "StateMachine" = None, statemachines_almostuml_Region12: "State" = None):
        self.container = container if container is not None else set()
        self.statemachines_almostuml_Region = statemachines_almostuml_Region if statemachines_almostuml_Region is not None else set()
        self.region = region
        self.statemachines_almostuml_Region12 = statemachines_almostuml_Region12
        
        pass
    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Region__container", None)
        self.__container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vertex"):
                    opp_val = getattr(item, "Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vertex"):
                    opp_val = getattr(item, "Vertex", None)
                    
                    setattr(item, "Vertex", self)
                    

    @property
    def statemachines_almostuml_Region(self):
        return self.__statemachines_almostuml_Region

    @statemachines_almostuml_Region.setter
    def statemachines_almostuml_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Region__statemachines_almostuml_Region", None)
        self.__statemachines_almostuml_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Region__region", None)
        self.__region = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine10"):
                opp_val = getattr(old_value, "StateMachine10", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine10"):
                opp_val = getattr(value, "StateMachine10", None)
                setattr(value, "StateMachine10", self)

    @property
    def statemachines_almostuml_Region12(self):
        return self.__statemachines_almostuml_Region12

    @statemachines_almostuml_Region12.setter
    def statemachines_almostuml_Region12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Region__statemachines_almostuml_Region12", None)
        self.__statemachines_almostuml_Region12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    def handleEvent(self, statemachines_eventOccurrence):
        # TODO: Implement handleEvent method
        pass

    def initialize(self):
        # TODO: Implement initialize method
        pass

class statemachines_almostuml_Event(NamedElement):

    pass
class statemachines_almostuml_Trigger(NamedElement):

    pass
class statemachines_almostuml_Behavior(NamedElement):

    pass
class statemachines_almostuml_StateMachine(NamedElement):

    def __init__(self, stateMachine: set["Region"] = None, statemachines_almostuml_StateMachine: set["almostuml_statemachines_EventOccurrence"] = None):
        self.stateMachine = stateMachine if stateMachine is not None else set()
        self.statemachines_almostuml_StateMachine = statemachines_almostuml_StateMachine if statemachines_almostuml_StateMachine is not None else set()
        
        pass
    @property
    def statemachines_almostuml_StateMachine(self):
        return self.__statemachines_almostuml_StateMachine

    @statemachines_almostuml_StateMachine.setter
    def statemachines_almostuml_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_StateMachine__statemachines_almostuml_StateMachine", None)
        self.__statemachines_almostuml_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "almostuml_statemachines_EventOccurrence"):
                    opp_val = getattr(item, "almostuml_statemachines_EventOccurrence", None)
                    
                    if opp_val == self:
                        setattr(item, "almostuml_statemachines_EventOccurrence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "almostuml_statemachines_EventOccurrence"):
                    opp_val = getattr(item, "almostuml_statemachines_EventOccurrence", None)
                    
                    setattr(item, "almostuml_statemachines_EventOccurrence", self)
                    

    @property
    def stateMachine(self):
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_StateMachine__stateMachine", None)
        self.__stateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Region"):
                    opp_val = getattr(item, "Region", None)
                    
                    if opp_val == self:
                        setattr(item, "Region", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Region"):
                    opp_val = getattr(item, "Region", None)
                    
                    setattr(item, "Region", self)
                    

    def run(self):
        # TODO: Implement run method
        pass

class statemachines_Util:

    def __init__(self):
        
        pass
    def log(self, statemachines_l):
        # TODO: Implement log method
        pass

class statemachines_almostuml_Transition(NamedElement):

    def __init__(self, statemachines_almostuml_Transition: "Vertex" = None, statemachines_almostuml_Transition28: "Vertex" = None, statemachines_almostuml_Transition31: set["Trigger"] = None, statemachines_almostuml_Transition33: "Constraint" = None, statemachines_almostuml_Transition35: "Behavior" = None):
        self.statemachines_almostuml_Transition = statemachines_almostuml_Transition
        self.statemachines_almostuml_Transition28 = statemachines_almostuml_Transition28
        self.statemachines_almostuml_Transition31 = statemachines_almostuml_Transition31 if statemachines_almostuml_Transition31 is not None else set()
        self.statemachines_almostuml_Transition33 = statemachines_almostuml_Transition33
        self.statemachines_almostuml_Transition35 = statemachines_almostuml_Transition35
        
        pass
    @property
    def statemachines_almostuml_Transition31(self):
        return self.__statemachines_almostuml_Transition31

    @statemachines_almostuml_Transition31.setter
    def statemachines_almostuml_Transition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Transition__statemachines_almostuml_Transition31", None)
        self.__statemachines_almostuml_Transition31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trigger"):
                    opp_val = getattr(item, "Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trigger"):
                    opp_val = getattr(item, "Trigger", None)
                    
                    setattr(item, "Trigger", self)
                    

    @property
    def statemachines_almostuml_Transition28(self):
        return self.__statemachines_almostuml_Transition28

    @statemachines_almostuml_Transition28.setter
    def statemachines_almostuml_Transition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Transition__statemachines_almostuml_Transition28", None)
        self.__statemachines_almostuml_Transition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex29"):
                opp_val = getattr(old_value, "Vertex29", None)
                if opp_val == self:
                    setattr(old_value, "Vertex29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex29"):
                opp_val = getattr(value, "Vertex29", None)
                setattr(value, "Vertex29", self)

    @property
    def statemachines_almostuml_Transition(self):
        return self.__statemachines_almostuml_Transition

    @statemachines_almostuml_Transition.setter
    def statemachines_almostuml_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Transition__statemachines_almostuml_Transition", None)
        self.__statemachines_almostuml_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex26"):
                opp_val = getattr(old_value, "Vertex26", None)
                if opp_val == self:
                    setattr(old_value, "Vertex26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex26"):
                opp_val = getattr(value, "Vertex26", None)
                setattr(value, "Vertex26", self)

    @property
    def statemachines_almostuml_Transition35(self):
        return self.__statemachines_almostuml_Transition35

    @statemachines_almostuml_Transition35.setter
    def statemachines_almostuml_Transition35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Transition__statemachines_almostuml_Transition35", None)
        self.__statemachines_almostuml_Transition35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior36"):
                opp_val = getattr(old_value, "Behavior36", None)
                if opp_val == self:
                    setattr(old_value, "Behavior36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior36"):
                opp_val = getattr(value, "Behavior36", None)
                setattr(value, "Behavior36", self)

    @property
    def statemachines_almostuml_Transition33(self):
        return self.__statemachines_almostuml_Transition33

    @statemachines_almostuml_Transition33.setter
    def statemachines_almostuml_Transition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Transition__statemachines_almostuml_Transition33", None)
        self.__statemachines_almostuml_Transition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constraint"):
                opp_val = getattr(old_value, "Constraint", None)
                if opp_val == self:
                    setattr(old_value, "Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint"):
                opp_val = getattr(value, "Constraint", None)
                setattr(value, "Constraint", self)

    def fire(self):
        # TODO: Implement fire method
        pass

class statemachines_almostuml_Vertex(NamedElement):

    pass
class statemachines_CustomSystem:

    def __init__(self, statemachines_CustomSystem2: set["statemachines_CustomEvent"] = None, statemachines_CustomSystem: "StateMachine" = None):
        self.statemachines_CustomSystem2 = statemachines_CustomSystem2 if statemachines_CustomSystem2 is not None else set()
        self.statemachines_CustomSystem = statemachines_CustomSystem
        
        pass
    @property
    def statemachines_CustomSystem2(self):
        return self.__statemachines_CustomSystem2

    @statemachines_CustomSystem2.setter
    def statemachines_CustomSystem2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_CustomSystem__statemachines_CustomSystem2", None)
        self.__statemachines_CustomSystem2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachines_CustomEvent"):
                    opp_val = getattr(item, "statemachines_CustomEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachines_CustomEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachines_CustomEvent"):
                    opp_val = getattr(item, "statemachines_CustomEvent", None)
                    
                    setattr(item, "statemachines_CustomEvent", self)
                    

    @property
    def statemachines_CustomSystem(self):
        return self.__statemachines_CustomSystem

    @statemachines_CustomSystem.setter
    def statemachines_CustomSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_CustomSystem__statemachines_CustomSystem", None)
        self.__statemachines_CustomSystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine"):
                opp_val = getattr(old_value, "StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine"):
                opp_val = getattr(value, "StateMachine", None)
                setattr(value, "StateMachine", self)

    def initialize(self, statemachines_args):
        # TODO: Implement initialize method
        pass

    def main(self):
        # TODO: Implement main method
        pass

class statemachines_EventOccurrence:

    pass
class Event:

    pass
class statemachines_CustomEvent(Event):

    pass
class StateMachine:

    pass