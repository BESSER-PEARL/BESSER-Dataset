from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransitionKind(Enum):
    internal = "internal"
    local = "local"
    external = "external"
class ChangeEventKind(Enum):
    WHEN = "WHEN"
class TimeEventKind(Enum):
    AT = "AT"
    AFTER = "AFTER"


############################################
# Definition of Classes
############################################

class StateEvent:

    pass
class capellacommon_TimeEvent(StateEvent):

    def __init__(self, kind: str, time: str):
        self.kind = kind
        self.time = time
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

class capellacommon_ChangeEvent(StateEvent):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class AbstractEvent:

    pass
class Pseudostate:

    pass
class capellacommon_ChoicePseudoState(Pseudostate):

    pass
class capellacommon_ExitPointPseudoState(Pseudostate):

    pass
class capellacommon_ShallowHistoryPseudoState(Pseudostate):

    pass
class capellacommon_JoinPseudoState(Pseudostate):

    pass
class capellacommon_TerminatePseudoState(Pseudostate):

    pass
class capellacommon_ForkPseudoState(Pseudostate):

    pass
class capellacommon_DeepHistoryPseudoState(Pseudostate):

    pass
class capellacommon_EntryPointPseudoState(Pseudostate):

    pass
class capellacommon_InitialPseudoState(Pseudostate):

    pass
class capellacommon_AbstractCapability:

    pass
class capellacommon_Constraint:

    pass
class IState:

    pass
class State:

    pass
class capellacommon_FinalState(State):

    pass
class capellacommon_Mode(State):

    pass
class capellacommon_AbstractEvent:

    pass
class AbstractBehavior:

    pass
class capellacommon_FunctionalChain:

    pass
class capellacommon_AbstractFunction:

    pass
class AbstractState:

    pass
class capellacommon_Pseudostate(AbstractState):

    pass
class capellacommon_State(AbstractState):

    pass
class NamedElement:

    pass
class capellacommon_Region(NamedElement):

    pass
class capellacommon_AbstractState(NamedElement, IState):

    pass
class capellacommon_StateEvent(AbstractEvent, NamedElement):

    pass
class capellacommon_TraceableElement:

    pass
class ModelElement:

    pass
class TraceableElement:

    pass
class CapellaElement:

    pass
