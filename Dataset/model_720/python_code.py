from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConstraintType(Enum):
    inv = "inv"
    pre = "pre"
    post = "post"
class ConstraintLanguage(Enum):
    kermeta = "kermeta"
    ocl = "ocl"


############################################
# Definition of Classes
############################################

class structure_ModelTypeVariable:

    pass
class ObjectTypeVariable:

    pass
class kermeta_structure_VirtualType(ObjectTypeVariable):

    pass
class structure_VirtualType:

    pass
class TypeVariable:

    pass
class kermeta_structure_ModelTypeVariable(TypeVariable):

    pass
class kermeta_structure_ObjectTypeVariable(TypeVariable):

    pass
class structure_TypeVariableBinding:

    pass
class Type:

    pass
class kermeta_structure_VoidType(Type):

    pass
class kermeta_structure_ParameterizedType(Type):

    pass
class TypeDefinition:

    pass
class kermeta_structure_GenericTypeDefinition(TypeDefinition):

    pass
class structure_Filter:

    pass
class structure_ModelingUnit:

    pass
class structure_Using:

    pass
class structure_Require:

    pass
class structure_GenericTypeDefinition:

    pass
class structure_DataType:

    pass
class structure_TypeDefinitionContainer:

    pass
class structure_NamedElement:

    pass
