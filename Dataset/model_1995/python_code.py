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

class trace_EStructuralFeature:

    pass
class trace_EReference:

    pass
class trace_EAttribute:

    pass
class trace_EClass:

    pass
class trace_ReferenceMapping:

    def __init__(self, type: str, trace_ReferenceMapping: "trace_Trace" = None, trace_ReferenceMapping16: "trace_EReference" = None, trace_ReferenceMapping18: "trace_EStructuralFeature" = None):
        self.type = type
        self.trace_ReferenceMapping = trace_ReferenceMapping
        self.trace_ReferenceMapping16 = trace_ReferenceMapping16
        self.trace_ReferenceMapping18 = trace_ReferenceMapping18
        
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
            if hasattr(old_value, "trace_Trace4"):
                opp_val = getattr(old_value, "trace_Trace4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace4"):
                opp_val = getattr(value, "trace_Trace4", None)
                if opp_val is None:
                    setattr(value, "trace_Trace4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_ReferenceMapping18(self):
        return self.__trace_ReferenceMapping18

    @trace_ReferenceMapping18.setter
    def trace_ReferenceMapping18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ReferenceMapping__trace_ReferenceMapping18", None)
        self.__trace_ReferenceMapping18 = value
        
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
    def trace_ReferenceMapping16(self):
        return self.__trace_ReferenceMapping16

    @trace_ReferenceMapping16.setter
    def trace_ReferenceMapping16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ReferenceMapping__trace_ReferenceMapping16", None)
        self.__trace_ReferenceMapping16 = value
        
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
class trace_Trace:

    pass