class capellacommon_StateTransition(ModelElement, CapellaElement, NamedElement):

    def __init__(self, kind: str, triggerDescription: str, capellacommon_StateTransition: "capellacommon_Region" = None, capellacommon_StateTransition26: "capellacommon_Constraint" = None, capellacommon_StateTransition34: "capellacommon_AbstractEvent" = None, capellacommon_StateTransition37: set["capellacommon_AbstractEvent"] = None, capellacommon_StateTransition41: "capellacommon_StateTransition" = None, capellacommon_StateTransition39: set["capellacommon_StateTransition"] = None, capellacommon_StateTransition28: "capellacommon_AbstractState" = None, capellacommon_StateTransition31: "capellacommon_AbstractState" = None):
        self.kind = kind
        self.triggerDescription = triggerDescription
        self.capellacommon_StateTransition = capellacommon_StateTransition
        self.capellacommon_StateTransition26 = capellacommon_StateTransition26
        self.capellacommon_StateTransition34 = capellacommon_StateTransition34
        self.capellacommon_StateTransition37 = capellacommon_StateTransition37 if capellacommon_StateTransition37 is not None else set()
        self.capellacommon_StateTransition41 = capellacommon_StateTransition41
        self.capellacommon_StateTransition39 = capellacommon_StateTransition39 if capellacommon_StateTransition39 is not None else set()
        self.capellacommon_StateTransition28 = capellacommon_StateTransition28
        self.capellacommon_StateTransition31 = capellacommon_StateTransition31
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def triggerDescription(self) -> str:
        return self.__triggerDescription

    @triggerDescription.setter
    def triggerDescription(self, triggerDescription: str):
        self.__triggerDescription = triggerDescription

    @property
    def capellacommon_StateTransition34(self):
        return self.__capellacommon_StateTransition34

    @capellacommon_StateTransition34.setter
    def capellacommon_StateTransition34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_capellacommon_StateTransition__capellacommon_StateTransition34", None)
        self.__capellacommon_StateTransition34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "capellacommon_AbstractEvent35"):
                opp_val = getattr(old_value, "capellacommon_AbstractEvent35", None)
                if opp_val == self:
                    setattr(old_value, "capellacommon_AbstractEvent35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "capellacommon_AbstractEvent35"):
                opp_val = getattr(value, "capellacommon_AbstractEvent35", None)
                setattr(value, "capellacommon_AbstractEvent35", self)

    @property
    def capellacommon_StateTransition37(self):
        return self.__capellacommon_StateTransition37

    @capellacommon_StateTransition37.setter
    def capellacommon_StateTransition37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_capellacommon_StateTransition__capellacommon_StateTransition37", None)
        self.__capellacommon_StateTransition37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "capellacommon_AbstractEvent38"):
                    opp_val = getattr(item, "capellacommon_AbstractEvent38", None)
                    
                    if opp_val == self:
                        setattr(item, "capellacommon_AbstractEvent38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "capellacommon_AbstractEvent38"):
                    opp_val = getattr(item, "capellacommon_AbstractEvent38", None)
                    
                    setattr(item, "capellacommon_AbstractEvent38", self)
                    

    @property
    def capellacommon_StateTransition39(self):
        return self.__capellacommon_StateTransition39

    @capellacommon_StateTransition39.setter
    def capellacommon_StateTransition39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_capellacommon_StateTransition__capellacommon_StateTransition39", None)
        self.__capellacommon_StateTransition39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "capellacommon_StateTransition41"):
                    opp_val = getattr(item, "capellacommon_StateTransition41", None)
                    
                    if opp_val == self:
                        setattr(item, "capellacommon_StateTransition41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "capellacommon_StateTransition41"):
                    opp_val = getattr(item, "capellacommon_StateTransition41", None)
                    
                    setattr(item, "capellacommon_StateTransition41", self)
                    

    @property
    def capellacommon_StateTransition28(self):
        return self.__capellacommon_StateTransition28

    @capellacommon_StateTransition28.setter
    def capellacommon_StateTransition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_capellacommon_StateTransition__capellacommon_StateTransition28", None)
        self.__capellacommon_StateTransition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "capellacommon_AbstractState29"):
                opp_val = getattr(old_value, "capellacommon_AbstractState29", None)
                if opp_val == self:
                    setattr(old_value, "capellacommon_AbstractState29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "capellacommon_AbstractState29"):
                opp_val = getattr(value, "capellacommon_AbstractState29", None)
                setattr(value, "capellacommon_AbstractState29", self)

    @property
    def capellacommon_StateTransition31(self):
        return self.__capellacommon_StateTransition31

    @capellacommon_StateTransition31.setter
    def capellacommon_StateTransition31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_capellacommon_StateTransition__capellacommon_StateTransition31", None)
        self.__capellacommon_StateTransition31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "capellacommon_AbstractState32"):
                opp_val = getattr(old_value, "capellacommon_AbstractState32", None)
                if opp_val == self:
                    setattr(old_value, "capellacommon_AbstractState32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "capellacommon_AbstractState32"):
                opp_val = getattr(value, "capellacommon_AbstractState32", None)
                setattr(value, "capellacommon_AbstractState32", self)

    @property
    def capellacommon_StateTransition41(self):
        return self.__capellacommon_StateTransition41

    @capellacommon_StateTransition41.setter
    def capellacommon_StateTransition41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_capellacommon_StateTransition__capellacommon_StateTransition41", None)
        self.__capellacommon_StateTransition41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "capellacommon_StateTransition39"):
                opp_val = getattr(old_value, "capellacommon_StateTransition39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "capellacommon_StateTransition39"):
                opp_val = getattr(value, "capellacommon_StateTransition39", None)
                if opp_val is None:
                    setattr(value, "capellacommon_StateTransition39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def capellacommon_StateTransition26(self):
        return self.__capellacommon_StateTransition26

    @capellacommon_StateTransition26.setter
    def capellacommon_StateTransition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_capellacommon_StateTransition__capellacommon_StateTransition26", None)
        self.__capellacommon_StateTransition26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "capellacommon_Constraint"):
                opp_val = getattr(old_value, "capellacommon_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "capellacommon_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "capellacommon_Constraint"):
                opp_val = getattr(value, "capellacommon_Constraint", None)
                setattr(value, "capellacommon_Constraint", self)

    @property
    def capellacommon_StateTransition(self):
        return self.__capellacommon_StateTransition

    @capellacommon_StateTransition.setter
    def capellacommon_StateTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_capellacommon_StateTransition__capellacommon_StateTransition", None)
        self.__capellacommon_StateTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "capellacommon_Region8"):
                opp_val = getattr(old_value, "capellacommon_Region8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "capellacommon_Region8"):
                opp_val = getattr(value, "capellacommon_Region8", None)
                if opp_val is None:
                    setattr(value, "capellacommon_Region8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class capellacommon_StateMachine(AbstractBehavior, CapellaElement):

    pass
class capellacommon_GenericTrace(TraceableElement, CapellaElement, ModelElement):

    pass
class Structure:

    pass
class capellacommon_AbstractCapabilityPkg(Structure):

    pass