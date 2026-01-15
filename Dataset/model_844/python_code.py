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

    def evaluate(self) -> bool:
        # TODO: Implement evaluate method
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

    def __init__(self, State: "tfsm_TFSM" = None, tfsm_State: "tfsm_TFSM" = None, State13: "tfsm_Transition" = None, State15: "tfsm_Transition" = None, ownedStates: "tfsm_TFSM" = None, source: set["tfsm_Transition"] = None, target: set["tfsm_Transition"] = None):
        self.State = State
        self.tfsm_State = tfsm_State
        self.State13 = State13
        self.State15 = State15
        self.ownedStates = ownedStates
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        
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
    def State15(self):
        return self.__State15

    @State15.setter
    def State15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__State15", None)
        self.__State15 = value
        
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
    def State13(self):
        return self.__State13

    @State13.setter
    def State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__State13", None)
        self.__State13 = value
        
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
                if hasattr(item, "Transition11"):
                    opp_val = getattr(item, "Transition11", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition11"):
                    opp_val = getattr(item, "Transition11", None)
                    
                    setattr(item, "Transition11", self)
                    

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
                    

    def onLeave(self):
        # TODO: Implement onLeave method
        pass

    def onEnter(self):
        # TODO: Implement onEnter method
        pass

class tfsm_FSMEvent(NamedElement):

    def __init__(self, tfsm_FSMEvent20: "tfsm_Transition" = None, tfsm_FSMEvent24: "tfsm_EventGuard" = None, tfsm_FSMEvent: "tfsm_TFSM" = None, tfsm_FSMEvent26: set["tfsm_Transition"] = None, tfsm_FSMEvent35: "tfsm_TimedSystem" = None):
        self.tfsm_FSMEvent20 = tfsm_FSMEvent20
        self.tfsm_FSMEvent24 = tfsm_FSMEvent24
        self.tfsm_FSMEvent = tfsm_FSMEvent
        self.tfsm_FSMEvent26 = tfsm_FSMEvent26 if tfsm_FSMEvent26 is not None else set()
        self.tfsm_FSMEvent35 = tfsm_FSMEvent35
        
    @property
    def tfsm_FSMEvent20(self):
        return self.__tfsm_FSMEvent20

    @tfsm_FSMEvent20.setter
    def tfsm_FSMEvent20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMEvent__tfsm_FSMEvent20", None)
        self.__tfsm_FSMEvent20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsm_Transition19"):
                opp_val = getattr(old_value, "tfsm_Transition19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_Transition19"):
                opp_val = getattr(value, "tfsm_Transition19", None)
                if opp_val is None:
                    setattr(value, "tfsm_Transition19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsm_FSMEvent35(self):
        return self.__tfsm_FSMEvent35

    @tfsm_FSMEvent35.setter
    def tfsm_FSMEvent35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMEvent__tfsm_FSMEvent35", None)
        self.__tfsm_FSMEvent35 = value
        
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
    def tfsm_FSMEvent24(self):
        return self.__tfsm_FSMEvent24

    @tfsm_FSMEvent24.setter
    def tfsm_FSMEvent24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMEvent__tfsm_FSMEvent24", None)
        self.__tfsm_FSMEvent24 = value
        
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
    def tfsm_FSMEvent26(self):
        return self.__tfsm_FSMEvent26

    @tfsm_FSMEvent26.setter
    def tfsm_FSMEvent26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_FSMEvent__tfsm_FSMEvent26", None)
        self.__tfsm_FSMEvent26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_Transition27"):
                    opp_val = getattr(item, "tfsm_Transition27", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_Transition27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_Transition27"):
                    opp_val = getattr(item, "tfsm_Transition27", None)
                    
                    setattr(item, "tfsm_Transition27", self)
                    

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

    def occurs(self):
        # TODO: Implement occurs method
        pass

class tfsm_Guard(NamedElement):

    pass
class tfsm_FSMClock(NamedElement):

    def __init__(self, tfsm_FSMClock22: "tfsm_TemporalGuard" = None, tfsm_FSMClock: "tfsm_TFSM" = None, tfsm_FSMClock32: "tfsm_TimedSystem" = None):
        self.tfsm_FSMClock22 = tfsm_FSMClock22
        self.tfsm_FSMClock = tfsm_FSMClock
        self.tfsm_FSMClock32 = tfsm_FSMClock32
        
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

    def ticks(self):
        # TODO: Implement ticks method
        pass

class tfsm_TimedSystem(NamedElement):

    def __init__(self, tfsm_TimedSystem: set["tfsm_TFSM"] = None, tfsm_TimedSystem31: set["tfsm_FSMClock"] = None, tfsm_TimedSystem34: set["tfsm_FSMEvent"] = None):
        self.tfsm_TimedSystem = tfsm_TimedSystem if tfsm_TimedSystem is not None else set()
        self.tfsm_TimedSystem31 = tfsm_TimedSystem31 if tfsm_TimedSystem31 is not None else set()
        self.tfsm_TimedSystem34 = tfsm_TimedSystem34 if tfsm_TimedSystem34 is not None else set()
        
    @property
    def tfsm_TimedSystem31(self):
        return self.__tfsm_TimedSystem31

    @tfsm_TimedSystem31.setter
    def tfsm_TimedSystem31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TimedSystem__tfsm_TimedSystem31", None)
        self.__tfsm_TimedSystem31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsm_FSMClock32"):
                    opp_val = getattr(item, "tfsm_FSMClock32", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_FSMClock32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_FSMClock32"):
                    opp_val = getattr(item, "tfsm_FSMClock32", None)
                    
                    setattr(item, "tfsm_FSMClock32", self)
                    

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
                if hasattr(item, "tfsm_TFSM29"):
                    opp_val = getattr(item, "tfsm_TFSM29", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_TFSM29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_TFSM29"):
                    opp_val = getattr(item, "tfsm_TFSM29", None)
                    
                    setattr(item, "tfsm_TFSM29", self)
                    

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
                if hasattr(item, "tfsm_FSMEvent35"):
                    opp_val = getattr(item, "tfsm_FSMEvent35", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsm_FSMEvent35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsm_FSMEvent35"):
                    opp_val = getattr(item, "tfsm_FSMEvent35", None)
                    
                    setattr(item, "tfsm_FSMEvent35", self)
                    

    def initialize(self):
        # TODO: Implement initialize method
        pass

class tfsm_Transition(NamedElement):

    def __init__(self, action: str, outgoingTransitions: "tfsm_State" = None, incomingTransitions: "tfsm_State" = None, tfsm_Transition17: "tfsm_Guard" = None, tfsm_Transition19: set["tfsm_FSMEvent"] = None, tfsm_Transition: "tfsm_TFSM" = None, Transition: "tfsm_State" = None, Transition11: "tfsm_State" = None, tfsm_Transition27: "tfsm_FSMEvent" = None):
        self.action = action
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.tfsm_Transition17 = tfsm_Transition17
        self.tfsm_Transition19 = tfsm_Transition19 if tfsm_Transition19 is not None else set()
        self.tfsm_Transition = tfsm_Transition
        self.Transition = Transition
        self.Transition11 = Transition11
        self.tfsm_Transition27 = tfsm_Transition27
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

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
                    

    def fire(self):
        # TODO: Implement fire method
        pass

class tfsm_TFSM(NamedElement):

    def __init__(self, owningFSM: set["tfsm_State"] = None, tfsm_TFSM: "tfsm_State" = None, tfsm_TFSM3: set["tfsm_FSMEvent"] = None, tfsm_TFSM5: "tfsm_FSMClock" = None, tfsm_TFSM7: set["tfsm_Transition"] = None, TFSM: "tfsm_State" = None, tfsm_TFSM29: "tfsm_TimedSystem" = None):
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.tfsm_TFSM = tfsm_TFSM
        self.tfsm_TFSM3 = tfsm_TFSM3 if tfsm_TFSM3 is not None else set()
        self.tfsm_TFSM5 = tfsm_TFSM5
        self.tfsm_TFSM7 = tfsm_TFSM7 if tfsm_TFSM7 is not None else set()
        self.TFSM = TFSM
        self.tfsm_TFSM29 = tfsm_TFSM29
        
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
    def tfsm_TFSM29(self):
        return self.__tfsm_TFSM29

    @tfsm_TFSM29.setter
    def tfsm_TFSM29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_TFSM__tfsm_TFSM29", None)
        self.__tfsm_TFSM29 = value
        
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
                    

    def initialize(self):
        # TODO: Implement initialize method
        pass
