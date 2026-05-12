from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class tfsm_plaink3_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Guard:

    pass
class tfsm_plaink3_EvaluateGuard(Guard):

    def __init__(self, condition: str):
        self.condition = condition
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


class tfsm_plaink3_EventGuard(Guard):

    pass
class tfsm_plaink3_TemporalGuard(Guard):

    def __init__(self, afterDuration: int, tfsm_plaink3_TemporalGuard: "tfsm_plaink3_FSMClock" = None):
        self.afterDuration = afterDuration
        self.tfsm_plaink3_TemporalGuard = tfsm_plaink3_TemporalGuard
        
        pass
    @property
    def afterDuration(self):
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
            if hasattr(old_value, "tfsm_plaink3_FSMClock25"):
                opp_val = getattr(old_value, "tfsm_plaink3_FSMClock25", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_FSMClock25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_FSMClock25"):
                opp_val = getattr(value, "tfsm_plaink3_FSMClock25", None)
                setattr(value, "tfsm_plaink3_FSMClock25", self)

class NamedElement:

    pass
class tfsm_plaink3_FSMEvent(NamedElement):

    def __init__(self, isTriggered: bool, tfsm_plaink3_FSMEvent: "tfsm_plaink3_TFSM" = None, tfsm_plaink3_FSMEvent23: "tfsm_plaink3_Transition" = None, tfsm_plaink3_FSMEvent27: "tfsm_plaink3_EventGuard" = None, tfsm_plaink3_FSMEvent29: set["tfsm_plaink3_Transition"] = None, tfsm_plaink3_FSMEvent38: "tfsm_plaink3_TimedSystem" = None):
        self.isTriggered = isTriggered
        self.tfsm_plaink3_FSMEvent = tfsm_plaink3_FSMEvent
        self.tfsm_plaink3_FSMEvent23 = tfsm_plaink3_FSMEvent23
        self.tfsm_plaink3_FSMEvent27 = tfsm_plaink3_FSMEvent27
        self.tfsm_plaink3_FSMEvent29 = tfsm_plaink3_FSMEvent29 if tfsm_plaink3_FSMEvent29 is not None else set()
        self.tfsm_plaink3_FSMEvent38 = tfsm_plaink3_FSMEvent38
        
        pass
    @property
    def isTriggered(self):
        return self.__isTriggered

    @isTriggered.setter
    def isTriggered(self, isTriggered: bool):
        self.__isTriggered = isTriggered


    @property
    def tfsm_plaink3_FSMEvent(self):
        return self.__tfsm_plaink3_FSMEvent

    @tfsm_plaink3_FSMEvent.setter
    def tfsm_plaink3_FSMEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMEvent__tfsm_plaink3_FSMEvent", None)
        self.__tfsm_plaink3_FSMEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TFSM3"):
                opp_val = getattr(old_value, "tfsm_plaink3_TFSM3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TFSM3"):
                opp_val = getattr(value, "tfsm_plaink3_TFSM3", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_TFSM3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_FSMEvent38(self):
        return self.__tfsm_plaink3_FSMEvent38

    @tfsm_plaink3_FSMEvent38.setter
    def tfsm_plaink3_FSMEvent38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMEvent__tfsm_plaink3_FSMEvent38", None)
        self.__tfsm_plaink3_FSMEvent38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TimedSystem37"):
                opp_val = getattr(old_value, "tfsm_plaink3_TimedSystem37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TimedSystem37"):
                opp_val = getattr(value, "tfsm_plaink3_TimedSystem37", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_TimedSystem37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_FSMEvent27(self):
        return self.__tfsm_plaink3_FSMEvent27

    @tfsm_plaink3_FSMEvent27.setter
    def tfsm_plaink3_FSMEvent27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMEvent__tfsm_plaink3_FSMEvent27", None)
        self.__tfsm_plaink3_FSMEvent27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_EventGuard"):
                opp_val = getattr(old_value, "tfsm_plaink3_EventGuard", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_EventGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_EventGuard"):
                opp_val = getattr(value, "tfsm_plaink3_EventGuard", None)
                setattr(value, "tfsm_plaink3_EventGuard", self)

    @property
    def tfsm_plaink3_FSMEvent23(self):
        return self.__tfsm_plaink3_FSMEvent23

    @tfsm_plaink3_FSMEvent23.setter
    def tfsm_plaink3_FSMEvent23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMEvent__tfsm_plaink3_FSMEvent23", None)
        self.__tfsm_plaink3_FSMEvent23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_Transition22"):
                opp_val = getattr(old_value, "tfsm_plaink3_Transition22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_Transition22"):
                opp_val = getattr(value, "tfsm_plaink3_Transition22", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_Transition22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_plaink3_FSMEvent29(self):
        return self.__tfsm_plaink3_FSMEvent29

    @tfsm_plaink3_FSMEvent29.setter
    def tfsm_plaink3_FSMEvent29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMEvent__tfsm_plaink3_FSMEvent29", None)
        self.__tfsm_plaink3_FSMEvent29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_plaink3_Transition30"):
                    opp_val = getattr(item, "tfsm_plaink3_Transition30", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_plaink3_Transition30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_plaink3_Transition30"):
                    opp_val = getattr(item, "tfsm_plaink3_Transition30", None)
                    
                    setattr(item, "tfsm_plaink3_Transition30", self)
                    

class tfsm_plaink3_TimedSystem(NamedElement):

    pass
class tfsm_plaink3_FSMClock(NamedElement):

    def __init__(self, numberOfTicks: str, tfsm_plaink3_FSMClock: "tfsm_plaink3_TFSM" = None, tfsm_plaink3_FSMClock25: "tfsm_plaink3_TemporalGuard" = None, tfsm_plaink3_FSMClock35: "tfsm_plaink3_TimedSystem" = None):
        self.numberOfTicks = numberOfTicks
        self.tfsm_plaink3_FSMClock = tfsm_plaink3_FSMClock
        self.tfsm_plaink3_FSMClock25 = tfsm_plaink3_FSMClock25
        self.tfsm_plaink3_FSMClock35 = tfsm_plaink3_FSMClock35
        
        pass
    @property
    def numberOfTicks(self):
        return self.__numberOfTicks

    @numberOfTicks.setter
    def numberOfTicks(self, numberOfTicks: str):
        self.__numberOfTicks = numberOfTicks


    @property
    def tfsm_plaink3_FSMClock25(self):
        return self.__tfsm_plaink3_FSMClock25

    @tfsm_plaink3_FSMClock25.setter
    def tfsm_plaink3_FSMClock25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMClock__tfsm_plaink3_FSMClock25", None)
        self.__tfsm_plaink3_FSMClock25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TemporalGuard"):
                opp_val = getattr(old_value, "tfsm_plaink3_TemporalGuard", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_TemporalGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TemporalGuard"):
                opp_val = getattr(value, "tfsm_plaink3_TemporalGuard", None)
                setattr(value, "tfsm_plaink3_TemporalGuard", self)

    @property
    def tfsm_plaink3_FSMClock(self):
        return self.__tfsm_plaink3_FSMClock

    @tfsm_plaink3_FSMClock.setter
    def tfsm_plaink3_FSMClock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMClock__tfsm_plaink3_FSMClock", None)
        self.__tfsm_plaink3_FSMClock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TFSM5"):
                opp_val = getattr(old_value, "tfsm_plaink3_TFSM5", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_plaink3_TFSM5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TFSM5"):
                opp_val = getattr(value, "tfsm_plaink3_TFSM5", None)
                setattr(value, "tfsm_plaink3_TFSM5", self)

    @property
    def tfsm_plaink3_FSMClock35(self):
        return self.__tfsm_plaink3_FSMClock35

    @tfsm_plaink3_FSMClock35.setter
    def tfsm_plaink3_FSMClock35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_FSMClock__tfsm_plaink3_FSMClock35", None)
        self.__tfsm_plaink3_FSMClock35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_TimedSystem34"):
                opp_val = getattr(old_value, "tfsm_plaink3_TimedSystem34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_TimedSystem34"):
                opp_val = getattr(value, "tfsm_plaink3_TimedSystem34", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_TimedSystem34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tfsm_plaink3_Guard(NamedElement):

    pass
class tfsm_plaink3_Transition(NamedElement):

    def __init__(self, action: str, tfsm_plaink3_Transition: "tfsm_plaink3_TFSM" = None, Transition: "tfsm_plaink3_State" = None, Transition14: "tfsm_plaink3_State" = None, outgoingTransitions: "tfsm_plaink3_State" = None, incomingTransitions: "tfsm_plaink3_State" = None, tfsm_plaink3_Transition20: "tfsm_plaink3_Guard" = None, tfsm_plaink3_Transition22: set["tfsm_plaink3_FSMEvent"] = None, tfsm_plaink3_Transition30: "tfsm_plaink3_FSMEvent" = None):
        self.action = action
        self.tfsm_plaink3_Transition = tfsm_plaink3_Transition
        self.Transition = Transition
        self.Transition14 = Transition14
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.tfsm_plaink3_Transition20 = tfsm_plaink3_Transition20
        self.tfsm_plaink3_Transition22 = tfsm_plaink3_Transition22 if tfsm_plaink3_Transition22 is not None else set()
        self.tfsm_plaink3_Transition30 = tfsm_plaink3_Transition30
        
        pass
    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


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
    def tfsm_plaink3_Transition20(self):
        return self.__tfsm_plaink3_Transition20

    @tfsm_plaink3_Transition20.setter
    def tfsm_plaink3_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition20", None)
        self.__tfsm_plaink3_Transition20 = value
        
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
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__incomingTransitions", None)
        self.__incomingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State18"):
                opp_val = getattr(old_value, "State18", None)
                if opp_val == self:
                    setattr(old_value, "State18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State18"):
                opp_val = getattr(value, "State18", None)
                setattr(value, "State18", self)

    @property
    def tfsm_plaink3_Transition22(self):
        return self.__tfsm_plaink3_Transition22

    @tfsm_plaink3_Transition22.setter
    def tfsm_plaink3_Transition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition22", None)
        self.__tfsm_plaink3_Transition22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_plaink3_FSMEvent23"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMEvent23", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_plaink3_FSMEvent23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_plaink3_FSMEvent23"):
                    opp_val = getattr(item, "tfsm_plaink3_FSMEvent23", None)
                    
                    setattr(item, "tfsm_plaink3_FSMEvent23", self)
                    

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
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__outgoingTransitions", None)
        self.__outgoingTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State16"):
                opp_val = getattr(old_value, "State16", None)
                if opp_val == self:
                    setattr(old_value, "State16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State16"):
                opp_val = getattr(value, "State16", None)
                setattr(value, "State16", self)

    @property
    def Transition14(self):
        return self.__Transition14

    @Transition14.setter
    def Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__Transition14", None)
        self.__Transition14 = value
        
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
    def tfsm_plaink3_Transition30(self):
        return self.__tfsm_plaink3_Transition30

    @tfsm_plaink3_Transition30.setter
    def tfsm_plaink3_Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_plaink3_Transition__tfsm_plaink3_Transition30", None)
        self.__tfsm_plaink3_Transition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_plaink3_FSMEvent29"):
                opp_val = getattr(old_value, "tfsm_plaink3_FSMEvent29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_plaink3_FSMEvent29"):
                opp_val = getattr(value, "tfsm_plaink3_FSMEvent29", None)
                if opp_val is None:
                    setattr(value, "tfsm_plaink3_FSMEvent29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tfsm_plaink3_State(NamedElement):

    pass
class tfsm_plaink3_TFSM(NamedElement):

    pass