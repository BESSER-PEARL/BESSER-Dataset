from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionKind(Enum):
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
    Collection = "Collection"
class DirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
class EnforcementMode(Enum):
    Creation = "Creation"
    Deletion = "Deletion"
class ImportKind(Enum):
    extension = "extension"
    access = "access"
class SeverityKind(Enum):
    error = "error"
    warning = "warning"
    fatal = "fatal"


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
class ModelType:

    pass
class ModuleImport:

    pass
class EntryOperation:

    pass
class RelationDomain:

    pass
class ModelParameter:

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

class Module:

    pass
class QVTOperational_OperationalTransformation(Module):

    pass
class QVTOperational_Library(Module):

    pass
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
class QVTOperational_MappingOperation(ImperativeOperation):

    pass
class QVTOperational_EntryOperation(ImperativeOperation):

    pass
class QVTOperational_Helper(ImperativeOperation):

    def __init__(self, isQuery: str, ImperativeOperation423: "QVTOperational_OperationBody", ImperativeOperation449: "QVTOperational_VarParameter", ImperativeOperation452: "QVTOperational_VarParameter", ImperativeOperation: "QVTOperational_ImperativeOperation"):
        self.isQuery = isQuery
        
    @property
    def isQuery(self) -> str:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery

class QVTOperational_Constructor(ImperativeOperation):

    pass
class Key:

    pass
class DomainPattern:

    pass
class RelationDomainAssignment:

    pass
class Relation:

    pass
class RelationalTransformation:

    pass
class RelationImplementation:

    pass
class PropertyCallExp:

    pass
class QVTRelation_OppositePropertyCallExp(PropertyCallExp):

    pass
class ObjectTemplateExp:

    pass
class TemplateExp:

    pass
class PropertyTemplateItem:

    pass
class QVTTemplate_ObjectTemplateExp(TemplateExp):

    pass
class QVTTemplate_CollectionTemplateExp(TemplateExp):

    pass
class Mapping:

    pass
class EnforcementOperation:

    pass
class Assignment:

    pass
class QVTCore_VariableAssignment(Assignment):

    pass
class QVTCore_PropertyAssignment(Assignment):

    pass
class RealizedVariable:

    pass
class BottomPattern:

    pass
class QVTCore_Area(ABC):

    pass
class Area:

    pass
class CorePattern:

    pass
class QVTCore_GuardPattern(CorePattern):

    pass
class QVTCore_BottomPattern(CorePattern):

    pass
class GuardPattern:

    pass
class Tag:

    pass
class Transformation:

    pass
class QVTRelation_RelationalTransformation(Transformation):

    pass
class Domain:

    pass
class QVTCore_CoreDomain(Area, Domain):

    pass
class QVTRelation_RelationDomain(Domain):

    pass
class TypedModel:

    pass
class Pattern:

    pass
class QVTRelation_DomainPattern(Pattern):

    pass
class QVTCore_CorePattern(Pattern):

    pass
class Predicate:

    pass
class Rule:

    pass
class QVTRelation_Relation(Rule):

    def __init__(self, isTopLevel: str, QVTRelation_Relation: set["RelationImplementation"] = None, QVTRelation_Relation317: set["Variable"] = None, QVTRelation_Relation320: "Pattern" = None, QVTRelation_Relation323: "Pattern" = None, Rule: "QVTBase_Domain", Rule232: "QVTBase_Transformation", Rule220: "QVTBase_Rule"):
        self.isTopLevel = isTopLevel
        self.QVTRelation_Relation = QVTRelation_Relation if QVTRelation_Relation is not None else set()
        self.QVTRelation_Relation317 = QVTRelation_Relation317 if QVTRelation_Relation317 is not None else set()
        self.QVTRelation_Relation320 = QVTRelation_Relation320
        self.QVTRelation_Relation323 = QVTRelation_Relation323
        
    @property
    def isTopLevel(self) -> str:
        return self.__isTopLevel

    @isTopLevel.setter
    def isTopLevel(self, isTopLevel: str):
        self.__isTopLevel = isTopLevel

    @property
    def QVTRelation_Relation320(self):
        return self.__QVTRelation_Relation320

    @QVTRelation_Relation320.setter
    def QVTRelation_Relation320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTRelation_Relation__QVTRelation_Relation320", None)
        self.__QVTRelation_Relation320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern321"):
                opp_val = getattr(old_value, "Pattern321", None)
                if opp_val == self:
                    setattr(old_value, "Pattern321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern321"):
                opp_val = getattr(value, "Pattern321", None)
                setattr(value, "Pattern321", self)

    @property
    def QVTRelation_Relation323(self):
        return self.__QVTRelation_Relation323

    @QVTRelation_Relation323.setter
    def QVTRelation_Relation323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTRelation_Relation__QVTRelation_Relation323", None)
        self.__QVTRelation_Relation323 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern324"):
                opp_val = getattr(old_value, "Pattern324", None)
                if opp_val == self:
                    setattr(old_value, "Pattern324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern324"):
                opp_val = getattr(value, "Pattern324", None)
                setattr(value, "Pattern324", self)

    @property
    def QVTRelation_Relation317(self):
        return self.__QVTRelation_Relation317

    @QVTRelation_Relation317.setter
    def QVTRelation_Relation317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTRelation_Relation__QVTRelation_Relation317", None)
        self.__QVTRelation_Relation317 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable318"):
                    opp_val = getattr(item, "Variable318", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable318", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable318"):
                    opp_val = getattr(item, "Variable318", None)
                    
                    setattr(item, "Variable318", self)
                    

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
                    

class QVTCore_Mapping(Area, Rule):

    pass
class AltExp:

    pass
