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
        
    @property
    def name(self) -> str:
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

    def __init__(self, statemachines_almostuml_State: "Behavior" = None, statemachines_almostuml_State19: "Behavior" = None, statemachines_almostuml_State22: "Behavior" = None, statemachines_almostuml_State25: set["Region"] = None):
        self.statemachines_almostuml_State = statemachines_almostuml_State
        self.statemachines_almostuml_State19 = statemachines_almostuml_State19
        self.statemachines_almostuml_State22 = statemachines_almostuml_State22
        self.statemachines_almostuml_State25 = statemachines_almostuml_State25 if statemachines_almostuml_State25 is not None else set()
        
    @property
    def statemachines_almostuml_State25(self):
        return self.__statemachines_almostuml_State25

    @statemachines_almostuml_State25.setter
    def statemachines_almostuml_State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_State__statemachines_almostuml_State25", None)
        self.__statemachines_almostuml_State25 = value if value is not None else set()
        
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
                    

    @property
    def statemachines_almostuml_State19(self):
        return self.__statemachines_almostuml_State19

    @statemachines_almostuml_State19.setter
    def statemachines_almostuml_State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_State__statemachines_almostuml_State19", None)
        self.__statemachines_almostuml_State19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior20"):
                opp_val = getattr(old_value, "Behavior20", None)
                if opp_val == self:
                    setattr(old_value, "Behavior20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior20"):
                opp_val = getattr(value, "Behavior20", None)
                setattr(value, "Behavior20", self)

    @property
    def statemachines_almostuml_State22(self):
        return self.__statemachines_almostuml_State22

    @statemachines_almostuml_State22.setter
    def statemachines_almostuml_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_State__statemachines_almostuml_State22", None)
        self.__statemachines_almostuml_State22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior23"):
                opp_val = getattr(old_value, "Behavior23", None)
                if opp_val == self:
                    setattr(old_value, "Behavior23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior23"):
                opp_val = getattr(value, "Behavior23", None)
                setattr(value, "Behavior23", self)

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

    def setAsCurrent(self):
        # TODO: Implement setAsCurrent method
        pass

    def handle(self, eventOccurrence: str):
        # TODO: Implement handle method
        pass

class State:

    pass
class statemachines_almostuml_FinalState(State):

    def __init__(self, State: "statemachines_almostuml_Region"):
        
    def handle(self, eventOccurrence: str):
        # TODO: Implement handle method
        pass

