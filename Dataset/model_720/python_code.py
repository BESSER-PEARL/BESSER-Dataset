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

class behavior_Rescue:

    pass
class structure_Type:

    pass
class behavior_Expression:

    pass
class behavior_CallExpression:

    pass
class Expression:

    pass
class kermeta_behavior_Block(Expression):

    pass
class kermeta_behavior_CallExpression(Expression):

    def __init__(self, name: str, kermeta_behavior_CallExpression: set["behavior_Expression"] = None, kermeta_behavior_CallExpression7: set["structure_Type"] = None):
        self.name = name
        self.kermeta_behavior_CallExpression = kermeta_behavior_CallExpression if kermeta_behavior_CallExpression is not None else set()
        self.kermeta_behavior_CallExpression7 = kermeta_behavior_CallExpression7 if kermeta_behavior_CallExpression7 is not None else set()
        
        pass
    @property
    def name(self):
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
                    

class kermeta_behavior_Assignment(Expression):

    def __init__(self, isCast: str, kermeta_behavior_Assignment: "behavior_CallExpression" = None, kermeta_behavior_Assignment2: "behavior_Expression" = None):
        self.isCast = isCast
        self.kermeta_behavior_Assignment = kermeta_behavior_Assignment
        self.kermeta_behavior_Assignment2 = kermeta_behavior_Assignment2
        
        pass
    @property
    def isCast(self):
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
class structure_TypeContainer:

    pass
class structure_Object:

    pass
class kermeta_behavior_Expression(structure_TypeContainer, structure_Object):

    pass
class kermeta_structure_FunctionType(structure_TypeContainer, structure_Type):

    pass
