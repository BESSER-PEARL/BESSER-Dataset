from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PropertyStorageModifier(Enum):
    VARIABLE = "VARIABLE"
    VALUE = "VALUE"
    TRANSIENT = "TRANSIENT"
class TypeStorageModifier(Enum):
    STORABLE = "STORABLE"
    EMBEDDABLE = "EMBEDDABLE"
class EntityRelationshipKind(Enum):
    UNIQUE = "UNIQUE"
    MANY = "MANY"


############################################
# Definition of Classes
############################################

class Literal:

    pass
class types_CharLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class types_BooleanLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class types_NumberLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class types_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class types_MappedByReference:

    pass
class types_EntityRelationship:

    def __init__(self, kind: str, types_EntityRelationship: "types_Property" = None, types_EntityRelationship28: "types_MappedByReference" = None):
        self.kind = kind
        self.types_EntityRelationship = types_EntityRelationship
        self.types_EntityRelationship28 = types_EntityRelationship28
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def types_EntityRelationship28(self):
        return self.__types_EntityRelationship28

    @types_EntityRelationship28.setter
    def types_EntityRelationship28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_EntityRelationship__types_EntityRelationship28", None)
        self.__types_EntityRelationship28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_MappedByReference"):
                opp_val = getattr(old_value, "types_MappedByReference", None)
                if opp_val == self:
                    setattr(old_value, "types_MappedByReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_MappedByReference"):
                opp_val = getattr(value, "types_MappedByReference", None)
                setattr(value, "types_MappedByReference", self)

    @property
    def types_EntityRelationship(self):
        return self.__types_EntityRelationship

    @types_EntityRelationship.setter
    def types_EntityRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_EntityRelationship__types_EntityRelationship", None)
        self.__types_EntityRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Property19"):
                opp_val = getattr(old_value, "types_Property19", None)
                if opp_val == self:
                    setattr(old_value, "types_Property19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Property19"):
                opp_val = getattr(value, "types_Property19", None)
                setattr(value, "types_Property19", self)