class statemachines_almostuml_Pseudostate(State):

    def __init__(self, kind: str, State: "statemachines_almostuml_Region"):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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

    def __init__(self, 9: set["Vertex"] = None, statemachines_almostuml_Region: set["Transition"] = None, 13: "StateMachine" = None, statemachines_almostuml_Region16: "State" = None):
        self.9 = 9 if 9 is not None else set()
        self.statemachines_almostuml_Region = statemachines_almostuml_Region if statemachines_almostuml_Region is not None else set()
        self.13 = 13
        self.statemachines_almostuml_Region16 = statemachines_almostuml_Region16
        
    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Region__9", None)
        self.__9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    if opp_val == self:
                        setattr(item, "10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    setattr(item, "10", self)
                    

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Region__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "14"):
                opp_val = getattr(old_value, "14", None)
                if opp_val == self:
                    setattr(old_value, "14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "14"):
                opp_val = getattr(value, "14", None)
                setattr(value, "14", self)

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
    def statemachines_almostuml_Region16(self):
        return self.__statemachines_almostuml_Region16

    @statemachines_almostuml_Region16.setter
    def statemachines_almostuml_Region16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Region__statemachines_almostuml_Region16", None)
        self.__statemachines_almostuml_Region16 = value
        
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

    def handleEvent(self, eventOccurrence: str):
        # TODO: Implement handleEvent method
        pass

    def initialize(self):
        # TODO: Implement initialize method
        pass

class statemachines_almostuml_Transition(NamedElement):

    def __init__(self, statemachines_almostuml_Transition: "Vertex" = None, statemachines_almostuml_Transition31: "Vertex" = None, statemachines_almostuml_Transition34: set["Trigger"] = None, statemachines_almostuml_Transition36: "Constraint" = None, statemachines_almostuml_Transition38: "Behavior" = None):
        self.statemachines_almostuml_Transition = statemachines_almostuml_Transition
        self.statemachines_almostuml_Transition31 = statemachines_almostuml_Transition31
        self.statemachines_almostuml_Transition34 = statemachines_almostuml_Transition34 if statemachines_almostuml_Transition34 is not None else set()
        self.statemachines_almostuml_Transition36 = statemachines_almostuml_Transition36
        self.statemachines_almostuml_Transition38 = statemachines_almostuml_Transition38
        
    @property
    def statemachines_almostuml_Transition31(self):
        return self.__statemachines_almostuml_Transition31

    @statemachines_almostuml_Transition31.setter
    def statemachines_almostuml_Transition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Transition__statemachines_almostuml_Transition31", None)
        self.__statemachines_almostuml_Transition31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex32"):
                opp_val = getattr(old_value, "Vertex32", None)
                if opp_val == self:
                    setattr(old_value, "Vertex32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex32"):
                opp_val = getattr(value, "Vertex32", None)
                setattr(value, "Vertex32", self)

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
            if hasattr(old_value, "Vertex"):
                opp_val = getattr(old_value, "Vertex", None)
                if opp_val == self:
                    setattr(old_value, "Vertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex"):
                opp_val = getattr(value, "Vertex", None)
                setattr(value, "Vertex", self)

    @property
    def statemachines_almostuml_Transition34(self):
        return self.__statemachines_almostuml_Transition34

    @statemachines_almostuml_Transition34.setter
    def statemachines_almostuml_Transition34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Transition__statemachines_almostuml_Transition34", None)
        self.__statemachines_almostuml_Transition34 = value if value is not None else set()
        
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
    def statemachines_almostuml_Transition36(self):
        return self.__statemachines_almostuml_Transition36

    @statemachines_almostuml_Transition36.setter
    def statemachines_almostuml_Transition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Transition__statemachines_almostuml_Transition36", None)
        self.__statemachines_almostuml_Transition36 = value
        
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

    @property
    def statemachines_almostuml_Transition38(self):
        return self.__statemachines_almostuml_Transition38

    @statemachines_almostuml_Transition38.setter
    def statemachines_almostuml_Transition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_Transition__statemachines_almostuml_Transition38", None)
        self.__statemachines_almostuml_Transition38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behavior39"):
                opp_val = getattr(old_value, "Behavior39", None)
                if opp_val == self:
                    setattr(old_value, "Behavior39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behavior39"):
                opp_val = getattr(value, "Behavior39", None)
                setattr(value, "Behavior39", self)

    def fire(self):
        # TODO: Implement fire method
        pass

class statemachines_almostuml_Trigger(NamedElement):

    pass
class statemachines_almostuml_Event(NamedElement):

    pass
class statemachines_almostuml_Behavior(NamedElement):

    pass
class statemachines_almostuml_Vertex(NamedElement):

    pass
class statemachines_almostuml_StateMachine(NamedElement):

    def __init__(self, : set["Region"] = None, statemachines_almostuml_StateMachine: set["almostuml_statemachines_EventOccurrence"] = None):
        self. =  if  is not None else set()
        self.statemachines_almostuml_StateMachine = statemachines_almostuml_StateMachine if statemachines_almostuml_StateMachine is not None else set()
        
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
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachines_almostuml_StateMachine__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "6"):
                    opp_val = getattr(item, "6", None)
                    
                    if opp_val == self:
                        setattr(item, "6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "6"):
                    opp_val = getattr(item, "6", None)
                    
                    setattr(item, "6", self)
                    

    def run(self):
        # TODO: Implement run method
        pass

class statemachines_Util:

    def __init__(self):
        
    def log(self, l: str):
        # TODO: Implement log method
        pass

class statemachines_EventOccurrence:

    pass
class Event:

    pass
class statemachines_CustomEvent(Event):

    pass
class statemachines_CustomSystem:

    def __init__(self, statemachines_CustomSystem: "StateMachine" = None, statemachines_CustomSystem2: set["statemachines_CustomEvent"] = None):
        self.statemachines_CustomSystem = statemachines_CustomSystem
        self.statemachines_CustomSystem2 = statemachines_CustomSystem2 if statemachines_CustomSystem2 is not None else set()
        
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

    def initialize(self, args: str):
        # TODO: Implement initialize method
        pass

    def main(self):
        # TODO: Implement main method
        pass

class StateMachine:

    pass