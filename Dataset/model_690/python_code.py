from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ImportKind(Enum):
    extension = "extension"
    access = "access"
class CollectionKind(Enum):
    OrderedSet = "OrderedSet"
    Set = "Set"
    Bag = "Bag"
    Sequence = "Sequence"
class EnforcementMode(Enum):
    Deletion = "Deletion"
    Creation = "Creation"
class DirectionKind(Enum):
    out = "out"
    in = "in"
    inout = "inout"
class SeverityKind(Enum):
    error = "error"
    fatal = "fatal"
    warning = "warning"


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
class essentialocl_CollectionItem(CollectionLiteralPart):

    pass
class essentialocl_CollectionRange(CollectionLiteralPart):

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
class NumericLiteralExp:

    pass
class essentialocl_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class essentialocl_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class essentialocl_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class TryExp:

    pass
class PrimitiveLiteralExp:

    pass
class essentialocl_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class essentialocl_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class essentialocl_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

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
class TypedModel:

    pass
class qvtcore_EnforcementOperation:

    def __init__(self, enforcementMode: str, 4290: "BottomPattern" = None, qvtcore_EnforcementOperation: "OperationCallExp" = None):
        self.enforcementMode = enforcementMode
        self.4290 = 4290
        self.qvtcore_EnforcementOperation = qvtcore_EnforcementOperation
        
    @property
    def enforcementMode(self) -> str:
        return self.__enforcementMode

    @enforcementMode.setter
    def enforcementMode(self, enforcementMode: str):
        self.__enforcementMode = enforcementMode

    @property
    def 4290(self):
        return self.__4290

    @4290.setter
    def 4290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_EnforcementOperation__4290", None)
        self.__4290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#291"):
                opp_val = getattr(old_value, "#291", None)
                if opp_val == self:
                    setattr(old_value, "#291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#291"):
                opp_val = getattr(value, "#291", None)
                setattr(value, "#291", self)

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

    def __init__(self, isTopLevel: str, 6346: set["RelationImplementation"] = None, 5349: "Pattern" = None, qvtrelation_Relation: set["Variable"] = None, 5352: "Pattern" = None, #295: "qvtbase_Domain", #305: "qvtbase_Transformation", Rule: "qvtbase_Rule"):
        self.isTopLevel = isTopLevel
        self.6346 = 6346 if 6346 is not None else set()
        self.5349 = 5349
        self.qvtrelation_Relation = qvtrelation_Relation if qvtrelation_Relation is not None else set()
        self.5352 = 5352
        
    @property
    def isTopLevel(self) -> str:
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: str):
        self.__isTopLevel = isTopLevel

    @property
    def 6346(self):
        return self.__6346

    @6346.setter
    def 6346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_Relation__6346", None)
        self.__6346 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#347"):
                    opp_val = getattr(item, "#347", None)
                    
                    if opp_val == self:
                        setattr(item, "#347", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#347"):
                    opp_val = getattr(item, "#347", None)
                    
                    setattr(item, "#347", self)
                    

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
                if hasattr(item, "Variable344"):
                    opp_val = getattr(item, "Variable344", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable344", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable344"):
                    opp_val = getattr(item, "Variable344", None)
                    
                    setattr(item, "Variable344", self)
                    

    @property
    def 5349(self):
        return self.__5349

    @5349.setter
    def 5349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_Relation__5349", None)
        self.__5349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#350"):
                opp_val = getattr(old_value, "#350", None)
                if opp_val == self:
                    setattr(old_value, "#350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#350"):
                opp_val = getattr(value, "#350", None)
                setattr(value, "#350", self)

    @property
    def 5352(self):
        return self.__5352

    @5352.setter
    def 5352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtrelation_Relation__5352", None)
        self.__5352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#353"):
                opp_val = getattr(old_value, "#353", None)
                if opp_val == self:
                    setattr(old_value, "#353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#353"):
                opp_val = getattr(value, "#353", None)
                setattr(value, "#353", self)

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
class qvtcore_Mapping(Rule, Area):

    pass
class CorePattern:

    pass
class qvtcore_GuardPattern(CorePattern):

    pass
class qvtcore_BottomPattern(CorePattern):

    pass
class qvtcore_Assignment:

    def __init__(self, isDefault: str, 4259: "BottomPattern" = None, qvtcore_Assignment: "OclExpression" = None, qvtcore_Assignment264: "OclExpression" = None, qvtcore_Assignment267: "Property" = None):
        self.isDefault = isDefault
        self.4259 = 4259
        self.qvtcore_Assignment = qvtcore_Assignment
        self.qvtcore_Assignment264 = qvtcore_Assignment264
        self.qvtcore_Assignment267 = qvtcore_Assignment267
        
    @property
    def isDefault(self) -> str:
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: str):
        self.__isDefault = isDefault

    @property
    def 4259(self):
        return self.__4259

    @4259.setter
    def 4259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_Assignment__4259", None)
        self.__4259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#260"):
                opp_val = getattr(old_value, "#260", None)
                if opp_val == self:
                    setattr(old_value, "#260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#260"):
                opp_val = getattr(value, "#260", None)
                setattr(value, "#260", self)

    @property
    def qvtcore_Assignment264(self):
        return self.__qvtcore_Assignment264

    @qvtcore_Assignment264.setter
    def qvtcore_Assignment264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_Assignment__qvtcore_Assignment264", None)
        self.__qvtcore_Assignment264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression265"):
                opp_val = getattr(old_value, "OclExpression265", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression265"):
                opp_val = getattr(value, "OclExpression265", None)
                setattr(value, "OclExpression265", self)

    @property
    def qvtcore_Assignment267(self):
        return self.__qvtcore_Assignment267

    @qvtcore_Assignment267.setter
    def qvtcore_Assignment267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtcore_Assignment__qvtcore_Assignment267", None)
        self.__qvtcore_Assignment267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property268"):
                opp_val = getattr(old_value, "Property268", None)
                if opp_val == self:
                    setattr(old_value, "Property268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property268"):
                opp_val = getattr(value, "Property268", None)
                setattr(value, "Property268", self)

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
            if hasattr(old_value, "OclExpression262"):
                opp_val = getattr(old_value, "OclExpression262", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression262"):
                opp_val = getattr(value, "OclExpression262", None)
                setattr(value, "OclExpression262", self)

class BottomPattern:

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
class ModuleImport:

    pass
class URIExtent:

    pass
class ModelType:

    pass
class OperationCallExp:

    pass
class qvtoperational_ImperativeCallExp(OperationCallExp):

    def __init__(self, isVirtual: str, OperationCallExp: "qvtcore_EnforcementOperation"):
        self.isVirtual = isVirtual
        
    @property
    def isVirtual(self) -> str:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: str):
        self.__isVirtual = isVirtual

class ImperativeCallExp:

    pass
class qvtoperational_MappingCallExp(ImperativeCallExp):

    def __init__(self, isStrict: str):
        self.isStrict = isStrict
        
    @property
    def isStrict(self) -> str:
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
class EntryOperation:

    pass
class ModelParameter:

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

    def __init__(self, isQuery: str, #246: "qvtoperational_OperationBody", #243: "qvtoperational_VarParameter", #240: "qvtoperational_VarParameter", ImperativeOperation: "qvtoperational_ImperativeOperation"):
        self.isQuery = isQuery
        
    @property
    def isQuery(self) -> str:
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
class Enumeration:

    pass
class Extent:

    pass
class emof_URIExtent(Extent):

    pass
class Package:

    pass
class NamedElement:

    pass
class emof_TypedElement(NamedElement):

    pass
class qvtbase_Rule(NamedElement):

    pass
class qvtbase_Domain(NamedElement):

    def __init__(self, isCheckable: str, isEnforceable: str, 5294: "Rule" = None, qvtbase_Domain: "TypedModel" = None, NamedElement: "emof_Comment"):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.5294 = 5294
        self.qvtbase_Domain = qvtbase_Domain
        
    @property
    def isCheckable(self) -> str:
        return self.__isCheckable

    @isCheckable.setter
    def isCheckable(self, isCheckable: str):
        self.__isCheckable = isCheckable

    @property
    def isEnforceable(self) -> str:
        return self.__isEnforceable

    @isEnforceable.setter
    def isEnforceable(self, isEnforceable: str):
        self.__isEnforceable = isEnforceable

    @property
    def 5294(self):
        return self.__5294

    @5294.setter
    def 5294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtbase_Domain__5294", None)
        self.__5294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#295"):
                opp_val = getattr(old_value, "#295", None)
                if opp_val == self:
                    setattr(old_value, "#295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#295"):
                opp_val = getattr(value, "#295", None)
                setattr(value, "#295", self)

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
class emof_Package(NamedElement):

    def __init__(self, uri: str, 2139: set["Type"] = None, emof_Package: set["Package"] = None, NamedElement: "emof_Comment"):
        self.uri = uri
        self.2139 = 2139 if 2139 is not None else set()
        self.emof_Package = emof_Package if emof_Package is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

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
                    

    @property
    def 2139(self):
        return self.__2139

    @2139.setter
    def 2139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Package__2139", None)
        self.__2139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#140"):
                    opp_val = getattr(item, "#140", None)
                    
                    if opp_val == self:
                        setattr(item, "#140", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#140"):
                    opp_val = getattr(item, "#140", None)
                    
                    setattr(item, "#140", self)
                    

class emof_EnumerationLiteral(NamedElement):

    pass
class emof_MultiplicityElement(ABC):

    def __init__(self, isUnique: str, isOrdered: str, lower: str, upper: str):
        self.isUnique = isUnique
        self.isOrdered = isOrdered
        self.lower = lower
        self.upper = upper
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

class Parameter:

    pass
class TypedElement:

    pass
class essentialocl_OclExpression(TypedElement):

    pass
class essentialocl_TupleLiteralPart(TypedElement):

    pass
class essentialocl_Variable(TypedElement):

    pass
class essentialocl_CollectionLiteralPart(TypedElement):

    pass
class MultiplicityElement:

    pass
class emof_Parameter(TypedElement, MultiplicityElement):

    pass
class emof_Property(TypedElement, MultiplicityElement):

    def __init__(self, isReadOnly: str, isDerived: str, isComposite: str, isId: str, default: str, emof_Property: "Class" = None, emof_Property154: "Property" = None, 3157: "Module" = None):
        self.isReadOnly = isReadOnly
        self.isDerived = isDerived
        self.isComposite = isComposite
        self.isId = isId
        self.default = default
        self.emof_Property = emof_Property
        self.emof_Property154 = emof_Property154
        self.3157 = 3157
        
    @property
    def isId(self) -> str:
        return self.__isId

    @isId.setter
    def isId(self, isId: str):
        self.__isId = isId

    @property
    def isComposite(self) -> str:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: str):
        self.__isComposite = isComposite

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def isDerived(self) -> str:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: str):
        self.__isDerived = isDerived

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def 3157(self):
        return self.__3157

    @3157.setter
    def 3157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Property__3157", None)
        self.__3157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#158"):
                opp_val = getattr(old_value, "#158", None)
                if opp_val == self:
                    setattr(old_value, "#158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#158"):
                opp_val = getattr(value, "#158", None)
                setattr(value, "#158", self)

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
            if hasattr(old_value, "Class152"):
                opp_val = getattr(old_value, "Class152", None)
                if opp_val == self:
                    setattr(old_value, "Class152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class152"):
                opp_val = getattr(value, "Class152", None)
                setattr(value, "Class152", self)

    @property
    def emof_Property154(self):
        return self.__emof_Property154

    @emof_Property154.setter
    def emof_Property154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Property__emof_Property154", None)
        self.__emof_Property154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property155"):
                opp_val = getattr(old_value, "Property155", None)
                if opp_val == self:
                    setattr(old_value, "Property155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property155"):
                opp_val = getattr(value, "Property155", None)
                setattr(value, "Property155", self)

class emof_Operation(TypedElement, MultiplicityElement):

    pass
class emof_Object:

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class essentialocl_CollectionType(DataType):

    pass
class emof_PrimitiveType(DataType):

    pass
class emof_Enumeration(DataType):

    pass
class Comment:

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
class qvtbase_Function(Operation):

    pass
class qvtoperational_ImperativeOperation(Operation):

    def __init__(self, isBlackbox: str, 3207: "VarParameter" = None, 3210: set["VarParameter"] = None, qvtoperational_ImperativeOperation: "ImperativeOperation" = None, 3214: "OperationBody" = None, #147: "emof_Parameter", #112: "emof_Class", Operation: "qvtrelation_RelationImplementation", Operation416: "essentialocl_OperationCallExp"):
        self.isBlackbox = isBlackbox
        self.3207 = 3207
        self.3210 = 3210 if 3210 is not None else set()
        self.qvtoperational_ImperativeOperation = qvtoperational_ImperativeOperation
        self.3214 = 3214
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

    @property
    def 3210(self):
        return self.__3210

    @3210.setter
    def 3210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__3210", None)
        self.__3210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#211"):
                    opp_val = getattr(item, "#211", None)
                    
                    if opp_val == self:
                        setattr(item, "#211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#211"):
                    opp_val = getattr(item, "#211", None)
                    
                    setattr(item, "#211", self)
                    

    @property
    def 3207(self):
        return self.__3207

    @3207.setter
    def 3207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__3207", None)
        self.__3207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#208"):
                opp_val = getattr(old_value, "#208", None)
                if opp_val == self:
                    setattr(old_value, "#208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#208"):
                opp_val = getattr(value, "#208", None)
                setattr(value, "#208", self)

    @property
    def 3214(self):
        return self.__3214

    @3214.setter
    def 3214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ImperativeOperation__3214", None)
        self.__3214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#215"):
                opp_val = getattr(old_value, "#215", None)
                if opp_val == self:
                    setattr(old_value, "#215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#215"):
                opp_val = getattr(value, "#215", None)
                setattr(value, "#215", self)

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

class qvtoperational_MappingOperation(NamedElement, Operation, ImperativeOperation):

    pass
class LoopExp:

    pass
class essentialocl_IteratorExp(LoopExp):

    pass
class essentialocl_IterateExp(LoopExp):

    pass
class AnonymousTupleLiteralPart:

    pass
class LogExp:

    pass
class DictLiteralPart:

    pass
class Type:

    pass
class emof_DataType(Type):

    pass
class emof_Class(Type):

    def __init__(self, isAbstract: str, emof_Class: set["Property"] = None, 2: set["Operation"] = None, emof_Class114: set["Class"] = None, Type406: "essentialocl_TypeExp", Type137: "emof_Operation", Type160: "emof_TypedElement", Type66: "imperativeocl_RaiseExp", #140: "emof_Package", Type105: "imperativeocl_AnonymousTupleType", Type70: "imperativeocl_Typedef", Type452: "essentialocl_CollectionType", Type83: "imperativeocl_DictionaryType", Type: "imperativeocl_TryExp"):
        self.isAbstract = isAbstract
        self.emof_Class = emof_Class if emof_Class is not None else set()
        self.2 = 2 if 2 is not None else set()
        self.emof_Class114 = emof_Class114 if emof_Class114 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def 2(self):
        return self.__2

    @2.setter
    def 2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__2", None)
        self.__2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#112"):
                    opp_val = getattr(item, "#112", None)
                    
                    if opp_val == self:
                        setattr(item, "#112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#112"):
                    opp_val = getattr(item, "#112", None)
                    
                    setattr(item, "#112", self)
                    

    @property
    def emof_Class114(self):
        return self.__emof_Class114

    @emof_Class114.setter
    def emof_Class114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Class__emof_Class114", None)
        self.__emof_Class114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class115"):
                    opp_val = getattr(item, "Class115", None)
                    
                    if opp_val == self:
                        setattr(item, "Class115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class115"):
                    opp_val = getattr(item, "Class115", None)
                    
                    setattr(item, "Class115", self)
                    

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
                if hasattr(item, "Property110"):
                    opp_val = getattr(item, "Property110", None)
                    
                    if opp_val == self:
                        setattr(item, "Property110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property110"):
                    opp_val = getattr(item, "Property110", None)
                    
                    setattr(item, "Property110", self)
                    

class imperativeocl_TemplateParameterType(Type):

    def __init__(self, specification: str, Type406: "essentialocl_TypeExp", Type137: "emof_Operation", Type160: "emof_TypedElement", Type66: "imperativeocl_RaiseExp", #140: "emof_Package", Type105: "imperativeocl_AnonymousTupleType", Type70: "imperativeocl_Typedef", Type452: "essentialocl_CollectionType", Type83: "imperativeocl_DictionaryType", Type: "imperativeocl_TryExp"):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class essentialocl_InvalidType(Type):

    pass
class essentialocl_VoidType(Type):

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
        
    @property
    def isDeferred(self) -> str:
        return self.__isDeferred

    @isDeferred.setter
    def isDeferred(self, isDeferred: str):
        self.__isDeferred = isDeferred

    @property
    def one(self) -> str:
        return self.__one

    @one.setter
    def one(self, one: str):
        self.__one = one

    @property
    def isInverse(self) -> str:
        return self.__isInverse

    @isInverse.setter
    def isInverse(self, isInverse: str):
        self.__isInverse = isInverse

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
            if hasattr(old_value, "OclExpression168"):
                opp_val = getattr(old_value, "OclExpression168", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression168"):
                opp_val = getattr(value, "OclExpression168", None)
                setattr(value, "OclExpression168", self)

class essentialocl_FeaturePropertyCall(CallExp):

    pass
class ImperativeExpression:

    pass
class imperativeocl_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, imperativeocl_AssertExp: "LogExp" = None, imperativeocl_AssertExp96: "OclExpression" = None):
        self.severity = severity
        self.imperativeocl_AssertExp = imperativeocl_AssertExp
        self.imperativeocl_AssertExp96 = imperativeocl_AssertExp96
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def imperativeocl_AssertExp96(self):
        return self.__imperativeocl_AssertExp96

    @imperativeocl_AssertExp96.setter
    def imperativeocl_AssertExp96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssertExp__imperativeocl_AssertExp96", None)
        self.__imperativeocl_AssertExp96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression97"):
                opp_val = getattr(old_value, "OclExpression97", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression97"):
                opp_val = getattr(value, "OclExpression97", None)
                setattr(value, "OclExpression97", self)

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

class imperativeocl_TupleExp(ImperativeExpression):

    pass
class imperativeocl_WhileExp(ImperativeExpression):

    pass
class imperativeocl_ReturnExp(ImperativeExpression):

    pass
class imperativeocl_LogExp(ImperativeExpression):

    def __init__(self, text: str, level: str, imperativeocl_LogExp: "OclExpression" = None, imperativeocl_LogExp93: "Element" = None):
        self.text = text
        self.level = level
        self.imperativeocl_LogExp = imperativeocl_LogExp
        self.imperativeocl_LogExp93 = imperativeocl_LogExp93
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

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
            if hasattr(old_value, "OclExpression91"):
                opp_val = getattr(old_value, "OclExpression91", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression91"):
                opp_val = getattr(value, "OclExpression91", None)
                setattr(value, "OclExpression91", self)

    @property
    def imperativeocl_LogExp93(self):
        return self.__imperativeocl_LogExp93

    @imperativeocl_LogExp93.setter
    def imperativeocl_LogExp93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_LogExp__imperativeocl_LogExp93", None)
        self.__imperativeocl_LogExp93 = value
        
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

class imperativeocl_AltExp(ImperativeExpression):

    pass
class imperativeocl_UnlinkExp(ImperativeExpression):

    pass
class imperativeocl_UnpackExp(ImperativeExpression):

    pass
class imperativeocl_InstantiationExp(ImperativeExpression):

    pass
class imperativeocl_ImperativeLoopExp(LoopExp, ImperativeExpression):

    pass
class imperativeocl_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: str, imperativeocl_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.imperativeocl_VariableInitExp = imperativeocl_VariableInitExp
        
    @property
    def withResult(self) -> str:
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
            if hasattr(old_value, "Variable36"):
                opp_val = getattr(old_value, "Variable36", None)
                if opp_val == self:
                    setattr(old_value, "Variable36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable36"):
                opp_val = getattr(value, "Variable36", None)
                setattr(value, "Variable36", self)

class imperativeocl_SwitchExp(CallExp, ImperativeExpression):

    pass
class imperativeocl_ContinueExp(ImperativeExpression):

    pass
class imperativeocl_ComputeExp(ImperativeExpression):

    pass
class imperativeocl_RaiseExp(ImperativeExpression):

    pass
class imperativeocl_BreakExp(ImperativeExpression):

    pass
class imperativeocl_TryExp(ImperativeExpression):

    pass
class imperativeocl_AssignExp(ImperativeExpression):

    def __init__(self, isReset: str, imperativeocl_AssignExp27: "OclExpression" = None, imperativeocl_AssignExp: set["OclExpression"] = None, imperativeocl_AssignExp24: "OclExpression" = None):
        self.isReset = isReset
        self.imperativeocl_AssignExp27 = imperativeocl_AssignExp27
        self.imperativeocl_AssignExp = imperativeocl_AssignExp if imperativeocl_AssignExp is not None else set()
        self.imperativeocl_AssignExp24 = imperativeocl_AssignExp24
        
    @property
    def isReset(self) -> str:
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: str):
        self.__isReset = isReset

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
                if hasattr(item, "OclExpression22"):
                    opp_val = getattr(item, "OclExpression22", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression22"):
                    opp_val = getattr(item, "OclExpression22", None)
                    
                    setattr(item, "OclExpression22", self)
                    

    @property
    def imperativeocl_AssignExp27(self):
        return self.__imperativeocl_AssignExp27

    @imperativeocl_AssignExp27.setter
    def imperativeocl_AssignExp27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssignExp__imperativeocl_AssignExp27", None)
        self.__imperativeocl_AssignExp27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression28"):
                opp_val = getattr(old_value, "OclExpression28", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression28"):
                opp_val = getattr(value, "OclExpression28", None)
                setattr(value, "OclExpression28", self)

    @property
    def imperativeocl_AssignExp24(self):
        return self.__imperativeocl_AssignExp24

    @imperativeocl_AssignExp24.setter
    def imperativeocl_AssignExp24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imperativeocl_AssignExp__imperativeocl_AssignExp24", None)
        self.__imperativeocl_AssignExp24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression25"):
                opp_val = getattr(old_value, "OclExpression25", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression25"):
                opp_val = getattr(value, "OclExpression25", None)
                setattr(value, "OclExpression25", self)

class ImperativeLoopExp:

    pass
class imperativeocl_CollectorExp(ImperativeLoopExp):

    pass
class imperativeocl_ForExp(ImperativeLoopExp):

    pass
class imperativeocl_ImperativeIterateExp(ImperativeLoopExp):

    pass
class Property:

    pass
class qvtoperational_ContextualProperty(Property):

    pass
class imperativeocl_BlockExp(ImperativeExpression):

    pass
class CollectionType:

    pass
class imperativeocl_ListType(CollectionType):

    pass
class essentialocl_SetType(CollectionType):

    pass
class essentialocl_BagType(CollectionType):

    pass
class essentialocl_SequenceType(CollectionType):

    pass
class imperativeocl_DictionaryType(CollectionType):

    pass
class essentialocl_OrderedSetType(CollectionType):

    pass
class Class:

    pass
class qvtoperational_Module(Class, Package):

    def __init__(self, isBlackbox: str, 2222: set["Tag"] = None, 2225: set["Property"] = None, 3228: set["ModuleImport"] = None, qvtoperational_Module: set["ModelType"] = None, Class115: "emof_Class", Class367: "qvtrelation_Key", Class202: "qvtoperational_ContextualProperty", Class: "qvttemplate_ObjectTemplateExp", Class75: "imperativeocl_InstantiationExp", Class152: "emof_Property", Class171: "qvtoperational_OperationalTransformation", #132: "emof_Operation", #144: "emof_Type", Package217: "qvtoperational_ModelType", Package: "emof_Package", Package312: "qvtbase_TypedModel"):
        self.isBlackbox = isBlackbox
        self.2222 = 2222 if 2222 is not None else set()
        self.2225 = 2225 if 2225 is not None else set()
        self.3228 = 3228 if 3228 is not None else set()
        self.qvtoperational_Module = qvtoperational_Module if qvtoperational_Module is not None else set()
        
    @property
    def isBlackbox(self) -> str:
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
    def 2222(self):
        return self.__2222

    @2222.setter
    def 2222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__2222", None)
        self.__2222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#223"):
                    opp_val = getattr(item, "#223", None)
                    
                    if opp_val == self:
                        setattr(item, "#223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#223"):
                    opp_val = getattr(item, "#223", None)
                    
                    setattr(item, "#223", self)
                    

    @property
    def 2225(self):
        return self.__2225

    @2225.setter
    def 2225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__2225", None)
        self.__2225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#226"):
                    opp_val = getattr(item, "#226", None)
                    
                    if opp_val == self:
                        setattr(item, "#226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#226"):
                    opp_val = getattr(item, "#226", None)
                    
                    setattr(item, "#226", self)
                    

    @property
    def 3228(self):
        return self.__3228

    @3228.setter
    def 3228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_Module__3228", None)
        self.__3228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#229"):
                    opp_val = getattr(item, "#229", None)
                    
                    if opp_val == self:
                        setattr(item, "#229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#229"):
                    opp_val = getattr(item, "#229", None)
                    
                    setattr(item, "#229", self)
                    

class imperativeocl_AnonymousTupleType(Class):

    pass
class essentialocl_AnyType(Class, Type):

    pass
class qvtbase_Transformation(Package, Class):

    pass
class essentialocl_TupleType(DataType, Class):

    pass
class qvtoperational_ModelType(Class, URIExtent):

    def __init__(self, conformanceKind: str, qvtoperational_ModelType: set["Package"] = None, qvtoperational_ModelType219: set["OclExpression"] = None, Class115: "emof_Class", Class367: "qvtrelation_Key", Class202: "qvtoperational_ContextualProperty", Class: "qvttemplate_ObjectTemplateExp", Class75: "imperativeocl_InstantiationExp", Class152: "emof_Property", Class171: "qvtoperational_OperationalTransformation", #132: "emof_Operation"):
        self.conformanceKind = conformanceKind
        self.qvtoperational_ModelType = qvtoperational_ModelType if qvtoperational_ModelType is not None else set()
        self.qvtoperational_ModelType219 = qvtoperational_ModelType219 if qvtoperational_ModelType219 is not None else set()
        
    @property
    def conformanceKind(self) -> str:
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
                if hasattr(item, "Package217"):
                    opp_val = getattr(item, "Package217", None)
                    
                    if opp_val == self:
                        setattr(item, "Package217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package217"):
                    opp_val = getattr(item, "Package217", None)
                    
                    setattr(item, "Package217", self)
                    

    @property
    def qvtoperational_ModelType219(self):
        return self.__qvtoperational_ModelType219

    @qvtoperational_ModelType219.setter
    def qvtoperational_ModelType219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModelType__qvtoperational_ModelType219", None)
        self.__qvtoperational_ModelType219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression220"):
                    opp_val = getattr(item, "OclExpression220", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression220"):
                    opp_val = getattr(item, "OclExpression220", None)
                    
                    setattr(item, "OclExpression220", self)
                    

class imperativeocl_Typedef(Class):

    pass
class PropertyTemplateItem:

    pass
class TemplateExp:

    pass
class qvttemplate_CollectionTemplateExp(TemplateExp):

    def __init__(self, kind: str, qvttemplate_CollectionTemplateExp10: "OclExpression" = None, qvttemplate_CollectionTemplateExp: set["OclExpression"] = None, qvttemplate_CollectionTemplateExp8: "CollectionType" = None, TemplateExp: "qvtrelation_DomainPattern"):
        self.kind = kind
        self.qvttemplate_CollectionTemplateExp10 = qvttemplate_CollectionTemplateExp10
        self.qvttemplate_CollectionTemplateExp = qvttemplate_CollectionTemplateExp if qvttemplate_CollectionTemplateExp is not None else set()
        self.qvttemplate_CollectionTemplateExp8 = qvttemplate_CollectionTemplateExp8
        
    @property
    def kind(self) -> str:
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

class qvttemplate_ObjectTemplateExp(TemplateExp):

    pass
class ObjectTemplateExp:

    pass
class Element:

    pass
class imperativeocl_DictLiteralPart(Element):

    pass
class qvtbase_Pattern(Element):

    pass
class qvtoperational_ModuleImport(Element):

    def __init__(self, kind: str, qvtoperational_ModuleImport: set["ModelType"] = None, 3234: "Module" = None, qvtoperational_ModuleImport237: "Module" = None, Element: "imperativeocl_LogExp", #122: "emof_Tag"):
        self.kind = kind
        self.qvtoperational_ModuleImport = qvtoperational_ModuleImport if qvtoperational_ModuleImport is not None else set()
        self.3234 = 3234
        self.qvtoperational_ModuleImport237 = qvtoperational_ModuleImport237
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def 3234(self):
        return self.__3234

    @3234.setter
    def 3234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModuleImport__3234", None)
        self.__3234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#235"):
                opp_val = getattr(old_value, "#235", None)
                if opp_val == self:
                    setattr(old_value, "#235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#235"):
                opp_val = getattr(value, "#235", None)
                setattr(value, "#235", self)

    @property
    def qvtoperational_ModuleImport237(self):
        return self.__qvtoperational_ModuleImport237

    @qvtoperational_ModuleImport237.setter
    def qvtoperational_ModuleImport237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_ModuleImport__qvtoperational_ModuleImport237", None)
        self.__qvtoperational_ModuleImport237 = value
        
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
                if hasattr(item, "ModelType232"):
                    opp_val = getattr(item, "ModelType232", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType232", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType232"):
                    opp_val = getattr(item, "ModelType232", None)
                    
                    setattr(item, "ModelType232", self)
                    

class qvtrelation_RelationImplementation(Element):

    pass
class emof_Comment(Element):

    pass
class imperativeocl_AnonymousTupleLiteralPart(Element):

    pass
class qvtbase_Predicate(Element):

    pass
class qvtoperational_OperationBody(Element):

    pass
class emof_NamedElement(Element):

    def __init__(self, name: str, Element: "imperativeocl_LogExp", #122: "emof_Tag"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class emof_Tag(Element):

    def __init__(self, value: str, name: str, 2121: set["Element"] = None, 5: "Transformation" = None, 3: "Module" = None, Element: "imperativeocl_LogExp", #122: "emof_Tag"):
        self.value = value
        self.name = name
        self.2121 = 2121 if 2121 is not None else set()
        self.5 = 5
        self.3 = 3
        
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
    def 2121(self):
        return self.__2121

    @2121.setter
    def 2121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Tag__2121", None)
        self.__2121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#122"):
                    opp_val = getattr(item, "#122", None)
                    
                    if opp_val == self:
                        setattr(item, "#122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#122"):
                    opp_val = getattr(item, "#122", None)
                    
                    setattr(item, "#122", self)
                    

    @property
    def 5(self):
        return self.__5

    @5.setter
    def 5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Tag__5", None)
        self.__5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#124"):
                opp_val = getattr(old_value, "#124", None)
                if opp_val == self:
                    setattr(old_value, "#124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#124"):
                opp_val = getattr(value, "#124", None)
                setattr(value, "#124", self)

    @property
    def 3(self):
        return self.__3

    @3.setter
    def 3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emof_Tag__3", None)
        self.__3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#126"):
                opp_val = getattr(old_value, "#126", None)
                if opp_val == self:
                    setattr(old_value, "#126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#126"):
                opp_val = getattr(value, "#126", None)
                setattr(value, "#126", self)

class qvtrelation_Key(Element):

    pass
class qvttemplate_PropertyTemplateItem(Element):

    pass
class LiteralExp:

    pass
class essentialocl_InvalidLiteralExp(LiteralExp):

    pass
class essentialocl_PrimitiveLiteralExp(LiteralExp):

    pass
class imperativeocl_DictLiteralExp(LiteralExp):

    pass
class essentialocl_NullLiteralExp(LiteralExp):

    pass
class essentialocl_TupleLiteralExp(LiteralExp):

    pass
class essentialocl_EnumLiteralExp(LiteralExp):

    pass
class essentialocl_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, 7420: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.7420 = 7420 if 7420 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def 7420(self):
        return self.__7420

    @7420.setter
    def 7420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_essentialocl_CollectionLiteralExp__7420", None)
        self.__7420 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#421"):
                    opp_val = getattr(item, "#421", None)
                    
                    if opp_val == self:
                        setattr(item, "#421", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#421"):
                    opp_val = getattr(item, "#421", None)
                    
                    setattr(item, "#421", self)
                    

class imperativeocl_AnonymousTupleLiteralExp(LiteralExp):

    pass
class qvttemplate_TemplateExp(LiteralExp):

    pass
class OclExpression:

    pass
class essentialocl_IfExp(OclExpression):

    pass
class essentialocl_CallExp(OclExpression):

    pass
class essentialocl_VariableExp(OclExpression):

    pass
class essentialocl_LoopExp(OclExpression, CallExp):

    pass
class essentialocl_TypeExp(OclExpression):

    pass
class essentialocl_LiteralExp(OclExpression):

    pass
class essentialocl_LetExp(OclExpression):

    pass
class imperativeocl_ImperativeExpression(OclExpression):

    pass
class Variable:

    pass
class qvtbase_FunctionParameter(Parameter, Variable):

    pass
class qvtcore_RealizedVariable(Variable):

    pass
class qvtoperational_VarParameter(Parameter, Variable):

    def __init__(self, kind: str, 3239: "ImperativeOperation" = None, 3242: "ImperativeOperation" = None, Variable445: "essentialocl_ExpressionInOcl", #390: "essentialocl_LetExp", Variable404: "essentialocl_VariableExp", Variable327: "qvtbase_Pattern", Variable: "qvttemplate_TemplateExp", Variable357: "qvtrelation_RelationDomain", Variable250: "qvtoperational_ObjectExp", Variable411: "essentialocl_LoopExp", Variable344: "qvtrelation_Relation", Variable439: "essentialocl_ExpressionInOcl", Variable101: "imperativeocl_CollectorExp", Variable36: "imperativeocl_VariableInitExp", Variable442: "essentialocl_ExpressionInOcl", #43: "imperativeocl_ComputeExp", Variable103: "imperativeocl_UnpackExp", Variable78: "imperativeocl_InstantiationExp", Variable20: "imperativeocl_ImperativeIterateExp", Variable418: "essentialocl_IterateExp", #135: "emof_Operation", Parameter: "essentialocl_Variable"):
        self.kind = kind
        self.3239 = 3239
        self.3242 = 3242
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def 3239(self):
        return self.__3239

    @3239.setter
    def 3239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_VarParameter__3239", None)
        self.__3239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#240"):
                opp_val = getattr(old_value, "#240", None)
                if opp_val == self:
                    setattr(old_value, "#240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#240"):
                opp_val = getattr(value, "#240", None)
                setattr(value, "#240", self)

    @property
    def 3242(self):
        return self.__3242

    @3242.setter
    def 3242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_VarParameter__3242", None)
        self.__3242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#243"):
                opp_val = getattr(old_value, "#243", None)
                if opp_val == self:
                    setattr(old_value, "#243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#243"):
                opp_val = getattr(value, "#243", None)
                setattr(value, "#243", self)
