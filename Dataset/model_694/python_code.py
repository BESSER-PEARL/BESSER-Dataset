from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
class SeverityKind(Enum):
    error = "error"
    warning = "warning"
    fatal = "fatal"
class CollectionKind(Enum):
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
    Collection = "Collection"
class ImportKind(Enum):
    extension = "extension"
    access = "access"
class EnforcementMode(Enum):
    Creation = "Creation"
    Deletion = "Deletion"


############################################
# Definition of Classes
############################################

class ResolveExp:

    pass
class QVTOperational_ResolveInExp(ResolveExp):

    pass
class ConstructorBody:

    pass
class InstantiationExp:

    pass
class QVTOperational_ObjectExp(InstantiationExp):

    pass
class ModuleImport:

    pass
class EntryOperation:

    pass
class ModelType:

    pass
class OperationalTransformation:

    pass
class ModelParameter:

    pass
class Module:

    pass
class QVTOperational_OperationalTransformation(Module):

    pass
class QVTOperational_Library(Module):

    pass
class MappingOperation:

    pass
class ImperativeCallExp:

    pass
class QVTOperational_MappingCallExp(ImperativeCallExp):

    def __init__(self, isStrict: str):
        self.isStrict = isStrict
        
    @property
    def isStrict(self) -> str:
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict

class VarParameter:

    pass
class QVTOperational_MappingParameter(VarParameter):

    pass
class QVTOperational_ModelParameter(VarParameter):

    pass
class OperationBody:

    pass
class QVTOperational_MappingBody(OperationBody):

    pass
class QVTOperational_ConstructorBody(OperationBody):

    pass
class ImperativeOperation:

    pass
