from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PseudoStateType(Enum):
    Initial = "Initial"
    Junction = "Junction"
    ShadowHistory = "ShadowHistory"
    DeepHistory = "DeepHistory"
    Terminate = "Terminate"
    EntryPoint = "EntryPoint"
    ExitPoint = "ExitPoint"
    Choice = "Choice"
    Join = "Join"
    Fork = "Fork"


############################################
# Definition of Classes
############################################

class stateChart_StateMachine:

    def __init__(self, name: str, stateChart_StateMachine: "stateChart_Region" = None):
        self.name = name
        self.stateChart_StateMachine = stateChart_StateMachine
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateChart_StateMachine(self):
        return self.__stateChart_StateMachine

    @stateChart_StateMachine.setter
    def stateChart_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_StateMachine__stateChart_StateMachine", None)
        self.__stateChart_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Region10"):
                opp_val = getattr(old_value, "stateChart_Region10", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Region10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Region10"):
                opp_val = getattr(value, "stateChart_Region10", None)
                setattr(value, "stateChart_Region10", self)

class stateChart_Transient:

    def __init__(self, name: str, trigger: str, guard: str, effect: str, priority: int, stateChart_Transient4: "stateChart_Vertex" = None, stateChart_Transient: "stateChart_Region" = None, stateChart_Transient7: "stateChart_Vertex" = None):
        self.name = name
        self.trigger = trigger
        self.guard = guard
        self.effect = effect
        self.priority = priority
        self.stateChart_Transient4 = stateChart_Transient4
        self.stateChart_Transient = stateChart_Transient
        self.stateChart_Transient7 = stateChart_Transient7
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def guard(self) -> str:
        return self.__guard

    @guard.setter
    def guard(self, guard: str):
        self.__guard = guard

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def stateChart_Transient7(self):
        return self.__stateChart_Transient7

    @stateChart_Transient7.setter
    def stateChart_Transient7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Transient__stateChart_Transient7", None)
        self.__stateChart_Transient7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Vertex8"):
                opp_val = getattr(old_value, "stateChart_Vertex8", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Vertex8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Vertex8"):
                opp_val = getattr(value, "stateChart_Vertex8", None)
                setattr(value, "stateChart_Vertex8", self)

    @property
    def stateChart_Transient(self):
        return self.__stateChart_Transient

    @stateChart_Transient.setter
    def stateChart_Transient(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Transient__stateChart_Transient", None)
        self.__stateChart_Transient = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Region"):
                opp_val = getattr(old_value, "stateChart_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Region"):
                opp_val = getattr(value, "stateChart_Region", None)
                if opp_val is None:
                    setattr(value, "stateChart_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateChart_Transient4(self):
        return self.__stateChart_Transient4

    @stateChart_Transient4.setter
    def stateChart_Transient4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Transient__stateChart_Transient4", None)
        self.__stateChart_Transient4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Vertex5"):
                opp_val = getattr(old_value, "stateChart_Vertex5", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Vertex5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Vertex5"):
                opp_val = getattr(value, "stateChart_Vertex5", None)
                setattr(value, "stateChart_Vertex5", self)

class stateChart_Region:

    def __init__(self, name: str, note: str, stateChart_Region2: set["stateChart_Vertex"] = None, stateChart_Region: set["stateChart_Transient"] = None, stateChart_Region10: "stateChart_StateMachine" = None, stateChart_Region12: "stateChart_CompositeState" = None):
        self.name = name
        self.note = note
        self.stateChart_Region2 = stateChart_Region2 if stateChart_Region2 is not None else set()
        self.stateChart_Region = stateChart_Region if stateChart_Region is not None else set()
        self.stateChart_Region10 = stateChart_Region10
        self.stateChart_Region12 = stateChart_Region12
        
    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateChart_Region10(self):
        return self.__stateChart_Region10

    @stateChart_Region10.setter
    def stateChart_Region10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Region__stateChart_Region10", None)
        self.__stateChart_Region10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_StateMachine"):
                opp_val = getattr(old_value, "stateChart_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_StateMachine"):
                opp_val = getattr(value, "stateChart_StateMachine", None)
                setattr(value, "stateChart_StateMachine", self)

    @property
    def stateChart_Region2(self):
        return self.__stateChart_Region2

    @stateChart_Region2.setter
    def stateChart_Region2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Region__stateChart_Region2", None)
        self.__stateChart_Region2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateChart_Vertex"):
                    opp_val = getattr(item, "stateChart_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "stateChart_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateChart_Vertex"):
                    opp_val = getattr(item, "stateChart_Vertex", None)
                    
                    setattr(item, "stateChart_Vertex", self)
                    

    @property
    def stateChart_Region12(self):
        return self.__stateChart_Region12

    @stateChart_Region12.setter
    def stateChart_Region12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Region__stateChart_Region12", None)
        self.__stateChart_Region12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_CompositeState"):
                opp_val = getattr(old_value, "stateChart_CompositeState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_CompositeState"):
                opp_val = getattr(value, "stateChart_CompositeState", None)
                if opp_val is None:
                    setattr(value, "stateChart_CompositeState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateChart_Region(self):
        return self.__stateChart_Region

    @stateChart_Region.setter
    def stateChart_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Region__stateChart_Region", None)
        self.__stateChart_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateChart_Transient"):
                    opp_val = getattr(item, "stateChart_Transient", None)
                    
                    if opp_val == self:
                        setattr(item, "stateChart_Transient", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateChart_Transient"):
                    opp_val = getattr(item, "stateChart_Transient", None)
                    
                    setattr(item, "stateChart_Transient", self)
                    

class State:

    pass
class stateChart_FinalState(State):

    pass
class stateChart_CompositeState(State):

    pass
class stateChart_SimpleState(State):

    pass
class Vertex:

    pass
class stateChart_State(Vertex):

    def __init__(self, exit: str, action: str, entry: str):
        self.exit = exit
        self.action = action
        self.entry = entry
        
    @property
    def exit(self) -> str:
        return self.__exit

    @exit.setter
    def exit(self, exit: str):
        self.__exit = exit

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def entry(self) -> str:
        return self.__entry

    @entry.setter
    def entry(self, entry: str):
        self.__entry = entry

class stateChart_PseudoState(Vertex):

    def __init__(self, PseudoStateType: str):
        self.PseudoStateType = PseudoStateType
        
    @property
    def PseudoStateType(self) -> str:
        return self.__PseudoStateType

    @PseudoStateType.setter
    def PseudoStateType(self, PseudoStateType: str):
        self.__PseudoStateType = PseudoStateType

class stateChart_Vertex(ABC):

    def __init__(self, note: str, name: str, isActive: bool, stateChart_Vertex5: "stateChart_Transient" = None, stateChart_Vertex: "stateChart_Region" = None, stateChart_Vertex8: "stateChart_Transient" = None):
        self.note = note
        self.name = name
        self.isActive = isActive
        self.stateChart_Vertex5 = stateChart_Vertex5
        self.stateChart_Vertex = stateChart_Vertex
        self.stateChart_Vertex8 = stateChart_Vertex8
        
    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stateChart_Vertex(self):
        return self.__stateChart_Vertex

    @stateChart_Vertex.setter
    def stateChart_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Vertex__stateChart_Vertex", None)
        self.__stateChart_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Region2"):
                opp_val = getattr(old_value, "stateChart_Region2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Region2"):
                opp_val = getattr(value, "stateChart_Region2", None)
                if opp_val is None:
                    setattr(value, "stateChart_Region2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stateChart_Vertex8(self):
        return self.__stateChart_Vertex8

    @stateChart_Vertex8.setter
    def stateChart_Vertex8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Vertex__stateChart_Vertex8", None)
        self.__stateChart_Vertex8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Transient7"):
                opp_val = getattr(old_value, "stateChart_Transient7", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Transient7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Transient7"):
                opp_val = getattr(value, "stateChart_Transient7", None)
                setattr(value, "stateChart_Transient7", self)

    @property
    def stateChart_Vertex5(self):
        return self.__stateChart_Vertex5

    @stateChart_Vertex5.setter
    def stateChart_Vertex5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stateChart_Vertex__stateChart_Vertex5", None)
        self.__stateChart_Vertex5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateChart_Transient4"):
                opp_val = getattr(old_value, "stateChart_Transient4", None)
                if opp_val == self:
                    setattr(old_value, "stateChart_Transient4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateChart_Transient4"):
                opp_val = getattr(value, "stateChart_Transient4", None)
                setattr(value, "stateChart_Transient4", self)
