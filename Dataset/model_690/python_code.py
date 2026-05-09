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
class DirectionKind(Enum):
    in_ = "in_"
    inout = "inout"
    out = "out"
class CollectionKind(Enum):
    OrderedSet = "OrderedSet"
    Set = "Set"
    Bag = "Bag"
    Sequence = "Sequence"
class ImportKind(Enum):
    extension = "extension"
    access = "access"
class EnforcementMode(Enum):
    Deletion = "Deletion"
    Creation = "Creation"


############################################
# Definition of Classes
############################################

class TupleLiteralExp:

    pass
class essentialocl_OpaqueExpression:

    pass
class OpaqueExpression:

    pass
class essentialocl_ExpressionInOcl(OpaqueExpression):

    pass
class TupleLiteralPart:

    pass
class CollectionLiteralExp:

    pass
class CollectionLiteralPart:

    pass
class essentialocl_CollectionRange(CollectionLiteralPart):

    pass
class essentialocl_CollectionItem(CollectionLiteralPart):

    pass
class FeaturePropertyCall:

    pass
class essentialocl_OperationCallExp(FeaturePropertyCall):

    pass
class essentialocl_PropertyCallExp(FeaturePropertyCall):

    pass
class ComputeExp:

    pass
class LetExp:

    pass
class PrimitiveLiteralExp:

    pass
class essentialocl_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class essentialocl_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class essentialocl_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class NumericLiteralExp:

    pass
class essentialocl_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


class essentialocl_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


class essentialocl_UnlimitedNaturalExp(NumericLiteralExp):

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
class RelationalTransformation:

    pass
class DomainPattern:

    pass
class RelationImplementation:

    pass
class Key:

    pass
class Predicate:

    pass
