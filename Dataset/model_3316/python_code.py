from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class traceability_EObject:

    pass
class traceability_Trace:

    def __init__(self, id: str, objects: str, traceability_Trace: "traceability_Traceability" = None, traceability_Trace4: set["traceability_EObject"] = None, traceability_Trace2: set["traceability_EObject"] = None):
        self.id = id
        self.objects = objects
        self.traceability_Trace = traceability_Trace
        self.traceability_Trace4 = traceability_Trace4 if traceability_Trace4 is not None else set()
        self.traceability_Trace2 = traceability_Trace2 if traceability_Trace2 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def objects(self) -> str:
        return self.__objects

    @objects.setter
    def objects(self, objects: str):
        self.__objects = objects

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

class traceability_Traceability:

    def __init__(self, id: str, traceability_Traceability: set["traceability_Trace"] = None):
        self.id = id
        self.traceability_Traceability = traceability_Traceability if traceability_Traceability is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def traceability_Traceability(self):
        return self.__traceability_Traceability

    @traceability_Traceability.setter
    def traceability_Traceability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceability_Traceability__traceability_Traceability", None)
        self.__traceability_Traceability = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "traceability_Trace"):
                    opp_val = getattr(item, "traceability_Trace", None)
                    
                    if opp_val == self:
                        setattr(item, "traceability_Trace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "traceability_Trace"):
                    opp_val = getattr(item, "traceability_Trace", None)
                    
                    setattr(item, "traceability_Trace", self)
                    
