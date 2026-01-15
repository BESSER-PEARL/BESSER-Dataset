from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class traces_Trace:

    def __init__(self, rule: str, traces_Trace2: "traces_EObject" = None, traces_Trace4: "traces_EObject" = None, traces_Trace: "traces_TraceSet" = None):
        self.rule = rule
        self.traces_Trace2 = traces_Trace2
        self.traces_Trace4 = traces_Trace4
        self.traces_Trace = traces_Trace
        
    @property
    def rule(self) -> str:
        return self.__rule

    @rule.setter
    def rule(self, rule: str):
        self.__rule = rule

    @property
    def traces_Trace(self):
        return self.__traces_Trace

    @traces_Trace.setter
    def traces_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Trace__traces_Trace", None)
        self.__traces_Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_TraceSet"):
                opp_val = getattr(old_value, "traces_TraceSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_TraceSet"):
                opp_val = getattr(value, "traces_TraceSet", None)
                if opp_val is None:
                    setattr(value, "traces_TraceSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def traces_Trace2(self):
        return self.__traces_Trace2

    @traces_Trace2.setter
    def traces_Trace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Trace__traces_Trace2", None)
        self.__traces_Trace2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_EObject"):
                opp_val = getattr(old_value, "traces_EObject", None)
                if opp_val == self:
                    setattr(old_value, "traces_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_EObject"):
                opp_val = getattr(value, "traces_EObject", None)
                setattr(value, "traces_EObject", self)

    @property
    def traces_Trace4(self):
        return self.__traces_Trace4

    @traces_Trace4.setter
    def traces_Trace4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Trace__traces_Trace4", None)
        self.__traces_Trace4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_EObject5"):
                opp_val = getattr(old_value, "traces_EObject5", None)
                if opp_val == self:
                    setattr(old_value, "traces_EObject5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_EObject5"):
                opp_val = getattr(value, "traces_EObject5", None)
                setattr(value, "traces_EObject5", self)

class traces_TraceSet:

    pass
class traces_EObject:

    pass