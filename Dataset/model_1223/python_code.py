from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DirectionKindEnum(Enum):
    DEFAULT = "DEFAULT"
    in = "in"
    out = "out"
    inout = "inout"
class QualifierKindCS(Enum):
    abstract = "abstract"
    blackbox = "blackbox"
    static = "static"
class MappingExtensionKindCS(Enum):
    disjuncts = "disjuncts"
    merges = "merges"
    inherits = "inherits"
class ImportKindEnum(Enum):
    extension = "extension"
    access = "access"
class ModuleKindEnum(Enum):
    transformation = "transformation"
    library = "library"


############################################
# Definition of Classes
############################################

class CollectionLiteralPartCS:

    pass
class LiteralExpCS:

    pass
class qvtoperational_cst_DictLiteralExpCS(LiteralExpCS):

    pass
class qvtoperational_cst_ListLiteralExpCS(LiteralExpCS):

    pass
class DictLiteralPartCS:

    pass
class LogExpCS:

    pass
class TransformationRefineCS:

    pass
class ModuleUsageCS:

    pass
class ModuleRefCS:

    pass
class ModuleKindCS:

    pass
class PackageRefCS:

    pass
class CallExpCS:

    pass
class qvtoperational_cst_ResolveExpCS(CallExpCS):

    def __init__(self, isInverse: bool, isDeferred: bool, one: bool, qvtoperational_cst_ResolveExpCS: "VariableCS" = None, qvtoperational_cst_ResolveExpCS158: "OCLExpressionCS" = None):
        self.isInverse = isInverse
        self.isDeferred = isDeferred
        self.one = one
        self.qvtoperational_cst_ResolveExpCS = qvtoperational_cst_ResolveExpCS
        self.qvtoperational_cst_ResolveExpCS158 = qvtoperational_cst_ResolveExpCS158
        
    @property
    def isInverse(self) -> bool:
        return self.__isInverse

    @isInverse.setter
    def isInverse(self, isInverse: bool):
        self.__isInverse = isInverse

    @property
    def isDeferred(self) -> bool:
        return self.__isDeferred

    @isDeferred.setter
    def isDeferred(self, isDeferred: bool):
        self.__isDeferred = isDeferred

    @property
    def one(self) -> bool:
        return self.__one

    @one.setter
    def one(self, one: bool):
        self.__one = one

    @property
    def qvtoperational_cst_ResolveExpCS(self):
        return self.__qvtoperational_cst_ResolveExpCS

    @qvtoperational_cst_ResolveExpCS.setter
    def qvtoperational_cst_ResolveExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ResolveExpCS__qvtoperational_cst_ResolveExpCS", None)
        self.__qvtoperational_cst_ResolveExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableCS156"):
                opp_val = getattr(old_value, "VariableCS156", None)
                if opp_val == self:
                    setattr(old_value, "VariableCS156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableCS156"):
                opp_val = getattr(value, "VariableCS156", None)
                setattr(value, "VariableCS156", self)

    @property
    def qvtoperational_cst_ResolveExpCS158(self):
        return self.__qvtoperational_cst_ResolveExpCS158

    @qvtoperational_cst_ResolveExpCS158.setter
    def qvtoperational_cst_ResolveExpCS158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ResolveExpCS__qvtoperational_cst_ResolveExpCS158", None)
        self.__qvtoperational_cst_ResolveExpCS158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS159"):
                opp_val = getattr(old_value, "OCLExpressionCS159", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS159"):
                opp_val = getattr(value, "OCLExpressionCS159", None)
                setattr(value, "OCLExpressionCS159", self)

class qvtoperational_cst_ElementWithBody(ABC):

    def __init__(self, bodyStartLocation: int, bodyEndLocation: int):
        self.bodyStartLocation = bodyStartLocation
        self.bodyEndLocation = bodyEndLocation
        
    @property
    def bodyStartLocation(self) -> int:
        return self.__bodyStartLocation

    @bodyStartLocation.setter
    def bodyStartLocation(self, bodyStartLocation: int):
        self.__bodyStartLocation = bodyStartLocation

    @property
    def bodyEndLocation(self) -> int:
        return self.__bodyEndLocation

    @bodyEndLocation.setter
    def bodyEndLocation(self, bodyEndLocation: int):
        self.__bodyEndLocation = bodyEndLocation

class ResolveExpCS:

    pass
class qvtoperational_cst_ResolveInExpCS(ResolveExpCS):

    pass
class OperationCallExpCS:

    pass
class qvtoperational_cst_LogExpCS(OperationCallExpCS):

    pass
class qvtoperational_cst_ImperativeOperationCallExpCS(OperationCallExpCS):

    pass
class ImperativeOperationCallExpCS:

    pass
class qvtoperational_cst_MappingCallExpCS(ImperativeOperationCallExpCS):

    def __init__(self, strict: bool):
        self.strict = strict
        
    @property
    def strict(self) -> bool:
        return self.__strict

    @strict.setter
    def strict(self, strict: bool):
        self.__strict = strict

class cst_InstantiationExpCS:

    pass
class cst_StatementCS:

    pass
class cst_LoopExpCS:

    pass
class qvtoperational_cst_ImperativeLoopExpCS(cst_StatementCS, cst_LoopExpCS):

    pass
class SwitchAltExpCS:

    pass
class ImperativeLoopExpCS:

    pass
class qvtoperational_cst_ImperativeIterateExpCS(ImperativeLoopExpCS):

    pass
class qvtoperational_cst_ForExpCS(ImperativeLoopExpCS):

    pass
class StatementCS:

    pass
class qvtoperational_cst_SwitchAltExpCS(StatementCS):

    pass
class qvtoperational_cst_SwitchExpCS(StatementCS):

    pass
class qvtoperational_cst_ReturnExpCS(StatementCS):

    pass
class qvtoperational_cst_ContinueExpCS(StatementCS):

    pass
class qvtoperational_cst_AssertExpCS(StatementCS):

    pass
class qvtoperational_cst_VariableInitializationCS(StatementCS):

    def __init__(self, withResult: bool, qvtoperational_cst_VariableInitializationCS136: "SimpleNameCS" = None, qvtoperational_cst_VariableInitializationCS139: "TypeCS" = None, qvtoperational_cst_VariableInitializationCS: "OCLExpressionCS" = None):
        self.withResult = withResult
        self.qvtoperational_cst_VariableInitializationCS136 = qvtoperational_cst_VariableInitializationCS136
        self.qvtoperational_cst_VariableInitializationCS139 = qvtoperational_cst_VariableInitializationCS139
        self.qvtoperational_cst_VariableInitializationCS = qvtoperational_cst_VariableInitializationCS
        
    @property
    def withResult(self) -> bool:
        return self.__withResult

    @withResult.setter
    def withResult(self, withResult: bool):
        self.__withResult = withResult

    @property
    def qvtoperational_cst_VariableInitializationCS(self):
        return self.__qvtoperational_cst_VariableInitializationCS

    @qvtoperational_cst_VariableInitializationCS.setter
    def qvtoperational_cst_VariableInitializationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_VariableInitializationCS__qvtoperational_cst_VariableInitializationCS", None)
        self.__qvtoperational_cst_VariableInitializationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS134"):
                opp_val = getattr(old_value, "OCLExpressionCS134", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS134"):
                opp_val = getattr(value, "OCLExpressionCS134", None)
                setattr(value, "OCLExpressionCS134", self)

    @property
    def qvtoperational_cst_VariableInitializationCS136(self):
        return self.__qvtoperational_cst_VariableInitializationCS136

    @qvtoperational_cst_VariableInitializationCS136.setter
    def qvtoperational_cst_VariableInitializationCS136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_VariableInitializationCS__qvtoperational_cst_VariableInitializationCS136", None)
        self.__qvtoperational_cst_VariableInitializationCS136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS137"):
                opp_val = getattr(old_value, "SimpleNameCS137", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS137"):
                opp_val = getattr(value, "SimpleNameCS137", None)
                setattr(value, "SimpleNameCS137", self)

    @property
    def qvtoperational_cst_VariableInitializationCS139(self):
        return self.__qvtoperational_cst_VariableInitializationCS139

    @qvtoperational_cst_VariableInitializationCS139.setter
    def qvtoperational_cst_VariableInitializationCS139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_VariableInitializationCS__qvtoperational_cst_VariableInitializationCS139", None)
        self.__qvtoperational_cst_VariableInitializationCS139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeCS140"):
                opp_val = getattr(old_value, "TypeCS140", None)
                if opp_val == self:
                    setattr(old_value, "TypeCS140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeCS140"):
                opp_val = getattr(value, "TypeCS140", None)
                setattr(value, "TypeCS140", self)

class qvtoperational_cst_BreakExpCS(StatementCS):

    pass
class qvtoperational_cst_AssignStatementCS(StatementCS):

    def __init__(self, incremental: bool, qvtoperational_cst_AssignStatementCS: "OCLExpressionCS" = None, qvtoperational_cst_AssignStatementCS144: "OCLExpressionCS" = None):
        self.incremental = incremental
        self.qvtoperational_cst_AssignStatementCS = qvtoperational_cst_AssignStatementCS
        self.qvtoperational_cst_AssignStatementCS144 = qvtoperational_cst_AssignStatementCS144
        
    @property
    def incremental(self) -> bool:
        return self.__incremental

    @incremental.setter
    def incremental(self, incremental: bool):
        self.__incremental = incremental

    @property
    def qvtoperational_cst_AssignStatementCS144(self):
        return self.__qvtoperational_cst_AssignStatementCS144

    @qvtoperational_cst_AssignStatementCS144.setter
    def qvtoperational_cst_AssignStatementCS144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_AssignStatementCS__qvtoperational_cst_AssignStatementCS144", None)
        self.__qvtoperational_cst_AssignStatementCS144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS145"):
                opp_val = getattr(old_value, "OCLExpressionCS145", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS145"):
                opp_val = getattr(value, "OCLExpressionCS145", None)
                setattr(value, "OCLExpressionCS145", self)

    @property
    def qvtoperational_cst_AssignStatementCS(self):
        return self.__qvtoperational_cst_AssignStatementCS

    @qvtoperational_cst_AssignStatementCS.setter
    def qvtoperational_cst_AssignStatementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_AssignStatementCS__qvtoperational_cst_AssignStatementCS", None)
        self.__qvtoperational_cst_AssignStatementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCLExpressionCS142"):
                opp_val = getattr(old_value, "OCLExpressionCS142", None)
                if opp_val == self:
                    setattr(old_value, "OCLExpressionCS142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCLExpressionCS142"):
                opp_val = getattr(value, "OCLExpressionCS142", None)
                setattr(value, "OCLExpressionCS142", self)

class qvtoperational_cst_ExpressionStatementCS(StatementCS):

    pass
class qvtoperational_cst_InstantiationExpCS(StatementCS):

    pass
class qvtoperational_cst_BlockExpCS(StatementCS):

    pass
class MappingEndCS:

    pass
class MappingBodyCS:

    pass
class qvtoperational_cst_WhileExpCS(StatementCS):

    pass
class VariableCS:

    pass
class qvtoperational_cst_ComputeExpCS(StatementCS):

    pass
class MappingSectionsCS:

    pass
class MappingInitCS:

    pass
class MappingSectionCS:

    pass
class qvtoperational_cst_MappingEndCS(MappingSectionCS):

    pass
class qvtoperational_cst_MappingBodyCS(MappingSectionCS):

    def __init__(self, hasPopulationKeyword: bool):
        self.hasPopulationKeyword = hasPopulationKeyword
        
    @property
    def hasPopulationKeyword(self) -> bool:
        return self.__hasPopulationKeyword

    @hasPopulationKeyword.setter
    def hasPopulationKeyword(self, hasPopulationKeyword: bool):
        self.__hasPopulationKeyword = hasPopulationKeyword

class qvtoperational_cst_MappingInitCS(MappingSectionCS):

    pass
class MappingRuleCS:

    pass
class cst_ElementWithBody:

    pass
class qvtoperational_cst_ObjectExpCS(cst_InstantiationExpCS, cst_ElementWithBody):

    def __init__(self, isImplicit: bool, qvtoperational_cst_ObjectExpCS: "SimpleNameCS" = None, qvtoperational_cst_ObjectExpCS151: set["OCLExpressionCS"] = None):
        self.isImplicit = isImplicit
        self.qvtoperational_cst_ObjectExpCS = qvtoperational_cst_ObjectExpCS
        self.qvtoperational_cst_ObjectExpCS151 = qvtoperational_cst_ObjectExpCS151 if qvtoperational_cst_ObjectExpCS151 is not None else set()
        
    @property
    def isImplicit(self) -> bool:
        return self.__isImplicit

    @isImplicit.setter
    def isImplicit(self, isImplicit: bool):
        self.__isImplicit = isImplicit

    @property
    def qvtoperational_cst_ObjectExpCS(self):
        return self.__qvtoperational_cst_ObjectExpCS

    @qvtoperational_cst_ObjectExpCS.setter
    def qvtoperational_cst_ObjectExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ObjectExpCS__qvtoperational_cst_ObjectExpCS", None)
        self.__qvtoperational_cst_ObjectExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS149"):
                opp_val = getattr(old_value, "SimpleNameCS149", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS149"):
                opp_val = getattr(value, "SimpleNameCS149", None)
                setattr(value, "SimpleNameCS149", self)

    @property
    def qvtoperational_cst_ObjectExpCS151(self):
        return self.__qvtoperational_cst_ObjectExpCS151

    @qvtoperational_cst_ObjectExpCS151.setter
    def qvtoperational_cst_ObjectExpCS151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ObjectExpCS__qvtoperational_cst_ObjectExpCS151", None)
        self.__qvtoperational_cst_ObjectExpCS151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCLExpressionCS152"):
                    opp_val = getattr(item, "OCLExpressionCS152", None)
                    
                    if opp_val == self:
                        setattr(item, "OCLExpressionCS152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCLExpressionCS152"):
                    opp_val = getattr(item, "OCLExpressionCS152", None)
                    
                    setattr(item, "OCLExpressionCS152", self)
                    

class cst_CSTNode:

    pass
class qvtoperational_cst_ModelTypeCS(cst_ElementWithBody, cst_CSTNode):

    pass
class qvtoperational_cst_MappingSectionCS(cst_ElementWithBody, cst_CSTNode):

    pass
class MappingExtensionCS:

    pass
class DirectionKindCS:

    pass
class ParameterDeclarationCS:

    pass
class MappingDeclarationCS:

    pass
class SimpleSignatureCS:

    pass
class TypeSpecCS:

    pass
class LocalPropertyCS:

    pass
class qvtoperational_cst_ClassifierPropertyCS(LocalPropertyCS):

    def __init__(self, isOrdered: bool, qvtoperational_cst_ClassifierPropertyCS: set["SimpleNameCS"] = None, qvtoperational_cst_ClassifierPropertyCS49: set["SimpleNameCS"] = None, qvtoperational_cst_ClassifierPropertyCS52: "MultiplicityDefCS" = None, qvtoperational_cst_ClassifierPropertyCS54: "OppositePropertyCS" = None):
        self.isOrdered = isOrdered
        self.qvtoperational_cst_ClassifierPropertyCS = qvtoperational_cst_ClassifierPropertyCS if qvtoperational_cst_ClassifierPropertyCS is not None else set()
        self.qvtoperational_cst_ClassifierPropertyCS49 = qvtoperational_cst_ClassifierPropertyCS49 if qvtoperational_cst_ClassifierPropertyCS49 is not None else set()
        self.qvtoperational_cst_ClassifierPropertyCS52 = qvtoperational_cst_ClassifierPropertyCS52
        self.qvtoperational_cst_ClassifierPropertyCS54 = qvtoperational_cst_ClassifierPropertyCS54
        
    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def qvtoperational_cst_ClassifierPropertyCS49(self):
        return self.__qvtoperational_cst_ClassifierPropertyCS49

    @qvtoperational_cst_ClassifierPropertyCS49.setter
    def qvtoperational_cst_ClassifierPropertyCS49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ClassifierPropertyCS__qvtoperational_cst_ClassifierPropertyCS49", None)
        self.__qvtoperational_cst_ClassifierPropertyCS49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimpleNameCS50"):
                    opp_val = getattr(item, "SimpleNameCS50", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleNameCS50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleNameCS50"):
                    opp_val = getattr(item, "SimpleNameCS50", None)
                    
                    setattr(item, "SimpleNameCS50", self)
                    

    @property
    def qvtoperational_cst_ClassifierPropertyCS54(self):
        return self.__qvtoperational_cst_ClassifierPropertyCS54

    @qvtoperational_cst_ClassifierPropertyCS54.setter
    def qvtoperational_cst_ClassifierPropertyCS54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ClassifierPropertyCS__qvtoperational_cst_ClassifierPropertyCS54", None)
        self.__qvtoperational_cst_ClassifierPropertyCS54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OppositePropertyCS"):
                opp_val = getattr(old_value, "OppositePropertyCS", None)
                if opp_val == self:
                    setattr(old_value, "OppositePropertyCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OppositePropertyCS"):
                opp_val = getattr(value, "OppositePropertyCS", None)
                setattr(value, "OppositePropertyCS", self)

    @property
    def qvtoperational_cst_ClassifierPropertyCS(self):
        return self.__qvtoperational_cst_ClassifierPropertyCS

    @qvtoperational_cst_ClassifierPropertyCS.setter
    def qvtoperational_cst_ClassifierPropertyCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ClassifierPropertyCS__qvtoperational_cst_ClassifierPropertyCS", None)
        self.__qvtoperational_cst_ClassifierPropertyCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimpleNameCS47"):
                    opp_val = getattr(item, "SimpleNameCS47", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleNameCS47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleNameCS47"):
                    opp_val = getattr(item, "SimpleNameCS47", None)
                    
                    setattr(item, "SimpleNameCS47", self)
                    

    @property
    def qvtoperational_cst_ClassifierPropertyCS52(self):
        return self.__qvtoperational_cst_ClassifierPropertyCS52

    @qvtoperational_cst_ClassifierPropertyCS52.setter
    def qvtoperational_cst_ClassifierPropertyCS52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ClassifierPropertyCS__qvtoperational_cst_ClassifierPropertyCS52", None)
        self.__qvtoperational_cst_ClassifierPropertyCS52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MultiplicityDefCS"):
                opp_val = getattr(old_value, "MultiplicityDefCS", None)
                if opp_val == self:
                    setattr(old_value, "MultiplicityDefCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MultiplicityDefCS"):
                opp_val = getattr(value, "MultiplicityDefCS", None)
                setattr(value, "MultiplicityDefCS", self)

class ClassifierPropertyCS:

    pass
class PrimitiveLiteralExpCS:

    pass
class OppositePropertyCS:

    pass
class MultiplicityDefCS:

    pass
class TypeCS:

    pass
class qvtoperational_cst_DictionaryTypeCS(TypeCS):

    pass
class qvtoperational_cst_ListTypeCS(TypeCS):

    pass
class PathNameCS:

    pass
class MappingModuleCS:

    pass
class qvtoperational_cst_LibraryCS(MappingModuleCS):

    pass
class TagCS:

    pass
class ScopedNameCS:

    pass
class OCLExpressionCS:

    pass
class qvtoperational_cst_StatementCS(OCLExpressionCS):

    pass
class StringLiteralExpCS:

    pass
class SimpleNameCS:

    pass
class ClassifierDefCS:

    pass
class MappingMethodCS:

    pass
class qvtoperational_cst_MappingRuleCS(MappingMethodCS):

    pass
class qvtoperational_cst_MappingQueryCS(MappingMethodCS):

    def __init__(self, isSimpleDefinition: bool, qvtoperational_cst_MappingQueryCS: set["OCLExpressionCS"] = None, MappingMethodCS: "qvtoperational_cst_MappingModuleCS"):
        self.isSimpleDefinition = isSimpleDefinition
        self.qvtoperational_cst_MappingQueryCS = qvtoperational_cst_MappingQueryCS if qvtoperational_cst_MappingQueryCS is not None else set()
        
    @property
    def isSimpleDefinition(self) -> bool:
        return self.__isSimpleDefinition

    @isSimpleDefinition.setter
    def isSimpleDefinition(self, isSimpleDefinition: bool):
        self.__isSimpleDefinition = isSimpleDefinition

    @property
    def qvtoperational_cst_MappingQueryCS(self):
        return self.__qvtoperational_cst_MappingQueryCS

    @qvtoperational_cst_MappingQueryCS.setter
    def qvtoperational_cst_MappingQueryCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_MappingQueryCS__qvtoperational_cst_MappingQueryCS", None)
        self.__qvtoperational_cst_MappingQueryCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCLExpressionCS94"):
                    opp_val = getattr(item, "OCLExpressionCS94", None)
                    
                    if opp_val == self:
                        setattr(item, "OCLExpressionCS94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCLExpressionCS94"):
                    opp_val = getattr(item, "OCLExpressionCS94", None)
                    
                    setattr(item, "OCLExpressionCS94", self)
                    

class qvtoperational_cst_ConstructorCS(MappingMethodCS):

    pass
class ModulePropertyCS:

    pass
class qvtoperational_cst_ContextualPropertyCS(ModulePropertyCS):

    pass
class qvtoperational_cst_ConfigPropertyCS(ModulePropertyCS):

    pass
class qvtoperational_cst_LocalPropertyCS(ModulePropertyCS):

    pass
class RenameCS:

    pass
class ModelTypeCS:

    pass
class ImportCS:

    pass
class qvtoperational_cst_LibraryImportCS(ImportCS):

    pass
class TransformationHeaderCS:

    pass
class CSTNode:

    pass
class qvtoperational_cst_ResolveOpArgsExpCS(CSTNode):

    pass
class qvtoperational_cst_ModuleKindCS(CSTNode):

    def __init__(self, moduleKind: str, CSTNode: "qvtoperational_cst_UnitCS"):
        self.moduleKind = moduleKind
        
    @property
    def moduleKind(self) -> str:
        return self.__moduleKind

    @moduleKind.setter
    def moduleKind(self, moduleKind: str):
        self.__moduleKind = moduleKind

class qvtoperational_cst_TransformationRefineCS(CSTNode):

    pass
class qvtoperational_cst_ModuleUsageCS(CSTNode):

    def __init__(self, importKind: str, qvtoperational_cst_ModuleUsageCS: "ModuleKindCS" = None, qvtoperational_cst_ModuleUsageCS199: set["ModuleRefCS"] = None, CSTNode: "qvtoperational_cst_UnitCS"):
        self.importKind = importKind
        self.qvtoperational_cst_ModuleUsageCS = qvtoperational_cst_ModuleUsageCS
        self.qvtoperational_cst_ModuleUsageCS199 = qvtoperational_cst_ModuleUsageCS199 if qvtoperational_cst_ModuleUsageCS199 is not None else set()
        
    @property
    def importKind(self) -> str:
        return self.__importKind

    @importKind.setter
    def importKind(self, importKind: str):
        self.__importKind = importKind

    @property
    def qvtoperational_cst_ModuleUsageCS(self):
        return self.__qvtoperational_cst_ModuleUsageCS

    @qvtoperational_cst_ModuleUsageCS.setter
    def qvtoperational_cst_ModuleUsageCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ModuleUsageCS__qvtoperational_cst_ModuleUsageCS", None)
        self.__qvtoperational_cst_ModuleUsageCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModuleKindCS"):
                opp_val = getattr(old_value, "ModuleKindCS", None)
                if opp_val == self:
                    setattr(old_value, "ModuleKindCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModuleKindCS"):
                opp_val = getattr(value, "ModuleKindCS", None)
                setattr(value, "ModuleKindCS", self)

    @property
    def qvtoperational_cst_ModuleUsageCS199(self):
        return self.__qvtoperational_cst_ModuleUsageCS199

    @qvtoperational_cst_ModuleUsageCS199.setter
    def qvtoperational_cst_ModuleUsageCS199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ModuleUsageCS__qvtoperational_cst_ModuleUsageCS199", None)
        self.__qvtoperational_cst_ModuleUsageCS199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModuleRefCS"):
                    opp_val = getattr(item, "ModuleRefCS", None)
                    
                    if opp_val == self:
                        setattr(item, "ModuleRefCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModuleRefCS"):
                    opp_val = getattr(item, "ModuleRefCS", None)
                    
                    setattr(item, "ModuleRefCS", self)
                    

class qvtoperational_cst_PackageRefCS(CSTNode):

    pass
class qvtoperational_cst_MappingMethodCS(CSTNode):

    def __init__(self, blackBox: bool, qvtoperational_cst_MappingMethodCS: "MappingDeclarationCS" = None, CSTNode: "qvtoperational_cst_UnitCS"):
        self.blackBox = blackBox
        self.qvtoperational_cst_MappingMethodCS = qvtoperational_cst_MappingMethodCS
        
    @property
    def blackBox(self) -> bool:
        return self.__blackBox

    @blackBox.setter
    def blackBox(self, blackBox: bool):
        self.__blackBox = blackBox

    @property
    def qvtoperational_cst_MappingMethodCS(self):
        return self.__qvtoperational_cst_MappingMethodCS

    @qvtoperational_cst_MappingMethodCS.setter
    def qvtoperational_cst_MappingMethodCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_MappingMethodCS__qvtoperational_cst_MappingMethodCS", None)
        self.__qvtoperational_cst_MappingMethodCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MappingDeclarationCS"):
                opp_val = getattr(old_value, "MappingDeclarationCS", None)
                if opp_val == self:
                    setattr(old_value, "MappingDeclarationCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MappingDeclarationCS"):
                opp_val = getattr(value, "MappingDeclarationCS", None)
                setattr(value, "MappingDeclarationCS", self)

class qvtoperational_cst_MappingExtensionCS(CSTNode):

    def __init__(self, kind: str, qvtoperational_cst_MappingExtensionCS: set["ScopedNameCS"] = None, CSTNode: "qvtoperational_cst_UnitCS"):
        self.kind = kind
        self.qvtoperational_cst_MappingExtensionCS = qvtoperational_cst_MappingExtensionCS if qvtoperational_cst_MappingExtensionCS is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def qvtoperational_cst_MappingExtensionCS(self):
        return self.__qvtoperational_cst_MappingExtensionCS

    @qvtoperational_cst_MappingExtensionCS.setter
    def qvtoperational_cst_MappingExtensionCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_MappingExtensionCS__qvtoperational_cst_MappingExtensionCS", None)
        self.__qvtoperational_cst_MappingExtensionCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ScopedNameCS222"):
                    opp_val = getattr(item, "ScopedNameCS222", None)
                    
                    if opp_val == self:
                        setattr(item, "ScopedNameCS222", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ScopedNameCS222"):
                    opp_val = getattr(item, "ScopedNameCS222", None)
                    
                    setattr(item, "ScopedNameCS222", self)
                    

class qvtoperational_cst_CompleteSignatureCS(CSTNode):

    pass
class qvtoperational_cst_OppositePropertyCS(CSTNode):

    def __init__(self, isNavigable: bool, qvtoperational_cst_OppositePropertyCS: "SimpleNameCS" = None, qvtoperational_cst_OppositePropertyCS58: "MultiplicityDefCS" = None, CSTNode: "qvtoperational_cst_UnitCS"):
        self.isNavigable = isNavigable
        self.qvtoperational_cst_OppositePropertyCS = qvtoperational_cst_OppositePropertyCS
        self.qvtoperational_cst_OppositePropertyCS58 = qvtoperational_cst_OppositePropertyCS58
        
    @property
    def isNavigable(self) -> bool:
        return self.__isNavigable

    @isNavigable.setter
    def isNavigable(self, isNavigable: bool):
        self.__isNavigable = isNavigable

    @property
    def qvtoperational_cst_OppositePropertyCS58(self):
        return self.__qvtoperational_cst_OppositePropertyCS58

    @qvtoperational_cst_OppositePropertyCS58.setter
    def qvtoperational_cst_OppositePropertyCS58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_OppositePropertyCS__qvtoperational_cst_OppositePropertyCS58", None)
        self.__qvtoperational_cst_OppositePropertyCS58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MultiplicityDefCS59"):
                opp_val = getattr(old_value, "MultiplicityDefCS59", None)
                if opp_val == self:
                    setattr(old_value, "MultiplicityDefCS59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MultiplicityDefCS59"):
                opp_val = getattr(value, "MultiplicityDefCS59", None)
                setattr(value, "MultiplicityDefCS59", self)

    @property
    def qvtoperational_cst_OppositePropertyCS(self):
        return self.__qvtoperational_cst_OppositePropertyCS

    @qvtoperational_cst_OppositePropertyCS.setter
    def qvtoperational_cst_OppositePropertyCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_OppositePropertyCS__qvtoperational_cst_OppositePropertyCS", None)
        self.__qvtoperational_cst_OppositePropertyCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS56"):
                opp_val = getattr(old_value, "SimpleNameCS56", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS56"):
                opp_val = getattr(value, "SimpleNameCS56", None)
                setattr(value, "SimpleNameCS56", self)

class qvtoperational_cst_TagCS(CSTNode):

    pass
class qvtoperational_cst_RenameCS(CSTNode):

    pass
class qvtoperational_cst_ImportCS(CSTNode):

    pass
class qvtoperational_cst_MappingSectionsCS(CSTNode):

    pass
class qvtoperational_cst_TypeSpecCS(CSTNode):

    pass
class qvtoperational_cst_ParameterDeclarationCS(CSTNode):

    def __init__(self, directionKind: str, qvtoperational_cst_ParameterDeclarationCS: "SimpleNameCS" = None, qvtoperational_cst_ParameterDeclarationCS81: "TypeSpecCS" = None, CSTNode: "qvtoperational_cst_UnitCS"):
        self.directionKind = directionKind
        self.qvtoperational_cst_ParameterDeclarationCS = qvtoperational_cst_ParameterDeclarationCS
        self.qvtoperational_cst_ParameterDeclarationCS81 = qvtoperational_cst_ParameterDeclarationCS81
        
    @property
    def directionKind(self) -> str:
        return self.__directionKind

    @directionKind.setter
    def directionKind(self, directionKind: str):
        self.__directionKind = directionKind

    @property
    def qvtoperational_cst_ParameterDeclarationCS(self):
        return self.__qvtoperational_cst_ParameterDeclarationCS

    @qvtoperational_cst_ParameterDeclarationCS.setter
    def qvtoperational_cst_ParameterDeclarationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ParameterDeclarationCS__qvtoperational_cst_ParameterDeclarationCS", None)
        self.__qvtoperational_cst_ParameterDeclarationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS79"):
                opp_val = getattr(old_value, "SimpleNameCS79", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS79"):
                opp_val = getattr(value, "SimpleNameCS79", None)
                setattr(value, "SimpleNameCS79", self)

    @property
    def qvtoperational_cst_ParameterDeclarationCS81(self):
        return self.__qvtoperational_cst_ParameterDeclarationCS81

    @qvtoperational_cst_ParameterDeclarationCS81.setter
    def qvtoperational_cst_ParameterDeclarationCS81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ParameterDeclarationCS__qvtoperational_cst_ParameterDeclarationCS81", None)
        self.__qvtoperational_cst_ParameterDeclarationCS81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeSpecCS"):
                opp_val = getattr(old_value, "TypeSpecCS", None)
                if opp_val == self:
                    setattr(old_value, "TypeSpecCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeSpecCS"):
                opp_val = getattr(value, "TypeSpecCS", None)
                setattr(value, "TypeSpecCS", self)

class qvtoperational_cst_SimpleSignatureCS(CSTNode):

    pass
class qvtoperational_cst_DictLiteralPartCS(CSTNode):

    pass
class qvtoperational_cst_DirectionKindCS(CSTNode):

    def __init__(self, directionKind: str, CSTNode: "qvtoperational_cst_UnitCS"):
        self.directionKind = directionKind
        
    @property
    def directionKind(self) -> str:
        return self.__directionKind

    @directionKind.setter
    def directionKind(self, directionKind: str):
        self.__directionKind = directionKind

class qvtoperational_cst_ScopedNameCS(CSTNode):

    def __init__(self, name: str, qvtoperational_cst_ScopedNameCS: "TypeCS" = None, CSTNode: "qvtoperational_cst_UnitCS"):
        self.name = name
        self.qvtoperational_cst_ScopedNameCS = qvtoperational_cst_ScopedNameCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def qvtoperational_cst_ScopedNameCS(self):
        return self.__qvtoperational_cst_ScopedNameCS

    @qvtoperational_cst_ScopedNameCS.setter
    def qvtoperational_cst_ScopedNameCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_ScopedNameCS__qvtoperational_cst_ScopedNameCS", None)
        self.__qvtoperational_cst_ScopedNameCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeCS264"):
                opp_val = getattr(old_value, "TypeCS264", None)
                if opp_val == self:
                    setattr(old_value, "TypeCS264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeCS264"):
                opp_val = getattr(value, "TypeCS264", None)
                setattr(value, "TypeCS264", self)

class qvtoperational_cst_ClassifierDefCS(CSTNode):

    pass
class qvtoperational_cst_UnitCS(CSTNode):

    pass
class qvtoperational_cst_TransformationHeaderCS(CSTNode):

    pass
class qvtoperational_cst_MultiplicityDefCS(CSTNode):

    pass
class qvtoperational_cst_ModulePropertyCS(CSTNode):

    pass
class qvtoperational_cst_MappingDeclarationCS(CSTNode):

    def __init__(self, qualifiers: str, isQuery: bool, qvtoperational_cst_MappingDeclarationCS: "SimpleNameCS" = None, qvtoperational_cst_MappingDeclarationCS67: "TypeCS" = None, qvtoperational_cst_MappingDeclarationCS70: set["ParameterDeclarationCS"] = None, qvtoperational_cst_MappingDeclarationCS72: set["ParameterDeclarationCS"] = None, qvtoperational_cst_MappingDeclarationCS75: "DirectionKindCS" = None, qvtoperational_cst_MappingDeclarationCS77: set["MappingExtensionCS"] = None, CSTNode: "qvtoperational_cst_UnitCS"):
        self.qualifiers = qualifiers
        self.isQuery = isQuery
        self.qvtoperational_cst_MappingDeclarationCS = qvtoperational_cst_MappingDeclarationCS
        self.qvtoperational_cst_MappingDeclarationCS67 = qvtoperational_cst_MappingDeclarationCS67
        self.qvtoperational_cst_MappingDeclarationCS70 = qvtoperational_cst_MappingDeclarationCS70 if qvtoperational_cst_MappingDeclarationCS70 is not None else set()
        self.qvtoperational_cst_MappingDeclarationCS72 = qvtoperational_cst_MappingDeclarationCS72 if qvtoperational_cst_MappingDeclarationCS72 is not None else set()
        self.qvtoperational_cst_MappingDeclarationCS75 = qvtoperational_cst_MappingDeclarationCS75
        self.qvtoperational_cst_MappingDeclarationCS77 = qvtoperational_cst_MappingDeclarationCS77 if qvtoperational_cst_MappingDeclarationCS77 is not None else set()
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def qualifiers(self) -> str:
        return self.__qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers: str):
        self.__qualifiers = qualifiers

    @property
    def qvtoperational_cst_MappingDeclarationCS72(self):
        return self.__qvtoperational_cst_MappingDeclarationCS72

    @qvtoperational_cst_MappingDeclarationCS72.setter
    def qvtoperational_cst_MappingDeclarationCS72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_MappingDeclarationCS__qvtoperational_cst_MappingDeclarationCS72", None)
        self.__qvtoperational_cst_MappingDeclarationCS72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParameterDeclarationCS73"):
                    opp_val = getattr(item, "ParameterDeclarationCS73", None)
                    
                    if opp_val == self:
                        setattr(item, "ParameterDeclarationCS73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParameterDeclarationCS73"):
                    opp_val = getattr(item, "ParameterDeclarationCS73", None)
                    
                    setattr(item, "ParameterDeclarationCS73", self)
                    

    @property
    def qvtoperational_cst_MappingDeclarationCS67(self):
        return self.__qvtoperational_cst_MappingDeclarationCS67

    @qvtoperational_cst_MappingDeclarationCS67.setter
    def qvtoperational_cst_MappingDeclarationCS67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_MappingDeclarationCS__qvtoperational_cst_MappingDeclarationCS67", None)
        self.__qvtoperational_cst_MappingDeclarationCS67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeCS68"):
                opp_val = getattr(old_value, "TypeCS68", None)
                if opp_val == self:
                    setattr(old_value, "TypeCS68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeCS68"):
                opp_val = getattr(value, "TypeCS68", None)
                setattr(value, "TypeCS68", self)

    @property
    def qvtoperational_cst_MappingDeclarationCS77(self):
        return self.__qvtoperational_cst_MappingDeclarationCS77

    @qvtoperational_cst_MappingDeclarationCS77.setter
    def qvtoperational_cst_MappingDeclarationCS77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_MappingDeclarationCS__qvtoperational_cst_MappingDeclarationCS77", None)
        self.__qvtoperational_cst_MappingDeclarationCS77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MappingExtensionCS"):
                    opp_val = getattr(item, "MappingExtensionCS", None)
                    
                    if opp_val == self:
                        setattr(item, "MappingExtensionCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MappingExtensionCS"):
                    opp_val = getattr(item, "MappingExtensionCS", None)
                    
                    setattr(item, "MappingExtensionCS", self)
                    

    @property
    def qvtoperational_cst_MappingDeclarationCS75(self):
        return self.__qvtoperational_cst_MappingDeclarationCS75

    @qvtoperational_cst_MappingDeclarationCS75.setter
    def qvtoperational_cst_MappingDeclarationCS75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_MappingDeclarationCS__qvtoperational_cst_MappingDeclarationCS75", None)
        self.__qvtoperational_cst_MappingDeclarationCS75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DirectionKindCS"):
                opp_val = getattr(old_value, "DirectionKindCS", None)
                if opp_val == self:
                    setattr(old_value, "DirectionKindCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DirectionKindCS"):
                opp_val = getattr(value, "DirectionKindCS", None)
                setattr(value, "DirectionKindCS", self)

    @property
    def qvtoperational_cst_MappingDeclarationCS70(self):
        return self.__qvtoperational_cst_MappingDeclarationCS70

    @qvtoperational_cst_MappingDeclarationCS70.setter
    def qvtoperational_cst_MappingDeclarationCS70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_MappingDeclarationCS__qvtoperational_cst_MappingDeclarationCS70", None)
        self.__qvtoperational_cst_MappingDeclarationCS70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ParameterDeclarationCS"):
                    opp_val = getattr(item, "ParameterDeclarationCS", None)
                    
                    if opp_val == self:
                        setattr(item, "ParameterDeclarationCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ParameterDeclarationCS"):
                    opp_val = getattr(item, "ParameterDeclarationCS", None)
                    
                    setattr(item, "ParameterDeclarationCS", self)
                    

    @property
    def qvtoperational_cst_MappingDeclarationCS(self):
        return self.__qvtoperational_cst_MappingDeclarationCS

    @qvtoperational_cst_MappingDeclarationCS.setter
    def qvtoperational_cst_MappingDeclarationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qvtoperational_cst_MappingDeclarationCS__qvtoperational_cst_MappingDeclarationCS", None)
        self.__qvtoperational_cst_MappingDeclarationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleNameCS65"):
                opp_val = getattr(old_value, "SimpleNameCS65", None)
                if opp_val == self:
                    setattr(old_value, "SimpleNameCS65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleNameCS65"):
                opp_val = getattr(value, "SimpleNameCS65", None)
                setattr(value, "SimpleNameCS65", self)

class qvtoperational_cst_ModuleRefCS(CSTNode):

    pass
class qvtoperational_cst_MappingModuleCS(CSTNode):

    pass