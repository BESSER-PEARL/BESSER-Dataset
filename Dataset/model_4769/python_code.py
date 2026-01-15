from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class annotations_atl_types_Type:

    pass
class annotations_atl_types_EObject:

    pass
class AtlAnnotation:

    pass
class atl_types_annotations_BindingAnnotation(AtlAnnotation):

    def __init__(self, name: str, atl_types_annotations_BindingAnnotation: "annotations_atl_types_EObject" = None, atl_types_annotations_BindingAnnotation18: "annotations_atl_types_EObject" = None, atl_types_annotations_BindingAnnotation21: "annotations_atl_types_Type" = None, atl_types_annotations_BindingAnnotation24: "annotations_atl_types_Type" = None):
        self.name = name
        self.atl_types_annotations_BindingAnnotation = atl_types_annotations_BindingAnnotation
        self.atl_types_annotations_BindingAnnotation18 = atl_types_annotations_BindingAnnotation18
        self.atl_types_annotations_BindingAnnotation21 = atl_types_annotations_BindingAnnotation21
        self.atl_types_annotations_BindingAnnotation24 = atl_types_annotations_BindingAnnotation24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atl_types_annotations_BindingAnnotation24(self):
        return self.__atl_types_annotations_BindingAnnotation24

    @atl_types_annotations_BindingAnnotation24.setter
    def atl_types_annotations_BindingAnnotation24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_annotations_BindingAnnotation__atl_types_annotations_BindingAnnotation24", None)
        self.__atl_types_annotations_BindingAnnotation24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotations_atl_types_Type25"):
                opp_val = getattr(old_value, "annotations_atl_types_Type25", None)
                if opp_val == self:
                    setattr(old_value, "annotations_atl_types_Type25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotations_atl_types_Type25"):
                opp_val = getattr(value, "annotations_atl_types_Type25", None)
                setattr(value, "annotations_atl_types_Type25", self)

    @property
    def atl_types_annotations_BindingAnnotation21(self):
        return self.__atl_types_annotations_BindingAnnotation21

    @atl_types_annotations_BindingAnnotation21.setter
    def atl_types_annotations_BindingAnnotation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_annotations_BindingAnnotation__atl_types_annotations_BindingAnnotation21", None)
        self.__atl_types_annotations_BindingAnnotation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotations_atl_types_Type22"):
                opp_val = getattr(old_value, "annotations_atl_types_Type22", None)
                if opp_val == self:
                    setattr(old_value, "annotations_atl_types_Type22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotations_atl_types_Type22"):
                opp_val = getattr(value, "annotations_atl_types_Type22", None)
                setattr(value, "annotations_atl_types_Type22", self)

    @property
    def atl_types_annotations_BindingAnnotation18(self):
        return self.__atl_types_annotations_BindingAnnotation18

    @atl_types_annotations_BindingAnnotation18.setter
    def atl_types_annotations_BindingAnnotation18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_annotations_BindingAnnotation__atl_types_annotations_BindingAnnotation18", None)
        self.__atl_types_annotations_BindingAnnotation18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotations_atl_types_EObject19"):
                opp_val = getattr(old_value, "annotations_atl_types_EObject19", None)
                if opp_val == self:
                    setattr(old_value, "annotations_atl_types_EObject19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotations_atl_types_EObject19"):
                opp_val = getattr(value, "annotations_atl_types_EObject19", None)
                setattr(value, "annotations_atl_types_EObject19", self)

    @property
    def atl_types_annotations_BindingAnnotation(self):
        return self.__atl_types_annotations_BindingAnnotation

    @atl_types_annotations_BindingAnnotation.setter
    def atl_types_annotations_BindingAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_annotations_BindingAnnotation__atl_types_annotations_BindingAnnotation", None)
        self.__atl_types_annotations_BindingAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotations_atl_types_EObject16"):
                opp_val = getattr(old_value, "annotations_atl_types_EObject16", None)
                if opp_val == self:
                    setattr(old_value, "annotations_atl_types_EObject16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotations_atl_types_EObject16"):
                opp_val = getattr(value, "annotations_atl_types_EObject16", None)
                setattr(value, "annotations_atl_types_EObject16", self)

