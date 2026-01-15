from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Guard:

    pass
class tfsmextended_EventGuard(Guard):

    pass
class tfsmextended_EvaluateGuard(Guard):

    def __init__(self, condition: str):
        self.condition = condition
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

class tfsmextended_TemporalGuard(Guard):

    def __init__(self, afterDuration: int, tfsmextended_TemporalGuard: "tfsmextended_FSMClock" = None):
        self.afterDuration = afterDuration
        self.tfsmextended_TemporalGuard = tfsmextended_TemporalGuard
        
    @property
    def afterDuration(self) -> int:
        return self.__afterDuration

    @afterDuration.setter
    def afterDuration(self, afterDuration: int):
        self.__afterDuration = afterDuration

    @property
    def tfsmextended_TemporalGuard(self):
        return self.__tfsmextended_TemporalGuard

    @tfsmextended_TemporalGuard.setter
    def tfsmextended_TemporalGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TemporalGuard__tfsmextended_TemporalGuard", None)
        self.__tfsmextended_TemporalGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_FSMClock25"):
                opp_val = getattr(old_value, "tfsmextended_FSMClock25", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_FSMClock25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_FSMClock25"):
                opp_val = getattr(value, "tfsmextended_FSMClock25", None)
                setattr(value, "tfsmextended_FSMClock25", self)

class tfsmextended_NamedElement:

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
class tfsmextended_Guard(NamedElement):

    pass
class tfsmextended_TimedSystem(NamedElement):

    pass
class tfsmextended_FSMEvent(NamedElement):

    def __init__(self, isTriggered: bool, tfsmextended_FSMEvent: "tfsmextended_TFSM" = None, tfsmextended_FSMEvent23: "tfsmextended_Transition" = None, tfsmextended_FSMEvent27: "tfsmextended_EventGuard" = None, tfsmextended_FSMEvent29: set["tfsmextended_Transition"] = None, tfsmextended_FSMEvent38: "tfsmextended_TimedSystem" = None):
        self.isTriggered = isTriggered
        self.tfsmextended_FSMEvent = tfsmextended_FSMEvent
        self.tfsmextended_FSMEvent23 = tfsmextended_FSMEvent23
        self.tfsmextended_FSMEvent27 = tfsmextended_FSMEvent27
        self.tfsmextended_FSMEvent29 = tfsmextended_FSMEvent29 if tfsmextended_FSMEvent29 is not None else set()
        self.tfsmextended_FSMEvent38 = tfsmextended_FSMEvent38
        
    @property
    def isTriggered(self) -> bool:
        return self.__isTriggered

    @isTriggered.setter
    def isTriggered(self, isTriggered: bool):
        self.__isTriggered = isTriggered

    @property
    def tfsmextended_FSMEvent29(self):
        return self.__tfsmextended_FSMEvent29

    @tfsmextended_FSMEvent29.setter
    def tfsmextended_FSMEvent29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMEvent__tfsmextended_FSMEvent29", None)
        self.__tfsmextended_FSMEvent29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsmextended_Transition30"):
                    opp_val = getattr(item, "tfsmextended_Transition30", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsmextended_Transition30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsmextended_Transition30"):
                    opp_val = getattr(item, "tfsmextended_Transition30", None)
                    
                    setattr(item, "tfsmextended_Transition30", self)
                    

    @property
    def tfsmextended_FSMEvent27(self):
        return self.__tfsmextended_FSMEvent27

    @tfsmextended_FSMEvent27.setter
    def tfsmextended_FSMEvent27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMEvent__tfsmextended_FSMEvent27", None)
        self.__tfsmextended_FSMEvent27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_EventGuard"):
                opp_val = getattr(old_value, "tfsmextended_EventGuard", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_EventGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_EventGuard"):
                opp_val = getattr(value, "tfsmextended_EventGuard", None)
                setattr(value, "tfsmextended_EventGuard", self)

    @property
    def tfsmextended_FSMEvent(self):
        return self.__tfsmextended_FSMEvent

    @tfsmextended_FSMEvent.setter
    def tfsmextended_FSMEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMEvent__tfsmextended_FSMEvent", None)
        self.__tfsmextended_FSMEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TFSM3"):
                opp_val = getattr(old_value, "tfsmextended_TFSM3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TFSM3"):
                opp_val = getattr(value, "tfsmextended_TFSM3", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_TFSM3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_FSMEvent23(self):
        return self.__tfsmextended_FSMEvent23

    @tfsmextended_FSMEvent23.setter
    def tfsmextended_FSMEvent23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMEvent__tfsmextended_FSMEvent23", None)
        self.__tfsmextended_FSMEvent23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_Transition22"):
                opp_val = getattr(old_value, "tfsmextended_Transition22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_Transition22"):
                opp_val = getattr(value, "tfsmextended_Transition22", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_Transition22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_FSMEvent38(self):
        return self.__tfsmextended_FSMEvent38

    @tfsmextended_FSMEvent38.setter
    def tfsmextended_FSMEvent38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMEvent__tfsmextended_FSMEvent38", None)
        self.__tfsmextended_FSMEvent38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TimedSystem37"):
                opp_val = getattr(old_value, "tfsmextended_TimedSystem37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TimedSystem37"):
                opp_val = getattr(value, "tfsmextended_TimedSystem37", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_TimedSystem37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def trigger(self):
        # TODO: Implement trigger method
        pass

    def unTrigger(self):
        # TODO: Implement unTrigger method
        pass

class tfsmextended_FSMClock(NamedElement):

    def __init__(self, numberOfTicks: str, tfsmextended_FSMClock: "tfsmextended_TFSM" = None, tfsmextended_FSMClock25: "tfsmextended_TemporalGuard" = None, tfsmextended_FSMClock35: "tfsmextended_TimedSystem" = None):
        self.numberOfTicks = numberOfTicks
        self.tfsmextended_FSMClock = tfsmextended_FSMClock
        self.tfsmextended_FSMClock25 = tfsmextended_FSMClock25
        self.tfsmextended_FSMClock35 = tfsmextended_FSMClock35
        
    @property
    def numberOfTicks(self) -> str:
        return self.__numberOfTicks

    @numberOfTicks.setter
    def numberOfTicks(self, numberOfTicks: str):
        self.__numberOfTicks = numberOfTicks

    @property
    def tfsmextended_FSMClock(self):
        return self.__tfsmextended_FSMClock

    @tfsmextended_FSMClock.setter
    def tfsmextended_FSMClock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMClock__tfsmextended_FSMClock", None)
        self.__tfsmextended_FSMClock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TFSM5"):
                opp_val = getattr(old_value, "tfsmextended_TFSM5", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_TFSM5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TFSM5"):
                opp_val = getattr(value, "tfsmextended_TFSM5", None)
                setattr(value, "tfsmextended_TFSM5", self)

    @property
    def tfsmextended_FSMClock25(self):
        return self.__tfsmextended_FSMClock25

    @tfsmextended_FSMClock25.setter
    def tfsmextended_FSMClock25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMClock__tfsmextended_FSMClock25", None)
        self.__tfsmextended_FSMClock25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TemporalGuard"):
                opp_val = getattr(old_value, "tfsmextended_TemporalGuard", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_TemporalGuard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TemporalGuard"):
                opp_val = getattr(value, "tfsmextended_TemporalGuard", None)
                setattr(value, "tfsmextended_TemporalGuard", self)

    @property
    def tfsmextended_FSMClock35(self):
        return self.__tfsmextended_FSMClock35

    @tfsmextended_FSMClock35.setter
    def tfsmextended_FSMClock35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_FSMClock__tfsmextended_FSMClock35", None)
        self.__tfsmextended_FSMClock35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TimedSystem34"):
                opp_val = getattr(old_value, "tfsmextended_TimedSystem34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TimedSystem34"):
                opp_val = getattr(value, "tfsmextended_TimedSystem34", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_TimedSystem34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def ticks(self) -> str:
        # TODO: Implement ticks method
        pass

class tfsmextended_Transition(NamedElement):

    def __init__(self, action: str, tfsmextended_Transition: "tfsmextended_TFSM" = None, Transition: "tfsmextended_State" = None, Transition14: "tfsmextended_State" = None, outgoingTransitions: "tfsmextended_State" = None, incomingTransitions: "tfsmextended_State" = None, tfsmextended_Transition20: "tfsmextended_Guard" = None, tfsmextended_Transition22: set["tfsmextended_FSMEvent"] = None, tfsmextended_Transition30: "tfsmextended_FSMEvent" = None):
        self.action = action
        self.tfsmextended_Transition = tfsmextended_Transition
        self.Transition = Transition
        self.Transition14 = Transition14
        self.outgoingTransitions = outgoingTransitions
        self.incomingTransitions = incomingTransitions
        self.tfsmextended_Transition20 = tfsmextended_Transition20
        self.tfsmextended_Transition22 = tfsmextended_Transition22 if tfsmextended_Transition22 is not None else set()
        self.tfsmextended_Transition30 = tfsmextended_Transition30
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def tfsmextended_Transition(self):
        return self.__tfsmextended_Transition

    @tfsmextended_Transition.setter
    def tfsmextended_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__tfsmextended_Transition", None)
        self.__tfsmextended_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TFSM7"):
                opp_val = getattr(old_value, "tfsmextended_TFSM7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TFSM7"):
                opp_val = getattr(value, "tfsmextended_TFSM7", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_TFSM7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_Transition20(self):
        return self.__tfsmextended_Transition20

    @tfsmextended_Transition20.setter
    def tfsmextended_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__tfsmextended_Transition20", None)
        self.__tfsmextended_Transition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_Guard"):
                opp_val = getattr(old_value, "tfsmextended_Guard", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_Guard"):
                opp_val = getattr(value, "tfsmextended_Guard", None)
                setattr(value, "tfsmextended_Guard", self)

    @property
    def tfsmextended_Transition30(self):
        return self.__tfsmextended_Transition30

    @tfsmextended_Transition30.setter
    def tfsmextended_Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__tfsmextended_Transition30", None)
        self.__tfsmextended_Transition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_FSMEvent29"):
                opp_val = getattr(old_value, "tfsmextended_FSMEvent29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_FSMEvent29"):
                opp_val = getattr(value, "tfsmextended_FSMEvent29", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_FSMEvent29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_Transition22(self):
        return self.__tfsmextended_Transition22

    @tfsmextended_Transition22.setter
    def tfsmextended_Transition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__tfsmextended_Transition22", None)
        self.__tfsmextended_Transition22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsmextended_FSMEvent23"):
                    opp_val = getattr(item, "tfsmextended_FSMEvent23", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsmextended_FSMEvent23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsmextended_FSMEvent23"):
                    opp_val = getattr(item, "tfsmextended_FSMEvent23", None)
                    
                    setattr(item, "tfsmextended_FSMEvent23", self)
                    

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__Transition", None)
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
        old_value = getattr(self, f"_tfsmextended_Transition__incomingTransitions", None)
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
    def outgoingTransitions(self):
        return self.__outgoingTransitions

    @outgoingTransitions.setter
    def outgoingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_Transition__outgoingTransitions", None)
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
        old_value = getattr(self, f"_tfsmextended_Transition__Transition14", None)
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

    def fire(self):
        # TODO: Implement fire method
        pass

class tfsmextended_State(NamedElement):

    def __init__(self, State: "tfsmextended_TFSM" = None, tfsmextended_State: "tfsmextended_TFSM" = None, tfsmextended_State10: "tfsmextended_TFSM" = None, ownedStates: "tfsmextended_TFSM" = None, source: set["tfsmextended_Transition"] = None, target: set["tfsmextended_Transition"] = None, State16: "tfsmextended_Transition" = None, State18: "tfsmextended_Transition" = None):
        self.State = State
        self.tfsmextended_State = tfsmextended_State
        self.tfsmextended_State10 = tfsmextended_State10
        self.ownedStates = ownedStates
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State16 = State16
        self.State18 = State18
        
    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__target", None)
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
                    

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__State", None)
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
    def tfsmextended_State(self):
        return self.__tfsmextended_State

    @tfsmextended_State.setter
    def tfsmextended_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__tfsmextended_State", None)
        self.__tfsmextended_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TFSM"):
                opp_val = getattr(old_value, "tfsmextended_TFSM", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_TFSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TFSM"):
                opp_val = getattr(value, "tfsmextended_TFSM", None)
                setattr(value, "tfsmextended_TFSM", self)

    @property
    def State18(self):
        return self.__State18

    @State18.setter
    def State18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__State18", None)
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
    def ownedStates(self):
        return self.__ownedStates

    @ownedStates.setter
    def ownedStates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__ownedStates", None)
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__source", None)
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
    def tfsmextended_State10(self):
        return self.__tfsmextended_State10

    @tfsmextended_State10.setter
    def tfsmextended_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__tfsmextended_State10", None)
        self.__tfsmextended_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TFSM9"):
                opp_val = getattr(old_value, "tfsmextended_TFSM9", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_TFSM9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TFSM9"):
                opp_val = getattr(value, "tfsmextended_TFSM9", None)
                setattr(value, "tfsmextended_TFSM9", self)

    @property
    def State16(self):
        return self.__State16

    @State16.setter
    def State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_State__State16", None)
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

    def onLeave(self):
        # TODO: Implement onLeave method
        pass

    def onEnter(self):
        # TODO: Implement onEnter method
        pass

class tfsmextended_TFSM(NamedElement):

    def __init__(self, owningFSM: set["tfsmextended_State"] = None, tfsmextended_TFSM: "tfsmextended_State" = None, tfsmextended_TFSM3: set["tfsmextended_FSMEvent"] = None, tfsmextended_TFSM5: "tfsmextended_FSMClock" = None, tfsmextended_TFSM7: set["tfsmextended_Transition"] = None, tfsmextended_TFSM9: "tfsmextended_State" = None, TFSM: "tfsmextended_State" = None, tfsmextended_TFSM32: "tfsmextended_TimedSystem" = None):
        self.owningFSM = owningFSM if owningFSM is not None else set()
        self.tfsmextended_TFSM = tfsmextended_TFSM
        self.tfsmextended_TFSM3 = tfsmextended_TFSM3 if tfsmextended_TFSM3 is not None else set()
        self.tfsmextended_TFSM5 = tfsmextended_TFSM5
        self.tfsmextended_TFSM7 = tfsmextended_TFSM7 if tfsmextended_TFSM7 is not None else set()
        self.tfsmextended_TFSM9 = tfsmextended_TFSM9
        self.TFSM = TFSM
        self.tfsmextended_TFSM32 = tfsmextended_TFSM32
        
    @property
    def tfsmextended_TFSM5(self):
        return self.__tfsmextended_TFSM5

    @tfsmextended_TFSM5.setter
    def tfsmextended_TFSM5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM5", None)
        self.__tfsmextended_TFSM5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_FSMClock"):
                opp_val = getattr(old_value, "tfsmextended_FSMClock", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_FSMClock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_FSMClock"):
                opp_val = getattr(value, "tfsmextended_FSMClock", None)
                setattr(value, "tfsmextended_FSMClock", self)

    @property
    def tfsmextended_TFSM7(self):
        return self.__tfsmextended_TFSM7

    @tfsmextended_TFSM7.setter
    def tfsmextended_TFSM7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM7", None)
        self.__tfsmextended_TFSM7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsmextended_Transition"):
                    opp_val = getattr(item, "tfsmextended_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsmextended_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsmextended_Transition"):
                    opp_val = getattr(item, "tfsmextended_Transition", None)
                    
                    setattr(item, "tfsmextended_Transition", self)
                    

    @property
    def TFSM(self):
        return self.__TFSM

    @TFSM.setter
    def TFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__TFSM", None)
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
    def tfsmextended_TFSM(self):
        return self.__tfsmextended_TFSM

    @tfsmextended_TFSM.setter
    def tfsmextended_TFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM", None)
        self.__tfsmextended_TFSM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_State"):
                opp_val = getattr(old_value, "tfsmextended_State", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_State"):
                opp_val = getattr(value, "tfsmextended_State", None)
                setattr(value, "tfsmextended_State", self)

    @property
    def owningFSM(self):
        return self.__owningFSM

    @owningFSM.setter
    def owningFSM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__owningFSM", None)
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
    def tfsmextended_TFSM32(self):
        return self.__tfsmextended_TFSM32

    @tfsmextended_TFSM32.setter
    def tfsmextended_TFSM32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM32", None)
        self.__tfsmextended_TFSM32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_TimedSystem"):
                opp_val = getattr(old_value, "tfsmextended_TimedSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_TimedSystem"):
                opp_val = getattr(value, "tfsmextended_TimedSystem", None)
                if opp_val is None:
                    setattr(value, "tfsmextended_TimedSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tfsmextended_TFSM9(self):
        return self.__tfsmextended_TFSM9

    @tfsmextended_TFSM9.setter
    def tfsmextended_TFSM9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM9", None)
        self.__tfsmextended_TFSM9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tfsmextended_State10"):
                opp_val = getattr(old_value, "tfsmextended_State10", None)
                if opp_val == self:
                    setattr(old_value, "tfsmextended_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsmextended_State10"):
                opp_val = getattr(value, "tfsmextended_State10", None)
                setattr(value, "tfsmextended_State10", self)

    @property
    def tfsmextended_TFSM3(self):
        return self.__tfsmextended_TFSM3

    @tfsmextended_TFSM3.setter
    def tfsmextended_TFSM3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsmextended_TFSM__tfsmextended_TFSM3", None)
        self.__tfsmextended_TFSM3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tfsmextended_FSMEvent"):
                    opp_val = getattr(item, "tfsmextended_FSMEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "tfsmextended_FSMEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tfsmextended_FSMEvent"):
                    opp_val = getattr(item, "tfsmextended_FSMEvent", None)
                    
                    setattr(item, "tfsmextended_FSMEvent", self)
                    

    def init(self):
        # TODO: Implement init method
        pass
