from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EnforcementMode(Enum):
    Creation = "Creation"
    Deletion = "Deletion"
class CollectionKind(Enum):
    Set = "Set"
    OrderedSet = "OrderedSet"
    Bag = "Bag"
    Sequence = "Sequence"
    Collection = "Collection"
class SeverityKind(Enum):
    warning = "warning"
    fatal = "fatal"
    error = "error"
class ImportKind(Enum):
    extension = "extension"
    access = "access"
class DirectionKind(Enum):
    in_ = "in_"
    inout = "inout"
    out = "out"


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
class VarParameter:

    pass
class QVTOperational_ModelParameter(VarParameter):

    pass
class QVTOperational_MappingParameter(VarParameter):

    pass
class MappingOperation:

    pass
class ImperativeCallExp:

    pass
class QVTOperational_MappingCallExp(ImperativeCallExp):

    def __init__(self, isStrict: str):
        self.isStrict = isStrict
        
        pass
    @property
    def isStrict(self):
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict


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
class QVTOperational_Constructor(ImperativeOperation):

    pass
class QVTOperational_Helper(ImperativeOperation):

    def __init__(self, isQuery: str, ImperativeOperation: "QVTOperational_ImperativeOperation" = None, ImperativeOperation401: "QVTOperational_OperationBody" = None, ImperativeOperation430: "QVTOperational_VarParameter" = None, ImperativeOperation428: "QVTOperational_VarParameter" = None):
        self.isQuery = isQuery
        
        pass
    @property
    def isQuery(self):
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery


class QVTOperational_EntryOperation(ImperativeOperation):

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
class DictLiteralExp:

    pass
class DictLiteralPart:

    pass
class LogExp:

    pass
class ImperativeExpression:

    pass
class ImperativeOCL_CatchExp(ImperativeExpression):

    pass
class ImperativeOCL_RaiseExp(ImperativeExpression):

    pass
class ImperativeOCL_InstantiationExp(ImperativeExpression):

    pass
class ImperativeOCL_TryExp(ImperativeExpression):

    pass
class ImperativeOCL_BlockExp(ImperativeExpression):

    pass
class ImperativeOCL_ReturnExp(ImperativeExpression):

    pass
class ImperativeOCL_ComputeExp(ImperativeExpression):

    pass
