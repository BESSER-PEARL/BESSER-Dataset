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
class types_ArrayType(Type):

    def __init__(self, arraySelector: int, types_ArrayType: "types_Type" = None):
        self.arraySelector = arraySelector
        self.types_ArrayType = types_ArrayType
        
    @property
    def arraySelector(self) -> int:
        return self.__arraySelector

    @arraySelector.setter
    def arraySelector(self, arraySelector: int):
        self.__arraySelector = arraySelector

    @property
    def types_ArrayType(self):
        return self.__types_ArrayType

    @types_ArrayType.setter
    def types_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_ArrayType__types_ArrayType", None)
        self.__types_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Type22"):
                opp_val = getattr(old_value, "types_Type22", None)
                if opp_val == self:
                    setattr(old_value, "types_Type22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Type22"):
                opp_val = getattr(value, "types_Type22", None)
                setattr(value, "types_Type22", self)

class types_ParameterizedType(Type):

    pass
class types_TypeParameter(Type):

    pass
class ParameterizedType:

    pass
class types_TypedElement(ABC):

    pass
class Feature:

    pass
class types_Property(Feature):

    pass
class types_Event(Feature):

    pass
class types_Operation(Feature):

    pass
class types_ComplexType(ParameterizedType):

    def __init__(self, ComplexType: "types_Feature" = None, owningType: set["types_Feature"] = None, types_ComplexType: "types_ComplexType" = None, types_ComplexType14: set["types_ComplexType"] = None):
        self.ComplexType = ComplexType
        self.owningType = owningType if owningType is not None else set()
        self.types_ComplexType = types_ComplexType
        self.types_ComplexType14 = types_ComplexType14 if types_ComplexType14 is not None else set()
        
    @property
    def types_ComplexType(self):
        return self.__types_ComplexType

    @types_ComplexType.setter
    def types_ComplexType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_ComplexType__types_ComplexType", None)
        self.__types_ComplexType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_ComplexType14"):
                opp_val = getattr(old_value, "types_ComplexType14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_ComplexType14"):
                opp_val = getattr(value, "types_ComplexType14", None)
                if opp_val is None:
                    setattr(value, "types_ComplexType14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owningType(self):
        return self.__owningType

    @owningType.setter
    def owningType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_ComplexType__owningType", None)
        self.__owningType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def ComplexType(self):
        return self.__ComplexType

    @ComplexType.setter
    def ComplexType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_ComplexType__ComplexType", None)
        self.__ComplexType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features"):
                opp_val = getattr(old_value, "features", None)
                if opp_val == self:
                    setattr(old_value, "features", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features"):
                opp_val = getattr(value, "features", None)
                setattr(value, "features", self)

    @property
    def types_ComplexType14(self):
        return self.__types_ComplexType14

    @types_ComplexType14.setter
    def types_ComplexType14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_ComplexType__types_ComplexType14", None)
        self.__types_ComplexType14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_ComplexType"):
                    opp_val = getattr(item, "types_ComplexType", None)
                    
                    if opp_val == self:
                        setattr(item, "types_ComplexType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_ComplexType"):
                    opp_val = getattr(item, "types_ComplexType", None)
                    
                    setattr(item, "types_ComplexType", self)
                    

    def getAllFeatures(self) -> Feature:
        # TODO: Implement getAllFeatures method
        pass

class TypedElement:

    pass
class PackageMember:

    pass
class types_Type(PackageMember):

    pass
class NamedElement:

    pass
class types_Parameter(NamedElement, TypedElement):

    pass
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

class types_Feature(NamedElement, TypedElement):

    pass
class types_Enumerator(NamedElement):

    def __init__(self, literalValue: str, enumerator: "types_EnumerationType" = None, Enumerator: "types_EnumerationType" = None):
        self.literalValue = literalValue
        self.enumerator = enumerator
        self.Enumerator = Enumerator
        
    @property
    def literalValue(self) -> str:
        return self.__literalValue

    @literalValue.setter
    def literalValue(self, literalValue: str):
        self.__literalValue = literalValue

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

class types_PackageMember(NamedElement):

    pass
class types_Package(NamedElement):

    pass