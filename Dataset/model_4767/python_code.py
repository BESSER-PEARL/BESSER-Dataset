from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class types_MetaModel:

    def __init__(self, name: str, types_MetaModel: "types_Metaclass" = None):
        self.name = name
        self.types_MetaModel = types_MetaModel
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_MetaModel(self):
        return self.__types_MetaModel

    @types_MetaModel.setter
    def types_MetaModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_MetaModel__types_MetaModel", None)
        self.__types_MetaModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Metaclass20"):
                opp_val = getattr(old_value, "types_Metaclass20", None)
                if opp_val == self:
                    setattr(old_value, "types_Metaclass20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Metaclass20"):
                opp_val = getattr(value, "types_Metaclass20", None)
                setattr(value, "types_Metaclass20", self)

class CollectionType:

    pass
class types_OrderedSetType(CollectionType):

    pass
class types_BagType(CollectionType):

    pass
class types_SetType(CollectionType):

    pass
class types_SequenceType(CollectionType):

    pass
class ReflectiveType:

    pass
class types_ReflectiveClass(ReflectiveType):

    pass
class Type:

    pass
class types_CollectionType(Type):

    pass
class types_ReflectiveType(Type):

    pass
class types_UnionType(Type):

    pass
class types_ThisModuleType(Type):

    pass
class types_OclUndefinedType(Type):

    pass
class types_EnumType(Type):

    def __init__(self, name: str, types_EnumType: "types_EObject" = None):
        self.name = name
        self.types_EnumType = types_EnumType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_EnumType(self):
        return self.__types_EnumType

    @types_EnumType.setter
    def types_EnumType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_EnumType__types_EnumType", None)
        self.__types_EnumType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_EObject15"):
                opp_val = getattr(old_value, "types_EObject15", None)
                if opp_val == self:
                    setattr(old_value, "types_EObject15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_EObject15"):
                opp_val = getattr(value, "types_EObject15", None)
                setattr(value, "types_EObject15", self)

class types_EmptyCollection(Type):

    pass
class types_EClass:

    pass
class EStructuralFeature:

    pass
class types_UnknownFeature(EStructuralFeature):

    pass
class Metaclass:

    pass
class TypeError:

    pass
class types_UnresolvedTypeError(Metaclass, TypeError):

    pass
class types_EObject:

    pass
class types_TypeError(Type):

    pass
class types_EmptyCollectionType(Type):

    pass
class RefType:

    pass
class types_Unknown(RefType):

    pass
class types_RefType(Type):

    pass
class types_MapType(Type):

    pass
