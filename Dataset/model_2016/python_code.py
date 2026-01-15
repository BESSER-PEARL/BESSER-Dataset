from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SchedulingEventKind(Enum):
    ACTIVATED = "ACTIVATED"
    RUNNING = "RUNNING"
    SUSPENDED = "SUSPENDED"
    BLOCKED = "BLOCKED"
    TERMINATED = "TERMINATED"
    DEADLINE = "DEADLINE"
class SliceKind(Enum):
    OTHER = "OTHER"
    TASK = "TASK"
    JOB = "JOB"
    FUNCTION = "FUNCTION"
    FUNCTION_INSTANCE = "FUNCTION_INSTANCE"
    PACKET = "PACKET"
    FRAME = "FRAME"
    LINK = "LINK"
    RESOURCE = "RESOURCE"
    STATE = "STATE"
    AUTOMATON = "AUTOMATON"
    TEMPORAL_CHAIN = "TEMPORAL_CHAIN"
    OS = "OS"
class ResourceEventKind(Enum):
    ACQUIRED = "ACQUIRED"
    RELEASED = "RELEASED"
    REQUESTED = "REQUESTED"
class MessageEventKind(Enum):
    INSTANTIATED = "INSTANTIATED"
    TRANSMITTED = "TRANSMITTED"
    RECEIVED = "RECEIVED"
    ERROR = "ERROR"


############################################
# Definition of Classes
############################################

class ValueChangeEvent:

    pass
class trace_ObjectValueChangeEvent(ValueChangeEvent):

    pass
class trace_EObject:

    pass
class trace_EStructuralFeature:

    pass
class trace_NumberValueChangeEvent(ValueChangeEvent):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class trace_DataSizeValueChangeEvent(ValueChangeEvent):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class trace_DurationValueChangeEvent(ValueChangeEvent):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class EModelElement:

    pass
class trace_Properties(EModelElement):

    def __init__(self, range: str, blockingTime: str, executionTime: str, remainingTime: str, responseTime: str, absoluteDeadline: str, index: str, trace_Properties: "trace_Slice" = None):
        self.range = range
        self.blockingTime = blockingTime
        self.executionTime = executionTime
        self.remainingTime = remainingTime
        self.responseTime = responseTime
        self.absoluteDeadline = absoluteDeadline
        self.index = index
        self.trace_Properties = trace_Properties
        
    @property
    def remainingTime(self) -> str:
        return self.__remainingTime

    @remainingTime.setter
    def remainingTime(self, remainingTime: str):
        self.__remainingTime = remainingTime

    @property
    def executionTime(self) -> str:
        return self.__executionTime

    @executionTime.setter
    def executionTime(self, executionTime: str):
        self.__executionTime = executionTime

    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def responseTime(self) -> str:
        return self.__responseTime

    @responseTime.setter
    def responseTime(self, responseTime: str):
        self.__responseTime = responseTime

    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def absoluteDeadline(self) -> str:
        return self.__absoluteDeadline

    @absoluteDeadline.setter
    def absoluteDeadline(self, absoluteDeadline: str):
        self.__absoluteDeadline = absoluteDeadline

    @property
    def blockingTime(self) -> str:
        return self.__blockingTime

    @blockingTime.setter
    def blockingTime(self, blockingTime: str):
        self.__blockingTime = blockingTime

    @property
    def trace_Properties(self):
        return self.__trace_Properties

    @trace_Properties.setter
    def trace_Properties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Properties__trace_Properties", None)
        self.__trace_Properties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Slice14"):
                opp_val = getattr(old_value, "trace_Slice14", None)
                if opp_val == self:
                    setattr(old_value, "trace_Slice14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Slice14"):
                opp_val = getattr(value, "trace_Slice14", None)
                setattr(value, "trace_Slice14", self)

