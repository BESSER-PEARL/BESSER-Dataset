from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class trace_TraceElement:

    def __init__(self, event: str, timestamp: int, trace_TraceElement: "trace_Trace" = None):
        self.event = event
        self.timestamp = timestamp
        self.trace_TraceElement = trace_TraceElement
        
    @property
    def timestamp(self) -> int:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: int):
        self.__timestamp = timestamp

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def trace_TraceElement(self):
        return self.__trace_TraceElement

    @trace_TraceElement.setter
    def trace_TraceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceElement__trace_TraceElement", None)
        self.__trace_TraceElement = value
        
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

class trace_Trace:

    pass