class kermeta_structure_ProductType(structure_TypeContainer, structure_Type):

    pass
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
class kermeta_structure_ClassDefinition(structure_TypeContainer, structure_GenericTypeDefinition):

    def __init__(self, isAbstract: str, invOwner: set["structure_Constraint"] = None, owningClass: set["structure_Property"] = None, owningClass124: set["structure_Operation"] = None, kermeta_structure_ClassDefinition: set["structure_Type"] = None, structure_GenericTypeDefinition: "kermeta_structure_ParameterizedType" = None, TypeContainer: "kermeta_structure_Type" = None):
        self.isAbstract = isAbstract
        self.invOwner = invOwner if invOwner is not None else set()
        self.owningClass = owningClass if owningClass is not None else set()
        self.owningClass124 = owningClass124 if owningClass124 is not None else set()
        self.kermeta_structure_ClassDefinition = kermeta_structure_ClassDefinition if kermeta_structure_ClassDefinition is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def owningClass(self):
        return self.__owningClass

    @owningClass.setter
    def owningClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_ClassDefinition__owningClass", None)
        self.__owningClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def owningClass124(self):
        return self.__owningClass124

    @owningClass124.setter
    def owningClass124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_ClassDefinition__owningClass124", None)
        self.__owningClass124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation125"):
                    opp_val = getattr(item, "Operation125", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation125"):
                    opp_val = getattr(item, "Operation125", None)
                    
                    setattr(item, "Operation125", self)
                    

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
                if hasattr(item, "structure_Type127"):
                    opp_val = getattr(item, "structure_Type127", None)
                    
                    if opp_val == self:
                        setattr(item, "structure_Type127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "structure_Type127"):
                    opp_val = getattr(item, "structure_Type127", None)
                    
                    setattr(item, "structure_Type127", self)
                    

    @property
    def invOwner(self):
        return self.__invOwner

    @invOwner.setter
    def invOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_ClassDefinition__invOwner", None)
        self.__invOwner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint121"):
                    opp_val = getattr(item, "Constraint121", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint121"):
                    opp_val = getattr(item, "Constraint121", None)
                    
                    setattr(item, "Constraint121", self)
                    

class structure_DataType:

    pass
class kermeta_structure_PrimitiveType(structure_DataType, structure_TypeContainer):

    pass
class structure_Package:

    pass
class structure_TypeDefinitionContainer:

    pass
class structure_NamedElement:

    pass
class kermeta_structure_TypeVariable(structure_TypeContainer, structure_NamedElement, structure_Type):

    pass
class kermeta_structure_TypedElement(structure_TypeContainer, structure_NamedElement):

    pass
class kermeta_structure_Package(structure_TypeDefinitionContainer, structure_NamedElement):

    def __init__(self, uri: str, nestingPackage: set["structure_Package"] = None, nestedPackage: "structure_Package" = None):
        self.uri = uri
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.nestedPackage = nestedPackage
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def nestingPackage(self):
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Package__nestingPackage", None)
        self.__nestingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    if opp_val == self:
                        setattr(item, "Package", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package"):
                    opp_val = getattr(item, "Package", None)
                    
                    setattr(item, "Package", self)
                    

    @property
    def nestedPackage(self):
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Package__nestedPackage", None)
        self.__nestedPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package105"):
                opp_val = getattr(old_value, "Package105", None)
                if opp_val == self:
                    setattr(old_value, "Package105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package105"):
                opp_val = getattr(value, "Package105", None)
                setattr(value, "Package105", self)

class DataType:

    pass
class kermeta_structure_Enumeration(DataType):

    pass
class TypedElement:

    pass
class kermeta_structure_MultiplicityElement(TypedElement):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
        pass
    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered


    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


class kermeta_structure_TypeVariableBinding(structure_TypeContainer, structure_Object):

    pass
class structure_Enumeration:

    pass
class NamedElement:

    pass
class kermeta_structure_TypeDefinitionContainer(NamedElement):

    pass
class kermeta_structure_TypeDefinition(NamedElement):

    def __init__(self, isAspect: str):
        self.isAspect = isAspect
        
        pass
    @property
    def isAspect(self):
        return self.__isAspect

    @isAspect.setter
    def isAspect(self, isAspect: str):
        self.__isAspect = isAspect


class kermeta_structure_Constraint(NamedElement):

    def __init__(self, stereotype: str, language: str, kermeta_structure_Constraint: "behavior_Expression" = None, inv: "structure_ClassDefinition" = None, pre: "structure_Operation" = None, post: "structure_Operation" = None):
        self.stereotype = stereotype
        self.language = language
        self.kermeta_structure_Constraint = kermeta_structure_Constraint
        self.inv = inv
        self.pre = pre
        self.post = post
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def stereotype(self):
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype


    @property
    def inv(self):
        return self.__inv

    @inv.setter
    def inv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Constraint__inv", None)
        self.__inv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDefinition115"):
                opp_val = getattr(old_value, "ClassDefinition115", None)
                if opp_val == self:
                    setattr(old_value, "ClassDefinition115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDefinition115"):
                opp_val = getattr(value, "ClassDefinition115", None)
                setattr(value, "ClassDefinition115", self)

    @property
    def post(self):
        return self.__post

    @post.setter
    def post(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Constraint__post", None)
        self.__post = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation119"):
                opp_val = getattr(old_value, "Operation119", None)
                if opp_val == self:
                    setattr(old_value, "Operation119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation119"):
                opp_val = getattr(value, "Operation119", None)
                setattr(value, "Operation119", self)

    @property
    def pre(self):
        return self.__pre

    @pre.setter
    def pre(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Constraint__pre", None)
        self.__pre = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation117"):
                opp_val = getattr(old_value, "Operation117", None)
                if opp_val == self:
                    setattr(old_value, "Operation117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation117"):
                opp_val = getattr(value, "Operation117", None)
                setattr(value, "Operation117", self)

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
            if hasattr(old_value, "behavior_Expression113"):
                opp_val = getattr(old_value, "behavior_Expression113", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression113"):
                opp_val = getattr(value, "behavior_Expression113", None)
                setattr(value, "behavior_Expression113", self)

class kermeta_structure_EnumerationLiteral(NamedElement):

    pass
class structure_TypeVariable:

    pass
class structure_ClassDefinition:

    pass
class structure_Constraint:

    pass
class structure_Parameter:

    pass
class structure_TypeDefinition:

    pass
class kermeta_structure_DataType(structure_TypeDefinition, structure_Type):

    pass
class kermeta_structure_ModelType(structure_TypeDefinition, structure_Type):

    def __init__(self, kermeta_structure_ModelType: set["structure_TypeDefinition"] = None, structure_TypeDefinition164: "kermeta_structure_TypeDefinitionContainer" = None, structure_TypeDefinition: "kermeta_structure_ModelType" = None, structure_Type108: "kermeta_structure_PrimitiveType" = None, structure_Type110: "kermeta_structure_TypedElement" = None, structure_Type159: "kermeta_structure_FunctionType" = None, structure_Type162: "kermeta_structure_FunctionType" = None, structure_Type8: "kermeta_behavior_CallExpression" = None, structure_Type101: "kermeta_structure_TypeVariableBinding" = None, structure_Type70: "kermeta_structure_Operation" = None, structure_Type: "kermeta_behavior_Expression" = None, structure_Type157: "kermeta_structure_ProductType" = None, structure_Type149: "kermeta_structure_TypeVariable" = None, structure_Type127: "kermeta_structure_ClassDefinition" = None, Type: "kermeta_structure_TypeContainer" = None):
        self.kermeta_structure_ModelType = kermeta_structure_ModelType if kermeta_structure_ModelType is not None else set()
        
        pass
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
                    

    def _new(self) :
        # TODO: Implement _new method
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

    def __init__(self, isAbstract: str, name: str, kermeta_structure_Class64: set["structure_Class"] = None, kermeta_structure_Class: set["structure_Property"] = None, kermeta_structure_Class61: set["structure_Operation"] = None):
        self.isAbstract = isAbstract
        self.name = name
        self.kermeta_structure_Class64 = kermeta_structure_Class64 if kermeta_structure_Class64 is not None else set()
        self.kermeta_structure_Class = kermeta_structure_Class if kermeta_structure_Class is not None else set()
        self.kermeta_structure_Class61 = kermeta_structure_Class61 if kermeta_structure_Class61 is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
                    

    def _new(self) :
        # TODO: Implement _new method
        pass

class kermeta_behavior_VariableDecl(Expression):

    def __init__(self, identifier: str, kermeta_behavior_VariableDecl: "behavior_Expression" = None, kermeta_behavior_VariableDecl56: "behavior_TypeReference" = None):
        self.identifier = identifier
        self.kermeta_behavior_VariableDecl = kermeta_behavior_VariableDecl
        self.kermeta_behavior_VariableDecl56 = kermeta_behavior_VariableDecl56
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


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

class kermeta_behavior_SelfExpression(Expression):

    pass
class Literal:

    pass
class kermeta_behavior_TypeLiteral(Literal):

    pass
class kermeta_behavior_VoidLiteral(Literal):

    pass
class kermeta_behavior_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class kermeta_behavior_BooleanLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class kermeta_behavior_IntegerLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class behavior_LambdaParameter:

    pass
class kermeta_behavior_LambdaExpression(Expression):

    pass
class kermeta_behavior_JavaStaticCall(Expression):

    def __init__(self, jclass: str, jmethod: str, kermeta_behavior_JavaStaticCall: set["behavior_Expression"] = None):
        self.jclass = jclass
        self.jmethod = jmethod
        self.kermeta_behavior_JavaStaticCall = kermeta_behavior_JavaStaticCall if kermeta_behavior_JavaStaticCall is not None else set()
        
        pass
    @property
    def jclass(self):
        return self.__jclass

    @jclass.setter
    def jclass(self, jclass: str):
        self.__jclass = jclass


    @property
    def jmethod(self):
        return self.__jmethod

    @jmethod.setter
    def jmethod(self, jmethod: str):
        self.__jmethod = jmethod


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
                    

class kermeta_behavior_Loop(Expression):

    pass
class kermeta_behavior_Literal(Expression):

    pass
class MultiplicityElement:

    pass
class kermeta_structure_Property(MultiplicityElement):

    def __init__(self, isReadOnly: str, default: str, isComposite: str, isDerived: str, isID: str, isGetterAbstract: str, isSetterAbstract: str, kermeta_structure_Property: "structure_Property" = None, kermeta_structure_Property87: "behavior_Expression" = None, kermeta_structure_Property90: "behavior_Expression" = None, ownedAttribute: "structure_ClassDefinition" = None):
        self.isReadOnly = isReadOnly
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.isGetterAbstract = isGetterAbstract
        self.isSetterAbstract = isSetterAbstract
        self.kermeta_structure_Property = kermeta_structure_Property
        self.kermeta_structure_Property87 = kermeta_structure_Property87
        self.kermeta_structure_Property90 = kermeta_structure_Property90
        self.ownedAttribute = ownedAttribute
        
        pass
    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def isID(self):
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID


    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


    @property
    def isSetterAbstract(self):
        return self.__isSetterAbstract

    @isSetterAbstract.setter
    def isSetterAbstract(self, isSetterAbstract: str):
        self.__isSetterAbstract = isSetterAbstract


    @property
    def isGetterAbstract(self):
        return self.__isGetterAbstract

    @isGetterAbstract.setter
    def isGetterAbstract(self, isGetterAbstract: str):
        self.__isGetterAbstract = isGetterAbstract


    @property
    def kermeta_structure_Property87(self):
        return self.__kermeta_structure_Property87

    @kermeta_structure_Property87.setter
    def kermeta_structure_Property87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Property__kermeta_structure_Property87", None)
        self.__kermeta_structure_Property87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression88"):
                opp_val = getattr(old_value, "behavior_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression88"):
                opp_val = getattr(value, "behavior_Expression88", None)
                setattr(value, "behavior_Expression88", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDefinition93"):
                opp_val = getattr(old_value, "ClassDefinition93", None)
                if opp_val == self:
                    setattr(old_value, "ClassDefinition93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDefinition93"):
                opp_val = getattr(value, "ClassDefinition93", None)
                setattr(value, "ClassDefinition93", self)

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
            if hasattr(old_value, "structure_Property85"):
                opp_val = getattr(old_value, "structure_Property85", None)
                if opp_val == self:
                    setattr(old_value, "structure_Property85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Property85"):
                opp_val = getattr(value, "structure_Property85", None)
                setattr(value, "structure_Property85", self)

    @property
    def kermeta_structure_Property90(self):
        return self.__kermeta_structure_Property90

    @kermeta_structure_Property90.setter
    def kermeta_structure_Property90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Property__kermeta_structure_Property90", None)
        self.__kermeta_structure_Property90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression91"):
                opp_val = getattr(old_value, "behavior_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression91"):
                opp_val = getattr(value, "behavior_Expression91", None)
                setattr(value, "behavior_Expression91", self)

class kermeta_structure_Parameter(MultiplicityElement):

    pass
class kermeta_structure_Operation(MultiplicityElement):

    def __init__(self, isAbstract: str, kermeta_structure_Operation: set["structure_Type"] = None, operation: set["structure_Parameter"] = None, preOwner: set["structure_Constraint"] = None, postOwner: set["structure_Constraint"] = None, kermeta_structure_Operation76: "behavior_Expression" = None, kermeta_structure_Operation79: "structure_Operation" = None, ownedOperation: "structure_ClassDefinition" = None, kermeta_structure_Operation83: set["structure_TypeVariable"] = None):
        self.isAbstract = isAbstract
        self.kermeta_structure_Operation = kermeta_structure_Operation if kermeta_structure_Operation is not None else set()
        self.operation = operation if operation is not None else set()
        self.preOwner = preOwner if preOwner is not None else set()
        self.postOwner = postOwner if postOwner is not None else set()
        self.kermeta_structure_Operation76 = kermeta_structure_Operation76
        self.kermeta_structure_Operation79 = kermeta_structure_Operation79
        self.ownedOperation = ownedOperation
        self.kermeta_structure_Operation83 = kermeta_structure_Operation83 if kermeta_structure_Operation83 is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__operation", None)
        self.__operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def preOwner(self):
        return self.__preOwner

    @preOwner.setter
    def preOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__preOwner", None)
        self.__preOwner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def postOwner(self):
        return self.__postOwner

    @postOwner.setter
    def postOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__postOwner", None)
        self.__postOwner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint74"):
                    opp_val = getattr(item, "Constraint74", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint74"):
                    opp_val = getattr(item, "Constraint74", None)
                    
                    setattr(item, "Constraint74", self)
                    

    @property
    def kermeta_structure_Operation79(self):
        return self.__kermeta_structure_Operation79

    @kermeta_structure_Operation79.setter
    def kermeta_structure_Operation79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__kermeta_structure_Operation79", None)
        self.__kermeta_structure_Operation79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "structure_Operation80"):
                opp_val = getattr(old_value, "structure_Operation80", None)
                if opp_val == self:
                    setattr(old_value, "structure_Operation80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "structure_Operation80"):
                opp_val = getattr(value, "structure_Operation80", None)
                setattr(value, "structure_Operation80", self)

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
    def kermeta_structure_Operation83(self):
        return self.__kermeta_structure_Operation83

    @kermeta_structure_Operation83.setter
    def kermeta_structure_Operation83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__kermeta_structure_Operation83", None)
        self.__kermeta_structure_Operation83 = value if value is not None else set()
        
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
    def kermeta_structure_Operation76(self):
        return self.__kermeta_structure_Operation76

    @kermeta_structure_Operation76.setter
    def kermeta_structure_Operation76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__kermeta_structure_Operation76", None)
        self.__kermeta_structure_Operation76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behavior_Expression77"):
                opp_val = getattr(old_value, "behavior_Expression77", None)
                if opp_val == self:
                    setattr(old_value, "behavior_Expression77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behavior_Expression77"):
                opp_val = getattr(value, "behavior_Expression77", None)
                setattr(value, "behavior_Expression77", self)

    @property
    def ownedOperation(self):
        return self.__ownedOperation

    @ownedOperation.setter
    def ownedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Operation__ownedOperation", None)
        self.__ownedOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassDefinition"):
                opp_val = getattr(old_value, "ClassDefinition", None)
                if opp_val == self:
                    setattr(old_value, "ClassDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassDefinition"):
                opp_val = getattr(value, "ClassDefinition", None)
                setattr(value, "ClassDefinition", self)

class kermeta_behavior_TypeReference(MultiplicityElement):

    pass
class behavior_TypeReference:

    pass
class Object:

    pass
class kermeta_structure_NamedElement(Object):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class kermeta_structure_Type(Object):

    pass
class kermeta_structure_TypeContainer(Object):

    pass
class kermeta_structure_Filter(Object):

    def __init__(self, qualifiedName: str):
        self.qualifiedName = qualifiedName
        
        pass
    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


class kermeta_behavior_LambdaParameter(Object):

    def __init__(self, name: str, kermeta_behavior_LambdaParameter: "behavior_TypeReference" = None):
        self.name = name
        self.kermeta_behavior_LambdaParameter = kermeta_behavior_LambdaParameter
        
        pass
    @property
    def name(self):
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
        
        pass
    @property
    def qualifiedName(self):
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName


class kermeta_structure_Tag(Object):

    def __init__(self, name: str, value: str, tag: set["structure_Object"] = None):
        self.name = name
        self.value = value
        self.tag = tag if tag is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kermeta_structure_Tag__tag", None)
        self.__tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Object"):
                    opp_val = getattr(item, "Object", None)
                    
                    if opp_val == self:
                        setattr(item, "Object", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Object"):
                    opp_val = getattr(item, "Object", None)
                    
                    setattr(item, "Object", self)
                    

class kermeta_structure_ModelingUnit(Object):

    pass
class kermeta_structure_Require(Object):

    def __init__(self, uri: str):
        self.uri = uri
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


class kermeta_structure_Model(Object):

    pass
class kermeta_behavior_Rescue(Object):

    def __init__(self, exceptionName: str, kermeta_behavior_Rescue: set["behavior_Expression"] = None, kermeta_behavior_Rescue34: "behavior_TypeReference" = None):
        self.exceptionName = exceptionName
        self.kermeta_behavior_Rescue = kermeta_behavior_Rescue if kermeta_behavior_Rescue is not None else set()
        self.kermeta_behavior_Rescue34 = kermeta_behavior_Rescue34
        
        pass
    @property
    def exceptionName(self):
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

class kermeta_behavior_Raise(Expression):

    pass
class kermeta_behavior_Conditional(Expression):

    pass
class CallVariable:

    pass
class kermeta_behavior_CallResult(CallVariable):

    pass
class structure_EnumerationLiteral:

    pass
class structure_Operation:

    pass
class kermeta_behavior_EmptyExpression(Expression):

    pass
class structure_Property:

    pass
class CallExpression:

    pass
class kermeta_behavior_CallValue(CallExpression):

    pass
class kermeta_behavior_CallVariable(CallExpression):

    def __init__(self, isAtpre: str):
        self.isAtpre = isAtpre
        
        pass
    @property
    def isAtpre(self):
        return self.__isAtpre

    @isAtpre.setter
    def isAtpre(self, isAtpre: str):
        self.__isAtpre = isAtpre


class kermeta_behavior_CallFeature(CallExpression):

    def __init__(self, isAtpre: str, kermeta_behavior_CallFeature: "behavior_Expression" = None, kermeta_behavior_CallFeature16: "structure_Property" = None, kermeta_behavior_CallFeature18: "structure_Operation" = None, kermeta_behavior_CallFeature20: "structure_EnumerationLiteral" = None):
        self.isAtpre = isAtpre
        self.kermeta_behavior_CallFeature = kermeta_behavior_CallFeature
        self.kermeta_behavior_CallFeature16 = kermeta_behavior_CallFeature16
        self.kermeta_behavior_CallFeature18 = kermeta_behavior_CallFeature18
        self.kermeta_behavior_CallFeature20 = kermeta_behavior_CallFeature20
        
        pass
    @property
    def isAtpre(self):
        return self.__isAtpre

    @isAtpre.setter
    def isAtpre(self, isAtpre: str):
        self.__isAtpre = isAtpre


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