class trace_Event(EModelElement):

    def __init__(self, timestamp: str, events: "trace_Trace" = None, trace_Event: set["trace_Slice"] = None, Event: "trace_Trace" = None, trace_Event7: "trace_Slice" = None):
        self.timestamp = timestamp
        self.events = events
        self.trace_Event = trace_Event if trace_Event is not None else set()
        self.Event = Event
        self.trace_Event7 = trace_Event7
        
    @property
    def timestamp(self) -> str:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        self.__timestamp = timestamp

    @property
    def trace_Event7(self):
        return self.__trace_Event7

    @trace_Event7.setter
    def trace_Event7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Event__trace_Event7", None)
        self.__trace_Event7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Slice6"):
                opp_val = getattr(old_value, "trace_Slice6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Slice6"):
                opp_val = getattr(value, "trace_Slice6", None)
                if opp_val is None:
                    setattr(value, "trace_Slice6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Event__Event", None)
        self.__Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace"):
                opp_val = getattr(old_value, "trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace"):
                opp_val = getattr(value, "trace", None)
                if opp_val is None:
                    setattr(value, "trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Event__events", None)
        self.__events = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trace"):
                opp_val = getattr(old_value, "Trace", None)
                if opp_val == self:
                    setattr(old_value, "Trace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trace"):
                opp_val = getattr(value, "Trace", None)
                setattr(value, "Trace", self)

    @property
    def trace_Event(self):
        return self.__trace_Event

    @trace_Event.setter
    def trace_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Event__trace_Event", None)
        self.__trace_Event = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_Slice4"):
                    opp_val = getattr(item, "trace_Slice4", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_Slice4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_Slice4"):
                    opp_val = getattr(item, "trace_Slice4", None)
                    
                    setattr(item, "trace_Slice4", self)
                    

class trace_Slice(EModelElement):

    def __init__(self, name: str, kind: str, kindLabel: str, trace_Slice4: "trace_Event" = None, trace_Slice: "trace_Trace" = None, Slice: "trace_Slice" = None, parent: set["trace_Slice"] = None, Slice12: "trace_Slice" = None, ownedSubSlices: "trace_Slice" = None, trace_Slice14: "trace_Properties" = None, trace_Slice17: "trace_Slice" = None, trace_Slice15: set["trace_Slice"] = None, trace_Slice6: set["trace_Event"] = None):
        self.name = name
        self.kind = kind
        self.kindLabel = kindLabel
        self.trace_Slice4 = trace_Slice4
        self.trace_Slice = trace_Slice
        self.Slice = Slice
        self.parent = parent if parent is not None else set()
        self.Slice12 = Slice12
        self.ownedSubSlices = ownedSubSlices
        self.trace_Slice14 = trace_Slice14
        self.trace_Slice17 = trace_Slice17
        self.trace_Slice15 = trace_Slice15 if trace_Slice15 is not None else set()
        self.trace_Slice6 = trace_Slice6 if trace_Slice6 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kindLabel(self) -> str:
        return self.__kindLabel

    @kindLabel.setter
    def kindLabel(self, kindLabel: str):
        self.__kindLabel = kindLabel

    @property
    def ownedSubSlices(self):
        return self.__ownedSubSlices

    @ownedSubSlices.setter
    def ownedSubSlices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Slice__ownedSubSlices", None)
        self.__ownedSubSlices = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Slice12"):
                opp_val = getattr(old_value, "Slice12", None)
                if opp_val == self:
                    setattr(old_value, "Slice12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Slice12"):
                opp_val = getattr(value, "Slice12", None)
                setattr(value, "Slice12", self)

    @property
    def trace_Slice17(self):
        return self.__trace_Slice17

    @trace_Slice17.setter
    def trace_Slice17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Slice__trace_Slice17", None)
        self.__trace_Slice17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Slice15"):
                opp_val = getattr(old_value, "trace_Slice15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Slice15"):
                opp_val = getattr(value, "trace_Slice15", None)
                if opp_val is None:
                    setattr(value, "trace_Slice15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_Slice(self):
        return self.__trace_Slice

    @trace_Slice.setter
    def trace_Slice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Slice__trace_Slice", None)
        self.__trace_Slice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Trace"):
                opp_val = getattr(old_value, "trace_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace"):
                opp_val = getattr(value, "trace_Trace", None)
                if opp_val is None:
                    setattr(value, "trace_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Slice12(self):
        return self.__Slice12

    @Slice12.setter
    def Slice12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Slice__Slice12", None)
        self.__Slice12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownedSubSlices"):
                opp_val = getattr(old_value, "ownedSubSlices", None)
                if opp_val == self:
                    setattr(old_value, "ownedSubSlices", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownedSubSlices"):
                opp_val = getattr(value, "ownedSubSlices", None)
                setattr(value, "ownedSubSlices", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Slice__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Slice"):
                    opp_val = getattr(item, "Slice", None)
                    
                    if opp_val == self:
                        setattr(item, "Slice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Slice"):
                    opp_val = getattr(item, "Slice", None)
                    
                    setattr(item, "Slice", self)
                    

    @property
    def trace_Slice15(self):
        return self.__trace_Slice15

    @trace_Slice15.setter
    def trace_Slice15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Slice__trace_Slice15", None)
        self.__trace_Slice15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_Slice17"):
                    opp_val = getattr(item, "trace_Slice17", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_Slice17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_Slice17"):
                    opp_val = getattr(item, "trace_Slice17", None)
                    
                    setattr(item, "trace_Slice17", self)
                    

    @property
    def trace_Slice14(self):
        return self.__trace_Slice14

    @trace_Slice14.setter
    def trace_Slice14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Slice__trace_Slice14", None)
        self.__trace_Slice14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Properties"):
                opp_val = getattr(old_value, "trace_Properties", None)
                if opp_val == self:
                    setattr(old_value, "trace_Properties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Properties"):
                opp_val = getattr(value, "trace_Properties", None)
                setattr(value, "trace_Properties", self)

    @property
    def Slice(self):
        return self.__Slice

    @Slice.setter
    def Slice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Slice__Slice", None)
        self.__Slice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_Slice6(self):
        return self.__trace_Slice6

    @trace_Slice6.setter
    def trace_Slice6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Slice__trace_Slice6", None)
        self.__trace_Slice6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_Event7"):
                    opp_val = getattr(item, "trace_Event7", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_Event7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_Event7"):
                    opp_val = getattr(item, "trace_Event7", None)
                    
                    setattr(item, "trace_Event7", self)
                    

    @property
    def trace_Slice4(self):
        return self.__trace_Slice4

    @trace_Slice4.setter
    def trace_Slice4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Slice__trace_Slice4", None)
        self.__trace_Slice4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Event"):
                opp_val = getattr(old_value, "trace_Event", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Event"):
                opp_val = getattr(value, "trace_Event", None)
                if opp_val is None:
                    setattr(value, "trace_Event", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getAggregatedEvents(self) -> Event:
        # TODO: Implement getAggregatedEvents method
        pass

    def getLatestTimestamp(self) -> str:
        # TODO: Implement getLatestTimestamp method
        pass

    def getHierarchicalName(self, separator: str) -> str:
        # TODO: Implement getHierarchicalName method
        pass

class trace_Trace(EModelElement):

    def __init__(self, hostId: str, precision: str, range: str, Trace: "trace_Event" = None, trace: set["trace_Event"] = None, trace_Trace: set["trace_Slice"] = None):
        self.hostId = hostId
        self.precision = precision
        self.range = range
        self.Trace = Trace
        self.trace = trace if trace is not None else set()
        self.trace_Trace = trace_Trace if trace_Trace is not None else set()
        
    @property
    def hostId(self) -> str:
        return self.__hostId

    @hostId.setter
    def hostId(self, hostId: str):
        self.__hostId = hostId

    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

    @property
    def trace(self):
        return self.__trace

    @trace.setter
    def trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace", None)
        self.__trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    setattr(item, "Event", self)
                    

    @property
    def Trace(self):
        return self.__Trace

    @Trace.setter
    def Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__Trace", None)
        self.__Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "events"):
                opp_val = getattr(old_value, "events", None)
                if opp_val == self:
                    setattr(old_value, "events", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "events"):
                opp_val = getattr(value, "events", None)
                setattr(value, "events", self)

    @property
    def trace_Trace(self):
        return self.__trace_Trace

    @trace_Trace.setter
    def trace_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace", None)
        self.__trace_Trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_Slice"):
                    opp_val = getattr(item, "trace_Slice", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_Slice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_Slice"):
                    opp_val = getattr(item, "trace_Slice", None)
                    
                    setattr(item, "trace_Slice", self)
                    

class Event:

    pass
class trace_ValueChangeEvent(Event):

    pass
class trace_MessageEvent(Event):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class trace_SchedulingEvent(Event):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class trace_ResourceEvent(Event):

    def __init__(self, kind: str):
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind
