from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SeverityKind(Enum):
    error = "error"
    fatal = "fatal"
    warning = "warning"
class CollectionKind(Enum):
    OrderedSet = "OrderedSet"
    Set = "Set"
    Bag = "Bag"
    Sequence = "Sequence"


############################################
# Definition of Classes
############################################

class PrimitiveLiteralExp:

    pass
class JTL_essentialocl_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: bool):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: bool):
        self.__booleanSymbol = booleanSymbol


class Relation:

    pass
class Model:

    pass
class emof_Package:

    pass
class emof_Class:

    pass
class JTL_JTL_Transformation(emof_Package, emof_Class):

    pass
class Extent:

    pass
class JTL_emof_URIExtent(Extent):

    pass
class Pattern:

    pass
class Variable:

    pass
class When:

    pass
class Where:

    pass
class Domain:

    pass
class Transformation:

    pass
class JTL_emof_MultiplicityElement(ABC):

    def __init__(self, upper: str, isOrdered: str, isUnique: str, lower: int):
        self.upper = upper
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        
        pass
    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower


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


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


class Parameter:

    pass
class emof_TypedElement:

    pass
class emof_MultiplicityElement:

    pass
class JTL_emof_Operation(emof_MultiplicityElement, emof_TypedElement):

    pass
class JTL_emof_Object:

    pass
class JTL_emof_Property(emof_MultiplicityElement, emof_TypedElement):

    def __init__(self, isReadOnly: bool, isDerived: bool, isComposite: bool, isId: bool, default: str, ownedAttribute: "Class" = None, JTL_emof_Property: "Property" = None):
        self.isReadOnly = isReadOnly
        self.isDerived = isDerived
        self.isComposite = isComposite
        self.isId = isId
        self.default = default
        self.ownedAttribute = ownedAttribute
        self.JTL_emof_Property = JTL_emof_Property
        
        pass
    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived


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
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite


    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Property__ownedAttribute", None)
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

    @property
    def JTL_emof_Property(self):
        return self.__JTL_emof_Property

    @JTL_emof_Property.setter
    def JTL_emof_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Property__JTL_emof_Property", None)
        self.__JTL_emof_Property = value
        
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

class Enumeration:

    pass
class JTL_emof_Parameter(emof_MultiplicityElement, emof_TypedElement):

    pass
class Package:

    pass
class NamedElement:

    pass
class JTL_JTL_Relation(NamedElement):

    def __init__(self, isTopLevel: bool, relation: "Transformation" = None, relation30: set["Domain"] = None, whereOwner: "Where" = None, whenOwner: "When" = None, JTL_JTL_Relation: set["Variable"] = None, NamedElement: "JTL_emof_Comment" = None):
        self.isTopLevel = isTopLevel
        self.relation = relation
        self.relation30 = relation30 if relation30 is not None else set()
        self.whereOwner = whereOwner
        self.whenOwner = whenOwner
        self.JTL_JTL_Relation = JTL_JTL_Relation if JTL_JTL_Relation is not None else set()
        
        pass
    @property
    def isTopLevel(self):
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: bool):
        self.__isTopLevel = isTopLevel


    @property
    def relation30(self):
        return self.__relation30

    @relation30.setter
    def relation30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Relation__relation30", None)
        self.__relation30 = value if value is not None else set()
        
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
    def JTL_JTL_Relation(self):
        return self.__JTL_JTL_Relation

    @JTL_JTL_Relation.setter
    def JTL_JTL_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Relation__JTL_JTL_Relation", None)
        self.__JTL_JTL_Relation = value if value is not None else set()
        
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
                    

    @property
    def whereOwner(self):
        return self.__whereOwner

    @whereOwner.setter
    def whereOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Relation__whereOwner", None)
        self.__whereOwner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Where"):
                opp_val = getattr(old_value, "Where", None)
                if opp_val == self:
                    setattr(old_value, "Where", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Where"):
                opp_val = getattr(value, "Where", None)
                setattr(value, "Where", self)

    @property
    def relation(self):
        return self.__relation

    @relation.setter
    def relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Relation__relation", None)
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
    def whenOwner(self):
        return self.__whenOwner

    @whenOwner.setter
    def whenOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Relation__whenOwner", None)
        self.__whenOwner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "When"):
                opp_val = getattr(old_value, "When", None)
                if opp_val == self:
                    setattr(old_value, "When", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "When"):
                opp_val = getattr(value, "When", None)
                setattr(value, "When", self)

