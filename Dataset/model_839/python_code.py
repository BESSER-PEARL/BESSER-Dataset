from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Guard:

    pass
class tfsm_plaink3_EventGuard(Guard):

    pass
class tfsm_plaink3_TemporalGuard(Guard):

    def __init__(self, afterDuration: int, tfsm_plaink3_TemporalGuard: "tfsm_plaink3_FSMClock" = None):
        self.afterDuration = afterDuration
        self.tfsm_plaink3_TemporalGuard = tfsm_plaink3_TemporalGuard
        
    @property
    def afterDuration(self) -> int:
        return self.__afterDuration

    @afterDuration.setter
    def afterDuration(self, afterDuration: int):
        self.__afterDuration = afterDuration

    @property
    def tfsm_plaink3_TemporalGuard(self):
        return self.__tfsm_plaink3_TemporalGuard

    @tfsm_plaink3_TemporalGuard.setter
    def tfsm_plaink3_TemporalGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_TemporalGuard__tfsm_plaink3_TemporalGuard", None)
        self.__tfsm_plaink3_TemporalGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_FSMClock22"):
                opp_val = getattr(old_value, "tfsm_plaink3_FSMClock22", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_FSMClock22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_FSMClock22"):
                opp_val = getattr(value, "tfsm_plaink3_FSMClock22", None)
                setattr(value, "tfsm_plaink3_FSMClock22", self)

class tfsm_plaink3_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class tfsm_plaink3_EvaluateGuard(Guard):

    def __init__(self, condition: str):
        self.condition = condition
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

class NamedElement:

    pass
class tfsm_plaink3_FSMEvent(NamedElement):

    pass
class tfsm_plaink3_State(NamedElement):

    pass
class tfsm_plaink3_Guard(NamedElement):

    pass
class tfsm_plaink3_TimedSystem(NamedElement):

    pass
class tfsm_plaink3_TFSM(NamedElement):

    pass
class tfsm_plaink3_Transition(NamedElement):

    def __init__(self, action: str, tfsm_plaink3_Transition: "tfsm_plaink3_TFSM" = None, Transition: "tfsm_plaink3_State" = None, Transition11: "tfsm_plaink3_State" = None, outgoingTransitions: "tfsm_plaink3_State" = None, incomingTransitions: "tfsm_plaink3_State" = None, tfsm_plaink3_Transition17: "tfsm_plaink3_Guard" = None, tfsm_plaink3_Transition19: set["tfsm_plaink3_FSMEvent"] = None, tfsm_plaink3_Transition27: "tfsm_plaink3_FSMEvent" = None):
        self.action = action
        self.tfsm_plaink3_Transition = tfsm_plaink3_Transition
        self.Transition = Transition
        self.Transition11 = Transition11
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.tfsm_plaink3_Transition17 = tfsm_plaink3_Transition17
        self.tfsm_plaink3_Transition19 = tfsm_plaink3_Transition19 if tfsm_plaink3_Transition19 is not None else set()
        self.tfsm_plaink3_Transition27 = tfsm_plaink3_Transition27
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State13"):
                opp_val = getattr(old_value, "State13", None)
                if opp_val == self:
                    setattr(old_value, "State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State13"):
                opp_val = getattr(value, "State13", None)
                setattr(value, "State13", self)

    @property
    def tfsm_plaink3_Transition(self):
        return self.__tfsm_plaink3_Transition

    @tfsm_plaink3_Transition.setter
    def tfsm_plaink3_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition", None)
        self.__tfsm_plaink3_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TFSM7"):
                opp_val = getattr(old_value, "tfsm_plaink3_TFSM7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TFSM7"):
                opp_val = getattr(value, "tfsm_plaink3_TFSM7", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_TFSM7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_Transition27(self):
        return self.__tfsm_plaink3_Transition27

    @tfsm_plaink3_Transition27.setter
    def tfsm_plaink3_Transition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition27", None)
        self.__tfsm_plaink3_Transition27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_FSMEvent26"):
                opp_val = getattr(old_value, "tfsm_plaink3_FSMEvent26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_FSMEvent26"):
                opp_val = getattr(value, "tfsm_plaink3_FSMEvent26", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_FSMEvent26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition11(self):
        return self.__Transition11

    @Transition11.setter
    def Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__Transition11", None)
        self.__Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_Transition17(self):
        return self.__tfsm_plaink3_Transition17

    @tfsm_plaink3_Transition17.setter
    def tfsm_plaink3_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition17", None)
        self.__tfsm_plaink3_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_Guard"):
                opp_val = getattr(old_value, "tfsm_plaink3_Guard", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_Guard"):
                opp_val = getattr(value, "tfsm_plaink3_Guard", None)
                setattr(value, "tfsm_plaink3_Guard", self)

    @property
    def tfsm_plaink3_Transition19(self):
        return self.__tfsm_plaink3_Transition19

    @tfsm_plaink3_Transition19.setter
    def tfsm_plaink3_Transition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition19", None)
        self.__tfsm_plaink3_Transition19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_plaink3_FSMEvent20"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMEvent20", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_plaink3_FSMEvent20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_plaink3_FSMEvent20"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMEvent20", None)
                    
                    setattr(item, "tfsm_plaink3_FSMEvent20", self)
                    

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State15"):
                opp_val = getattr(old_value, "State15", None)
                if opp_val == self:
                    setattr(old_value, "State15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State15"):
                opp_val = getattr(value, "State15", None)
                setattr(value, "State15", self)

class tfsm_plaink3_FSMClock(NamedElement):

    pass