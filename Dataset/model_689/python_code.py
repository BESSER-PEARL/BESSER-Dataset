from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionKind(Enum):
    OrderedSet = "OrderedSet"
    Set = "Set"
    Bag = "Bag"
    Sequence = "Sequence"
class SeverityKind(Enum):
    error = "error"
    fatal = "fatal"
    warning = "warning"


############################################
# Definition of Classes
############################################

class AnonymousTupleLiteralPart:

    pass
class essentialocl_LoopExp:

    pass
class DictLiteralPart:

    pass
class LogExp:

    pass
class AltExp:

    pass
class imperativeocl_ImperativeExpression:

    pass
class Janus_imperativeocl_ImperativeLoopExp(essentialocl_LoopExp, imperativeocl_ImperativeExpression):

    pass
class ComputeExp:

    pass
class LetExp:

    pass
class LoopExp:

    pass
class Janus_essentialocl_IteratorExp(LoopExp):

    pass
class essentialocl_OclExpression:

    pass
class essentialocl_CallExp:

    pass
class Janus_imperativeocl_SwitchExp(imperativeocl_ImperativeExpression, essentialocl_CallExp):

    pass
class PrimitiveLiteralExp:

    pass
class Janus_essentialocl_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class Janus_essentialocl_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: bool):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: bool):
        self.__booleanSymbol = booleanSymbol


class OclExpression:

    pass
class Janus_essentialocl_CallExp(OclExpression):

    pass
class Janus_essentialocl_LetExp(OclExpression):

    pass
class Janus_imperativeocl_ImperativeExpression(OclExpression):

    pass
class TemplateExp:

    pass
class Predicate:

    pass
class Janus_essentialocl_IfExp(OclExpression):

    pass
class NumericLiteralExp:

    pass
class Janus_essentialocl_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: float):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: float):
        self.__realSymbol = realSymbol


class Janus_essentialocl_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: int):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: int):
        self.__integerSymbol = integerSymbol


class Janus_essentialocl_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


class TryExp:

    pass
class TypedElement:

    pass