class JTL_JTL_Model(NamedElement):

    def __init__(self, usedPackage: str, modelParameter: "Transformation" = None, JTL_JTL_Model: set["Model"] = None, NamedElement: "JTL_emof_Comment" = None):
        self.usedPackage = usedPackage
        self.modelParameter = modelParameter
        self.JTL_JTL_Model = JTL_JTL_Model if JTL_JTL_Model is not None else set()
        
        pass
    @property
    def usedPackage(self):
        return self.__usedPackage

    @usedPackage.setter
    def usedPackage(self, usedPackage: str):
        self.__usedPackage = usedPackage


    @property
    def JTL_JTL_Model(self):
        return self.__JTL_JTL_Model

    @JTL_JTL_Model.setter
    def JTL_JTL_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Model__JTL_JTL_Model", None)
        self.__JTL_JTL_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Model46"):
                    opp_val = getattr(item, "Model46", None)
                    
                    if opp_val == self:
                        setattr(item, "Model46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Model46"):
                    opp_val = getattr(item, "Model46", None)
                    
                    setattr(item, "Model46", self)
                    

    @property
    def modelParameter(self):
        return self.__modelParameter

    @modelParameter.setter
    def modelParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Model__modelParameter", None)
        self.__modelParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transformation44"):
                opp_val = getattr(old_value, "Transformation44", None)
                if opp_val == self:
                    setattr(old_value, "Transformation44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transformation44"):
                opp_val = getattr(value, "Transformation44", None)
                setattr(value, "Transformation44", self)

class JTL_emof_Type(NamedElement):

    pass