class qvtcore_EnforcementOperation:

    def __init__(self, enforcementMode: str, enforcementOperation: "BottomPattern" = None, qvtcore_EnforcementOperation: "OperationCallExp" = None):
        self.enforcementMode = enforcementMode
        self.enforcementOperation = enforcementOperation
        self.qvtcore_EnforcementOperation = qvtcore_EnforcementOperation
        
        pass
    @property
    def enforcementMode(self):
        return self.__enforcementMode

    @enforcementMode.setter
    def enforcementMode(self, enforcementMode: str):
        self.__enforcementMode = enforcementMode


    @property
    def qvtcore_EnforcementOperation(self):
        return self.__qvtcore_EnforcementOperation

    @qvtcore_EnforcementOperation.setter
    def qvtcore_EnforcementOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_EnforcementOperation__qvtcore_EnforcementOperation", None)
        self.__qvtcore_EnforcementOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationCallExp"):
                opp_val = getattr(old_value, "OperationCallExp", None)
                if opp_val == self:
                    setattr(old_value, "OperationCallExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationCallExp"):
                opp_val = getattr(value, "OperationCallExp", None)
                setattr(value, "OperationCallExp", self)

    @property
    def enforcementOperation(self):
        return self.__enforcementOperation

    @enforcementOperation.setter
    def enforcementOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_EnforcementOperation__enforcementOperation", None)
        self.__enforcementOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottomPattern253"):
                opp_val = getattr(old_value, "BottomPattern253", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern253"):
                opp_val = getattr(value, "BottomPattern253", None)
                setattr(value, "BottomPattern253", self)

class TypedModel:

    pass
class qvtcore_Assignment:

    def __init__(self, isDefault: str, qvtcore_Assignment233: "OclExpression" = None, qvtcore_Assignment236: "Property" = None, assignment: "BottomPattern" = None, qvtcore_Assignment: "OclExpression" = None):
        self.isDefault = isDefault
        self.qvtcore_Assignment233 = qvtcore_Assignment233
        self.qvtcore_Assignment236 = qvtcore_Assignment236
        self.assignment = assignment
        self.qvtcore_Assignment = qvtcore_Assignment
        
        pass
    @property
    def isDefault(self):
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: str):
        self.__isDefault = isDefault


    @property
    def qvtcore_Assignment(self):
        return self.__qvtcore_Assignment

    @qvtcore_Assignment.setter
    def qvtcore_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_Assignment__qvtcore_Assignment", None)
        self.__qvtcore_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression231"):
                opp_val = getattr(old_value, "OclExpression231", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression231"):
                opp_val = getattr(value, "OclExpression231", None)
                setattr(value, "OclExpression231", self)

    @property
    def assignment(self):
        return self.__assignment

    @assignment.setter
    def assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_Assignment__assignment", None)
        self.__assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottomPattern229"):
                opp_val = getattr(old_value, "BottomPattern229", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern229"):
                opp_val = getattr(value, "BottomPattern229", None)
                setattr(value, "BottomPattern229", self)

    @property
    def qvtcore_Assignment233(self):
        return self.__qvtcore_Assignment233

    @qvtcore_Assignment233.setter
    def qvtcore_Assignment233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_Assignment__qvtcore_Assignment233", None)
        self.__qvtcore_Assignment233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression234"):
                opp_val = getattr(old_value, "OclExpression234", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression234"):
                opp_val = getattr(value, "OclExpression234", None)
                setattr(value, "OclExpression234", self)

    @property
    def qvtcore_Assignment236(self):
        return self.__qvtcore_Assignment236

    @qvtcore_Assignment236.setter
    def qvtcore_Assignment236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_Assignment__qvtcore_Assignment236", None)
        self.__qvtcore_Assignment236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property237"):
                opp_val = getattr(old_value, "Property237", None)
                if opp_val == self:
                    setattr(old_value, "Property237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property237"):
                opp_val = getattr(value, "Property237", None)
                setattr(value, "Property237", self)

class BottomPattern:

    pass
class Pattern:

    pass
class qvtrelation_DomainPattern(Pattern):

    pass
class qvtcore_CorePattern(Pattern):

    pass
class Domain:

    pass
class qvtrelation_RelationDomain(Domain):

    pass
class Mapping:

    pass
class Rule:

    pass
class qvtrelation_Relation(Rule):

    def __init__(self, isTopLevel: str, qvtrelation_Relation: set["Variable"] = None, whereOwner: "Pattern" = None, relation: set["RelationImplementation"] = None, whenOwner: "Pattern" = None, Rule: "qvtbase_Domain" = None, Rule279: "qvtbase_Rule" = None, Rule264: "qvtbase_Transformation" = None):
        self.isTopLevel = isTopLevel
        self.qvtrelation_Relation = qvtrelation_Relation if qvtrelation_Relation is not None else set()
        self.whereOwner = whereOwner
        self.relation = relation if relation is not None else set()
        self.whenOwner = whenOwner
        
        pass
    @property
    def isTopLevel(self):
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: str):
        self.__isTopLevel = isTopLevel


    @property
    def relation(self):
        return self.__relation

    @relation.setter
    def relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_Relation__relation", None)
        self.__relation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelationImplementation"):
                    opp_val = getattr(item, "RelationImplementation", None)
                    
                    if opp_val == self:
                        setattr(item, "RelationImplementation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelationImplementation"):
                    opp_val = getattr(item, "RelationImplementation", None)
                    
                    setattr(item, "RelationImplementation", self)
                    

    @property
    def whenOwner(self):
        return self.__whenOwner

    @whenOwner.setter
    def whenOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_Relation__whenOwner", None)
        self.__whenOwner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern298"):
                opp_val = getattr(old_value, "Pattern298", None)
                if opp_val == self:
                    setattr(old_value, "Pattern298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern298"):
                opp_val = getattr(value, "Pattern298", None)
                setattr(value, "Pattern298", self)

    @property
    def qvtrelation_Relation(self):
        return self.__qvtrelation_Relation

    @qvtrelation_Relation.setter
    def qvtrelation_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_Relation__qvtrelation_Relation", None)
        self.__qvtrelation_Relation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable295"):
                    opp_val = getattr(item, "Variable295", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable295"):
                    opp_val = getattr(item, "Variable295", None)
                    
                    setattr(item, "Variable295", self)
                    

    @property
    def whereOwner(self):
        return self.__whereOwner

    @whereOwner.setter
    def whereOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_Relation__whereOwner", None)
        self.__whereOwner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern300"):
                opp_val = getattr(old_value, "Pattern300", None)
                if opp_val == self:
                    setattr(old_value, "Pattern300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern300"):
                opp_val = getattr(value, "Pattern300", None)
                setattr(value, "Pattern300", self)

class EnforcementOperation:

    pass
class RealizedVariable:

    pass
class Assignment:

    pass
class Area:

    pass
class qvtcore_CoreDomain(Domain, Area):

    pass
class qvtcore_Mapping(Area, Rule):

    pass
class CorePattern:

    pass
class qvtcore_GuardPattern(CorePattern):

    pass
class qvtcore_BottomPattern(CorePattern):

    pass
class GuardPattern:

    pass
class qvtcore_Area(ABC):

    pass
class ConstructorBody:

    pass
class InstantiationExp:

    pass
class qvtoperational_ObjectExp(InstantiationExp):

    pass
class OperationCallExp:

    pass
class qvtoperational_ImperativeCallExp(OperationCallExp):

    def __init__(self, isVirtual: str, OperationCallExp: "qvtcore_EnforcementOperation" = None):
        self.isVirtual = isVirtual
        
        pass
    @property
    def isVirtual(self):
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: str):
        self.__isVirtual = isVirtual


class ModelType:

    pass
class ModuleImport:

    pass
class URIExtent:

    pass
class EntryOperation:

    pass
class ModelParameter:

    pass
class ImperativeCallExp:

    pass
class qvtoperational_MappingCallExp(ImperativeCallExp):

    def __init__(self, isStrict: str):
        self.isStrict = isStrict
        
        pass
    @property
    def isStrict(self):
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict


class RelationDomain:

    pass
class VarParameter:

    pass
class qvtoperational_ModelParameter(VarParameter):

    pass
class qvtoperational_MappingParameter(VarParameter):

    pass
class Relation:

    pass
class MappingOperation:

    pass
class ResolveExp:

    pass
class qvtoperational_ResolveInExp(ResolveExp):

    pass
class ImperativeOperation:

    pass
class qvtoperational_Constructor(ImperativeOperation):

    pass
class qvtoperational_EntryOperation(ImperativeOperation):

    pass
class qvtoperational_Helper(ImperativeOperation):

    def __init__(self, isQuery: str, ImperativeOperation218: "qvtoperational_OperationBody" = None, ImperativeOperation: "qvtoperational_ImperativeOperation" = None, ImperativeOperation216: "qvtoperational_VarParameter" = None, ImperativeOperation214: "qvtoperational_VarParameter" = None):
        self.isQuery = isQuery
        
        pass
    @property
    def isQuery(self):
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery


class OperationBody:

    pass
class qvtoperational_ConstructorBody(OperationBody):

    pass
class qvtoperational_MappingBody(OperationBody):

    pass
class Extent:

    pass
class emof_URIExtent(Extent):

    pass
class Parameter:

    pass
class Enumeration:

    pass
class Package:

    pass
class NamedElement:

    pass
class emof_TypedElement(NamedElement):

    pass
class qvtbase_Domain(NamedElement):

    def __init__(self, isCheckable: str, isEnforceable: str, domain: "Rule" = None, qvtbase_Domain: "TypedModel" = None, NamedElement: "emof_Comment" = None):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.domain = domain
        self.qvtbase_Domain = qvtbase_Domain
        
        pass
    @property
    def isCheckable(self):
        return self.__isCheckable

    @isCheckable.setter
    def isCheckable(self, isCheckable: str):
        self.__isCheckable = isCheckable


    @property
    def isEnforceable(self):
        return self.__isEnforceable

    @isEnforceable.setter
    def isEnforceable(self, isEnforceable: str):
        self.__isEnforceable = isEnforceable


    @property
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtbase_Domain__domain", None)
        self.__domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rule"):
                opp_val = getattr(old_value, "Rule", None)
                if opp_val == self:
                    setattr(old_value, "Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rule"):
                opp_val = getattr(value, "Rule", None)
                setattr(value, "Rule", self)

    @property
    def qvtbase_Domain(self):
        return self.__qvtbase_Domain

    @qvtbase_Domain.setter
    def qvtbase_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtbase_Domain__qvtbase_Domain", None)
        self.__qvtbase_Domain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypedModel"):
                opp_val = getattr(old_value, "TypedModel", None)
                if opp_val == self:
                    setattr(old_value, "TypedModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypedModel"):
                opp_val = getattr(value, "TypedModel", None)
                setattr(value, "TypedModel", self)

class qvtbase_TypedModel(NamedElement):

    pass
class emof_Type(NamedElement):

    pass
class emof_EnumerationLiteral(NamedElement):

    pass
class qvtbase_Rule(NamedElement):

    pass
class emof_Package(NamedElement):

    def __init__(self, uri: str, package: set["Type"] = None, emof_Package: set["Package"] = None, NamedElement: "emof_Comment" = None):
        self.uri = uri
        self.package = package if package is not None else set()
        self.emof_Package = emof_Package if emof_Package is not None else set()
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Package__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type126"):
                    opp_val = getattr(item, "Type126", None)
                    
                    if opp_val == self:
                        setattr(item, "Type126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type126"):
                    opp_val = getattr(item, "Type126", None)
                    
                    setattr(item, "Type126", self)
                    

    @property
    def emof_Package(self):
        return self.__emof_Package

    @emof_Package.setter
    def emof_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Package__emof_Package", None)
        self.__emof_Package = value if value is not None else set()
        
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
                    

class emof_MultiplicityElement(ABC):

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
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


class TypedElement:

    pass
class essentialocl_CollectionLiteralPart(TypedElement):

    pass
class essentialocl_Variable(TypedElement):

    pass
class essentialocl_OclExpression(TypedElement):

    pass
class essentialocl_TupleLiteralPart(TypedElement):

    pass
class MultiplicityElement:

    pass
class emof_Property(TypedElement, MultiplicityElement):

    def __init__(self, isReadOnly: str, isDerived: str, isComposite: str, isId: str, default: str, emof_Property: "Class" = None, emof_Property136: "Property" = None, configProperty: "Module" = None):
        self.isReadOnly = isReadOnly
        self.isDerived = isDerived
        self.isComposite = isComposite
        self.isId = isId
        self.default = default
        self.emof_Property = emof_Property
        self.emof_Property136 = emof_Property136
        self.configProperty = configProperty
        
        pass
    @property
    def isDerived(self):
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
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
    def isId(self, isId: str):
        self.__isId = isId


    @property
    def isComposite(self):
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


    @property
    def emof_Property(self):
        return self.__emof_Property

    @emof_Property.setter
    def emof_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Property__emof_Property", None)
        self.__emof_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class134"):
                opp_val = getattr(old_value, "Class134", None)
                if opp_val == self:
                    setattr(old_value, "Class134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class134"):
                opp_val = getattr(value, "Class134", None)
                setattr(value, "Class134", self)

    @property
    def configProperty(self):
        return self.__configProperty

    @configProperty.setter
    def configProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Property__configProperty", None)
        self.__configProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module139"):
                opp_val = getattr(old_value, "Module139", None)
                if opp_val == self:
                    setattr(old_value, "Module139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module139"):
                opp_val = getattr(value, "Module139", None)
                setattr(value, "Module139", self)

    @property
    def emof_Property136(self):
        return self.__emof_Property136

    @emof_Property136.setter
    def emof_Property136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Property__emof_Property136", None)
        self.__emof_Property136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property137"):
                opp_val = getattr(old_value, "Property137", None)
                if opp_val == self:
                    setattr(old_value, "Property137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property137"):
                opp_val = getattr(value, "Property137", None)
                setattr(value, "Property137", self)

class emof_Parameter(TypedElement, MultiplicityElement):

    pass
class emof_Operation(TypedElement, MultiplicityElement):

    pass
class emof_Object:

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class emof_PrimitiveType(DataType):

    pass
class essentialocl_CollectionType(DataType):

    pass
class emof_Enumeration(DataType):

    pass
class Module:

    pass
class qvtoperational_Library(Module):

    pass
class qvtoperational_OperationalTransformation(Module):

    pass
class Transformation:

    pass
class qvtrelation_RelationalTransformation(Transformation):

    pass
class Comment:

    pass
class Tag:

    pass
class Object:

    pass
class emof_Extent(Object):

    pass
class emof_Element(Object):

    pass
class Operation:

    pass
class qvtoperational_MappingOperation(Operation, NamedElement, ImperativeOperation):

    pass
class qvtbase_Function(Operation):

    pass
class qvtoperational_ImperativeOperation(Operation):

    def __init__(self, isBlackbox: str, resOwner: set["VarParameter"] = None, qvtoperational_ImperativeOperation: "ImperativeOperation" = None, operation193: "OperationBody" = None, ctxOwner: "VarParameter" = None, Operation309: "qvtrelation_RelationImplementation" = None, Operation: "emof_Class" = None, Operation357: "essentialocl_OperationCallExp" = None, Operation131: "emof_Parameter" = None):
        self.isBlackbox = isBlackbox
        self.resOwner = resOwner if resOwner is not None else set()
        self.qvtoperational_ImperativeOperation = qvtoperational_ImperativeOperation
        self.operation193 = operation193
        self.ctxOwner = ctxOwner
        
        pass
    @property
    def isBlackbox(self):
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox


    @property
    def ctxOwner(self):
        return self.__ctxOwner

    @ctxOwner.setter
    def ctxOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__ctxOwner", None)
        self.__ctxOwner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VarParameter"):
                opp_val = getattr(old_value, "VarParameter", None)
                if opp_val == self:
                    setattr(old_value, "VarParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VarParameter"):
                opp_val = getattr(value, "VarParameter", None)
                setattr(value, "VarParameter", self)

    @property
    def resOwner(self):
        return self.__resOwner

    @resOwner.setter
    def resOwner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__resOwner", None)
        self.__resOwner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarParameter190"):
                    opp_val = getattr(item, "VarParameter190", None)
                    
                    if opp_val == self:
                        setattr(item, "VarParameter190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarParameter190"):
                    opp_val = getattr(item, "VarParameter190", None)
                    
                    setattr(item, "VarParameter190", self)
                    

    @property
    def qvtoperational_ImperativeOperation(self):
        return self.__qvtoperational_ImperativeOperation

    @qvtoperational_ImperativeOperation.setter
    def qvtoperational_ImperativeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__qvtoperational_ImperativeOperation", None)
        self.__qvtoperational_ImperativeOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation"):
                opp_val = getattr(old_value, "ImperativeOperation", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation"):
                opp_val = getattr(value, "ImperativeOperation", None)
                setattr(value, "ImperativeOperation", self)

    @property
    def operation193(self):
        return self.__operation193

    @operation193.setter
    def operation193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__operation193", None)
        self.__operation193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OperationBody"):
                opp_val = getattr(old_value, "OperationBody", None)
                if opp_val == self:
                    setattr(old_value, "OperationBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationBody"):
                opp_val = getattr(value, "OperationBody", None)
                setattr(value, "OperationBody", self)

class AnonymousTupleLiteralPart:

    pass
class LoopExp:

    pass
class essentialocl_IterateExp(LoopExp):

    pass
class essentialocl_IteratorExp(LoopExp):

    pass
class CollectionType:

    pass
class essentialocl_SetType(CollectionType):

    pass
class essentialocl_SequenceType(CollectionType):

    pass
class essentialocl_BagType(CollectionType):

    pass
class essentialocl_OrderedSetType(CollectionType):

    pass
class imperativeocl_ListType(CollectionType):

    pass
class AltExp:

    pass
class CallExp:

    pass
class qvtoperational_ResolveExp(CallExp):

    def __init__(self, one: str, isInverse: str, isDeferred: str, qvtoperational_ResolveExp: "OclExpression" = None):
        self.one = one
        self.isInverse = isInverse
        self.isDeferred = isDeferred
        self.qvtoperational_ResolveExp = qvtoperational_ResolveExp
        
        pass
    @property
    def isInverse(self):
        return self.__isInverse

    @isInverse.setter
    def isInverse(self, isInverse: str):
        self.__isInverse = isInverse


    @property
    def one(self):
        return self.__one

    @one.setter
    def one(self, one: str):
        self.__one = one


    @property
    def isDeferred(self):
        return self.__isDeferred

    @isDeferred.setter
    def isDeferred(self, isDeferred: str):
        self.__isDeferred = isDeferred


    @property
    def qvtoperational_ResolveExp(self):
        return self.__qvtoperational_ResolveExp

    @qvtoperational_ResolveExp.setter
    def qvtoperational_ResolveExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ResolveExp__qvtoperational_ResolveExp", None)
        self.__qvtoperational_ResolveExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression149"):
                opp_val = getattr(old_value, "OclExpression149", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression149"):
                opp_val = getattr(value, "OclExpression149", None)
                setattr(value, "OclExpression149", self)

class essentialocl_FeaturePropertyCall(CallExp):

    pass
class ImperativeExpression:

    pass
class imperativeocl_BlockExp(ImperativeExpression):

    pass
class imperativeocl_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: str, imperativeocl_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.imperativeocl_VariableInitExp = imperativeocl_VariableInitExp
        
        pass
    @property
    def withResult(self):
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: str):
        self.__withResult = withResult


    @property
    def imperativeocl_VariableInitExp(self):
        return self.__imperativeocl_VariableInitExp

    @imperativeocl_VariableInitExp.setter
    def imperativeocl_VariableInitExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_VariableInitExp__imperativeocl_VariableInitExp", None)
        self.__imperativeocl_VariableInitExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable34"):
                opp_val = getattr(old_value, "Variable34", None)
                if opp_val == self:
                    setattr(old_value, "Variable34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable34"):
                opp_val = getattr(value, "Variable34", None)
                setattr(value, "Variable34", self)

class imperativeocl_SwitchExp(ImperativeExpression, CallExp):

    pass
class imperativeocl_ComputeExp(ImperativeExpression):

    pass
class imperativeocl_ImperativeLoopExp(LoopExp, ImperativeExpression):

    pass
class imperativeocl_UnpackExp(ImperativeExpression):

    pass
class imperativeocl_AssignExp(ImperativeExpression):

    def __init__(self, isReset: str, imperativeocl_AssignExp: set["OclExpression"] = None, imperativeocl_AssignExp22: "OclExpression" = None, imperativeocl_AssignExp25: "OclExpression" = None):
        self.isReset = isReset
        self.imperativeocl_AssignExp = imperativeocl_AssignExp if imperativeocl_AssignExp is not None else set()
        self.imperativeocl_AssignExp22 = imperativeocl_AssignExp22
        self.imperativeocl_AssignExp25 = imperativeocl_AssignExp25
        
        pass
    @property
    def isReset(self):
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: str):
        self.__isReset = isReset


    @property
    def imperativeocl_AssignExp22(self):
        return self.__imperativeocl_AssignExp22

    @imperativeocl_AssignExp22.setter
    def imperativeocl_AssignExp22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssignExp__imperativeocl_AssignExp22", None)
        self.__imperativeocl_AssignExp22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression23"):
                opp_val = getattr(old_value, "OclExpression23", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression23"):
                opp_val = getattr(value, "OclExpression23", None)
                setattr(value, "OclExpression23", self)

    @property
    def imperativeocl_AssignExp25(self):
        return self.__imperativeocl_AssignExp25

    @imperativeocl_AssignExp25.setter
    def imperativeocl_AssignExp25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssignExp__imperativeocl_AssignExp25", None)
        self.__imperativeocl_AssignExp25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression26"):
                opp_val = getattr(old_value, "OclExpression26", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression26"):
                opp_val = getattr(value, "OclExpression26", None)
                setattr(value, "OclExpression26", self)

    @property
    def imperativeocl_AssignExp(self):
        return self.__imperativeocl_AssignExp

    @imperativeocl_AssignExp.setter
    def imperativeocl_AssignExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssignExp__imperativeocl_AssignExp", None)
        self.__imperativeocl_AssignExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression20"):
                    opp_val = getattr(item, "OclExpression20", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression20"):
                    opp_val = getattr(item, "OclExpression20", None)
                    
                    setattr(item, "OclExpression20", self)
                    

class ImperativeLoopExp:

    pass
class imperativeocl_CollectorExp(ImperativeLoopExp):

    pass
class imperativeocl_ImperativeIterateExp(ImperativeLoopExp):

    pass
class Property:

    pass
class qvtoperational_ContextualProperty(Property):

    pass
class ObjectTemplateExp:

    pass
class Element:

    pass
class emof_Tag(Element):

    def __init__(self, value: str, name: str, tag: set["Element"] = None, ownedTag: "Transformation" = None, ownedTag118: "Module" = None, Element: "imperativeocl_LogExp" = None, Element115: "emof_Tag" = None):
        self.value = value
        self.name = name
        self.tag = tag if tag is not None else set()
        self.ownedTag = ownedTag
        self.ownedTag118 = ownedTag118
        
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
    def ownedTag118(self):
        return self.__ownedTag118

    @ownedTag118.setter
    def ownedTag118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Tag__ownedTag118", None)
        self.__ownedTag118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module"):
                opp_val = getattr(old_value, "Module", None)
                if opp_val == self:
                    setattr(old_value, "Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module"):
                opp_val = getattr(value, "Module", None)
                setattr(value, "Module", self)

    @property
    def ownedTag(self):
        return self.__ownedTag

    @ownedTag.setter
    def ownedTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Tag__ownedTag", None)
        self.__ownedTag = value
        
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
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Tag__tag", None)
        self.__tag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element115"):
                    opp_val = getattr(item, "Element115", None)
                    
                    if opp_val == self:
                        setattr(item, "Element115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element115"):
                    opp_val = getattr(item, "Element115", None)
                    
                    setattr(item, "Element115", self)
                    

class qvtbase_Predicate(Element):

    pass
class emof_Comment(Element):

    pass
class qvtoperational_ModuleImport(Element):

    def __init__(self, kind: str, moduleImport: "Module" = None, qvtoperational_ModuleImport211: "Module" = None, qvtoperational_ModuleImport: set["ModelType"] = None, Element: "imperativeocl_LogExp" = None, Element115: "emof_Tag" = None):
        self.kind = kind
        self.moduleImport = moduleImport
        self.qvtoperational_ModuleImport211 = qvtoperational_ModuleImport211
        self.qvtoperational_ModuleImport = qvtoperational_ModuleImport if qvtoperational_ModuleImport is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def qvtoperational_ModuleImport(self):
        return self.__qvtoperational_ModuleImport

    @qvtoperational_ModuleImport.setter
    def qvtoperational_ModuleImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModuleImport__qvtoperational_ModuleImport", None)
        self.__qvtoperational_ModuleImport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelType207"):
                    opp_val = getattr(item, "ModelType207", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType207", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType207"):
                    opp_val = getattr(item, "ModelType207", None)
                    
                    setattr(item, "ModelType207", self)
                    

    @property
    def qvtoperational_ModuleImport211(self):
        return self.__qvtoperational_ModuleImport211

    @qvtoperational_ModuleImport211.setter
    def qvtoperational_ModuleImport211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModuleImport__qvtoperational_ModuleImport211", None)
        self.__qvtoperational_ModuleImport211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module212"):
                opp_val = getattr(old_value, "Module212", None)
                if opp_val == self:
                    setattr(old_value, "Module212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module212"):
                opp_val = getattr(value, "Module212", None)
                setattr(value, "Module212", self)

    @property
    def moduleImport(self):
        return self.__moduleImport

    @moduleImport.setter
    def moduleImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModuleImport__moduleImport", None)
        self.__moduleImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module209"):
                opp_val = getattr(old_value, "Module209", None)
                if opp_val == self:
                    setattr(old_value, "Module209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module209"):
                opp_val = getattr(value, "Module209", None)
                setattr(value, "Module209", self)

class qvtbase_Pattern(Element):

    pass
class qvtoperational_OperationBody(Element):

    pass
class emof_NamedElement(Element):

    def __init__(self, name: str, Element: "imperativeocl_LogExp" = None, Element115: "emof_Tag" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class qvtrelation_RelationImplementation(Element):

    pass
class qvtrelation_Key(Element):

    pass
class imperativeocl_AnonymousTupleLiteralPart(Element):

    pass
class qvttemplate_PropertyTemplateItem(Element):

    pass
class Class:

    pass
class imperativeocl_AnonymousTupleType(Class):

    pass
class qvtbase_Transformation(Package, Class):

    pass
class essentialocl_TupleType(Class, DataType):

    pass
class qvtoperational_Module(Class, Package):

    def __init__(self, isBlackbox: str, owner: set["Tag"] = None, module: set["Property"] = None, module204: set["ModuleImport"] = None, qvtoperational_Module: set["ModelType"] = None, Class314: "qvtrelation_Key" = None, Class121: "emof_Operation" = None, Class72: "imperativeocl_InstantiationExp" = None, Class: "qvttemplate_ObjectTemplateExp" = None, Class152: "qvtoperational_OperationalTransformation" = None, Class111: "emof_Class" = None, Class184: "qvtoperational_ContextualProperty" = None, Class134: "emof_Property" = None, Package270: "qvtbase_TypedModel" = None, Package195: "qvtoperational_ModelType" = None, Package: "emof_Package" = None, Package129: "emof_Type" = None):
        self.isBlackbox = isBlackbox
        self.owner = owner if owner is not None else set()
        self.module = module if module is not None else set()
        self.module204 = module204 if module204 is not None else set()
        self.qvtoperational_Module = qvtoperational_Module if qvtoperational_Module is not None else set()
        
        pass
    @property
    def isBlackbox(self):
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox


    @property
    def qvtoperational_Module(self):
        return self.__qvtoperational_Module

    @qvtoperational_Module.setter
    def qvtoperational_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__qvtoperational_Module", None)
        self.__qvtoperational_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelType"):
                    opp_val = getattr(item, "ModelType", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType"):
                    opp_val = getattr(item, "ModelType", None)
                    
                    setattr(item, "ModelType", self)
                    

    @property
    def module(self):
        return self.__module

    @module.setter
    def module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__module", None)
        self.__module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property202"):
                    opp_val = getattr(item, "Property202", None)
                    
                    if opp_val == self:
                        setattr(item, "Property202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property202"):
                    opp_val = getattr(item, "Property202", None)
                    
                    setattr(item, "Property202", self)
                    

    @property
    def module204(self):
        return self.__module204

    @module204.setter
    def module204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__module204", None)
        self.__module204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModuleImport"):
                    opp_val = getattr(item, "ModuleImport", None)
                    
                    if opp_val == self:
                        setattr(item, "ModuleImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModuleImport"):
                    opp_val = getattr(item, "ModuleImport", None)
                    
                    setattr(item, "ModuleImport", self)
                    

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tag200"):
                    opp_val = getattr(item, "Tag200", None)
                    
                    if opp_val == self:
                        setattr(item, "Tag200", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tag200"):
                    opp_val = getattr(item, "Tag200", None)
                    
                    setattr(item, "Tag200", self)
                    

class qvtoperational_ModelType(URIExtent, Class):

    def __init__(self, conformanceKind: str, qvtoperational_ModelType: set["Package"] = None, qvtoperational_ModelType197: set["OclExpression"] = None, Class314: "qvtrelation_Key" = None, Class121: "emof_Operation" = None, Class72: "imperativeocl_InstantiationExp" = None, Class: "qvttemplate_ObjectTemplateExp" = None, Class152: "qvtoperational_OperationalTransformation" = None, Class111: "emof_Class" = None, Class184: "qvtoperational_ContextualProperty" = None, Class134: "emof_Property" = None):
        self.conformanceKind = conformanceKind
        self.qvtoperational_ModelType = qvtoperational_ModelType if qvtoperational_ModelType is not None else set()
        self.qvtoperational_ModelType197 = qvtoperational_ModelType197 if qvtoperational_ModelType197 is not None else set()
        
        pass
    @property
    def conformanceKind(self):
        return self.__conformanceKind

    @conformanceKind.setter
    def conformanceKind(self, conformanceKind: str):
        self.__conformanceKind = conformanceKind


    @property
    def qvtoperational_ModelType(self):
        return self.__qvtoperational_ModelType

    @qvtoperational_ModelType.setter
    def qvtoperational_ModelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModelType__qvtoperational_ModelType", None)
        self.__qvtoperational_ModelType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package195"):
                    opp_val = getattr(item, "Package195", None)
                    
                    if opp_val == self:
                        setattr(item, "Package195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package195"):
                    opp_val = getattr(item, "Package195", None)
                    
                    setattr(item, "Package195", self)
                    

    @property
    def qvtoperational_ModelType197(self):
        return self.__qvtoperational_ModelType197

    @qvtoperational_ModelType197.setter
    def qvtoperational_ModelType197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModelType__qvtoperational_ModelType197", None)
        self.__qvtoperational_ModelType197 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression198"):
                    opp_val = getattr(item, "OclExpression198", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression198", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression198"):
                    opp_val = getattr(item, "OclExpression198", None)
                    
                    setattr(item, "OclExpression198", self)
                    

class PropertyTemplateItem:

    pass
class TemplateExp:

    pass
class qvttemplate_CollectionTemplateExp(TemplateExp):

    def __init__(self, kind: str, qvttemplate_CollectionTemplateExp: set["OclExpression"] = None, qvttemplate_CollectionTemplateExp10: "OclExpression" = None, qvttemplate_CollectionTemplateExp8: "CollectionType" = None, TemplateExp: "qvtrelation_DomainPattern" = None):
        self.kind = kind
        self.qvttemplate_CollectionTemplateExp = qvttemplate_CollectionTemplateExp if qvttemplate_CollectionTemplateExp is not None else set()
        self.qvttemplate_CollectionTemplateExp10 = qvttemplate_CollectionTemplateExp10
        self.qvttemplate_CollectionTemplateExp8 = qvttemplate_CollectionTemplateExp8
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def qvttemplate_CollectionTemplateExp10(self):
        return self.__qvttemplate_CollectionTemplateExp10

    @qvttemplate_CollectionTemplateExp10.setter
    def qvttemplate_CollectionTemplateExp10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvttemplate_CollectionTemplateExp__qvttemplate_CollectionTemplateExp10", None)
        self.__qvttemplate_CollectionTemplateExp10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression11"):
                opp_val = getattr(old_value, "OclExpression11", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression11"):
                opp_val = getattr(value, "OclExpression11", None)
                setattr(value, "OclExpression11", self)

    @property
    def qvttemplate_CollectionTemplateExp8(self):
        return self.__qvttemplate_CollectionTemplateExp8

    @qvttemplate_CollectionTemplateExp8.setter
    def qvttemplate_CollectionTemplateExp8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvttemplate_CollectionTemplateExp__qvttemplate_CollectionTemplateExp8", None)
        self.__qvttemplate_CollectionTemplateExp8 = value
        
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
    def qvttemplate_CollectionTemplateExp(self):
        return self.__qvttemplate_CollectionTemplateExp

    @qvttemplate_CollectionTemplateExp.setter
    def qvttemplate_CollectionTemplateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvttemplate_CollectionTemplateExp__qvttemplate_CollectionTemplateExp", None)
        self.__qvttemplate_CollectionTemplateExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression6"):
                    opp_val = getattr(item, "OclExpression6", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression6"):
                    opp_val = getattr(item, "OclExpression6", None)
                    
                    setattr(item, "OclExpression6", self)
                    

class qvttemplate_ObjectTemplateExp(TemplateExp):

    pass
class OclExpression:

    pass
class essentialocl_LiteralExp(OclExpression):

    pass
class essentialocl_LoopExp(CallExp, OclExpression):

    pass
class essentialocl_LetExp(OclExpression):

    pass
class essentialocl_IfExp(OclExpression):

    pass
class essentialocl_TypeExp(OclExpression):

    pass
class essentialocl_CallExp(OclExpression):

    pass
class essentialocl_VariableExp(OclExpression):

    pass
class imperativeocl_ImperativeExpression(OclExpression):

    pass
class Variable:

    pass
class qvtcore_RealizedVariable(Variable):

    pass
class qvtbase_FunctionParameter(Variable, Parameter):

    pass
class qvtoperational_VarParameter(Variable, Parameter):

    def __init__(self, kind: str, context: "ImperativeOperation" = None, result: "ImperativeOperation" = None, Variable352: "essentialocl_LoopExp" = None, Variable295: "qvtrelation_Relation" = None, Variable75: "imperativeocl_InstantiationExp" = None, Variable379: "essentialocl_ExpressionInOcl" = None, Variable18: "imperativeocl_ImperativeIterateExp" = None, Variable98: "imperativeocl_CollectorExp" = None, Variable282: "qvtbase_Pattern" = None, Variable: "qvttemplate_TemplateExp" = None, Variable376: "essentialocl_ExpressionInOcl" = None, Variable100: "imperativeocl_UnpackExp" = None, Variable382: "essentialocl_ExpressionInOcl" = None, Variable34: "imperativeocl_VariableInitExp" = None, Variable345: "essentialocl_VariableExp" = None, Variable333: "essentialocl_LetExp" = None, Variable41: "imperativeocl_ComputeExp" = None, Variable222: "qvtoperational_ObjectExp" = None, Variable359: "essentialocl_IterateExp" = None, Variable304: "qvtrelation_RelationDomain" = None, Parameter: "emof_Operation" = None, Parameter341: "essentialocl_Variable" = None):
        self.kind = kind
        self.context = context
        self.result = result
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_VarParameter__context", None)
        self.__context = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation214"):
                opp_val = getattr(old_value, "ImperativeOperation214", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation214"):
                opp_val = getattr(value, "ImperativeOperation214", None)
                setattr(value, "ImperativeOperation214", self)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_VarParameter__result", None)
        self.__result = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation216"):
                opp_val = getattr(old_value, "ImperativeOperation216", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation216"):
                opp_val = getattr(value, "ImperativeOperation216", None)
                setattr(value, "ImperativeOperation216", self)

class LiteralExp:

    pass
class imperativeocl_AnonymousTupleLiteralExp(LiteralExp):

    pass
class essentialocl_PrimitiveLiteralExp(LiteralExp):

    pass
class essentialocl_NullLiteralExp(LiteralExp):

    pass
class essentialocl_EnumLiteralExp(LiteralExp):

    pass
class essentialocl_CollectionLiteralExp(LiteralExp):

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
        old_value = getattr(self, f"_essentialocl_CollectionLiteralExp__CollectionLiteralExp", None)
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
                    

class essentialocl_TupleLiteralExp(LiteralExp):

    pass
class essentialocl_InvalidLiteralExp(LiteralExp):

    pass
class qvttemplate_TemplateExp(LiteralExp):

    pass
class LogExp:

    pass
class imperativeocl_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, imperativeocl_AssertExp: "LogExp" = None, imperativeocl_AssertExp93: "OclExpression" = None):
        self.severity = severity
        self.imperativeocl_AssertExp = imperativeocl_AssertExp
        self.imperativeocl_AssertExp93 = imperativeocl_AssertExp93
        
        pass
    @property
    def severity(self):
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity


    @property
    def imperativeocl_AssertExp(self):
        return self.__imperativeocl_AssertExp

    @imperativeocl_AssertExp.setter
    def imperativeocl_AssertExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssertExp__imperativeocl_AssertExp", None)
        self.__imperativeocl_AssertExp = value
        
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
    def imperativeocl_AssertExp93(self):
        return self.__imperativeocl_AssertExp93

    @imperativeocl_AssertExp93.setter
    def imperativeocl_AssertExp93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssertExp__imperativeocl_AssertExp93", None)
        self.__imperativeocl_AssertExp93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression94"):
                opp_val = getattr(old_value, "OclExpression94", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression94"):
                opp_val = getattr(value, "OclExpression94", None)
                setattr(value, "OclExpression94", self)

class imperativeocl_TupleExp(ImperativeExpression):

    pass
class imperativeocl_ForExp(ImperativeLoopExp):

    pass
class imperativeocl_ContinueExp(ImperativeExpression):

    pass
class imperativeocl_LogExp(ImperativeExpression):

    def __init__(self, text: str, level: str, imperativeocl_LogExp: "OclExpression" = None, imperativeocl_LogExp90: "Element" = None):
        self.text = text
        self.level = level
        self.imperativeocl_LogExp = imperativeocl_LogExp
        self.imperativeocl_LogExp90 = imperativeocl_LogExp90
        
        pass
    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def imperativeocl_LogExp90(self):
        return self.__imperativeocl_LogExp90

    @imperativeocl_LogExp90.setter
    def imperativeocl_LogExp90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_LogExp__imperativeocl_LogExp90", None)
        self.__imperativeocl_LogExp90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element"):
                opp_val = getattr(old_value, "Element", None)
                if opp_val == self:
                    setattr(old_value, "Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element"):
                opp_val = getattr(value, "Element", None)
                setattr(value, "Element", self)

    @property
    def imperativeocl_LogExp(self):
        return self.__imperativeocl_LogExp

    @imperativeocl_LogExp.setter
    def imperativeocl_LogExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_LogExp__imperativeocl_LogExp", None)
        self.__imperativeocl_LogExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression88"):
                opp_val = getattr(old_value, "OclExpression88", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression88"):
                opp_val = getattr(value, "OclExpression88", None)
                setattr(value, "OclExpression88", self)

class imperativeocl_DictLiteralPart(Element):

    pass
class DictLiteralPart:

    pass
class imperativeocl_DictLiteralExp(LiteralExp):

    pass
class imperativeocl_DictionaryType(CollectionType):

    pass
class imperativeocl_InstantiationExp(ImperativeExpression):

    pass
class imperativeocl_Typedef(Class):

    pass
class imperativeocl_WhileExp(ImperativeExpression):

    pass
class imperativeocl_RaiseExp(ImperativeExpression):

    pass
class Type:

    pass
class imperativeocl_TemplateParameterType(Type):

    def __init__(self, specification: str, Type389: "essentialocl_CollectionType" = None, Type: "imperativeocl_TryExp" = None, Type63: "imperativeocl_RaiseExp" = None, Type141: "emof_TypedElement" = None, Type347: "essentialocl_TypeExp" = None, Type102: "imperativeocl_AnonymousTupleType" = None, Type126: "emof_Package" = None, Type124: "emof_Operation" = None, Type80: "imperativeocl_DictionaryType" = None, Type67: "imperativeocl_Typedef" = None):
        self.specification = specification
        
        pass
    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


class emof_DataType(Type):

    pass
class essentialocl_VoidType(Type):

    pass
class essentialocl_AnyType(Type, Class):

    pass
class emof_Class(Type):

    def __init__(self, isAbstract: str, emof_Class: set["Property"] = None, class_: set["Operation"] = None, emof_Class110: set["Class"] = None, Type389: "essentialocl_CollectionType" = None, Type: "imperativeocl_TryExp" = None, Type63: "imperativeocl_RaiseExp" = None, Type141: "emof_TypedElement" = None, Type347: "essentialocl_TypeExp" = None, Type102: "imperativeocl_AnonymousTupleType" = None, Type126: "emof_Package" = None, Type124: "emof_Operation" = None, Type80: "imperativeocl_DictionaryType" = None, Type67: "imperativeocl_Typedef" = None):
        self.isAbstract = isAbstract
        self.emof_Class = emof_Class if emof_Class is not None else set()
        self.class_ = class_ if class_ is not None else set()
        self.emof_Class110 = emof_Class110 if emof_Class110 is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def emof_Class110(self):
        return self.__emof_Class110

    @emof_Class110.setter
    def emof_Class110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__emof_Class110", None)
        self.__emof_Class110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class111"):
                    opp_val = getattr(item, "Class111", None)
                    
                    if opp_val == self:
                        setattr(item, "Class111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class111"):
                    opp_val = getattr(item, "Class111", None)
                    
                    setattr(item, "Class111", self)
                    

    @property
    def emof_Class(self):
        return self.__emof_Class

    @emof_Class.setter
    def emof_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__emof_Class", None)
        self.__emof_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property107"):
                    opp_val = getattr(item, "Property107", None)
                    
                    if opp_val == self:
                        setattr(item, "Property107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property107"):
                    opp_val = getattr(item, "Property107", None)
                    
                    setattr(item, "Property107", self)
                    

    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__class_", None)
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
                    

class essentialocl_InvalidType(Type):

    pass
class imperativeocl_TryExp(ImperativeExpression):

    pass
class imperativeocl_BreakExp(ImperativeExpression):

    pass
class imperativeocl_ReturnExp(ImperativeExpression):

    pass
class imperativeocl_UnlinkExp(ImperativeExpression):

    pass
class imperativeocl_AltExp(ImperativeExpression):

    pass