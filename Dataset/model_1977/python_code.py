from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeGraphTrace_TClass:

    pass
class TypeGraphTrace_TMethodSignature:

    pass
class TypeGraphTrace_ClassListTrace:

    def __init__(self, concatSignature: str, TypeGraphTrace_ClassListTrace: "TypeGraphTrace_Trace" = None, TypeGraphTrace_ClassListTrace8: set["TypeGraphTrace_TClass"] = None):
        self.concatSignature = concatSignature
        self.TypeGraphTrace_ClassListTrace = TypeGraphTrace_ClassListTrace
        self.TypeGraphTrace_ClassListTrace8 = TypeGraphTrace_ClassListTrace8 if TypeGraphTrace_ClassListTrace8 is not None else set()
        
    @property
    def concatSignature(self) -> str:
        return self.__concatSignature

    @concatSignature.setter
    def concatSignature(self, concatSignature: str):
        self.__concatSignature = concatSignature

    @property
    def TypeGraphTrace_ClassListTrace8(self):
        return self.__TypeGraphTrace_ClassListTrace8

    @TypeGraphTrace_ClassListTrace8.setter
    def TypeGraphTrace_ClassListTrace8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphTrace_ClassListTrace__TypeGraphTrace_ClassListTrace8", None)
        self.__TypeGraphTrace_ClassListTrace8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeGraphTrace_TClass"):
                    opp_val = getattr(item, "TypeGraphTrace_TClass", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeGraphTrace_TClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeGraphTrace_TClass"):
                    opp_val = getattr(item, "TypeGraphTrace_TClass", None)
                    
                    setattr(item, "TypeGraphTrace_TClass", self)
                    

    @property
    def TypeGraphTrace_ClassListTrace(self):
        return self.__TypeGraphTrace_ClassListTrace

    @TypeGraphTrace_ClassListTrace.setter
    def TypeGraphTrace_ClassListTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphTrace_ClassListTrace__TypeGraphTrace_ClassListTrace", None)
        self.__TypeGraphTrace_ClassListTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphTrace_Trace4"):
                opp_val = getattr(old_value, "TypeGraphTrace_Trace4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphTrace_Trace4"):
                opp_val = getattr(value, "TypeGraphTrace_Trace4", None)
                if opp_val is None:
                    setattr(value, "TypeGraphTrace_Trace4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypeGraphTrace_MethodSignatureTrace:

    def __init__(self, signatureString: str, TypeGraphTrace_MethodSignatureTrace: "TypeGraphTrace_Trace" = None, TypeGraphTrace_MethodSignatureTrace6: "TypeGraphTrace_TMethodSignature" = None):
        self.signatureString = signatureString
        self.TypeGraphTrace_MethodSignatureTrace = TypeGraphTrace_MethodSignatureTrace
        self.TypeGraphTrace_MethodSignatureTrace6 = TypeGraphTrace_MethodSignatureTrace6
        
    @property
    def signatureString(self) -> str:
        return self.__signatureString

    @signatureString.setter
    def signatureString(self, signatureString: str):
        self.__signatureString = signatureString

    @property
    def TypeGraphTrace_MethodSignatureTrace6(self):
        return self.__TypeGraphTrace_MethodSignatureTrace6

    @TypeGraphTrace_MethodSignatureTrace6.setter
    def TypeGraphTrace_MethodSignatureTrace6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphTrace_MethodSignatureTrace__TypeGraphTrace_MethodSignatureTrace6", None)
        self.__TypeGraphTrace_MethodSignatureTrace6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphTrace_TMethodSignature"):
                opp_val = getattr(old_value, "TypeGraphTrace_TMethodSignature", None)
                if opp_val == self:
                    setattr(old_value, "TypeGraphTrace_TMethodSignature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphTrace_TMethodSignature"):
                opp_val = getattr(value, "TypeGraphTrace_TMethodSignature", None)
                setattr(value, "TypeGraphTrace_TMethodSignature", self)

    @property
    def TypeGraphTrace_MethodSignatureTrace(self):
        return self.__TypeGraphTrace_MethodSignatureTrace

    @TypeGraphTrace_MethodSignatureTrace.setter
    def TypeGraphTrace_MethodSignatureTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeGraphTrace_MethodSignatureTrace__TypeGraphTrace_MethodSignatureTrace", None)
        self.__TypeGraphTrace_MethodSignatureTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeGraphTrace_Trace2"):
                opp_val = getattr(old_value, "TypeGraphTrace_Trace2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeGraphTrace_Trace2"):
                opp_val = getattr(value, "TypeGraphTrace_Trace2", None)
                if opp_val is None:
                    setattr(value, "TypeGraphTrace_Trace2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypeGraphTrace_TypeGraph:

    pass
class TypeGraphTrace_Trace:

    pass