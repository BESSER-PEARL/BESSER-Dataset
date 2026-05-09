from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SingleEntityValue:

    pass
class instances_AggregateValue:

    pass
class core_Instance:

    pass
class express_instances_LISTValue(instances_AggregateValue, core_Instance):

    pass
class express_core_AggregationType(ABC):

    def __init__(self, isUnique: str, ordering: str, express_core_AggregationType372: "SizeConstraint" = None, express_core_AggregationType: "SizeConstraint" = None):
        self.isUnique = isUnique
        self.ordering = ordering
        self.express_core_AggregationType372 = express_core_AggregationType372
        self.express_core_AggregationType = express_core_AggregationType
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


    @property
    def ordering(self):
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering


    @property
    def express_core_AggregationType372(self):
        return self.__express_core_AggregationType372

    @express_core_AggregationType372.setter
    def express_core_AggregationType372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_AggregationType__express_core_AggregationType372", None)
        self.__express_core_AggregationType372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint373"):
                opp_val = getattr(old_value, "SizeConstraint373", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint373"):
                opp_val = getattr(value, "SizeConstraint373", None)
                setattr(value, "SizeConstraint373", self)

    @property
    def express_core_AggregationType(self):
        return self.__express_core_AggregationType

    @express_core_AggregationType.setter
    def express_core_AggregationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_AggregationType__express_core_AggregationType", None)
        self.__express_core_AggregationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint370"):
                opp_val = getattr(old_value, "SizeConstraint370", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint370", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint370"):
                opp_val = getattr(value, "SizeConstraint370", None)
                setattr(value, "SizeConstraint370", self)

class express_core_ScopedId:

    def __init__(self, localName: str, express_core_ScopedId: "Scope" = None):
        self.localName = localName
        self.express_core_ScopedId = express_core_ScopedId
        
        pass
    @property
    def localName(self):
        return self.__localName

    @localName.setter
    def localName(self, localName: str):
        self.__localName = localName


    @property
    def express_core_ScopedId(self):
        return self.__express_core_ScopedId

    @express_core_ScopedId.setter
    def express_core_ScopedId(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_ScopedId__express_core_ScopedId", None)
        self.__express_core_ScopedId = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Scope368"):
                opp_val = getattr(old_value, "Scope368", None)
                if opp_val == self:
                    setattr(old_value, "Scope368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Scope368"):
                opp_val = getattr(value, "Scope368", None)
                setattr(value, "Scope368", self)

class DomainRule:

    pass
class SelectType:

    pass
class core_CommonElement:

    pass
class core_Scope:

    pass
class express_core_Relationship:

    pass
class express_core_ParameterType(ABC):

    pass
class express_core_Scope(ABC):

    pass
class express_core_Role(ABC):

    pass
class express_core_Remark:

    def __init__(self, isTagged: str, isTail: str, text: str, documentation: set["Schema"] = None, includesRemarks: "Scope" = None, documentation338: set["NamedElement"] = None):
        self.isTagged = isTagged
        self.isTail = isTail
        self.text = text
        self.documentation = documentation if documentation is not None else set()
        self.includesRemarks = includesRemarks
        self.documentation338 = documentation338 if documentation338 is not None else set()
        
        pass
    @property
    def isTail(self):
        return self.__isTail

    @isTail.setter
    def isTail(self, isTail: str):
        self.__isTail = isTail


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def isTagged(self):
        return self.__isTagged

    @isTagged.setter
    def isTagged(self, isTagged: str):
        self.__isTagged = isTagged


    @property
    def includesRemarks(self):
        return self.__includesRemarks

    @includesRemarks.setter
    def includesRemarks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Remark__includesRemarks", None)
        self.__includesRemarks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Scope336"):
                opp_val = getattr(old_value, "Scope336", None)
                if opp_val == self:
                    setattr(old_value, "Scope336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Scope336"):
                opp_val = getattr(value, "Scope336", None)
                setattr(value, "Scope336", self)

    @property
    def documentation338(self):
        return self.__documentation338

    @documentation338.setter
    def documentation338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Remark__documentation338", None)
        self.__documentation338 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedElement"):
                    opp_val = getattr(item, "NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedElement"):
                    opp_val = getattr(item, "NamedElement", None)
                    
                    setattr(item, "NamedElement", self)
                    

    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Remark__documentation", None)
        self.__documentation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Schema334"):
                    opp_val = getattr(item, "Schema334", None)
                    
                    if opp_val == self:
                        setattr(item, "Schema334", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Schema334"):
                    opp_val = getattr(item, "Schema334", None)
                    
                    setattr(item, "Schema334", self)
                    

class ArrayBound:

    pass
class ConcreteType:

    pass
class LocalScope:

    pass
class express_core_AlgorithmScope(LocalScope):

    pass
class AnonymousType:

    pass
class LengthConstraint:

    pass
class ActualTypeConstraint:

    pass
class NumericType:

    pass
class express_core_RealType(NumericType):

    def __init__(self, precision: str):
        self.precision = precision
        
        pass
    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


class DomainConstraint:

    pass
class express_core_SizeConstraint(DomainConstraint):

    def __init__(self, bound: str, DomainConstraint: "express_core_AttributeType" = None):
        self.bound = bound
        
        pass
    @property
    def bound(self):
        return self.__bound

    @bound.setter
    def bound(self, bound: str):
        self.__bound = bound


class express_core_LengthConstraint(DomainConstraint):

    def __init__(self, maxLength: str, isFixed: str, DomainConstraint: "express_core_AttributeType" = None):
        self.maxLength = maxLength
        self.isFixed = isFixed
        
        pass
    @property
    def isFixed(self):
        return self.__isFixed

    @isFixed.setter
    def isFixed(self, isFixed: str):
        self.__isFixed = isFixed


    @property
    def maxLength(self):
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: str):
        self.__maxLength = maxLength


class express_core_AttributeType(ABC):

    pass
class express_core_Instance(ABC):

    pass
class express_core_NamedElement(ABC):

    pass
class core_VariableType:

    pass
class express_core_DomainConstraint(ABC):

    pass
class TypeElement:

    pass
class express_core_UniqueRule(TypeElement):

    def __init__(self, position: str, uniqueRules: "EntityType" = None, express_core_UniqueRule: set["Attribute"] = None):
        self.position = position
        self.uniqueRules = uniqueRules
        self.express_core_UniqueRule = express_core_UniqueRule if express_core_UniqueRule is not None else set()
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def uniqueRules(self):
        return self.__uniqueRules

    @uniqueRules.setter
    def uniqueRules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_UniqueRule__uniqueRules", None)
        self.__uniqueRules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityType283"):
                opp_val = getattr(old_value, "EntityType283", None)
                if opp_val == self:
                    setattr(old_value, "EntityType283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityType283"):
                opp_val = getattr(value, "EntityType283", None)
                setattr(value, "EntityType283", self)

    @property
    def express_core_UniqueRule(self):
        return self.__express_core_UniqueRule

    @express_core_UniqueRule.setter
    def express_core_UniqueRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_UniqueRule__express_core_UniqueRule", None)
        self.__express_core_UniqueRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute285"):
                    opp_val = getattr(item, "Attribute285", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute285", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute285"):
                    opp_val = getattr(item, "Attribute285", None)
                    
                    setattr(item, "Attribute285", self)
                    

class core_ConcreteType:

    pass
class SimpleType:

    pass
class express_core_BinaryType(SimpleType):

    pass
class express_core_LogicType(SimpleType):

    pass
class express_core_StringType(SimpleType):

    pass
class express_core_NumericType(SimpleType):

    pass
class express_core_Attribute(TypeElement):

    def __init__(self, isAbstract: str, position: str, role: "AttributeType" = None, declaresAttribute: "SingleEntityType" = None, attributes: set["EntityType"] = None):
        self.isAbstract = isAbstract
        self.position = position
        self.role = role
        self.declaresAttribute = declaresAttribute
        self.attributes = attributes if attributes is not None else set()
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Attribute__attributes", None)
        self.__attributes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EntityType309"):
                    opp_val = getattr(item, "EntityType309", None)
                    
                    if opp_val == self:
                        setattr(item, "EntityType309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EntityType309"):
                    opp_val = getattr(item, "EntityType309", None)
                    
                    setattr(item, "EntityType309", self)
                    

    @property
    def declaresAttribute(self):
        return self.__declaresAttribute

    @declaresAttribute.setter
    def declaresAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Attribute__declaresAttribute", None)
        self.__declaresAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleEntityType307"):
                opp_val = getattr(old_value, "SingleEntityType307", None)
                if opp_val == self:
                    setattr(old_value, "SingleEntityType307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleEntityType307"):
                opp_val = getattr(value, "SingleEntityType307", None)
                setattr(value, "SingleEntityType307", self)

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Attribute__role", None)
        self.__role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributeType305"):
                opp_val = getattr(old_value, "AttributeType305", None)
                if opp_val == self:
                    setattr(old_value, "AttributeType305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributeType305"):
                opp_val = getattr(value, "AttributeType305", None)
                setattr(value, "AttributeType305", self)

class Relationship:

    pass
class InverseAttribute:

    pass
class SchemaElement:

    pass
class InterfacedElement:

    pass
class Remark:

    pass
class express_core_DataType(ABC):

    pass
class Schema:

    pass
class express_core_InterfacedElement:

    def __init__(self, isUSE: str, interfaces: "Schema" = None, referencedAs: "SchemaElement" = None, express_core_InterfacedElement: "ScopedId" = None):
        self.isUSE = isUSE
        self.interfaces = interfaces
        self.referencedAs = referencedAs
        self.express_core_InterfacedElement = express_core_InterfacedElement
        
        pass
    @property
    def isUSE(self):
        return self.__isUSE

    @isUSE.setter
    def isUSE(self, isUSE: str):
        self.__isUSE = isUSE


    @property
    def express_core_InterfacedElement(self):
        return self.__express_core_InterfacedElement

    @express_core_InterfacedElement.setter
    def express_core_InterfacedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_InterfacedElement__express_core_InterfacedElement", None)
        self.__express_core_InterfacedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScopedId281"):
                opp_val = getattr(old_value, "ScopedId281", None)
                if opp_val == self:
                    setattr(old_value, "ScopedId281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScopedId281"):
                opp_val = getattr(value, "ScopedId281", None)
                setattr(value, "ScopedId281", self)

    @property
    def interfaces(self):
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_InterfacedElement__interfaces", None)
        self.__interfaces = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema"):
                opp_val = getattr(old_value, "Schema", None)
                if opp_val == self:
                    setattr(old_value, "Schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema"):
                opp_val = getattr(value, "Schema", None)
                setattr(value, "Schema", self)

    @property
    def referencedAs(self):
        return self.__referencedAs

    @referencedAs.setter
    def referencedAs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_InterfacedElement__referencedAs", None)
        self.__referencedAs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchemaElement279"):
                opp_val = getattr(old_value, "SchemaElement279", None)
                if opp_val == self:
                    setattr(old_value, "SchemaElement279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchemaElement279"):
                opp_val = getattr(value, "SchemaElement279", None)
                setattr(value, "SchemaElement279", self)

class core_ParameterType:

    pass
class express_core_InstantiableType(core_ParameterType, core_VariableType):

    pass
class core_InstantiableType:

    pass
class express_core_AnonymousType(core_ConcreteType, core_InstantiableType):

    pass
class core_NamedType:

    pass
class express_core_DefinedType(core_NamedType, core_ConcreteType):

    pass
class express_core_EntityType(core_NamedType, core_InstantiableType):

    def __init__(self, isAbstract: str, ofEntity236: set["Role"] = None, scope: set["Redeclaration"] = None, owningEntity: set["Attribute"] = None, range: set["RangeRole"] = None, declaredIn244: "SingleEntityType" = None, forType: set["Extent"] = None, referencingType: set["InvertibleAttribute"] = None, domain: set["DomainRole"] = None, domain253: set["UniqueRule"] = None, rangeType: set["InvertibleAttribute"] = None, express_core_EntityType: set["EntityType"] = None):
        self.isAbstract = isAbstract
        self.ofEntity236 = ofEntity236 if ofEntity236 is not None else set()
        self.scope = scope if scope is not None else set()
        self.owningEntity = owningEntity if owningEntity is not None else set()
        self.range = range if range is not None else set()
        self.declaredIn244 = declaredIn244
        self.forType = forType if forType is not None else set()
        self.referencingType = referencingType if referencingType is not None else set()
        self.domain = domain if domain is not None else set()
        self.domain253 = domain253 if domain253 is not None else set()
        self.rangeType = rangeType if rangeType is not None else set()
        self.express_core_EntityType = express_core_EntityType if express_core_EntityType is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def rangeType(self):
        return self.__rangeType

    @rangeType.setter
    def rangeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__rangeType", None)
        self.__rangeType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InvertibleAttribute255"):
                    opp_val = getattr(item, "InvertibleAttribute255", None)
                    
                    if opp_val == self:
                        setattr(item, "InvertibleAttribute255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InvertibleAttribute255"):
                    opp_val = getattr(item, "InvertibleAttribute255", None)
                    
                    setattr(item, "InvertibleAttribute255", self)
                    

    @property
    def ofEntity236(self):
        return self.__ofEntity236

    @ofEntity236.setter
    def ofEntity236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__ofEntity236", None)
        self.__ofEntity236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role237"):
                    opp_val = getattr(item, "Role237", None)
                    
                    if opp_val == self:
                        setattr(item, "Role237", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role237"):
                    opp_val = getattr(item, "Role237", None)
                    
                    setattr(item, "Role237", self)
                    

    @property
    def express_core_EntityType(self):
        return self.__express_core_EntityType

    @express_core_EntityType.setter
    def express_core_EntityType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__express_core_EntityType", None)
        self.__express_core_EntityType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EntityType257"):
                    opp_val = getattr(item, "EntityType257", None)
                    
                    if opp_val == self:
                        setattr(item, "EntityType257", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EntityType257"):
                    opp_val = getattr(item, "EntityType257", None)
                    
                    setattr(item, "EntityType257", self)
                    

    @property
    def forType(self):
        return self.__forType

    @forType.setter
    def forType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__forType", None)
        self.__forType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Extent247"):
                    opp_val = getattr(item, "Extent247", None)
                    
                    if opp_val == self:
                        setattr(item, "Extent247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Extent247"):
                    opp_val = getattr(item, "Extent247", None)
                    
                    setattr(item, "Extent247", self)
                    

    @property
    def domain253(self):
        return self.__domain253

    @domain253.setter
    def domain253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__domain253", None)
        self.__domain253 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UniqueRule"):
                    opp_val = getattr(item, "UniqueRule", None)
                    
                    if opp_val == self:
                        setattr(item, "UniqueRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UniqueRule"):
                    opp_val = getattr(item, "UniqueRule", None)
                    
                    setattr(item, "UniqueRule", self)
                    

    @property
    def referencingType(self):
        return self.__referencingType

    @referencingType.setter
    def referencingType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__referencingType", None)
        self.__referencingType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InvertibleAttribute249"):
                    opp_val = getattr(item, "InvertibleAttribute249", None)
                    
                    if opp_val == self:
                        setattr(item, "InvertibleAttribute249", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InvertibleAttribute249"):
                    opp_val = getattr(item, "InvertibleAttribute249", None)
                    
                    setattr(item, "InvertibleAttribute249", self)
                    

    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__scope", None)
        self.__scope = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Redeclaration239"):
                    opp_val = getattr(item, "Redeclaration239", None)
                    
                    if opp_val == self:
                        setattr(item, "Redeclaration239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Redeclaration239"):
                    opp_val = getattr(item, "Redeclaration239", None)
                    
                    setattr(item, "Redeclaration239", self)
                    

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__range", None)
        self.__range = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RangeRole"):
                    opp_val = getattr(item, "RangeRole", None)
                    
                    if opp_val == self:
                        setattr(item, "RangeRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RangeRole"):
                    opp_val = getattr(item, "RangeRole", None)
                    
                    setattr(item, "RangeRole", self)
                    

    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__domain", None)
        self.__domain = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DomainRole251"):
                    opp_val = getattr(item, "DomainRole251", None)
                    
                    if opp_val == self:
                        setattr(item, "DomainRole251", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DomainRole251"):
                    opp_val = getattr(item, "DomainRole251", None)
                    
                    setattr(item, "DomainRole251", self)
                    

    @property
    def owningEntity(self):
        return self.__owningEntity

    @owningEntity.setter
    def owningEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__owningEntity", None)
        self.__owningEntity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute241"):
                    opp_val = getattr(item, "Attribute241", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute241"):
                    opp_val = getattr(item, "Attribute241", None)
                    
                    setattr(item, "Attribute241", self)
                    

    @property
    def declaredIn244(self):
        return self.__declaredIn244

    @declaredIn244.setter
    def declaredIn244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EntityType__declaredIn244", None)
        self.__declaredIn244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleEntityType245"):
                opp_val = getattr(old_value, "SingleEntityType245", None)
                if opp_val == self:
                    setattr(old_value, "SingleEntityType245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleEntityType245"):
                opp_val = getattr(value, "SingleEntityType245", None)
                setattr(value, "SingleEntityType245", self)

class Role:

    pass
class express_core_DomainRole(Role):

    pass
class express_core_RangeRole(Role):

    pass
class Redeclaration:

    pass
class AttributeType:

    pass
class express_core_Redeclaration:

    def __init__(self, position: str, isMandatory: str, express_core_Redeclaration223: "SizeConstraint" = None, redeclarations: "EntityType" = None, express_core_Redeclaration228: "Attribute" = None, express_core_Redeclaration231: "Role" = None, express_core_Redeclaration233: "ScopedId" = None, express_core_Redeclaration: "Expression" = None, express_core_Redeclaration216: "AttributeType" = None, express_core_Redeclaration218: "Redeclaration" = None, express_core_Redeclaration220: "SizeConstraint" = None):
        self.position = position
        self.isMandatory = isMandatory
        self.express_core_Redeclaration223 = express_core_Redeclaration223
        self.redeclarations = redeclarations
        self.express_core_Redeclaration228 = express_core_Redeclaration228
        self.express_core_Redeclaration231 = express_core_Redeclaration231
        self.express_core_Redeclaration233 = express_core_Redeclaration233
        self.express_core_Redeclaration = express_core_Redeclaration
        self.express_core_Redeclaration216 = express_core_Redeclaration216
        self.express_core_Redeclaration218 = express_core_Redeclaration218
        self.express_core_Redeclaration220 = express_core_Redeclaration220
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def isMandatory(self):
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: str):
        self.__isMandatory = isMandatory


    @property
    def express_core_Redeclaration223(self):
        return self.__express_core_Redeclaration223

    @express_core_Redeclaration223.setter
    def express_core_Redeclaration223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration223", None)
        self.__express_core_Redeclaration223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint224"):
                opp_val = getattr(old_value, "SizeConstraint224", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint224"):
                opp_val = getattr(value, "SizeConstraint224", None)
                setattr(value, "SizeConstraint224", self)

    @property
    def express_core_Redeclaration(self):
        return self.__express_core_Redeclaration

    @express_core_Redeclaration.setter
    def express_core_Redeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration", None)
        self.__express_core_Redeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression214"):
                opp_val = getattr(old_value, "Expression214", None)
                if opp_val == self:
                    setattr(old_value, "Expression214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression214"):
                opp_val = getattr(value, "Expression214", None)
                setattr(value, "Expression214", self)

    @property
    def express_core_Redeclaration231(self):
        return self.__express_core_Redeclaration231

    @express_core_Redeclaration231.setter
    def express_core_Redeclaration231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration231", None)
        self.__express_core_Redeclaration231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role"):
                opp_val = getattr(old_value, "Role", None)
                if opp_val == self:
                    setattr(old_value, "Role", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role"):
                opp_val = getattr(value, "Role", None)
                setattr(value, "Role", self)

    @property
    def express_core_Redeclaration220(self):
        return self.__express_core_Redeclaration220

    @express_core_Redeclaration220.setter
    def express_core_Redeclaration220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration220", None)
        self.__express_core_Redeclaration220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint221"):
                opp_val = getattr(old_value, "SizeConstraint221", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint221"):
                opp_val = getattr(value, "SizeConstraint221", None)
                setattr(value, "SizeConstraint221", self)

    @property
    def express_core_Redeclaration228(self):
        return self.__express_core_Redeclaration228

    @express_core_Redeclaration228.setter
    def express_core_Redeclaration228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration228", None)
        self.__express_core_Redeclaration228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute229"):
                opp_val = getattr(old_value, "Attribute229", None)
                if opp_val == self:
                    setattr(old_value, "Attribute229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute229"):
                opp_val = getattr(value, "Attribute229", None)
                setattr(value, "Attribute229", self)

    @property
    def express_core_Redeclaration216(self):
        return self.__express_core_Redeclaration216

    @express_core_Redeclaration216.setter
    def express_core_Redeclaration216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration216", None)
        self.__express_core_Redeclaration216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributeType"):
                opp_val = getattr(old_value, "AttributeType", None)
                if opp_val == self:
                    setattr(old_value, "AttributeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributeType"):
                opp_val = getattr(value, "AttributeType", None)
                setattr(value, "AttributeType", self)

    @property
    def express_core_Redeclaration233(self):
        return self.__express_core_Redeclaration233

    @express_core_Redeclaration233.setter
    def express_core_Redeclaration233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration233", None)
        self.__express_core_Redeclaration233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScopedId234"):
                opp_val = getattr(old_value, "ScopedId234", None)
                if opp_val == self:
                    setattr(old_value, "ScopedId234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScopedId234"):
                opp_val = getattr(value, "ScopedId234", None)
                setattr(value, "ScopedId234", self)

    @property
    def express_core_Redeclaration218(self):
        return self.__express_core_Redeclaration218

    @express_core_Redeclaration218.setter
    def express_core_Redeclaration218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__express_core_Redeclaration218", None)
        self.__express_core_Redeclaration218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Redeclaration"):
                opp_val = getattr(old_value, "Redeclaration", None)
                if opp_val == self:
                    setattr(old_value, "Redeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Redeclaration"):
                opp_val = getattr(value, "Redeclaration", None)
                setattr(value, "Redeclaration", self)

    @property
    def redeclarations(self):
        return self.__redeclarations

    @redeclarations.setter
    def redeclarations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Redeclaration__redeclarations", None)
        self.__redeclarations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityType226"):
                opp_val = getattr(old_value, "EntityType226", None)
                if opp_val == self:
                    setattr(old_value, "EntityType226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityType226"):
                opp_val = getattr(value, "EntityType226", None)
                setattr(value, "EntityType226", self)

class ConcreteAggregationType:

    pass
class express_core_SETType(ConcreteAggregationType):

    pass
class express_core_BAGType(ConcreteAggregationType):

    pass
class express_core_ARRAYType(ConcreteAggregationType):

    def __init__(self, isOptional: str, express_core_ARRAYType: "ArrayBound" = None, express_core_ARRAYType403: "ArrayBound" = None):
        self.isOptional = isOptional
        self.express_core_ARRAYType = express_core_ARRAYType
        self.express_core_ARRAYType403 = express_core_ARRAYType403
        
        pass
    @property
    def isOptional(self):
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional


    @property
    def express_core_ARRAYType(self):
        return self.__express_core_ARRAYType

    @express_core_ARRAYType.setter
    def express_core_ARRAYType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_ARRAYType__express_core_ARRAYType", None)
        self.__express_core_ARRAYType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound401"):
                opp_val = getattr(old_value, "ArrayBound401", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound401", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound401"):
                opp_val = getattr(value, "ArrayBound401", None)
                setattr(value, "ArrayBound401", self)

    @property
    def express_core_ARRAYType403(self):
        return self.__express_core_ARRAYType403

    @express_core_ARRAYType403.setter
    def express_core_ARRAYType403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_ARRAYType__express_core_ARRAYType403", None)
        self.__express_core_ARRAYType403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound404"):
                opp_val = getattr(old_value, "ArrayBound404", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound404"):
                opp_val = getattr(value, "ArrayBound404", None)
                setattr(value, "ArrayBound404", self)

class express_core_LISTType(ConcreteAggregationType):

    pass
class UniqueRule:

    pass
class RangeRole:

    pass
class DefinedType:

    pass
class express_core_SelectType(DefinedType):

    def __init__(self, isExtensible: str, isEntity: str, instantiates: set["NamedType"] = None, base383: set["SelectType"] = None, extension386: "SelectType" = None, express_core_SelectType: set["NamedType"] = None):
        self.isExtensible = isExtensible
        self.isEntity = isEntity
        self.instantiates = instantiates if instantiates is not None else set()
        self.base383 = base383 if base383 is not None else set()
        self.extension386 = extension386
        self.express_core_SelectType = express_core_SelectType if express_core_SelectType is not None else set()
        
        pass
    @property
    def isExtensible(self):
        return self.__isExtensible

    @isExtensible.setter
    def isExtensible(self, isExtensible: str):
        self.__isExtensible = isExtensible


    @property
    def isEntity(self):
        return self.__isEntity

    @isEntity.setter
    def isEntity(self, isEntity: str):
        self.__isEntity = isEntity


    @property
    def base383(self):
        return self.__base383

    @base383.setter
    def base383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_SelectType__base383", None)
        self.__base383 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SelectType384"):
                    opp_val = getattr(item, "SelectType384", None)
                    
                    if opp_val == self:
                        setattr(item, "SelectType384", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SelectType384"):
                    opp_val = getattr(item, "SelectType384", None)
                    
                    setattr(item, "SelectType384", self)
                    

    @property
    def express_core_SelectType(self):
        return self.__express_core_SelectType

    @express_core_SelectType.setter
    def express_core_SelectType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_SelectType__express_core_SelectType", None)
        self.__express_core_SelectType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedType389"):
                    opp_val = getattr(item, "NamedType389", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedType389", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedType389"):
                    opp_val = getattr(item, "NamedType389", None)
                    
                    setattr(item, "NamedType389", self)
                    

    @property
    def instantiates(self):
        return self.__instantiates

    @instantiates.setter
    def instantiates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_SelectType__instantiates", None)
        self.__instantiates = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NamedType381"):
                    opp_val = getattr(item, "NamedType381", None)
                    
                    if opp_val == self:
                        setattr(item, "NamedType381", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NamedType381"):
                    opp_val = getattr(item, "NamedType381", None)
                    
                    setattr(item, "NamedType381", self)
                    

    @property
    def extension386(self):
        return self.__extension386

    @extension386.setter
    def extension386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_SelectType__extension386", None)
        self.__extension386 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SelectType387"):
                opp_val = getattr(old_value, "SelectType387", None)
                if opp_val == self:
                    setattr(old_value, "SelectType387", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SelectType387"):
                opp_val = getattr(value, "SelectType387", None)
                setattr(value, "SelectType387", self)

class express_core_SpecializedType(DefinedType):

    pass
class express_core_EnumerationType(DefinedType):

    def __init__(self, isExtensible: str, express_core_EnumerationType: set["EnumerationItem"] = None, declaredIn: set["EnumerationItem"] = None, base: set["EnumerationType"] = None, extension209: "EnumerationType" = None):
        self.isExtensible = isExtensible
        self.express_core_EnumerationType = express_core_EnumerationType if express_core_EnumerationType is not None else set()
        self.declaredIn = declaredIn if declaredIn is not None else set()
        self.base = base if base is not None else set()
        self.extension209 = extension209
        
        pass
    @property
    def isExtensible(self):
        return self.__isExtensible

    @isExtensible.setter
    def isExtensible(self, isExtensible: str):
        self.__isExtensible = isExtensible


    @property
    def declaredIn(self):
        return self.__declaredIn

    @declaredIn.setter
    def declaredIn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EnumerationType__declaredIn", None)
        self.__declaredIn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnumerationItem206"):
                    opp_val = getattr(item, "EnumerationItem206", None)
                    
                    if opp_val == self:
                        setattr(item, "EnumerationItem206", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnumerationItem206"):
                    opp_val = getattr(item, "EnumerationItem206", None)
                    
                    setattr(item, "EnumerationItem206", self)
                    

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EnumerationType__base", None)
        self.__base = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnumerationType"):
                    opp_val = getattr(item, "EnumerationType", None)
                    
                    if opp_val == self:
                        setattr(item, "EnumerationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnumerationType"):
                    opp_val = getattr(item, "EnumerationType", None)
                    
                    setattr(item, "EnumerationType", self)
                    

    @property
    def extension209(self):
        return self.__extension209

    @extension209.setter
    def extension209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EnumerationType__extension209", None)
        self.__extension209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnumerationType210"):
                opp_val = getattr(old_value, "EnumerationType210", None)
                if opp_val == self:
                    setattr(old_value, "EnumerationType210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnumerationType210"):
                opp_val = getattr(value, "EnumerationType210", None)
                setattr(value, "EnumerationType210", self)

    @property
    def express_core_EnumerationType(self):
        return self.__express_core_EnumerationType

    @express_core_EnumerationType.setter
    def express_core_EnumerationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_EnumerationType__express_core_EnumerationType", None)
        self.__express_core_EnumerationType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnumerationItem204"):
                    opp_val = getattr(item, "EnumerationItem204", None)
                    
                    if opp_val == self:
                        setattr(item, "EnumerationItem204", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnumerationItem204"):
                    opp_val = getattr(item, "EnumerationItem204", None)
                    
                    setattr(item, "EnumerationItem204", self)
                    

class InvertibleAttribute:

    pass
class DomainRole:

    pass
class DataType:

    pass
class express_core_PartialEntityType(DataType):

    pass
class Scope:

    pass
class express_core_LocalScope(Scope):

    pass
class express_core_Schema(Scope):

    def __init__(self, name: str, version: str, describesSchema: set["Remark"] = None, interfacingSchema: set["InterfacedElement"] = None, definedIn: set["SchemaElement"] = None, referencedIn: set["SchemaElement"] = None, Scope368: "express_core_ScopedId" = None, Scope299: "express_core_NamedElement" = None, Scope: "express_core_Expression" = None, Scope336: "express_core_Remark" = None):
        self.name = name
        self.version = version
        self.describesSchema = describesSchema if describesSchema is not None else set()
        self.interfacingSchema = interfacingSchema if interfacingSchema is not None else set()
        self.definedIn = definedIn if definedIn is not None else set()
        self.referencedIn = referencedIn if referencedIn is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def describesSchema(self):
        return self.__describesSchema

    @describesSchema.setter
    def describesSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Schema__describesSchema", None)
        self.__describesSchema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Remark"):
                    opp_val = getattr(item, "Remark", None)
                    
                    if opp_val == self:
                        setattr(item, "Remark", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Remark"):
                    opp_val = getattr(item, "Remark", None)
                    
                    setattr(item, "Remark", self)
                    

    @property
    def referencedIn(self):
        return self.__referencedIn

    @referencedIn.setter
    def referencedIn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Schema__referencedIn", None)
        self.__referencedIn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SchemaElement266"):
                    opp_val = getattr(item, "SchemaElement266", None)
                    
                    if opp_val == self:
                        setattr(item, "SchemaElement266", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SchemaElement266"):
                    opp_val = getattr(item, "SchemaElement266", None)
                    
                    setattr(item, "SchemaElement266", self)
                    

    @property
    def definedIn(self):
        return self.__definedIn

    @definedIn.setter
    def definedIn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Schema__definedIn", None)
        self.__definedIn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SchemaElement"):
                    opp_val = getattr(item, "SchemaElement", None)
                    
                    if opp_val == self:
                        setattr(item, "SchemaElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SchemaElement"):
                    opp_val = getattr(item, "SchemaElement", None)
                    
                    setattr(item, "SchemaElement", self)
                    

    @property
    def interfacingSchema(self):
        return self.__interfacingSchema

    @interfacingSchema.setter
    def interfacingSchema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Schema__interfacingSchema", None)
        self.__interfacingSchema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InterfacedElement"):
                    opp_val = getattr(item, "InterfacedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "InterfacedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InterfacedElement"):
                    opp_val = getattr(item, "InterfacedElement", None)
                    
                    setattr(item, "InterfacedElement", self)
                    

class Instance:

    pass
class express_instances_ConcreteValue(Instance):

    pass
class express_instances_PartialEntityValue(Instance):

    pass
class express_core_Expression:

    def __init__(self, text: str, express_core_Expression: "Instance" = None, express_core_Expression198: "Scope" = None, express_core_Expression200: "DataType" = None):
        self.text = text
        self.express_core_Expression = express_core_Expression
        self.express_core_Expression198 = express_core_Expression198
        self.express_core_Expression200 = express_core_Expression200
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def express_core_Expression(self):
        return self.__express_core_Expression

    @express_core_Expression.setter
    def express_core_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Expression__express_core_Expression", None)
        self.__express_core_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instance"):
                opp_val = getattr(old_value, "Instance", None)
                if opp_val == self:
                    setattr(old_value, "Instance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instance"):
                opp_val = getattr(value, "Instance", None)
                setattr(value, "Instance", self)

    @property
    def express_core_Expression200(self):
        return self.__express_core_Expression200

    @express_core_Expression200.setter
    def express_core_Expression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Expression__express_core_Expression200", None)
        self.__express_core_Expression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def express_core_Expression198(self):
        return self.__express_core_Expression198

    @express_core_Expression198.setter
    def express_core_Expression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_Expression__express_core_Expression198", None)
        self.__express_core_Expression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Scope"):
                opp_val = getattr(old_value, "Scope", None)
                if opp_val == self:
                    setattr(old_value, "Scope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Scope"):
                opp_val = getattr(value, "Scope", None)
                setattr(value, "Scope", self)

class InstantiableType:

    pass
class express_core_ConcreteType(InstantiableType):

    pass
class core_AggregationType:

    pass
class core_GeneralizedType:

    pass
class express_core_GeneralAggregationType(core_AggregationType, core_GeneralizedType):

    pass
class core_TypeElement:

    pass
class core_DomainConstraint:

    pass
class express_core_DomainRule(core_DomainConstraint, core_TypeElement):

    def __init__(self, position: str):
        self.position = position
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


class GeneralAggregationType:

    pass
class express_core_GeneralSETType(GeneralAggregationType):

    pass
class express_core_GeneralLISTType(GeneralAggregationType):

    pass
class express_core_GeneralARRAYType(GeneralAggregationType):

    def __init__(self, isOptional: str, express_core_GeneralARRAYType: "ArrayBound" = None, express_core_GeneralARRAYType351: "ArrayBound" = None):
        self.isOptional = isOptional
        self.express_core_GeneralARRAYType = express_core_GeneralARRAYType
        self.express_core_GeneralARRAYType351 = express_core_GeneralARRAYType351
        
        pass
    @property
    def isOptional(self):
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional


    @property
    def express_core_GeneralARRAYType351(self):
        return self.__express_core_GeneralARRAYType351

    @express_core_GeneralARRAYType351.setter
    def express_core_GeneralARRAYType351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_GeneralARRAYType__express_core_GeneralARRAYType351", None)
        self.__express_core_GeneralARRAYType351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound352"):
                opp_val = getattr(old_value, "ArrayBound352", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound352"):
                opp_val = getattr(value, "ArrayBound352", None)
                setattr(value, "ArrayBound352", self)

    @property
    def express_core_GeneralARRAYType(self):
        return self.__express_core_GeneralARRAYType

    @express_core_GeneralARRAYType.setter
    def express_core_GeneralARRAYType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_GeneralARRAYType__express_core_GeneralARRAYType", None)
        self.__express_core_GeneralARRAYType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound"):
                opp_val = getattr(old_value, "ArrayBound", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound"):
                opp_val = getattr(value, "ArrayBound", None)
                setattr(value, "ArrayBound", self)

class express_core_GeneralBAGType(GeneralAggregationType):

    pass
class ActualStructureConstraint:

    pass
class ParameterType:

    pass
class express_core_ArrayBound:

    def __init__(self, bound: str, express_core_ArrayBound: "Expression" = None):
        self.bound = bound
        self.express_core_ArrayBound = express_core_ArrayBound
        
        pass
    @property
    def bound(self):
        return self.__bound

    @bound.setter
    def bound(self, bound: str):
        self.__bound = bound


    @property
    def express_core_ArrayBound(self):
        return self.__express_core_ArrayBound

    @express_core_ArrayBound.setter
    def express_core_ArrayBound(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_ArrayBound__express_core_ArrayBound", None)
        self.__express_core_ArrayBound = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression212"):
                opp_val = getattr(old_value, "Expression212", None)
                if opp_val == self:
                    setattr(old_value, "Expression212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression212"):
                opp_val = getattr(value, "Expression212", None)
                setattr(value, "Expression212", self)

class core_AttributeType:

    pass
class express_core_NamedType(core_AttributeType, core_Scope, core_CommonElement, core_InstantiableType):

    pass
class express_core_GeneralizedType(core_ParameterType, core_AttributeType):

    pass
class core_DataType:

    pass
class express_core_VariableType(core_DataType, core_AttributeType):

    pass
class EnumerationType:

    pass
class NamedType:

    pass
class ListMember:

    pass
class RepeatCount:

    pass
class express_expressions_MemberBinding:

    def __init__(self, position: str, express_expressions_MemberBinding: "RepeatCount" = None, express_expressions_MemberBinding171: set["ListMember"] = None, express_expressions_MemberBinding173: "Expression" = None):
        self.position = position
        self.express_expressions_MemberBinding = express_expressions_MemberBinding
        self.express_expressions_MemberBinding171 = express_expressions_MemberBinding171 if express_expressions_MemberBinding171 is not None else set()
        self.express_expressions_MemberBinding173 = express_expressions_MemberBinding173
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def express_expressions_MemberBinding173(self):
        return self.__express_expressions_MemberBinding173

    @express_expressions_MemberBinding173.setter
    def express_expressions_MemberBinding173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_MemberBinding__express_expressions_MemberBinding173", None)
        self.__express_expressions_MemberBinding173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression174"):
                opp_val = getattr(old_value, "Expression174", None)
                if opp_val == self:
                    setattr(old_value, "Expression174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression174"):
                opp_val = getattr(value, "Expression174", None)
                setattr(value, "Expression174", self)

    @property
    def express_expressions_MemberBinding171(self):
        return self.__express_expressions_MemberBinding171

    @express_expressions_MemberBinding171.setter
    def express_expressions_MemberBinding171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_MemberBinding__express_expressions_MemberBinding171", None)
        self.__express_expressions_MemberBinding171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ListMember"):
                    opp_val = getattr(item, "ListMember", None)
                    
                    if opp_val == self:
                        setattr(item, "ListMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ListMember"):
                    opp_val = getattr(item, "ListMember", None)
                    
                    setattr(item, "ListMember", self)
                    

    @property
    def express_expressions_MemberBinding(self):
        return self.__express_expressions_MemberBinding

    @express_expressions_MemberBinding.setter
    def express_expressions_MemberBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_MemberBinding__express_expressions_MemberBinding", None)
        self.__express_expressions_MemberBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepeatCount"):
                opp_val = getattr(old_value, "RepeatCount", None)
                if opp_val == self:
                    setattr(old_value, "RepeatCount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepeatCount"):
                opp_val = getattr(value, "RepeatCount", None)
                setattr(value, "RepeatCount", self)

class FunctionResult:

    pass
class Function:

    pass
class SizeConstraint:

    pass
class GeneralizedType:

    pass
class express_core_GenericType(GeneralizedType):

    def __init__(self, isEntity: str, matchingType: "ActualTypeConstraint" = None, GeneralizedType: "express_core_GeneralAggregationType" = None, GeneralizedType379: "express_core_ParameterType" = None):
        self.isEntity = isEntity
        self.matchingType = matchingType
        
        pass
    @property
    def isEntity(self):
        return self.__isEntity

    @isEntity.setter
    def isEntity(self, isEntity: str):
        self.__isEntity = isEntity


    @property
    def matchingType(self):
        return self.__matchingType

    @matchingType.setter
    def matchingType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_GenericType__matchingType", None)
        self.__matchingType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActualTypeConstraint"):
                opp_val = getattr(old_value, "ActualTypeConstraint", None)
                if opp_val == self:
                    setattr(old_value, "ActualTypeConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActualTypeConstraint"):
                opp_val = getattr(value, "ActualTypeConstraint", None)
                setattr(value, "ActualTypeConstraint", self)

class express_core_AGGREGATEType(GeneralizedType):

    pass
class PartialEntityType:

    pass
class express_core_SingleEntityType:

    pass
class NamedElement:

    pass
class express_core_LocalElement(NamedElement):

    pass
class express_core_TypeElement(NamedElement):

    pass
class core_Expression:

    pass
class Constant:

    pass
class Attribute:

    pass
class express_core_DerivedAttribute(Attribute):

    pass
class express_core_InverseAttribute(Attribute):

    def __init__(self, isUnique: str, rangeView: "DomainRole" = None, inverse: "InvertibleAttribute" = None, Attribute241: "express_core_EntityType" = None, Attribute148: "express_expressions_UsedInRef" = None, Attribute285: "express_core_UniqueRule" = None, Attribute321: "express_core_AttributeType" = None, Attribute469: "express_instances_RoleName" = None, Attribute180: "express_core_SingleEntityType" = None, Attribute229: "express_core_Redeclaration" = None, Attribute: "express_expressions_AttributeRef" = None):
        self.isUnique = isUnique
        self.rangeView = rangeView
        self.inverse = inverse
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


    @property
    def rangeView(self):
        return self.__rangeView

    @rangeView.setter
    def rangeView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_InverseAttribute__rangeView", None)
        self.__rangeView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DomainRole"):
                opp_val = getattr(old_value, "DomainRole", None)
                if opp_val == self:
                    setattr(old_value, "DomainRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DomainRole"):
                opp_val = getattr(value, "DomainRole", None)
                setattr(value, "DomainRole", self)

    @property
    def inverse(self):
        return self.__inverse

    @inverse.setter
    def inverse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_core_InverseAttribute__inverse", None)
        self.__inverse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InvertibleAttribute"):
                opp_val = getattr(old_value, "InvertibleAttribute", None)
                if opp_val == self:
                    setattr(old_value, "InvertibleAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InvertibleAttribute"):
                opp_val = getattr(value, "InvertibleAttribute", None)
                setattr(value, "InvertibleAttribute", self)

class Selector:

    pass
class express_expressions_GroupRef(Selector):

    def __init__(self, id: str, express_expressions_GroupRef: "SingleEntityType" = None):
        self.id = id
        self.express_expressions_GroupRef = express_expressions_GroupRef
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_expressions_GroupRef(self):
        return self.__express_expressions_GroupRef

    @express_expressions_GroupRef.setter
    def express_expressions_GroupRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_GroupRef__express_expressions_GroupRef", None)
        self.__express_expressions_GroupRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleEntityType144"):
                opp_val = getattr(old_value, "SingleEntityType144", None)
                if opp_val == self:
                    setattr(old_value, "SingleEntityType144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleEntityType144"):
                opp_val = getattr(value, "SingleEntityType144", None)
                setattr(value, "SingleEntityType144", self)

class express_expressions_UsedInRef(Selector):

    pass
class express_expressions_AttributeRef(Selector):

    def __init__(self, id: str, express_expressions_AttributeRef: "Attribute" = None):
        self.id = id
        self.express_expressions_AttributeRef = express_expressions_AttributeRef
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_expressions_AttributeRef(self):
        return self.__express_expressions_AttributeRef

    @express_expressions_AttributeRef.setter
    def express_expressions_AttributeRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_AttributeRef__express_expressions_AttributeRef", None)
        self.__express_expressions_AttributeRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute"):
                opp_val = getattr(old_value, "Attribute", None)
                if opp_val == self:
                    setattr(old_value, "Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute"):
                opp_val = getattr(value, "Attribute", None)
                setattr(value, "Attribute", self)

class AttributeValue:

    pass
class express_expressions_AttributeBinding:

    def __init__(self, position: str, express_expressions_AttributeBinding: "Expression" = None, express_expressions_AttributeBinding160: "AttributeValue" = None, express_expressions_AttributeBinding162: "ExplicitAttribute" = None):
        self.position = position
        self.express_expressions_AttributeBinding = express_expressions_AttributeBinding
        self.express_expressions_AttributeBinding160 = express_expressions_AttributeBinding160
        self.express_expressions_AttributeBinding162 = express_expressions_AttributeBinding162
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def express_expressions_AttributeBinding162(self):
        return self.__express_expressions_AttributeBinding162

    @express_expressions_AttributeBinding162.setter
    def express_expressions_AttributeBinding162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_AttributeBinding__express_expressions_AttributeBinding162", None)
        self.__express_expressions_AttributeBinding162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExplicitAttribute163"):
                opp_val = getattr(old_value, "ExplicitAttribute163", None)
                if opp_val == self:
                    setattr(old_value, "ExplicitAttribute163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExplicitAttribute163"):
                opp_val = getattr(value, "ExplicitAttribute163", None)
                setattr(value, "ExplicitAttribute163", self)

    @property
    def express_expressions_AttributeBinding(self):
        return self.__express_expressions_AttributeBinding

    @express_expressions_AttributeBinding.setter
    def express_expressions_AttributeBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_AttributeBinding__express_expressions_AttributeBinding", None)
        self.__express_expressions_AttributeBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression158"):
                opp_val = getattr(old_value, "Expression158", None)
                if opp_val == self:
                    setattr(old_value, "Expression158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression158"):
                opp_val = getattr(value, "Expression158", None)
                setattr(value, "Expression158", self)

    @property
    def express_expressions_AttributeBinding160(self):
        return self.__express_expressions_AttributeBinding160

    @express_expressions_AttributeBinding160.setter
    def express_expressions_AttributeBinding160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_AttributeBinding__express_expressions_AttributeBinding160", None)
        self.__express_expressions_AttributeBinding160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributeValue"):
                opp_val = getattr(old_value, "AttributeValue", None)
                if opp_val == self:
                    setattr(old_value, "AttributeValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributeValue"):
                opp_val = getattr(value, "AttributeValue", None)
                setattr(value, "AttributeValue", self)

class QueryVariable:

    pass
class VariableType:

    pass
class AttributeBinding:

    pass
class PartialEntityValue:

    pass
class MemberBinding:

    pass
class GenericAggregate:

    pass
class Operation:

    pass
class express_expressions_UnaryOperation(Operation):

    def __init__(self, operator: str, express_expressions_UnaryOperation: "Expression" = None):
        self.operator = operator
        self.express_expressions_UnaryOperation = express_expressions_UnaryOperation
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def express_expressions_UnaryOperation(self):
        return self.__express_expressions_UnaryOperation

    @express_expressions_UnaryOperation.setter
    def express_expressions_UnaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_UnaryOperation__express_expressions_UnaryOperation", None)
        self.__express_expressions_UnaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression146"):
                opp_val = getattr(old_value, "Expression146", None)
                if opp_val == self:
                    setattr(old_value, "Expression146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression146"):
                opp_val = getattr(value, "Expression146", None)
                setattr(value, "Expression146", self)

class express_expressions_Coercion(Operation):

    pass
class express_expressions_BinaryOperation(Operation):

    def __init__(self, operator: str, express_expressions_BinaryOperation: "Expression" = None, express_expressions_BinaryOperation108: "Expression" = None):
        self.operator = operator
        self.express_expressions_BinaryOperation = express_expressions_BinaryOperation
        self.express_expressions_BinaryOperation108 = express_expressions_BinaryOperation108
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def express_expressions_BinaryOperation(self):
        return self.__express_expressions_BinaryOperation

    @express_expressions_BinaryOperation.setter
    def express_expressions_BinaryOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_BinaryOperation__express_expressions_BinaryOperation", None)
        self.__express_expressions_BinaryOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression106"):
                opp_val = getattr(old_value, "Expression106", None)
                if opp_val == self:
                    setattr(old_value, "Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression106"):
                opp_val = getattr(value, "Expression106", None)
                setattr(value, "Expression106", self)

    @property
    def express_expressions_BinaryOperation108(self):
        return self.__express_expressions_BinaryOperation108

    @express_expressions_BinaryOperation108.setter
    def express_expressions_BinaryOperation108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_BinaryOperation__express_expressions_BinaryOperation108", None)
        self.__express_expressions_BinaryOperation108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression109"):
                opp_val = getattr(old_value, "Expression109", None)
                if opp_val == self:
                    setattr(old_value, "Expression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression109"):
                opp_val = getattr(value, "Expression109", None)
                setattr(value, "Expression109", self)

class Parameter:

    pass
class FunctionCall:

    pass
class ProcedureCall:

    pass
class express_expressions_ActualParameter:

    def __init__(self, position: str, actualParameters: "ProcedureCall" = None, actualParameters130: "FunctionCall" = None, express_expressions_ActualParameter: "Parameter" = None, express_expressions_ActualParameter133: "VARExpression" = None, express_expressions_ActualParameter136: "Expression" = None):
        self.position = position
        self.actualParameters = actualParameters
        self.actualParameters130 = actualParameters130
        self.express_expressions_ActualParameter = express_expressions_ActualParameter
        self.express_expressions_ActualParameter133 = express_expressions_ActualParameter133
        self.express_expressions_ActualParameter136 = express_expressions_ActualParameter136
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def express_expressions_ActualParameter(self):
        return self.__express_expressions_ActualParameter

    @express_expressions_ActualParameter.setter
    def express_expressions_ActualParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ActualParameter__express_expressions_ActualParameter", None)
        self.__express_expressions_ActualParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter"):
                opp_val = getattr(old_value, "Parameter", None)
                if opp_val == self:
                    setattr(old_value, "Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter"):
                opp_val = getattr(value, "Parameter", None)
                setattr(value, "Parameter", self)

    @property
    def express_expressions_ActualParameter133(self):
        return self.__express_expressions_ActualParameter133

    @express_expressions_ActualParameter133.setter
    def express_expressions_ActualParameter133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ActualParameter__express_expressions_ActualParameter133", None)
        self.__express_expressions_ActualParameter133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VARExpression134"):
                opp_val = getattr(old_value, "VARExpression134", None)
                if opp_val == self:
                    setattr(old_value, "VARExpression134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VARExpression134"):
                opp_val = getattr(value, "VARExpression134", None)
                setattr(value, "VARExpression134", self)

    @property
    def actualParameters(self):
        return self.__actualParameters

    @actualParameters.setter
    def actualParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ActualParameter__actualParameters", None)
        self.__actualParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcedureCall"):
                opp_val = getattr(old_value, "ProcedureCall", None)
                if opp_val == self:
                    setattr(old_value, "ProcedureCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcedureCall"):
                opp_val = getattr(value, "ProcedureCall", None)
                setattr(value, "ProcedureCall", self)

    @property
    def express_expressions_ActualParameter136(self):
        return self.__express_expressions_ActualParameter136

    @express_expressions_ActualParameter136.setter
    def express_expressions_ActualParameter136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ActualParameter__express_expressions_ActualParameter136", None)
        self.__express_expressions_ActualParameter136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression137"):
                opp_val = getattr(old_value, "Expression137", None)
                if opp_val == self:
                    setattr(old_value, "Expression137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression137"):
                opp_val = getattr(value, "Expression137", None)
                setattr(value, "Expression137", self)

    @property
    def actualParameters130(self):
        return self.__actualParameters130

    @actualParameters130.setter
    def actualParameters130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ActualParameter__actualParameters130", None)
        self.__actualParameters130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FunctionCall"):
                opp_val = getattr(old_value, "FunctionCall", None)
                if opp_val == self:
                    setattr(old_value, "FunctionCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FunctionCall"):
                opp_val = getattr(value, "FunctionCall", None)
                setattr(value, "FunctionCall", self)

class IndexOperation:

    pass
class express_expressions_StringIndex(IndexOperation):

    pass
class express_expressions_AggregateIndex(IndexOperation):

    pass
class express_expressions_BinaryIndex(IndexOperation):

    pass
class SimpleValue:

    pass
class express_instances_StringValue(SimpleValue):

    pass
class EnumerationItem:

    pass
class Primary:

    pass
class express_expressions_ParameterRef(Primary):

    def __init__(self, id: str, express_expressions_ParameterRef: "Parameter" = None):
        self.id = id
        self.express_expressions_ParameterRef = express_expressions_ParameterRef
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_expressions_ParameterRef(self):
        return self.__express_expressions_ParameterRef

    @express_expressions_ParameterRef.setter
    def express_expressions_ParameterRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ParameterRef__express_expressions_ParameterRef", None)
        self.__express_expressions_ParameterRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Parameter139"):
                opp_val = getattr(old_value, "Parameter139", None)
                if opp_val == self:
                    setattr(old_value, "Parameter139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Parameter139"):
                opp_val = getattr(value, "Parameter139", None)
                setattr(value, "Parameter139", self)

class express_expressions_ConstantRef(Primary):

    def __init__(self, id: str, express_expressions_ConstantRef: "Constant" = None):
        self.id = id
        self.express_expressions_ConstantRef = express_expressions_ConstantRef
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_expressions_ConstantRef(self):
        return self.__express_expressions_ConstantRef

    @express_expressions_ConstantRef.setter
    def express_expressions_ConstantRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ConstantRef__express_expressions_ConstantRef", None)
        self.__express_expressions_ConstantRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constant"):
                opp_val = getattr(old_value, "Constant", None)
                if opp_val == self:
                    setattr(old_value, "Constant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constant"):
                opp_val = getattr(value, "Constant", None)
                setattr(value, "Constant", self)

class express_expressions_IndeterminateRef(Primary):

    pass
class express_expressions_ExtentRef(Primary):

    def __init__(self, id: str, express_expressions_ExtentRef: "NamedType" = None):
        self.id = id
        self.express_expressions_ExtentRef = express_expressions_ExtentRef
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_expressions_ExtentRef(self):
        return self.__express_expressions_ExtentRef

    @express_expressions_ExtentRef.setter
    def express_expressions_ExtentRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_ExtentRef__express_expressions_ExtentRef", None)
        self.__express_expressions_ExtentRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamedType"):
                opp_val = getattr(old_value, "NamedType", None)
                if opp_val == self:
                    setattr(old_value, "NamedType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamedType"):
                opp_val = getattr(value, "NamedType", None)
                setattr(value, "NamedType", self)

class express_expressions_VariableRef(Primary):

    def __init__(self, id: str, express_expressions_VariableRef: "NamedVariable" = None):
        self.id = id
        self.express_expressions_VariableRef = express_expressions_VariableRef
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_expressions_VariableRef(self):
        return self.__express_expressions_VariableRef

    @express_expressions_VariableRef.setter
    def express_expressions_VariableRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_VariableRef__express_expressions_VariableRef", None)
        self.__express_expressions_VariableRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamedVariable"):
                opp_val = getattr(old_value, "NamedVariable", None)
                if opp_val == self:
                    setattr(old_value, "NamedVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamedVariable"):
                opp_val = getattr(value, "NamedVariable", None)
                setattr(value, "NamedVariable", self)

class express_expressions_Literal(Primary):

    pass
class express_expressions_EnumItemRef(Primary):

    def __init__(self, id: str, express_expressions_EnumItemRef: "EnumerationItem" = None):
        self.id = id
        self.express_expressions_EnumItemRef = express_expressions_EnumItemRef
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_expressions_EnumItemRef(self):
        return self.__express_expressions_EnumItemRef

    @express_expressions_EnumItemRef.setter
    def express_expressions_EnumItemRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_EnumItemRef__express_expressions_EnumItemRef", None)
        self.__express_expressions_EnumItemRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnumerationItem"):
                opp_val = getattr(old_value, "EnumerationItem", None)
                if opp_val == self:
                    setattr(old_value, "EnumerationItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnumerationItem"):
                opp_val = getattr(value, "EnumerationItem", None)
                setattr(value, "EnumerationItem", self)

class express_expressions_RepeatCount:

    pass
class express_expressions_SELFRef(Primary):

    pass
class Indeterminate:

    pass
class CaseAction:

    pass
class Variable:

    pass
class SingleEntityType:

    pass
class ControlVariable:

    pass
class ExplicitAttribute:

    pass
class express_core_InvertibleAttribute(ExplicitAttribute):

    pass
class express_statements_VARExpression(ABC):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class VARVariable:

    pass
class algorithms_VARVariable:

    pass
class algorithms_NamedVariable:

    pass
class express_statements_AliasVariable(algorithms_NamedVariable, algorithms_VARVariable):

    pass
class NamedVariable:

    pass
class express_expressions_QueryVariable(NamedVariable):

    pass
class express_statements_ControlVariable(NamedVariable):

    pass
class AliasVariable:

    pass
class VARExpression:

    pass
class express_statements_VariableCell(VARExpression):

    def __init__(self, id: str, express_statements_VariableCell: "Variable" = None, VARExpression134: "express_expressions_ActualParameter" = None, VARExpression68: "express_statements_GroupCell" = None, VARExpression45: "express_statements_AttributeCell" = None, VARExpression90: "express_statements_Assignment" = None, VARExpression40: "express_statements_AliasVariable" = None, VARExpression57: "express_statements_MemberCell" = None, VARExpression: "express_statements_AliasStatement" = None):
        self.id = id
        self.express_statements_VariableCell = express_statements_VariableCell
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_statements_VariableCell(self):
        return self.__express_statements_VariableCell

    @express_statements_VariableCell.setter
    def express_statements_VariableCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_VariableCell__express_statements_VariableCell", None)
        self.__express_statements_VariableCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable"):
                opp_val = getattr(old_value, "Variable", None)
                if opp_val == self:
                    setattr(old_value, "Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable"):
                opp_val = getattr(value, "Variable", None)
                setattr(value, "Variable", self)

class express_statements_AttributeCell(VARExpression):

    def __init__(self, id: str, express_statements_AttributeCell: "ExplicitAttribute" = None, express_statements_AttributeCell44: "VARExpression" = None, VARExpression134: "express_expressions_ActualParameter" = None, VARExpression68: "express_statements_GroupCell" = None, VARExpression45: "express_statements_AttributeCell" = None, VARExpression90: "express_statements_Assignment" = None, VARExpression40: "express_statements_AliasVariable" = None, VARExpression57: "express_statements_MemberCell" = None, VARExpression: "express_statements_AliasStatement" = None):
        self.id = id
        self.express_statements_AttributeCell = express_statements_AttributeCell
        self.express_statements_AttributeCell44 = express_statements_AttributeCell44
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_statements_AttributeCell(self):
        return self.__express_statements_AttributeCell

    @express_statements_AttributeCell.setter
    def express_statements_AttributeCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_AttributeCell__express_statements_AttributeCell", None)
        self.__express_statements_AttributeCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExplicitAttribute"):
                opp_val = getattr(old_value, "ExplicitAttribute", None)
                if opp_val == self:
                    setattr(old_value, "ExplicitAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExplicitAttribute"):
                opp_val = getattr(value, "ExplicitAttribute", None)
                setattr(value, "ExplicitAttribute", self)

    @property
    def express_statements_AttributeCell44(self):
        return self.__express_statements_AttributeCell44

    @express_statements_AttributeCell44.setter
    def express_statements_AttributeCell44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_AttributeCell__express_statements_AttributeCell44", None)
        self.__express_statements_AttributeCell44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VARExpression45"):
                opp_val = getattr(old_value, "VARExpression45", None)
                if opp_val == self:
                    setattr(old_value, "VARExpression45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VARExpression45"):
                opp_val = getattr(value, "VARExpression45", None)
                setattr(value, "VARExpression45", self)

class express_statements_GroupCell(VARExpression):

    def __init__(self, id: str, express_statements_GroupCell: "VARExpression" = None, express_statements_GroupCell70: "SingleEntityType" = None, VARExpression134: "express_expressions_ActualParameter" = None, VARExpression68: "express_statements_GroupCell" = None, VARExpression45: "express_statements_AttributeCell" = None, VARExpression90: "express_statements_Assignment" = None, VARExpression40: "express_statements_AliasVariable" = None, VARExpression57: "express_statements_MemberCell" = None, VARExpression: "express_statements_AliasStatement" = None):
        self.id = id
        self.express_statements_GroupCell = express_statements_GroupCell
        self.express_statements_GroupCell70 = express_statements_GroupCell70
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_statements_GroupCell(self):
        return self.__express_statements_GroupCell

    @express_statements_GroupCell.setter
    def express_statements_GroupCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_GroupCell__express_statements_GroupCell", None)
        self.__express_statements_GroupCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VARExpression68"):
                opp_val = getattr(old_value, "VARExpression68", None)
                if opp_val == self:
                    setattr(old_value, "VARExpression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VARExpression68"):
                opp_val = getattr(value, "VARExpression68", None)
                setattr(value, "VARExpression68", self)

    @property
    def express_statements_GroupCell70(self):
        return self.__express_statements_GroupCell70

    @express_statements_GroupCell70.setter
    def express_statements_GroupCell70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_GroupCell__express_statements_GroupCell70", None)
        self.__express_statements_GroupCell70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleEntityType"):
                opp_val = getattr(old_value, "SingleEntityType", None)
                if opp_val == self:
                    setattr(old_value, "SingleEntityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleEntityType"):
                opp_val = getattr(value, "SingleEntityType", None)
                setattr(value, "SingleEntityType", self)

class express_statements_VARCell(VARExpression):

    def __init__(self, id: str, express_statements_VARCell: "VARVariable" = None, VARExpression134: "express_expressions_ActualParameter" = None, VARExpression68: "express_statements_GroupCell" = None, VARExpression45: "express_statements_AttributeCell" = None, VARExpression90: "express_statements_Assignment" = None, VARExpression40: "express_statements_AliasVariable" = None, VARExpression57: "express_statements_MemberCell" = None, VARExpression: "express_statements_AliasStatement" = None):
        self.id = id
        self.express_statements_VARCell = express_statements_VARCell
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_statements_VARCell(self):
        return self.__express_statements_VARCell

    @express_statements_VARCell.setter
    def express_statements_VARCell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_VARCell__express_statements_VARCell", None)
        self.__express_statements_VARCell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VARVariable"):
                opp_val = getattr(old_value, "VARVariable", None)
                if opp_val == self:
                    setattr(old_value, "VARVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VARVariable"):
                opp_val = getattr(value, "VARVariable", None)
                setattr(value, "VARVariable", self)

class express_statements_MemberCell(VARExpression):

    pass
class core_LocalScope:

    pass
class express_expressions_QueryExpression(core_LocalScope, core_Expression):

    pass
class algorithms_Statement:

    pass
class express_statements_RepeatStatement(core_LocalScope, algorithms_Statement):

    pass
class express_statements_AliasStatement(core_LocalScope, algorithms_Statement):

    pass
class ControlStatement:

    pass
class express_statements_EscapeStatement(ControlStatement):

    pass
class express_statements_ReturnStatement(ControlStatement):

    pass
class express_statements_NullStatement(ControlStatement):

    pass
class express_statements_SkipStatement(ControlStatement):

    pass
class express_statements_CaseAction:

    def __init__(self, isDefault: str, express_statements_CaseAction: set["Expression"] = None, express_statements_CaseAction51: "Statement" = None):
        self.isDefault = isDefault
        self.express_statements_CaseAction = express_statements_CaseAction if express_statements_CaseAction is not None else set()
        self.express_statements_CaseAction51 = express_statements_CaseAction51
        
        pass
    @property
    def isDefault(self):
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: str):
        self.__isDefault = isDefault


    @property
    def express_statements_CaseAction51(self):
        return self.__express_statements_CaseAction51

    @express_statements_CaseAction51.setter
    def express_statements_CaseAction51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_CaseAction__express_statements_CaseAction51", None)
        self.__express_statements_CaseAction51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Statement52"):
                opp_val = getattr(old_value, "Statement52", None)
                if opp_val == self:
                    setattr(old_value, "Statement52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement52"):
                opp_val = getattr(value, "Statement52", None)
                setattr(value, "Statement52", self)

    @property
    def express_statements_CaseAction(self):
        return self.__express_statements_CaseAction

    @express_statements_CaseAction.setter
    def express_statements_CaseAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_CaseAction__express_statements_CaseAction", None)
        self.__express_statements_CaseAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression49"):
                    opp_val = getattr(item, "Expression49", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression49"):
                    opp_val = getattr(item, "Expression49", None)
                    
                    setattr(item, "Expression49", self)
                    

class LocalElement:

    pass
class express_rules_NamedRule(LocalElement):

    def __init__(self, position: str, express_rules_NamedRule: "Expression" = None, LocalElement: "express_core_LocalScope" = None):
        self.position = position
        self.express_rules_NamedRule = express_rules_NamedRule
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def express_rules_NamedRule(self):
        return self.__express_rules_NamedRule

    @express_rules_NamedRule.setter
    def express_rules_NamedRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_rules_NamedRule__express_rules_NamedRule", None)
        self.__express_rules_NamedRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression22"):
                opp_val = getattr(old_value, "Expression22", None)
                if opp_val == self:
                    setattr(old_value, "Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression22"):
                opp_val = getattr(value, "Expression22", None)
                setattr(value, "Expression22", self)

class NamedRule:

    pass
class Statement:

    pass
class express_statements_ControlStatement(Statement):

    pass
class express_statements_StatementBlock(Statement):

    def __init__(self, delimited: str, inBlock: set["Statement"] = None, Statement47: "express_statements_StatementBlock" = None, Statement453: "express_algorithms_Algorithm" = None, Statement28: "express_statements_AliasStatement" = None, Statement52: "express_statements_CaseAction" = None, Statement80: "express_statements_IfStatement" = None, Statement83: "express_statements_IfStatement" = None, Statement: "express_rules_GlobalRule" = None, Statement61: "express_statements_RepeatStatement" = None):
        self.delimited = delimited
        self.inBlock = inBlock if inBlock is not None else set()
        
        pass
    @property
    def delimited(self):
        return self.__delimited

    @delimited.setter
    def delimited(self, delimited: str):
        self.__delimited = delimited


    @property
    def inBlock(self):
        return self.__inBlock

    @inBlock.setter
    def inBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_statements_StatementBlock__inBlock", None)
        self.__inBlock = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement47"):
                    opp_val = getattr(item, "Statement47", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement47"):
                    opp_val = getattr(item, "Statement47", None)
                    
                    setattr(item, "Statement47", self)
                    

class express_statements_IfStatement(Statement):

    pass
class express_statements_CaseStatement(Statement):

    pass
class express_statements_Assignment(Statement):

    pass
class core_AlgorithmScope:

    pass
class core_SchemaElement:

    pass
class express_rules_GlobalRule(core_AlgorithmScope, core_SchemaElement):

    pass
class ScopedId:

    pass
class GlobalRule:

    pass
class Population:

    pass
class EntityInstance:

    pass
class express_instances_MultiLeafInstance(EntityInstance):

    pass
class SETValue:

    pass
class express_rules_Extent(SETValue):

    pass
class SupertypeRule:

    pass
class Expression:

    pass
class express_expressions_AggregateInitializer(Expression):

    pass
class express_expressions_FunctionCall(Expression):

    pass
class express_expressions_IndexOperation(Expression):

    pass
class express_expressions_Primary(Expression):

    pass
class express_expressions_Selector(Expression):

    pass
class express_expressions_PartialEntityConstructor(Expression):

    def __init__(self, id: str, express_expressions_PartialEntityConstructor: "PartialEntityValue" = None, express_expressions_PartialEntityConstructor120: "SingleEntityType" = None, express_expressions_PartialEntityConstructor123: set["AttributeBinding"] = None, Expression142: "express_expressions_AggregateIndex" = None, Expression66: "express_statements_RepeatStatement" = None, Expression106: "express_expressions_BinaryOperation" = None, Expression117: "express_expressions_StringIndex" = None, Expression104: "express_expressions_IndexOperation" = None, Expression109: "express_expressions_BinaryOperation" = None, Expression214: "express_core_Redeclaration" = None, Expression477: "express_instances_Constant" = None, Expression59: "express_statements_RepeatStatement" = None, Expression92: "express_expressions_Selector" = None, Expression94: "express_expressions_RepeatCount" = None, Expression156: "express_expressions_QueryExpression" = None, Expression54: "express_statements_MemberCell" = None, Expression87: "express_statements_Assignment" = None, Expression77: "express_statements_IfStatement" = None, Expression411: "express_algorithms_LocalVariable" = None, Expression212: "express_core_ArrayBound" = None, Expression174: "express_expressions_MemberBinding" = None, Expression32: "express_statements_ControlVariable" = None, Expression158: "express_expressions_AttributeBinding" = None, Expression85: "express_statements_ReturnStatement" = None, Expression137: "express_expressions_ActualParameter" = None, Expression125: "express_expressions_Coercion" = None, Expression101: "express_expressions_BinaryIndex" = None, Expression49: "express_statements_CaseAction" = None, Expression98: "express_expressions_BinaryIndex" = None, Expression325: "express_core_DerivedAttribute" = None, Expression151: "express_expressions_QueryExpression" = None, Expression296: "express_core_DomainConstraint" = None, Expression146: "express_expressions_UnaryOperation" = None, Expression22: "express_rules_NamedRule" = None, Expression114: "express_expressions_StringIndex" = None, Expression38: "express_statements_ControlVariable" = None, Expression35: "express_statements_ControlVariable" = None, Expression75: "express_statements_CaseStatement" = None, Expression: "express_rules_SubtypeConstraint" = None):
        self.id = id
        self.express_expressions_PartialEntityConstructor = express_expressions_PartialEntityConstructor
        self.express_expressions_PartialEntityConstructor120 = express_expressions_PartialEntityConstructor120
        self.express_expressions_PartialEntityConstructor123 = express_expressions_PartialEntityConstructor123 if express_expressions_PartialEntityConstructor123 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_expressions_PartialEntityConstructor120(self):
        return self.__express_expressions_PartialEntityConstructor120

    @express_expressions_PartialEntityConstructor120.setter
    def express_expressions_PartialEntityConstructor120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_PartialEntityConstructor__express_expressions_PartialEntityConstructor120", None)
        self.__express_expressions_PartialEntityConstructor120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SingleEntityType121"):
                opp_val = getattr(old_value, "SingleEntityType121", None)
                if opp_val == self:
                    setattr(old_value, "SingleEntityType121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SingleEntityType121"):
                opp_val = getattr(value, "SingleEntityType121", None)
                setattr(value, "SingleEntityType121", self)

    @property
    def express_expressions_PartialEntityConstructor(self):
        return self.__express_expressions_PartialEntityConstructor

    @express_expressions_PartialEntityConstructor.setter
    def express_expressions_PartialEntityConstructor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_PartialEntityConstructor__express_expressions_PartialEntityConstructor", None)
        self.__express_expressions_PartialEntityConstructor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PartialEntityValue"):
                opp_val = getattr(old_value, "PartialEntityValue", None)
                if opp_val == self:
                    setattr(old_value, "PartialEntityValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PartialEntityValue"):
                opp_val = getattr(value, "PartialEntityValue", None)
                setattr(value, "PartialEntityValue", self)

    @property
    def express_expressions_PartialEntityConstructor123(self):
        return self.__express_expressions_PartialEntityConstructor123

    @express_expressions_PartialEntityConstructor123.setter
    def express_expressions_PartialEntityConstructor123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_expressions_PartialEntityConstructor__express_expressions_PartialEntityConstructor123", None)
        self.__express_expressions_PartialEntityConstructor123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeBinding"):
                    opp_val = getattr(item, "AttributeBinding", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeBinding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeBinding"):
                    opp_val = getattr(item, "AttributeBinding", None)
                    
                    setattr(item, "AttributeBinding", self)
                    

class express_expressions_Operation(Expression):

    pass
class Extent:

    pass
class express_rules_SubtypeConstraint:

    pass
class ActualParameter:

    pass
class Procedure:

    pass
class express_statements_ProcedureCall(Statement):

    pass
class EntityType:

    pass
class CommonElement:

    pass
class express_rules_SupertypeRule(CommonElement):

    def __init__(self, assertsAbstract: str, express_rules_SupertypeRule: "EntityType" = None, collection: set["SubtypeConstraint"] = None, CommonElement: "express_core_AlgorithmScope" = None):
        self.assertsAbstract = assertsAbstract
        self.express_rules_SupertypeRule = express_rules_SupertypeRule
        self.collection = collection if collection is not None else set()
        
        pass
    @property
    def assertsAbstract(self):
        return self.__assertsAbstract

    @assertsAbstract.setter
    def assertsAbstract(self, assertsAbstract: str):
        self.__assertsAbstract = assertsAbstract


    @property
    def express_rules_SupertypeRule(self):
        return self.__express_rules_SupertypeRule

    @express_rules_SupertypeRule.setter
    def express_rules_SupertypeRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_rules_SupertypeRule__express_rules_SupertypeRule", None)
        self.__express_rules_SupertypeRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityType"):
                opp_val = getattr(old_value, "EntityType", None)
                if opp_val == self:
                    setattr(old_value, "EntityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityType"):
                opp_val = getattr(value, "EntityType", None)
                setattr(value, "EntityType", self)

    @property
    def collection(self):
        return self.__collection

    @collection.setter
    def collection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_rules_SupertypeRule__collection", None)
        self.__collection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SubtypeConstraint"):
                    opp_val = getattr(item, "SubtypeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "SubtypeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SubtypeConstraint"):
                    opp_val = getattr(item, "SubtypeConstraint", None)
                    
                    setattr(item, "SubtypeConstraint", self)
                    

class SubtypeConstraint:

    pass
class express_rules_ANDConstraint(SubtypeConstraint):

    pass
class express_rules_TOTAL_OVERConstraint(SubtypeConstraint):

    pass
class LogicalValue:

    pass
class express_instances_BooleanValue(LogicalValue):

    pass
class express_instances_NumberValue(SimpleValue):

    pass
class NumberValue:

    pass
class express_instances_RealValue(NumberValue):

    pass
class express_instances_Population:

    pass
class express_rules_ONEOFConstraint(SubtypeConstraint):

    pass
class express_instances_ArrayMember:

    def __init__(self, index: str, express_instances_ArrayMember: "Instance" = None):
        self.index = index
        self.express_instances_ArrayMember = express_instances_ArrayMember
        
        pass
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index


    @property
    def express_instances_ArrayMember(self):
        return self.__express_instances_ArrayMember

    @express_instances_ArrayMember.setter
    def express_instances_ArrayMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_ArrayMember__express_instances_ArrayMember", None)
        self.__express_instances_ArrayMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instance511"):
                opp_val = getattr(old_value, "Instance511", None)
                if opp_val == self:
                    setattr(old_value, "Instance511", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instance511"):
                opp_val = getattr(value, "Instance511", None)
                setattr(value, "Instance511", self)

class instances_ConcreteValue:

    pass
class instances_TypedInstance:

    pass
class express_instances_EnumerationItem(instances_TypedInstance, instances_ConcreteValue, core_TypeElement):

    def __init__(self, position: str, declaredItems: "EnumerationType" = None):
        self.position = position
        self.declaredItems = declaredItems
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def declaredItems(self):
        return self.__declaredItems

    @declaredItems.setter
    def declaredItems(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_EnumerationItem__declaredItems", None)
        self.__declaredItems = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EnumerationType503"):
                opp_val = getattr(old_value, "EnumerationType503", None)
                if opp_val == self:
                    setattr(old_value, "EnumerationType503", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EnumerationType503"):
                opp_val = getattr(value, "EnumerationType503", None)
                setattr(value, "EnumerationType503", self)

class BagMember:

    pass
class express_instances_BinaryValue(SimpleValue):

    pass
class LISTValue:

    pass
class express_instances_GenericAggregate(LISTValue):

    pass
class express_instances_SingleLeafInstance(EntityInstance):

    pass
class express_instances_Indeterminate(Instance):

    pass
class express_instances_SingleEntityValue:

    pass
class express_instances_BagMember:

    def __init__(self, count: str, express_instances_BagMember: "Instance" = None):
        self.count = count
        self.express_instances_BagMember = express_instances_BagMember
        
        pass
    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count


    @property
    def express_instances_BagMember(self):
        return self.__express_instances_BagMember

    @express_instances_BagMember.setter
    def express_instances_BagMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_BagMember__express_instances_BagMember", None)
        self.__express_instances_BagMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instance489"):
                opp_val = getattr(old_value, "Instance489", None)
                if opp_val == self:
                    setattr(old_value, "Instance489", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instance489"):
                opp_val = getattr(value, "Instance489", None)
                setattr(value, "Instance489", self)

class express_instances_ListMember:

    def __init__(self, position: str, express_instances_ListMember: "Instance" = None):
        self.position = position
        self.express_instances_ListMember = express_instances_ListMember
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def express_instances_ListMember(self):
        return self.__express_instances_ListMember

    @express_instances_ListMember.setter
    def express_instances_ListMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_ListMember__express_instances_ListMember", None)
        self.__express_instances_ListMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Instance487"):
                opp_val = getattr(old_value, "Instance487", None)
                if opp_val == self:
                    setattr(old_value, "Instance487", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Instance487"):
                opp_val = getattr(value, "Instance487", None)
                setattr(value, "Instance487", self)

class express_instances_EntityValue(PartialEntityValue):

    pass
class EntityValue:

    pass
class TypedInstance:

    pass
class express_instances_SpecializedValue(TypedInstance):

    pass
class express_instances_EntityInstance(TypedInstance):

    def __init__(self, id: str, describes: "EntityValue" = None, express_instances_EntityInstance: set["EntityType"] = None):
        self.id = id
        self.describes = describes
        self.express_instances_EntityInstance = express_instances_EntityInstance if express_instances_EntityInstance is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def express_instances_EntityInstance(self):
        return self.__express_instances_EntityInstance

    @express_instances_EntityInstance.setter
    def express_instances_EntityInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_EntityInstance__express_instances_EntityInstance", None)
        self.__express_instances_EntityInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EntityType475"):
                    opp_val = getattr(item, "EntityType475", None)
                    
                    if opp_val == self:
                        setattr(item, "EntityType475", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EntityType475"):
                    opp_val = getattr(item, "EntityType475", None)
                    
                    setattr(item, "EntityType475", self)
                    

    @property
    def describes(self):
        return self.__describes

    @describes.setter
    def describes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_instances_EntityInstance__describes", None)
        self.__describes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityValue"):
                opp_val = getattr(old_value, "EntityValue", None)
                if opp_val == self:
                    setattr(old_value, "EntityValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityValue"):
                opp_val = getattr(value, "EntityValue", None)
                setattr(value, "EntityValue", self)

class StringValue:

    pass
class express_instances_TypeName(StringValue):

    pass
class express_instances_RoleName(StringValue):

    pass
class ArrayMember:

    pass
class AggregateValue:

    pass
class express_instances_SETValue(AggregateValue):

    pass
class express_instances_BAGValue(AggregateValue):

    pass
class express_instances_ARRAYValue(AggregateValue):

    pass
class express_instances_AttributeValue:

    pass
class core_GenericType:

    pass
class algorithms_Parameter:

    pass
class express_algorithms_VARParameter(algorithms_Parameter, algorithms_VARVariable):

    pass
class express_algorithms_GenericElement(LocalElement):

    pass
class express_algorithms_Variable(NamedVariable):

    pass
class express_instances_TypedInstance(Instance):

    pass
class express_instances_LogicalValue(SimpleValue):

    pass
class express_instances_Constant(CommonElement):

    pass
class ConcreteValue:

    pass
class express_instances_SimpleValue(ConcreteValue):

    def __init__(self, name: str, ConcreteValue: "express_instances_SpecializedValue" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class express_instances_AggregateValue(ConcreteValue):

    pass
class RealValue:

    pass
class express_instances_IntegerValue(RealValue):

    pass
class AGGREGATEType:

    pass
class express_algorithms_ActualStructureConstraint:

    def __init__(self, label: str, express_algorithms_ActualStructureConstraint: "ActualStructure" = None, constraint449: "AGGREGATEType" = None):
        self.label = label
        self.express_algorithms_ActualStructureConstraint = express_algorithms_ActualStructureConstraint
        self.constraint449 = constraint449
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def constraint449(self):
        return self.__constraint449

    @constraint449.setter
    def constraint449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualStructureConstraint__constraint449", None)
        self.__constraint449 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AGGREGATEType"):
                opp_val = getattr(old_value, "AGGREGATEType", None)
                if opp_val == self:
                    setattr(old_value, "AGGREGATEType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AGGREGATEType"):
                opp_val = getattr(value, "AGGREGATEType", None)
                setattr(value, "AGGREGATEType", self)

    @property
    def express_algorithms_ActualStructureConstraint(self):
        return self.__express_algorithms_ActualStructureConstraint

    @express_algorithms_ActualStructureConstraint.setter
    def express_algorithms_ActualStructureConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualStructureConstraint__express_algorithms_ActualStructureConstraint", None)
        self.__express_algorithms_ActualStructureConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActualStructure451"):
                opp_val = getattr(old_value, "ActualStructure451", None)
                if opp_val == self:
                    setattr(old_value, "ActualStructure451", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActualStructure451"):
                opp_val = getattr(value, "ActualStructure451", None)
                setattr(value, "ActualStructure451", self)

class express_algorithms_Parameter(LocalElement):

    def __init__(self, inout: str, position: str, express_algorithms_Parameter: set["ActualStructureConstraint"] = None, express_algorithms_Parameter443: set["ActualTypeConstraint"] = None, express_algorithms_Parameter446: "ParameterType" = None, LocalElement: "express_core_LocalScope" = None):
        self.inout = inout
        self.position = position
        self.express_algorithms_Parameter = express_algorithms_Parameter if express_algorithms_Parameter is not None else set()
        self.express_algorithms_Parameter443 = express_algorithms_Parameter443 if express_algorithms_Parameter443 is not None else set()
        self.express_algorithms_Parameter446 = express_algorithms_Parameter446
        
        pass
    @property
    def inout(self):
        return self.__inout

    @inout.setter
    def inout(self, inout: str):
        self.__inout = inout


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def express_algorithms_Parameter443(self):
        return self.__express_algorithms_Parameter443

    @express_algorithms_Parameter443.setter
    def express_algorithms_Parameter443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Parameter__express_algorithms_Parameter443", None)
        self.__express_algorithms_Parameter443 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActualTypeConstraint444"):
                    opp_val = getattr(item, "ActualTypeConstraint444", None)
                    
                    if opp_val == self:
                        setattr(item, "ActualTypeConstraint444", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActualTypeConstraint444"):
                    opp_val = getattr(item, "ActualTypeConstraint444", None)
                    
                    setattr(item, "ActualTypeConstraint444", self)
                    

    @property
    def express_algorithms_Parameter446(self):
        return self.__express_algorithms_Parameter446

    @express_algorithms_Parameter446.setter
    def express_algorithms_Parameter446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Parameter__express_algorithms_Parameter446", None)
        self.__express_algorithms_Parameter446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ParameterType447"):
                opp_val = getattr(old_value, "ParameterType447", None)
                if opp_val == self:
                    setattr(old_value, "ParameterType447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ParameterType447"):
                opp_val = getattr(value, "ParameterType447", None)
                setattr(value, "ParameterType447", self)

    @property
    def express_algorithms_Parameter(self):
        return self.__express_algorithms_Parameter

    @express_algorithms_Parameter.setter
    def express_algorithms_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Parameter__express_algorithms_Parameter", None)
        self.__express_algorithms_Parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActualStructureConstraint441"):
                    opp_val = getattr(item, "ActualStructureConstraint441", None)
                    
                    if opp_val == self:
                        setattr(item, "ActualStructureConstraint441", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActualStructureConstraint441"):
                    opp_val = getattr(item, "ActualStructureConstraint441", None)
                    
                    setattr(item, "ActualStructureConstraint441", self)
                    

class ActualStructure:

    pass
class express_algorithms_VARVariable(ABC):

    pass
class core_ActualType:

    pass
class express_algorithms_ActualAggregationType(core_ActualType, core_AggregationType):

    pass
class express_algorithms_Algorithm(core_AlgorithmScope, core_CommonElement):

    pass
class EscapeStatement:

    pass
class SkipStatement:

    pass
class StatementBlock:

    pass
class express_algorithms_Statement:

    def __init__(self, text: str, body: "RepeatStatement" = None, body420: "Algorithm" = None, bodyStatements_Statement: "StatementBlock" = None, express_algorithms_Statement: set["SkipStatement"] = None, express_algorithms_Statement417: set["EscapeStatement"] = None):
        self.text = text
        self.body = body
        self.body420 = body420
        self.bodyStatements_Statement = bodyStatements_Statement
        self.express_algorithms_Statement = express_algorithms_Statement if express_algorithms_Statement is not None else set()
        self.express_algorithms_Statement417 = express_algorithms_Statement417 if express_algorithms_Statement417 is not None else set()
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def express_algorithms_Statement(self):
        return self.__express_algorithms_Statement

    @express_algorithms_Statement.setter
    def express_algorithms_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Statement__express_algorithms_Statement", None)
        self.__express_algorithms_Statement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SkipStatement"):
                    opp_val = getattr(item, "SkipStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "SkipStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SkipStatement"):
                    opp_val = getattr(item, "SkipStatement", None)
                    
                    setattr(item, "SkipStatement", self)
                    

    @property
    def body420(self):
        return self.__body420

    @body420.setter
    def body420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Statement__body420", None)
        self.__body420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Algorithm421"):
                opp_val = getattr(old_value, "Algorithm421", None)
                if opp_val == self:
                    setattr(old_value, "Algorithm421", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Algorithm421"):
                opp_val = getattr(value, "Algorithm421", None)
                setattr(value, "Algorithm421", self)

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Statement__body", None)
        self.__body = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepeatStatement"):
                opp_val = getattr(old_value, "RepeatStatement", None)
                if opp_val == self:
                    setattr(old_value, "RepeatStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepeatStatement"):
                opp_val = getattr(value, "RepeatStatement", None)
                setattr(value, "RepeatStatement", self)

    @property
    def express_algorithms_Statement417(self):
        return self.__express_algorithms_Statement417

    @express_algorithms_Statement417.setter
    def express_algorithms_Statement417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Statement__express_algorithms_Statement417", None)
        self.__express_algorithms_Statement417 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EscapeStatement"):
                    opp_val = getattr(item, "EscapeStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "EscapeStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EscapeStatement"):
                    opp_val = getattr(item, "EscapeStatement", None)
                    
                    setattr(item, "EscapeStatement", self)
                    

    @property
    def bodyStatements_Statement(self):
        return self.__bodyStatements_Statement

    @bodyStatements_Statement.setter
    def bodyStatements_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_Statement__bodyStatements_Statement", None)
        self.__bodyStatements_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StatementBlock"):
                opp_val = getattr(old_value, "StatementBlock", None)
                if opp_val == self:
                    setattr(old_value, "StatementBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StatementBlock"):
                opp_val = getattr(value, "StatementBlock", None)
                setattr(value, "StatementBlock", self)

class ActualType:

    pass
class express_algorithms_ActualAGGREGATEType(ActualType):

    def __init__(self, label: str, express_algorithms_ActualAGGREGATEType: "SizeConstraint" = None, express_algorithms_ActualAGGREGATEType433: "ActualStructure" = None, express_algorithms_ActualAGGREGATEType435: "VariableType" = None, express_algorithms_ActualAGGREGATEType438: "SizeConstraint" = None, ActualType: "express_algorithms_ActualAggregationType" = None):
        self.label = label
        self.express_algorithms_ActualAGGREGATEType = express_algorithms_ActualAGGREGATEType
        self.express_algorithms_ActualAGGREGATEType433 = express_algorithms_ActualAGGREGATEType433
        self.express_algorithms_ActualAGGREGATEType435 = express_algorithms_ActualAGGREGATEType435
        self.express_algorithms_ActualAGGREGATEType438 = express_algorithms_ActualAGGREGATEType438
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def express_algorithms_ActualAGGREGATEType438(self):
        return self.__express_algorithms_ActualAGGREGATEType438

    @express_algorithms_ActualAGGREGATEType438.setter
    def express_algorithms_ActualAGGREGATEType438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualAGGREGATEType__express_algorithms_ActualAGGREGATEType438", None)
        self.__express_algorithms_ActualAGGREGATEType438 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint439"):
                opp_val = getattr(old_value, "SizeConstraint439", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint439", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint439"):
                opp_val = getattr(value, "SizeConstraint439", None)
                setattr(value, "SizeConstraint439", self)

    @property
    def express_algorithms_ActualAGGREGATEType433(self):
        return self.__express_algorithms_ActualAGGREGATEType433

    @express_algorithms_ActualAGGREGATEType433.setter
    def express_algorithms_ActualAGGREGATEType433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualAGGREGATEType__express_algorithms_ActualAGGREGATEType433", None)
        self.__express_algorithms_ActualAGGREGATEType433 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActualStructure"):
                opp_val = getattr(old_value, "ActualStructure", None)
                if opp_val == self:
                    setattr(old_value, "ActualStructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActualStructure"):
                opp_val = getattr(value, "ActualStructure", None)
                setattr(value, "ActualStructure", self)

    @property
    def express_algorithms_ActualAGGREGATEType435(self):
        return self.__express_algorithms_ActualAGGREGATEType435

    @express_algorithms_ActualAGGREGATEType435.setter
    def express_algorithms_ActualAGGREGATEType435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualAGGREGATEType__express_algorithms_ActualAGGREGATEType435", None)
        self.__express_algorithms_ActualAGGREGATEType435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableType436"):
                opp_val = getattr(old_value, "VariableType436", None)
                if opp_val == self:
                    setattr(old_value, "VariableType436", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableType436"):
                opp_val = getattr(value, "VariableType436", None)
                setattr(value, "VariableType436", self)

    @property
    def express_algorithms_ActualAGGREGATEType(self):
        return self.__express_algorithms_ActualAGGREGATEType

    @express_algorithms_ActualAGGREGATEType.setter
    def express_algorithms_ActualAGGREGATEType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualAGGREGATEType__express_algorithms_ActualAGGREGATEType", None)
        self.__express_algorithms_ActualAGGREGATEType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SizeConstraint431"):
                opp_val = getattr(old_value, "SizeConstraint431", None)
                if opp_val == self:
                    setattr(old_value, "SizeConstraint431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SizeConstraint431"):
                opp_val = getattr(value, "SizeConstraint431", None)
                setattr(value, "SizeConstraint431", self)

class express_algorithms_ActualGenericType(ActualType):

    def __init__(self, isEntity: str, label: str, express_algorithms_ActualGenericType: "ActualDataType" = None, ActualType: "express_algorithms_ActualAggregationType" = None):
        self.isEntity = isEntity
        self.label = label
        self.express_algorithms_ActualGenericType = express_algorithms_ActualGenericType
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def isEntity(self):
        return self.__isEntity

    @isEntity.setter
    def isEntity(self, isEntity: str):
        self.__isEntity = isEntity


    @property
    def express_algorithms_ActualGenericType(self):
        return self.__express_algorithms_ActualGenericType

    @express_algorithms_ActualGenericType.setter
    def express_algorithms_ActualGenericType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualGenericType__express_algorithms_ActualGenericType", None)
        self.__express_algorithms_ActualGenericType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActualDataType413"):
                opp_val = getattr(old_value, "ActualDataType413", None)
                if opp_val == self:
                    setattr(old_value, "ActualDataType413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActualDataType413"):
                opp_val = getattr(value, "ActualDataType413", None)
                setattr(value, "ActualDataType413", self)

class core_AGGREGATEType:

    pass
class algorithms_GenericElement:

    pass
class express_algorithms_ActualDataType(algorithms_GenericElement, core_GenericType):

    pass
class express_algorithms_ActualStructure(algorithms_GenericElement, core_AGGREGATEType):

    pass
class express_algorithms_LocalVariable(Variable):

    pass
class InVariable:

    pass
class express_algorithms_InParameter(Parameter):

    pass
class express_algorithms_FunctionResult(Variable):

    pass
class ActualDataType:

    pass
class GenericType:

    pass
class ActualAggregationType:

    pass
class express_algorithms_ActualSETType(ActualAggregationType):

    pass
class express_algorithms_ActualBAGType(ActualAggregationType):

    pass
class express_algorithms_ActualLISTType(ActualAggregationType):

    pass
class express_algorithms_ActualARRAYType(ActualAggregationType):

    def __init__(self, isOptional: str, express_algorithms_ActualARRAYType: "ArrayBound" = None, express_algorithms_ActualARRAYType428: "ArrayBound" = None):
        self.isOptional = isOptional
        self.express_algorithms_ActualARRAYType = express_algorithms_ActualARRAYType
        self.express_algorithms_ActualARRAYType428 = express_algorithms_ActualARRAYType428
        
        pass
    @property
    def isOptional(self):
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional


    @property
    def express_algorithms_ActualARRAYType(self):
        return self.__express_algorithms_ActualARRAYType

    @express_algorithms_ActualARRAYType.setter
    def express_algorithms_ActualARRAYType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualARRAYType__express_algorithms_ActualARRAYType", None)
        self.__express_algorithms_ActualARRAYType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound426"):
                opp_val = getattr(old_value, "ArrayBound426", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound426", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound426"):
                opp_val = getattr(value, "ArrayBound426", None)
                setattr(value, "ArrayBound426", self)

    @property
    def express_algorithms_ActualARRAYType428(self):
        return self.__express_algorithms_ActualARRAYType428

    @express_algorithms_ActualARRAYType428.setter
    def express_algorithms_ActualARRAYType428(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualARRAYType__express_algorithms_ActualARRAYType428", None)
        self.__express_algorithms_ActualARRAYType428 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArrayBound429"):
                opp_val = getattr(old_value, "ArrayBound429", None)
                if opp_val == self:
                    setattr(old_value, "ArrayBound429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArrayBound429"):
                opp_val = getattr(value, "ArrayBound429", None)
                setattr(value, "ArrayBound429", self)

class InParameter:

    pass
class express_algorithms_InVariable(Variable):

    pass
class express_algorithms_NamedVariable(LocalElement):

    pass
class RepeatStatement:

    pass
class core_AnonymousType:

    pass
class express_core_ConcreteAggregationType(core_AnonymousType, core_AggregationType):

    pass
class express_core_SchemaElement(NamedElement):

    pass
class AlgorithmScope:

    pass
class express_core_CommonElement(SchemaElement):

    pass
class express_core_SimpleType(AnonymousType):

    def __init__(self, id: str, AnonymousType: "express_core_AnonymousType" = None):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class express_core_ExplicitAttribute(Attribute):

    def __init__(self, isOptional: str, Attribute241: "express_core_EntityType" = None, Attribute148: "express_expressions_UsedInRef" = None, Attribute285: "express_core_UniqueRule" = None, Attribute321: "express_core_AttributeType" = None, Attribute469: "express_instances_RoleName" = None, Attribute180: "express_core_SingleEntityType" = None, Attribute229: "express_core_Redeclaration" = None, Attribute: "express_expressions_AttributeRef" = None):
        self.isOptional = isOptional
        
        pass
    @property
    def isOptional(self):
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: str):
        self.__isOptional = isOptional


class Algorithm:

    pass
class express_algorithms_Function(Algorithm):

    pass
class express_algorithms_Procedure(Algorithm):

    pass
class express_core_ActualType(VariableType):

    pass
class express_algorithms_ActualTypeConstraint:

    def __init__(self, label: str, constraint: "GenericType" = None, express_algorithms_ActualTypeConstraint: "ActualDataType" = None):
        self.label = label
        self.constraint = constraint
        self.express_algorithms_ActualTypeConstraint = express_algorithms_ActualTypeConstraint
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def constraint(self):
        return self.__constraint

    @constraint.setter
    def constraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualTypeConstraint__constraint", None)
        self.__constraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GenericType"):
                opp_val = getattr(old_value, "GenericType", None)
                if opp_val == self:
                    setattr(old_value, "GenericType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GenericType"):
                opp_val = getattr(value, "GenericType", None)
                setattr(value, "GenericType", self)

    @property
    def express_algorithms_ActualTypeConstraint(self):
        return self.__express_algorithms_ActualTypeConstraint

    @express_algorithms_ActualTypeConstraint.setter
    def express_algorithms_ActualTypeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_express_algorithms_ActualTypeConstraint__express_algorithms_ActualTypeConstraint", None)
        self.__express_algorithms_ActualTypeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActualDataType"):
                opp_val = getattr(old_value, "ActualDataType", None)
                if opp_val == self:
                    setattr(old_value, "ActualDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActualDataType"):
                opp_val = getattr(value, "ActualDataType", None)
                setattr(value, "ActualDataType", self)