class CatchExp:

    pass
class OrderedTupleLiteralPart:

    pass
class OperationCallExp:

    pass
class ImperativeLoopExp:

    pass
class ImperativeOCL_ImperativeIterateExp(ImperativeLoopExp):

    pass
class ImperativeOCL_ForExp(ImperativeLoopExp):

    pass
class DictLiteralPart:

    pass
class LogExp:

    pass
class LetExp:

    pass
class ImperativeExpression:

    pass
class ImperativeOCL_UnpackExp(ImperativeExpression):

    pass
class ImperativeOCL_InstantiationExp(ImperativeExpression):

    pass
class ImperativeOCL_UnlinkExp(ImperativeExpression):

    pass
class ImperativeOCL_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, ImperativeOCL_AssertExp117: "LogExp" = None, ImperativeOCL_AssertExp: "OclExpression" = None):
        self.severity = severity
        self.ImperativeOCL_AssertExp117 = ImperativeOCL_AssertExp117
        self.ImperativeOCL_AssertExp = ImperativeOCL_AssertExp
        
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
            if hasattr(old_value, "OclExpression115"):
                opp_val = getattr(old_value, "OclExpression115", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression115"):
                opp_val = getattr(value, "OclExpression115", None)
                setattr(value, "OclExpression115", self)

    @property
    def ImperativeOCL_AssertExp117(self):
        return self.__ImperativeOCL_AssertExp117

    @ImperativeOCL_AssertExp117.setter
    def ImperativeOCL_AssertExp117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssertExp__ImperativeOCL_AssertExp117", None)
        self.__ImperativeOCL_AssertExp117 = value
        
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

class ImperativeOCL_ComputeExp(ImperativeExpression):

    pass
class ImperativeOCL_BlockExp(ImperativeExpression):

    pass
class ImperativeOCL_ContinueExp(ImperativeExpression):

    pass
class ImperativeOCL_WhileExp(ImperativeExpression):

    pass
class QVTOperational_ImperativeCallExp(OperationCallExp, ImperativeExpression):

    def __init__(self, isVirtual: str, OperationCallExp: "QVTCore_EnforcementOperation"):
        self.isVirtual = isVirtual
        
    @property
    def isVirtual(self) -> str:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: str):
        self.__isVirtual = isVirtual

class ImperativeOCL_ReturnExp(ImperativeExpression):

    pass
