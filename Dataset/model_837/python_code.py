from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Guard:

    pass
class tfsm_EventGuard(Guard):

    pass
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
            if hasattr(old_value, "tfsm_FSMClock25"):
                opp_val = getattr(old_value, "tfsm_FSMClock25", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_FSMClock25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSMClock25"):
                opp_val = getattr(value, "tfsm_FSMClock25", None)
                setattr(value, "tfsm_FSMClock25", self)

class tfsm_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class tfsm_EvaluateGuard(Guard):

    def __init__(self, condition: str):
        self.condition = condition
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    def evaluate(self) -> bool:
        # TODO: Implement evaluate method
        pass

class NamedElement:

    pass
class tfsm_Guard(NamedElement):

    pass
class tfsm_TimedSystem(NamedElement):

    def __init__(self, tfsm_TimedSystem37: set["tfsm_FSMEvent"] = None, tfsm_TimedSystem: set["tfsm_TFSM"] = None, tfsm_TimedSystem34: set["tfsm_FSMClock"] = None):
        self.tfsm_TimedSystem37 = tfsm_TimedSystem37 if tfsm_TimedSystem37 is not None else set()
        self.tfsm_TimedSystem = tfsm_TimedSystem if tfsm_TimedSystem is not None else set()
        self.tfsm_TimedSystem34 = tfsm_TimedSystem34 if tfsm_TimedSystem34 is not None else set()
        
    @property
    def tfsm_TimedSystem(self):
        return self.__tfsm_TimedSystem

    @tfsm_TimedSystem.setter
    def tfsm_TimedSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TimedSystem__tfsm_TimedSystem", None)
        self.__tfsm_TimedSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_TFSM32"):
                    opp_val = getattr(item, "tfsm_TFSM32", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_TFSM32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_TFSM32"):
                    opp_val = getattr(item, "tfsm_TFSM32", None)
                    
                    setattr(item, "tfsm_TFSM32", self)
                    

    @property
    def tfsm_TimedSystem37(self):
        return self.__tfsm_TimedSystem37

    @tfsm_TimedSystem37.setter
    def tfsm_TimedSystem37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TimedSystem__tfsm_TimedSystem37", None)
        self.__tfsm_TimedSystem37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_FSMEvent38"):
                    opp_val = getattr(item, "tfsm_FSMEvent38", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_FSMEvent38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_FSMEvent38"):
                    opp_val = getattr(item, "tfsm_FSMEvent38", None)
                    
                    setattr(item, "tfsm_FSMEvent38", self)
                    

    @property
    def tfsm_TimedSystem34(self):
        return self.__tfsm_TimedSystem34

    @tfsm_TimedSystem34.setter
    def tfsm_TimedSystem34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TimedSystem__tfsm_TimedSystem34", None)
        self.__tfsm_TimedSystem34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_FSMClock35"):
                    opp_val = getattr(item, "tfsm_FSMClock35", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_FSMClock35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_FSMClock35"):
                    opp_val = getattr(item, "tfsm_FSMClock35", None)
                    
                    setattr(item, "tfsm_FSMClock35", self)
                    

    def init(self) -> str:
        # TODO: Implement init method
        pass

class tfsm_Transition(NamedElement):

    def __init__(self, action: str, tfsm_Transition: "tfsm_TFSM" = None, Transition: "tfsm_State" = None, Transition14: "tfsm_State" = None, incomingTransitions: "tfsm_State" = None, tfsm_Transition20: "tfsm_Guard" = None, tfsm_Transition22: set["tfsm_FSMEvent"] = None, tfsm_Transition30: "tfsm_FSMEvent" = None, outgoingTransitions: "tfsm_State" = None):
        self.action = action
        self.tfsm_Transition = tfsm_Transition
        self.Transition = Transition
        self.Transition14 = Transition14
        self.incomingTransitions = incomingTransitions
        self.tfsm_Transition20 = tfsm_Transition20
        self.tfsm_Transition22 = tfsm_Transition22 if tfsm_Transition22 is not None else set()
        self.tfsm_Transition30 = tfsm_Transition30
        self.outgoingTransitions = outgoingTransitions
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def tfsm_Transition30(self):
        return self.__tfsm_Transition30

    @tfsm_Transition30.setter
    def tfsm_Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition30", None)
        self.__tfsm_Transition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSMEvent29"):
                opp_val = getattr(old_value, "tfsm_FSMEvent29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSMEvent29"):
                opp_val = getattr(value, "tfsm_FSMEvent29", None)
                if opp_val is None:
                    setattr(value, "tfsm_FSMEvent29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition14(self):
        return self.__Transition14

    @Transition14.setter
    def Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__Transition14", None)
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
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__outgoingTransitions", None)
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
    def tfsm_Transition20(self):
        return self.__tfsm_Transition20

    @tfsm_Transition20.setter
    def tfsm_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition20", None)
        self.__tfsm_Transition20 = value
        
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
    def incomingTransitions(self):
        return self.__incomingTransitions

    @incomingTransitions.setter
    def incomingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__incomingTransitions", None)
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
    def tfsm_Transition22(self):
        return self.__tfsm_Transition22

    @tfsm_Transition22.setter
    def tfsm_Transition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__tfsm_Transition22", None)
        self.__tfsm_Transition22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_FSMEvent23"):
                    opp_val = getattr(item, "tfsm_FSMEvent23", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_FSMEvent23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_FSMEvent23"):
                    opp_val = getattr(item, "tfsm_FSMEvent23", None)
                    
                    setattr(item, "tfsm_FSMEvent23", self)
                    

    def fire(self) -> str:
        # TODO: Implement fire method
        pass

class tfsm_FSMClock(NamedElement):

    def __init__(self, numberOfTicks: int, tfsm_FSMClock: "tfsm_TFSM" = None, tfsm_FSMClock25: "tfsm_TemporalGuard" = None, tfsm_FSMClock35: "tfsm_TimedSystem" = None):
        self.numberOfTicks = numberOfTicks
        self.tfsm_FSMClock = tfsm_FSMClock
        self.tfsm_FSMClock25 = tfsm_FSMClock25
        self.tfsm_FSMClock35 = tfsm_FSMClock35
        
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
    def tfsm_FSMClock35(self):
        return self.__tfsm_FSMClock35

    @tfsm_FSMClock35.setter
    def tfsm_FSMClock35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMClock__tfsm_FSMClock35", None)
        self.__tfsm_FSMClock35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TimedSystem34"):
                opp_val = getattr(old_value, "tfsm_TimedSystem34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TimedSystem34"):
                opp_val = getattr(value, "tfsm_TimedSystem34", None)
                if opp_val is None:
                    setattr(value, "tfsm_TimedSystem34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_FSMClock25(self):
        return self.__tfsm_FSMClock25

    @tfsm_FSMClock25.setter
    def tfsm_FSMClock25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMClock__tfsm_FSMClock25", None)
        self.__tfsm_FSMClock25 = value
        
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

    def ticks(self) -> str:
        # TODO: Implement ticks method
        pass

class tfsm_FSMEvent(NamedElement):

    def __init__(self, tfsm_FSMEvent: "tfsm_TFSM" = None, tfsm_FSMEvent38: "tfsm_TimedSystem" = None, tfsm_FSMEvent23: "tfsm_Transition" = None, tfsm_FSMEvent27: "tfsm_EventGuard" = None, tfsm_FSMEvent29: set["tfsm_Transition"] = None):
        self.tfsm_FSMEvent = tfsm_FSMEvent
        self.tfsm_FSMEvent38 = tfsm_FSMEvent38
        self.tfsm_FSMEvent23 = tfsm_FSMEvent23
        self.tfsm_FSMEvent27 = tfsm_FSMEvent27
        self.tfsm_FSMEvent29 = tfsm_FSMEvent29 if tfsm_FSMEvent29 is not None else set()
        
    @property
    def tfsm_FSMEvent27(self):
        return self.__tfsm_FSMEvent27

    @tfsm_FSMEvent27.setter
    def tfsm_FSMEvent27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMEvent__tfsm_FSMEvent27", None)
        self.__tfsm_FSMEvent27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_EventGuard"):
                opp_val = getattr(old_value, "tfsm_EventGuard", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_EventGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_EventGuard"):
                opp_val = getattr(value, "tfsm_EventGuard", None)
                setattr(value, "tfsm_EventGuard", self)

    @property
    def tfsm_FSMEvent23(self):
        return self.__tfsm_FSMEvent23

    @tfsm_FSMEvent23.setter
    def tfsm_FSMEvent23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMEvent__tfsm_FSMEvent23", None)
        self.__tfsm_FSMEvent23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_Transition22"):
                opp_val = getattr(old_value, "tfsm_Transition22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_Transition22"):
                opp_val = getattr(value, "tfsm_Transition22", None)
                if opp_val is None:
                    setattr(value, "tfsm_Transition22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_FSMEvent29(self):
        return self.__tfsm_FSMEvent29

    @tfsm_FSMEvent29.setter
    def tfsm_FSMEvent29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMEvent__tfsm_FSMEvent29", None)
        self.__tfsm_FSMEvent29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_Transition30"):
                    opp_val = getattr(item, "tfsm_Transition30", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_Transition30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_Transition30"):
                    opp_val = getattr(item, "tfsm_Transition30", None)
                    
                    setattr(item, "tfsm_Transition30", self)
                    

    @property
    def tfsm_FSMEvent(self):
        return self.__tfsm_FSMEvent

    @tfsm_FSMEvent.setter
    def tfsm_FSMEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMEvent__tfsm_FSMEvent", None)
        self.__tfsm_FSMEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TFSM3"):
                opp_val = getattr(old_value, "tfsm_TFSM3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TFSM3"):
                opp_val = getattr(value, "tfsm_TFSM3", None)
                if opp_val is None:
                    setattr(value, "tfsm_TFSM3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_FSMEvent38(self):
        return self.__tfsm_FSMEvent38

    @tfsm_FSMEvent38.setter
    def tfsm_FSMEvent38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMEvent__tfsm_FSMEvent38", None)
        self.__tfsm_FSMEvent38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TimedSystem37"):
                opp_val = getattr(old_value, "tfsm_TimedSystem37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TimedSystem37"):
                opp_val = getattr(value, "tfsm_TimedSystem37", None)
                if opp_val is None:
                    setattr(value, "tfsm_TimedSystem37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def occurs(self) -> str:
        # TODO: Implement occurs method
        pass

class tfsm_State(NamedElement):

    def __init__(self, State: "tfsm_TFSM" = None, tfsm_State: "tfsm_TFSM" = None, tfsm_State10: "tfsm_TFSM" = None, ownedStates: "tfsm_TFSM" = None, source: set["tfsm_Transition"] = None, target: set["tfsm_Transition"] = None, State18: "tfsm_Transition" = None, State16: "tfsm_Transition" = None):
        self.State = State
        self.tfsm_State = tfsm_State
        self.tfsm_State10 = tfsm_State10
        self.ownedStates = ownedStates
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State18 = State18
        self.State16 = State16
        
    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningFSM"):
                opp_val = getattr(old_value, "owningFSM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningFSM"):
                opp_val = getattr(value, "owningFSM", None)
                if opp_val is None:
                    setattr(value, "owningFSM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__source", None)
        self.__source = value if value is not None else set()
        
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
    def State16(self):
        return self.__State16

    @State16.setter
    def State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__State16", None)
        self.__State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransitions"):
                opp_val = getattr(old_value, "outgoingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransitions"):
                opp_val = getattr(value, "outgoingTransitions", None)
                setattr(value, "outgoingTransitions", self)

    @property
    def tfsm_State(self):
        return self.__tfsm_State

    @tfsm_State.setter
    def tfsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__tfsm_State", None)
        self.__tfsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TFSM"):
                opp_val = getattr(old_value, "tfsm_TFSM", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_TFSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TFSM"):
                opp_val = getattr(value, "tfsm_TFSM", None)
                setattr(value, "tfsm_TFSM", self)

    @property
    def tfsm_State10(self):
        return self.__tfsm_State10

    @tfsm_State10.setter
    def tfsm_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__tfsm_State10", None)
        self.__tfsm_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TFSM9"):
                opp_val = getattr(old_value, "tfsm_TFSM9", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_TFSM9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TFSM9"):
                opp_val = getattr(value, "tfsm_TFSM9", None)
                setattr(value, "tfsm_TFSM9", self)

    @property
    def ownedStates(self):
        return self.__ownedStates

    @ownedStates.setter
    def ownedStates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__ownedStates", None)
        self.__ownedStates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TFSM"):
                opp_val = getattr(old_value, "TFSM", None)
                if opp_val == self:
                    setattr(old_value, "TFSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TFSM"):
                opp_val = getattr(value, "TFSM", None)
                setattr(value, "TFSM", self)

    @property
    def State18(self):
        return self.__State18

    @State18.setter
    def State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__State18", None)
        self.__State18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransitions"):
                opp_val = getattr(old_value, "incomingTransitions", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransitions"):
                opp_val = getattr(value, "incomingTransitions", None)
                setattr(value, "incomingTransitions", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition14"):
                    opp_val = getattr(item, "Transition14", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition14"):
                    opp_val = getattr(item, "Transition14", None)
                    
                    setattr(item, "Transition14", self)
                    

    def onEnter(self) -> str:
        # TODO: Implement onEnter method
        pass

    def onLeave(self) -> str:
        # TODO: Implement onLeave method
        pass

class tfsm_TFSM(NamedElement):

    def __init__(self, owningFSM: set["tfsm_State"] = None, tfsm_TFSM: "tfsm_State" = None, tfsm_TFSM3: set["tfsm_FSMEvent"] = None, tfsm_TFSM5: "tfsm_FSMClock" = None, tfsm_TFSM7: set["tfsm_Transition"] = None, tfsm_TFSM9: "tfsm_State" = None, TFSM: "tfsm_State" = None, tfsm_TFSM32: "tfsm_TimedSystem" = None):
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.tfsm_TFSM = tfsm_TFSM
        self.tfsm_TFSM3 = tfsm_TFSM3 if tfsm_TFSM3 is not None else set()
        self.tfsm_TFSM5 = tfsm_TFSM5
        self.tfsm_TFSM7 = tfsm_TFSM7 if tfsm_TFSM7 is not None else set()
        self.tfsm_TFSM9 = tfsm_TFSM9
        self.TFSM = TFSM
        self.tfsm_TFSM32 = tfsm_TFSM32
        
    @property
    def tfsm_TFSM7(self):
        return self.__tfsm_TFSM7

    @tfsm_TFSM7.setter
    def tfsm_TFSM7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TFSM__tfsm_TFSM7", None)
        self.__tfsm_TFSM7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_Transition"):
                    opp_val = getattr(item, "tfsm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_Transition"):
                    opp_val = getattr(item, "tfsm_Transition", None)
                    
                    setattr(item, "tfsm_Transition", self)
                    

    @property
    def tfsm_TFSM3(self):
        return self.__tfsm_TFSM3

    @tfsm_TFSM3.setter
    def tfsm_TFSM3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TFSM__tfsm_TFSM3", None)
        self.__tfsm_TFSM3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_FSMEvent"):
                    opp_val = getattr(item, "tfsm_FSMEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_FSMEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_FSMEvent"):
                    opp_val = getattr(item, "tfsm_FSMEvent", None)
                    
                    setattr(item, "tfsm_FSMEvent", self)
                    

    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TFSM__owningFSM", None)
        self.__owningFSM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def tfsm_TFSM(self):
        return self.__tfsm_TFSM

    @tfsm_TFSM.setter
    def tfsm_TFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TFSM__tfsm_TFSM", None)
        self.__tfsm_TFSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_State"):
                opp_val = getattr(old_value, "tfsm_State", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_State"):
                opp_val = getattr(value, "tfsm_State", None)
                setattr(value, "tfsm_State", self)

    @property
    def tfsm_TFSM9(self):
        return self.__tfsm_TFSM9

    @tfsm_TFSM9.setter
    def tfsm_TFSM9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TFSM__tfsm_TFSM9", None)
        self.__tfsm_TFSM9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_State10"):
                opp_val = getattr(old_value, "tfsm_State10", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_State10"):
                opp_val = getattr(value, "tfsm_State10", None)
                setattr(value, "tfsm_State10", self)

    @property
    def tfsm_TFSM5(self):
        return self.__tfsm_TFSM5

    @tfsm_TFSM5.setter
    def tfsm_TFSM5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TFSM__tfsm_TFSM5", None)
        self.__tfsm_TFSM5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_FSMClock"):
                opp_val = getattr(old_value, "tfsm_FSMClock", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_FSMClock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSMClock"):
                opp_val = getattr(value, "tfsm_FSMClock", None)
                setattr(value, "tfsm_FSMClock", self)

    @property
    def tfsm_TFSM32(self):
        return self.__tfsm_TFSM32

    @tfsm_TFSM32.setter
    def tfsm_TFSM32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TFSM__tfsm_TFSM32", None)
        self.__tfsm_TFSM32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_TimedSystem"):
                opp_val = getattr(old_value, "tfsm_TimedSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_TimedSystem"):
                opp_val = getattr(value, "tfsm_TimedSystem", None)
                if opp_val is None:
                    setattr(value, "tfsm_TimedSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TFSM(self):
        return self.__TFSM

    @TFSM.setter
    def TFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TFSM__TFSM", None)
        self.__TFSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedStates"):
                opp_val = getattr(old_value, "ownedStates", None)
                if opp_val == self:
                    setattr(old_value, "ownedStates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedStates"):
                opp_val = getattr(value, "ownedStates", None)
                setattr(value, "ownedStates", self)

    def changeCurrentState(self, newState: str):
        # TODO: Implement changeCurrentState method
        pass

    def init(self) -> str:
        # TODO: Implement init method
        pass