class QVTOperational_Helper(ImperativeOperation):

    def __init__(self, isQuery: str, #465: "QVTOperational_OperationBody", ImperativeOperation: "QVTOperational_ImperativeOperation", #491: "QVTOperational_VarParameter", #494: "QVTOperational_VarParameter"):
        self.isQuery = isQuery
        
    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

class QVTOperational_EntryOperation(ImperativeOperation):

    pass
class QVTOperational_MappingOperation(ImperativeOperation):

    pass
class QVTOperational_Constructor(ImperativeOperation):

    pass
class CatchExp:

    pass
class AltExp:

    pass
class ImperativeLoopExp:

    pass
class ImperativeOCL_ImperativeIterateExp(ImperativeLoopExp):

    pass
class ImperativeOCL_ForExp(ImperativeLoopExp):

    pass
class DictLiteralPart:

    pass
class DictLiteralExp:

    pass
class ImperativeExpression:

    pass
class ImperativeOCL_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, ImperativeOCL_AssertExp: "OclExpression" = None, ImperativeOCL_AssertExp299: "LogExp" = None):
        self.severity = severity
        self.ImperativeOCL_AssertExp = ImperativeOCL_AssertExp
        self.ImperativeOCL_AssertExp299 = ImperativeOCL_AssertExp299
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def ImperativeOCL_AssertExp(self):
        return self.__ImperativeOCL_AssertExp

    @ImperativeOCL_AssertExp.setter
    def ImperativeOCL_AssertExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssertExp__ImperativeOCL_AssertExp", None)
        self.__ImperativeOCL_AssertExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression297"):
                opp_val = getattr(old_value, "OclExpression297", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression297"):
                opp_val = getattr(value, "OclExpression297", None)
                setattr(value, "OclExpression297", self)

    @property
    def ImperativeOCL_AssertExp299(self):
        return self.__ImperativeOCL_AssertExp299

    @ImperativeOCL_AssertExp299.setter
    def ImperativeOCL_AssertExp299(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssertExp__ImperativeOCL_AssertExp299", None)
        self.__ImperativeOCL_AssertExp299 = value
        
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

class ImperativeOCL_WhileExp(ImperativeExpression):

    pass
class ImperativeOCL_CatchExp(ImperativeExpression):

    pass
class ImperativeOCL_ComputeExp(ImperativeExpression):

    pass
class ImperativeOCL_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: str, ImperativeOCL_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.ImperativeOCL_VariableInitExp = ImperativeOCL_VariableInitExp
        
    @property
    def withResult(self) -> str:
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: str):
        self.__withResult = withResult

    @property
    def ImperativeOCL_VariableInitExp(self):
        return self.__ImperativeOCL_VariableInitExp

    @ImperativeOCL_VariableInitExp.setter
    def ImperativeOCL_VariableInitExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_VariableInitExp__ImperativeOCL_VariableInitExp", None)
        self.__ImperativeOCL_VariableInitExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable380"):
                opp_val = getattr(old_value, "Variable380", None)
                if opp_val == self:
                    setattr(old_value, "Variable380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable380"):
                opp_val = getattr(value, "Variable380", None)
                setattr(value, "Variable380", self)

class ImperativeOCL_TryExp(ImperativeExpression):

    pass
class ImperativeOCL_ContinueExp(ImperativeExpression):

    pass
class ImperativeOCL_RaiseExp(ImperativeExpression):

    pass
class ImperativeOCL_SwitchExp(ImperativeExpression):

    pass
class ImperativeOCL_InstantiationExp(ImperativeExpression):

    pass
class ImperativeOCL_ReturnExp(ImperativeExpression):

    pass
class ImperativeOCL_UnlinkExp(ImperativeExpression):

    pass
class ImperativeOCL_BreakExp(ImperativeExpression):

    pass
class ImperativeOCL_BlockExp(ImperativeExpression):

    pass
class ImperativeOCL_AltExp(ImperativeExpression):

    pass
class Key:

    pass
class ImperativeOCL_AssignExp(ImperativeExpression):

    def __init__(self, isReset: str, ImperativeOCL_AssignExp: "OclExpression" = None, ImperativeOCL_AssignExp303: "OclExpression" = None, ImperativeOCL_AssignExp306: set["OclExpression"] = None):
        self.isReset = isReset
        self.ImperativeOCL_AssignExp = ImperativeOCL_AssignExp
        self.ImperativeOCL_AssignExp303 = ImperativeOCL_AssignExp303
        self.ImperativeOCL_AssignExp306 = ImperativeOCL_AssignExp306 if ImperativeOCL_AssignExp306 is not None else set()
        
    @property
    def isReset(self) -> str:
        return self.__isReset

    @isReset.setter
    def isReset(self, isReset: str):
        self.__isReset = isReset

    @property
    def ImperativeOCL_AssignExp(self):
        return self.__ImperativeOCL_AssignExp

    @ImperativeOCL_AssignExp.setter
    def ImperativeOCL_AssignExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssignExp__ImperativeOCL_AssignExp", None)
        self.__ImperativeOCL_AssignExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression301"):
                opp_val = getattr(old_value, "OclExpression301", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression301"):
                opp_val = getattr(value, "OclExpression301", None)
                setattr(value, "OclExpression301", self)

    @property
    def ImperativeOCL_AssignExp303(self):
        return self.__ImperativeOCL_AssignExp303

    @ImperativeOCL_AssignExp303.setter
    def ImperativeOCL_AssignExp303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssignExp__ImperativeOCL_AssignExp303", None)
        self.__ImperativeOCL_AssignExp303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression304"):
                opp_val = getattr(old_value, "OclExpression304", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression304"):
                opp_val = getattr(value, "OclExpression304", None)
                setattr(value, "OclExpression304", self)

    @property
    def ImperativeOCL_AssignExp306(self):
        return self.__ImperativeOCL_AssignExp306

    @ImperativeOCL_AssignExp306.setter
    def ImperativeOCL_AssignExp306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssignExp__ImperativeOCL_AssignExp306", None)
        self.__ImperativeOCL_AssignExp306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression307"):
                    opp_val = getattr(item, "OclExpression307", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression307"):
                    opp_val = getattr(item, "OclExpression307", None)
                    
                    setattr(item, "OclExpression307", self)
                    

class LogExp:

    pass
class DomainPattern:

    pass
class RelationDomainAssignment:

    pass
class RelationImplementation:

    pass
class PropertyCallExp:

    pass
class QVTRelation_OppositePropertyCallExp(PropertyCallExp):

    pass
class Relation:

    pass
class RelationDomain:

    pass
class RelationalTransformation:

    pass
class PropertyTemplateItem:

    pass
class TemplateExp:

    pass
class QVTTemplate_ObjectTemplateExp(TemplateExp):

    pass
class QVTTemplate_CollectionTemplateExp(TemplateExp):

    pass
class ObjectTemplateExp:

    pass
class Mapping:

    pass
class RealizedVariable:

    pass
class EnforcementOperation:

    pass
class Assignment:

    pass
class QVTCore_PropertyAssignment(Assignment):

    pass
class QVTCore_VariableAssignment(Assignment):

    pass
class Area:

    pass
class CorePattern:

    pass
class QVTCore_BottomPattern(CorePattern):

    pass
class QVTCore_GuardPattern(CorePattern):

    pass
class OperationCallExp:

    pass
class QVTOperational_ImperativeCallExp(ImperativeExpression, OperationCallExp):

    def __init__(self, isVirtual: str, OperationCallExp: "QVTCore_EnforcementOperation"):
        self.isVirtual = isVirtual
        
    @property
    def isVirtual(self) -> str:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: str):
        self.__isVirtual = isVirtual

class ImperativeOCL_LogExp(ImperativeExpression, OperationCallExp):

    pass
class Tag:

    pass
class GuardPattern:

    pass
class BottomPattern:

    pass
class QVTCore_Area(ABC):

    pass
class Domain:

    pass
class QVTCore_CoreDomain(Domain, Area):

    pass
class QVTRelation_RelationDomain(Domain):

    pass
class Pattern:

    pass
class QVTRelation_DomainPattern(Pattern):

    pass
class QVTCore_CorePattern(Pattern):

    pass
class Predicate:

    pass
class Transformation:

    pass
class QVTRelation_RelationalTransformation(Transformation):

    pass
class Rule:

    pass
class QVTCore_Mapping(Rule, Area):

    pass
class QVTRelation_Relation(Rule):

    def __init__(self, isTopLevel: str, 6251: set["RelationImplementation"] = None, QVTRelation_Relation: set["Variable"] = None, QVTRelation_Relation256: "Pattern" = None, QVTRelation_Relation258: "Pattern" = None, #150: "QVTBase_Transformation", Rule: "QVTBase_Rule", #121: "QVTBase_Domain"):
        self.isTopLevel = isTopLevel
        self.6251 = 6251 if 6251 is not None else set()
        self.QVTRelation_Relation = QVTRelation_Relation if QVTRelation_Relation is not None else set()
        self.QVTRelation_Relation256 = QVTRelation_Relation256
        self.QVTRelation_Relation258 = QVTRelation_Relation258
        
    @property
    def isTopLevel(self) -> str:
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: str):
        self.__isTopLevel = isTopLevel

    @property
    def QVTRelation_Relation258(self):
        return self.__QVTRelation_Relation258

    @QVTRelation_Relation258.setter
    def QVTRelation_Relation258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTRelation_Relation__QVTRelation_Relation258", None)
        self.__QVTRelation_Relation258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern259"):
                opp_val = getattr(old_value, "Pattern259", None)
                if opp_val == self:
                    setattr(old_value, "Pattern259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern259"):
                opp_val = getattr(value, "Pattern259", None)
                setattr(value, "Pattern259", self)

    @property
    def 6251(self):
        return self.__6251

    @6251.setter
    def 6251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTRelation_Relation__6251", None)
        self.__6251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#252"):
                    opp_val = getattr(item, "#252", None)
                    
                    if opp_val == self:
                        setattr(item, "#252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#252"):
                    opp_val = getattr(item, "#252", None)
                    
                    setattr(item, "#252", self)
                    

    @property
    def QVTRelation_Relation256(self):
        return self.__QVTRelation_Relation256

    @QVTRelation_Relation256.setter
    def QVTRelation_Relation256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTRelation_Relation__QVTRelation_Relation256", None)
        self.__QVTRelation_Relation256 = value
        
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
    def QVTRelation_Relation(self):
        return self.__QVTRelation_Relation

    @QVTRelation_Relation.setter
    def QVTRelation_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTRelation_Relation__QVTRelation_Relation", None)
        self.__QVTRelation_Relation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable254"):
                    opp_val = getattr(item, "Variable254", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable254"):
                    opp_val = getattr(item, "Variable254", None)
                    
                    setattr(item, "Variable254", self)
                    

class LetExp:

    pass
class TypedModel:

    pass
class TupleLiteralPart:

    pass
class NavigationCallExp:

    pass
class EssentialOCL_PropertyCallExp(NavigationCallExp):

    pass
class TupleLiteralExp:

    pass
class LoopExp:

    pass
class EssentialOCL_IteratorExp(LoopExp):

    pass
class ImperativeOCL_ImperativeLoopExp(LoopExp, ImperativeExpression):

    pass
class EssentialOCL_IterateExp(LoopExp):

    pass
class NumericLiteralExp:

    pass
class EssentialOCL_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class EssentialOCL_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class EssentialOCL_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class FeatureCallExp:

    pass
class EssentialOCL_OperationCallExp(FeatureCallExp):

    pass
class EssentialOCL_NavigationCallExp(FeatureCallExp):

    pass
class Variable:

    pass
class QVTCore_RealizedVariable(Variable):

    pass
class CallExp:

    pass
class QVTOperational_ResolveExp(ImperativeExpression, CallExp):

    def __init__(self, isDeferred: str, isInverse: str, one: str, QVTOperational_ResolveExp: "OclExpression" = None, QVTOperational_ResolveExp485: "Variable" = None):
        self.isDeferred = isDeferred
        self.isInverse = isInverse
        self.one = one
        self.QVTOperational_ResolveExp = QVTOperational_ResolveExp
        self.QVTOperational_ResolveExp485 = QVTOperational_ResolveExp485
        
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
    def QVTOperational_ResolveExp485(self):
        return self.__QVTOperational_ResolveExp485

    @QVTOperational_ResolveExp485.setter
    def QVTOperational_ResolveExp485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ResolveExp__QVTOperational_ResolveExp485", None)
        self.__QVTOperational_ResolveExp485 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable486"):
                opp_val = getattr(old_value, "Variable486", None)
                if opp_val == self:
                    setattr(old_value, "Variable486", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable486"):
                opp_val = getattr(value, "Variable486", None)
                setattr(value, "Variable486", self)

    @property
    def QVTOperational_ResolveExp(self):
        return self.__QVTOperational_ResolveExp

    @QVTOperational_ResolveExp.setter
    def QVTOperational_ResolveExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ResolveExp__QVTOperational_ResolveExp", None)
        self.__QVTOperational_ResolveExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression483"):
                opp_val = getattr(old_value, "OclExpression483", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression483", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression483"):
                opp_val = getattr(value, "OclExpression483", None)
                setattr(value, "OclExpression483", self)

class EssentialOCL_FeatureCallExp(CallExp):

    pass
class CollectionLiteralExp:

    pass
class LiteralExp:

    pass
class QVTTemplate_TemplateExp(LiteralExp):

    pass
class EssentialOCL_NullLiteralExp(LiteralExp):

    pass
class EssentialOCL_TupleLiteralExp(LiteralExp):

    pass
class EssentialOCL_PrimitiveLiteralExp(LiteralExp):

    pass
class ImperativeOCL_ListLiteralExp(LiteralExp):

    pass
class ImperativeOCL_DictLiteralExp(LiteralExp):

    pass
class EssentialOCL_InvalidLiteralExp(LiteralExp):

    pass
class EssentialOCL_EnumLiteralExp(LiteralExp):

    pass
class EssentialOCL_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, 2: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.2 = 2 if 2 is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def 2(self):
        return self.__2

    @2.setter
    def 2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EssentialOCL_CollectionLiteralExp__2", None)
        self.__2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#47"):
                    opp_val = getattr(item, "#47", None)
                    
                    if opp_val == self:
                        setattr(item, "#47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#47"):
                    opp_val = getattr(item, "#47", None)
                    
                    setattr(item, "#47", self)
                    

class CollectionType:

    pass
class EssentialOCL_SetType(CollectionType):

    pass
class EssentialOCL_OrderedSetType(CollectionType):

    pass
class EssentialOCL_SequenceType(CollectionType):

    pass
class ImperativeOCL_ListType(CollectionType):

    pass
class ImperativeOCL_DictionaryType(CollectionType):

    pass
class EssentialOCL_BagType(CollectionType):

    pass
class Extent:

    pass
class EMOF_URIExtent(Extent):

    def __init__(self):
        
    def uri(self, element: str) -> str:
        # TODO: Implement uri method
        pass

    def contextURI(self) -> str:
        # TODO: Implement contextURI method
        pass

    def element(self, uri: str) -> str:
        # TODO: Implement element method
        pass

class CollectionLiteralPart:

    pass
class EssentialOCL_CollectionRange(CollectionLiteralPart):

    pass
class EssentialOCL_CollectionItem(CollectionLiteralPart):

    pass
class OclExpression:

    pass
class ImperativeOCL_ImperativeExpression(OclExpression):

    pass
class EssentialOCL_TypeExp(OclExpression):

    pass
class QVTRelation_RelationCallExp(OclExpression):

    pass
class EssentialOCL_VariableExp(OclExpression):

    pass
class EssentialOCL_LoopExp(CallExp, OclExpression):

    pass
class EssentialOCL_LetExp(OclExpression):

    pass
class EssentialOCL_LiteralExp(OclExpression):

    pass
class EssentialOCL_IfExp(OclExpression):

    pass
class EssentialOCL_CallExp(OclExpression):

    pass
class PrimitiveLiteralExp:

    pass
class EssentialOCL_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class EssentialOCL_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class EssentialOCL_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class ReflectiveCollection:

    pass
class EMOF_ReflectiveSequence(ReflectiveCollection):

    def __init__(self):
        
    def remove(self, index: str) -> str:
        # TODO: Implement remove method
        pass

    def get(self, index: str) -> str:
        # TODO: Implement get method
        pass

    def add(self, object: str, index: str):
        # TODO: Implement add method
        pass

    def set(self, index: str, object: str) -> str:
        # TODO: Implement set method
        pass

class Parameter:

    pass
class QVTOperational_VarParameter(Parameter, Variable):

    def __init__(self, kind: str, 8490: "ImperativeOperation" = None, 8493: "ImperativeOperation" = None, #19: "EMOF_Operation", Parameter: "EssentialOCL_Variable", Variable218: "QVTTemplate_CollectionTemplateExp", Variable447: "QVTOperational_Module", Variable468: "QVTOperational_OperationBody", Variable71: "EssentialOCL_ExpressionInOcl", Variable182: "QVTCore_CorePattern", Variable232: "QVTTemplate_TemplateExp", #86: "EssentialOCL_LetExp", Variable68: "EssentialOCL_ExpressionInOcl", Variable271: "QVTRelation_RelationDomain", Variable343: "ImperativeOCL_InstantiationExp", Variable317: "ImperativeOCL_CatchExp", Variable211: "QVTCore_VariableAssignment", Variable81: "EssentialOCL_IterateExp", Variable336: "ImperativeOCL_ImperativeIterateExp", Variable119: "EssentialOCL_VariableExp", Variable126: "QVTBase_Pattern", Variable91: "EssentialOCL_LoopExp", Variable279: "QVTRelation_RelationDomainAssignment", Variable460: "QVTOperational_ObjectExp", Variable380: "ImperativeOCL_VariableInitExp", Variable254: "QVTRelation_Relation", Variable486: "QVTOperational_ResolveExp", Variable322: "ImperativeOCL_ComputeExp", Variable: "EssentialOCL_ExpressionInOcl"):
        self.kind = kind
        self.8490 = 8490
        self.8493 = 8493
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def 8493(self):
        return self.__8493

    @8493.setter
    def 8493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_VarParameter__8493", None)
        self.__8493 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#494"):
                opp_val = getattr(old_value, "#494", None)
                if opp_val == self:
                    setattr(old_value, "#494", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#494"):
                opp_val = getattr(value, "#494", None)
                setattr(value, "#494", self)

    @property
    def 8490(self):
        return self.__8490

    @8490.setter
    def 8490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_VarParameter__8490", None)
        self.__8490 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#491"):
                opp_val = getattr(old_value, "#491", None)
                if opp_val == self:
                    setattr(old_value, "#491", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#491"):
                opp_val = getattr(value, "#491", None)
                setattr(value, "#491", self)

class QVTBase_FunctionParameter(Parameter, Variable):

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class EssentialOCL_ExpressionInOcl(TypedElement):

    pass
class EssentialOCL_CollectionLiteralPart(TypedElement):

    pass
class EssentialOCL_OclExpression(TypedElement):

    pass
class EMOF_Property(MultiplicityElement, TypedElement):

    def __init__(self, default: str, isComposite: str, isDerived: str, isID: str, isReadOnly: str, 134: "Class" = None, EMOF_Property: "Property" = None):
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.isReadOnly = isReadOnly
        self.134 = 134
        self.EMOF_Property = EMOF_Property
        
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
    def isID(self) -> str:
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID

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
    def 134(self):
        return self.__134

    @134.setter
    def 134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Property__134", None)
        self.__134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#35"):
                opp_val = getattr(old_value, "#35", None)
                if opp_val == self:
                    setattr(old_value, "#35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#35"):
                opp_val = getattr(value, "#35", None)
                setattr(value, "#35", self)

    @property
    def EMOF_Property(self):
        return self.__EMOF_Property

    @EMOF_Property.setter
    def EMOF_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Property__EMOF_Property", None)
        self.__EMOF_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property"):
                opp_val = getattr(old_value, "Property", None)
                if opp_val == self:
                    setattr(old_value, "Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property"):
                opp_val = getattr(value, "Property", None)
                setattr(value, "Property", self)

class EssentialOCL_Variable(TypedElement):

    pass
class EssentialOCL_TupleLiteralPart(TypedElement):

    pass
class EMOF_Operation(MultiplicityElement, TypedElement):

    pass
class EMOF_Object:

    pass
class EMOF_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def isOrdered(self) -> str:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: str):
        self.__isOrdered = isOrdered

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

class EMOF_Parameter(MultiplicityElement, TypedElement):

    pass
class EnumerationLiteral:

    pass
class DataType:

    pass
class EMOF_PrimitiveType(DataType):

    pass
class EssentialOCL_CollectionType(DataType):

    pass
class EMOF_Enumeration(DataType):

    pass
class Comment:

    pass
class Package:

    pass
class Enumeration:

    pass
class Operation:

    pass
class QVTOperational_ImperativeOperation(Operation):

    def __init__(self, isBlackbox: str, QVTOperational_ImperativeOperation: "ImperativeOperation" = None, 8401: set["VarParameter"] = None, 8: "OperationBody" = None, 8397: "VarParameter" = None, Operation: "EssentialOCL_OperationCallExp", Operation281: "QVTRelation_RelationImplementation", #3: "EMOF_Class", Operation349: "ImperativeOCL_InstantiationExp", #32: "EMOF_Parameter"):
        self.isBlackbox = isBlackbox
        self.QVTOperational_ImperativeOperation = QVTOperational_ImperativeOperation
        self.8401 = 8401 if 8401 is not None else set()
        self.8 = 8
        self.8397 = 8397
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

    @property
    def 8397(self):
        return self.__8397

    @8397.setter
    def 8397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__8397", None)
        self.__8397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#398"):
                opp_val = getattr(old_value, "#398", None)
                if opp_val == self:
                    setattr(old_value, "#398", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#398"):
                opp_val = getattr(value, "#398", None)
                setattr(value, "#398", self)

    @property
    def 8(self):
        return self.__8

    @8.setter
    def 8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__8", None)
        self.__8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#395"):
                opp_val = getattr(old_value, "#395", None)
                if opp_val == self:
                    setattr(old_value, "#395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#395"):
                opp_val = getattr(value, "#395", None)
                setattr(value, "#395", self)

    @property
    def QVTOperational_ImperativeOperation(self):
        return self.__QVTOperational_ImperativeOperation

    @QVTOperational_ImperativeOperation.setter
    def QVTOperational_ImperativeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation", None)
        self.__QVTOperational_ImperativeOperation = value
        
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
    def 8401(self):
        return self.__8401

    @8401.setter
    def 8401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__8401", None)
        self.__8401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#402"):
                    opp_val = getattr(item, "#402", None)
                    
                    if opp_val == self:
                        setattr(item, "#402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#402"):
                    opp_val = getattr(item, "#402", None)
                    
                    setattr(item, "#402", self)
                    

class QVTBase_Function(Operation):

    pass
class Property:

    pass
class QVTOperational_ContextualProperty(Property):

    pass
class Type:

    pass
class EssentialOCL_InvalidType(Type):

    pass
class EssentialOCL_VoidType(Type):

    pass
class EssentialOCL_AnyType(Type):

    pass
class EssentialOCL_TemplateParameterType(Type):

    def __init__(self, specification: str, Type57: "EssentialOCL_CollectionType", Type370: "ImperativeOCL_Typedef", Type358: "ImperativeOCL_RaiseExp", #29: "EMOF_Package", Type65: "EssentialOCL_ExpressionInOcl", Type314: "ImperativeOCL_CatchExp", Type110: "EssentialOCL_TypeExp", Type: "EMOF_Operation", Type42: "EMOF_TypedElement", Type334: "ImperativeOCL_DictionaryType"):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class EMOF_Class(Type):

    def __init__(self, isAbstract: str, EMOF_Class: set["Class"] = None, 1: set["Property"] = None, 12: set["Operation"] = None, Type57: "EssentialOCL_CollectionType", Type370: "ImperativeOCL_Typedef", Type358: "ImperativeOCL_RaiseExp", #29: "EMOF_Package", Type65: "EssentialOCL_ExpressionInOcl", Type314: "ImperativeOCL_CatchExp", Type110: "EssentialOCL_TypeExp", Type: "EMOF_Operation", Type42: "EMOF_TypedElement", Type334: "ImperativeOCL_DictionaryType"):
        self.isAbstract = isAbstract
        self.EMOF_Class = EMOF_Class if EMOF_Class is not None else set()
        self.1 = 1 if 1 is not None else set()
        self.12 = 12 if 12 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def EMOF_Class(self):
        return self.__EMOF_Class

    @EMOF_Class.setter
    def EMOF_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Class__EMOF_Class", None)
        self.__EMOF_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    if opp_val == self:
                        setattr(item, "Class", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Class"):
                    opp_val = getattr(item, "Class", None)
                    
                    setattr(item, "Class", self)
                    

    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Class__12", None)
        self.__12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#3"):
                    opp_val = getattr(item, "#3", None)
                    
                    if opp_val == self:
                        setattr(item, "#3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#3"):
                    opp_val = getattr(item, "#3", None)
                    
                    setattr(item, "#3", self)
                    

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Class__1", None)
        self.__1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    if opp_val == self:
                        setattr(item, "#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    setattr(item, "#", self)
                    

class Object:

    pass
class EMOF_ReflectiveCollection(Object):

    def __init__(self):
        
    def add(self, object: str) -> str:
        # TODO: Implement add method
        pass

    def addAll(self, objects: str) -> str:
        # TODO: Implement addAll method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def remove(self, object: str) -> str:
        # TODO: Implement remove method
        pass

    def size(self) -> str:
        # TODO: Implement size method
        pass

class EMOF_Extent(Object):

    def __init__(self):
        
    def useContainment(self) -> str:
        # TODO: Implement useContainment method
        pass

    def elements(self) -> str:
        # TODO: Implement elements method
        pass

class EMOF_Element(Object):

    def __init__(self, EMOF_Element: set["Comment"] = None):
        self.EMOF_Element = EMOF_Element if EMOF_Element is not None else set()
        
    @property
    def EMOF_Element(self):
        return self.__EMOF_Element

    @EMOF_Element.setter
    def EMOF_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Element__EMOF_Element", None)
        self.__EMOF_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

    def set(self, property: str, object: str):
        # TODO: Implement set method
        pass

    def unset(self, property: str):
        # TODO: Implement unset method
        pass

    def getMetaClass(self) -> str:
        # TODO: Implement getMetaClass method
        pass

    def isSet(self, property: str) -> str:
        # TODO: Implement isSet method
        pass

    def equals(self, object: str) -> str:
        # TODO: Implement equals method
        pass

    def get(self, property: str) -> str:
        # TODO: Implement get method
        pass

    def container(self) -> str:
        # TODO: Implement container method
        pass

class EMOF_DataType(Type):

    pass
class NamedElement:

    pass
class QVTBase_Rule(NamedElement):

    pass
class EMOF_TypedElement(NamedElement):

    pass
class EMOF_Type(NamedElement):

    def __init__(self, 139: "Package" = None, NamedElement: "EMOF_Comment"):
        self.139 = 139
        
    @property
    def 139(self):
        return self.__139

    @139.setter
    def 139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Type__139", None)
        self.__139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#40"):
                opp_val = getattr(old_value, "#40", None)
                if opp_val == self:
                    setattr(old_value, "#40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#40"):
                opp_val = getattr(value, "#40", None)
                setattr(value, "#40", self)

    def isInstance(self, object: str) -> str:
        # TODO: Implement isInstance method
        pass

class QVTBase_Domain(NamedElement):

    def __init__(self, isCheckable: str, isEnforceable: str, QVTBase_Domain: "TypedModel" = None, 3: "Rule" = None, NamedElement: "EMOF_Comment"):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.QVTBase_Domain = QVTBase_Domain
        self.3 = 3
        
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
    def QVTBase_Domain(self):
        return self.__QVTBase_Domain

    @QVTBase_Domain.setter
    def QVTBase_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTBase_Domain__QVTBase_Domain", None)
        self.__QVTBase_Domain = value
        
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

    @property
    def 3(self):
        return self.__3

    @3.setter
    def 3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTBase_Domain__3", None)
        self.__3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#121"):
                opp_val = getattr(old_value, "#121", None)
                if opp_val == self:
                    setattr(old_value, "#121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#121"):
                opp_val = getattr(value, "#121", None)
                setattr(value, "#121", self)

class EMOF_EnumerationLiteral(NamedElement):

    pass
class EMOF_Package(NamedElement):

    def __init__(self, uri: str, 122: set["Package"] = None, 125: "Package" = None, 128: set["Type"] = None, NamedElement: "EMOF_Comment"):
        self.uri = uri
        self.122 = 122 if 122 is not None else set()
        self.125 = 125
        self.128 = 128 if 128 is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def 122(self):
        return self.__122

    @122.setter
    def 122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__122", None)
        self.__122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#23"):
                    opp_val = getattr(item, "#23", None)
                    
                    if opp_val == self:
                        setattr(item, "#23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#23"):
                    opp_val = getattr(item, "#23", None)
                    
                    setattr(item, "#23", self)
                    

    @property
    def 125(self):
        return self.__125

    @125.setter
    def 125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__125", None)
        self.__125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#26"):
                opp_val = getattr(old_value, "#26", None)
                if opp_val == self:
                    setattr(old_value, "#26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#26"):
                opp_val = getattr(value, "#26", None)
                setattr(value, "#26", self)

    @property
    def 128(self):
        return self.__128

    @128.setter
    def 128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__128", None)
        self.__128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#29"):
                    opp_val = getattr(item, "#29", None)
                    
                    if opp_val == self:
                        setattr(item, "#29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#29"):
                    opp_val = getattr(item, "#29", None)
                    
                    setattr(item, "#29", self)
                    

class QVTBase_TypedModel(NamedElement):

    pass
class Element:

    pass
class QVTTemplate_PropertyTemplateItem(Element):

    def __init__(self, isOpposite: str, 5224: "ObjectTemplateExp" = None, QVTTemplate_PropertyTemplateItem: "Property" = None, QVTTemplate_PropertyTemplateItem229: "OclExpression" = None, Element: "EMOF_Tag"):
        self.isOpposite = isOpposite
        self.5224 = 5224
        self.QVTTemplate_PropertyTemplateItem = QVTTemplate_PropertyTemplateItem
        self.QVTTemplate_PropertyTemplateItem229 = QVTTemplate_PropertyTemplateItem229
        
    @property
    def isOpposite(self) -> str:
        return self.__isOpposite

    @isOpposite.setter
    def isOpposite(self, isOpposite: str):
        self.__isOpposite = isOpposite

    @property
    def 5224(self):
        return self.__5224

    @5224.setter
    def 5224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTTemplate_PropertyTemplateItem__5224", None)
        self.__5224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#225"):
                opp_val = getattr(old_value, "#225", None)
                if opp_val == self:
                    setattr(old_value, "#225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#225"):
                opp_val = getattr(value, "#225", None)
                setattr(value, "#225", self)

    @property
    def QVTTemplate_PropertyTemplateItem229(self):
        return self.__QVTTemplate_PropertyTemplateItem229

    @QVTTemplate_PropertyTemplateItem229.setter
    def QVTTemplate_PropertyTemplateItem229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTTemplate_PropertyTemplateItem__QVTTemplate_PropertyTemplateItem229", None)
        self.__QVTTemplate_PropertyTemplateItem229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression230"):
                opp_val = getattr(old_value, "OclExpression230", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression230"):
                opp_val = getattr(value, "OclExpression230", None)
                setattr(value, "OclExpression230", self)

    @property
    def QVTTemplate_PropertyTemplateItem(self):
        return self.__QVTTemplate_PropertyTemplateItem

    @QVTTemplate_PropertyTemplateItem.setter
    def QVTTemplate_PropertyTemplateItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTTemplate_PropertyTemplateItem__QVTTemplate_PropertyTemplateItem", None)
        self.__QVTTemplate_PropertyTemplateItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property227"):
                opp_val = getattr(old_value, "Property227", None)
                if opp_val == self:
                    setattr(old_value, "Property227", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property227"):
                opp_val = getattr(value, "Property227", None)
                setattr(value, "Property227", self)

class QVTCore_Assignment(Element):

    def __init__(self, isDefault: str, 4165: "BottomPattern" = None, QVTCore_Assignment: "OclExpression" = None, Element: "EMOF_Tag"):
        self.isDefault = isDefault
        self.4165 = 4165
        self.QVTCore_Assignment = QVTCore_Assignment
        
    @property
    def isDefault(self) -> str:
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: str):
        self.__isDefault = isDefault

    @property
    def 4165(self):
        return self.__4165

    @4165.setter
    def 4165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTCore_Assignment__4165", None)
        self.__4165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#166"):
                opp_val = getattr(old_value, "#166", None)
                if opp_val == self:
                    setattr(old_value, "#166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#166"):
                opp_val = getattr(value, "#166", None)
                setattr(value, "#166", self)

    @property
    def QVTCore_Assignment(self):
        return self.__QVTCore_Assignment

    @QVTCore_Assignment.setter
    def QVTCore_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTCore_Assignment__QVTCore_Assignment", None)
        self.__QVTCore_Assignment = value
        
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

class ImperativeOCL_DictLiteralPart(Element):

    pass
class EMOF_Factory(Element):

    def __init__(self, EMOF_Factory: "Package" = None, Element: "EMOF_Tag"):
        self.EMOF_Factory = EMOF_Factory
        
    @property
    def EMOF_Factory(self):
        return self.__EMOF_Factory

    @EMOF_Factory.setter
    def EMOF_Factory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Factory__EMOF_Factory", None)
        self.__EMOF_Factory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package"):
                opp_val = getattr(old_value, "Package", None)
                if opp_val == self:
                    setattr(old_value, "Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package"):
                opp_val = getattr(value, "Package", None)
                setattr(value, "Package", self)

    def createFromString(self, string: str, dataType: str) -> str:
        # TODO: Implement createFromString method
        pass

    def create(self, metaClass: str) -> str:
        # TODO: Implement create method
        pass

    def convertToString(self, dataType: str, object: str) -> str:
        # TODO: Implement convertToString method
        pass

class EMOF_NamedElement(Element):

    def __init__(self, name: str, Element: "EMOF_Tag"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class QVTOperational_OperationBody(Element):

    pass
class QVTOperational_ModuleImport(Element):

    def __init__(self, kind: str, QVTOperational_ModuleImport: set["ModelType"] = None, QVTOperational_ModuleImport453: "Module" = None, 8455: "Module" = None, Element: "EMOF_Tag"):
        self.kind = kind
        self.QVTOperational_ModuleImport = QVTOperational_ModuleImport if QVTOperational_ModuleImport is not None else set()
        self.QVTOperational_ModuleImport453 = QVTOperational_ModuleImport453
        self.8455 = 8455
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def QVTOperational_ModuleImport453(self):
        return self.__QVTOperational_ModuleImport453

    @QVTOperational_ModuleImport453.setter
    def QVTOperational_ModuleImport453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__QVTOperational_ModuleImport453", None)
        self.__QVTOperational_ModuleImport453 = value
        
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
    def QVTOperational_ModuleImport(self):
        return self.__QVTOperational_ModuleImport

    @QVTOperational_ModuleImport.setter
    def QVTOperational_ModuleImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__QVTOperational_ModuleImport", None)
        self.__QVTOperational_ModuleImport = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelType451"):
                    opp_val = getattr(item, "ModelType451", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType451", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType451"):
                    opp_val = getattr(item, "ModelType451", None)
                    
                    setattr(item, "ModelType451", self)
                    

    @property
    def 8455(self):
        return self.__8455

    @8455.setter
    def 8455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__8455", None)
        self.__8455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#456"):
                opp_val = getattr(old_value, "#456", None)
                if opp_val == self:
                    setattr(old_value, "#456", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#456"):
                opp_val = getattr(value, "#456", None)
                setattr(value, "#456", self)

class QVTRelation_RelationImplementation(Element):

    pass
class QVTRelation_RelationDomainAssignment(Element):

    pass
class EMOF_Tag(Element):

    def __init__(self, name: str, value: str, EMOF_Tag: set["Element"] = None, Element: "EMOF_Tag"):
        self.name = name
        self.value = value
        self.EMOF_Tag = EMOF_Tag if EMOF_Tag is not None else set()
        
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
    def EMOF_Tag(self):
        return self.__EMOF_Tag

    @EMOF_Tag.setter
    def EMOF_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Tag__EMOF_Tag", None)
        self.__EMOF_Tag = value if value is not None else set()
        
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
                    

class QVTBase_Predicate(Element):

    pass
class QVTCore_EnforcementOperation(Element):

    def __init__(self, enforcementMode: str, 4184: "BottomPattern" = None, QVTCore_EnforcementOperation: "OperationCallExp" = None, Element: "EMOF_Tag"):
        self.enforcementMode = enforcementMode
        self.4184 = 4184
        self.QVTCore_EnforcementOperation = QVTCore_EnforcementOperation
        
    @property
    def enforcementMode(self) -> str:
        return self.__enforcementMode

    @enforcementMode.setter
    def enforcementMode(self, enforcementMode: str):
        self.__enforcementMode = enforcementMode

    @property
    def 4184(self):
        return self.__4184

    @4184.setter
    def 4184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTCore_EnforcementOperation__4184", None)
        self.__4184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#185"):
                opp_val = getattr(old_value, "#185", None)
                if opp_val == self:
                    setattr(old_value, "#185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#185"):
                opp_val = getattr(value, "#185", None)
                setattr(value, "#185", self)

    @property
    def QVTCore_EnforcementOperation(self):
        return self.__QVTCore_EnforcementOperation

    @QVTCore_EnforcementOperation.setter
    def QVTCore_EnforcementOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTCore_EnforcementOperation__QVTCore_EnforcementOperation", None)
        self.__QVTCore_EnforcementOperation = value
        
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

class QVTBase_Pattern(Element):

    pass
class QVTRelation_Key(Element):

    pass
class EMOF_Comment(Element):

    def __init__(self, body: str, EMOF_Comment: set["NamedElement"] = None, Element: "EMOF_Tag"):
        self.body = body
        self.EMOF_Comment = EMOF_Comment if EMOF_Comment is not None else set()
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def EMOF_Comment(self):
        return self.__EMOF_Comment

    @EMOF_Comment.setter
    def EMOF_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Comment__EMOF_Comment", None)
        self.__EMOF_Comment = value if value is not None else set()
        
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
                    

class Class:

    pass
class ImperativeOCL_Typedef(Class):

    pass
class QVTOperational_Module(Class, Package):

    def __init__(self, isBlackbox: str, QVTOperational_Module: set["Property"] = None, QVTOperational_Module449: set["ModelType"] = None, QVTOperational_Module438: "EntryOperation" = None, 8440: set["ModuleImport"] = None, QVTOperational_Module443: set["Tag"] = None, QVTOperational_Module446: set["Variable"] = None, Class387: "QVTOperational_ContextualProperty", #35: "EMOF_Property", #16: "EMOF_Operation", Class346: "ImperativeOCL_InstantiationExp", Class470: "QVTOperational_OperationalTransformation", Class222: "QVTTemplate_ObjectTemplateExp", Class: "EMOF_Class", Class240: "QVTRelation_Key", #40: "EMOF_Type", Package434: "QVTOperational_ModelType", Package: "EMOF_Factory", #26: "EMOF_Package", Package158: "QVTBase_TypedModel", #23: "EMOF_Package"):
        self.isBlackbox = isBlackbox
        self.QVTOperational_Module = QVTOperational_Module if QVTOperational_Module is not None else set()
        self.QVTOperational_Module449 = QVTOperational_Module449 if QVTOperational_Module449 is not None else set()
        self.QVTOperational_Module438 = QVTOperational_Module438
        self.8440 = 8440 if 8440 is not None else set()
        self.QVTOperational_Module443 = QVTOperational_Module443 if QVTOperational_Module443 is not None else set()
        self.QVTOperational_Module446 = QVTOperational_Module446 if QVTOperational_Module446 is not None else set()
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

    @property
    def QVTOperational_Module(self):
        return self.__QVTOperational_Module

    @QVTOperational_Module.setter
    def QVTOperational_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module", None)
        self.__QVTOperational_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property436"):
                    opp_val = getattr(item, "Property436", None)
                    
                    if opp_val == self:
                        setattr(item, "Property436", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property436"):
                    opp_val = getattr(item, "Property436", None)
                    
                    setattr(item, "Property436", self)
                    

    @property
    def QVTOperational_Module449(self):
        return self.__QVTOperational_Module449

    @QVTOperational_Module449.setter
    def QVTOperational_Module449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module449", None)
        self.__QVTOperational_Module449 = value if value is not None else set()
        
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
    def QVTOperational_Module443(self):
        return self.__QVTOperational_Module443

    @QVTOperational_Module443.setter
    def QVTOperational_Module443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module443", None)
        self.__QVTOperational_Module443 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tag444"):
                    opp_val = getattr(item, "Tag444", None)
                    
                    if opp_val == self:
                        setattr(item, "Tag444", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tag444"):
                    opp_val = getattr(item, "Tag444", None)
                    
                    setattr(item, "Tag444", self)
                    

    @property
    def QVTOperational_Module446(self):
        return self.__QVTOperational_Module446

    @QVTOperational_Module446.setter
    def QVTOperational_Module446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module446", None)
        self.__QVTOperational_Module446 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable447"):
                    opp_val = getattr(item, "Variable447", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable447", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable447"):
                    opp_val = getattr(item, "Variable447", None)
                    
                    setattr(item, "Variable447", self)
                    

    @property
    def 8440(self):
        return self.__8440

    @8440.setter
    def 8440(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__8440", None)
        self.__8440 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#441"):
                    opp_val = getattr(item, "#441", None)
                    
                    if opp_val == self:
                        setattr(item, "#441", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#441"):
                    opp_val = getattr(item, "#441", None)
                    
                    setattr(item, "#441", self)
                    

    @property
    def QVTOperational_Module438(self):
        return self.__QVTOperational_Module438

    @QVTOperational_Module438.setter
    def QVTOperational_Module438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module438", None)
        self.__QVTOperational_Module438 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntryOperation"):
                opp_val = getattr(old_value, "EntryOperation", None)
                if opp_val == self:
                    setattr(old_value, "EntryOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntryOperation"):
                opp_val = getattr(value, "EntryOperation", None)
                setattr(value, "EntryOperation", self)

class QVTOperational_ModelType(Class):

    def __init__(self, conformanceKind: str, QVTOperational_ModelType433: set["Package"] = None, QVTOperational_ModelType: set["OclExpression"] = None, Class387: "QVTOperational_ContextualProperty", #35: "EMOF_Property", #16: "EMOF_Operation", Class346: "ImperativeOCL_InstantiationExp", Class470: "QVTOperational_OperationalTransformation", Class222: "QVTTemplate_ObjectTemplateExp", Class: "EMOF_Class", Class240: "QVTRelation_Key"):
        self.conformanceKind = conformanceKind
        self.QVTOperational_ModelType433 = QVTOperational_ModelType433 if QVTOperational_ModelType433 is not None else set()
        self.QVTOperational_ModelType = QVTOperational_ModelType if QVTOperational_ModelType is not None else set()
        
    @property
    def conformanceKind(self) -> str:
        return self.__conformanceKind

    @conformanceKind.setter
    def conformanceKind(self, conformanceKind: str):
        self.__conformanceKind = conformanceKind

    @property
    def QVTOperational_ModelType433(self):
        return self.__QVTOperational_ModelType433

    @QVTOperational_ModelType433.setter
    def QVTOperational_ModelType433(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModelType__QVTOperational_ModelType433", None)
        self.__QVTOperational_ModelType433 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package434"):
                    opp_val = getattr(item, "Package434", None)
                    
                    if opp_val == self:
                        setattr(item, "Package434", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package434"):
                    opp_val = getattr(item, "Package434", None)
                    
                    setattr(item, "Package434", self)
                    

    @property
    def QVTOperational_ModelType(self):
        return self.__QVTOperational_ModelType

    @QVTOperational_ModelType.setter
    def QVTOperational_ModelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModelType__QVTOperational_ModelType", None)
        self.__QVTOperational_ModelType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression431"):
                    opp_val = getattr(item, "OclExpression431", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression431", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression431"):
                    opp_val = getattr(item, "OclExpression431", None)
                    
                    setattr(item, "OclExpression431", self)
                    

class QVTBase_Transformation(Class, Package):

    pass
class EssentialOCL_TupleType(DataType, Class):

    pass