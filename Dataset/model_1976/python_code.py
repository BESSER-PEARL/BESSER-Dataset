from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class EtlSimpleTrace_EObject:

    pass
class EtlSimpleTrace_TraceLink:

    def __init__(self, description: str, EtlSimpleTrace_TraceLink: "EtlSimpleTrace_Trace" = None, EtlSimpleTrace_TraceLink2: set["EtlSimpleTrace_EObject"] = None, EtlSimpleTrace_TraceLink4: set["EtlSimpleTrace_EObject"] = None):
        self.description = description
        self.EtlSimpleTrace_TraceLink = EtlSimpleTrace_TraceLink
        self.EtlSimpleTrace_TraceLink2 = EtlSimpleTrace_TraceLink2 if EtlSimpleTrace_TraceLink2 is not None else set()
        self.EtlSimpleTrace_TraceLink4 = EtlSimpleTrace_TraceLink4 if EtlSimpleTrace_TraceLink4 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def EtlSimpleTrace_TraceLink4(self):
        return self.__EtlSimpleTrace_TraceLink4

    @EtlSimpleTrace_TraceLink4.setter
    def EtlSimpleTrace_TraceLink4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EtlSimpleTrace_TraceLink__EtlSimpleTrace_TraceLink4", None)
        self.__EtlSimpleTrace_TraceLink4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EtlSimpleTrace_EObject5"):
                    opp_val = getattr(item, "EtlSimpleTrace_EObject5", None)
                    
                    if opp_val == self:
                        setattr(item, "EtlSimpleTrace_EObject5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EtlSimpleTrace_EObject5"):
                    opp_val = getattr(item, "EtlSimpleTrace_EObject5", None)
                    
                    setattr(item, "EtlSimpleTrace_EObject5", self)
                    

    @property
    def EtlSimpleTrace_TraceLink2(self):
        return self.__EtlSimpleTrace_TraceLink2

    @EtlSimpleTrace_TraceLink2.setter
    def EtlSimpleTrace_TraceLink2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EtlSimpleTrace_TraceLink__EtlSimpleTrace_TraceLink2", None)
        self.__EtlSimpleTrace_TraceLink2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EtlSimpleTrace_EObject"):
                    opp_val = getattr(item, "EtlSimpleTrace_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "EtlSimpleTrace_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EtlSimpleTrace_EObject"):
                    opp_val = getattr(item, "EtlSimpleTrace_EObject", None)
                    
                    setattr(item, "EtlSimpleTrace_EObject", self)
                    

    @property
    def EtlSimpleTrace_TraceLink(self):
        return self.__EtlSimpleTrace_TraceLink

    @EtlSimpleTrace_TraceLink.setter
    def EtlSimpleTrace_TraceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EtlSimpleTrace_TraceLink__EtlSimpleTrace_TraceLink", None)
        self.__EtlSimpleTrace_TraceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EtlSimpleTrace_Trace"):
                opp_val = getattr(old_value, "EtlSimpleTrace_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EtlSimpleTrace_Trace"):
                opp_val = getattr(value, "EtlSimpleTrace_Trace", None)
                if opp_val is None:
                    setattr(value, "EtlSimpleTrace_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EtlSimpleTrace_Trace:

    pass