class types_TupleAttribute:

    def __init__(self, name: str, types_TupleAttribute: "types_TupleType" = None, types_TupleAttribute10: "types_Type" = None):
        self.name = name
        self.types_TupleAttribute = types_TupleAttribute
        self.types_TupleAttribute10 = types_TupleAttribute10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_TupleAttribute(self):
        return self.__types_TupleAttribute

    @types_TupleAttribute.setter
    def types_TupleAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_TupleAttribute__types_TupleAttribute", None)
        self.__types_TupleAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TupleType"):
                opp_val = getattr(old_value, "types_TupleType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TupleType"):
                opp_val = getattr(value, "types_TupleType", None)
                if opp_val is None:
                    setattr(value, "types_TupleType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_TupleAttribute10(self):
        return self.__types_TupleAttribute10

    @types_TupleAttribute10.setter
    def types_TupleAttribute10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_TupleAttribute__types_TupleAttribute10", None)
        self.__types_TupleAttribute10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Type11"):
                opp_val = getattr(old_value, "types_Type11", None)
                if opp_val == self:
                    setattr(old_value, "types_Type11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Type11"):
                opp_val = getattr(value, "types_Type11", None)
                setattr(value, "types_Type11", self)

class types_TupleType(Type):

    pass
class types_Metaclass(RefType):

    def __init__(self, name: str, explicitOcurrence: bool, types_Metaclass: "types_BooleanType" = None, types_Metaclass17: "types_EClass" = None, types_Metaclass20: "types_MetaModel" = None):
        self.name = name
        self.explicitOcurrence = explicitOcurrence
        self.types_Metaclass = types_Metaclass
        self.types_Metaclass17 = types_Metaclass17
        self.types_Metaclass20 = types_Metaclass20
        
    @property
    def explicitOcurrence(self) -> bool:
        return self.__explicitOcurrence

    @explicitOcurrence.setter
    def explicitOcurrence(self, explicitOcurrence: bool):
        self.__explicitOcurrence = explicitOcurrence

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_Metaclass(self):
        return self.__types_Metaclass

    @types_Metaclass.setter
    def types_Metaclass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Metaclass__types_Metaclass", None)
        self.__types_Metaclass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_BooleanType"):
                opp_val = getattr(old_value, "types_BooleanType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_BooleanType"):
                opp_val = getattr(value, "types_BooleanType", None)
                if opp_val is None:
                    setattr(value, "types_BooleanType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_Metaclass17(self):
        return self.__types_Metaclass17

    @types_Metaclass17.setter
    def types_Metaclass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Metaclass__types_Metaclass17", None)
        self.__types_Metaclass17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_EClass18"):
                opp_val = getattr(old_value, "types_EClass18", None)
                if opp_val == self:
                    setattr(old_value, "types_EClass18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_EClass18"):
                opp_val = getattr(value, "types_EClass18", None)
                setattr(value, "types_EClass18", self)

    @property
    def types_Metaclass20(self):
        return self.__types_Metaclass20

    @types_Metaclass20.setter
    def types_Metaclass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Metaclass__types_Metaclass20", None)
        self.__types_Metaclass20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_MetaModel"):
                opp_val = getattr(old_value, "types_MetaModel", None)
                if opp_val == self:
                    setattr(old_value, "types_MetaModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_MetaModel"):
                opp_val = getattr(value, "types_MetaModel", None)
                setattr(value, "types_MetaModel", self)

class PrimitiveType:

    pass
class types_StringType(PrimitiveType):

    pass
class types_IntegerType(PrimitiveType):

    pass
class types_FloatType(PrimitiveType):

    pass
class types_BooleanType(PrimitiveType):

    pass
class types_PrimitiveType(Type):

    pass
class types_Type(ABC):

    def __init__(self, multivalued: bool, metamodelRef: str, mayBeUndefined: bool, types_Type5: "types_MapType" = None, types_Type8: "types_MapType" = None, types_Type11: "types_TupleAttribute" = None, types_Type: "types_Type" = None, types_Type0: "types_Type" = None, types_Type22: "types_UnionType" = None, types_Type24: "types_CollectionType" = None):
        self.multivalued = multivalued
        self.metamodelRef = metamodelRef
        self.mayBeUndefined = mayBeUndefined
        self.types_Type5 = types_Type5
        self.types_Type8 = types_Type8
        self.types_Type11 = types_Type11
        self.types_Type = types_Type
        self.types_Type0 = types_Type0
        self.types_Type22 = types_Type22
        self.types_Type24 = types_Type24
        
    @property
    def mayBeUndefined(self) -> bool:
        return self.__mayBeUndefined

    @mayBeUndefined.setter
    def mayBeUndefined(self, mayBeUndefined: bool):
        self.__mayBeUndefined = mayBeUndefined

    @property
    def multivalued(self) -> bool:
        return self.__multivalued

    @multivalued.setter
    def multivalued(self, multivalued: bool):
        self.__multivalued = multivalued

    @property
    def metamodelRef(self) -> str:
        return self.__metamodelRef

    @metamodelRef.setter
    def metamodelRef(self, metamodelRef: str):
        self.__metamodelRef = metamodelRef

    @property
    def types_Type5(self):
        return self.__types_Type5

    @types_Type5.setter
    def types_Type5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type5", None)
        self.__types_Type5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_MapType"):
                opp_val = getattr(old_value, "types_MapType", None)
                if opp_val == self:
                    setattr(old_value, "types_MapType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_MapType"):
                opp_val = getattr(value, "types_MapType", None)
                setattr(value, "types_MapType", self)

    @property
    def types_Type0(self):
        return self.__types_Type0

    @types_Type0.setter
    def types_Type0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type0", None)
        self.__types_Type0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Type"):
                opp_val = getattr(old_value, "types_Type", None)
                if opp_val == self:
                    setattr(old_value, "types_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Type"):
                opp_val = getattr(value, "types_Type", None)
                setattr(value, "types_Type", self)

    @property
    def types_Type8(self):
        return self.__types_Type8

    @types_Type8.setter
    def types_Type8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type8", None)
        self.__types_Type8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_MapType7"):
                opp_val = getattr(old_value, "types_MapType7", None)
                if opp_val == self:
                    setattr(old_value, "types_MapType7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_MapType7"):
                opp_val = getattr(value, "types_MapType7", None)
                setattr(value, "types_MapType7", self)

    @property
    def types_Type22(self):
        return self.__types_Type22

    @types_Type22.setter
    def types_Type22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type22", None)
        self.__types_Type22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_UnionType"):
                opp_val = getattr(old_value, "types_UnionType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_UnionType"):
                opp_val = getattr(value, "types_UnionType", None)
                if opp_val is None:
                    setattr(value, "types_UnionType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_Type24(self):
        return self.__types_Type24

    @types_Type24.setter
    def types_Type24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type24", None)
        self.__types_Type24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_CollectionType"):
                opp_val = getattr(old_value, "types_CollectionType", None)
                if opp_val == self:
                    setattr(old_value, "types_CollectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_CollectionType"):
                opp_val = getattr(value, "types_CollectionType", None)
                setattr(value, "types_CollectionType", self)

    @property
    def types_Type11(self):
        return self.__types_Type11

    @types_Type11.setter
    def types_Type11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type11", None)
        self.__types_Type11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TupleAttribute10"):
                opp_val = getattr(old_value, "types_TupleAttribute10", None)
                if opp_val == self:
                    setattr(old_value, "types_TupleAttribute10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TupleAttribute10"):
                opp_val = getattr(value, "types_TupleAttribute10", None)
                setattr(value, "types_TupleAttribute10", self)

    @property
    def types_Type(self):
        return self.__types_Type

    @types_Type.setter
    def types_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Type__types_Type", None)
        self.__types_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Type0"):
                opp_val = getattr(old_value, "types_Type0", None)
                if opp_val == self:
                    setattr(old_value, "types_Type0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Type0"):
                opp_val = getattr(value, "types_Type0", None)
                setattr(value, "types_Type0", self)
