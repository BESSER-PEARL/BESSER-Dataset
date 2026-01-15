from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class trace_EObject:

    pass
class trace_TraceLink:

    def __init__(self, ruleName: str, trace_TraceLink: "trace_Trace" = None, trace_TraceLink2: set["trace_EObject"] = None, trace_TraceLink4: set["trace_EObject"] = None):
        self.ruleName = ruleName
        self.trace_TraceLink = trace_TraceLink
        self.trace_TraceLink2 = trace_TraceLink2 if trace_TraceLink2 is not None else set()
        self.trace_TraceLink4 = trace_TraceLink4 if trace_TraceLink4 is not None else set()
        
    @property
    def ruleName(self) -> str:
        return self.__ruleName

    @ruleName.setter
    def ruleName(self, ruleName: str):
        self.__ruleName = ruleName

    @property
    def trace_TraceLink2(self):
        return self.__trace_TraceLink2

    @trace_TraceLink2.setter
    def trace_TraceLink2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__trace_TraceLink2", None)
        self.__trace_TraceLink2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_EObject"):
                    opp_val = getattr(item, "trace_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_EObject"):
                    opp_val = getattr(item, "trace_EObject", None)
                    
                    setattr(item, "trace_EObject", self)
                    

    @property
    def trace_TraceLink(self):
        return self.__trace_TraceLink

    @trace_TraceLink.setter
    def trace_TraceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__trace_TraceLink", None)
        self.__trace_TraceLink = value
        
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
    def trace_TraceLink4(self):
        return self.__trace_TraceLink4

    @trace_TraceLink4.setter
    def trace_TraceLink4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__trace_TraceLink4", None)
        self.__trace_TraceLink4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_EObject5"):
                    opp_val = getattr(item, "trace_EObject5", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_EObject5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_EObject5"):
                    opp_val = getattr(item, "trace_EObject5", None)
                    
                    setattr(item, "trace_EObject5", self)
                    

class trace_Trace:

    pass