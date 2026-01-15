from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class tfsm_System:

    pass
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
            if hasattr(old_value, "tfsm_FSMClock17"):
                opp_val = getattr(old_value, "tfsm_FSMClock17", None)
                if opp_val == self:
                    setattr(old_value, "tfsm_FSMClock17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tfsm_FSMClock17"):
                opp_val = getattr(value, "tfsm_FSMClock17", None)
                setattr(value, "tfsm_FSMClock17", self)

class tfsm_NamedElement:

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
class tfsm_Guard(NamedElement):

    pass
class tfsm_Transition(NamedElement):

    def __init__(self, action: str, Transition: "tfsm_State" = None, Transition9: "tfsm_State" = None, outgoingTransition: "tfsm_State" = None, incomingTransition: "tfsm_State" = None, tfsm_Transition: "tfsm_Guard" = None, sollicitingTransitions: set["tfsm_FSMEvent"] = None, Transition21: "tfsm_FSMEvent" = None):
        self.action = action
        self.Transition = Transition
        self.Transition9 = Transition9
        self.outgoingTransition = outgoingTransition
        self.incomingTransition = incomingTransition
        self.tfsm_Transition = tfsm_Transition
        self.sollicitingTransitions = sollicitingTransitions if sollicitingTransitions is not None else set()
        self.Transition21 = Transition21
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def incomingTransition(self):
        return self.__incomingTransition

    @incomingTransition.setter
    def incomingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__incomingTransition", None)
        self.__incomingTransition = value
        
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
    def outgoingTransition(self):
        return self.__outgoingTransition

    @outgoingTransition.setter
    def outgoingTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__outgoingTransition", None)
        self.__outgoingTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State11"):
                opp_val = getattr(old_value, "State11", None)
                if opp_val == self:
                    setattr(old_value, "State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State11"):
                opp_val = getattr(value, "State11", None)
                setattr(value, "State11", self)

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
    def Transition21(self):
        return self.__Transition21

    @Transition21.setter
    def Transition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__Transition21", None)
        self.__Transition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatedEvents"):
                opp_val = getattr(old_value, "generatedEvents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatedEvents"):
                opp_val = getattr(value, "generatedEvents", None)
                if opp_val is None:
                    setattr(value, "generatedEvents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sollicitingTransitions(self):
        return self.__sollicitingTransitions

    @sollicitingTransitions.setter
    def sollicitingTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__sollicitingTransitions", None)
        self.__sollicitingTransitions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FSMEvent"):
                    opp_val = getattr(item, "FSMEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "FSMEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FSMEvent"):
                    opp_val = getattr(item, "FSMEvent", None)
                    
                    setattr(item, "FSMEvent", self)
                    

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
    def Transition9(self):
        return self.__Transition9

    @Transition9.setter
    def Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_Transition__Transition9", None)
        self.__Transition9 = value
        
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

    def fire(self) -> str:
        # TODO: Implement fire method
        pass

class tfsm_FSMClock(NamedElement):

    pass
class tfsm_State(NamedElement):

    def __init__(self, ownedState: "tfsm_TFSM" = None, source: set["tfsm_Transition"] = None, target: set["tfsm_Transition"] = None, State11: "tfsm_Transition" = None, State13: "tfsm_Transition" = None, State: "tfsm_TFSM" = None, tfsm_State: "tfsm_TFSM" = None):
        self.ownedState = ownedState
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.State11 = State11
        self.State13 = State13
        self.State = State
        self.tfsm_State = tfsm_State
        
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
    def ownedState(self):
        return self.__ownedState

    @ownedState.setter
    def ownedState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__ownedState", None)
        self.__ownedState = value
        
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
    def State13(self):
        return self.__State13

    @State13.setter
    def State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__State13", None)
        self.__State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingTransition"):
                opp_val = getattr(old_value, "incomingTransition", None)
                if opp_val == self:
                    setattr(old_value, "incomingTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingTransition"):
                opp_val = getattr(value, "incomingTransition", None)
                setattr(value, "incomingTransition", self)

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
                if hasattr(item, "Transition9"):
                    opp_val = getattr(item, "Transition9", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition9"):
                    opp_val = getattr(item, "Transition9", None)
                    
                    setattr(item, "Transition9", self)
                    

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
    def State11(self):
        return self.__State11

    @State11.setter
    def State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tfsm_State__State11", None)
        self.__State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingTransition"):
                opp_val = getattr(old_value, "outgoingTransition", None)
                if opp_val == self:
                    setattr(old_value, "outgoingTransition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingTransition"):
                opp_val = getattr(value, "outgoingTransition", None)
                setattr(value, "outgoingTransition", self)

    def onLeave(self) -> str:
        # TODO: Implement onLeave method
        pass

    def onEnter(self) -> str:
        # TODO: Implement onEnter method
        pass

class tfsm_FSMEvent(NamedElement):

    pass
class tfsm_TFSM(NamedElement):

    pass