class types_Property:

    def __init__(self, storageModifier: str, name: str, types_Property19: "types_EntityRelationship" = None, types_Property21: "types_PropertyReference" = None, types_Property23: "types_PropertyReference" = None, types_Property26: "types_Literal" = None, types_Property: "types_EntityType" = None, types_Property17: "types_DeclarationTypeReference" = None, types_Property31: "types_MappedByReference" = None, types_Property37: "types_PropertyReference" = None):
        self.storageModifier = storageModifier
        self.name = name
        self.types_Property19 = types_Property19
        self.types_Property21 = types_Property21
        self.types_Property23 = types_Property23
        self.types_Property26 = types_Property26
        self.types_Property = types_Property
        self.types_Property17 = types_Property17
        self.types_Property31 = types_Property31
        self.types_Property37 = types_Property37
        
    @property
    def storageModifier(self) -> str:
        return self.__storageModifier

    @storageModifier.setter
    def storageModifier(self, storageModifier: str):
        self.__storageModifier = storageModifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_Property23(self):
        return self.__types_Property23

    @types_Property23.setter
    def types_Property23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property23", None)
        self.__types_Property23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_PropertyReference24"):
                opp_val = getattr(old_value, "types_PropertyReference24", None)
                if opp_val == self:
                    setattr(old_value, "types_PropertyReference24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_PropertyReference24"):
                opp_val = getattr(value, "types_PropertyReference24", None)
                setattr(value, "types_PropertyReference24", self)

    @property
    def types_Property26(self):
        return self.__types_Property26

    @types_Property26.setter
    def types_Property26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property26", None)
        self.__types_Property26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Literal"):
                opp_val = getattr(old_value, "types_Literal", None)
                if opp_val == self:
                    setattr(old_value, "types_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Literal"):
                opp_val = getattr(value, "types_Literal", None)
                setattr(value, "types_Literal", self)

    @property
    def types_Property37(self):
        return self.__types_Property37

    @types_Property37.setter
    def types_Property37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property37", None)
        self.__types_Property37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_PropertyReference36"):
                opp_val = getattr(old_value, "types_PropertyReference36", None)
                if opp_val == self:
                    setattr(old_value, "types_PropertyReference36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_PropertyReference36"):
                opp_val = getattr(value, "types_PropertyReference36", None)
                setattr(value, "types_PropertyReference36", self)

    @property
    def types_Property21(self):
        return self.__types_Property21

    @types_Property21.setter
    def types_Property21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property21", None)
        self.__types_Property21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_PropertyReference"):
                opp_val = getattr(old_value, "types_PropertyReference", None)
                if opp_val == self:
                    setattr(old_value, "types_PropertyReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_PropertyReference"):
                opp_val = getattr(value, "types_PropertyReference", None)
                setattr(value, "types_PropertyReference", self)

    @property
    def types_Property(self):
        return self.__types_Property

    @types_Property.setter
    def types_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property", None)
        self.__types_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_EntityType"):
                opp_val = getattr(old_value, "types_EntityType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_EntityType"):
                opp_val = getattr(value, "types_EntityType", None)
                if opp_val is None:
                    setattr(value, "types_EntityType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def types_Property31(self):
        return self.__types_Property31

    @types_Property31.setter
    def types_Property31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property31", None)
        self.__types_Property31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_MappedByReference30"):
                opp_val = getattr(old_value, "types_MappedByReference30", None)
                if opp_val == self:
                    setattr(old_value, "types_MappedByReference30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_MappedByReference30"):
                opp_val = getattr(value, "types_MappedByReference30", None)
                setattr(value, "types_MappedByReference30", self)

    @property
    def types_Property17(self):
        return self.__types_Property17

    @types_Property17.setter
    def types_Property17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property17", None)
        self.__types_Property17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_DeclarationTypeReference"):
                opp_val = getattr(old_value, "types_DeclarationTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "types_DeclarationTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_DeclarationTypeReference"):
                opp_val = getattr(value, "types_DeclarationTypeReference", None)
                setattr(value, "types_DeclarationTypeReference", self)

    @property
    def types_Property19(self):
        return self.__types_Property19

    @types_Property19.setter
    def types_Property19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Property__types_Property19", None)
        self.__types_Property19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_EntityRelationship"):
                opp_val = getattr(old_value, "types_EntityRelationship", None)
                if opp_val == self:
                    setattr(old_value, "types_EntityRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_EntityRelationship"):
                opp_val = getattr(value, "types_EntityRelationship", None)
                setattr(value, "types_EntityRelationship", self)

class types_EnumerationLiteral:

    def __init__(self, name: str, types_EnumerationLiteral: "types_EnumerationType" = None):
        self.name = name
        self.types_EnumerationLiteral = types_EnumerationLiteral
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_EnumerationLiteral(self):
        return self.__types_EnumerationLiteral

    @types_EnumerationLiteral.setter
    def types_EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_EnumerationLiteral__types_EnumerationLiteral", None)
        self.__types_EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_EnumerationType"):
                opp_val = getattr(old_value, "types_EnumerationType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_EnumerationType"):
                opp_val = getattr(value, "types_EnumerationType", None)
                if opp_val is None:
                    setattr(value, "types_EnumerationType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ComplexType:

    pass
class types_EntityType(ComplexType):

    def __init__(self, storageModifier: str, types_EntityType: set["types_Property"] = None):
        self.storageModifier = storageModifier
        self.types_EntityType = types_EntityType if types_EntityType is not None else set()
        
    @property
    def storageModifier(self) -> str:
        return self.__storageModifier

    @storageModifier.setter
    def storageModifier(self, storageModifier: str):
        self.__storageModifier = storageModifier

    @property
    def types_EntityType(self):
        return self.__types_EntityType

    @types_EntityType.setter
    def types_EntityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_EntityType__types_EntityType", None)
        self.__types_EntityType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_Property"):
                    opp_val = getattr(item, "types_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "types_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_Property"):
                    opp_val = getattr(item, "types_Property", None)
                    
                    setattr(item, "types_Property", self)
                    

class types_EnumerationType(ComplexType):

    pass
class NamedType:

    pass
class types_PrimitiveType(NamedType):

    pass
class types_DeclarationTypeReference:

    pass
class types_Literal:

    pass
class types_PropertyReference(Literal):

    pass
class Type:

    pass
class types_NamedType(Type):

    def __init__(self, name: str, types_NamedType: "types_TypeReference" = None):
        self.name = name
        self.types_NamedType = types_NamedType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_NamedType(self):
        return self.__types_NamedType

    @types_NamedType.setter
    def types_NamedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_NamedType__types_NamedType", None)
        self.__types_NamedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TypeReference10"):
                opp_val = getattr(old_value, "types_TypeReference10", None)
                if opp_val == self:
                    setattr(old_value, "types_TypeReference10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypeReference10"):
                opp_val = getattr(value, "types_TypeReference10", None)
                setattr(value, "types_TypeReference10", self)

class types_Type:

    pass
class types_ComplexType(NamedType):

    pass
class types_Import:

    def __init__(self, importedNamespace: str, types_Import: "types_Model" = None):
        self.importedNamespace = importedNamespace
        self.types_Import = types_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def types_Import(self):
        return self.__types_Import

    @types_Import.setter
    def types_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Import__types_Import", None)
        self.__types_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_Model"):
                opp_val = getattr(old_value, "types_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_Model"):
                opp_val = getattr(value, "types_Model", None)
                if opp_val is None:
                    setattr(value, "types_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class types_Model:

    def __init__(self, name: str, types_Model: set["types_Import"] = None, types_Model2: set["types_ComplexType"] = None):
        self.name = name
        self.types_Model = types_Model if types_Model is not None else set()
        self.types_Model2 = types_Model2 if types_Model2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def types_Model(self):
        return self.__types_Model

    @types_Model.setter
    def types_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Model__types_Model", None)
        self.__types_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "types_Import"):
                    opp_val = getattr(item, "types_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "types_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "types_Import"):
                    opp_val = getattr(item, "types_Import", None)
                    
                    setattr(item, "types_Import", self)
                    

    @property
    def types_Model2(self):
        return self.__types_Model2

    @types_Model2.setter
    def types_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_Model__types_Model2", None)
        self.__types_Model2 = value if value is not None else set()
        
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
                    

class DeclarationTypeReference:

    pass
class types_MapType(DeclarationTypeReference, Type):

    def __init__(self, size: int, types_MapType: "types_TypeReference" = None, types_MapType7: "types_TypeReference" = None):
        self.size = size
        self.types_MapType = types_MapType
        self.types_MapType7 = types_MapType7
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def types_MapType(self):
        return self.__types_MapType

    @types_MapType.setter
    def types_MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_MapType__types_MapType", None)
        self.__types_MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TypeReference5"):
                opp_val = getattr(old_value, "types_TypeReference5", None)
                if opp_val == self:
                    setattr(old_value, "types_TypeReference5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypeReference5"):
                opp_val = getattr(value, "types_TypeReference5", None)
                setattr(value, "types_TypeReference5", self)

    @property
    def types_MapType7(self):
        return self.__types_MapType7

    @types_MapType7.setter
    def types_MapType7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_MapType__types_MapType7", None)
        self.__types_MapType7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TypeReference8"):
                opp_val = getattr(old_value, "types_TypeReference8", None)
                if opp_val == self:
                    setattr(old_value, "types_TypeReference8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypeReference8"):
                opp_val = getattr(value, "types_TypeReference8", None)
                setattr(value, "types_TypeReference8", self)

class types_TypeReference(DeclarationTypeReference):

    pass
class types_CollectionType(DeclarationTypeReference, Type):

    def __init__(self, size: int, types_CollectionType: "types_TypeReference" = None):
        self.size = size
        self.types_CollectionType = types_CollectionType
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def types_CollectionType(self):
        return self.__types_CollectionType

    @types_CollectionType.setter
    def types_CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_types_CollectionType__types_CollectionType", None)
        self.__types_CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "types_TypeReference"):
                opp_val = getattr(old_value, "types_TypeReference", None)
                if opp_val == self:
                    setattr(old_value, "types_TypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "types_TypeReference"):
                opp_val = getattr(value, "types_TypeReference", None)
                setattr(value, "types_TypeReference", self)
