from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ReferenceMappingType(Enum):
    NONE = "NONE"
    TRANSLATED = "TRANSLATED"
    MAPPED = "MAPPED"


############################################
# Definition of Classes
############################################

class trace_EPackage:

    pass
class trace_EStructuralFeature:

    pass
class trace_EReference:

    pass
class trace_EAttribute:

    pass
class trace_ReferenceMapping:

    def __init__(self, type: str, trace_ReferenceMapping: "trace_Trace" = None, trace_ReferenceMapping27: "trace_EReference" = None, trace_ReferenceMapping29: "trace_EStructuralFeature" = None):
        self.type = type
        self.trace_ReferenceMapping = trace_ReferenceMapping
        self.trace_ReferenceMapping27 = trace_ReferenceMapping27
        self.trace_ReferenceMapping29 = trace_ReferenceMapping29
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def trace_ReferenceMapping(self):
        return self.__trace_ReferenceMapping

    @trace_ReferenceMapping.setter
    def trace_ReferenceMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ReferenceMapping__trace_ReferenceMapping", None)
        self.__trace_ReferenceMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Trace14"):
                opp_val = getattr(old_value, "trace_Trace14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace14"):
                opp_val = getattr(value, "trace_Trace14", None)
                if opp_val is None:
                    setattr(value, "trace_Trace14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_ReferenceMapping29(self):
        return self.__trace_ReferenceMapping29

    @trace_ReferenceMapping29.setter
    def trace_ReferenceMapping29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ReferenceMapping__trace_ReferenceMapping29", None)
        self.__trace_ReferenceMapping29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EStructuralFeature"):
                opp_val = getattr(old_value, "trace_EStructuralFeature", None)
                if opp_val == self:
                    setattr(old_value, "trace_EStructuralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EStructuralFeature"):
                opp_val = getattr(value, "trace_EStructuralFeature", None)
                setattr(value, "trace_EStructuralFeature", self)

    @property
    def trace_ReferenceMapping27(self):
        return self.__trace_ReferenceMapping27

    @trace_ReferenceMapping27.setter
    def trace_ReferenceMapping27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ReferenceMapping__trace_ReferenceMapping27", None)
        self.__trace_ReferenceMapping27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EReference"):
                opp_val = getattr(old_value, "trace_EReference", None)
                if opp_val == self:
                    setattr(old_value, "trace_EReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EReference"):
                opp_val = getattr(value, "trace_EReference", None)
                setattr(value, "trace_EReference", self)

class trace_AttributeMapping:

    pass
class trace_ClassMapping:

    pass
class trace_EClass:

    pass
class trace_Trace:

    def __init__(self, trace_Trace: "trace_EPackage" = None, trace_Trace2: "trace_EPackage" = None, trace_Trace5: "trace_EClass" = None, trace_Trace7: "trace_EClass" = None, trace_Trace10: set["trace_ClassMapping"] = None, trace_Trace12: set["trace_AttributeMapping"] = None, trace_Trace14: set["trace_ReferenceMapping"] = None):
        self.trace_Trace = trace_Trace
        self.trace_Trace2 = trace_Trace2
        self.trace_Trace5 = trace_Trace5
        self.trace_Trace7 = trace_Trace7
        self.trace_Trace10 = trace_Trace10 if trace_Trace10 is not None else set()
        self.trace_Trace12 = trace_Trace12 if trace_Trace12 is not None else set()
        self.trace_Trace14 = trace_Trace14 if trace_Trace14 is not None else set()
        
    @property
    def trace_Trace12(self):
        return self.__trace_Trace12

    @trace_Trace12.setter
    def trace_Trace12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace12", None)
        self.__trace_Trace12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_AttributeMapping"):
                    opp_val = getattr(item, "trace_AttributeMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_AttributeMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_AttributeMapping"):
                    opp_val = getattr(item, "trace_AttributeMapping", None)
                    
                    setattr(item, "trace_AttributeMapping", self)
                    

    @property
    def trace_Trace7(self):
        return self.__trace_Trace7

    @trace_Trace7.setter
    def trace_Trace7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace7", None)
        self.__trace_Trace7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EClass8"):
                opp_val = getattr(old_value, "trace_EClass8", None)
                if opp_val == self:
                    setattr(old_value, "trace_EClass8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EClass8"):
                opp_val = getattr(value, "trace_EClass8", None)
                setattr(value, "trace_EClass8", self)

    @property
    def trace_Trace10(self):
        return self.__trace_Trace10

    @trace_Trace10.setter
    def trace_Trace10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace10", None)
        self.__trace_Trace10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_ClassMapping"):
                    opp_val = getattr(item, "trace_ClassMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_ClassMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_ClassMapping"):
                    opp_val = getattr(item, "trace_ClassMapping", None)
                    
                    setattr(item, "trace_ClassMapping", self)
                    

    @property
    def trace_Trace14(self):
        return self.__trace_Trace14

    @trace_Trace14.setter
    def trace_Trace14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace14", None)
        self.__trace_Trace14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_ReferenceMapping"):
                    opp_val = getattr(item, "trace_ReferenceMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_ReferenceMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_ReferenceMapping"):
                    opp_val = getattr(item, "trace_ReferenceMapping", None)
                    
                    setattr(item, "trace_ReferenceMapping", self)
                    

    @property
    def trace_Trace2(self):
        return self.__trace_Trace2

    @trace_Trace2.setter
    def trace_Trace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace2", None)
        self.__trace_Trace2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EPackage3"):
                opp_val = getattr(old_value, "trace_EPackage3", None)
                if opp_val == self:
                    setattr(old_value, "trace_EPackage3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EPackage3"):
                opp_val = getattr(value, "trace_EPackage3", None)
                setattr(value, "trace_EPackage3", self)

    @property
    def trace_Trace5(self):
        return self.__trace_Trace5

    @trace_Trace5.setter
    def trace_Trace5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace5", None)
        self.__trace_Trace5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EClass"):
                opp_val = getattr(old_value, "trace_EClass", None)
                if opp_val == self:
                    setattr(old_value, "trace_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EClass"):
                opp_val = getattr(value, "trace_EClass", None)
                setattr(value, "trace_EClass", self)

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
            if hasattr(old_value, "trace_EPackage"):
                opp_val = getattr(old_value, "trace_EPackage", None)
                if opp_val == self:
                    setattr(old_value, "trace_EPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EPackage"):
                opp_val = getattr(value, "trace_EPackage", None)
                setattr(value, "trace_EPackage", self)

    def addReferenceMapping(self, type: str, image: str, proto: str):
        # TODO: Implement addReferenceMapping method
        pass

    def addClassMapping(self, proto: str, image: str) -> str:
        # TODO: Implement addClassMapping method
        pass

    def addAttributeMapping(self, image: str, proto: str):
        # TODO: Implement addAttributeMapping method
        pass