class Janus_essentialocl_Variable(TypedElement):

    def __init__(self, varType: str, Janus_essentialocl_Variable: "OclExpression" = None, variable: "LetExp" = None, Janus_essentialocl_Variable89: "Parameter" = None, returnedElement: "ComputeExp" = None):
        self.varType = varType
        self.Janus_essentialocl_Variable = Janus_essentialocl_Variable
        self.variable = variable
        self.Janus_essentialocl_Variable89 = Janus_essentialocl_Variable89
        self.returnedElement = returnedElement
        
        pass
    @property
    def varType(self):
        return self.__varType

    @varType.setter
    def varType(self, varType: str):
        self.__varType = varType


    @property
    def Janus_essentialocl_Variable(self):
        return self.__Janus_essentialocl_Variable

    @Janus_essentialocl_Variable.setter
    def Janus_essentialocl_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_essentialocl_Variable__Janus_essentialocl_Variable", None)
        self.__Janus_essentialocl_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression85"):
                opp_val = getattr(old_value, "OclExpression85", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression85"):
                opp_val = getattr(value, "OclExpression85", None)
                setattr(value, "OclExpression85", self)

    @property
    def Janus_essentialocl_Variable89(self):
        return self.__Janus_essentialocl_Variable89

    @Janus_essentialocl_Variable89.setter
    def Janus_essentialocl_Variable89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_essentialocl_Variable__Janus_essentialocl_Variable89", None)
        self.__Janus_essentialocl_Variable89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter90"):
                opp_val = getattr(old_value, "Parameter90", None)
                if opp_val == self:
                    setattr(old_value, "Parameter90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter90"):
                opp_val = getattr(value, "Parameter90", None)
                setattr(value, "Parameter90", self)

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_essentialocl_Variable__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp87"):
                opp_val = getattr(old_value, "LetExp87", None)
                if opp_val == self:
                    setattr(old_value, "LetExp87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp87"):
                opp_val = getattr(value, "LetExp87", None)
                setattr(value, "LetExp87", self)

    @property
    def returnedElement(self):
        return self.__returnedElement

    @returnedElement.setter
    def returnedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_essentialocl_Variable__returnedElement", None)
        self.__returnedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComputeExp"):
                opp_val = getattr(old_value, "ComputeExp", None)
                if opp_val == self:
                    setattr(old_value, "ComputeExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComputeExp"):
                opp_val = getattr(value, "ComputeExp", None)
                setattr(value, "ComputeExp", self)

class Janus_essentialocl_OclExpression(TypedElement):

    pass
class Pattern:

    pass
class Domain:

    pass
class Transformation:

    pass
class Relation:

    pass
class Model:

    pass
class emof_Package:

    pass
class emof_Class:

    pass
class Janus_JTL_Transformation(emof_Class, emof_Package):

    pass
class Extent:

    pass
class Janus_emof_URIExtent(Extent):

    pass
class Variable:

    pass
class Package:

    pass
class NamedElement:

    pass
class Janus_JTL_Model(NamedElement):

    pass
class Janus_JTL_Domain(NamedElement):

    def __init__(self, isCheckable: bool, isEnforceable: bool, domain: "Relation" = None, Janus_JTL_Domain: "Pattern" = None, Janus_JTL_Domain42: "Model" = None, Janus_JTL_Domain45: "Variable" = None, NamedElement: "Janus_emof_Comment" = None):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.domain = domain
        self.Janus_JTL_Domain = Janus_JTL_Domain
        self.Janus_JTL_Domain42 = Janus_JTL_Domain42
        self.Janus_JTL_Domain45 = Janus_JTL_Domain45
        
        pass
    @property
    def isCheckable(self):
        return self.__isCheckable

    @isCheckable.setter
    def isCheckable(self, isCheckable: bool):
        self.__isCheckable = isCheckable


    @property
    def isEnforceable(self):
        return self.__isEnforceable

    @isEnforceable.setter
    def isEnforceable(self, isEnforceable: bool):
        self.__isEnforceable = isEnforceable


    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Domain__domain", None)
        self.__domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relation38"):
                opp_val = getattr(old_value, "Relation38", None)
                if opp_val == self:
                    setattr(old_value, "Relation38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relation38"):
                opp_val = getattr(value, "Relation38", None)
                setattr(value, "Relation38", self)

    @property
    def Janus_JTL_Domain45(self):
        return self.__Janus_JTL_Domain45

    @Janus_JTL_Domain45.setter
    def Janus_JTL_Domain45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Domain__Janus_JTL_Domain45", None)
        self.__Janus_JTL_Domain45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable46"):
                opp_val = getattr(old_value, "Variable46", None)
                if opp_val == self:
                    setattr(old_value, "Variable46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable46"):
                opp_val = getattr(value, "Variable46", None)
                setattr(value, "Variable46", self)

    @property
    def Janus_JTL_Domain(self):
        return self.__Janus_JTL_Domain

    @Janus_JTL_Domain.setter
    def Janus_JTL_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Domain__Janus_JTL_Domain", None)
        self.__Janus_JTL_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern40"):
                opp_val = getattr(old_value, "Pattern40", None)
                if opp_val == self:
                    setattr(old_value, "Pattern40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern40"):
                opp_val = getattr(value, "Pattern40", None)
                setattr(value, "Pattern40", self)

    @property
    def Janus_JTL_Domain42(self):
        return self.__Janus_JTL_Domain42

    @Janus_JTL_Domain42.setter
    def Janus_JTL_Domain42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Domain__Janus_JTL_Domain42", None)
        self.__Janus_JTL_Domain42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model43"):
                opp_val = getattr(old_value, "Model43", None)
                if opp_val == self:
                    setattr(old_value, "Model43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model43"):
                opp_val = getattr(value, "Model43", None)
                setattr(value, "Model43", self)

class Janus_JTL_Relation(NamedElement):

    def __init__(self, isTopLevel: bool, whenOwner: "Pattern" = None, Janus_JTL_Relation: set["Variable"] = None, relation: "Transformation" = None, relation32: set["Domain"] = None, whereOwner: "Pattern" = None, NamedElement: "Janus_emof_Comment" = None):
        self.isTopLevel = isTopLevel
        self.whenOwner = whenOwner
        self.Janus_JTL_Relation = Janus_JTL_Relation if Janus_JTL_Relation is not None else set()
        self.relation = relation
        self.relation32 = relation32 if relation32 is not None else set()
        self.whereOwner = whereOwner
        
        pass
    @property
    def isTopLevel(self):
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: bool):
        self.__isTopLevel = isTopLevel


    @property
    def relation32(self):
        return self.__relation32

    @relation32.setter
    def relation32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Relation__relation32", None)
        self.__relation32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Domain"):
                    opp_val = getattr(item, "Domain", None)
                    
                    if opp_val == self:
                        setattr(item, "Domain", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Domain"):
                    opp_val = getattr(item, "Domain", None)
                    
                    setattr(item, "Domain", self)
                    

    @property
    def whenOwner(self):
        return self.__whenOwner

    @whenOwner.setter
    def whenOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Relation__whenOwner", None)
        self.__whenOwner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern35"):
                opp_val = getattr(old_value, "Pattern35", None)
                if opp_val == self:
                    setattr(old_value, "Pattern35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern35"):
                opp_val = getattr(value, "Pattern35", None)
                setattr(value, "Pattern35", self)

    @property
    def whereOwner(self):
        return self.__whereOwner

    @whereOwner.setter
    def whereOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Relation__whereOwner", None)
        self.__whereOwner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern"):
                opp_val = getattr(old_value, "Pattern", None)
                if opp_val == self:
                    setattr(old_value, "Pattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern"):
                opp_val = getattr(value, "Pattern", None)
                setattr(value, "Pattern", self)

    @property
    def relation(self):
        return self.__relation

    @relation.setter
    def relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Relation__relation", None)
        self.__relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transformation"):
                opp_val = getattr(old_value, "Transformation", None)
                if opp_val == self:
                    setattr(old_value, "Transformation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transformation"):
                opp_val = getattr(value, "Transformation", None)
                setattr(value, "Transformation", self)

    @property
    def Janus_JTL_Relation(self):
        return self.__Janus_JTL_Relation

    @Janus_JTL_Relation.setter
    def Janus_JTL_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_JTL_Relation__Janus_JTL_Relation", None)
        self.__Janus_JTL_Relation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    setattr(item, "Variable", self)
                    

class Janus_emof_TypedElement(NamedElement):

    pass
class Janus_emof_Type(NamedElement):

    pass
class Janus_emof_Package(NamedElement):

    def __init__(self, uri: str, package: set["Type"] = None, Janus_emof_Package: set["Package"] = None, NamedElement: "Janus_emof_Comment" = None):
        self.uri = uri
        self.package = package if package is not None else set()
        self.Janus_emof_Package = Janus_emof_Package if Janus_emof_Package is not None else set()
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def Janus_emof_Package(self):
        return self.__Janus_emof_Package

    @Janus_emof_Package.setter
    def Janus_emof_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Package__Janus_emof_Package", None)
        self.__Janus_emof_Package = value if value is not None else set()
        
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
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Package__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type13"):
                    opp_val = getattr(item, "Type13", None)
                    
                    if opp_val == self:
                        setattr(item, "Type13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type13"):
                    opp_val = getattr(item, "Type13", None)
                    
                    setattr(item, "Type13", self)
                    

class Janus_emof_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: int, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
        pass
    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


    @property
    def isOrdered(self):
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


class Parameter:

    pass
class emof_TypedElement:

    pass
class emof_MultiplicityElement:

    pass
class Janus_emof_Operation(emof_TypedElement, emof_MultiplicityElement):

    pass
class Janus_emof_Object:

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class Janus_emof_PrimitiveType(DataType):

    pass
class Janus_emof_Enumeration(DataType):

    pass
class Janus_emof_Property(emof_TypedElement, emof_MultiplicityElement):

    def __init__(self, isReadOnly: bool, isDerived: bool, isComposite: bool, isId: bool, default: str, ownedAttribute: "Class" = None, Janus_emof_Property: "Property" = None):
        self.isReadOnly = isReadOnly
        self.isDerived = isDerived
        self.isComposite = isComposite
        self.isId = isId
        self.default = default
        self.ownedAttribute = ownedAttribute
        self.Janus_emof_Property = Janus_emof_Property
        
        pass
    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived


    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite


    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def isId(self):
        return self.__isId

    @isId.setter
    def isId(self, isId: bool):
        self.__isId = isId


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly


    @property
    def Janus_emof_Property(self):
        return self.__Janus_emof_Property

    @Janus_emof_Property.setter
    def Janus_emof_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Property__Janus_emof_Property", None)
        self.__Janus_emof_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property23"):
                opp_val = getattr(old_value, "Property23", None)
                if opp_val == self:
                    setattr(old_value, "Property23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property23"):
                opp_val = getattr(value, "Property23", None)
                setattr(value, "Property23", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class21"):
                opp_val = getattr(old_value, "Class21", None)
                if opp_val == self:
                    setattr(old_value, "Class21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class21"):
                opp_val = getattr(value, "Class21", None)
                setattr(value, "Class21", self)

class Enumeration:

    pass
class Janus_emof_EnumerationLiteral(NamedElement):

    pass
class Janus_emof_Parameter(emof_TypedElement, emof_MultiplicityElement):

    pass
class Operation:

    pass
class Property:

    pass
class Type:

    pass
class Janus_imperativeocl_TemplateParameterType(Type):

    def __init__(self, specification: str, Type212: "Janus_imperativeocl_Typedef" = None, Type248: "Janus_imperativeocl_AnonymousTupleType" = None, Type225: "Janus_imperativeocl_DictionaryType" = None, Type: "Janus_emof_Operation" = None, Type97: "Janus_essentialocl_TypeExp" = None, Type203: "Janus_imperativeocl_TryExp" = None, Type138: "Janus_essentialocl_CollectionType" = None, Type208: "Janus_imperativeocl_RaiseExp" = None, Type13: "Janus_emof_Package" = None, Type25: "Janus_emof_TypedElement" = None):
        self.specification = specification
        
        pass
    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


class Janus_emof_Class(Type):

    def __init__(self, isAbstract: bool, Janus_emof_Class: set["Class"] = None, Class: set["Property"] = None, class_: set["Operation"] = None, Type212: "Janus_imperativeocl_Typedef" = None, Type248: "Janus_imperativeocl_AnonymousTupleType" = None, Type225: "Janus_imperativeocl_DictionaryType" = None, Type: "Janus_emof_Operation" = None, Type97: "Janus_essentialocl_TypeExp" = None, Type203: "Janus_imperativeocl_TryExp" = None, Type138: "Janus_essentialocl_CollectionType" = None, Type208: "Janus_imperativeocl_RaiseExp" = None, Type13: "Janus_emof_Package" = None, Type25: "Janus_emof_TypedElement" = None):
        self.isAbstract = isAbstract
        self.Janus_emof_Class = Janus_emof_Class if Janus_emof_Class is not None else set()
        self.Class = Class if Class is not None else set()
        self.class_ = class_ if class_ is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract


    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Class__class_", None)
        self.__class_ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Class__Class", None)
        self.__Class = value if value is not None else set()
        
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
    def Janus_emof_Class(self):
        return self.__Janus_emof_Class

    @Janus_emof_Class.setter
    def Janus_emof_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_emof_Class__Janus_emof_Class", None)
        self.__Janus_emof_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class3"):
                    opp_val = getattr(item, "Class3", None)
                    
                    if opp_val == self:
                        setattr(item, "Class3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class3"):
                    opp_val = getattr(item, "Class3", None)
                    
                    setattr(item, "Class3", self)
                    

class Element:

    pass
class Janus_imperativeocl_AnonymousTupleLiteralPart(Element):

    pass
class Janus_JTL_Predicate(Element):

    pass
class Janus_emof_Comment(Element):

    pass
class Janus_JTL_Pattern(Element):

    pass
class Janus_emof_NamedElement(Element):

    def __init__(self, name: str, Element: "Janus_emof_Tag" = None, Element236: "Janus_imperativeocl_LogExp" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Janus_imperativeocl_DictLiteralPart(Element):

    pass
class Janus_emof_Tag(Element):

    def __init__(self, value: str, name: str, tag: set["Element"] = None, Element: "Janus_emof_Tag" = None, Element236: "Janus_imperativeocl_LogExp" = None):
        self.value = value
        self.name = name
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
        old_value = getattr(self, f"_Janus_emof_Tag__tag", None)
        self.__tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

class Comment:

    pass
class Tag:

    pass
class Object:

    pass
class Janus_emof_Extent(Object):

    pass
class Janus_emof_Element(Object):

    pass
class Janus_emof_DataType(Type):

    pass
class Class:

    pass
class Janus_imperativeocl_AnonymousTupleType(Class):

    pass
class Janus_imperativeocl_Typedef(Class):

    pass
class ImperativeExpression:

    pass
class Janus_imperativeocl_RaiseExp(ImperativeExpression):

    pass
class Janus_imperativeocl_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: bool, Janus_imperativeocl_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.Janus_imperativeocl_VariableInitExp = Janus_imperativeocl_VariableInitExp
        
        pass
    @property
    def withResult(self):
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: bool):
        self.__withResult = withResult


    @property
    def Janus_imperativeocl_VariableInitExp(self):
        return self.__Janus_imperativeocl_VariableInitExp

    @Janus_imperativeocl_VariableInitExp.setter
    def Janus_imperativeocl_VariableInitExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_VariableInitExp__Janus_imperativeocl_VariableInitExp", None)
        self.__Janus_imperativeocl_VariableInitExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable178"):
                opp_val = getattr(old_value, "Variable178", None)
                if opp_val == self:
                    setattr(old_value, "Variable178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable178"):
                opp_val = getattr(value, "Variable178", None)
                setattr(value, "Variable178", self)

class Janus_imperativeocl_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, Janus_imperativeocl_AssertExp: "LogExp" = None, Janus_imperativeocl_AssertExp239: "OclExpression" = None):
        self.severity = severity
        self.Janus_imperativeocl_AssertExp = Janus_imperativeocl_AssertExp
        self.Janus_imperativeocl_AssertExp239 = Janus_imperativeocl_AssertExp239
        
        pass
    @property
    def severity(self):
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity


    @property
    def Janus_imperativeocl_AssertExp(self):
        return self.__Janus_imperativeocl_AssertExp

    @Janus_imperativeocl_AssertExp.setter
    def Janus_imperativeocl_AssertExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_AssertExp__Janus_imperativeocl_AssertExp", None)
        self.__Janus_imperativeocl_AssertExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LogExp"):
                opp_val = getattr(old_value, "LogExp", None)
                if opp_val == self:
                    setattr(old_value, "LogExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LogExp"):
                opp_val = getattr(value, "LogExp", None)
                setattr(value, "LogExp", self)

    @property
    def Janus_imperativeocl_AssertExp239(self):
        return self.__Janus_imperativeocl_AssertExp239

    @Janus_imperativeocl_AssertExp239.setter
    def Janus_imperativeocl_AssertExp239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_AssertExp__Janus_imperativeocl_AssertExp239", None)
        self.__Janus_imperativeocl_AssertExp239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression240"):
                opp_val = getattr(old_value, "OclExpression240", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression240"):
                opp_val = getattr(value, "OclExpression240", None)
                setattr(value, "OclExpression240", self)

class Janus_imperativeocl_BlockExp(ImperativeExpression):

    pass
class Janus_imperativeocl_ReturnExp(ImperativeExpression):

    pass
class Janus_imperativeocl_TryExp(ImperativeExpression):

    pass
class Janus_imperativeocl_LogExp(ImperativeExpression):

    def __init__(self, text: str, level: int, Janus_imperativeocl_LogExp: "OclExpression" = None, Janus_imperativeocl_LogExp235: "Element" = None):
        self.text = text
        self.level = level
        self.Janus_imperativeocl_LogExp = Janus_imperativeocl_LogExp
        self.Janus_imperativeocl_LogExp235 = Janus_imperativeocl_LogExp235
        
        pass
    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def Janus_imperativeocl_LogExp(self):
        return self.__Janus_imperativeocl_LogExp

    @Janus_imperativeocl_LogExp.setter
    def Janus_imperativeocl_LogExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_LogExp__Janus_imperativeocl_LogExp", None)
        self.__Janus_imperativeocl_LogExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression233"):
                opp_val = getattr(old_value, "OclExpression233", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression233"):
                opp_val = getattr(value, "OclExpression233", None)
                setattr(value, "OclExpression233", self)

    @property
    def Janus_imperativeocl_LogExp235(self):
        return self.__Janus_imperativeocl_LogExp235

    @Janus_imperativeocl_LogExp235.setter
    def Janus_imperativeocl_LogExp235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_LogExp__Janus_imperativeocl_LogExp235", None)
        self.__Janus_imperativeocl_LogExp235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element236"):
                opp_val = getattr(old_value, "Element236", None)
                if opp_val == self:
                    setattr(old_value, "Element236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element236"):
                opp_val = getattr(value, "Element236", None)
                setattr(value, "Element236", self)

class Janus_imperativeocl_BreakExp(ImperativeExpression):

    pass
class Janus_imperativeocl_UnlinkExp(ImperativeExpression):

    pass
class Janus_imperativeocl_AltExp(ImperativeExpression):

    pass
class Janus_imperativeocl_UnpackExp(ImperativeExpression):

    pass
class Janus_imperativeocl_ContinueExp(ImperativeExpression):

    pass
class Janus_imperativeocl_TupleExp(ImperativeExpression):

    pass
class Janus_imperativeocl_InstantiationExp(ImperativeExpression):

    pass
class Janus_imperativeocl_AssignExp(ImperativeExpression):

    def __init__(self, isReset: bool, Janus_imperativeocl_AssignExp: set["OclExpression"] = None, Janus_imperativeocl_AssignExp166: "OclExpression" = None, Janus_imperativeocl_AssignExp169: "OclExpression" = None):
        self.isReset = isReset
        self.Janus_imperativeocl_AssignExp = Janus_imperativeocl_AssignExp if Janus_imperativeocl_AssignExp is not None else set()
        self.Janus_imperativeocl_AssignExp166 = Janus_imperativeocl_AssignExp166
        self.Janus_imperativeocl_AssignExp169 = Janus_imperativeocl_AssignExp169
        
        pass
    @property
    def isReset(self):
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: bool):
        self.__isReset = isReset


    @property
    def Janus_imperativeocl_AssignExp169(self):
        return self.__Janus_imperativeocl_AssignExp169

    @Janus_imperativeocl_AssignExp169.setter
    def Janus_imperativeocl_AssignExp169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_AssignExp__Janus_imperativeocl_AssignExp169", None)
        self.__Janus_imperativeocl_AssignExp169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression170"):
                opp_val = getattr(old_value, "OclExpression170", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression170"):
                opp_val = getattr(value, "OclExpression170", None)
                setattr(value, "OclExpression170", self)

    @property
    def Janus_imperativeocl_AssignExp(self):
        return self.__Janus_imperativeocl_AssignExp

    @Janus_imperativeocl_AssignExp.setter
    def Janus_imperativeocl_AssignExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_AssignExp__Janus_imperativeocl_AssignExp", None)
        self.__Janus_imperativeocl_AssignExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression164"):
                    opp_val = getattr(item, "OclExpression164", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression164"):
                    opp_val = getattr(item, "OclExpression164", None)
                    
                    setattr(item, "OclExpression164", self)
                    

    @property
    def Janus_imperativeocl_AssignExp166(self):
        return self.__Janus_imperativeocl_AssignExp166

    @Janus_imperativeocl_AssignExp166.setter
    def Janus_imperativeocl_AssignExp166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_imperativeocl_AssignExp__Janus_imperativeocl_AssignExp166", None)
        self.__Janus_imperativeocl_AssignExp166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression167"):
                opp_val = getattr(old_value, "OclExpression167", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression167"):
                opp_val = getattr(value, "OclExpression167", None)
                setattr(value, "OclExpression167", self)

class ImperativeLoopExp:

    pass
class Janus_imperativeocl_CollectorExp(ImperativeLoopExp):

    pass
class Janus_imperativeocl_ForExp(ImperativeLoopExp):

    pass
class Janus_imperativeocl_ImperativeIterateExp(ImperativeLoopExp):

    pass
class Janus_imperativeocl_ComputeExp(ImperativeExpression):

    pass
class Janus_imperativeocl_WhileExp(ImperativeExpression):

    pass
class PropertyTemplateItem:

    pass
class Janus_template_ObjectTemplateExp(TemplateExp):

    def __init__(self, referredClass: str, objContainer: set["PropertyTemplateItem"] = None, TemplateExp: "Janus_JTL_Pattern" = None):
        self.referredClass = referredClass
        self.objContainer = objContainer if objContainer is not None else set()
        
        pass
    @property
    def referredClass(self):
        return self.__referredClass

    @referredClass.setter
    def referredClass(self, referredClass: str):
        self.__referredClass = referredClass


    @property
    def objContainer(self):
        return self.__objContainer

    @objContainer.setter
    def objContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_template_ObjectTemplateExp__objContainer", None)
        self.__objContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PropertyTemplateItem"):
                    opp_val = getattr(item, "PropertyTemplateItem", None)
                    
                    if opp_val == self:
                        setattr(item, "PropertyTemplateItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PropertyTemplateItem"):
                    opp_val = getattr(item, "PropertyTemplateItem", None)
                    
                    setattr(item, "PropertyTemplateItem", self)
                    

class emof_Type:

    pass
class Janus_essentialocl_AnyType(emof_Class, emof_Type):

    pass
class Janus_essentialocl_VoidType(Type):

    pass
class emof_DataType:

    pass
class Janus_essentialocl_TupleType(emof_Class, emof_DataType):

    pass
class Janus_essentialocl_InvalidType(Type):

    pass
class Janus_essentialocl_CollectionType(DataType):

    pass
class CollectionType:

    pass
class Janus_essentialocl_OrderedSetType(CollectionType):

    pass
class Janus_imperativeocl_DictionaryType(CollectionType):

    pass
class Janus_imperativeocl_ListType(CollectionType):

    pass
class Janus_essentialocl_SetType(CollectionType):

    pass
class Janus_essentialocl_SequenceType(CollectionType):

    pass
class Janus_essentialocl_BagType(CollectionType):

    pass
class ObjectTemplateExp:

    pass
class Janus_template_PropertyTemplateItem(Element):

    pass
class Janus_template_CollectionTemplateExp(TemplateExp):

    def __init__(self, kind: str, Janus_template_CollectionTemplateExp: set["OclExpression"] = None, Janus_template_CollectionTemplateExp150: "CollectionType" = None, Janus_template_CollectionTemplateExp152: "OclExpression" = None, TemplateExp: "Janus_JTL_Pattern" = None):
        self.kind = kind
        self.Janus_template_CollectionTemplateExp = Janus_template_CollectionTemplateExp if Janus_template_CollectionTemplateExp is not None else set()
        self.Janus_template_CollectionTemplateExp150 = Janus_template_CollectionTemplateExp150
        self.Janus_template_CollectionTemplateExp152 = Janus_template_CollectionTemplateExp152
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def Janus_template_CollectionTemplateExp150(self):
        return self.__Janus_template_CollectionTemplateExp150

    @Janus_template_CollectionTemplateExp150.setter
    def Janus_template_CollectionTemplateExp150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_template_CollectionTemplateExp__Janus_template_CollectionTemplateExp150", None)
        self.__Janus_template_CollectionTemplateExp150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CollectionType"):
                opp_val = getattr(old_value, "CollectionType", None)
                if opp_val == self:
                    setattr(old_value, "CollectionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CollectionType"):
                opp_val = getattr(value, "CollectionType", None)
                setattr(value, "CollectionType", self)

    @property
    def Janus_template_CollectionTemplateExp(self):
        return self.__Janus_template_CollectionTemplateExp

    @Janus_template_CollectionTemplateExp.setter
    def Janus_template_CollectionTemplateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_template_CollectionTemplateExp__Janus_template_CollectionTemplateExp", None)
        self.__Janus_template_CollectionTemplateExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression148"):
                    opp_val = getattr(item, "OclExpression148", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression148"):
                    opp_val = getattr(item, "OclExpression148", None)
                    
                    setattr(item, "OclExpression148", self)
                    

    @property
    def Janus_template_CollectionTemplateExp152(self):
        return self.__Janus_template_CollectionTemplateExp152

    @Janus_template_CollectionTemplateExp152.setter
    def Janus_template_CollectionTemplateExp152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_template_CollectionTemplateExp__Janus_template_CollectionTemplateExp152", None)
        self.__Janus_template_CollectionTemplateExp152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression153"):
                opp_val = getattr(old_value, "OclExpression153", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression153"):
                opp_val = getattr(value, "OclExpression153", None)
                setattr(value, "OclExpression153", self)

class CollectionLiteralExp:

    pass
class Janus_essentialocl_CollectionLiteralPart(TypedElement):

    pass
class CollectionLiteralPart:

    pass
class Janus_essentialocl_CollectionItem(CollectionLiteralPart):

    pass
class Janus_essentialocl_CollectionRange(CollectionLiteralPart):

    pass
class Janus_essentialocl_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class LiteralExp:

    pass
class Janus_imperativeocl_DictLiteralExp(LiteralExp):

    pass
class Janus_template_TemplateExp(LiteralExp):

    pass
class Janus_essentialocl_TupleLiteralExp(LiteralExp):

    pass
class Janus_essentialocl_EnumLiteralExp(LiteralExp):

    pass
class Janus_essentialocl_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, CollectionLiteralExp: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.CollectionLiteralExp = CollectionLiteralExp if CollectionLiteralExp is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def CollectionLiteralExp(self):
        return self.__CollectionLiteralExp

    @CollectionLiteralExp.setter
    def CollectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Janus_essentialocl_CollectionLiteralExp__CollectionLiteralExp", None)
        self.__CollectionLiteralExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CollectionLiteralPart"):
                    opp_val = getattr(item, "CollectionLiteralPart", None)
                    
                    if opp_val == self:
                        setattr(item, "CollectionLiteralPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CollectionLiteralPart"):
                    opp_val = getattr(item, "CollectionLiteralPart", None)
                    
                    setattr(item, "CollectionLiteralPart", self)
                    

class Janus_imperativeocl_AnonymousTupleLiteralExp(LiteralExp):

    pass
class Janus_essentialocl_PrimitiveLiteralExp(LiteralExp):

    pass
class Janus_essentialocl_IterateExp(LoopExp):

    pass
class Janus_essentialocl_LiteralExp(OclExpression):

    pass
class TupleLiteralExp:

    pass
class Janus_essentialocl_TupleLiteralPart(TypedElement):

    pass
class CallExp:

    pass
class Janus_essentialocl_FeaturePropertyCall(CallExp):

    pass
class Janus_essentialocl_InvalidLiteralExp(LiteralExp):

    pass
class Janus_essentialocl_OpaqueExpression:

    pass
class OpaqueExpression:

    pass
class Janus_essentialocl_ExpressionInOcl(OpaqueExpression):

    pass
class Janus_essentialocl_NullLiteralExp(LiteralExp):

    pass
class TupleLiteralPart:

    pass
class Janus_essentialocl_LoopExp(essentialocl_OclExpression, essentialocl_CallExp):

    pass
class Janus_essentialocl_TypeExp(OclExpression):

    pass
class Janus_essentialocl_VariableExp(OclExpression):

    pass
class FeaturePropertyCall:

    pass
class Janus_essentialocl_OperationCallExp(FeaturePropertyCall):

    pass
class Janus_essentialocl_PropertyCallExp(FeaturePropertyCall):

    pass