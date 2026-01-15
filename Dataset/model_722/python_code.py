from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConstraintLanguage(Enum):
    kermeta = "kermeta"
    ocl = "ocl"
class ConstraintType(Enum):
    inv = "inv"
    pre = "pre"
    post = "post"


############################################
# Definition of Classes
############################################

class structure_Metamodel:

    pass
class TypeDefinition:

    pass
class org_structure_ModelElementTypeDefinition(TypeDefinition):

    pass
class structure_ModelTypeDefinitionBinding:

    pass
class org_structure_ModelTypeDefinition(TypeDefinition):

    pass
class structure_AdaptationParameter:

    pass
class AdaptationOperator:

    pass
class org_structure_OperationAdaptationOperator(AdaptationOperator):

    def __init__(self, body: str, org_structure_OperationAdaptationOperator: "structure_Operation" = None):
        self.body = body
        self.org_structure_OperationAdaptationOperator = org_structure_OperationAdaptationOperator
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def org_structure_OperationAdaptationOperator(self):
        return self.__org_structure_OperationAdaptationOperator

    @org_structure_OperationAdaptationOperator.setter
    def org_structure_OperationAdaptationOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_OperationAdaptationOperator__org_structure_OperationAdaptationOperator", None)
        self.__org_structure_OperationAdaptationOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Operation247"):
                opp_val = getattr(old_value, "structure_Operation247", None)
                if opp_val == self:
                    setattr(old_value, "structure_Operation247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Operation247"):
                opp_val = getattr(value, "structure_Operation247", None)
                setattr(value, "structure_Operation247", self)

class org_structure_PropertyAdaptationOperator(AdaptationOperator):

    def __init__(self, getter: str, setter: str, adder: str, remover: str, org_structure_PropertyAdaptationOperator: "structure_Property" = None):
        self.getter = getter
        self.setter = setter
        self.adder = adder
        self.remover = remover
        self.org_structure_PropertyAdaptationOperator = org_structure_PropertyAdaptationOperator
        
    @property
    def getter(self) -> str:
        return self.__getter

    @getter.setter
    def getter(self, getter: str):
        self.__getter = getter

    @property
    def setter(self) -> str:
        return self.__setter

    @setter.setter
    def setter(self, setter: str):
        self.__setter = setter

    @property
    def adder(self) -> str:
        return self.__adder

    @adder.setter
    def adder(self, adder: str):
        self.__adder = adder

    @property
    def remover(self) -> str:
        return self.__remover

    @remover.setter
    def remover(self, remover: str):
        self.__remover = remover

    @property
    def org_structure_PropertyAdaptationOperator(self):
        return self.__org_structure_PropertyAdaptationOperator

    @org_structure_PropertyAdaptationOperator.setter
    def org_structure_PropertyAdaptationOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_PropertyAdaptationOperator__org_structure_PropertyAdaptationOperator", None)
        self.__org_structure_PropertyAdaptationOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Property245"):
                opp_val = getattr(old_value, "structure_Property245", None)
                if opp_val == self:
                    setattr(old_value, "structure_Property245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Property245"):
                opp_val = getattr(value, "structure_Property245", None)
                setattr(value, "structure_Property245", self)

class structure_ModelTypeDefinition:

    pass
class structure_EnumerationBinding:

    pass
class structure_UseAdaptationOperator:

    pass
class structure_ClassDefinitionBinding:

    pass
class structure_OperationBinding:

    pass
class structure_PropertyBinding:

    pass
class structure_ModelTypeVariable:

    pass
class ObjectTypeVariable:

    pass
class org_structure_VirtualType(ObjectTypeVariable):

    pass
class structure_VirtualType:

    pass
class structure_GenericTypeDefinition:

    pass
class structure_TypeVariableBinding:

    pass
class Type:

    pass
class org_structure_ModelType(Type):

    pass
class org_structure_VoidType(Type):

    pass
class org_structure_ParameterizedType(Type):

    pass
class ModelElementTypeDefinition:

    pass
class org_structure_GenericTypeDefinition(ModelElementTypeDefinition):

    pass
class TypeVariable:

    pass
class org_structure_ModelTypeVariable(TypeVariable):

    pass
class org_structure_ObjectTypeVariable(TypeVariable):

    pass
class GenericTypeDefinition:

    pass
class structure_FilteredMetamodelReference:

    pass
class structure_ModelTypeDefinitionContainer:

    pass
class org_structure_ClassDefinition(GenericTypeDefinition):

    def __init__(self, isAbstract: str, isSingleton: str, isFinal: str, language158: set["structure_Constraint"] = None, language161: set["structure_Property"] = None, language164: set["structure_Operation"] = None):
        self.isAbstract = isAbstract
        self.isSingleton = isSingleton
        self.isFinal = isFinal
        self.language158 = language158 if language158 is not None else set()
        self.language161 = language161 if language161 is not None else set()
        self.language164 = language164 if language164 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def isSingleton(self) -> str:
        return self.__isSingleton

    @isSingleton.setter
    def isSingleton(self, isSingleton: str):
        self.__isSingleton = isSingleton

    @property
    def isFinal(self) -> str:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: str):
        self.__isFinal = isFinal

    @property
    def language164(self):
        return self.__language164

    @language164.setter
    def language164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ClassDefinition__language164", None)
        self.__language164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kermeta165"):
                    opp_val = getattr(item, "kermeta165", None)
                    
                    if opp_val == self:
                        setattr(item, "kermeta165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kermeta165"):
                    opp_val = getattr(item, "kermeta165", None)
                    
                    setattr(item, "kermeta165", self)
                    

    @property
    def language158(self):
        return self.__language158

    @language158.setter
    def language158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ClassDefinition__language158", None)
        self.__language158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kermeta159"):
                    opp_val = getattr(item, "kermeta159", None)
                    
                    if opp_val == self:
                        setattr(item, "kermeta159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kermeta159"):
                    opp_val = getattr(item, "kermeta159", None)
                    
                    setattr(item, "kermeta159", self)
                    

    @property
    def language161(self):
        return self.__language161

    @language161.setter
    def language161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ClassDefinition__language161", None)
        self.__language161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kermeta162"):
                    opp_val = getattr(item, "kermeta162", None)
                    
                    if opp_val == self:
                        setattr(item, "kermeta162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kermeta162"):
                    opp_val = getattr(item, "kermeta162", None)
                    
                    setattr(item, "kermeta162", self)
                    