class atl_types_annotations_HelperAnnotation(AtlAnnotation):

    def __init__(self, name: str, atl_types_annotations_HelperAnnotation: "annotations_atl_types_EObject" = None, atl_types_annotations_HelperAnnotation14: "annotations_atl_types_Type" = None):
        self.name = name
        self.atl_types_annotations_HelperAnnotation = atl_types_annotations_HelperAnnotation
        self.atl_types_annotations_HelperAnnotation14 = atl_types_annotations_HelperAnnotation14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atl_types_annotations_HelperAnnotation14(self):
        return self.__atl_types_annotations_HelperAnnotation14

    @atl_types_annotations_HelperAnnotation14.setter
    def atl_types_annotations_HelperAnnotation14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_annotations_HelperAnnotation__atl_types_annotations_HelperAnnotation14", None)
        self.__atl_types_annotations_HelperAnnotation14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotations_atl_types_Type"):
                opp_val = getattr(old_value, "annotations_atl_types_Type", None)
                if opp_val == self:
                    setattr(old_value, "annotations_atl_types_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotations_atl_types_Type"):
                opp_val = getattr(value, "annotations_atl_types_Type", None)
                setattr(value, "annotations_atl_types_Type", self)

    @property
    def atl_types_annotations_HelperAnnotation(self):
        return self.__atl_types_annotations_HelperAnnotation

    @atl_types_annotations_HelperAnnotation.setter
    def atl_types_annotations_HelperAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_annotations_HelperAnnotation__atl_types_annotations_HelperAnnotation", None)
        self.__atl_types_annotations_HelperAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotations_atl_types_EObject"):
                opp_val = getattr(old_value, "annotations_atl_types_EObject", None)
                if opp_val == self:
                    setattr(old_value, "annotations_atl_types_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotations_atl_types_EObject"):
                opp_val = getattr(value, "annotations_atl_types_EObject", None)
                setattr(value, "annotations_atl_types_EObject", self)

class atl_types_annotations_AtlAnnotation(ABC):

    pass
class ReflectiveType:

    pass
class atl_types_ReflectiveClass(ReflectiveType):

    pass
class atl_types_annotations_ExpressionAnnotation(AtlAnnotation):

    pass
class PrimitiveType:

    pass
class atl_types_StringType(PrimitiveType):

    pass
class atl_types_IntegerType(PrimitiveType):

    pass
class atl_types_FloatType(PrimitiveType):

    pass
class atl_types_BooleanType(PrimitiveType):

    pass
class Type:

    pass
class atl_types_ThisModuleType(Type):

    pass
class atl_types_TupleType(Type):

    pass
class atl_types_PrimitiveType(Type):

    pass
