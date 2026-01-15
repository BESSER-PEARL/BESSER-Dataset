from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Type:

    pass
class types_PrimitiveType(Type):

    pass
class PrimitiveType:

    pass
class types_EnumerationType(PrimitiveType):

    pass
class types_TypedElement(ABC):

    pass
class Feature:

    pass
class types_Event(Feature):

    pass
class types_Property(Feature):

    pass
class types_Operation(Feature):

    pass
class types_ComplexType(Type):

    pass
class TypedElement:

    pass
class NamedElement:

    pass
class types_Parameter(NamedElement, TypedElement):

    pass
class types_Feature(NamedElement, TypedElement):

    pass
class types_Enumerator(NamedElement):

    def __init__(self, literalValue: str, Enumerator: "types_EnumerationType" = None, enumerator: "types_EnumerationType" = None):
        self.literalValue = literalValue
        self.Enumerator = Enumerator
        self.enumerator = enumerator
        
    @property
    def literalValue(self) -> str:
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue

    @property
    def enumerator(self):
        return self.__enumerator

    @enumerator.setter
    def enumerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Enumerator__enumerator", None)
        self.__enumerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnumerationType"):
                opp_val = getattr(old_value, "EnumerationType", None)
                if opp_val == self:
                    setattr(old_value, "EnumerationType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnumerationType"):
                opp_val = getattr(value, "EnumerationType", None)
                setattr(value, "EnumerationType", self)

    @property
    def Enumerator(self):
        return self.__Enumerator

    @Enumerator.setter
    def Enumerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Enumerator__Enumerator", None)
        self.__Enumerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owningEnumeration"):
                opp_val = getattr(old_value, "owningEnumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owningEnumeration"):
                opp_val = getattr(value, "owningEnumeration", None)
                if opp_val is None:
                    setattr(value, "owningEnumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class types_TypeConstraint(NamedElement):

    def __init__(self, value: str, types_TypeConstraint: "types_Type" = None):
        self.value = value
        self.types_TypeConstraint = types_TypeConstraint
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def types_TypeConstraint(self):
        return self.__types_TypeConstraint

    @types_TypeConstraint.setter
    def types_TypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_TypeConstraint__types_TypeConstraint", None)
        self.__types_TypeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Type"):
                opp_val = getattr(old_value, "types_Type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Type"):
                opp_val = getattr(value, "types_Type", None)
                if opp_val is None:
                    setattr(value, "types_Type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class types_Type(NamedElement):

    pass