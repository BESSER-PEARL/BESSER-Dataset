from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class traces_TraceRepository:

    pass
class traces_EObject:

    pass
class traces_Trace:

    def __init__(self, Role: str, traces_Trace: "traces_EObject" = None, traces_Trace2: "traces_EObject" = None, traces_Trace5: "traces_TraceRepository" = None):
        self.Role = Role
        self.traces_Trace = traces_Trace
        self.traces_Trace2 = traces_Trace2
        self.traces_Trace5 = traces_Trace5
        
    @property
    def Role(self) -> str:
        return self.__Role

    @Role.setter
    def Role(self, Role: str):
        self.__Role = Role

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
            if hasattr(old_value, "traces_EObject3"):
                opp_val = getattr(old_value, "traces_EObject3", None)
                if opp_val == self:
                    setattr(old_value, "traces_EObject3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_EObject3"):
                opp_val = getattr(value, "traces_EObject3", None)
                setattr(value, "traces_EObject3", self)

    @property
    def traces_Trace5(self):
        return self.__traces_Trace5

    @traces_Trace5.setter
    def traces_Trace5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traces_Trace__traces_Trace5", None)
        self.__traces_Trace5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces_TraceRepository"):
                opp_val = getattr(old_value, "traces_TraceRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_TraceRepository"):
                opp_val = getattr(value, "traces_TraceRepository", None)
                if opp_val is None:
                    setattr(value, "traces_TraceRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "traces_EObject"):
                opp_val = getattr(old_value, "traces_EObject", None)
                if opp_val == self:
                    setattr(old_value, "traces_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces_EObject"):
                opp_val = getattr(value, "traces_EObject", None)
                setattr(value, "traces_EObject", self)