class structure_Package:

    pass
class structure_ModelElementTypeDefinitionContainer:

    pass
class DataType:

    pass
class org_structure_Enumeration(DataType):

    pass
class org_structure_PrimitiveType(DataType):

    pass
class structure_AdaptationOperator:

    pass
class ParameterizedType:

    pass
class org_structure_Class(ParameterizedType):

    def __init__(self, isAbstract: str, name: str, org_structure_Class122: set["structure_Operation"] = None, org_structure_Class125: set["structure_Class"] = None, org_structure_Class: set["structure_Property"] = None):
        self.isAbstract = isAbstract
        self.name = name
        self.org_structure_Class122 = org_structure_Class122 if org_structure_Class122 is not None else set()
        self.org_structure_Class125 = org_structure_Class125 if org_structure_Class125 is not None else set()
        self.org_structure_Class = org_structure_Class if org_structure_Class is not None else set()
        
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
    def org_structure_Class(self):
        return self.__org_structure_Class

    @org_structure_Class.setter
    def org_structure_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Class__org_structure_Class", None)
        self.__org_structure_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Property120"):
                    opp_val = getattr(item, "structure_Property120", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Property120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Property120"):
                    opp_val = getattr(item, "structure_Property120", None)
                    
                    setattr(item, "structure_Property120", self)
                    

    @property
    def org_structure_Class122(self):
        return self.__org_structure_Class122

    @org_structure_Class122.setter
    def org_structure_Class122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Class__org_structure_Class122", None)
        self.__org_structure_Class122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Operation123"):
                    opp_val = getattr(item, "structure_Operation123", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Operation123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Operation123"):
                    opp_val = getattr(item, "structure_Operation123", None)
                    
                    setattr(item, "structure_Operation123", self)
                    

    @property
    def org_structure_Class125(self):
        return self.__org_structure_Class125

    @org_structure_Class125.setter
    def org_structure_Class125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Class__org_structure_Class125", None)
        self.__org_structure_Class125 = value if value is not None else set()
        
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
                    

class structure_NamedElement:

    pass
class org_structure_Package(structure_NamedElement, structure_ModelElementTypeDefinitionContainer):

    def __init__(self, uri: str, org_structure_Package: set["structure_AdaptationOperator"] = None, language130: set["structure_Package"] = None, language133: "structure_Package" = None):
        self.uri = uri
        self.org_structure_Package = org_structure_Package if org_structure_Package is not None else set()
        self.language130 = language130 if language130 is not None else set()
        self.language133 = language133
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def org_structure_Package(self):
        return self.__org_structure_Package

    @org_structure_Package.setter
    def org_structure_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Package__org_structure_Package", None)
        self.__org_structure_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_AdaptationOperator"):
                    opp_val = getattr(item, "structure_AdaptationOperator", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_AdaptationOperator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_AdaptationOperator"):
                    opp_val = getattr(item, "structure_AdaptationOperator", None)
                    
                    setattr(item, "structure_AdaptationOperator", self)
                    

    @property
    def language130(self):
        return self.__language130

    @language130.setter
    def language130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Package__language130", None)
        self.__language130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kermeta131"):
                    opp_val = getattr(item, "kermeta131", None)
                    
                    if opp_val == self:
                        setattr(item, "kermeta131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kermeta131"):
                    opp_val = getattr(item, "kermeta131", None)
                    
                    setattr(item, "kermeta131", self)
                    

    @property
    def language133(self):
        return self.__language133

    @language133.setter
    def language133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Package__language133", None)
        self.__language133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kermeta134"):
                opp_val = getattr(old_value, "kermeta134", None)
                if opp_val == self:
                    setattr(old_value, "kermeta134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kermeta134"):
                opp_val = getattr(value, "kermeta134", None)
                setattr(value, "kermeta134", self)

class structure_ModelElementTypeDefinition:

    pass
class structure_Class:

    pass
class structure_Enumeration:

    pass
class NamedElement:

    pass
class org_structure_AdaptationOperator(NamedElement):

    pass
class org_structure_Constraint(NamedElement):

    def __init__(self, language: str, stereotype: str, language149: "structure_ClassDefinition" = None, language152: "structure_Operation" = None, language155: "structure_Operation" = None, org_structure_Constraint: "behavior_Expression" = None):
        self.language = language
        self.stereotype = stereotype
        self.language149 = language149
        self.language152 = language152
        self.language155 = language155
        self.org_structure_Constraint = org_structure_Constraint
        
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
    def language152(self):
        return self.__language152

    @language152.setter
    def language152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Constraint__language152", None)
        self.__language152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kermeta153"):
                opp_val = getattr(old_value, "kermeta153", None)
                if opp_val == self:
                    setattr(old_value, "kermeta153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kermeta153"):
                opp_val = getattr(value, "kermeta153", None)
                setattr(value, "kermeta153", self)

    @property
    def language149(self):
        return self.__language149

    @language149.setter
    def language149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Constraint__language149", None)
        self.__language149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kermeta150"):
                opp_val = getattr(old_value, "kermeta150", None)
                if opp_val == self:
                    setattr(old_value, "kermeta150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kermeta150"):
                opp_val = getattr(value, "kermeta150", None)
                setattr(value, "kermeta150", self)

    @property
    def language155(self):
        return self.__language155

    @language155.setter
    def language155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Constraint__language155", None)
        self.__language155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kermeta156"):
                opp_val = getattr(old_value, "kermeta156", None)
                if opp_val == self:
                    setattr(old_value, "kermeta156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kermeta156"):
                opp_val = getattr(value, "kermeta156", None)
                setattr(value, "kermeta156", self)

    @property
    def org_structure_Constraint(self):
        return self.__org_structure_Constraint

    @org_structure_Constraint.setter
    def org_structure_Constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Constraint__org_structure_Constraint", None)
        self.__org_structure_Constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression147"):
                opp_val = getattr(old_value, "behavior_Expression147", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression147"):
                opp_val = getattr(value, "behavior_Expression147", None)
                setattr(value, "behavior_Expression147", self)

class org_structure_ModelElementTypeDefinitionContainer(NamedElement):

    pass
class org_structure_EnumerationLiteral(NamedElement):

    pass
class structure_UnresolvedProperty:

    pass
class TypedElement:

    pass
class org_structure_AdaptationParameter(TypedElement):

    pass
class org_structure_MultiplicityElement(TypedElement):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

class structure_AbstractProperty:

    pass
class structure_TypeVariable:

    pass
class structure_ClassDefinition:

    pass
class structure_Parameter:

    pass
class structure_AbstractOperation:

    pass
class structure_MultiplicityElement:

    pass
class org_structure_Property(structure_AbstractProperty, structure_MultiplicityElement):

    def __init__(self, isGetterAbstract: str, isSetterAbstract: str, isReadOnly: str, default: str, isComposite: str, isDerived: str, isID: str, org_structure_Property93: "behavior_Expression" = None, org_structure_Property96: "behavior_Expression" = None, org_structure_Property: "structure_AbstractProperty" = None, org_structure_Property99: set["structure_UnresolvedProperty"] = None, language101: "structure_ClassDefinition" = None, structure_AbstractProperty: "org_structure_Property"):
        self.isGetterAbstract = isGetterAbstract
        self.isSetterAbstract = isSetterAbstract
        self.isReadOnly = isReadOnly
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.org_structure_Property93 = org_structure_Property93
        self.org_structure_Property96 = org_structure_Property96
        self.org_structure_Property = org_structure_Property
        self.org_structure_Property99 = org_structure_Property99 if org_structure_Property99 is not None else set()
        self.language101 = language101
        
    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def isGetterAbstract(self) -> str:
        return self.__isGetterAbstract

    @isGetterAbstract.setter
    def isGetterAbstract(self, isGetterAbstract: str):
        self.__isGetterAbstract = isGetterAbstract

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
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def org_structure_Property93(self):
        return self.__org_structure_Property93

    @org_structure_Property93.setter
    def org_structure_Property93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Property__org_structure_Property93", None)
        self.__org_structure_Property93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression94"):
                opp_val = getattr(old_value, "behavior_Expression94", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression94"):
                opp_val = getattr(value, "behavior_Expression94", None)
                setattr(value, "behavior_Expression94", self)

    @property
    def org_structure_Property96(self):
        return self.__org_structure_Property96

    @org_structure_Property96.setter
    def org_structure_Property96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Property__org_structure_Property96", None)
        self.__org_structure_Property96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression97"):
                opp_val = getattr(old_value, "behavior_Expression97", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression97"):
                opp_val = getattr(value, "behavior_Expression97", None)
                setattr(value, "behavior_Expression97", self)

    @property
    def org_structure_Property99(self):
        return self.__org_structure_Property99

    @org_structure_Property99.setter
    def org_structure_Property99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Property__org_structure_Property99", None)
        self.__org_structure_Property99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_UnresolvedProperty"):
                    opp_val = getattr(item, "structure_UnresolvedProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_UnresolvedProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_UnresolvedProperty"):
                    opp_val = getattr(item, "structure_UnresolvedProperty", None)
                    
                    setattr(item, "structure_UnresolvedProperty", self)
                    

    @property
    def org_structure_Property(self):
        return self.__org_structure_Property

    @org_structure_Property.setter
    def org_structure_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Property__org_structure_Property", None)
        self.__org_structure_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_AbstractProperty"):
                opp_val = getattr(old_value, "structure_AbstractProperty", None)
                if opp_val == self:
                    setattr(old_value, "structure_AbstractProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_AbstractProperty"):
                opp_val = getattr(value, "structure_AbstractProperty", None)
                setattr(value, "structure_AbstractProperty", self)

    @property
    def language101(self):
        return self.__language101

    @language101.setter
    def language101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Property__language101", None)
        self.__language101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kermeta102"):
                opp_val = getattr(old_value, "kermeta102", None)
                if opp_val == self:
                    setattr(old_value, "kermeta102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kermeta102"):
                opp_val = getattr(value, "kermeta102", None)
                setattr(value, "kermeta102", self)

class org_structure_Operation(structure_AbstractOperation, structure_MultiplicityElement):

    def __init__(self, isAbstract: str, uniqueName: str, language76: set["structure_Constraint"] = None, language79: set["structure_Constraint"] = None, org_structure_Operation82: "behavior_Expression" = None, org_structure_Operation85: set["structure_UnresolvedOperation"] = None, org_structure_Operation: set["structure_Type"] = None, language73: set["structure_Parameter"] = None, language87: "structure_ClassDefinition" = None, org_structure_Operation90: set["structure_TypeVariable"] = None):
        self.isAbstract = isAbstract
        self.uniqueName = uniqueName
        self.language76 = language76 if language76 is not None else set()
        self.language79 = language79 if language79 is not None else set()
        self.org_structure_Operation82 = org_structure_Operation82
        self.org_structure_Operation85 = org_structure_Operation85 if org_structure_Operation85 is not None else set()
        self.org_structure_Operation = org_structure_Operation if org_structure_Operation is not None else set()
        self.language73 = language73 if language73 is not None else set()
        self.language87 = language87
        self.org_structure_Operation90 = org_structure_Operation90 if org_structure_Operation90 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def uniqueName(self) -> str:
        return self.__uniqueName

    @uniqueName.setter
    def uniqueName(self, uniqueName: str):
        self.__uniqueName = uniqueName

    @property
    def org_structure_Operation(self):
        return self.__org_structure_Operation

    @org_structure_Operation.setter
    def org_structure_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__org_structure_Operation", None)
        self.__org_structure_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type71"):
                    opp_val = getattr(item, "structure_Type71", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type71"):
                    opp_val = getattr(item, "structure_Type71", None)
                    
                    setattr(item, "structure_Type71", self)
                    

    @property
    def org_structure_Operation82(self):
        return self.__org_structure_Operation82

    @org_structure_Operation82.setter
    def org_structure_Operation82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__org_structure_Operation82", None)
        self.__org_structure_Operation82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression83"):
                opp_val = getattr(old_value, "behavior_Expression83", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression83"):
                opp_val = getattr(value, "behavior_Expression83", None)
                setattr(value, "behavior_Expression83", self)

    @property
    def language73(self):
        return self.__language73

    @language73.setter
    def language73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__language73", None)
        self.__language73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kermeta74"):
                    opp_val = getattr(item, "kermeta74", None)
                    
                    if opp_val == self:
                        setattr(item, "kermeta74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kermeta74"):
                    opp_val = getattr(item, "kermeta74", None)
                    
                    setattr(item, "kermeta74", self)
                    

    @property
    def language76(self):
        return self.__language76

    @language76.setter
    def language76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__language76", None)
        self.__language76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kermeta77"):
                    opp_val = getattr(item, "kermeta77", None)
                    
                    if opp_val == self:
                        setattr(item, "kermeta77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kermeta77"):
                    opp_val = getattr(item, "kermeta77", None)
                    
                    setattr(item, "kermeta77", self)
                    

    @property
    def org_structure_Operation90(self):
        return self.__org_structure_Operation90

    @org_structure_Operation90.setter
    def org_structure_Operation90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__org_structure_Operation90", None)
        self.__org_structure_Operation90 = value if value is not None else set()
        
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
    def language79(self):
        return self.__language79

    @language79.setter
    def language79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__language79", None)
        self.__language79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kermeta80"):
                    opp_val = getattr(item, "kermeta80", None)
                    
                    if opp_val == self:
                        setattr(item, "kermeta80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kermeta80"):
                    opp_val = getattr(item, "kermeta80", None)
                    
                    setattr(item, "kermeta80", self)
                    

    @property
    def org_structure_Operation85(self):
        return self.__org_structure_Operation85

    @org_structure_Operation85.setter
    def org_structure_Operation85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__org_structure_Operation85", None)
        self.__org_structure_Operation85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_UnresolvedOperation"):
                    opp_val = getattr(item, "structure_UnresolvedOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_UnresolvedOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_UnresolvedOperation"):
                    opp_val = getattr(item, "structure_UnresolvedOperation", None)
                    
                    setattr(item, "structure_UnresolvedOperation", self)
                    

    @property
    def language87(self):
        return self.__language87

    @language87.setter
    def language87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Operation__language87", None)
        self.__language87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kermeta88"):
                opp_val = getattr(old_value, "kermeta88", None)
                if opp_val == self:
                    setattr(old_value, "kermeta88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kermeta88"):
                opp_val = getattr(value, "kermeta88", None)
                setattr(value, "kermeta88", self)

class structure_Tag:

    pass
class org_structure_KermetaModelElement(ABC):

    pass
class structure_ModelTransformation:

    pass
class structure_UnresolvedOperation:

    pass
class structure_Constraint:

    pass
class structure_Property:

    pass
class structure_Operation:

    pass
class CallFeature:

    pass
class org_behavior_CallProperty(CallFeature):

    pass
class org_behavior_CallOperation(CallFeature):

    pass
class org_behavior_CallModelTransformation(CallFeature):

    pass
class structure_EnumerationLiteral:

    pass
class structure_UnresolvedReference:

    pass
class org_structure_UnresolvedModelTransformation(structure_ModelTransformation, structure_UnresolvedReference):

    pass
class org_structure_UnresolvedTypeVariable(structure_TypeVariable, structure_UnresolvedReference):

    pass
class org_structure_UnresolvedModelTypeDefinition(structure_UnresolvedReference, structure_ModelTypeDefinition):

    pass
class org_structure_UnresolvedAdaptationOperator(structure_AdaptationOperator, structure_UnresolvedReference):

    pass
class org_structure_UnresolvedProperty(structure_AbstractProperty, structure_UnresolvedReference):

    def __init__(self, propertyIdentifier: str, structure_UnresolvedReference: "org_structure_UseAdaptationOperator", structure_AbstractProperty: "org_structure_Property"):
        self.propertyIdentifier = propertyIdentifier
        
    @property
    def propertyIdentifier(self) -> str:
        return self.__propertyIdentifier

    @propertyIdentifier.setter
    def propertyIdentifier(self, propertyIdentifier: str):
        self.__propertyIdentifier = propertyIdentifier

class structure_Using:

    pass
class Literal:

    pass
class org_behavior_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class org_behavior_CallTypeLiteral(Literal):

    pass
class org_behavior_BooleanLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class org_behavior_IntegerLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class org_behavior_VoidLiteral(Literal):

    pass
class MultiplicityElement:

    pass
class org_structure_Parameter(MultiplicityElement):

    pass
class org_structure_ModelTransformation(MultiplicityElement):

    def __init__(self, isAbstract: str, org_structure_ModelTransformation: set["structure_ModelTypeVariable"] = None, org_structure_ModelTransformation263: "behavior_Expression" = None, org_structure_ModelTransformation266: set["structure_Operation"] = None, language269: "structure_ModelTypeDefinition" = None, org_structure_ModelTransformation272: set["structure_Parameter"] = None):
        self.isAbstract = isAbstract
        self.org_structure_ModelTransformation = org_structure_ModelTransformation if org_structure_ModelTransformation is not None else set()
        self.org_structure_ModelTransformation263 = org_structure_ModelTransformation263
        self.org_structure_ModelTransformation266 = org_structure_ModelTransformation266 if org_structure_ModelTransformation266 is not None else set()
        self.language269 = language269
        self.org_structure_ModelTransformation272 = org_structure_ModelTransformation272 if org_structure_ModelTransformation272 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def org_structure_ModelTransformation272(self):
        return self.__org_structure_ModelTransformation272

    @org_structure_ModelTransformation272.setter
    def org_structure_ModelTransformation272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ModelTransformation__org_structure_ModelTransformation272", None)
        self.__org_structure_ModelTransformation272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Parameter"):
                    opp_val = getattr(item, "structure_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Parameter"):
                    opp_val = getattr(item, "structure_Parameter", None)
                    
                    setattr(item, "structure_Parameter", self)
                    

    @property
    def org_structure_ModelTransformation(self):
        return self.__org_structure_ModelTransformation

    @org_structure_ModelTransformation.setter
    def org_structure_ModelTransformation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ModelTransformation__org_structure_ModelTransformation", None)
        self.__org_structure_ModelTransformation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_ModelTypeVariable"):
                    opp_val = getattr(item, "structure_ModelTypeVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_ModelTypeVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_ModelTypeVariable"):
                    opp_val = getattr(item, "structure_ModelTypeVariable", None)
                    
                    setattr(item, "structure_ModelTypeVariable", self)
                    

    @property
    def org_structure_ModelTransformation266(self):
        return self.__org_structure_ModelTransformation266

    @org_structure_ModelTransformation266.setter
    def org_structure_ModelTransformation266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ModelTransformation__org_structure_ModelTransformation266", None)
        self.__org_structure_ModelTransformation266 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Operation267"):
                    opp_val = getattr(item, "structure_Operation267", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Operation267", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Operation267"):
                    opp_val = getattr(item, "structure_Operation267", None)
                    
                    setattr(item, "structure_Operation267", self)
                    

    @property
    def org_structure_ModelTransformation263(self):
        return self.__org_structure_ModelTransformation263

    @org_structure_ModelTransformation263.setter
    def org_structure_ModelTransformation263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ModelTransformation__org_structure_ModelTransformation263", None)
        self.__org_structure_ModelTransformation263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression264"):
                opp_val = getattr(old_value, "behavior_Expression264", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression264"):
                opp_val = getattr(value, "behavior_Expression264", None)
                setattr(value, "behavior_Expression264", self)

    @property
    def language269(self):
        return self.__language269

    @language269.setter
    def language269(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_ModelTransformation__language269", None)
        self.__language269 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kermeta270"):
                opp_val = getattr(old_value, "kermeta270", None)
                if opp_val == self:
                    setattr(old_value, "kermeta270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kermeta270"):
                opp_val = getattr(value, "kermeta270", None)
                setattr(value, "kermeta270", self)

class org_behavior_TypeReference(MultiplicityElement):

    pass
class behavior_LambdaParameter:

    pass
class CallVariable:

    pass
class org_behavior_CallResult(CallVariable):

    pass
class behavior_TypeReference:

    pass
class KermetaModelElement:

    pass
class org_structure_EnumerationBinding(KermetaModelElement):

    pass
class org_structure_TypeContainer(KermetaModelElement):

    pass
class org_structure_Type(KermetaModelElement):

    pass
class org_structure_Model(KermetaModelElement):

    pass
class org_structure_FilteredMetamodelReference(KermetaModelElement):

    pass
class org_structure_UseAdaptationOperator(KermetaModelElement):

    pass
class org_structure_UnresolvedReference(KermetaModelElement):

    pass
class org_structure_AbstractOperation(KermetaModelElement):

    pass
class org_structure_ClassDefinitionBinding(KermetaModelElement):

    pass
class org_structure_PropertyBinding(KermetaModelElement):

    pass
class org_structure_ModelTypeDefinitionContainer(KermetaModelElement):

    pass
class org_structure_Tag(KermetaModelElement):

    def __init__(self, name: str, value: str, language144: set["structure_KermetaModelElement"] = None):
        self.name = name
        self.value = value
        self.language144 = language144 if language144 is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def language144(self):
        return self.__language144

    @language144.setter
    def language144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Tag__language144", None)
        self.__language144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kermeta145"):
                    opp_val = getattr(item, "kermeta145", None)
                    
                    if opp_val == self:
                        setattr(item, "kermeta145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kermeta145"):
                    opp_val = getattr(item, "kermeta145", None)
                    
                    setattr(item, "kermeta145", self)
                    

class org_structure_AbstractProperty(KermetaModelElement):

    pass
class org_structure_Using(KermetaModelElement):

    def __init__(self, fromQName: str, toName: str):
        self.fromQName = fromQName
        self.toName = toName
        
    @property
    def toName(self) -> str:
        return self.__toName

    @toName.setter
    def toName(self, toName: str):
        self.__toName = toName

    @property
    def fromQName(self) -> str:
        return self.__fromQName

    @fromQName.setter
    def fromQName(self, fromQName: str):
        self.__fromQName = fromQName

class org_behavior_LambdaParameter(KermetaModelElement):

    def __init__(self, name: str, org_behavior_LambdaParameter: "behavior_TypeReference" = None):
        self.name = name
        self.org_behavior_LambdaParameter = org_behavior_LambdaParameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def org_behavior_LambdaParameter(self):
        return self.__org_behavior_LambdaParameter

    @org_behavior_LambdaParameter.setter
    def org_behavior_LambdaParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_LambdaParameter__org_behavior_LambdaParameter", None)
        self.__org_behavior_LambdaParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_TypeReference38"):
                opp_val = getattr(old_value, "behavior_TypeReference38", None)
                if opp_val == self:
                    setattr(old_value, "behavior_TypeReference38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_TypeReference38"):
                opp_val = getattr(value, "behavior_TypeReference38", None)
                setattr(value, "behavior_TypeReference38", self)

class org_structure_OperationBinding(KermetaModelElement):

    pass
class org_structure_NamedElement(KermetaModelElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class org_behavior_Rescue(KermetaModelElement):

    def __init__(self, exceptionName: str, org_behavior_Rescue: set["behavior_Expression"] = None, org_behavior_Rescue30: "behavior_TypeReference" = None):
        self.exceptionName = exceptionName
        self.org_behavior_Rescue = org_behavior_Rescue if org_behavior_Rescue is not None else set()
        self.org_behavior_Rescue30 = org_behavior_Rescue30
        
    @property
    def exceptionName(self) -> str:
        return self.__exceptionName

    @exceptionName.setter
    def exceptionName(self, exceptionName: str):
        self.__exceptionName = exceptionName

    @property
    def org_behavior_Rescue(self):
        return self.__org_behavior_Rescue

    @org_behavior_Rescue.setter
    def org_behavior_Rescue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_Rescue__org_behavior_Rescue", None)
        self.__org_behavior_Rescue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behavior_Expression28"):
                    opp_val = getattr(item, "behavior_Expression28", None)
                    
                    if opp_val == self:
                        setattr(item, "behavior_Expression28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behavior_Expression28"):
                    opp_val = getattr(item, "behavior_Expression28", None)
                    
                    setattr(item, "behavior_Expression28", self)
                    

    @property
    def org_behavior_Rescue30(self):
        return self.__org_behavior_Rescue30

    @org_behavior_Rescue30.setter
    def org_behavior_Rescue30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_Rescue__org_behavior_Rescue30", None)
        self.__org_behavior_Rescue30 = value
        
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

class CallExpression:

    pass
class org_behavior_CallEnumLiteral(CallExpression):

    pass
class org_behavior_CallValue(CallExpression):

    pass
class org_behavior_CallVariable(CallExpression):

    def __init__(self, isAtpre: str):
        self.isAtpre = isAtpre
        
    @property
    def isAtpre(self) -> str:
        return self.__isAtpre

    @isAtpre.setter
    def isAtpre(self, isAtpre: str):
        self.__isAtpre = isAtpre

class behavior_Rescue:

    pass
class CallOperation:

    pass
class org_behavior_CallSuperOperation(CallOperation):

    pass
class org_behavior_CallFeature(CallExpression):

    def __init__(self, isAtpre: str, org_behavior_CallFeature: "behavior_Expression" = None):
        self.isAtpre = isAtpre
        self.org_behavior_CallFeature = org_behavior_CallFeature
        
    @property
    def isAtpre(self) -> str:
        return self.__isAtpre

    @isAtpre.setter
    def isAtpre(self, isAtpre: str):
        self.__isAtpre = isAtpre

    @property
    def org_behavior_CallFeature(self):
        return self.__org_behavior_CallFeature

    @org_behavior_CallFeature.setter
    def org_behavior_CallFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_CallFeature__org_behavior_CallFeature", None)
        self.__org_behavior_CallFeature = value
        
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

class behavior_Expression:

    pass
class behavior_CallExpression:

    pass
class Expression:

    pass
class org_behavior_Conditional(Expression):

    pass
class org_behavior_Literal(Expression):

    pass
class org_behavior_VariableDecl(Expression):

    def __init__(self, identifier: str, org_behavior_VariableDecl: "behavior_Expression" = None, org_behavior_VariableDecl52: "behavior_TypeReference" = None):
        self.identifier = identifier
        self.org_behavior_VariableDecl = org_behavior_VariableDecl
        self.org_behavior_VariableDecl52 = org_behavior_VariableDecl52
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def org_behavior_VariableDecl(self):
        return self.__org_behavior_VariableDecl

    @org_behavior_VariableDecl.setter
    def org_behavior_VariableDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_VariableDecl__org_behavior_VariableDecl", None)
        self.__org_behavior_VariableDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression50"):
                opp_val = getattr(old_value, "behavior_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression50"):
                opp_val = getattr(value, "behavior_Expression50", None)
                setattr(value, "behavior_Expression50", self)

    @property
    def org_behavior_VariableDecl52(self):
        return self.__org_behavior_VariableDecl52

    @org_behavior_VariableDecl52.setter
    def org_behavior_VariableDecl52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_VariableDecl__org_behavior_VariableDecl52", None)
        self.__org_behavior_VariableDecl52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_TypeReference53"):
                opp_val = getattr(old_value, "behavior_TypeReference53", None)
                if opp_val == self:
                    setattr(old_value, "behavior_TypeReference53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_TypeReference53"):
                opp_val = getattr(value, "behavior_TypeReference53", None)
                setattr(value, "behavior_TypeReference53", self)

class org_behavior_SelfExpression(Expression):

    pass
class org_behavior_EmptyExpression(Expression):

    pass
class org_behavior_Loop(Expression):

    pass
class org_behavior_JavaStaticCall(Expression):

    def __init__(self, jclass: str, jmethod: str, org_behavior_JavaStaticCall: set["behavior_Expression"] = None):
        self.jclass = jclass
        self.jmethod = jmethod
        self.org_behavior_JavaStaticCall = org_behavior_JavaStaticCall if org_behavior_JavaStaticCall is not None else set()
        
    @property
    def jclass(self) -> str:
        return self.__jclass

    @jclass.setter
    def jclass(self, jclass: str):
        self.__jclass = jclass

    @property
    def jmethod(self) -> str:
        return self.__jmethod

    @jmethod.setter
    def jmethod(self, jmethod: str):
        self.__jmethod = jmethod

    @property
    def org_behavior_JavaStaticCall(self):
        return self.__org_behavior_JavaStaticCall

    @org_behavior_JavaStaticCall.setter
    def org_behavior_JavaStaticCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_JavaStaticCall__org_behavior_JavaStaticCall", None)
        self.__org_behavior_JavaStaticCall = value if value is not None else set()
        
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
                    

class org_behavior_Block(Expression):

    pass
class org_behavior_LambdaExpression(Expression):

    pass
class org_behavior_Raise(Expression):

    pass
class org_behavior_Assignment(Expression):

    def __init__(self, isCast: str, org_behavior_Assignment: "behavior_CallExpression" = None, org_behavior_Assignment2: "behavior_Expression" = None):
        self.isCast = isCast
        self.org_behavior_Assignment = org_behavior_Assignment
        self.org_behavior_Assignment2 = org_behavior_Assignment2
        
    @property
    def isCast(self) -> str:
        return self.__isCast

    @isCast.setter
    def isCast(self, isCast: str):
        self.__isCast = isCast

    @property
    def org_behavior_Assignment(self):
        return self.__org_behavior_Assignment

    @org_behavior_Assignment.setter
    def org_behavior_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_Assignment__org_behavior_Assignment", None)
        self.__org_behavior_Assignment = value
        
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
    def org_behavior_Assignment2(self):
        return self.__org_behavior_Assignment2

    @org_behavior_Assignment2.setter
    def org_behavior_Assignment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_Assignment__org_behavior_Assignment2", None)
        self.__org_behavior_Assignment2 = value
        
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

class org_behavior_CallExpression(Expression):

    def __init__(self, name: str, org_behavior_CallExpression: set["behavior_Expression"] = None, org_behavior_CallExpression7: set["structure_Type"] = None):
        self.name = name
        self.org_behavior_CallExpression = org_behavior_CallExpression if org_behavior_CallExpression is not None else set()
        self.org_behavior_CallExpression7 = org_behavior_CallExpression7 if org_behavior_CallExpression7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def org_behavior_CallExpression(self):
        return self.__org_behavior_CallExpression

    @org_behavior_CallExpression.setter
    def org_behavior_CallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_CallExpression__org_behavior_CallExpression", None)
        self.__org_behavior_CallExpression = value if value is not None else set()
        
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
    def org_behavior_CallExpression7(self):
        return self.__org_behavior_CallExpression7

    @org_behavior_CallExpression7.setter
    def org_behavior_CallExpression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_CallExpression__org_behavior_CallExpression7", None)
        self.__org_behavior_CallExpression7 = value if value is not None else set()
        
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
                    

class structure_Type:

    pass
class org_structure_UnresolvedInferredType(structure_Type, structure_UnresolvedReference):

    pass
class org_structure_DataType(structure_Type, structure_ModelElementTypeDefinition):

    pass
class structure_TypeContainer:

    pass
class org_structure_UnresolvedOperation(structure_AbstractOperation, structure_TypeContainer, structure_UnresolvedReference):

    def __init__(self, operationIdentifier: str, kermeta105: "org_structure_Type", structure_UnresolvedReference: "org_structure_UseAdaptationOperator"):
        self.operationIdentifier = operationIdentifier
        
    @property
    def operationIdentifier(self) -> str:
        return self.__operationIdentifier

    @operationIdentifier.setter
    def operationIdentifier(self, operationIdentifier: str):
        self.__operationIdentifier = operationIdentifier

class org_structure_FunctionType(structure_Type, structure_TypeContainer):

    pass
class org_structure_ProductType(structure_Type, structure_TypeContainer):

    pass
class org_structure_TypeDefinition(structure_NamedElement, structure_TypeContainer):

    def __init__(self, isAspect: str, org_structure_TypeDefinition: set["structure_Type"] = None, kermeta105: "org_structure_Type"):
        self.isAspect = isAspect
        self.org_structure_TypeDefinition = org_structure_TypeDefinition if org_structure_TypeDefinition is not None else set()
        
    @property
    def isAspect(self) -> str:
        return self.__isAspect

    @isAspect.setter
    def isAspect(self, isAspect: str):
        self.__isAspect = isAspect

    @property
    def org_structure_TypeDefinition(self):
        return self.__org_structure_TypeDefinition

    @org_structure_TypeDefinition.setter
    def org_structure_TypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_TypeDefinition__org_structure_TypeDefinition", None)
        self.__org_structure_TypeDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type118"):
                    opp_val = getattr(item, "structure_Type118", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type118"):
                    opp_val = getattr(item, "structure_Type118", None)
                    
                    setattr(item, "structure_Type118", self)
                    

class org_structure_TypeVariable(structure_Type, structure_NamedElement, structure_TypeContainer):

    pass
class org_structure_UnresolvedType(structure_Type, structure_TypeContainer, structure_UnresolvedReference):

    def __init__(self, typeIdentifier: str, org_structure_UnresolvedType: set["structure_Using"] = None, org_structure_UnresolvedType195: set["structure_Type"] = None, kermeta105: "org_structure_Type", structure_Type8: "org_behavior_CallExpression", structure_Type60: "org_behavior_UnresolvedCall", structure_Type71: "org_structure_Operation", structure_Type200: "org_structure_FunctionType", structure_Type116: "org_structure_TypeVariableBinding", structure_Type203: "org_structure_FunctionType", structure_Type118: "org_structure_TypeDefinition", structure_Type179: "org_structure_TypeVariable", structure_Type63: "org_behavior_UnresolvedCall", structure_Type142: "org_structure_TypedElement", structure_Type140: "org_structure_PrimitiveType", structure_Type: "org_behavior_Expression", structure_Type198: "org_structure_ProductType", structure_Type196: "org_structure_UnresolvedType", structure_Type16: "org_behavior_CallSuperOperation", kermeta108: "org_structure_TypeContainer", structure_UnresolvedReference: "org_structure_UseAdaptationOperator"):
        self.typeIdentifier = typeIdentifier
        self.org_structure_UnresolvedType = org_structure_UnresolvedType if org_structure_UnresolvedType is not None else set()
        self.org_structure_UnresolvedType195 = org_structure_UnresolvedType195 if org_structure_UnresolvedType195 is not None else set()
        
    @property
    def typeIdentifier(self) -> str:
        return self.__typeIdentifier

    @typeIdentifier.setter
    def typeIdentifier(self, typeIdentifier: str):
        self.__typeIdentifier = typeIdentifier

    @property
    def org_structure_UnresolvedType195(self):
        return self.__org_structure_UnresolvedType195

    @org_structure_UnresolvedType195.setter
    def org_structure_UnresolvedType195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_UnresolvedType__org_structure_UnresolvedType195", None)
        self.__org_structure_UnresolvedType195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type196"):
                    opp_val = getattr(item, "structure_Type196", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type196"):
                    opp_val = getattr(item, "structure_Type196", None)
                    
                    setattr(item, "structure_Type196", self)
                    

    @property
    def org_structure_UnresolvedType(self):
        return self.__org_structure_UnresolvedType

    @org_structure_UnresolvedType.setter
    def org_structure_UnresolvedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_UnresolvedType__org_structure_UnresolvedType", None)
        self.__org_structure_UnresolvedType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Using193"):
                    opp_val = getattr(item, "structure_Using193", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Using193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Using193"):
                    opp_val = getattr(item, "structure_Using193", None)
                    
                    setattr(item, "structure_Using193", self)
                    

class org_structure_TypedElement(structure_NamedElement, structure_TypeContainer):

    pass
class org_behavior_UnresolvedCall(behavior_CallExpression, structure_TypeContainer, structure_UnresolvedReference):

    def __init__(self, isAtpre: str, isCalledWithParenthesis: str, org_behavior_UnresolvedCall: set["structure_Using"] = None, org_behavior_UnresolvedCall56: "behavior_Expression" = None, org_behavior_UnresolvedCall59: "structure_Type" = None, org_behavior_UnresolvedCall62: set["structure_Type"] = None, kermeta105: "org_structure_Type", behavior_CallExpression: "org_behavior_Assignment", structure_UnresolvedReference: "org_structure_UseAdaptationOperator"):
        self.isAtpre = isAtpre
        self.isCalledWithParenthesis = isCalledWithParenthesis
        self.org_behavior_UnresolvedCall = org_behavior_UnresolvedCall if org_behavior_UnresolvedCall is not None else set()
        self.org_behavior_UnresolvedCall56 = org_behavior_UnresolvedCall56
        self.org_behavior_UnresolvedCall59 = org_behavior_UnresolvedCall59
        self.org_behavior_UnresolvedCall62 = org_behavior_UnresolvedCall62 if org_behavior_UnresolvedCall62 is not None else set()
        
    @property
    def isCalledWithParenthesis(self) -> str:
        return self.__isCalledWithParenthesis

    @isCalledWithParenthesis.setter
    def isCalledWithParenthesis(self, isCalledWithParenthesis: str):
        self.__isCalledWithParenthesis = isCalledWithParenthesis

    @property
    def isAtpre(self) -> str:
        return self.__isAtpre

    @isAtpre.setter
    def isAtpre(self, isAtpre: str):
        self.__isAtpre = isAtpre

    @property
    def org_behavior_UnresolvedCall59(self):
        return self.__org_behavior_UnresolvedCall59

    @org_behavior_UnresolvedCall59.setter
    def org_behavior_UnresolvedCall59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_UnresolvedCall__org_behavior_UnresolvedCall59", None)
        self.__org_behavior_UnresolvedCall59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Type60"):
                opp_val = getattr(old_value, "structure_Type60", None)
                if opp_val == self:
                    setattr(old_value, "structure_Type60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Type60"):
                opp_val = getattr(value, "structure_Type60", None)
                setattr(value, "structure_Type60", self)

    @property
    def org_behavior_UnresolvedCall56(self):
        return self.__org_behavior_UnresolvedCall56

    @org_behavior_UnresolvedCall56.setter
    def org_behavior_UnresolvedCall56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_UnresolvedCall__org_behavior_UnresolvedCall56", None)
        self.__org_behavior_UnresolvedCall56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression57"):
                opp_val = getattr(old_value, "behavior_Expression57", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression57"):
                opp_val = getattr(value, "behavior_Expression57", None)
                setattr(value, "behavior_Expression57", self)

    @property
    def org_behavior_UnresolvedCall62(self):
        return self.__org_behavior_UnresolvedCall62

    @org_behavior_UnresolvedCall62.setter
    def org_behavior_UnresolvedCall62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_UnresolvedCall__org_behavior_UnresolvedCall62", None)
        self.__org_behavior_UnresolvedCall62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Type63"):
                    opp_val = getattr(item, "structure_Type63", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type63"):
                    opp_val = getattr(item, "structure_Type63", None)
                    
                    setattr(item, "structure_Type63", self)
                    

    @property
    def org_behavior_UnresolvedCall(self):
        return self.__org_behavior_UnresolvedCall

    @org_behavior_UnresolvedCall.setter
    def org_behavior_UnresolvedCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_behavior_UnresolvedCall__org_behavior_UnresolvedCall", None)
        self.__org_behavior_UnresolvedCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Using"):
                    opp_val = getattr(item, "structure_Using", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Using", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Using"):
                    opp_val = getattr(item, "structure_Using", None)
                    
                    setattr(item, "structure_Using", self)
                    

class structure_KermetaModelElement:

    pass
class org_structure_Metamodel(structure_KermetaModelElement, structure_NamedElement, structure_ModelTypeDefinitionContainer):

    def __init__(self, uri: str, isResolved: bool, org_structure_Metamodel: set["structure_Package"] = None, org_structure_Metamodel168: set["structure_FilteredMetamodelReference"] = None, structure_KermetaModelElement: "org_structure_Model", kermeta145: "org_structure_Tag", structure_KermetaModelElement238: "org_structure_UseAdaptationOperator"):
        self.uri = uri
        self.isResolved = isResolved
        self.org_structure_Metamodel = org_structure_Metamodel if org_structure_Metamodel is not None else set()
        self.org_structure_Metamodel168 = org_structure_Metamodel168 if org_structure_Metamodel168 is not None else set()
        
    @property
    def isResolved(self) -> bool:
        return self.__isResolved

    @isResolved.setter
    def isResolved(self, isResolved: bool):
        self.__isResolved = isResolved

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def org_structure_Metamodel(self):
        return self.__org_structure_Metamodel

    @org_structure_Metamodel.setter
    def org_structure_Metamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Metamodel__org_structure_Metamodel", None)
        self.__org_structure_Metamodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_Package"):
                    opp_val = getattr(item, "structure_Package", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Package"):
                    opp_val = getattr(item, "structure_Package", None)
                    
                    setattr(item, "structure_Package", self)
                    

    @property
    def org_structure_Metamodel168(self):
        return self.__org_structure_Metamodel168

    @org_structure_Metamodel168.setter
    def org_structure_Metamodel168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_org_structure_Metamodel__org_structure_Metamodel168", None)
        self.__org_structure_Metamodel168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "structure_FilteredMetamodelReference"):
                    opp_val = getattr(item, "structure_FilteredMetamodelReference", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_FilteredMetamodelReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_FilteredMetamodelReference"):
                    opp_val = getattr(item, "structure_FilteredMetamodelReference", None)
                    
                    setattr(item, "structure_FilteredMetamodelReference", self)
                    

class org_structure_TypeVariableBinding(structure_TypeContainer, structure_KermetaModelElement):

    pass
class org_structure_ModelTypeDefinitionBinding(structure_KermetaModelElement, structure_ModelTypeDefinitionContainer):

    pass
class org_behavior_Expression(structure_TypeContainer, structure_KermetaModelElement):

    pass