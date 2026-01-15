from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Guard:

    pass
class tfsm_EventGuard(Guard):

    pass
class tfsm_EvaluateGuard(Guard):

    def __init__(self, condition: str):
        self.condition = condition
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

class tfsm_TemporalGuard(Guard):

    def __init__(self, afterDuration: int, tfsm_TemporalGuard: "tfsm_FSMClock" = None):
        self.afterDuration = afterDuration
        self.tfsm_TemporalGuard = tfsm_TemporalGuard
        
    @property
    def afterDuration(self) -> int:
        return self.__afterDuration

    @afterDuration.setter
    def afterDuration(self, afterDuration: int):
        self.__afterDuration = afterDuration

    @property
    def tfsm_TemporalGuard(self):
        return self.__tfsm_TemporalGuard

    @tfsm_TemporalGuard.setter
    def tfsm_TemporalGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TemporalGuard__tfsm_TemporalGuard", None)
        self.__tfsm_TemporalGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSMClock22"):
                opp_val = getattr(old_value, "tfsm_FSMClock22", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_FSMClock22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSMClock22"):
                opp_val = getattr(value, "tfsm_FSMClock22", None)
                setattr(value, "tfsm_FSMClock22", self)

class tfsm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class tfsm_State(NamedElement):

    pass
class tfsm_FSMClock(NamedElement):

    def __init__(self, numberOfTicks: int, tfsm_FSMClock: "tfsm_TFSM" = None, tfsm_FSMClock22: "tfsm_TemporalGuard" = None, tfsm_FSMClock32: "tfsm_TimedSystem" = None):
        self.numberOfTicks = numberOfTicks
        self.tfsm_FSMClock = tfsm_FSMClock
        self.tfsm_FSMClock22 = tfsm_FSMClock22
        self.tfsm_FSMClock32 = tfsm_FSMClock32
        
    @property
    def numberOfTicks(self) -> int:
        return self.__numberOfTicks

    @numberOfTicks.setter
    def numberOfTicks(self, numberOfTicks: int):
        self.__numberOfTicks = numberOfTicks

    @property
    def tfsm_FSMClock(self):
        return self.__tfsm_FSMClock

    @tfsm_FSMClock.setter
    def tfsm_FSMClock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMClock__tfsm_FSMClock", None)
        self.__tfsm_FSMClock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TFSM5"):
                opp_val = getattr(old_value, "tfsm_TFSM5", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_TFSM5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TFSM5"):
                opp_val = getattr(value, "tfsm_TFSM5", None)
                setattr(value, "tfsm_TFSM5", self)

    @property
    def tfsm_FSMClock32(self):
        return self.__tfsm_FSMClock32

    @tfsm_FSMClock32.setter
    def tfsm_FSMClock32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMClock__tfsm_FSMClock32", None)
        self.__tfsm_FSMClock32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TimedSystem31"):
                opp_val = getattr(old_value, "tfsm_TimedSystem31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TimedSystem31"):
                opp_val = getattr(value, "tfsm_TimedSystem31", None)
                if opp_val is None:
                    setattr(value, "tfsm_TimedSystem31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_FSMClock22(self):
        return self.__tfsm_FSMClock22

    @tfsm_FSMClock22.setter
    def tfsm_FSMClock22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMClock__tfsm_FSMClock22", None)
        self.__tfsm_FSMClock22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TemporalGuard"):
                opp_val = getattr(old_value, "tfsm_TemporalGuard", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_TemporalGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TemporalGuard"):
                opp_val = getattr(value, "tfsm_TemporalGuard", None)
                setattr(value, "tfsm_TemporalGuard", self)

class tfsm_Guard(NamedElement):

    pass
class tfsm_Transition(NamedElement):

    def __init__(self, action: str, tfsm_Transition: "tfsm_TFSM" = None, Transition: "tfsm_State" = None, Transition11: "tfsm_State" = None, outgoingTransitions: "tfsm_State" = None, incomingTransitions: "tfsm_State" = None, tfsm_Transition19: set["tfsm_FSMEvent"] = None, tfsm_Transition27: "tfsm_FSMEvent" = None, tfsm_Transition17: "tfsm_Guard" = None):
        self.action = action
        self.tfsm_Transition = tfsm_Transition
        self.Transition = Transition
        self.Transition11 = Transition11
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.tfsm_Transition19 = tfsm_Transition19 if tfsm_Transition19 is not None else set()
        self.tfsm_Transition27 = tfsm_Transition27
        self.tfsm_Transition17 = tfsm_Transition17
        
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
        old_value = getattr(self, f"_tfsm_Transition__outgoingTransitions", None)
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
    def Transition11(self):
        return self.__Transition11

    @Transition11.setter
    def Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__Transition11", None)
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
    def tfsm_Transition27(self):
        return self.__tfsm_Transition27

    @tfsm_Transition27.setter
    def tfsm_Transition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition27", None)
        self.__tfsm_Transition27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSMEvent26"):
                opp_val = getattr(old_value, "tfsm_FSMEvent26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSMEvent26"):
                opp_val = getattr(value, "tfsm_FSMEvent26", None)
                if opp_val is None:
                    setattr(value, "tfsm_FSMEvent26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__Transition", None)
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
    def tfsm_Transition17(self):
        return self.__tfsm_Transition17

    @tfsm_Transition17.setter
    def tfsm_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition17", None)
        self.__tfsm_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_Guard"):
                opp_val = getattr(old_value, "tfsm_Guard", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_Guard"):
                opp_val = getattr(value, "tfsm_Guard", None)
                setattr(value, "tfsm_Guard", self)

    @property
    def tfsm_Transition(self):
        return self.__tfsm_Transition

    @tfsm_Transition.setter
    def tfsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition", None)
        self.__tfsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TFSM7"):
                opp_val = getattr(old_value, "tfsm_TFSM7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TFSM7"):
                opp_val = getattr(value, "tfsm_TFSM7", None)
                if opp_val is None:
                    setattr(value, "tfsm_TFSM7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__incomingTransitions", None)
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

    @property
    def tfsm_Transition19(self):
        return self.__tfsm_Transition19

    @tfsm_Transition19.setter
    def tfsm_Transition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition19", None)
        self.__tfsm_Transition19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_FSMEvent20"):
                    opp_val = getattr(item, "tfsm_FSMEvent20", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_FSMEvent20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_FSMEvent20"):
                    opp_val = getattr(item, "tfsm_FSMEvent20", None)
                    
                    setattr(item, "tfsm_FSMEvent20", self)
                    

class tfsm_TimedSystem(NamedElement):

    pass
class tfsm_FSMEvent(NamedElement):

    pass
class tfsm_TFSM(NamedElement):

    pass