class JTL_emof_TypedElement(NamedElement):

    def __init__(self, type: str, NamedElement: "JTL_emof_Comment" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class JTL_JTL_Domain(NamedElement):

    def __init__(self, isCheckable: bool, isEnforceable: bool, domain: "Relation" = None, JTL_JTL_Domain: "Pattern" = None, JTL_JTL_Domain38: "Model" = None, JTL_JTL_Domain41: "Variable" = None, NamedElement: "JTL_emof_Comment" = None):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.domain = domain
        self.JTL_JTL_Domain = JTL_JTL_Domain
        self.JTL_JTL_Domain38 = JTL_JTL_Domain38
        self.JTL_JTL_Domain41 = JTL_JTL_Domain41
        
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
        old_value = getattr(self, f"_JTL_JTL_Domain__domain", None)
        self.__domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relation35"):
                opp_val = getattr(old_value, "Relation35", None)
                if opp_val == self:
                    setattr(old_value, "Relation35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relation35"):
                opp_val = getattr(value, "Relation35", None)
                setattr(value, "Relation35", self)

    @property
    def JTL_JTL_Domain41(self):
        return self.__JTL_JTL_Domain41

    @JTL_JTL_Domain41.setter
    def JTL_JTL_Domain41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Domain__JTL_JTL_Domain41", None)
        self.__JTL_JTL_Domain41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable42"):
                opp_val = getattr(old_value, "Variable42", None)
                if opp_val == self:
                    setattr(old_value, "Variable42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable42"):
                opp_val = getattr(value, "Variable42", None)
                setattr(value, "Variable42", self)

    @property
    def JTL_JTL_Domain38(self):
        return self.__JTL_JTL_Domain38

    @JTL_JTL_Domain38.setter
    def JTL_JTL_Domain38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Domain__JTL_JTL_Domain38", None)
        self.__JTL_JTL_Domain38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model39"):
                opp_val = getattr(old_value, "Model39", None)
                if opp_val == self:
                    setattr(old_value, "Model39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model39"):
                opp_val = getattr(value, "Model39", None)
                setattr(value, "Model39", self)

    @property
    def JTL_JTL_Domain(self):
        return self.__JTL_JTL_Domain

    @JTL_JTL_Domain.setter
    def JTL_JTL_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_JTL_Domain__JTL_JTL_Domain", None)
        self.__JTL_JTL_Domain = value
        
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

class JTL_emof_EnumerationLiteral(NamedElement):

    pass
class JTL_emof_Package(NamedElement):

    def __init__(self, uri: str, package: set["Type"] = None, JTL_emof_Package: set["Package"] = None, NamedElement: "JTL_emof_Comment" = None):
        self.uri = uri
        self.package = package if package is not None else set()
        self.JTL_emof_Package = JTL_emof_Package if JTL_emof_Package is not None else set()
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def JTL_emof_Package(self):
        return self.__JTL_emof_Package

    @JTL_emof_Package.setter
    def JTL_emof_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Package__JTL_emof_Package", None)
        self.__JTL_emof_Package = value if value is not None else set()
        
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
        old_value = getattr(self, f"_JTL_emof_Package__package", None)
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
                    

class Property:

    pass
class Type:

    pass
class JTL_emof_Class(Type):

    def __init__(self, isAbstract: bool, class_: set["Operation"] = None, JTL_emof_Class: set["Class"] = None, Class: set["Property"] = None, Type129: "JTL_essentialocl_CollectionType" = None, Type200: "JTL_imperativeocl_RaiseExp" = None, Type195: "JTL_imperativeocl_TryExp" = None, Type204: "JTL_imperativeocl_Typedef" = None, Type: "JTL_emof_Operation" = None, Type90: "JTL_essentialocl_TypeExp" = None, Type240: "JTL_imperativeocl_AnonymousTupleType" = None, Type217: "JTL_imperativeocl_DictionaryType" = None, Type13: "JTL_emof_Package" = None):
        self.isAbstract = isAbstract
        self.class_ = class_ if class_ is not None else set()
        self.JTL_emof_Class = JTL_emof_Class if JTL_emof_Class is not None else set()
        self.Class = Class if Class is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract


    @property
    def JTL_emof_Class(self):
        return self.__JTL_emof_Class

    @JTL_emof_Class.setter
    def JTL_emof_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Class__JTL_emof_Class", None)
        self.__JTL_emof_Class = value if value is not None else set()
        
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
                    

    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Class__class_", None)
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
        old_value = getattr(self, f"_JTL_emof_Class__Class", None)
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
                    

class EnumerationLiteral:

    pass
class DataType:

    pass
class JTL_emof_PrimitiveType(DataType):

    pass
class JTL_emof_Enumeration(DataType):

    pass
class Element:

    pass
class JTL_emof_NamedElement(Element):

    def __init__(self, name: str, Element228: "JTL_imperativeocl_LogExp" = None, Element: "JTL_emof_Tag" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class JTL_emof_Comment(Element):

    pass
class JTL_emof_Tag(Element):

    def __init__(self, value: str, name: str, tag: set["Element"] = None, Element228: "JTL_imperativeocl_LogExp" = None, Element: "JTL_emof_Tag" = None):
        self.value = value
        self.name = name
        self.tag = tag if tag is not None else set()
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_emof_Tag__tag", None)
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
class JTL_emof_Extent(Object):

    pass
class JTL_emof_Element(Object):

    pass
class JTL_emof_DataType(Type):

    pass
class Class:

    pass
class Operation:

    pass
class JTL_imperativeocl_AnonymousTupleLiteralPart(Element):

    pass
class AnonymousTupleLiteralPart:

    pass
class JTL_imperativeocl_AnonymousTupleType(Class):

    pass
class JTL_imperativeocl_TemplateParameterType(Type):

    def __init__(self, specification: str, Type129: "JTL_essentialocl_CollectionType" = None, Type200: "JTL_imperativeocl_RaiseExp" = None, Type195: "JTL_imperativeocl_TryExp" = None, Type204: "JTL_imperativeocl_Typedef" = None, Type: "JTL_emof_Operation" = None, Type90: "JTL_essentialocl_TypeExp" = None, Type240: "JTL_imperativeocl_AnonymousTupleType" = None, Type217: "JTL_imperativeocl_DictionaryType" = None, Type13: "JTL_emof_Package" = None):
        self.specification = specification
        
        pass
    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


class JTL_imperativeocl_DictLiteralPart(Element):

    pass
class DictLiteralPart:

    pass
class essentialocl_LoopExp:

    pass
class LogExp:

    pass
class JTL_imperativeocl_Typedef(Class):

    pass
class AltExp:

    pass
class imperativeocl_ImperativeExpression:

    pass
class JTL_imperativeocl_ImperativeLoopExp(imperativeocl_ImperativeExpression, essentialocl_LoopExp):

    pass
class AssignExp:

    pass
class PropertyTemplateItem:

    pass
class ImperativeExpression:

    pass
class JTL_imperativeocl_TupleExp(ImperativeExpression):

    pass
class JTL_imperativeocl_WhileExp(ImperativeExpression):

    pass
class JTL_imperativeocl_BlockExp(ImperativeExpression):

    pass
class JTL_imperativeocl_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: bool, JTL_imperativeocl_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.JTL_imperativeocl_VariableInitExp = JTL_imperativeocl_VariableInitExp
        
        pass
    @property
    def withResult(self):
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: bool):
        self.__withResult = withResult


    @property
    def JTL_imperativeocl_VariableInitExp(self):
        return self.__JTL_imperativeocl_VariableInitExp

    @JTL_imperativeocl_VariableInitExp.setter
    def JTL_imperativeocl_VariableInitExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_VariableInitExp__JTL_imperativeocl_VariableInitExp", None)
        self.__JTL_imperativeocl_VariableInitExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable170"):
                opp_val = getattr(old_value, "Variable170", None)
                if opp_val == self:
                    setattr(old_value, "Variable170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable170"):
                opp_val = getattr(value, "Variable170", None)
                setattr(value, "Variable170", self)

class JTL_imperativeocl_ComputeExp(ImperativeExpression):

    pass
class JTL_imperativeocl_RaiseExp(ImperativeExpression):

    pass
class JTL_imperativeocl_AltExp(ImperativeExpression):

    pass
class JTL_imperativeocl_InstantiationExp(ImperativeExpression):

    pass
class JTL_imperativeocl_BreakExp(ImperativeExpression):

    pass
class JTL_imperativeocl_LogExp(ImperativeExpression):

    def __init__(self, text: str, level: int, JTL_imperativeocl_LogExp227: "Element" = None, JTL_imperativeocl_LogExp: "OclExpression" = None):
        self.text = text
        self.level = level
        self.JTL_imperativeocl_LogExp227 = JTL_imperativeocl_LogExp227
        self.JTL_imperativeocl_LogExp = JTL_imperativeocl_LogExp
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level


    @property
    def JTL_imperativeocl_LogExp(self):
        return self.__JTL_imperativeocl_LogExp

    @JTL_imperativeocl_LogExp.setter
    def JTL_imperativeocl_LogExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_LogExp__JTL_imperativeocl_LogExp", None)
        self.__JTL_imperativeocl_LogExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression225"):
                opp_val = getattr(old_value, "OclExpression225", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression225"):
                opp_val = getattr(value, "OclExpression225", None)
                setattr(value, "OclExpression225", self)

    @property
    def JTL_imperativeocl_LogExp227(self):
        return self.__JTL_imperativeocl_LogExp227

    @JTL_imperativeocl_LogExp227.setter
    def JTL_imperativeocl_LogExp227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_LogExp__JTL_imperativeocl_LogExp227", None)
        self.__JTL_imperativeocl_LogExp227 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element228"):
                opp_val = getattr(old_value, "Element228", None)
                if opp_val == self:
                    setattr(old_value, "Element228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element228"):
                opp_val = getattr(value, "Element228", None)
                setattr(value, "Element228", self)

class JTL_imperativeocl_TryExp(ImperativeExpression):

    pass
class JTL_imperativeocl_UnlinkExp(ImperativeExpression):

    pass
class JTL_imperativeocl_ContinueExp(ImperativeExpression):

    pass
class JTL_imperativeocl_UnpackExp(ImperativeExpression):

    pass
class JTL_imperativeocl_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, JTL_imperativeocl_AssertExp: "LogExp" = None, JTL_imperativeocl_AssertExp231: "OclExpression" = None):
        self.severity = severity
        self.JTL_imperativeocl_AssertExp = JTL_imperativeocl_AssertExp
        self.JTL_imperativeocl_AssertExp231 = JTL_imperativeocl_AssertExp231
        
        pass
    @property
    def severity(self):
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity


    @property
    def JTL_imperativeocl_AssertExp(self):
        return self.__JTL_imperativeocl_AssertExp

    @JTL_imperativeocl_AssertExp.setter
    def JTL_imperativeocl_AssertExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_AssertExp__JTL_imperativeocl_AssertExp", None)
        self.__JTL_imperativeocl_AssertExp = value
        
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
    def JTL_imperativeocl_AssertExp231(self):
        return self.__JTL_imperativeocl_AssertExp231

    @JTL_imperativeocl_AssertExp231.setter
    def JTL_imperativeocl_AssertExp231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_AssertExp__JTL_imperativeocl_AssertExp231", None)
        self.__JTL_imperativeocl_AssertExp231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression232"):
                opp_val = getattr(old_value, "OclExpression232", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression232"):
                opp_val = getattr(value, "OclExpression232", None)
                setattr(value, "OclExpression232", self)

class JTL_imperativeocl_ReturnExp(ImperativeExpression):

    pass
class JTL_imperativeocl_AssignExp(ImperativeExpression):

    def __init__(self, isReset: bool, JTL_imperativeocl_AssignExp: set["OclExpression"] = None, JTL_imperativeocl_AssignExp158: "OclExpression" = None, JTL_imperativeocl_AssignExp161: "OclExpression" = None):
        self.isReset = isReset
        self.JTL_imperativeocl_AssignExp = JTL_imperativeocl_AssignExp if JTL_imperativeocl_AssignExp is not None else set()
        self.JTL_imperativeocl_AssignExp158 = JTL_imperativeocl_AssignExp158
        self.JTL_imperativeocl_AssignExp161 = JTL_imperativeocl_AssignExp161
        
        pass
    @property
    def isReset(self):
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: bool):
        self.__isReset = isReset


    @property
    def JTL_imperativeocl_AssignExp(self):
        return self.__JTL_imperativeocl_AssignExp

    @JTL_imperativeocl_AssignExp.setter
    def JTL_imperativeocl_AssignExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_AssignExp__JTL_imperativeocl_AssignExp", None)
        self.__JTL_imperativeocl_AssignExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression156"):
                    opp_val = getattr(item, "OclExpression156", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression156"):
                    opp_val = getattr(item, "OclExpression156", None)
                    
                    setattr(item, "OclExpression156", self)
                    

    @property
    def JTL_imperativeocl_AssignExp161(self):
        return self.__JTL_imperativeocl_AssignExp161

    @JTL_imperativeocl_AssignExp161.setter
    def JTL_imperativeocl_AssignExp161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_AssignExp__JTL_imperativeocl_AssignExp161", None)
        self.__JTL_imperativeocl_AssignExp161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression162"):
                opp_val = getattr(old_value, "OclExpression162", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression162"):
                opp_val = getattr(value, "OclExpression162", None)
                setattr(value, "OclExpression162", self)

    @property
    def JTL_imperativeocl_AssignExp158(self):
        return self.__JTL_imperativeocl_AssignExp158

    @JTL_imperativeocl_AssignExp158.setter
    def JTL_imperativeocl_AssignExp158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_imperativeocl_AssignExp__JTL_imperativeocl_AssignExp158", None)
        self.__JTL_imperativeocl_AssignExp158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression159"):
                opp_val = getattr(old_value, "OclExpression159", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression159"):
                opp_val = getattr(value, "OclExpression159", None)
                setattr(value, "OclExpression159", self)

class ImperativeLoopExp:

    pass
class JTL_imperativeocl_ForExp(ImperativeLoopExp):

    pass
class JTL_imperativeocl_CollectorExp(ImperativeLoopExp):

    pass
class JTL_imperativeocl_ImperativeIterateExp(ImperativeLoopExp):

    pass
class ObjectTemplateExp:

    pass
class JTL_template_PropertyTemplateItem(Element):

    pass
class JTL_essentialocl_CollectionType(DataType):

    pass
class CollectionType:

    pass
class JTL_imperativeocl_DictionaryType(CollectionType):

    pass
class JTL_imperativeocl_ListType(CollectionType):

    pass
class JTL_essentialocl_BagType(CollectionType):

    pass
class TupleLiteralExp:

    pass
class CallExp:

    pass
class JTL_essentialocl_FeaturePropertyCall(CallExp):

    pass
class JTL_essentialocl_OpaqueExpression:

    pass
class emof_Type:

    pass
class JTL_essentialocl_AnyType(emof_Class, emof_Type):

    pass
class JTL_essentialocl_VoidType(Type):

    pass
class emof_DataType:

    pass
class JTL_essentialocl_TupleType(emof_DataType, emof_Class):

    pass
class JTL_essentialocl_SetType(CollectionType):

    pass
class JTL_essentialocl_SequenceType(CollectionType):

    pass
class JTL_essentialocl_OrderedSetType(CollectionType):

    pass
class JTL_essentialocl_InvalidType(Type):

    pass
class CollectionLiteralExp:

    pass
class CollectionLiteralPart:

    pass
class JTL_essentialocl_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class LiteralExp:

    pass
class JTL_imperativeocl_AnonymousTupleLiteralExp(LiteralExp):

    pass
class JTL_essentialocl_EnumLiteralExp(LiteralExp):

    pass
class JTL_essentialocl_CollectionLiteralExp(LiteralExp):

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
        old_value = getattr(self, f"_JTL_essentialocl_CollectionLiteralExp__CollectionLiteralExp", None)
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
                    

class JTL_essentialocl_InvalidLiteralExp(LiteralExp):

    pass
class JTL_template_TemplateExp(LiteralExp):

    pass
class JTL_imperativeocl_DictLiteralExp(LiteralExp):

    pass
class JTL_essentialocl_PrimitiveLiteralExp(LiteralExp):

    pass
class OpaqueExpression:

    pass
class JTL_essentialocl_ExpressionInOcl(OpaqueExpression):

    pass
class JTL_essentialocl_NullLiteralExp(LiteralExp):

    pass
class TupleLiteralPart:

    pass
class JTL_essentialocl_TupleLiteralExp(LiteralExp):

    pass
class JTL_essentialocl_CollectionRange(CollectionLiteralPart):

    pass
class JTL_essentialocl_CollectionItem(CollectionLiteralPart):

    pass
class FeaturePropertyCall:

    pass
class JTL_essentialocl_PropertyCallExp(FeaturePropertyCall):

    pass
class ComputeExp:

    pass
class LetExp:

    pass
class JTL_essentialocl_OperationCallExp(FeaturePropertyCall):

    pass
class JTL_essentialocl_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class LoopExp:

    pass
class JTL_essentialocl_IterateExp(LoopExp):

    pass
class JTL_essentialocl_IteratorExp(LoopExp):

    pass
class essentialocl_OclExpression:

    pass
class essentialocl_CallExp:

    pass
class JTL_imperativeocl_SwitchExp(essentialocl_CallExp, imperativeocl_ImperativeExpression):

    pass
class JTL_essentialocl_LoopExp(essentialocl_OclExpression, essentialocl_CallExp):

    pass
class JTL_JTL_Where(Pattern):

    pass
class JTL_JTL_When(Pattern):

    pass
class OclExpression:

    pass
class JTL_essentialocl_LiteralExp(OclExpression):

    pass
class JTL_essentialocl_LetExp(OclExpression):

    pass
class JTL_essentialocl_TypeExp(OclExpression):

    pass
class JTL_essentialocl_VariableExp(OclExpression):

    pass
class JTL_essentialocl_CallExp(OclExpression):

    pass
class JTL_imperativeocl_ImperativeExpression(OclExpression):

    pass
class JTL_JTL_Predicate(Element):

    pass
class TemplateExp:

    pass
class JTL_template_ObjectTemplateExp(TemplateExp):

    def __init__(self, referredClass: str, objContainer: set["PropertyTemplateItem"] = None, JTL_template_ObjectTemplateExp: set["AssignExp"] = None, TemplateExp: "JTL_JTL_Pattern" = None):
        self.referredClass = referredClass
        self.objContainer = objContainer if objContainer is not None else set()
        self.JTL_template_ObjectTemplateExp = JTL_template_ObjectTemplateExp if JTL_template_ObjectTemplateExp is not None else set()
        
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
        old_value = getattr(self, f"_JTL_template_ObjectTemplateExp__objContainer", None)
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
                    

    @property
    def JTL_template_ObjectTemplateExp(self):
        return self.__JTL_template_ObjectTemplateExp

    @JTL_template_ObjectTemplateExp.setter
    def JTL_template_ObjectTemplateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_template_ObjectTemplateExp__JTL_template_ObjectTemplateExp", None)
        self.__JTL_template_ObjectTemplateExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssignExp"):
                    opp_val = getattr(item, "AssignExp", None)
                    
                    if opp_val == self:
                        setattr(item, "AssignExp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssignExp"):
                    opp_val = getattr(item, "AssignExp", None)
                    
                    setattr(item, "AssignExp", self)
                    

class JTL_template_CollectionTemplateExp(TemplateExp):

    def __init__(self, kind: str, JTL_template_CollectionTemplateExp142: "CollectionType" = None, JTL_template_CollectionTemplateExp144: "OclExpression" = None, JTL_template_CollectionTemplateExp: set["OclExpression"] = None, TemplateExp: "JTL_JTL_Pattern" = None):
        self.kind = kind
        self.JTL_template_CollectionTemplateExp142 = JTL_template_CollectionTemplateExp142
        self.JTL_template_CollectionTemplateExp144 = JTL_template_CollectionTemplateExp144
        self.JTL_template_CollectionTemplateExp = JTL_template_CollectionTemplateExp if JTL_template_CollectionTemplateExp is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def JTL_template_CollectionTemplateExp144(self):
        return self.__JTL_template_CollectionTemplateExp144

    @JTL_template_CollectionTemplateExp144.setter
    def JTL_template_CollectionTemplateExp144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_template_CollectionTemplateExp__JTL_template_CollectionTemplateExp144", None)
        self.__JTL_template_CollectionTemplateExp144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression145"):
                opp_val = getattr(old_value, "OclExpression145", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression145"):
                opp_val = getattr(value, "OclExpression145", None)
                setattr(value, "OclExpression145", self)

    @property
    def JTL_template_CollectionTemplateExp142(self):
        return self.__JTL_template_CollectionTemplateExp142

    @JTL_template_CollectionTemplateExp142.setter
    def JTL_template_CollectionTemplateExp142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_template_CollectionTemplateExp__JTL_template_CollectionTemplateExp142", None)
        self.__JTL_template_CollectionTemplateExp142 = value
        
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
    def JTL_template_CollectionTemplateExp(self):
        return self.__JTL_template_CollectionTemplateExp

    @JTL_template_CollectionTemplateExp.setter
    def JTL_template_CollectionTemplateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JTL_template_CollectionTemplateExp__JTL_template_CollectionTemplateExp", None)
        self.__JTL_template_CollectionTemplateExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression140"):
                    opp_val = getattr(item, "OclExpression140", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression140"):
                    opp_val = getattr(item, "OclExpression140", None)
                    
                    setattr(item, "OclExpression140", self)
                    

class Predicate:

    pass
class JTL_JTL_Pattern(Element):

    pass
class JTL_essentialocl_IfExp(OclExpression):

    pass
class NumericLiteralExp:

    pass
class JTL_essentialocl_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: int):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: int):
        self.__integerSymbol = integerSymbol


class JTL_essentialocl_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: float):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: float):
        self.__realSymbol = realSymbol


class JTL_essentialocl_UnlimitedNaturalExp(NumericLiteralExp):

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
class JTL_essentialocl_Variable(TypedElement):

    pass
class JTL_essentialocl_TupleLiteralPart(TypedElement):

    pass
class JTL_essentialocl_CollectionLiteralPart(TypedElement):

    pass
class JTL_essentialocl_OclExpression(TypedElement):

    pass