class atl_types_Type(ABC):

    def __init__(self, multivalued: bool, atl_types_Type: "atl_types_MapType" = None, atl_types_Type4: "atl_types_MapType" = None, atl_types_Type7: "atl_types_TupleAttribute" = None, atl_types_Type11: "atl_types_UnionType" = None):
        self.multivalued = multivalued
        self.atl_types_Type = atl_types_Type
        self.atl_types_Type4 = atl_types_Type4
        self.atl_types_Type7 = atl_types_Type7
        self.atl_types_Type11 = atl_types_Type11
        
    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

    @property
    def atl_types_Type7(self):
        return self.__atl_types_Type7

    @atl_types_Type7.setter
    def atl_types_Type7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_Type__atl_types_Type7", None)
        self.__atl_types_Type7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atl_types_TupleAttribute6"):
                opp_val = getattr(old_value, "atl_types_TupleAttribute6", None)
                if opp_val == self:
                    setattr(old_value, "atl_types_TupleAttribute6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atl_types_TupleAttribute6"):
                opp_val = getattr(value, "atl_types_TupleAttribute6", None)
                setattr(value, "atl_types_TupleAttribute6", self)

    @property
    def atl_types_Type(self):
        return self.__atl_types_Type

    @atl_types_Type.setter
    def atl_types_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_Type__atl_types_Type", None)
        self.__atl_types_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atl_types_MapType"):
                opp_val = getattr(old_value, "atl_types_MapType", None)
                if opp_val == self:
                    setattr(old_value, "atl_types_MapType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atl_types_MapType"):
                opp_val = getattr(value, "atl_types_MapType", None)
                setattr(value, "atl_types_MapType", self)

    @property
    def atl_types_Type11(self):
        return self.__atl_types_Type11

    @atl_types_Type11.setter
    def atl_types_Type11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_Type__atl_types_Type11", None)
        self.__atl_types_Type11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atl_types_UnionType"):
                opp_val = getattr(old_value, "atl_types_UnionType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atl_types_UnionType"):
                opp_val = getattr(value, "atl_types_UnionType", None)
                if opp_val is None:
                    setattr(value, "atl_types_UnionType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def atl_types_Type4(self):
        return self.__atl_types_Type4

    @atl_types_Type4.setter
    def atl_types_Type4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_Type__atl_types_Type4", None)
        self.__atl_types_Type4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atl_types_MapType3"):
                opp_val = getattr(old_value, "atl_types_MapType3", None)
                if opp_val == self:
                    setattr(old_value, "atl_types_MapType3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atl_types_MapType3"):
                opp_val = getattr(value, "atl_types_MapType3", None)
                setattr(value, "atl_types_MapType3", self)

class atl_types_UnionType(Type):

    pass
class atl_types_ReflectiveType(Type):

    pass
class atl_types_EClass:

    pass
class atl_types_EObject:

    pass
class atl_types_EnumType(Type):

    def __init__(self, name: str, atl_types_EnumType: "atl_types_EObject" = None):
        self.name = name
        self.atl_types_EnumType = atl_types_EnumType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atl_types_EnumType(self):
        return self.__atl_types_EnumType

    @atl_types_EnumType.setter
    def atl_types_EnumType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_EnumType__atl_types_EnumType", None)
        self.__atl_types_EnumType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atl_types_EObject"):
                opp_val = getattr(old_value, "atl_types_EObject", None)
                if opp_val == self:
                    setattr(old_value, "atl_types_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atl_types_EObject"):
                opp_val = getattr(value, "atl_types_EObject", None)
                setattr(value, "atl_types_EObject", self)

class atl_types_EmptyCollection(Type):

    pass
class RefType:

    pass
class atl_types_Metaclass(RefType):

    def __init__(self, name: str, atl_types_Metaclass: "atl_types_EClass" = None):
        self.name = name
        self.atl_types_Metaclass = atl_types_Metaclass
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atl_types_Metaclass(self):
        return self.__atl_types_Metaclass

    @atl_types_Metaclass.setter
    def atl_types_Metaclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_Metaclass__atl_types_Metaclass", None)
        self.__atl_types_Metaclass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atl_types_EClass"):
                opp_val = getattr(old_value, "atl_types_EClass", None)
                if opp_val == self:
                    setattr(old_value, "atl_types_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atl_types_EClass"):
                opp_val = getattr(value, "atl_types_EClass", None)
                setattr(value, "atl_types_EClass", self)

class atl_types_Unknown(RefType):

    pass
class atl_types_RefType(Type):

    pass
class atl_types_MapType(Type):

    pass
class atl_types_TupleAttribute:

    def __init__(self, name: str, atl_types_TupleAttribute: "atl_types_TupleType" = None, atl_types_TupleAttribute6: "atl_types_Type" = None):
        self.name = name
        self.atl_types_TupleAttribute = atl_types_TupleAttribute
        self.atl_types_TupleAttribute6 = atl_types_TupleAttribute6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def atl_types_TupleAttribute(self):
        return self.__atl_types_TupleAttribute

    @atl_types_TupleAttribute.setter
    def atl_types_TupleAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_TupleAttribute__atl_types_TupleAttribute", None)
        self.__atl_types_TupleAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atl_types_TupleType"):
                opp_val = getattr(old_value, "atl_types_TupleType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atl_types_TupleType"):
                opp_val = getattr(value, "atl_types_TupleType", None)
                if opp_val is None:
                    setattr(value, "atl_types_TupleType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def atl_types_TupleAttribute6(self):
        return self.__atl_types_TupleAttribute6

    @atl_types_TupleAttribute6.setter
    def atl_types_TupleAttribute6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atl_types_TupleAttribute__atl_types_TupleAttribute6", None)
        self.__atl_types_TupleAttribute6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atl_types_Type7"):
                opp_val = getattr(old_value, "atl_types_Type7", None)
                if opp_val == self:
                    setattr(old_value, "atl_types_Type7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atl_types_Type7"):
                opp_val = getattr(value, "atl_types_Type7", None)
                setattr(value, "atl_types_Type7", self)