class ImperativeOCL_AssignExp(ImperativeExpression):

    def __init__(self, isReset: str, ImperativeOCL_AssignExp: "OclExpression" = None, ImperativeOCL_AssignExp121: "OclExpression" = None, ImperativeOCL_AssignExp124: set["OclExpression"] = None):
        self.isReset = isReset
        self.ImperativeOCL_AssignExp = ImperativeOCL_AssignExp
        self.ImperativeOCL_AssignExp121 = ImperativeOCL_AssignExp121
        self.ImperativeOCL_AssignExp124 = ImperativeOCL_AssignExp124 if ImperativeOCL_AssignExp124 is not None else set()
        
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
            if hasattr(old_value, "OclExpression119"):
                opp_val = getattr(old_value, "OclExpression119", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression119"):
                opp_val = getattr(value, "OclExpression119", None)
                setattr(value, "OclExpression119", self)

    @property
    def ImperativeOCL_AssignExp121(self):
        return self.__ImperativeOCL_AssignExp121

    @ImperativeOCL_AssignExp121.setter
    def ImperativeOCL_AssignExp121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssignExp__ImperativeOCL_AssignExp121", None)
        self.__ImperativeOCL_AssignExp121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression122"):
                opp_val = getattr(old_value, "OclExpression122", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression122"):
                opp_val = getattr(value, "OclExpression122", None)
                setattr(value, "OclExpression122", self)

    @property
    def ImperativeOCL_AssignExp124(self):
        return self.__ImperativeOCL_AssignExp124

    @ImperativeOCL_AssignExp124.setter
    def ImperativeOCL_AssignExp124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssignExp__ImperativeOCL_AssignExp124", None)
        self.__ImperativeOCL_AssignExp124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression125"):
                    opp_val = getattr(item, "OclExpression125", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression125"):
                    opp_val = getattr(item, "OclExpression125", None)
                    
                    setattr(item, "OclExpression125", self)
                    

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
            if hasattr(old_value, "Variable198"):
                opp_val = getattr(old_value, "Variable198", None)
                if opp_val == self:
                    setattr(old_value, "Variable198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable198"):
                opp_val = getattr(value, "Variable198", None)
                setattr(value, "Variable198", self)

class ImperativeOCL_CatchExp(ImperativeExpression):

    pass
class ImperativeOCL_SwitchExp(ImperativeExpression):

    pass
class ImperativeOCL_BreakExp(ImperativeExpression):

    pass
class ImperativeOCL_RaiseExp(ImperativeExpression):

    pass
class ImperativeOCL_LogExp(OperationCallExp, ImperativeExpression):

    pass
class ImperativeOCL_TryExp(ImperativeExpression):

    pass
class ImperativeOCL_AltExp(ImperativeExpression):

    pass
class TupleLiteralExp:

    pass
class NavigationCallExp:

    pass
class EssentialOCL_PropertyCallExp(NavigationCallExp):

    pass
class TupleLiteralPart:

    pass
class FeatureCallExp:

    pass
class EssentialOCL_NavigationCallExp(FeatureCallExp):

    pass
class EssentialOCL_OperationCallExp(FeatureCallExp):

    pass
class LoopExp:

    pass
class EssentialOCL_IteratorExp(LoopExp):

    pass
class ImperativeOCL_ImperativeLoopExp(ImperativeExpression, LoopExp):

    pass
class EssentialOCL_IterateExp(LoopExp):

    pass
class NumericLiteralExp:

    pass
class EssentialOCL_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

class EssentialOCL_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class EssentialOCL_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class CallExp:

    pass
class QVTOperational_ResolveExp(ImperativeExpression, CallExp):

    def __init__(self, isDeferred: str, isInverse: str, one: str, QVTOperational_ResolveExp: "OclExpression" = None, QVTOperational_ResolveExp444: "Variable" = None):
        self.isDeferred = isDeferred
        self.isInverse = isInverse
        self.one = one
        self.QVTOperational_ResolveExp = QVTOperational_ResolveExp
        self.QVTOperational_ResolveExp444 = QVTOperational_ResolveExp444
        
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
    def QVTOperational_ResolveExp444(self):
        return self.__QVTOperational_ResolveExp444

    @QVTOperational_ResolveExp444.setter
    def QVTOperational_ResolveExp444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ResolveExp__QVTOperational_ResolveExp444", None)
        self.__QVTOperational_ResolveExp444 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable445"):
                opp_val = getattr(old_value, "Variable445", None)
                if opp_val == self:
                    setattr(old_value, "Variable445", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable445"):
                opp_val = getattr(value, "Variable445", None)
                setattr(value, "Variable445", self)

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
            if hasattr(old_value, "OclExpression442"):
                opp_val = getattr(old_value, "OclExpression442", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression442"):
                opp_val = getattr(value, "OclExpression442", None)
                setattr(value, "OclExpression442", self)

class EssentialOCL_FeatureCallExp(CallExp):

    pass
class Variable:

    pass
class QVTCore_RealizedVariable(Variable):

    pass
class CollectionLiteralPart:

    pass
class EssentialOCL_CollectionItem(CollectionLiteralPart):

    pass
class EssentialOCL_CollectionRange(CollectionLiteralPart):

    pass
class CollectionLiteralExp:

    pass
class LiteralExp:

    pass
class EssentialOCL_EnumLiteralExp(LiteralExp):

    pass
class EssentialOCL_InvalidLiteralExp(LiteralExp):

    pass
class EssentialOCL_NullLiteralExp(LiteralExp):

    pass
class EssentialOCL_TupleLiteralExp(LiteralExp):

    pass
class ImperativeOCL_DictLiteralExp(LiteralExp):

    pass
class ImperativeOCL_ListLiteralExp(LiteralExp):

    pass
class QVTTemplate_TemplateExp(LiteralExp):

    pass
class EssentialOCL_PrimitiveLiteralExp(LiteralExp):

    pass
class ImperativeOCL_OrderedTupleLiteralExp(LiteralExp):

    pass
class EssentialOCL_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, EssentialOCL_CollectionLiteralExp: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.EssentialOCL_CollectionLiteralExp = EssentialOCL_CollectionLiteralExp if EssentialOCL_CollectionLiteralExp is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def EssentialOCL_CollectionLiteralExp(self):
        return self.__EssentialOCL_CollectionLiteralExp

    @EssentialOCL_CollectionLiteralExp.setter
    def EssentialOCL_CollectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EssentialOCL_CollectionLiteralExp__EssentialOCL_CollectionLiteralExp", None)
        self.__EssentialOCL_CollectionLiteralExp = value if value is not None else set()
        
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
                    

class OclExpression:

    pass
class EssentialOCL_LiteralExp(OclExpression):

    pass
class EssentialOCL_VariableExp(OclExpression):

    pass
class EssentialOCL_LetExp(OclExpression):

    pass
class EssentialOCL_LoopExp(OclExpression, CallExp):

    pass
class ImperativeOCL_ImperativeExpression(OclExpression):

    pass
class EssentialOCL_IfExp(OclExpression):

    pass
class QVTRelation_RelationCallExp(OclExpression):

    pass
class EssentialOCL_TypeExp(OclExpression):

    pass
class EssentialOCL_CallExp(OclExpression):

    pass
class PrimitiveLiteralExp:

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

class EssentialOCL_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class EssentialOCL_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class CollectionType:

    pass
class EssentialOCL_SequenceType(CollectionType):

    pass
class EssentialOCL_OrderedSetType(CollectionType):

    pass
class ImperativeOCL_DictionaryType(CollectionType):

    pass
class ImperativeOCL_ListType(CollectionType):

    pass
class EssentialOCL_SetType(CollectionType):

    pass
class EssentialOCL_BagType(CollectionType):

    pass
class Extent:

    pass
class EMOF_URIExtent(Extent):

    def __init__(self):
        
    def element(self, uri: str) -> str:
        # TODO: Implement element method
        pass

    def uri(self, element: str) -> str:
        # TODO: Implement uri method
        pass

    def contextURI(self) -> str:
        # TODO: Implement contextURI method
        pass

class ReflectiveCollection:

    pass
class EMOF_ReflectiveSequence(ReflectiveCollection):

    def __init__(self):
        
    def remove(self, index: str) -> str:
        # TODO: Implement remove method
        pass

    def add(self, index: str, object: str):
        # TODO: Implement add method
        pass

    def get(self, index: str) -> str:
        # TODO: Implement get method
        pass

    def set(self, index: str, object: str) -> str:
        # TODO: Implement set method
        pass

class TypedElement:

    pass
class EssentialOCL_OclExpression(TypedElement):

    pass
class EssentialOCL_Variable(TypedElement):

    pass
class EssentialOCL_ExpressionInOcl(TypedElement):

    pass
class EssentialOCL_TupleLiteralPart(TypedElement):

    pass
class EssentialOCL_CollectionLiteralPart(TypedElement):

    pass
class EMOF_Object:

    pass
class Parameter:

    pass
class QVTBase_FunctionParameter(Variable, Parameter):

    pass
class QVTOperational_VarParameter(Variable, Parameter):

    def __init__(self, kind: str, QVTOperational_VarParameter: "ImperativeOperation" = None, QVTOperational_VarParameter451: "ImperativeOperation" = None, Parameter106: "EssentialOCL_Variable", Parameter: "EMOF_Operation", Variable287: "QVTTemplate_CollectionTemplateExp", Variable210: "QVTBase_Pattern", Variable77: "EssentialOCL_LetExp", Variable154: "ImperativeOCL_InstantiationExp", Variable198: "ImperativeOCL_VariableInitExp", Variable318: "QVTRelation_Relation", Variable339: "QVTRelation_RelationDomainAssignment", Variable300: "QVTTemplate_TemplateExp", Variable62: "EssentialOCL_ExpressionInOcl", Variable280: "QVTCore_VariableAssignment", Variable108: "EssentialOCL_VariableExp", Variable72: "EssentialOCL_IterateExp", Variable82: "EssentialOCL_LoopExp", Variable445: "QVTOperational_ResolveExp", Variable137: "ImperativeOCL_ComputeExp", Variable196: "ImperativeOCL_UnpackExp", Variable334: "QVTRelation_RelationDomain", Variable257: "QVTCore_CorePattern", Variable426: "QVTOperational_OperationBody", Variable: "EssentialOCL_ExpressionInOcl", Variable59: "EssentialOCL_ExpressionInOcl", Variable418: "QVTOperational_ObjectExp", Variable405: "QVTOperational_Module", Variable147: "ImperativeOCL_ImperativeIterateExp"):
        self.kind = kind
        self.QVTOperational_VarParameter = QVTOperational_VarParameter
        self.QVTOperational_VarParameter451 = QVTOperational_VarParameter451
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def QVTOperational_VarParameter(self):
        return self.__QVTOperational_VarParameter

    @QVTOperational_VarParameter.setter
    def QVTOperational_VarParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_VarParameter__QVTOperational_VarParameter", None)
        self.__QVTOperational_VarParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation449"):
                opp_val = getattr(old_value, "ImperativeOperation449", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation449", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation449"):
                opp_val = getattr(value, "ImperativeOperation449", None)
                setattr(value, "ImperativeOperation449", self)

    @property
    def QVTOperational_VarParameter451(self):
        return self.__QVTOperational_VarParameter451

    @QVTOperational_VarParameter451.setter
    def QVTOperational_VarParameter451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_VarParameter__QVTOperational_VarParameter451", None)
        self.__QVTOperational_VarParameter451 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation452"):
                opp_val = getattr(old_value, "ImperativeOperation452", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation452", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation452"):
                opp_val = getattr(value, "ImperativeOperation452", None)
                setattr(value, "ImperativeOperation452", self)

class MultiplicityElement:

    pass
class EMOF_Property(TypedElement, MultiplicityElement):

    def __init__(self, default: str, isComposite: str, isDerived: str, isID: str, isReadOnly: str, EMOF_Property: "Class" = None, EMOF_Property29: "Property" = None):
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.isReadOnly = isReadOnly
        self.EMOF_Property = EMOF_Property
        self.EMOF_Property29 = EMOF_Property29
        
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
    def isID(self) -> str:
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID

    @property
    def isReadOnly(self) -> str:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

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
            if hasattr(old_value, "Class27"):
                opp_val = getattr(old_value, "Class27", None)
                if opp_val == self:
                    setattr(old_value, "Class27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class27"):
                opp_val = getattr(value, "Class27", None)
                setattr(value, "Class27", self)

    @property
    def EMOF_Property29(self):
        return self.__EMOF_Property29

    @EMOF_Property29.setter
    def EMOF_Property29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Property__EMOF_Property29", None)
        self.__EMOF_Property29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property30"):
                opp_val = getattr(old_value, "Property30", None)
                if opp_val == self:
                    setattr(old_value, "Property30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property30"):
                opp_val = getattr(value, "Property30", None)
                setattr(value, "Property30", self)

class EMOF_Parameter(TypedElement, MultiplicityElement):

    pass
class EMOF_Operation(TypedElement, MultiplicityElement):

    pass
class Enumeration:

    pass
class EMOF_MultiplicityElement(ABC):

    def __init__(self, isOrdered: str, isUnique: str, lower: str, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

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
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

class Package:

    pass
class NamedElement:

    pass
class QVTBase_Rule(NamedElement):

    pass
class EMOF_TypedElement(NamedElement):

    pass
class EMOF_EnumerationLiteral(NamedElement):

    pass
class EMOF_Package(NamedElement):

    def __init__(self, uri: str, EMOF_Package: set["Package"] = None, EMOF_Package19: "Package" = None, EMOF_Package22: set["Type"] = None, NamedElement: "EMOF_Comment"):
        self.uri = uri
        self.EMOF_Package = EMOF_Package if EMOF_Package is not None else set()
        self.EMOF_Package19 = EMOF_Package19
        self.EMOF_Package22 = EMOF_Package22 if EMOF_Package22 is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def EMOF_Package19(self):
        return self.__EMOF_Package19

    @EMOF_Package19.setter
    def EMOF_Package19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__EMOF_Package19", None)
        self.__EMOF_Package19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package20"):
                opp_val = getattr(old_value, "Package20", None)
                if opp_val == self:
                    setattr(old_value, "Package20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package20"):
                opp_val = getattr(value, "Package20", None)
                setattr(value, "Package20", self)

    @property
    def EMOF_Package(self):
        return self.__EMOF_Package

    @EMOF_Package.setter
    def EMOF_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__EMOF_Package", None)
        self.__EMOF_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package17"):
                    opp_val = getattr(item, "Package17", None)
                    
                    if opp_val == self:
                        setattr(item, "Package17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package17"):
                    opp_val = getattr(item, "Package17", None)
                    
                    setattr(item, "Package17", self)
                    

    @property
    def EMOF_Package22(self):
        return self.__EMOF_Package22

    @EMOF_Package22.setter
    def EMOF_Package22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__EMOF_Package22", None)
        self.__EMOF_Package22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type23"):
                    opp_val = getattr(item, "Type23", None)
                    
                    if opp_val == self:
                        setattr(item, "Type23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type23"):
                    opp_val = getattr(item, "Type23", None)
                    
                    setattr(item, "Type23", self)
                    

class QVTBase_Domain(NamedElement):

    def __init__(self, isCheckable: str, isEnforceable: str, QVTBase_Domain: "Rule" = None, QVTBase_Domain206: "TypedModel" = None, NamedElement: "EMOF_Comment"):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.QVTBase_Domain = QVTBase_Domain
        self.QVTBase_Domain206 = QVTBase_Domain206
        
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
    def QVTBase_Domain206(self):
        return self.__QVTBase_Domain206

    @QVTBase_Domain206.setter
    def QVTBase_Domain206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTBase_Domain__QVTBase_Domain206", None)
        self.__QVTBase_Domain206 = value
        
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
    def QVTBase_Domain(self):
        return self.__QVTBase_Domain

    @QVTBase_Domain.setter
    def QVTBase_Domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTBase_Domain__QVTBase_Domain", None)
        self.__QVTBase_Domain = value
        
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

class QVTBase_TypedModel(NamedElement):

    pass
class EMOF_Type(NamedElement):

    def __init__(self, EMOF_Type: "Package" = None, NamedElement: "EMOF_Comment"):
        self.EMOF_Type = EMOF_Type
        
    @property
    def EMOF_Type(self):
        return self.__EMOF_Type

    @EMOF_Type.setter
    def EMOF_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Type__EMOF_Type", None)
        self.__EMOF_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package33"):
                opp_val = getattr(old_value, "Package33", None)
                if opp_val == self:
                    setattr(old_value, "Package33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package33"):
                opp_val = getattr(value, "Package33", None)
                setattr(value, "Package33", self)

    def isInstance(self, object: str) -> str:
        # TODO: Implement isInstance method
        pass

class Element:

    pass
class ImperativeOCL_DictLiteralPart(Element):

    pass
class QVTRelation_RelationDomainAssignment(Element):

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

    def convertToString(self, object: str, dataType: str) -> str:
        # TODO: Implement convertToString method
        pass

    def createFromString(self, dataType: str, string: str) -> str:
        # TODO: Implement createFromString method
        pass

    def create(self, metaClass: str) -> str:
        # TODO: Implement create method
        pass

class EMOF_Tag(Element):

    def __init__(self, name: str, value: str, EMOF_Tag: set["Element"] = None, Element: "EMOF_Tag"):
        self.name = name
        self.value = value
        self.EMOF_Tag = EMOF_Tag if EMOF_Tag is not None else set()
        
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
                    

class QVTRelation_Key(Element):

    pass
class QVTTemplate_PropertyTemplateItem(Element):

    def __init__(self, isOpposite: str, QVTTemplate_PropertyTemplateItem: "ObjectTemplateExp" = None, QVTTemplate_PropertyTemplateItem294: "Property" = None, QVTTemplate_PropertyTemplateItem297: "OclExpression" = None, Element: "EMOF_Tag"):
        self.isOpposite = isOpposite
        self.QVTTemplate_PropertyTemplateItem = QVTTemplate_PropertyTemplateItem
        self.QVTTemplate_PropertyTemplateItem294 = QVTTemplate_PropertyTemplateItem294
        self.QVTTemplate_PropertyTemplateItem297 = QVTTemplate_PropertyTemplateItem297
        
    @property
    def isOpposite(self) -> str:
        return self.__isOpposite

    @isOpposite.setter
    def isOpposite(self, isOpposite: str):
        self.__isOpposite = isOpposite

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
            if hasattr(old_value, "ObjectTemplateExp"):
                opp_val = getattr(old_value, "ObjectTemplateExp", None)
                if opp_val == self:
                    setattr(old_value, "ObjectTemplateExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ObjectTemplateExp"):
                opp_val = getattr(value, "ObjectTemplateExp", None)
                setattr(value, "ObjectTemplateExp", self)

    @property
    def QVTTemplate_PropertyTemplateItem294(self):
        return self.__QVTTemplate_PropertyTemplateItem294

    @QVTTemplate_PropertyTemplateItem294.setter
    def QVTTemplate_PropertyTemplateItem294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTTemplate_PropertyTemplateItem__QVTTemplate_PropertyTemplateItem294", None)
        self.__QVTTemplate_PropertyTemplateItem294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property295"):
                opp_val = getattr(old_value, "Property295", None)
                if opp_val == self:
                    setattr(old_value, "Property295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property295"):
                opp_val = getattr(value, "Property295", None)
                setattr(value, "Property295", self)

    @property
    def QVTTemplate_PropertyTemplateItem297(self):
        return self.__QVTTemplate_PropertyTemplateItem297

    @QVTTemplate_PropertyTemplateItem297.setter
    def QVTTemplate_PropertyTemplateItem297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTTemplate_PropertyTemplateItem__QVTTemplate_PropertyTemplateItem297", None)
        self.__QVTTemplate_PropertyTemplateItem297 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression298"):
                opp_val = getattr(old_value, "OclExpression298", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression298"):
                opp_val = getattr(value, "OclExpression298", None)
                setattr(value, "OclExpression298", self)

class QVTOperational_OperationBody(Element):

    pass
class QVTOperational_ModuleImport(Element):

    def __init__(self, kind: str, QVTOperational_ModuleImport: set["ModelType"] = None, QVTOperational_ModuleImport411: "Module" = None, QVTOperational_ModuleImport413: "Module" = None, Element: "EMOF_Tag"):
        self.kind = kind
        self.QVTOperational_ModuleImport = QVTOperational_ModuleImport if QVTOperational_ModuleImport is not None else set()
        self.QVTOperational_ModuleImport411 = QVTOperational_ModuleImport411
        self.QVTOperational_ModuleImport413 = QVTOperational_ModuleImport413
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

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
                if hasattr(item, "ModelType409"):
                    opp_val = getattr(item, "ModelType409", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType409", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType409"):
                    opp_val = getattr(item, "ModelType409", None)
                    
                    setattr(item, "ModelType409", self)
                    

    @property
    def QVTOperational_ModuleImport413(self):
        return self.__QVTOperational_ModuleImport413

    @QVTOperational_ModuleImport413.setter
    def QVTOperational_ModuleImport413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__QVTOperational_ModuleImport413", None)
        self.__QVTOperational_ModuleImport413 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module414"):
                opp_val = getattr(old_value, "Module414", None)
                if opp_val == self:
                    setattr(old_value, "Module414", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module414"):
                opp_val = getattr(value, "Module414", None)
                setattr(value, "Module414", self)

    @property
    def QVTOperational_ModuleImport411(self):
        return self.__QVTOperational_ModuleImport411

    @QVTOperational_ModuleImport411.setter
    def QVTOperational_ModuleImport411(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__QVTOperational_ModuleImport411", None)
        self.__QVTOperational_ModuleImport411 = value
        
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

class QVTCore_EnforcementOperation(Element):

    def __init__(self, enforcementMode: str, QVTCore_EnforcementOperation: "BottomPattern" = None, QVTCore_EnforcementOperation261: "OperationCallExp" = None, Element: "EMOF_Tag"):
        self.enforcementMode = enforcementMode
        self.QVTCore_EnforcementOperation = QVTCore_EnforcementOperation
        self.QVTCore_EnforcementOperation261 = QVTCore_EnforcementOperation261
        
    @property
    def enforcementMode(self) -> str:
        return self.__enforcementMode

    @enforcementMode.setter
    def enforcementMode(self, enforcementMode: str):
        self.__enforcementMode = enforcementMode

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
            if hasattr(old_value, "BottomPattern259"):
                opp_val = getattr(old_value, "BottomPattern259", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern259", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern259"):
                opp_val = getattr(value, "BottomPattern259", None)
                setattr(value, "BottomPattern259", self)

    @property
    def QVTCore_EnforcementOperation261(self):
        return self.__QVTCore_EnforcementOperation261

    @QVTCore_EnforcementOperation261.setter
    def QVTCore_EnforcementOperation261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTCore_EnforcementOperation__QVTCore_EnforcementOperation261", None)
        self.__QVTCore_EnforcementOperation261 = value
        
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
class ImperativeOCL_OrderedTupleLiteralPart(Element):

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

class QVTBase_Predicate(Element):

    pass
class QVTCore_Assignment(Element):

    def __init__(self, isDefault: str, QVTCore_Assignment: "BottomPattern" = None, QVTCore_Assignment247: "OclExpression" = None, Element: "EMOF_Tag"):
        self.isDefault = isDefault
        self.QVTCore_Assignment = QVTCore_Assignment
        self.QVTCore_Assignment247 = QVTCore_Assignment247
        
    @property
    def isDefault(self) -> str:
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: str):
        self.__isDefault = isDefault

    @property
    def QVTCore_Assignment247(self):
        return self.__QVTCore_Assignment247

    @QVTCore_Assignment247.setter
    def QVTCore_Assignment247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTCore_Assignment__QVTCore_Assignment247", None)
        self.__QVTCore_Assignment247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression248"):
                opp_val = getattr(old_value, "OclExpression248", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression248"):
                opp_val = getattr(value, "OclExpression248", None)
                setattr(value, "OclExpression248", self)

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
            if hasattr(old_value, "BottomPattern245"):
                opp_val = getattr(old_value, "BottomPattern245", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern245"):
                opp_val = getattr(value, "BottomPattern245", None)
                setattr(value, "BottomPattern245", self)

class QVTRelation_RelationImplementation(Element):

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
                    

class EnumerationLiteral:

    pass
class DataType:

    pass
class EssentialOCL_CollectionType(DataType):

    pass
class EMOF_PrimitiveType(DataType):

    pass
class EMOF_Enumeration(DataType):

    pass
class Comment:

    pass
class Object:

    pass
class EMOF_Extent(Object):

    def __init__(self):
        
    def elements(self) -> str:
        # TODO: Implement elements method
        pass

    def useContainment(self) -> str:
        # TODO: Implement useContainment method
        pass

class EMOF_ReflectiveCollection(Object):

    def __init__(self):
        
    def clear(self):
        # TODO: Implement clear method
        pass

    def size(self) -> str:
        # TODO: Implement size method
        pass

    def addAll(self, objects: str) -> str:
        # TODO: Implement addAll method
        pass

    def add(self, object: str) -> str:
        # TODO: Implement add method
        pass

    def remove(self, object: str) -> str:
        # TODO: Implement remove method
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
                    

    def getMetaClass(self) -> str:
        # TODO: Implement getMetaClass method
        pass

    def isSet(self, property: str) -> str:
        # TODO: Implement isSet method
        pass

    def get(self, property: str) -> str:
        # TODO: Implement get method
        pass

    def unset(self, property: str):
        # TODO: Implement unset method
        pass

    def container(self) -> str:
        # TODO: Implement container method
        pass

    def set(self, property: str, object: str):
        # TODO: Implement set method
        pass

    def equals(self, object: str) -> str:
        # TODO: Implement equals method
        pass

class Class:

    pass
class QVTOperational_ModelType(Class):

    def __init__(self, conformanceKind: str, QVTOperational_ModelType: set["OclExpression"] = None, QVTOperational_ModelType392: set["Package"] = None, Class27: "EMOF_Property", Class: "EMOF_Class", Class306: "QVTRelation_Key", Class11: "EMOF_Operation", Class157: "ImperativeOCL_InstantiationExp", Class350: "QVTOperational_ContextualProperty", Class291: "QVTTemplate_ObjectTemplateExp", Class428: "QVTOperational_OperationalTransformation"):
        self.conformanceKind = conformanceKind
        self.QVTOperational_ModelType = QVTOperational_ModelType if QVTOperational_ModelType is not None else set()
        self.QVTOperational_ModelType392 = QVTOperational_ModelType392 if QVTOperational_ModelType392 is not None else set()
        
    @property
    def conformanceKind(self) -> str:
        return self.__conformanceKind

    @conformanceKind.setter
    def conformanceKind(self, conformanceKind: str):
        self.__conformanceKind = conformanceKind

    @property
    def QVTOperational_ModelType392(self):
        return self.__QVTOperational_ModelType392

    @QVTOperational_ModelType392.setter
    def QVTOperational_ModelType392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModelType__QVTOperational_ModelType392", None)
        self.__QVTOperational_ModelType392 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package393"):
                    opp_val = getattr(item, "Package393", None)
                    
                    if opp_val == self:
                        setattr(item, "Package393", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package393"):
                    opp_val = getattr(item, "Package393", None)
                    
                    setattr(item, "Package393", self)
                    

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
                if hasattr(item, "OclExpression390"):
                    opp_val = getattr(item, "OclExpression390", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression390", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression390"):
                    opp_val = getattr(item, "OclExpression390", None)
                    
                    setattr(item, "OclExpression390", self)
                    

class ImperativeOCL_OrderedTupleType(Class):

    pass
class ImperativeOCL_Typedef(Class):

    pass
class QVTOperational_Module(Class, Package):

    def __init__(self, isBlackbox: str, QVTOperational_Module397: "EntryOperation" = None, QVTOperational_Module399: set["ModuleImport"] = None, QVTOperational_Module401: set["Tag"] = None, QVTOperational_Module: set["Property"] = None, QVTOperational_Module407: set["ModelType"] = None, QVTOperational_Module404: set["Variable"] = None, Class27: "EMOF_Property", Class: "EMOF_Class", Class306: "QVTRelation_Key", Class11: "EMOF_Operation", Class157: "ImperativeOCL_InstantiationExp", Class350: "QVTOperational_ContextualProperty", Class291: "QVTTemplate_ObjectTemplateExp", Class428: "QVTOperational_OperationalTransformation", Package33: "EMOF_Type", Package20: "EMOF_Package", Package393: "QVTOperational_ModelType", Package: "EMOF_Factory", Package17: "EMOF_Package", Package240: "QVTBase_TypedModel"):
        self.isBlackbox = isBlackbox
        self.QVTOperational_Module397 = QVTOperational_Module397
        self.QVTOperational_Module399 = QVTOperational_Module399 if QVTOperational_Module399 is not None else set()
        self.QVTOperational_Module401 = QVTOperational_Module401 if QVTOperational_Module401 is not None else set()
        self.QVTOperational_Module = QVTOperational_Module if QVTOperational_Module is not None else set()
        self.QVTOperational_Module407 = QVTOperational_Module407 if QVTOperational_Module407 is not None else set()
        self.QVTOperational_Module404 = QVTOperational_Module404 if QVTOperational_Module404 is not None else set()
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

    @property
    def QVTOperational_Module399(self):
        return self.__QVTOperational_Module399

    @QVTOperational_Module399.setter
    def QVTOperational_Module399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module399", None)
        self.__QVTOperational_Module399 = value if value is not None else set()
        
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
    def QVTOperational_Module401(self):
        return self.__QVTOperational_Module401

    @QVTOperational_Module401.setter
    def QVTOperational_Module401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module401", None)
        self.__QVTOperational_Module401 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tag402"):
                    opp_val = getattr(item, "Tag402", None)
                    
                    if opp_val == self:
                        setattr(item, "Tag402", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tag402"):
                    opp_val = getattr(item, "Tag402", None)
                    
                    setattr(item, "Tag402", self)
                    

    @property
    def QVTOperational_Module404(self):
        return self.__QVTOperational_Module404

    @QVTOperational_Module404.setter
    def QVTOperational_Module404(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module404", None)
        self.__QVTOperational_Module404 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable405"):
                    opp_val = getattr(item, "Variable405", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable405", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable405"):
                    opp_val = getattr(item, "Variable405", None)
                    
                    setattr(item, "Variable405", self)
                    

    @property
    def QVTOperational_Module397(self):
        return self.__QVTOperational_Module397

    @QVTOperational_Module397.setter
    def QVTOperational_Module397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module397", None)
        self.__QVTOperational_Module397 = value
        
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
                if hasattr(item, "Property395"):
                    opp_val = getattr(item, "Property395", None)
                    
                    if opp_val == self:
                        setattr(item, "Property395", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property395"):
                    opp_val = getattr(item, "Property395", None)
                    
                    setattr(item, "Property395", self)
                    

    @property
    def QVTOperational_Module407(self):
        return self.__QVTOperational_Module407

    @QVTOperational_Module407.setter
    def QVTOperational_Module407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module407", None)
        self.__QVTOperational_Module407 = value if value is not None else set()
        
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
                    

class QVTBase_Transformation(Class, Package):

    pass
class EssentialOCL_TupleType(DataType, Class):

    pass
class Operation:

    pass
class QVTBase_Function(Operation):

    pass
class QVTOperational_ImperativeOperation(Operation):

    def __init__(self, isBlackbox: str, QVTOperational_ImperativeOperation: "OperationBody" = None, QVTOperational_ImperativeOperation359: "VarParameter" = None, QVTOperational_ImperativeOperation361: "ImperativeOperation" = None, QVTOperational_ImperativeOperation363: set["VarParameter"] = None, Operation87: "EssentialOCL_OperationCallExp", Operation341: "QVTRelation_RelationImplementation", Operation25: "EMOF_Parameter", Operation: "EMOF_Class"):
        self.isBlackbox = isBlackbox
        self.QVTOperational_ImperativeOperation = QVTOperational_ImperativeOperation
        self.QVTOperational_ImperativeOperation359 = QVTOperational_ImperativeOperation359
        self.QVTOperational_ImperativeOperation361 = QVTOperational_ImperativeOperation361
        self.QVTOperational_ImperativeOperation363 = QVTOperational_ImperativeOperation363 if QVTOperational_ImperativeOperation363 is not None else set()
        
    @property
    def isBlackbox(self) -> str:
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox

    @property
    def QVTOperational_ImperativeOperation359(self):
        return self.__QVTOperational_ImperativeOperation359

    @QVTOperational_ImperativeOperation359.setter
    def QVTOperational_ImperativeOperation359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation359", None)
        self.__QVTOperational_ImperativeOperation359 = value
        
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
    def QVTOperational_ImperativeOperation361(self):
        return self.__QVTOperational_ImperativeOperation361

    @QVTOperational_ImperativeOperation361.setter
    def QVTOperational_ImperativeOperation361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation361", None)
        self.__QVTOperational_ImperativeOperation361 = value
        
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
    def QVTOperational_ImperativeOperation363(self):
        return self.__QVTOperational_ImperativeOperation363

    @QVTOperational_ImperativeOperation363.setter
    def QVTOperational_ImperativeOperation363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__QVTOperational_ImperativeOperation363", None)
        self.__QVTOperational_ImperativeOperation363 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarParameter364"):
                    opp_val = getattr(item, "VarParameter364", None)
                    
                    if opp_val == self:
                        setattr(item, "VarParameter364", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarParameter364"):
                    opp_val = getattr(item, "VarParameter364", None)
                    
                    setattr(item, "VarParameter364", self)
                    

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
            if hasattr(old_value, "OperationBody"):
                opp_val = getattr(old_value, "OperationBody", None)
                if opp_val == self:
                    setattr(old_value, "OperationBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OperationBody"):
                opp_val = getattr(value, "OperationBody", None)
                setattr(value, "OperationBody", self)

class Property:

    pass
class QVTOperational_ContextualProperty(Property):

    pass
class Type:

    pass
class EMOF_DataType(Type):

    pass
class EssentialOCL_AnyType(Type):

    pass
class EssentialOCL_InvalidType(Type):

    pass
class EssentialOCL_TemplateParameterType(Type):

    def __init__(self, specification: str, Type47: "EssentialOCL_CollectionType", Type132: "ImperativeOCL_CatchExp", Type: "EMOF_Operation", Type56: "EssentialOCL_ExpressionInOcl", Type166: "ImperativeOCL_OrderedTupleType", Type23: "EMOF_Package", Type99: "EssentialOCL_TypeExp", Type171: "ImperativeOCL_RaiseExp", Type35: "EMOF_TypedElement", Type183: "ImperativeOCL_Typedef", Type145: "ImperativeOCL_DictionaryType"):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class EssentialOCL_VoidType(Type):

    pass
class EMOF_Class(Type):

    def __init__(self, isAbstract: str, EMOF_Class: set["Property"] = None, EMOF_Class2: set["Operation"] = None, EMOF_Class4: set["Class"] = None, Type47: "EssentialOCL_CollectionType", Type132: "ImperativeOCL_CatchExp", Type: "EMOF_Operation", Type56: "EssentialOCL_ExpressionInOcl", Type166: "ImperativeOCL_OrderedTupleType", Type23: "EMOF_Package", Type99: "EssentialOCL_TypeExp", Type171: "ImperativeOCL_RaiseExp", Type35: "EMOF_TypedElement", Type183: "ImperativeOCL_Typedef", Type145: "ImperativeOCL_DictionaryType"):
        self.isAbstract = isAbstract
        self.EMOF_Class = EMOF_Class if EMOF_Class is not None else set()
        self.EMOF_Class2 = EMOF_Class2 if EMOF_Class2 is not None else set()
        self.EMOF_Class4 = EMOF_Class4 if EMOF_Class4 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def EMOF_Class2(self):
        return self.__EMOF_Class2

    @EMOF_Class2.setter
    def EMOF_Class2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Class__EMOF_Class2", None)
        self.__EMOF_Class2 = value if value is not None else set()
        
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
    def EMOF_Class4(self):
        return self.__EMOF_Class4

    @EMOF_Class4.setter
    def EMOF_Class4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Class__EMOF_Class4", None)
        self.__EMOF_Class4 = value if value is not None else set()
        
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
                    
