from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ComplexEventOperator:

    pass
class events_AND(ComplexEventOperator):

    pass
class events_NEG(ComplexEventOperator):

    pass
class events_FOLLOWS(ComplexEventOperator):

    pass
class events_OR(ComplexEventOperator):

    pass
class events_EventSource(ABC):

    def __init__(self, events_EventSource: "events_Event" = None):
        self.events_EventSource = events_EventSource
        
    @property
    def events_EventSource(self):
        return self.__events_EventSource

    @events_EventSource.setter
    def events_EventSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_EventSource__events_EventSource", None)
        self.__events_EventSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events_Event"):
                opp_val = getattr(old_value, "events_Event", None)
                if opp_val == self:
                    setattr(old_value, "events_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events_Event"):
                opp_val = getattr(value, "events_Event", None)
                setattr(value, "events_Event", self)

    def getId(self) -> str:
        # TODO: Implement getId method
        pass

class events_Event:

    def __init__(self, type: str, timestamp: str, isProcessed: bool, events_Event: "events_EventSource" = None):
        self.type = type
        self.timestamp = timestamp
        self.isProcessed = isProcessed
        self.events_Event = events_Event
        
    @property
    def isProcessed(self) -> bool:
        return self.__isProcessed

    @isProcessed.setter
    def isProcessed(self, isProcessed: bool):
        self.__isProcessed = isProcessed

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def events_Event(self):
        return self.__events_Event

    @events_Event.setter
    def events_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_Event__events_Event", None)
        self.__events_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events_EventSource"):
                opp_val = getattr(old_value, "events_EventSource", None)
                if opp_val == self:
                    setattr(old_value, "events_EventSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events_EventSource"):
                opp_val = getattr(value, "events_EventSource", None)
                setattr(value, "events_EventSource", self)

class events_AbstractMultiplicity(ABC):

    pass
class AbstractMultiplicity:

    pass
class events_Infinite(AbstractMultiplicity):

    pass
class events_AtLeastOne(AbstractMultiplicity):

    pass
class events_Multiplicity(AbstractMultiplicity):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class events_Timewindow:

    def __init__(self, time: str, events_Timewindow: "events_ComplexEventPattern" = None):
        self.time = time
        self.events_Timewindow = events_Timewindow
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def events_Timewindow(self):
        return self.__events_Timewindow

    @events_Timewindow.setter
    def events_Timewindow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_Timewindow__events_Timewindow", None)
        self.__events_Timewindow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events_ComplexEventPattern5"):
                opp_val = getattr(old_value, "events_ComplexEventPattern5", None)
                if opp_val == self:
                    setattr(old_value, "events_ComplexEventPattern5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events_ComplexEventPattern5"):
                opp_val = getattr(value, "events_ComplexEventPattern5", None)
                setattr(value, "events_ComplexEventPattern5", self)

class events_ComplexEventOperator(ABC):

    pass
class EventPattern:

    pass
class events_ComplexEventPattern(EventPattern):

    def __init__(self, eventContext: str, events_ComplexEventPattern7: set["events_EventPatternReference"] = None, events_ComplexEventPattern: "events_ComplexEventOperator" = None, events_ComplexEventPattern5: "events_Timewindow" = None):
        self.eventContext = eventContext
        self.events_ComplexEventPattern7 = events_ComplexEventPattern7 if events_ComplexEventPattern7 is not None else set()
        self.events_ComplexEventPattern = events_ComplexEventPattern
        self.events_ComplexEventPattern5 = events_ComplexEventPattern5
        
    @property
    def eventContext(self) -> str:
        return self.__eventContext

    @eventContext.setter
    def eventContext(self, eventContext: str):
        self.__eventContext = eventContext

    @property
    def events_ComplexEventPattern5(self):
        return self.__events_ComplexEventPattern5

    @events_ComplexEventPattern5.setter
    def events_ComplexEventPattern5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_ComplexEventPattern__events_ComplexEventPattern5", None)
        self.__events_ComplexEventPattern5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events_Timewindow"):
                opp_val = getattr(old_value, "events_Timewindow", None)
                if opp_val == self:
                    setattr(old_value, "events_Timewindow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events_Timewindow"):
                opp_val = getattr(value, "events_Timewindow", None)
                setattr(value, "events_Timewindow", self)

    @property
    def events_ComplexEventPattern7(self):
        return self.__events_ComplexEventPattern7

    @events_ComplexEventPattern7.setter
    def events_ComplexEventPattern7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_ComplexEventPattern__events_ComplexEventPattern7", None)
        self.__events_ComplexEventPattern7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events_EventPatternReference"):
                    opp_val = getattr(item, "events_EventPatternReference", None)
                    
                    if opp_val == self:
                        setattr(item, "events_EventPatternReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events_EventPatternReference"):
                    opp_val = getattr(item, "events_EventPatternReference", None)
                    
                    setattr(item, "events_EventPatternReference", self)
                    

    @property
    def events_ComplexEventPattern(self):
        return self.__events_ComplexEventPattern

    @events_ComplexEventPattern.setter
    def events_ComplexEventPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_ComplexEventPattern__events_ComplexEventPattern", None)
        self.__events_ComplexEventPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events_ComplexEventOperator"):
                opp_val = getattr(old_value, "events_ComplexEventOperator", None)
                if opp_val == self:
                    setattr(old_value, "events_ComplexEventOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events_ComplexEventOperator"):
                opp_val = getattr(value, "events_ComplexEventOperator", None)
                setattr(value, "events_ComplexEventOperator", self)