class kermeta_structure_Package(structure_NamedElement, structure_TypeDefinitionContainer):

    def __init__(self, uri: str, structure120: set["structure_Package"] = None, structure123: "structure_Package" = None):
        self.uri = uri
        self.structure120 = structure120 if structure120 is not None else set()
        self.structure123 = structure123
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def structure120(self):
        return self.__structure120

    @structure120.setter
    def structure120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Package__structure120", None)
        self.__structure120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "language121"):
                    opp_val = getattr(item, "language121", None)
                    
                    if opp_val == self:
                        setattr(item, "language121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "language121"):
                    opp_val = getattr(item, "language121", None)
                    
                    setattr(item, "language121", self)
                    

    @property
    def structure123(self):
        return self.__structure123

    @structure123.setter
    def structure123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Package__structure123", None)
        self.__structure123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "language124"):
                opp_val = getattr(old_value, "language124", None)
                if opp_val == self:
                    setattr(old_value, "language124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "language124"):
                opp_val = getattr(value, "language124", None)
                setattr(value, "language124", self)

class DataType:

    pass
class kermeta_structure_Enumeration(DataType):

    pass
class structure_Package:

    pass
class TypedElement:

    pass
class kermeta_structure_MultiplicityElement(TypedElement):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

class structure_Enumeration:

    pass
class NamedElement:

    pass
class kermeta_structure_TypeDefinition(NamedElement):

    def __init__(self, isAspect: str):
        self.isAspect = isAspect
        
    @property
    def isAspect(self) -> str:
        return self.__isAspect

    @isAspect.setter
    def isAspect(self, isAspect: str):
        self.__isAspect = isAspect

class kermeta_structure_Constraint(NamedElement):

    def __init__(self, stereotype: str, language: str, kermeta_structure_Constraint: "behavior_Expression" = None, structure138: "structure_ClassDefinition" = None, structure141: "structure_Operation" = None, structure144: "structure_Operation" = None):
        self.stereotype = stereotype
        self.language = language
        self.kermeta_structure_Constraint = kermeta_structure_Constraint
        self.structure138 = structure138
        self.structure141 = structure141
        self.structure144 = structure144
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def stereotype(self) -> str:
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype

    @property
    def kermeta_structure_Constraint(self):
        return self.__kermeta_structure_Constraint

    @kermeta_structure_Constraint.setter
    def kermeta_structure_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Constraint__kermeta_structure_Constraint", None)
        self.__kermeta_structure_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression136"):
                opp_val = getattr(old_value, "behavior_Expression136", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression136"):
                opp_val = getattr(value, "behavior_Expression136", None)
                setattr(value, "behavior_Expression136", self)

    @property
    def structure144(self):
        return self.__structure144

    @structure144.setter
    def structure144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Constraint__structure144", None)
        self.__structure144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "language145"):
                opp_val = getattr(old_value, "language145", None)
                if opp_val == self:
                    setattr(old_value, "language145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "language145"):
                opp_val = getattr(value, "language145", None)
                setattr(value, "language145", self)

    @property
    def structure138(self):
        return self.__structure138

    @structure138.setter
    def structure138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Constraint__structure138", None)
        self.__structure138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "language139"):
                opp_val = getattr(old_value, "language139", None)
                if opp_val == self:
                    setattr(old_value, "language139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "language139"):
                opp_val = getattr(value, "language139", None)
                setattr(value, "language139", self)

    @property
    def structure141(self):
        return self.__structure141

    @structure141.setter
    def structure141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Constraint__structure141", None)
        self.__structure141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "language142"):
                opp_val = getattr(old_value, "language142", None)
                if opp_val == self:
                    setattr(old_value, "language142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "language142"):
                opp_val = getattr(value, "language142", None)
                setattr(value, "language142", self)

class kermeta_structure_TypeDefinitionContainer(NamedElement):

    pass
class kermeta_structure_EnumerationLiteral(NamedElement):

    pass
class structure_TypeVariable:

    pass
class structure_ClassDefinition:

    pass
class structure_Parameter:

    pass
class structure_TypeDefinition:

    pass
class structure_Constraint:

    pass
class structure_Tag:

    pass
class kermeta_structure_Object:

    pass
class structure_Class:

    pass
class ParameterizedType:

    pass
class kermeta_structure_Class(ParameterizedType):

    def __init__(self, isAbstract: str, name: str, kermeta_structure_Class: set["structure_Property"] = None, kermeta_structure_Class61: set["structure_Operation"] = None, kermeta_structure_Class64: set["structure_Class"] = None):
        self.isAbstract = isAbstract
        self.name = name
        self.kermeta_structure_Class = kermeta_structure_Class if kermeta_structure_Class is not None else set()
        self.kermeta_structure_Class61 = kermeta_structure_Class61 if kermeta_structure_Class61 is not None else set()
        self.kermeta_structure_Class64 = kermeta_structure_Class64 if kermeta_structure_Class64 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kermeta_structure_Class64(self):
        return self.__kermeta_structure_Class64

    @kermeta_structure_Class64.setter
    def kermeta_structure_Class64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Class__kermeta_structure_Class64", None)
        self.__kermeta_structure_Class64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Class"):
                    opp_val = getattr(item, "structure_Class", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Class"):
                    opp_val = getattr(item, "structure_Class", None)
                    
                    setattr(item, "structure_Class", self)
                    

    @property
    def kermeta_structure_Class(self):
        return self.__kermeta_structure_Class

    @kermeta_structure_Class.setter
    def kermeta_structure_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Class__kermeta_structure_Class", None)
        self.__kermeta_structure_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Property59"):
                    opp_val = getattr(item, "structure_Property59", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Property59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Property59"):
                    opp_val = getattr(item, "structure_Property59", None)
                    
                    setattr(item, "structure_Property59", self)
                    

    @property
    def kermeta_structure_Class61(self):
        return self.__kermeta_structure_Class61

    @kermeta_structure_Class61.setter
    def kermeta_structure_Class61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Class__kermeta_structure_Class61", None)
        self.__kermeta_structure_Class61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Operation62"):
                    opp_val = getattr(item, "structure_Operation62", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Operation62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Operation62"):
                    opp_val = getattr(item, "structure_Operation62", None)
                    
                    setattr(item, "structure_Operation62", self)
                    

    def _new(self) -> str:
        # TODO: Implement _new method
        pass

class Literal:

    pass
class kermeta_behavior_VoidLiteral(Literal):

    pass
class kermeta_behavior_TypeLiteral(Literal):

    pass
class kermeta_behavior_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class kermeta_behavior_BooleanLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class kermeta_behavior_IntegerLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class behavior_LambdaParameter:

    pass
class MultiplicityElement:

    pass
class kermeta_structure_Property(MultiplicityElement):

    def __init__(self, isReadOnly: str, default: str, isComposite: str, isDerived: str, isID: str, isGetterAbstract: str, isSetterAbstract: str, kermeta_structure_Property: "structure_Property" = None, kermeta_structure_Property94: "behavior_Expression" = None, kermeta_structure_Property97: "behavior_Expression" = None, structure100: "structure_ClassDefinition" = None):
        self.isReadOnly = isReadOnly
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.isGetterAbstract = isGetterAbstract
        self.isSetterAbstract = isSetterAbstract
        self.kermeta_structure_Property = kermeta_structure_Property
        self.kermeta_structure_Property94 = kermeta_structure_Property94
        self.kermeta_structure_Property97 = kermeta_structure_Property97
        self.structure100 = structure100
        
    @property
    def isID(self) -> str:
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def isSetterAbstract(self) -> str:
        return self.__isSetterAbstract

    @isSetterAbstract.setter
    def isSetterAbstract(self, isSetterAbstract: str):
        self.__isSetterAbstract = isSetterAbstract

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def isGetterAbstract(self) -> str:
        return self.__isGetterAbstract

    @isGetterAbstract.setter
    def isGetterAbstract(self, isGetterAbstract: str):
        self.__isGetterAbstract = isGetterAbstract

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def structure100(self):
        return self.__structure100

    @structure100.setter
    def structure100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Property__structure100", None)
        self.__structure100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "language101"):
                opp_val = getattr(old_value, "language101", None)
                if opp_val == self:
                    setattr(old_value, "language101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "language101"):
                opp_val = getattr(value, "language101", None)
                setattr(value, "language101", self)

    @property
    def kermeta_structure_Property94(self):
        return self.__kermeta_structure_Property94

    @kermeta_structure_Property94.setter
    def kermeta_structure_Property94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Property__kermeta_structure_Property94", None)
        self.__kermeta_structure_Property94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression95"):
                opp_val = getattr(old_value, "behavior_Expression95", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression95"):
                opp_val = getattr(value, "behavior_Expression95", None)
                setattr(value, "behavior_Expression95", self)

    @property
    def kermeta_structure_Property97(self):
        return self.__kermeta_structure_Property97

    @kermeta_structure_Property97.setter
    def kermeta_structure_Property97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Property__kermeta_structure_Property97", None)
        self.__kermeta_structure_Property97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression98"):
                opp_val = getattr(old_value, "behavior_Expression98", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression98"):
                opp_val = getattr(value, "behavior_Expression98", None)
                setattr(value, "behavior_Expression98", self)

    @property
    def kermeta_structure_Property(self):
        return self.__kermeta_structure_Property

    @kermeta_structure_Property.setter
    def kermeta_structure_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Property__kermeta_structure_Property", None)
        self.__kermeta_structure_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Property92"):
                opp_val = getattr(old_value, "structure_Property92", None)
                if opp_val == self:
                    setattr(old_value, "structure_Property92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Property92"):
                opp_val = getattr(value, "structure_Property92", None)
                setattr(value, "structure_Property92", self)

class kermeta_structure_Parameter(MultiplicityElement):

    pass
class kermeta_structure_Operation(MultiplicityElement):

    def __init__(self, isAbstract: str, structure75: set["structure_Constraint"] = None, kermeta_structure_Operation: set["structure_Type"] = None, structure72: set["structure_Parameter"] = None, structure78: set["structure_Constraint"] = None, kermeta_structure_Operation81: "behavior_Expression" = None, kermeta_structure_Operation84: "structure_Operation" = None, structure87: "structure_ClassDefinition" = None, kermeta_structure_Operation90: set["structure_TypeVariable"] = None):
        self.isAbstract = isAbstract
        self.structure75 = structure75 if structure75 is not None else set()
        self.kermeta_structure_Operation = kermeta_structure_Operation if kermeta_structure_Operation is not None else set()
        self.structure72 = structure72 if structure72 is not None else set()
        self.structure78 = structure78 if structure78 is not None else set()
        self.kermeta_structure_Operation81 = kermeta_structure_Operation81
        self.kermeta_structure_Operation84 = kermeta_structure_Operation84
        self.structure87 = structure87
        self.kermeta_structure_Operation90 = kermeta_structure_Operation90 if kermeta_structure_Operation90 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def structure78(self):
        return self.__structure78

    @structure78.setter
    def structure78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__structure78", None)
        self.__structure78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "language79"):
                    opp_val = getattr(item, "language79", None)
                    
                    if opp_val == self:
                        setattr(item, "language79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "language79"):
                    opp_val = getattr(item, "language79", None)
                    
                    setattr(item, "language79", self)
                    

    @property
    def kermeta_structure_Operation84(self):
        return self.__kermeta_structure_Operation84

    @kermeta_structure_Operation84.setter
    def kermeta_structure_Operation84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__kermeta_structure_Operation84", None)
        self.__kermeta_structure_Operation84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Operation85"):
                opp_val = getattr(old_value, "structure_Operation85", None)
                if opp_val == self:
                    setattr(old_value, "structure_Operation85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Operation85"):
                opp_val = getattr(value, "structure_Operation85", None)
                setattr(value, "structure_Operation85", self)

    @property
    def kermeta_structure_Operation90(self):
        return self.__kermeta_structure_Operation90

    @kermeta_structure_Operation90.setter
    def kermeta_structure_Operation90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__kermeta_structure_Operation90", None)
        self.__kermeta_structure_Operation90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_TypeVariable"):
                    opp_val = getattr(item, "structure_TypeVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_TypeVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_TypeVariable"):
                    opp_val = getattr(item, "structure_TypeVariable", None)
                    
                    setattr(item, "structure_TypeVariable", self)
                    

    @property
    def kermeta_structure_Operation(self):
        return self.__kermeta_structure_Operation

    @kermeta_structure_Operation.setter
    def kermeta_structure_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__kermeta_structure_Operation", None)
        self.__kermeta_structure_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type70"):
                    opp_val = getattr(item, "structure_Type70", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type70"):
                    opp_val = getattr(item, "structure_Type70", None)
                    
                    setattr(item, "structure_Type70", self)
                    

    @property
    def kermeta_structure_Operation81(self):
        return self.__kermeta_structure_Operation81

    @kermeta_structure_Operation81.setter
    def kermeta_structure_Operation81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__kermeta_structure_Operation81", None)
        self.__kermeta_structure_Operation81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression82"):
                opp_val = getattr(old_value, "behavior_Expression82", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression82"):
                opp_val = getattr(value, "behavior_Expression82", None)
                setattr(value, "behavior_Expression82", self)

    @property
    def structure87(self):
        return self.__structure87

    @structure87.setter
    def structure87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__structure87", None)
        self.__structure87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "language88"):
                opp_val = getattr(old_value, "language88", None)
                if opp_val == self:
                    setattr(old_value, "language88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "language88"):
                opp_val = getattr(value, "language88", None)
                setattr(value, "language88", self)

    @property
    def structure72(self):
        return self.__structure72

    @structure72.setter
    def structure72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__structure72", None)
        self.__structure72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "language73"):
                    opp_val = getattr(item, "language73", None)
                    
                    if opp_val == self:
                        setattr(item, "language73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "language73"):
                    opp_val = getattr(item, "language73", None)
                    
                    setattr(item, "language73", self)
                    

    @property
    def structure75(self):
        return self.__structure75

    @structure75.setter
    def structure75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__structure75", None)
        self.__structure75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "language76"):
                    opp_val = getattr(item, "language76", None)
                    
                    if opp_val == self:
                        setattr(item, "language76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "language76"):
                    opp_val = getattr(item, "language76", None)
                    
                    setattr(item, "language76", self)
                    

class kermeta_behavior_TypeReference(MultiplicityElement):

    pass
class behavior_TypeReference:

    pass
class Object:

    pass
class kermeta_structure_Tag(Object):

    def __init__(self, name: str, value: str, structure133: set["structure_Object"] = None):
        self.name = name
        self.value = value
        self.structure133 = structure133 if structure133 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def structure133(self):
        return self.__structure133

    @structure133.setter
    def structure133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Tag__structure133", None)
        self.__structure133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "language134"):
                    opp_val = getattr(item, "language134", None)
                    
                    if opp_val == self:
                        setattr(item, "language134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "language134"):
                    opp_val = getattr(item, "language134", None)
                    
                    setattr(item, "language134", self)
                    

class kermeta_structure_TypeContainer(Object):

    pass
class kermeta_structure_Type(Object):

    pass
class kermeta_behavior_LambdaParameter(Object):

    def __init__(self, name: str, kermeta_behavior_LambdaParameter: "behavior_TypeReference" = None):
        self.name = name
        self.kermeta_behavior_LambdaParameter = kermeta_behavior_LambdaParameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kermeta_behavior_LambdaParameter(self):
        return self.__kermeta_behavior_LambdaParameter

    @kermeta_behavior_LambdaParameter.setter
    def kermeta_behavior_LambdaParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_LambdaParameter__kermeta_behavior_LambdaParameter", None)
        self.__kermeta_behavior_LambdaParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_TypeReference42"):
                opp_val = getattr(old_value, "behavior_TypeReference42", None)
                if opp_val == self:
                    setattr(old_value, "behavior_TypeReference42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_TypeReference42"):
                opp_val = getattr(value, "behavior_TypeReference42", None)
                setattr(value, "behavior_TypeReference42", self)

class kermeta_structure_Using(Object):

    def __init__(self, qualifiedName: str):
        self.qualifiedName = qualifiedName
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

class kermeta_structure_Filter(Object):

    def __init__(self, qualifiedName: str):
        self.qualifiedName = qualifiedName
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

class kermeta_structure_ModelingUnit(Object):

    pass
class kermeta_structure_NamedElement(Object):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class kermeta_structure_Model(Object):

    pass
class kermeta_structure_Require(Object):

    def __init__(self, uri: str):
        self.uri = uri
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class kermeta_behavior_Rescue(Object):

    def __init__(self, exceptionName: str, kermeta_behavior_Rescue: set["behavior_Expression"] = None, kermeta_behavior_Rescue34: "behavior_TypeReference" = None):
        self.exceptionName = exceptionName
        self.kermeta_behavior_Rescue = kermeta_behavior_Rescue if kermeta_behavior_Rescue is not None else set()
        self.kermeta_behavior_Rescue34 = kermeta_behavior_Rescue34
        
    @property
    def exceptionName(self) -> str:
        return self.__exceptionName

    @exceptionName.setter
    def exceptionName(self, exceptionName: str):
        self.__exceptionName = exceptionName

    @property
    def kermeta_behavior_Rescue(self):
        return self.__kermeta_behavior_Rescue

    @kermeta_behavior_Rescue.setter
    def kermeta_behavior_Rescue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_Rescue__kermeta_behavior_Rescue", None)
        self.__kermeta_behavior_Rescue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Expression32"):
                    opp_val = getattr(item, "behavior_Expression32", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Expression32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Expression32"):
                    opp_val = getattr(item, "behavior_Expression32", None)
                    
                    setattr(item, "behavior_Expression32", self)
                    

    @property
    def kermeta_behavior_Rescue34(self):
        return self.__kermeta_behavior_Rescue34

    @kermeta_behavior_Rescue34.setter
    def kermeta_behavior_Rescue34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_Rescue__kermeta_behavior_Rescue34", None)
        self.__kermeta_behavior_Rescue34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_TypeReference"):
                opp_val = getattr(old_value, "behavior_TypeReference", None)
                if opp_val == self:
                    setattr(old_value, "behavior_TypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_TypeReference"):
                opp_val = getattr(value, "behavior_TypeReference", None)
                setattr(value, "behavior_TypeReference", self)

class CallVariable:

    pass
class kermeta_behavior_CallResult(CallVariable):

    pass
class structure_EnumerationLiteral:

    pass
class structure_Property:

    pass
class CallExpression:

    pass
class kermeta_behavior_CallFeature(CallExpression):

    def __init__(self, isAtpre: str, kermeta_behavior_CallFeature18: "structure_Operation" = None, kermeta_behavior_CallFeature: "behavior_Expression" = None, kermeta_behavior_CallFeature16: "structure_Property" = None, kermeta_behavior_CallFeature20: "structure_EnumerationLiteral" = None):
        self.isAtpre = isAtpre
        self.kermeta_behavior_CallFeature18 = kermeta_behavior_CallFeature18
        self.kermeta_behavior_CallFeature = kermeta_behavior_CallFeature
        self.kermeta_behavior_CallFeature16 = kermeta_behavior_CallFeature16
        self.kermeta_behavior_CallFeature20 = kermeta_behavior_CallFeature20
        
    @property
    def isAtpre(self) -> str:
        return self.__isAtpre

    @isAtpre.setter
    def isAtpre(self, isAtpre: str):
        self.__isAtpre = isAtpre

    @property
    def kermeta_behavior_CallFeature16(self):
        return self.__kermeta_behavior_CallFeature16

    @kermeta_behavior_CallFeature16.setter
    def kermeta_behavior_CallFeature16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_CallFeature__kermeta_behavior_CallFeature16", None)
        self.__kermeta_behavior_CallFeature16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Property"):
                opp_val = getattr(old_value, "structure_Property", None)
                if opp_val == self:
                    setattr(old_value, "structure_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Property"):
                opp_val = getattr(value, "structure_Property", None)
                setattr(value, "structure_Property", self)

    @property
    def kermeta_behavior_CallFeature18(self):
        return self.__kermeta_behavior_CallFeature18

    @kermeta_behavior_CallFeature18.setter
    def kermeta_behavior_CallFeature18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_CallFeature__kermeta_behavior_CallFeature18", None)
        self.__kermeta_behavior_CallFeature18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Operation"):
                opp_val = getattr(old_value, "structure_Operation", None)
                if opp_val == self:
                    setattr(old_value, "structure_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Operation"):
                opp_val = getattr(value, "structure_Operation", None)
                setattr(value, "structure_Operation", self)

    @property
    def kermeta_behavior_CallFeature(self):
        return self.__kermeta_behavior_CallFeature

    @kermeta_behavior_CallFeature.setter
    def kermeta_behavior_CallFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_CallFeature__kermeta_behavior_CallFeature", None)
        self.__kermeta_behavior_CallFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression14"):
                opp_val = getattr(old_value, "behavior_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression14"):
                opp_val = getattr(value, "behavior_Expression14", None)
                setattr(value, "behavior_Expression14", self)

    @property
    def kermeta_behavior_CallFeature20(self):
        return self.__kermeta_behavior_CallFeature20

    @kermeta_behavior_CallFeature20.setter
    def kermeta_behavior_CallFeature20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_CallFeature__kermeta_behavior_CallFeature20", None)
        self.__kermeta_behavior_CallFeature20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_EnumerationLiteral"):
                opp_val = getattr(old_value, "structure_EnumerationLiteral", None)
                if opp_val == self:
                    setattr(old_value, "structure_EnumerationLiteral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_EnumerationLiteral"):
                opp_val = getattr(value, "structure_EnumerationLiteral", None)
                setattr(value, "structure_EnumerationLiteral", self)

class kermeta_behavior_CallSuperOperation(CallExpression):

    pass
class kermeta_behavior_CallValue(CallExpression):

    pass
class kermeta_behavior_CallVariable(CallExpression):

    def __init__(self, isAtpre: str):
        self.isAtpre = isAtpre
        
    @property
    def isAtpre(self) -> str:
        return self.__isAtpre

    @isAtpre.setter
    def isAtpre(self, isAtpre: str):
        self.__isAtpre = isAtpre

class structure_Operation:

    pass
class behavior_Rescue:

    pass
class behavior_Expression:

    pass
class behavior_CallExpression:

    pass
class Expression:

    pass
class kermeta_behavior_EmptyExpression(Expression):

    pass
class kermeta_behavior_Literal(Expression):

    pass
class kermeta_behavior_VariableDecl(Expression):

    def __init__(self, identifier: str, kermeta_behavior_VariableDecl: "behavior_Expression" = None, kermeta_behavior_VariableDecl56: "behavior_TypeReference" = None):
        self.identifier = identifier
        self.kermeta_behavior_VariableDecl = kermeta_behavior_VariableDecl
        self.kermeta_behavior_VariableDecl56 = kermeta_behavior_VariableDecl56
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def kermeta_behavior_VariableDecl(self):
        return self.__kermeta_behavior_VariableDecl

    @kermeta_behavior_VariableDecl.setter
    def kermeta_behavior_VariableDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_VariableDecl__kermeta_behavior_VariableDecl", None)
        self.__kermeta_behavior_VariableDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression54"):
                opp_val = getattr(old_value, "behavior_Expression54", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression54"):
                opp_val = getattr(value, "behavior_Expression54", None)
                setattr(value, "behavior_Expression54", self)

    @property
    def kermeta_behavior_VariableDecl56(self):
        return self.__kermeta_behavior_VariableDecl56

    @kermeta_behavior_VariableDecl56.setter
    def kermeta_behavior_VariableDecl56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_VariableDecl__kermeta_behavior_VariableDecl56", None)
        self.__kermeta_behavior_VariableDecl56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_TypeReference57"):
                opp_val = getattr(old_value, "behavior_TypeReference57", None)
                if opp_val == self:
                    setattr(old_value, "behavior_TypeReference57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_TypeReference57"):
                opp_val = getattr(value, "behavior_TypeReference57", None)
                setattr(value, "behavior_TypeReference57", self)

class kermeta_behavior_Raise(Expression):

    pass
class kermeta_behavior_CallExpression(Expression):

    def __init__(self, name: str, kermeta_behavior_CallExpression: set["behavior_Expression"] = None, kermeta_behavior_CallExpression7: set["structure_Type"] = None):
        self.name = name
        self.kermeta_behavior_CallExpression = kermeta_behavior_CallExpression if kermeta_behavior_CallExpression is not None else set()
        self.kermeta_behavior_CallExpression7 = kermeta_behavior_CallExpression7 if kermeta_behavior_CallExpression7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kermeta_behavior_CallExpression(self):
        return self.__kermeta_behavior_CallExpression

    @kermeta_behavior_CallExpression.setter
    def kermeta_behavior_CallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_CallExpression__kermeta_behavior_CallExpression", None)
        self.__kermeta_behavior_CallExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Expression5"):
                    opp_val = getattr(item, "behavior_Expression5", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Expression5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Expression5"):
                    opp_val = getattr(item, "behavior_Expression5", None)
                    
                    setattr(item, "behavior_Expression5", self)
                    

    @property
    def kermeta_behavior_CallExpression7(self):
        return self.__kermeta_behavior_CallExpression7

    @kermeta_behavior_CallExpression7.setter
    def kermeta_behavior_CallExpression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_CallExpression__kermeta_behavior_CallExpression7", None)
        self.__kermeta_behavior_CallExpression7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type8"):
                    opp_val = getattr(item, "structure_Type8", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type8"):
                    opp_val = getattr(item, "structure_Type8", None)
                    
                    setattr(item, "structure_Type8", self)
                    

class kermeta_behavior_Loop(Expression):

    pass
class kermeta_behavior_SelfExpression(Expression):

    pass
class kermeta_behavior_Block(Expression):

    pass
class kermeta_behavior_JavaStaticCall(Expression):

    def __init__(self, jclass: str, jmethod: str, kermeta_behavior_JavaStaticCall: set["behavior_Expression"] = None):
        self.jclass = jclass
        self.jmethod = jmethod
        self.kermeta_behavior_JavaStaticCall = kermeta_behavior_JavaStaticCall if kermeta_behavior_JavaStaticCall is not None else set()
        
    @property
    def jmethod(self) -> str:
        return self.__jmethod

    @jmethod.setter
    def jmethod(self, jmethod: str):
        self.__jmethod = jmethod

    @property
    def jclass(self) -> str:
        return self.__jclass

    @jclass.setter
    def jclass(self, jclass: str):
        self.__jclass = jclass

    @property
    def kermeta_behavior_JavaStaticCall(self):
        return self.__kermeta_behavior_JavaStaticCall

    @kermeta_behavior_JavaStaticCall.setter
    def kermeta_behavior_JavaStaticCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_JavaStaticCall__kermeta_behavior_JavaStaticCall", None)
        self.__kermeta_behavior_JavaStaticCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Expression36"):
                    opp_val = getattr(item, "behavior_Expression36", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Expression36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Expression36"):
                    opp_val = getattr(item, "behavior_Expression36", None)
                    
                    setattr(item, "behavior_Expression36", self)
                    

class kermeta_behavior_LambdaExpression(Expression):

    pass
class kermeta_behavior_Conditional(Expression):

    pass
class kermeta_behavior_Assignment(Expression):

    def __init__(self, isCast: str, kermeta_behavior_Assignment: "behavior_CallExpression" = None, kermeta_behavior_Assignment2: "behavior_Expression" = None):
        self.isCast = isCast
        self.kermeta_behavior_Assignment = kermeta_behavior_Assignment
        self.kermeta_behavior_Assignment2 = kermeta_behavior_Assignment2
        
    @property
    def isCast(self) -> str:
        return self.__isCast

    @isCast.setter
    def isCast(self, isCast: str):
        self.__isCast = isCast

    @property
    def kermeta_behavior_Assignment(self):
        return self.__kermeta_behavior_Assignment

    @kermeta_behavior_Assignment.setter
    def kermeta_behavior_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_Assignment__kermeta_behavior_Assignment", None)
        self.__kermeta_behavior_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_CallExpression"):
                opp_val = getattr(old_value, "behavior_CallExpression", None)
                if opp_val == self:
                    setattr(old_value, "behavior_CallExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_CallExpression"):
                opp_val = getattr(value, "behavior_CallExpression", None)
                setattr(value, "behavior_CallExpression", self)

    @property
    def kermeta_behavior_Assignment2(self):
        return self.__kermeta_behavior_Assignment2

    @kermeta_behavior_Assignment2.setter
    def kermeta_behavior_Assignment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_behavior_Assignment__kermeta_behavior_Assignment2", None)
        self.__kermeta_behavior_Assignment2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression"):
                opp_val = getattr(old_value, "behavior_Expression", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression"):
                opp_val = getattr(value, "behavior_Expression", None)
                setattr(value, "behavior_Expression", self)

class kermeta_language_DummyClass(ABC):

    pass
class kermeta_DummyClass(ABC):

    pass
class structure_Type:

    pass
class kermeta_structure_ModelType(structure_TypeDefinition, structure_Type):

    def __init__(self, kermeta_structure_ModelType: set["structure_TypeDefinition"] = None, structure_Type131: "kermeta_structure_TypedElement", structure_Type192: "kermeta_structure_FunctionType", structure_Type115: "kermeta_structure_TypeVariableBinding", structure_Type8: "kermeta_behavior_CallExpression", structure_Type195: "kermeta_structure_FunctionType", language107: "kermeta_structure_TypeContainer", structure_Type70: "kermeta_structure_Operation", structure_Type178: "kermeta_structure_TypeVariable", structure_Type129: "kermeta_structure_PrimitiveType", structure_Type190: "kermeta_structure_ProductType", structure_Type156: "kermeta_structure_ClassDefinition", structure_Type: "kermeta_behavior_Expression", structure_TypeDefinition: "kermeta_structure_ModelType", structure_TypeDefinition197: "kermeta_structure_TypeDefinitionContainer"):
        self.kermeta_structure_ModelType = kermeta_structure_ModelType if kermeta_structure_ModelType is not None else set()
        
    @property
    def kermeta_structure_ModelType(self):
        return self.__kermeta_structure_ModelType

    @kermeta_structure_ModelType.setter
    def kermeta_structure_ModelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_ModelType__kermeta_structure_ModelType", None)
        self.__kermeta_structure_ModelType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_TypeDefinition"):
                    opp_val = getattr(item, "structure_TypeDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_TypeDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_TypeDefinition"):
                    opp_val = getattr(item, "structure_TypeDefinition", None)
                    
                    setattr(item, "structure_TypeDefinition", self)
                    

    def _new(self) -> str:
        # TODO: Implement _new method
        pass

class kermeta_structure_DataType(structure_TypeDefinition, structure_Type):

    pass
class structure_TypeContainer:

    pass
class kermeta_structure_PrimitiveType(structure_DataType, structure_TypeContainer):

    pass
class kermeta_structure_TypeVariable(structure_NamedElement, structure_TypeContainer, structure_Type):

    pass
class kermeta_structure_ClassDefinition(structure_GenericTypeDefinition, structure_TypeContainer):

    def __init__(self, isAbstract: str, structure147: set["structure_Constraint"] = None, structure150: set["structure_Property"] = None, structure153: set["structure_Operation"] = None, kermeta_structure_ClassDefinition: set["structure_Type"] = None, language104: "kermeta_structure_Type", structure_GenericTypeDefinition: "kermeta_structure_ParameterizedType"):
        self.isAbstract = isAbstract
        self.structure147 = structure147 if structure147 is not None else set()
        self.structure150 = structure150 if structure150 is not None else set()
        self.structure153 = structure153 if structure153 is not None else set()
        self.kermeta_structure_ClassDefinition = kermeta_structure_ClassDefinition if kermeta_structure_ClassDefinition is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def structure147(self):
        return self.__structure147

    @structure147.setter
    def structure147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_ClassDefinition__structure147", None)
        self.__structure147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "language148"):
                    opp_val = getattr(item, "language148", None)
                    
                    if opp_val == self:
                        setattr(item, "language148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "language148"):
                    opp_val = getattr(item, "language148", None)
                    
                    setattr(item, "language148", self)
                    

    @property
    def structure153(self):
        return self.__structure153

    @structure153.setter
    def structure153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_ClassDefinition__structure153", None)
        self.__structure153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "language154"):
                    opp_val = getattr(item, "language154", None)
                    
                    if opp_val == self:
                        setattr(item, "language154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "language154"):
                    opp_val = getattr(item, "language154", None)
                    
                    setattr(item, "language154", self)
                    

    @property
    def structure150(self):
        return self.__structure150

    @structure150.setter
    def structure150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_ClassDefinition__structure150", None)
        self.__structure150 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "language151"):
                    opp_val = getattr(item, "language151", None)
                    
                    if opp_val == self:
                        setattr(item, "language151", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "language151"):
                    opp_val = getattr(item, "language151", None)
                    
                    setattr(item, "language151", self)
                    

    @property
    def kermeta_structure_ClassDefinition(self):
        return self.__kermeta_structure_ClassDefinition

    @kermeta_structure_ClassDefinition.setter
    def kermeta_structure_ClassDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_ClassDefinition__kermeta_structure_ClassDefinition", None)
        self.__kermeta_structure_ClassDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type156"):
                    opp_val = getattr(item, "structure_Type156", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type156"):
                    opp_val = getattr(item, "structure_Type156", None)
                    
                    setattr(item, "structure_Type156", self)
                    

class kermeta_structure_FunctionType(structure_TypeContainer, structure_Type):

    pass
class kermeta_structure_ProductType(structure_TypeContainer, structure_Type):

    pass
class kermeta_structure_TypedElement(structure_NamedElement, structure_TypeContainer):

    pass
class structure_Object:

    pass
class kermeta_structure_TypeVariableBinding(structure_TypeContainer, structure_Object):

    pass
class kermeta_behavior_Expression(structure_TypeContainer, structure_Object):

    pass