class ImperativeOCL_AssertExp(ImperativeExpression):

    def __init__(self, severity: str, ImperativeOCL_AssertExp: "OclExpression" = None, ImperativeOCL_AssertExp244: "LogExp" = None):
        self.severity = severity
        self.ImperativeOCL_AssertExp = ImperativeOCL_AssertExp
        self.ImperativeOCL_AssertExp244 = ImperativeOCL_AssertExp244
        
        pass
    @property
    def severity(self):
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
            if hasattr(old_value, "OclExpression242"):
                opp_val = getattr(old_value, "OclExpression242", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression242"):
                opp_val = getattr(value, "OclExpression242", None)
                setattr(value, "OclExpression242", self)

    @property
    def ImperativeOCL_AssertExp244(self):
        return self.__ImperativeOCL_AssertExp244

    @ImperativeOCL_AssertExp244.setter
    def ImperativeOCL_AssertExp244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssertExp__ImperativeOCL_AssertExp244", None)
        self.__ImperativeOCL_AssertExp244 = value
        
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

class ImperativeOCL_SwitchExp(ImperativeExpression):

    pass
class ImperativeOCL_UnlinkExp(ImperativeExpression):

    pass
class ImperativeOCL_BreakExp(ImperativeExpression):

    pass
class ImperativeOCL_WhileExp(ImperativeExpression):

    pass
class ImperativeOCL_ContinueExp(ImperativeExpression):

    pass
class ImperativeOCL_VariableInitExp(ImperativeExpression):

    def __init__(self, withResult: str, ImperativeOCL_VariableInitExp: "Variable" = None):
        self.withResult = withResult
        self.ImperativeOCL_VariableInitExp = ImperativeOCL_VariableInitExp
        
        pass
    @property
    def withResult(self):
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
            if hasattr(old_value, "Variable323"):
                opp_val = getattr(old_value, "Variable323", None)
                if opp_val == self:
                    setattr(old_value, "Variable323", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable323"):
                opp_val = getattr(value, "Variable323", None)
                setattr(value, "Variable323", self)

class ImperativeOCL_AltExp(ImperativeExpression):

    pass
class Key:

    pass
class ImperativeOCL_AssignExp(ImperativeExpression):

    def __init__(self, isReset: str, ImperativeOCL_AssignExp: "OclExpression" = None, ImperativeOCL_AssignExp248: "OclExpression" = None, ImperativeOCL_AssignExp251: set["OclExpression"] = None):
        self.isReset = isReset
        self.ImperativeOCL_AssignExp = ImperativeOCL_AssignExp
        self.ImperativeOCL_AssignExp248 = ImperativeOCL_AssignExp248
        self.ImperativeOCL_AssignExp251 = ImperativeOCL_AssignExp251 if ImperativeOCL_AssignExp251 is not None else set()
        
        pass
    @property
    def isReset(self):
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
            if hasattr(old_value, "OclExpression246"):
                opp_val = getattr(old_value, "OclExpression246", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression246"):
                opp_val = getattr(value, "OclExpression246", None)
                setattr(value, "OclExpression246", self)

    @property
    def ImperativeOCL_AssignExp251(self):
        return self.__ImperativeOCL_AssignExp251

    @ImperativeOCL_AssignExp251.setter
    def ImperativeOCL_AssignExp251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssignExp__ImperativeOCL_AssignExp251", None)
        self.__ImperativeOCL_AssignExp251 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression252"):
                    opp_val = getattr(item, "OclExpression252", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression252"):
                    opp_val = getattr(item, "OclExpression252", None)
                    
                    setattr(item, "OclExpression252", self)
                    

    @property
    def ImperativeOCL_AssignExp248(self):
        return self.__ImperativeOCL_AssignExp248

    @ImperativeOCL_AssignExp248.setter
    def ImperativeOCL_AssignExp248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ImperativeOCL_AssignExp__ImperativeOCL_AssignExp248", None)
        self.__ImperativeOCL_AssignExp248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression249"):
                opp_val = getattr(old_value, "OclExpression249", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression249"):
                opp_val = getattr(value, "OclExpression249", None)
                setattr(value, "OclExpression249", self)

class DomainPattern:

    pass
class RelationDomainAssignment:

    pass
class Relation:

    pass
class RelationImplementation:

    pass
class RelationDomain:

    pass
class PropertyCallExp:

    pass
class QVTRelation_OppositePropertyCallExp(PropertyCallExp):

    pass
class RelationalTransformation:

    pass
class TemplateExp:

    pass
class QVTTemplate_CollectionTemplateExp(TemplateExp):

    pass
class ObjectTemplateExp:

    pass
class PropertyTemplateItem:

    pass
class QVTTemplate_ObjectTemplateExp(TemplateExp):

    pass
class OperationCallExp:

    pass
class ImperativeOCL_LogExp(ImperativeExpression, OperationCallExp):

    pass
class QVTOperational_ImperativeCallExp(ImperativeExpression, OperationCallExp):

    def __init__(self, isVirtual: str, OperationCallExp: "QVTCore_EnforcementOperation" = None):
        self.isVirtual = isVirtual
        
        pass
    @property
    def isVirtual(self):
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: str):
        self.__isVirtual = isVirtual


class RealizedVariable:

    pass
class Mapping:

    pass
class GuardPattern:

    pass
class BottomPattern:

    pass
class QVTCore_Area(ABC):

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
class QVTCore_GuardPattern(CorePattern):

    pass
class QVTCore_BottomPattern(CorePattern):

    pass
class Transformation:

    pass
class QVTRelation_RelationalTransformation(Transformation):

    pass
class Domain:

    pass
class QVTCore_CoreDomain(Domain, Area):

    pass
class QVTRelation_RelationDomain(Domain):

    pass
class Pattern:

    pass
class QVTCore_CorePattern(Pattern):

    pass
class QVTRelation_DomainPattern(Pattern):

    pass
class Predicate:

    pass
class Tag:

    pass
class LetExp:

    pass
class TypedModel:

    pass
class Rule:

    pass
class QVTCore_Mapping(Rule, Area):

    pass
class QVTRelation_Relation(Rule):

    def __init__(self, isTopLevel: str, relation: set["RelationImplementation"] = None, QVTRelation_Relation: set["Variable"] = None, QVTRelation_Relation207: "Pattern" = None, QVTRelation_Relation210: "Pattern" = None, Rule113: "QVTBase_Rule" = None, Rule: "QVTBase_Domain" = None, Rule124: "QVTBase_Transformation" = None):
        self.isTopLevel = isTopLevel
        self.relation = relation if relation is not None else set()
        self.QVTRelation_Relation = QVTRelation_Relation if QVTRelation_Relation is not None else set()
        self.QVTRelation_Relation207 = QVTRelation_Relation207
        self.QVTRelation_Relation210 = QVTRelation_Relation210
        
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
        old_value = getattr(self, f"_QVTRelation_Relation__relation", None)
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
    def QVTRelation_Relation210(self):
        return self.__QVTRelation_Relation210

    @QVTRelation_Relation210.setter
    def QVTRelation_Relation210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTRelation_Relation__QVTRelation_Relation210", None)
        self.__QVTRelation_Relation210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern211"):
                opp_val = getattr(old_value, "Pattern211", None)
                if opp_val == self:
                    setattr(old_value, "Pattern211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern211"):
                opp_val = getattr(value, "Pattern211", None)
                setattr(value, "Pattern211", self)

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
                if hasattr(item, "Variable205"):
                    opp_val = getattr(item, "Variable205", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable205"):
                    opp_val = getattr(item, "Variable205", None)
                    
                    setattr(item, "Variable205", self)
                    

    @property
    def QVTRelation_Relation207(self):
        return self.__QVTRelation_Relation207

    @QVTRelation_Relation207.setter
    def QVTRelation_Relation207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTRelation_Relation__QVTRelation_Relation207", None)
        self.__QVTRelation_Relation207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pattern208"):
                opp_val = getattr(old_value, "Pattern208", None)
                if opp_val == self:
                    setattr(old_value, "Pattern208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pattern208"):
                opp_val = getattr(value, "Pattern208", None)
                setattr(value, "Pattern208", self)

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
class ImperativeOCL_ImperativeLoopExp(ImperativeExpression, LoopExp):

    pass
class EssentialOCL_IterateExp(LoopExp):

    pass
class NumericLiteralExp:

    pass
class EssentialOCL_UnlimitedNaturalExp(NumericLiteralExp):

    def __init__(self, symbol: str):
        self.symbol = symbol
        
        pass
    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol


class EssentialOCL_RealLiteralExp(NumericLiteralExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


class EssentialOCL_IntegerLiteralExp(NumericLiteralExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
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

    def __init__(self, isDeferred: str, isInverse: str, one: str, QVTOperational_ResolveExp: "OclExpression" = None, QVTOperational_ResolveExp422: "Variable" = None):
        self.isDeferred = isDeferred
        self.isInverse = isInverse
        self.one = one
        self.QVTOperational_ResolveExp = QVTOperational_ResolveExp
        self.QVTOperational_ResolveExp422 = QVTOperational_ResolveExp422
        
        pass
    @property
    def one(self):
        return self.__one

    @one.setter
    def one(self, one: str):
        self.__one = one


    @property
    def isInverse(self):
        return self.__isInverse

    @isInverse.setter
    def isInverse(self, isInverse: str):
        self.__isInverse = isInverse


    @property
    def isDeferred(self):
        return self.__isDeferred

    @isDeferred.setter
    def isDeferred(self, isDeferred: str):
        self.__isDeferred = isDeferred


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
            if hasattr(old_value, "OclExpression420"):
                opp_val = getattr(old_value, "OclExpression420", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression420", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression420"):
                opp_val = getattr(value, "OclExpression420", None)
                setattr(value, "OclExpression420", self)

    @property
    def QVTOperational_ResolveExp422(self):
        return self.__QVTOperational_ResolveExp422

    @QVTOperational_ResolveExp422.setter
    def QVTOperational_ResolveExp422(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ResolveExp__QVTOperational_ResolveExp422", None)
        self.__QVTOperational_ResolveExp422 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Variable423"):
                opp_val = getattr(old_value, "Variable423", None)
                if opp_val == self:
                    setattr(old_value, "Variable423", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Variable423"):
                opp_val = getattr(value, "Variable423", None)
                setattr(value, "Variable423", self)

class EssentialOCL_FeatureCallExp(CallExp):

    pass
class LiteralExp:

    pass
class EssentialOCL_PrimitiveLiteralExp(LiteralExp):

    pass
class EssentialOCL_NullLiteralExp(LiteralExp):

    pass
class ImperativeOCL_DictLiteralExp(LiteralExp):

    pass
class EssentialOCL_EnumLiteralExp(LiteralExp):

    pass
class ImperativeOCL_ListLiteralExp(LiteralExp):

    pass
class QVTTemplate_TemplateExp(LiteralExp):

    pass
class EssentialOCL_InvalidLiteralExp(LiteralExp):

    pass
class EssentialOCL_TupleLiteralExp(LiteralExp):

    pass
class EssentialOCL_CollectionLiteralExp(LiteralExp):

    def __init__(self, kind: str, collectionLiteralExp: set["CollectionLiteralPart"] = None):
        self.kind = kind
        self.collectionLiteralExp = collectionLiteralExp if collectionLiteralExp is not None else set()
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def collectionLiteralExp(self):
        return self.__collectionLiteralExp

    @collectionLiteralExp.setter
    def collectionLiteralExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EssentialOCL_CollectionLiteralExp__collectionLiteralExp", None)
        self.__collectionLiteralExp = value if value is not None else set()
        
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
                    

class CollectionLiteralPart:

    pass
class EssentialOCL_CollectionItem(CollectionLiteralPart):

    pass
class OclExpression:

    pass
class EssentialOCL_LetExp(OclExpression):

    pass
class EssentialOCL_LiteralExp(OclExpression):

    pass
class QVTRelation_RelationCallExp(OclExpression):

    pass
class EssentialOCL_IfExp(OclExpression):

    pass
class ImperativeOCL_ImperativeExpression(OclExpression):

    pass
class EssentialOCL_VariableExp(OclExpression):

    pass
class EssentialOCL_TypeExp(OclExpression):

    pass
class EssentialOCL_LoopExp(OclExpression, CallExp):

    pass
class EssentialOCL_CallExp(OclExpression):

    pass
class PrimitiveLiteralExp:

    pass
class EssentialOCL_StringLiteralExp(PrimitiveLiteralExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class EssentialOCL_NumericLiteralExp(PrimitiveLiteralExp):

    pass
class EssentialOCL_BooleanLiteralExp(PrimitiveLiteralExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class CollectionType:

    pass
class EssentialOCL_SetType(CollectionType):

    pass
class EssentialOCL_SequenceType(CollectionType):

    pass
class ImperativeOCL_ListType(CollectionType):

    pass
class ImperativeOCL_DictionaryType(CollectionType):

    pass
class EssentialOCL_OrderedSetType(CollectionType):

    pass
class EssentialOCL_BagType(CollectionType):

    pass
class Extent:

    pass
class EMOF_URIExtent(Extent):

    def __init__(self):
        
        pass
    def uri(self, EMOF_element) :
        # TODO: Implement uri method
        pass

    def element(self, EMOF_uri) :
        # TODO: Implement element method
        pass

    def contextURI(self) :
        # TODO: Implement contextURI method
        pass

class EssentialOCL_CollectionRange(CollectionLiteralPart):

    pass
class CollectionLiteralExp:

    pass
class ReflectiveCollection:

    pass
class EMOF_ReflectiveSequence(ReflectiveCollection):

    def __init__(self):
        
        pass
    def add(self, EMOF_index, EMOF_object):
        # TODO: Implement add method
        pass

    def remove(self, EMOF_index) :
        # TODO: Implement remove method
        pass

    def set(self, EMOF_object, EMOF_index) :
        # TODO: Implement set method
        pass

    def get(self, EMOF_index) :
        # TODO: Implement get method
        pass

class MultiplicityElement:

    pass
class TypedElement:

    pass
class EssentialOCL_TupleLiteralPart(TypedElement):

    pass
class EssentialOCL_ExpressionInOcl(TypedElement):

    pass
class EMOF_Property(MultiplicityElement, TypedElement):

    def __init__(self, default: str, isComposite: str, isDerived: str, isID: str, isReadOnly: str, ownedAttribute: "Class" = None, EMOF_Property: "Property" = None):
        self.default = default
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isID = isID
        self.isReadOnly = isReadOnly
        self.ownedAttribute = ownedAttribute
        self.EMOF_Property = EMOF_Property
        
        pass
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
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


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
    def EMOF_Property(self):
        return self.__EMOF_Property

    @EMOF_Property.setter
    def EMOF_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Property__EMOF_Property", None)
        self.__EMOF_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property24"):
                opp_val = getattr(old_value, "Property24", None)
                if opp_val == self:
                    setattr(old_value, "Property24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property24"):
                opp_val = getattr(value, "Property24", None)
                setattr(value, "Property24", self)

    @property
    def ownedAttribute(self):
        return self.__ownedAttribute

    @ownedAttribute.setter
    def ownedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Property__ownedAttribute", None)
        self.__ownedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class22"):
                opp_val = getattr(old_value, "Class22", None)
                if opp_val == self:
                    setattr(old_value, "Class22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class22"):
                opp_val = getattr(value, "Class22", None)
                setattr(value, "Class22", self)

class EssentialOCL_CollectionLiteralPart(TypedElement):

    pass
class EMOF_Parameter(MultiplicityElement, TypedElement):

    pass
class EssentialOCL_Variable(TypedElement):

    pass
class EssentialOCL_OclExpression(TypedElement):

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


class Package:

    pass
class Enumeration:

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
class Parameter:

    pass
class QVTBase_FunctionParameter(Variable, Parameter):

    pass
class QVTOperational_VarParameter(Variable, Parameter):

    def __init__(self, kind: str, context427: "ImperativeOperation" = None, result: "ImperativeOperation" = None, Parameter: "EMOF_Operation" = None, Parameter98: "EssentialOCL_Variable" = None, Variable70: "EssentialOCL_LetExp" = None, Variable262: "ImperativeOCL_CatchExp" = None, Variable100: "EssentialOCL_VariableExp" = None, Variable53: "EssentialOCL_ExpressionInOcl" = None, Variable323: "ImperativeOCL_VariableInitExp" = None, Variable423: "QVTOperational_ResolveExp" = None, Variable175: "QVTTemplate_CollectionTemplateExp" = None, Variable147: "QVTCore_CorePattern" = None, Variable385: "QVTOperational_Module" = None, Variable226: "QVTRelation_RelationDomainAssignment" = None, Variable187: "QVTTemplate_TemplateExp" = None, Variable286: "ImperativeOCL_InstantiationExp" = None, Variable75: "EssentialOCL_LoopExp" = None, Variable: "EssentialOCL_ExpressionInOcl" = None, Variable168: "QVTCore_VariableAssignment" = None, Variable267: "ImperativeOCL_ComputeExp" = None, Variable404: "QVTOperational_OperationBody" = None, Variable66: "EssentialOCL_IterateExp" = None, Variable106: "QVTBase_Pattern" = None, Variable56: "EssentialOCL_ExpressionInOcl" = None, Variable205: "QVTRelation_Relation" = None, Variable397: "QVTOperational_ObjectExp" = None, Variable219: "QVTRelation_RelationDomain" = None, Variable279: "ImperativeOCL_ImperativeIterateExp" = None):
        self.kind = kind
        self.context427 = context427
        self.result = result
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_VarParameter__result", None)
        self.__result = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation430"):
                opp_val = getattr(old_value, "ImperativeOperation430", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation430", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation430"):
                opp_val = getattr(value, "ImperativeOperation430", None)
                setattr(value, "ImperativeOperation430", self)

    @property
    def context427(self):
        return self.__context427

    @context427.setter
    def context427(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_VarParameter__context427", None)
        self.__context427 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ImperativeOperation428"):
                opp_val = getattr(old_value, "ImperativeOperation428", None)
                if opp_val == self:
                    setattr(old_value, "ImperativeOperation428", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ImperativeOperation428"):
                opp_val = getattr(value, "ImperativeOperation428", None)
                setattr(value, "ImperativeOperation428", self)

class Object:

    pass
class EMOF_Extent(Object):

    def __init__(self):
        
        pass
    def elements(self) :
        # TODO: Implement elements method
        pass

    def useContainment(self) :
        # TODO: Implement useContainment method
        pass

class EMOF_ReflectiveCollection(Object):

    def __init__(self):
        
        pass
    def remove(self, EMOF_object) :
        # TODO: Implement remove method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def add(self, EMOF_object) :
        # TODO: Implement add method
        pass

    def size(self) :
        # TODO: Implement size method
        pass

    def addAll(self, EMOF_objects) :
        # TODO: Implement addAll method
        pass

class EMOF_Element(Object):

    def __init__(self, EMOF_Element: set["Comment"] = None):
        self.EMOF_Element = EMOF_Element if EMOF_Element is not None else set()
        
        pass
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
                    

    def get(self, EMOF_property) :
        # TODO: Implement get method
        pass

    def getMetaClass(self) :
        # TODO: Implement getMetaClass method
        pass

    def unset(self, EMOF_property):
        # TODO: Implement unset method
        pass

    def set(self, EMOF_property, EMOF_object):
        # TODO: Implement set method
        pass

    def isSet(self, EMOF_property) :
        # TODO: Implement isSet method
        pass

    def container(self) :
        # TODO: Implement container method
        pass

    def equals(self, EMOF_object) :
        # TODO: Implement equals method
        pass

class NamedElement:

    pass
class QVTBase_Domain(NamedElement):

    def __init__(self, isCheckable: str, isEnforceable: str, domain: "Rule" = None, QVTBase_Domain: "TypedModel" = None, NamedElement: "EMOF_Comment" = None):
        self.isCheckable = isCheckable
        self.isEnforceable = isEnforceable
        self.domain = domain
        self.QVTBase_Domain = QVTBase_Domain
        
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
    def domain(self):
        return self.__domain

    @domain.setter
    def domain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTBase_Domain__domain", None)
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

class EMOF_Type(NamedElement):

    def __init__(self, ownedType: "Package" = None, NamedElement: "EMOF_Comment" = None):
        self.ownedType = ownedType
        
        pass
    @property
    def ownedType(self):
        return self.__ownedType

    @ownedType.setter
    def ownedType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Type__ownedType", None)
        self.__ownedType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package27"):
                opp_val = getattr(old_value, "Package27", None)
                if opp_val == self:
                    setattr(old_value, "Package27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package27"):
                opp_val = getattr(value, "Package27", None)
                setattr(value, "Package27", self)

    def isInstance(self, EMOF_object) :
        # TODO: Implement isInstance method
        pass

class EMOF_Package(NamedElement):

    def __init__(self, uri: str, nestingPackage: set["Package"] = None, nestedPackage: "Package" = None, package: set["Type"] = None, NamedElement: "EMOF_Comment" = None):
        self.uri = uri
        self.nestingPackage = nestingPackage if nestingPackage is not None else set()
        self.nestedPackage = nestedPackage
        self.package = package if package is not None else set()
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def nestedPackage(self):
        return self.__nestedPackage

    @nestedPackage.setter
    def nestedPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__nestedPackage", None)
        self.__nestedPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Package16"):
                opp_val = getattr(old_value, "Package16", None)
                if opp_val == self:
                    setattr(old_value, "Package16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Package16"):
                opp_val = getattr(value, "Package16", None)
                setattr(value, "Package16", self)

    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__package", None)
        self.__package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Type18"):
                    opp_val = getattr(item, "Type18", None)
                    
                    if opp_val == self:
                        setattr(item, "Type18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Type18"):
                    opp_val = getattr(item, "Type18", None)
                    
                    setattr(item, "Type18", self)
                    

    @property
    def nestingPackage(self):
        return self.__nestingPackage

    @nestingPackage.setter
    def nestingPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Package__nestingPackage", None)
        self.__nestingPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package14"):
                    opp_val = getattr(item, "Package14", None)
                    
                    if opp_val == self:
                        setattr(item, "Package14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package14"):
                    opp_val = getattr(item, "Package14", None)
                    
                    setattr(item, "Package14", self)
                    

class QVTBase_TypedModel(NamedElement):

    pass
class QVTBase_Rule(NamedElement):

    pass
class EMOF_EnumerationLiteral(NamedElement):

    pass
class EMOF_TypedElement(NamedElement):

    pass
class Element:

    pass
class QVTOperational_ModuleImport(Element):

    def __init__(self, kind: str, QVTOperational_ModuleImport: set["ModelType"] = None, QVTOperational_ModuleImport391: "Module" = None, moduleImport: "Module" = None, Element: "EMOF_Tag" = None):
        self.kind = kind
        self.QVTOperational_ModuleImport = QVTOperational_ModuleImport if QVTOperational_ModuleImport is not None else set()
        self.QVTOperational_ModuleImport391 = QVTOperational_ModuleImport391
        self.moduleImport = moduleImport
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def QVTOperational_ModuleImport391(self):
        return self.__QVTOperational_ModuleImport391

    @QVTOperational_ModuleImport391.setter
    def QVTOperational_ModuleImport391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__QVTOperational_ModuleImport391", None)
        self.__QVTOperational_ModuleImport391 = value
        
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
    def moduleImport(self):
        return self.__moduleImport

    @moduleImport.setter
    def moduleImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModuleImport__moduleImport", None)
        self.__moduleImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module393"):
                opp_val = getattr(old_value, "Module393", None)
                if opp_val == self:
                    setattr(old_value, "Module393", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module393"):
                opp_val = getattr(value, "Module393", None)
                setattr(value, "Module393", self)

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
                if hasattr(item, "ModelType389"):
                    opp_val = getattr(item, "ModelType389", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelType389", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelType389"):
                    opp_val = getattr(item, "ModelType389", None)
                    
                    setattr(item, "ModelType389", self)
                    

class QVTCore_EnforcementOperation(Element):

    def __init__(self, enforcementMode: str, enforcementOperation: "BottomPattern" = None, QVTCore_EnforcementOperation: "OperationCallExp" = None, Element: "EMOF_Tag" = None):
        self.enforcementMode = enforcementMode
        self.enforcementOperation = enforcementOperation
        self.QVTCore_EnforcementOperation = QVTCore_EnforcementOperation
        
        pass
    @property
    def enforcementMode(self):
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
        old_value = getattr(self, f"_QVTCore_EnforcementOperation__enforcementOperation", None)
        self.__enforcementOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottomPattern149"):
                opp_val = getattr(old_value, "BottomPattern149", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern149"):
                opp_val = getattr(value, "BottomPattern149", None)
                setattr(value, "BottomPattern149", self)

class EMOF_NamedElement(Element):

    def __init__(self, name: str, Element: "EMOF_Tag" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class QVTTemplate_PropertyTemplateItem(Element):

    def __init__(self, isOpposite: str, part180: "ObjectTemplateExp" = None, QVTTemplate_PropertyTemplateItem: "Property" = None, QVTTemplate_PropertyTemplateItem184: "OclExpression" = None, Element: "EMOF_Tag" = None):
        self.isOpposite = isOpposite
        self.part180 = part180
        self.QVTTemplate_PropertyTemplateItem = QVTTemplate_PropertyTemplateItem
        self.QVTTemplate_PropertyTemplateItem184 = QVTTemplate_PropertyTemplateItem184
        
        pass
    @property
    def isOpposite(self):
        return self.__isOpposite

    @isOpposite.setter
    def isOpposite(self, isOpposite: str):
        self.__isOpposite = isOpposite


    @property
    def part180(self):
        return self.__part180

    @part180.setter
    def part180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTTemplate_PropertyTemplateItem__part180", None)
        self.__part180 = value
        
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
    def QVTTemplate_PropertyTemplateItem(self):
        return self.__QVTTemplate_PropertyTemplateItem

    @QVTTemplate_PropertyTemplateItem.setter
    def QVTTemplate_PropertyTemplateItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTTemplate_PropertyTemplateItem__QVTTemplate_PropertyTemplateItem", None)
        self.__QVTTemplate_PropertyTemplateItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Property182"):
                opp_val = getattr(old_value, "Property182", None)
                if opp_val == self:
                    setattr(old_value, "Property182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Property182"):
                opp_val = getattr(value, "Property182", None)
                setattr(value, "Property182", self)

    @property
    def QVTTemplate_PropertyTemplateItem184(self):
        return self.__QVTTemplate_PropertyTemplateItem184

    @QVTTemplate_PropertyTemplateItem184.setter
    def QVTTemplate_PropertyTemplateItem184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTTemplate_PropertyTemplateItem__QVTTemplate_PropertyTemplateItem184", None)
        self.__QVTTemplate_PropertyTemplateItem184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression185"):
                opp_val = getattr(old_value, "OclExpression185", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression185"):
                opp_val = getattr(value, "OclExpression185", None)
                setattr(value, "OclExpression185", self)

class ImperativeOCL_DictLiteralPart(Element):

    pass
class QVTRelation_RelationDomainAssignment(Element):

    pass
class QVTRelation_Key(Element):

    pass
class QVTBase_Pattern(Element):

    pass
class QVTCore_Assignment(Element):

    def __init__(self, isDefault: str, QVTCore_Assignment: "OclExpression" = None, assignment: "BottomPattern" = None, Element: "EMOF_Tag" = None):
        self.isDefault = isDefault
        self.QVTCore_Assignment = QVTCore_Assignment
        self.assignment = assignment
        
        pass
    @property
    def isDefault(self):
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: str):
        self.__isDefault = isDefault


    @property
    def assignment(self):
        return self.__assignment

    @assignment.setter
    def assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTCore_Assignment__assignment", None)
        self.__assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BottomPattern136"):
                opp_val = getattr(old_value, "BottomPattern136", None)
                if opp_val == self:
                    setattr(old_value, "BottomPattern136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BottomPattern136"):
                opp_val = getattr(value, "BottomPattern136", None)
                setattr(value, "BottomPattern136", self)

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
            if hasattr(old_value, "OclExpression138"):
                opp_val = getattr(old_value, "OclExpression138", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression138"):
                opp_val = getattr(value, "OclExpression138", None)
                setattr(value, "OclExpression138", self)

class EMOF_Factory(Element):

    def __init__(self, EMOF_Factory: "Package" = None, Element: "EMOF_Tag" = None):
        self.EMOF_Factory = EMOF_Factory
        
        pass
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

    def createFromString(self, EMOF_string, EMOF_dataType) :
        # TODO: Implement createFromString method
        pass

    def convertToString(self, EMOF_dataType, EMOF_object) :
        # TODO: Implement convertToString method
        pass

    def create(self, EMOF_metaClass) :
        # TODO: Implement create method
        pass

class QVTBase_Predicate(Element):

    pass
class QVTRelation_RelationImplementation(Element):

    pass
class QVTOperational_OperationBody(Element):

    pass
class EMOF_Tag(Element):

    def __init__(self, name: str, value: str, EMOF_Tag: set["Element"] = None, Element: "EMOF_Tag" = None):
        self.name = name
        self.value = value
        self.EMOF_Tag = EMOF_Tag if EMOF_Tag is not None else set()
        
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
                    

class EMOF_Comment(Element):

    def __init__(self, body: str, EMOF_Comment: set["NamedElement"] = None, Element: "EMOF_Tag" = None):
        self.body = body
        self.EMOF_Comment = EMOF_Comment if EMOF_Comment is not None else set()
        
        pass
    @property
    def body(self):
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
class QVTOperational_ModelType(Class):

    def __init__(self, conformanceKind: str, QVTOperational_ModelType: set["OclExpression"] = None, QVTOperational_ModelType373: set["Package"] = None, Class178: "QVTTemplate_ObjectTemplateExp" = None, Class22: "EMOF_Property" = None, Class10: "EMOF_Operation" = None, Class406: "QVTOperational_OperationalTransformation" = None, Class330: "QVTOperational_ContextualProperty" = None, Class: "EMOF_Class" = None, Class289: "ImperativeOCL_InstantiationExp" = None, Class195: "QVTRelation_Key" = None):
        self.conformanceKind = conformanceKind
        self.QVTOperational_ModelType = QVTOperational_ModelType if QVTOperational_ModelType is not None else set()
        self.QVTOperational_ModelType373 = QVTOperational_ModelType373 if QVTOperational_ModelType373 is not None else set()
        
        pass
    @property
    def conformanceKind(self):
        return self.__conformanceKind

    @conformanceKind.setter
    def conformanceKind(self, conformanceKind: str):
        self.__conformanceKind = conformanceKind


    @property
    def QVTOperational_ModelType373(self):
        return self.__QVTOperational_ModelType373

    @QVTOperational_ModelType373.setter
    def QVTOperational_ModelType373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ModelType__QVTOperational_ModelType373", None)
        self.__QVTOperational_ModelType373 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Package374"):
                    opp_val = getattr(item, "Package374", None)
                    
                    if opp_val == self:
                        setattr(item, "Package374", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Package374"):
                    opp_val = getattr(item, "Package374", None)
                    
                    setattr(item, "Package374", self)
                    

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
                if hasattr(item, "OclExpression371"):
                    opp_val = getattr(item, "OclExpression371", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression371", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression371"):
                    opp_val = getattr(item, "OclExpression371", None)
                    
                    setattr(item, "OclExpression371", self)
                    

class QVTOperational_Module(Class, Package):

    def __init__(self, isBlackbox: str, QVTOperational_Module381: set["Tag"] = None, QVTOperational_Module384: set["Variable"] = None, QVTOperational_Module387: set["ModelType"] = None, QVTOperational_Module: set["Property"] = None, QVTOperational_Module378: "EntryOperation" = None, module: set["ModuleImport"] = None, Class178: "QVTTemplate_ObjectTemplateExp" = None, Class22: "EMOF_Property" = None, Class10: "EMOF_Operation" = None, Class406: "QVTOperational_OperationalTransformation" = None, Class330: "QVTOperational_ContextualProperty" = None, Class: "EMOF_Class" = None, Class289: "ImperativeOCL_InstantiationExp" = None, Class195: "QVTRelation_Key" = None, Package27: "EMOF_Type" = None, Package: "EMOF_Factory" = None, Package131: "QVTBase_TypedModel" = None, Package14: "EMOF_Package" = None, Package374: "QVTOperational_ModelType" = None, Package16: "EMOF_Package" = None):
        self.isBlackbox = isBlackbox
        self.QVTOperational_Module381 = QVTOperational_Module381 if QVTOperational_Module381 is not None else set()
        self.QVTOperational_Module384 = QVTOperational_Module384 if QVTOperational_Module384 is not None else set()
        self.QVTOperational_Module387 = QVTOperational_Module387 if QVTOperational_Module387 is not None else set()
        self.QVTOperational_Module = QVTOperational_Module if QVTOperational_Module is not None else set()
        self.QVTOperational_Module378 = QVTOperational_Module378
        self.module = module if module is not None else set()
        
        pass
    @property
    def isBlackbox(self):
        return self.__isBlackbox

    @isBlackbox.setter
    def isBlackbox(self, isBlackbox: str):
        self.__isBlackbox = isBlackbox


    @property
    def QVTOperational_Module378(self):
        return self.__QVTOperational_Module378

    @QVTOperational_Module378.setter
    def QVTOperational_Module378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module378", None)
        self.__QVTOperational_Module378 = value
        
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
    def module(self):
        return self.__module

    @module.setter
    def module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__module", None)
        self.__module = value if value is not None else set()
        
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
                if hasattr(item, "Property376"):
                    opp_val = getattr(item, "Property376", None)
                    
                    if opp_val == self:
                        setattr(item, "Property376", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property376"):
                    opp_val = getattr(item, "Property376", None)
                    
                    setattr(item, "Property376", self)
                    

    @property
    def QVTOperational_Module384(self):
        return self.__QVTOperational_Module384

    @QVTOperational_Module384.setter
    def QVTOperational_Module384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module384", None)
        self.__QVTOperational_Module384 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable385"):
                    opp_val = getattr(item, "Variable385", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable385", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable385"):
                    opp_val = getattr(item, "Variable385", None)
                    
                    setattr(item, "Variable385", self)
                    

    @property
    def QVTOperational_Module387(self):
        return self.__QVTOperational_Module387

    @QVTOperational_Module387.setter
    def QVTOperational_Module387(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module387", None)
        self.__QVTOperational_Module387 = value if value is not None else set()
        
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
    def QVTOperational_Module381(self):
        return self.__QVTOperational_Module381

    @QVTOperational_Module381.setter
    def QVTOperational_Module381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_Module__QVTOperational_Module381", None)
        self.__QVTOperational_Module381 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tag382"):
                    opp_val = getattr(item, "Tag382", None)
                    
                    if opp_val == self:
                        setattr(item, "Tag382", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tag382"):
                    opp_val = getattr(item, "Tag382", None)
                    
                    setattr(item, "Tag382", self)
                    

class EssentialOCL_TupleType(DataType, Class):

    pass
class QVTBase_Transformation(Class, Package):

    pass
class ImperativeOCL_Typedef(Class):

    pass
class Operation:

    pass
class QVTBase_Function(Operation):

    pass
class QVTOperational_ImperativeOperation(Operation):

    def __init__(self, isBlackbox: str, operation338: "OperationBody" = None, ctxOwner: "VarParameter" = None, QVTOperational_ImperativeOperation: "ImperativeOperation" = None, resOwner: set["VarParameter"] = None, Operation20: "EMOF_Parameter" = None, Operation: "EMOF_Class" = None, Operation292: "ImperativeOCL_InstantiationExp" = None, Operation80: "EssentialOCL_OperationCallExp" = None, Operation228: "QVTRelation_RelationImplementation" = None):
        self.isBlackbox = isBlackbox
        self.operation338 = operation338
        self.ctxOwner = ctxOwner
        self.QVTOperational_ImperativeOperation = QVTOperational_ImperativeOperation
        self.resOwner = resOwner if resOwner is not None else set()
        
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
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__ctxOwner", None)
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
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__resOwner", None)
        self.__resOwner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarParameter342"):
                    opp_val = getattr(item, "VarParameter342", None)
                    
                    if opp_val == self:
                        setattr(item, "VarParameter342", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarParameter342"):
                    opp_val = getattr(item, "VarParameter342", None)
                    
                    setattr(item, "VarParameter342", self)
                    

    @property
    def operation338(self):
        return self.__operation338

    @operation338.setter
    def operation338(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_QVTOperational_ImperativeOperation__operation338", None)
        self.__operation338 = value
        
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

class Property:

    pass
class QVTOperational_ContextualProperty(Property):

    pass
class Type:

    pass
class EssentialOCL_InvalidType(Type):

    pass
class EMOF_DataType(Type):

    pass
class EssentialOCL_AnyType(Type):

    pass
class EssentialOCL_TemplateParameterType(Type):

    def __init__(self, specification: str, Type313: "ImperativeOCL_Typedef" = None, Type277: "ImperativeOCL_DictionaryType" = None, Type41: "EssentialOCL_CollectionType" = None, Type29: "EMOF_TypedElement" = None, Type301: "ImperativeOCL_RaiseExp" = None, Type259: "ImperativeOCL_CatchExp" = None, Type: "EMOF_Operation" = None, Type50: "EssentialOCL_ExpressionInOcl" = None, Type92: "EssentialOCL_TypeExp" = None, Type18: "EMOF_Package" = None):
        self.specification = specification
        
        pass
    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


class EssentialOCL_VoidType(Type):

    pass
class EMOF_Class(Type):

    def __init__(self, isAbstract: str, class_: set["Property"] = None, class_2: set["Operation"] = None, EMOF_Class: set["Class"] = None, Type313: "ImperativeOCL_Typedef" = None, Type277: "ImperativeOCL_DictionaryType" = None, Type41: "EssentialOCL_CollectionType" = None, Type29: "EMOF_TypedElement" = None, Type301: "ImperativeOCL_RaiseExp" = None, Type259: "ImperativeOCL_CatchExp" = None, Type: "EMOF_Operation" = None, Type50: "EssentialOCL_ExpressionInOcl" = None, Type92: "EssentialOCL_TypeExp" = None, Type18: "EMOF_Package" = None):
        self.isAbstract = isAbstract
        self.class_ = class_ if class_ is not None else set()
        self.class_2 = class_2 if class_2 is not None else set()
        self.EMOF_Class = EMOF_Class if EMOF_Class is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def class_(self):
        return self.__class_

    @class_.setter
    def class_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Class__class_", None)
        self.__class_ = value if value is not None else set()
        
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
    def class_2(self):
        return self.__class_2

    @class_2.setter
    def class_2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EMOF_Class__class_2", None)
        self.__class_2 = value if value is not None else set()
        
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
                    

class Comment:

    pass