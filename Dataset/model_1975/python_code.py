from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SimpleTrace_EObject:

    pass
class SimpleTrace_TraceLink:

    def __init__(self, description: str, SimpleTrace_TraceLink: "SimpleTrace_Trace" = None, SimpleTrace_TraceLink2: set["SimpleTrace_EObject"] = None, SimpleTrace_TraceLink4: set["SimpleTrace_EObject"] = None):
        self.description = description
        self.SimpleTrace_TraceLink = SimpleTrace_TraceLink
        self.SimpleTrace_TraceLink2 = SimpleTrace_TraceLink2 if SimpleTrace_TraceLink2 is not None else set()
        self.SimpleTrace_TraceLink4 = SimpleTrace_TraceLink4 if SimpleTrace_TraceLink4 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def SimpleTrace_TraceLink4(self):
        return self.__SimpleTrace_TraceLink4

    @SimpleTrace_TraceLink4.setter
    def SimpleTrace_TraceLink4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleTrace_TraceLink__SimpleTrace_TraceLink4", None)
        self.__SimpleTrace_TraceLink4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimpleTrace_EObject5"):
                    opp_val = getattr(item, "SimpleTrace_EObject5", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleTrace_EObject5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleTrace_EObject5"):
                    opp_val = getattr(item, "SimpleTrace_EObject5", None)
                    
                    setattr(item, "SimpleTrace_EObject5", self)
                    

    @property
    def SimpleTrace_TraceLink(self):
        return self.__SimpleTrace_TraceLink

    @SimpleTrace_TraceLink.setter
    def SimpleTrace_TraceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleTrace_TraceLink__SimpleTrace_TraceLink", None)
        self.__SimpleTrace_TraceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleTrace_Trace"):
                opp_val = getattr(old_value, "SimpleTrace_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleTrace_Trace"):
                opp_val = getattr(value, "SimpleTrace_Trace", None)
                if opp_val is None:
                    setattr(value, "SimpleTrace_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleTrace_TraceLink2(self):
        return self.__SimpleTrace_TraceLink2

    @SimpleTrace_TraceLink2.setter
    def SimpleTrace_TraceLink2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleTrace_TraceLink__SimpleTrace_TraceLink2", None)
        self.__SimpleTrace_TraceLink2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimpleTrace_EObject"):
                    opp_val = getattr(item, "SimpleTrace_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleTrace_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleTrace_EObject"):
                    opp_val = getattr(item, "SimpleTrace_EObject", None)
                    
                    setattr(item, "SimpleTrace_EObject", self)
                    

class SimpleTrace_Trace:

    pass