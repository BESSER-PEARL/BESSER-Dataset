from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class traceability_EObject:

    pass
class traceability_Trace:

    def __init__(self, ruleDescriptorId: str, traceability_Trace: "traceability_Traceability" = None, traceability_Trace2: set["traceability_EObject"] = None, traceability_Trace4: set["traceability_EObject"] = None):
        self.ruleDescriptorId = ruleDescriptorId
        self.traceability_Trace = traceability_Trace
        self.traceability_Trace2 = traceability_Trace2 if traceability_Trace2 is not None else set()
        self.traceability_Trace4 = traceability_Trace4 if traceability_Trace4 is not None else set()
        
    @property
    def ruleDescriptorId(self) -> str:
        return self.__ruleDescriptorId

    @ruleDescriptorId.setter
    def ruleDescriptorId(self, ruleDescriptorId: str):
        self.__ruleDescriptorId = ruleDescriptorId

    @property
    def traceability_Trace2(self):
        return self.__traceability_Trace2

    @traceability_Trace2.setter
    def traceability_Trace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Trace__traceability_Trace2", None)
        self.__traceability_Trace2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_EObject"):
                    opp_val = getattr(item, "traceability_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_EObject"):
                    opp_val = getattr(item, "traceability_EObject", None)
                    
                    setattr(item, "traceability_EObject", self)
                    

    @property
    def traceability_Trace(self):
        return self.__traceability_Trace

    @traceability_Trace.setter
    def traceability_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Trace__traceability_Trace", None)
        self.__traceability_Trace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traceability_Traceability"):
                opp_val = getattr(old_value, "traceability_Traceability", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traceability_Traceability"):
                opp_val = getattr(value, "traceability_Traceability", None)
                if opp_val is None:
                    setattr(value, "traceability_Traceability", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def traceability_Trace4(self):
        return self.__traceability_Trace4

    @traceability_Trace4.setter
    def traceability_Trace4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Trace__traceability_Trace4", None)
        self.__traceability_Trace4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_EObject5"):
                    opp_val = getattr(item, "traceability_EObject5", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_EObject5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_EObject5"):
                    opp_val = getattr(item, "traceability_EObject5", None)
                    
                    setattr(item, "traceability_EObject5", self)
                    

class traceability_Traceability:

    pass