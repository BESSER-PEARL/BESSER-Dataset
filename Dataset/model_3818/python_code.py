from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EventAutomatonModel_EventGuard:

    pass
class EventAutomatonModel_Event:

    pass
class EventAutomatonModel_Action(ABC):

    pass
class AbstractTransition:

    pass
class EventAutomatonModel_EpsilonTransition(AbstractTransition):

    pass
class EventAutomatonModel_Transition(AbstractTransition):

    pass
class Parameter:

    pass
class EventAutomatonModel_FreeParameter(Parameter):

    def __init__(self, excludedValues: str):
        self.excludedValues = excludedValues
        
    @property
    def excludedValues(self) -> str:
        return self.__excludedValues

    @excludedValues.setter
    def excludedValues(self, excludedValues: str):
        self.__excludedValues = excludedValues

class EventAutomatonModel_FixParameter(Parameter):

    def __init__(self, value: str, EventAutomatonModel_FixParameter: "EventAutomatonModel_ConstantBinding" = None, EventAutomatonModel_FixParameter36: "EventAutomatonModel_Event" = None):
        self.value = value
        self.EventAutomatonModel_FixParameter = EventAutomatonModel_FixParameter
        self.EventAutomatonModel_FixParameter36 = EventAutomatonModel_FixParameter36
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def EventAutomatonModel_FixParameter36(self):
        return self.__EventAutomatonModel_FixParameter36

    @EventAutomatonModel_FixParameter36.setter
    def EventAutomatonModel_FixParameter36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_FixParameter__EventAutomatonModel_FixParameter36", None)
        self.__EventAutomatonModel_FixParameter36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_Event35"):
                opp_val = getattr(old_value, "EventAutomatonModel_Event35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_Event35"):
                opp_val = getattr(value, "EventAutomatonModel_Event35", None)
                if opp_val is None:
                    setattr(value, "EventAutomatonModel_Event35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EventAutomatonModel_FixParameter(self):
        return self.__EventAutomatonModel_FixParameter

    @EventAutomatonModel_FixParameter.setter
    def EventAutomatonModel_FixParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_FixParameter__EventAutomatonModel_FixParameter", None)
        self.__EventAutomatonModel_FixParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_ConstantBinding"):
                opp_val = getattr(old_value, "EventAutomatonModel_ConstantBinding", None)
                if opp_val == self:
                    setattr(old_value, "EventAutomatonModel_ConstantBinding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_ConstantBinding"):
                opp_val = getattr(value, "EventAutomatonModel_ConstantBinding", None)
                setattr(value, "EventAutomatonModel_ConstantBinding", self)

class Action:

    pass
class EventAutomatonModel_TimerAction(Action):

    pass
class EventAutomatonModel_Binding(ABC):

    pass
class EventAutomatonModel_Parameter(ABC):

    pass
class EventAutomatonModel_SymbolicEvent(ABC):

    pass
class EventAutomatonModel_AbstractTransition:

    pass
class SymbolicEvent:

    pass
class EventAutomatonModel_SymbolicTimeoutEvent(SymbolicEvent):

    pass
class EventAutomatonModel_SymbolicInputEvent(SymbolicEvent):

    def __init__(self, name: str, EventAutomatonModel_SymbolicInputEvent: "EventAutomatonModel_ComplexEventProcessor" = None):
        self.name = name
        self.EventAutomatonModel_SymbolicInputEvent = EventAutomatonModel_SymbolicInputEvent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EventAutomatonModel_SymbolicInputEvent(self):
        return self.__EventAutomatonModel_SymbolicInputEvent

    @EventAutomatonModel_SymbolicInputEvent.setter
    def EventAutomatonModel_SymbolicInputEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_SymbolicInputEvent__EventAutomatonModel_SymbolicInputEvent", None)
        self.__EventAutomatonModel_SymbolicInputEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_ComplexEventProcessor18"):
                opp_val = getattr(old_value, "EventAutomatonModel_ComplexEventProcessor18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_ComplexEventProcessor18"):
                opp_val = getattr(value, "EventAutomatonModel_ComplexEventProcessor18", None)
                if opp_val is None:
                    setattr(value, "EventAutomatonModel_ComplexEventProcessor18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TimerAction:

    pass
class EventAutomatonModel_SetTimerAction(TimerAction):

    def __init__(self, toValue: int):
        self.toValue = toValue
        
    @property
    def toValue(self) -> int:
        return self.__toValue

    @toValue.setter
    def toValue(self, toValue: int):
        self.__toValue = toValue

class EventAutomatonModel_ResetTimerAction(TimerAction):

    pass
class Binding:

    pass
class EventAutomatonModel_ConstantBinding(Binding):

    pass
class EventAutomatonModel_TokenParameterBinding(Binding):

    pass
class EventAutomatonModel_ComplexEventProcessor:

    pass
class SymbolicParameter:

    pass
class EventAutomatonModel_SymbolicTokenParameter(SymbolicParameter):

    pass
class EventAutomatonModel_SymbolicEventParameter(SymbolicParameter):

    pass
class EventAutomatonModel_Token:

    pass
class EventAutomatonModel_State:

    def __init__(self, acceptor: str, id: int, EventAutomatonModel_State5: "EventAutomatonModel_Automaton" = None, EventAutomatonModel_State12: "EventAutomatonModel_Automaton" = None, EventAutomatonModel_State: "EventAutomatonModel_Automaton" = None, to: set["EventAutomatonModel_AbstractTransition"] = None, from: set["EventAutomatonModel_AbstractTransition"] = None, on: set["EventAutomatonModel_Token"] = None, State: "EventAutomatonModel_Token" = None, State49: "EventAutomatonModel_AbstractTransition" = None, State51: "EventAutomatonModel_AbstractTransition" = None):
        self.acceptor = acceptor
        self.id = id
        self.EventAutomatonModel_State5 = EventAutomatonModel_State5
        self.EventAutomatonModel_State12 = EventAutomatonModel_State12
        self.EventAutomatonModel_State = EventAutomatonModel_State
        self.to = to if to is not None else set()
        self.from = from if from is not None else set()
        self.on = on if on is not None else set()
        self.State = State
        self.State49 = State49
        self.State51 = State51
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def acceptor(self) -> str:
        return self.__acceptor

    @acceptor.setter
    def acceptor(self, acceptor: str):
        self.__acceptor = acceptor

    @property
    def EventAutomatonModel_State12(self):
        return self.__EventAutomatonModel_State12

    @EventAutomatonModel_State12.setter
    def EventAutomatonModel_State12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_State__EventAutomatonModel_State12", None)
        self.__EventAutomatonModel_State12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_Automaton11"):
                opp_val = getattr(old_value, "EventAutomatonModel_Automaton11", None)
                if opp_val == self:
                    setattr(old_value, "EventAutomatonModel_Automaton11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_Automaton11"):
                opp_val = getattr(value, "EventAutomatonModel_Automaton11", None)
                setattr(value, "EventAutomatonModel_Automaton11", self)

    @property
    def EventAutomatonModel_State(self):
        return self.__EventAutomatonModel_State

    @EventAutomatonModel_State.setter
    def EventAutomatonModel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_State__EventAutomatonModel_State", None)
        self.__EventAutomatonModel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_Automaton"):
                opp_val = getattr(old_value, "EventAutomatonModel_Automaton", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_Automaton"):
                opp_val = getattr(value, "EventAutomatonModel_Automaton", None)
                if opp_val is None:
                    setattr(value, "EventAutomatonModel_Automaton", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EventAutomatonModel_State5(self):
        return self.__EventAutomatonModel_State5

    @EventAutomatonModel_State5.setter
    def EventAutomatonModel_State5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_State__EventAutomatonModel_State5", None)
        self.__EventAutomatonModel_State5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_Automaton4"):
                opp_val = getattr(old_value, "EventAutomatonModel_Automaton4", None)
                if opp_val == self:
                    setattr(old_value, "EventAutomatonModel_Automaton4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_Automaton4"):
                opp_val = getattr(value, "EventAutomatonModel_Automaton4", None)
                setattr(value, "EventAutomatonModel_Automaton4", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tokens"):
                opp_val = getattr(old_value, "tokens", None)
                if opp_val == self:
                    setattr(old_value, "tokens", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tokens"):
                opp_val = getattr(value, "tokens", None)
                setattr(value, "tokens", self)

    @property
    def State49(self):
        return self.__State49

    @State49.setter
    def State49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_State__State49", None)
        self.__State49 = value
        
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
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_State__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractTransition"):
                    opp_val = getattr(item, "AbstractTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractTransition"):
                    opp_val = getattr(item, "AbstractTransition", None)
                    
                    setattr(item, "AbstractTransition", self)
                    

    @property
    def State51(self):
        return self.__State51

    @State51.setter
    def State51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_State__State51", None)
        self.__State51 = value
        
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
    def on(self):
        return self.__on

    @on.setter
    def on(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_State__on", None)
        self.__on = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Token"):
                    opp_val = getattr(item, "Token", None)
                    
                    if opp_val == self:
                        setattr(item, "Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Token"):
                    opp_val = getattr(item, "Token", None)
                    
                    setattr(item, "Token", self)
                    

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_State__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractTransition26"):
                    opp_val = getattr(item, "AbstractTransition26", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractTransition26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractTransition26"):
                    opp_val = getattr(item, "AbstractTransition26", None)
                    
                    setattr(item, "AbstractTransition26", self)
                    

class EventAutomatonModel_Automaton:

    def __init__(self, name: str, EventAutomatonModel_Automaton4: "EventAutomatonModel_State" = None, EventAutomatonModel_Automaton7: set["EventAutomatonModel_SymbolicParameter"] = None, EventAutomatonModel_Automaton9: set["EventAutomatonModel_SymbolicTimer"] = None, EventAutomatonModel_Automaton11: "EventAutomatonModel_State" = None, EventAutomatonModel_Automaton: set["EventAutomatonModel_State"] = None, EventAutomatonModel_Automaton2: set["EventAutomatonModel_Token"] = None, EventAutomatonModel_Automaton16: "EventAutomatonModel_ComplexEventProcessor" = None):
        self.name = name
        self.EventAutomatonModel_Automaton4 = EventAutomatonModel_Automaton4
        self.EventAutomatonModel_Automaton7 = EventAutomatonModel_Automaton7 if EventAutomatonModel_Automaton7 is not None else set()
        self.EventAutomatonModel_Automaton9 = EventAutomatonModel_Automaton9 if EventAutomatonModel_Automaton9 is not None else set()
        self.EventAutomatonModel_Automaton11 = EventAutomatonModel_Automaton11
        self.EventAutomatonModel_Automaton = EventAutomatonModel_Automaton if EventAutomatonModel_Automaton is not None else set()
        self.EventAutomatonModel_Automaton2 = EventAutomatonModel_Automaton2 if EventAutomatonModel_Automaton2 is not None else set()
        self.EventAutomatonModel_Automaton16 = EventAutomatonModel_Automaton16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EventAutomatonModel_Automaton9(self):
        return self.__EventAutomatonModel_Automaton9

    @EventAutomatonModel_Automaton9.setter
    def EventAutomatonModel_Automaton9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_Automaton__EventAutomatonModel_Automaton9", None)
        self.__EventAutomatonModel_Automaton9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EventAutomatonModel_SymbolicTimer"):
                    opp_val = getattr(item, "EventAutomatonModel_SymbolicTimer", None)
                    
                    if opp_val == self:
                        setattr(item, "EventAutomatonModel_SymbolicTimer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EventAutomatonModel_SymbolicTimer"):
                    opp_val = getattr(item, "EventAutomatonModel_SymbolicTimer", None)
                    
                    setattr(item, "EventAutomatonModel_SymbolicTimer", self)
                    

    @property
    def EventAutomatonModel_Automaton4(self):
        return self.__EventAutomatonModel_Automaton4

    @EventAutomatonModel_Automaton4.setter
    def EventAutomatonModel_Automaton4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_Automaton__EventAutomatonModel_Automaton4", None)
        self.__EventAutomatonModel_Automaton4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_State5"):
                opp_val = getattr(old_value, "EventAutomatonModel_State5", None)
                if opp_val == self:
                    setattr(old_value, "EventAutomatonModel_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_State5"):
                opp_val = getattr(value, "EventAutomatonModel_State5", None)
                setattr(value, "EventAutomatonModel_State5", self)

    @property
    def EventAutomatonModel_Automaton(self):
        return self.__EventAutomatonModel_Automaton

    @EventAutomatonModel_Automaton.setter
    def EventAutomatonModel_Automaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_Automaton__EventAutomatonModel_Automaton", None)
        self.__EventAutomatonModel_Automaton = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EventAutomatonModel_State"):
                    opp_val = getattr(item, "EventAutomatonModel_State", None)
                    
                    if opp_val == self:
                        setattr(item, "EventAutomatonModel_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EventAutomatonModel_State"):
                    opp_val = getattr(item, "EventAutomatonModel_State", None)
                    
                    setattr(item, "EventAutomatonModel_State", self)
                    

    @property
    def EventAutomatonModel_Automaton11(self):
        return self.__EventAutomatonModel_Automaton11

    @EventAutomatonModel_Automaton11.setter
    def EventAutomatonModel_Automaton11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_Automaton__EventAutomatonModel_Automaton11", None)
        self.__EventAutomatonModel_Automaton11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_State12"):
                opp_val = getattr(old_value, "EventAutomatonModel_State12", None)
                if opp_val == self:
                    setattr(old_value, "EventAutomatonModel_State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_State12"):
                opp_val = getattr(value, "EventAutomatonModel_State12", None)
                setattr(value, "EventAutomatonModel_State12", self)

    @property
    def EventAutomatonModel_Automaton2(self):
        return self.__EventAutomatonModel_Automaton2

    @EventAutomatonModel_Automaton2.setter
    def EventAutomatonModel_Automaton2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_Automaton__EventAutomatonModel_Automaton2", None)
        self.__EventAutomatonModel_Automaton2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EventAutomatonModel_Token"):
                    opp_val = getattr(item, "EventAutomatonModel_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "EventAutomatonModel_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EventAutomatonModel_Token"):
                    opp_val = getattr(item, "EventAutomatonModel_Token", None)
                    
                    setattr(item, "EventAutomatonModel_Token", self)
                    

    @property
    def EventAutomatonModel_Automaton7(self):
        return self.__EventAutomatonModel_Automaton7

    @EventAutomatonModel_Automaton7.setter
    def EventAutomatonModel_Automaton7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_Automaton__EventAutomatonModel_Automaton7", None)
        self.__EventAutomatonModel_Automaton7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EventAutomatonModel_SymbolicParameter"):
                    opp_val = getattr(item, "EventAutomatonModel_SymbolicParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "EventAutomatonModel_SymbolicParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EventAutomatonModel_SymbolicParameter"):
                    opp_val = getattr(item, "EventAutomatonModel_SymbolicParameter", None)
                    
                    setattr(item, "EventAutomatonModel_SymbolicParameter", self)
                    

    @property
    def EventAutomatonModel_Automaton16(self):
        return self.__EventAutomatonModel_Automaton16

    @EventAutomatonModel_Automaton16.setter
    def EventAutomatonModel_Automaton16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_Automaton__EventAutomatonModel_Automaton16", None)
        self.__EventAutomatonModel_Automaton16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_ComplexEventProcessor"):
                opp_val = getattr(old_value, "EventAutomatonModel_ComplexEventProcessor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_ComplexEventProcessor"):
                opp_val = getattr(value, "EventAutomatonModel_ComplexEventProcessor", None)
                if opp_val is None:
                    setattr(value, "EventAutomatonModel_ComplexEventProcessor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EventAutomatonModel_SymbolicTimer:

    def __init__(self, name: str, EventAutomatonModel_SymbolicTimer: "EventAutomatonModel_Automaton" = None, timer: "EventAutomatonModel_SymbolicTimeoutEvent" = None, SymbolicTimer: "EventAutomatonModel_SymbolicTimeoutEvent" = None, EventAutomatonModel_SymbolicTimer31: "EventAutomatonModel_TimerAction" = None):
        self.name = name
        self.EventAutomatonModel_SymbolicTimer = EventAutomatonModel_SymbolicTimer
        self.timer = timer
        self.SymbolicTimer = SymbolicTimer
        self.EventAutomatonModel_SymbolicTimer31 = EventAutomatonModel_SymbolicTimer31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SymbolicTimer(self):
        return self.__SymbolicTimer

    @SymbolicTimer.setter
    def SymbolicTimer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_SymbolicTimer__SymbolicTimer", None)
        self.__SymbolicTimer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "timeoutEvent"):
                opp_val = getattr(old_value, "timeoutEvent", None)
                if opp_val == self:
                    setattr(old_value, "timeoutEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "timeoutEvent"):
                opp_val = getattr(value, "timeoutEvent", None)
                setattr(value, "timeoutEvent", self)

    @property
    def EventAutomatonModel_SymbolicTimer31(self):
        return self.__EventAutomatonModel_SymbolicTimer31

    @EventAutomatonModel_SymbolicTimer31.setter
    def EventAutomatonModel_SymbolicTimer31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_SymbolicTimer__EventAutomatonModel_SymbolicTimer31", None)
        self.__EventAutomatonModel_SymbolicTimer31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_TimerAction"):
                opp_val = getattr(old_value, "EventAutomatonModel_TimerAction", None)
                if opp_val == self:
                    setattr(old_value, "EventAutomatonModel_TimerAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_TimerAction"):
                opp_val = getattr(value, "EventAutomatonModel_TimerAction", None)
                setattr(value, "EventAutomatonModel_TimerAction", self)

    @property
    def timer(self):
        return self.__timer

    @timer.setter
    def timer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_SymbolicTimer__timer", None)
        self.__timer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SymbolicTimeoutEvent"):
                opp_val = getattr(old_value, "SymbolicTimeoutEvent", None)
                if opp_val == self:
                    setattr(old_value, "SymbolicTimeoutEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SymbolicTimeoutEvent"):
                opp_val = getattr(value, "SymbolicTimeoutEvent", None)
                setattr(value, "SymbolicTimeoutEvent", self)

    @property
    def EventAutomatonModel_SymbolicTimer(self):
        return self.__EventAutomatonModel_SymbolicTimer

    @EventAutomatonModel_SymbolicTimer.setter
    def EventAutomatonModel_SymbolicTimer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_SymbolicTimer__EventAutomatonModel_SymbolicTimer", None)
        self.__EventAutomatonModel_SymbolicTimer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_Automaton9"):
                opp_val = getattr(old_value, "EventAutomatonModel_Automaton9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_Automaton9"):
                opp_val = getattr(value, "EventAutomatonModel_Automaton9", None)
                if opp_val is None:
                    setattr(value, "EventAutomatonModel_Automaton9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EventAutomatonModel_SymbolicParameter(ABC):

    def __init__(self, name: str, EventAutomatonModel_SymbolicParameter: "EventAutomatonModel_Automaton" = None, EventAutomatonModel_SymbolicParameter20: "EventAutomatonModel_SymbolicEvent" = None, EventAutomatonModel_SymbolicParameter22: "EventAutomatonModel_Parameter" = None):
        self.name = name
        self.EventAutomatonModel_SymbolicParameter = EventAutomatonModel_SymbolicParameter
        self.EventAutomatonModel_SymbolicParameter20 = EventAutomatonModel_SymbolicParameter20
        self.EventAutomatonModel_SymbolicParameter22 = EventAutomatonModel_SymbolicParameter22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EventAutomatonModel_SymbolicParameter20(self):
        return self.__EventAutomatonModel_SymbolicParameter20

    @EventAutomatonModel_SymbolicParameter20.setter
    def EventAutomatonModel_SymbolicParameter20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_SymbolicParameter__EventAutomatonModel_SymbolicParameter20", None)
        self.__EventAutomatonModel_SymbolicParameter20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_SymbolicEvent"):
                opp_val = getattr(old_value, "EventAutomatonModel_SymbolicEvent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_SymbolicEvent"):
                opp_val = getattr(value, "EventAutomatonModel_SymbolicEvent", None)
                if opp_val is None:
                    setattr(value, "EventAutomatonModel_SymbolicEvent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EventAutomatonModel_SymbolicParameter22(self):
        return self.__EventAutomatonModel_SymbolicParameter22

    @EventAutomatonModel_SymbolicParameter22.setter
    def EventAutomatonModel_SymbolicParameter22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_SymbolicParameter__EventAutomatonModel_SymbolicParameter22", None)
        self.__EventAutomatonModel_SymbolicParameter22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_Parameter"):
                opp_val = getattr(old_value, "EventAutomatonModel_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "EventAutomatonModel_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_Parameter"):
                opp_val = getattr(value, "EventAutomatonModel_Parameter", None)
                setattr(value, "EventAutomatonModel_Parameter", self)

    @property
    def EventAutomatonModel_SymbolicParameter(self):
        return self.__EventAutomatonModel_SymbolicParameter

    @EventAutomatonModel_SymbolicParameter.setter
    def EventAutomatonModel_SymbolicParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EventAutomatonModel_SymbolicParameter__EventAutomatonModel_SymbolicParameter", None)
        self.__EventAutomatonModel_SymbolicParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventAutomatonModel_Automaton7"):
                opp_val = getattr(old_value, "EventAutomatonModel_Automaton7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventAutomatonModel_Automaton7"):
                opp_val = getattr(value, "EventAutomatonModel_Automaton7", None)
                if opp_val is None:
                    setattr(value, "EventAutomatonModel_Automaton7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
