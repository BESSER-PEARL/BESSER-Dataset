from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class trace_EObject:

    pass
class trace_Trace:

    def __init__(self, name: str, trace_Trace: "trace_Trace" = None, trace_Trace0: set["trace_Trace"] = None, trace_Trace3: set["trace_EObject"] = None, trace_Trace5: set["trace_EObject"] = None):
        self.name = name
        self.trace_Trace = trace_Trace
        self.trace_Trace0 = trace_Trace0 if trace_Trace0 is not None else set()
        self.trace_Trace3 = trace_Trace3 if trace_Trace3 is not None else set()
        self.trace_Trace5 = trace_Trace5 if trace_Trace5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trace_Trace3(self):
        return self.__trace_Trace3

    @trace_Trace3.setter
    def trace_Trace3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace3", None)
        self.__trace_Trace3 = value if value is not None else set()
        
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
    def trace_Trace5(self):
        return self.__trace_Trace5

    @trace_Trace5.setter
    def trace_Trace5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace5", None)
        self.__trace_Trace5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_EObject6"):
                    opp_val = getattr(item, "trace_EObject6", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_EObject6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_EObject6"):
                    opp_val = getattr(item, "trace_EObject6", None)
                    
                    setattr(item, "trace_EObject6", self)
                    

    @property
    def trace_Trace0(self):
        return self.__trace_Trace0

    @trace_Trace0.setter
    def trace_Trace0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace0", None)
        self.__trace_Trace0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_Trace"):
                    opp_val = getattr(item, "trace_Trace", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_Trace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_Trace"):
                    opp_val = getattr(item, "trace_Trace", None)
                    
                    setattr(item, "trace_Trace", self)
                    

    @property
    def trace_Trace(self):
        return self.__trace_Trace

    @trace_Trace.setter
    def trace_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace", None)
        self.__trace_Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Trace0"):
                opp_val = getattr(old_value, "trace_Trace0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace0"):
                opp_val = getattr(value, "trace_Trace0", None)
                if opp_val is None:
                    setattr(value, "trace_Trace0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