class events_AtomicEventPattern(EventPattern):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class events_Automaton:

    pass
class events_EventPattern(ABC):

    def __init__(self, id: str, EventPattern: "events_EventModel" = None, eventPatterns: "events_EventModel" = None, events_EventPattern: "events_Automaton" = None, events_EventPattern10: "events_EventPatternReference" = None):
        self.id = id
        self.EventPattern = EventPattern
        self.eventPatterns = eventPatterns
        self.events_EventPattern = events_EventPattern
        self.events_EventPattern10 = events_EventPattern10
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def events_EventPattern10(self):
        return self.__events_EventPattern10

    @events_EventPattern10.setter
    def events_EventPattern10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_EventPattern__events_EventPattern10", None)
        self.__events_EventPattern10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events_EventPatternReference9"):
                opp_val = getattr(old_value, "events_EventPatternReference9", None)
                if opp_val == self:
                    setattr(old_value, "events_EventPatternReference9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events_EventPatternReference9"):
                opp_val = getattr(value, "events_EventPatternReference9", None)
                setattr(value, "events_EventPatternReference9", self)

    @property
    def eventPatterns(self):
        return self.__eventPatterns

    @eventPatterns.setter
    def eventPatterns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_EventPattern__eventPatterns", None)
        self.__eventPatterns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EventModel"):
                opp_val = getattr(old_value, "EventModel", None)
                if opp_val == self:
                    setattr(old_value, "EventModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EventModel"):
                opp_val = getattr(value, "EventModel", None)
                setattr(value, "EventModel", self)

    @property
    def EventPattern(self):
        return self.__EventPattern

    @EventPattern.setter
    def EventPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_EventPattern__EventPattern", None)
        self.__EventPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventModel"):
                opp_val = getattr(old_value, "eventModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventModel"):
                opp_val = getattr(value, "eventModel", None)
                if opp_val is None:
                    setattr(value, "eventModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def events_EventPattern(self):
        return self.__events_EventPattern

    @events_EventPattern.setter
    def events_EventPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_EventPattern__events_EventPattern", None)
        self.__events_EventPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events_Automaton"):
                opp_val = getattr(old_value, "events_Automaton", None)
                if opp_val == self:
                    setattr(old_value, "events_Automaton", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events_Automaton"):
                opp_val = getattr(value, "events_Automaton", None)
                setattr(value, "events_Automaton", self)

class events_EventModel:

    pass
class events_EventPatternReference:

    def __init__(self, parameterSymbolicNames: str, events_EventPatternReference: "events_ComplexEventPattern" = None, events_EventPatternReference9: "events_EventPattern" = None, events_EventPatternReference12: "events_AbstractMultiplicity" = None):
        self.parameterSymbolicNames = parameterSymbolicNames
        self.events_EventPatternReference = events_EventPatternReference
        self.events_EventPatternReference9 = events_EventPatternReference9
        self.events_EventPatternReference12 = events_EventPatternReference12
        
    @property
    def parameterSymbolicNames(self) -> str:
        return self.__parameterSymbolicNames

    @parameterSymbolicNames.setter
    def parameterSymbolicNames(self, parameterSymbolicNames: str):
        self.__parameterSymbolicNames = parameterSymbolicNames

    @property
    def events_EventPatternReference12(self):
        return self.__events_EventPatternReference12

    @events_EventPatternReference12.setter
    def events_EventPatternReference12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_EventPatternReference__events_EventPatternReference12", None)
        self.__events_EventPatternReference12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events_AbstractMultiplicity"):
                opp_val = getattr(old_value, "events_AbstractMultiplicity", None)
                if opp_val == self:
                    setattr(old_value, "events_AbstractMultiplicity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events_AbstractMultiplicity"):
                opp_val = getattr(value, "events_AbstractMultiplicity", None)
                setattr(value, "events_AbstractMultiplicity", self)

    @property
    def events_EventPatternReference9(self):
        return self.__events_EventPatternReference9

    @events_EventPatternReference9.setter
    def events_EventPatternReference9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_EventPatternReference__events_EventPatternReference9", None)
        self.__events_EventPatternReference9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events_EventPattern10"):
                opp_val = getattr(old_value, "events_EventPattern10", None)
                if opp_val == self:
                    setattr(old_value, "events_EventPattern10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events_EventPattern10"):
                opp_val = getattr(value, "events_EventPattern10", None)
                setattr(value, "events_EventPattern10", self)

    @property
    def events_EventPatternReference(self):
        return self.__events_EventPatternReference

    @events_EventPatternReference.setter
    def events_EventPatternReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_events_EventPatternReference__events_EventPatternReference", None)
        self.__events_EventPatternReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events_ComplexEventPattern7"):
                opp_val = getattr(old_value, "events_ComplexEventPattern7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events_ComplexEventPattern7"):
                opp_val = getattr(value, "events_ComplexEventPattern7", None)
                if opp_val is None:
                    setattr(value, "events_ComplexEventPattern7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
