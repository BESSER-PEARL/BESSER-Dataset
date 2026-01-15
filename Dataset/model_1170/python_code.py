from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModelElement:

    pass
class OclFeature:

    pass
class atlstatic_OCL_Operation(OclFeature):

    def __init__(self, name: str, atlstatic_OCL_Operation: set["Parameter"] = None, OclType261: "OclType" = None, OclExpression264: "OclExpression" = None, OCL239: "atlstatic_OCL_OclFeatureDefinition"):
        self.name = name
        self.atlstatic_OCL_Operation = atlstatic_OCL_Operation if atlstatic_OCL_Operation is not None else set()
        self.OclType261 = OclType261
        self.OclExpression264 = OclExpression264
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclType261(self):
        return self.__OclType261

    @OclType261.setter
    def OclType261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Operation__OclType261", None)
        self.__OclType261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL262"):
                opp_val = getattr(old_value, "OCL262", None)
                if opp_val == self:
                    setattr(old_value, "OCL262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL262"):
                opp_val = getattr(value, "OCL262", None)
                setattr(value, "OCL262", self)

    @property
    def OclExpression264(self):
        return self.__OclExpression264

    @OclExpression264.setter
    def OclExpression264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Operation__OclExpression264", None)
        self.__OclExpression264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL265"):
                opp_val = getattr(old_value, "OCL265", None)
                if opp_val == self:
                    setattr(old_value, "OCL265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL265"):
                opp_val = getattr(value, "OCL265", None)
                setattr(value, "OCL265", self)

    @property
    def atlstatic_OCL_Operation(self):
        return self.__atlstatic_OCL_Operation

    @atlstatic_OCL_Operation.setter
    def atlstatic_OCL_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Operation__atlstatic_OCL_Operation", None)
        self.__atlstatic_OCL_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter259"):
                    opp_val = getattr(item, "Parameter259", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter259"):
                    opp_val = getattr(item, "Parameter259", None)
                    
                    setattr(item, "Parameter259", self)
                    

class atlstatic_OCL_Attribute(OclFeature):

    def __init__(self, name: str, OclExpression253: "OclExpression" = None, OclType256: "OclType" = None, OCL239: "atlstatic_OCL_OclFeatureDefinition"):
        self.name = name
        self.OclExpression253 = OclExpression253
        self.OclType256 = OclType256
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclExpression253(self):
        return self.__OclExpression253

    @OclExpression253.setter
    def OclExpression253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Attribute__OclExpression253", None)
        self.__OclExpression253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL254"):
                opp_val = getattr(old_value, "OCL254", None)
                if opp_val == self:
                    setattr(old_value, "OCL254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL254"):
                opp_val = getattr(value, "OCL254", None)
                setattr(value, "OCL254", self)

    @property
    def OclType256(self):
        return self.__OclType256

    @OclType256.setter
    def OclType256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Attribute__OclType256", None)
        self.__OclType256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL257"):
                opp_val = getattr(old_value, "OCL257", None)
                if opp_val == self:
                    setattr(old_value, "OCL257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL257"):
                opp_val = getattr(value, "OCL257", None)
                setattr(value, "OCL257", self)

class TupleType:

    pass
class CollectionType:

    pass
class atlstatic_OCL_BagType(CollectionType):

    pass
class atlstatic_OCL_SetType(CollectionType):

    pass
class atlstatic_OCL_OrderedSetType(CollectionType):

    pass
class atlstatic_OCL_SequenceType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class NumericType:

    pass
class atlstatic_OCL_RealType(NumericType):

    pass
class atlstatic_OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class atlstatic_OCL_BooleanType(Primitive):

    pass
class atlstatic_OCL_NumericType(Primitive):

    pass
class atlstatic_OCL_StringType(Primitive):

    pass
class VariableExp:

    pass
class TupleTypeAttribute:

    pass
class IterateExp:

    pass
class MapExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class NumericExp:

    pass
class atlstatic_OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class atlstatic_OCL_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class PrimitiveExp:

    pass
class atlstatic_OCL_NumericExp(PrimitiveExp):

    pass
class atlstatic_OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class atlstatic_OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
    @property
    def stringSymbol(self) -> str:
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol

class Attribute:

    pass
class TuplePart:

    pass
class LoopExp:

    pass
class atlstatic_OCL_IterateExp(LoopExp):

    pass
class atlstatic_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, OCL194: "atlstatic_OCL_Iterator", OCL115: "atlstatic_OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class LetExp:

    pass
class CollectionExp:

    pass
class atlstatic_OCL_SetExp(CollectionExp):

    pass
class atlstatic_OCL_OrderedSetExp(CollectionExp):

    pass
class atlstatic_OCL_SequenceExp(CollectionExp):

    pass
class atlstatic_OCL_BagExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class atlstatic_OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, OclExpression153: set["OclExpression"] = None, OCL109: "atlstatic_OCL_OclExpression"):
        self.operationName = operationName
        self.OclExpression153 = OclExpression153 if OclExpression153 is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def OclExpression153(self):
        return self.__OclExpression153

    @OclExpression153.setter
    def OclExpression153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OperationCallExp__OclExpression153", None)
        self.__OclExpression153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL154"):
                    opp_val = getattr(item, "OCL154", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL154"):
                    opp_val = getattr(item, "OCL154", None)
                    
                    setattr(item, "OCL154", self)
                    

class atlstatic_OCL_LoopExp(PropertyCallExp):

    pass
class atlstatic_OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, OCL109: "atlstatic_OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class IfExp:

    pass
class OclType:

    pass
class atlstatic_OCL_OclModelElement(OclType):

    pass
class atlstatic_OCL_OclAnyType(OclType):

    pass
class atlstatic_OCL_TupleType(OclType):

    pass
class atlstatic_OCL_Primitive(OclType):

    pass
class atlstatic_OCL_MapType(OclType):

    pass
class atlstatic_OCL_CollectionType(OclType):

    pass
class Operation:

    pass
class OperationCallExp:

    pass
class atlstatic_OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class atlstatic_OCL_OperatorCallExp(OperationCallExp):

    pass
class Statement:

    pass
class atlstatic_ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, atlstatic_ATL_BindingStat87: "OclExpression" = None, atlstatic_ATL_BindingStat: "OclExpression" = None, Statement93: "atlstatic_ATL_IfStat", Statement96: "atlstatic_ATL_IfStat", Statement104: "atlstatic_ATL_ForStat", Statement: "atlstatic_ATL_ActionBlock"):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlstatic_ATL_BindingStat87 = atlstatic_ATL_BindingStat87
        self.atlstatic_ATL_BindingStat = atlstatic_ATL_BindingStat
        
    @property
    def isAssignment(self) -> str:
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def atlstatic_ATL_BindingStat(self):
        return self.__atlstatic_ATL_BindingStat

    @atlstatic_ATL_BindingStat.setter
    def atlstatic_ATL_BindingStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_BindingStat__atlstatic_ATL_BindingStat", None)
        self.__atlstatic_ATL_BindingStat = value
        
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
    def atlstatic_ATL_BindingStat87(self):
        return self.__atlstatic_ATL_BindingStat87

    @atlstatic_ATL_BindingStat87.setter
    def atlstatic_ATL_BindingStat87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_BindingStat__atlstatic_ATL_BindingStat87", None)
        self.__atlstatic_ATL_BindingStat87 = value
        
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

class atlstatic_ATL_ExpressionStat(Statement):

    pass
class atlstatic_ATL_ForStat(Statement):

    pass
class atlstatic_ATL_IfStat(Statement):

    pass
class Iterator:

    pass
class Binding:

    pass
class DropPattern:

    pass
class InPatternElement:

    pass
class atlstatic_ATL_SimpleInPatternElement(InPatternElement):

    pass
class Parameter:

    pass
class StaticRule:

    pass
class atlstatic_ATL_CalledRule(StaticRule):

    def __init__(self, isEntrypoint: str, isEndpoint: str, atlstatic_ATL_CalledRule: set["Parameter"] = None):
        self.isEntrypoint = isEntrypoint
        self.isEndpoint = isEndpoint
        self.atlstatic_ATL_CalledRule = atlstatic_ATL_CalledRule if atlstatic_ATL_CalledRule is not None else set()
        
    @property
    def isEndpoint(self) -> str:
        return self.__isEndpoint

    @isEndpoint.setter
    def isEndpoint(self, isEndpoint: str):
        self.__isEndpoint = isEndpoint

    @property
    def isEntrypoint(self) -> str:
        return self.__isEntrypoint

    @isEntrypoint.setter
    def isEntrypoint(self, isEntrypoint: str):
        self.__isEntrypoint = isEntrypoint

    @property
    def atlstatic_ATL_CalledRule(self):
        return self.__atlstatic_ATL_CalledRule

    @atlstatic_ATL_CalledRule.setter
    def atlstatic_ATL_CalledRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_CalledRule__atlstatic_ATL_CalledRule", None)
        self.__atlstatic_ATL_CalledRule = value if value is not None else set()
        
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
                    

class ATL_StaticRule:

    pass
class PatternElement:

    pass
class atlstatic_ATL_OutPatternElement(PatternElement):

    pass
class atlstatic_ATL_InPatternElement(PatternElement):

    pass
class VariableDeclaration:

    pass
class atlstatic_ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class atlstatic_OCL_Parameter(VariableDeclaration):

    pass
class atlstatic_OCL_TuplePart(VariableDeclaration):

    pass
class atlstatic_OCL_Iterator(VariableDeclaration):

    pass
class atlstatic_ATL_PatternElement(VariableDeclaration):

    pass
class OutPatternElement:

    pass
class atlstatic_ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class atlstatic_ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class Rule:

    pass
class atlstatic_ATL_RuleWithPattern(Rule):

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, atlstatic_ATL_RuleWithPattern: "InPattern" = None, RuleWithPattern: set["RuleWithPattern"] = None, RuleWithPattern28: "RuleWithPattern" = None, ATL36: "atlstatic_ATL_OutPattern", ATL80: "atlstatic_ATL_ActionBlock", ATL75: "atlstatic_ATL_RuleVariableDeclaration"):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.atlstatic_ATL_RuleWithPattern = atlstatic_ATL_RuleWithPattern
        self.RuleWithPattern = RuleWithPattern if RuleWithPattern is not None else set()
        self.RuleWithPattern28 = RuleWithPattern28
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def isNoDefault(self) -> str:
        return self.__isNoDefault

    @isNoDefault.setter
    def isNoDefault(self, isNoDefault: str):
        self.__isNoDefault = isNoDefault

    @property
    def RuleWithPattern28(self):
        return self.__RuleWithPattern28

    @RuleWithPattern28.setter
    def RuleWithPattern28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_RuleWithPattern__RuleWithPattern28", None)
        self.__RuleWithPattern28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL29"):
                opp_val = getattr(old_value, "ATL29", None)
                if opp_val == self:
                    setattr(old_value, "ATL29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL29"):
                opp_val = getattr(value, "ATL29", None)
                setattr(value, "ATL29", self)

    @property
    def RuleWithPattern(self):
        return self.__RuleWithPattern

    @RuleWithPattern.setter
    def RuleWithPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_RuleWithPattern__RuleWithPattern", None)
        self.__RuleWithPattern = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL26"):
                    opp_val = getattr(item, "ATL26", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL26"):
                    opp_val = getattr(item, "ATL26", None)
                    
                    setattr(item, "ATL26", self)
                    

    @property
    def atlstatic_ATL_RuleWithPattern(self):
        return self.__atlstatic_ATL_RuleWithPattern

    @atlstatic_ATL_RuleWithPattern.setter
    def atlstatic_ATL_RuleWithPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_RuleWithPattern__atlstatic_ATL_RuleWithPattern", None)
        self.__atlstatic_ATL_RuleWithPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InPattern"):
                opp_val = getattr(old_value, "InPattern", None)
                if opp_val == self:
                    setattr(old_value, "InPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InPattern"):
                opp_val = getattr(value, "InPattern", None)
                setattr(value, "InPattern", self)

class atlstatic_ATL_Callable(ABC):

    pass
class Callable:

    pass
class atlstatic_ATL_ModuleCallable(Callable):

    pass
class ATL_Rule:

    pass
class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OutPattern:

    pass
class ATL_ModuleCallable:

    pass
class atlstatic_ATL_StaticRule(ATL_Rule, ATL_ModuleCallable):

    pass
class ATL_Helper:

    pass
class atlstatic_ATL_StaticHelper(ATL_ModuleCallable, ATL_Helper):

    pass
class OclFeatureDefinition:

    pass
class ATL_RuleWithPattern:

    pass
class atlstatic_ATL_LazyRule(ATL_StaticRule, ATL_RuleWithPattern):

    def __init__(self, isUnique: str):
        self.isUnique = isUnique
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

class RuleWithPattern:

    pass
class atlstatic_ATL_MatchedRule(RuleWithPattern):

    pass
class InPattern:

    pass
class OclModel:

    pass
class OclExpression:

    pass
class atlstatic_OCL_TupleExp(OclExpression):

    pass
class atlstatic_OCL_CollectionExp(OclExpression):

    pass
class atlstatic_OCL_SuperExp(OclExpression):

    pass
class atlstatic_OCL_PropertyCallExp(OclExpression):

    pass
class atlstatic_OCL_MapExp(OclExpression):

    pass
class atlstatic_OCL_PrimitiveExp(OclExpression):

    pass
class atlstatic_OCL_OclUndefinedExp(OclExpression):

    pass
class atlstatic_OCL_LetExp(OclExpression):

    pass
class atlstatic_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression88: "atlstatic_ATL_BindingStat", OCL135: "atlstatic_OCL_CollectionExp", OclExpression145: "atlstatic_OCL_MapElement", OCL178: "atlstatic_OCL_IfExp", OclExpression90: "atlstatic_ATL_IfStat", OCL254: "atlstatic_OCL_Attribute", OCL265: "atlstatic_OCL_Operation", OclExpression148: "atlstatic_OCL_MapElement", OclExpression63: "atlstatic_ATL_SimpleOutPatternElement", OCL157: "atlstatic_OCL_LoopExp", OCL169: "atlstatic_OCL_LetExp", OCL202: "atlstatic_OCL_OclType", OCL184: "atlstatic_OCL_VariableDeclaration", OclExpression83: "atlstatic_ATL_ExpressionStat", OCL175: "atlstatic_OCL_IfExp", OclExpression: "atlstatic_ATL_Query", OclExpression69: "atlstatic_ATL_Binding", OclExpression85: "atlstatic_ATL_BindingStat", OclExpression65: "atlstatic_ATL_ForEachOutPatternElement", OCL172: "atlstatic_OCL_IfExp", OCL151: "atlstatic_OCL_PropertyCallExp", OclExpression34: "atlstatic_ATL_InPattern", OCL154: "atlstatic_OCL_OperationCallExp", OclExpression101: "atlstatic_ATL_ForStat"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class atlstatic_OCL_OclType(OclExpression):

    def __init__(self, name: str, TupleTypeAttribute: "TupleTypeAttribute" = None, VariableDeclaration219: "VariableDeclaration" = None, OclContextDefinition: "OclContextDefinition" = None, OclExpression201: "OclExpression" = None, Operation204: "Operation" = None, MapType: "MapType" = None, Attribute209: "Attribute" = None, MapType212: "MapType" = None, CollectionType: "CollectionType" = None, OclExpression88: "atlstatic_ATL_BindingStat", OCL135: "atlstatic_OCL_CollectionExp", OclExpression145: "atlstatic_OCL_MapElement", OCL178: "atlstatic_OCL_IfExp", OclExpression90: "atlstatic_ATL_IfStat", OCL254: "atlstatic_OCL_Attribute", OCL265: "atlstatic_OCL_Operation", OclExpression148: "atlstatic_OCL_MapElement", OclExpression63: "atlstatic_ATL_SimpleOutPatternElement", OCL157: "atlstatic_OCL_LoopExp", OCL169: "atlstatic_OCL_LetExp", OCL202: "atlstatic_OCL_OclType", OCL184: "atlstatic_OCL_VariableDeclaration", OclExpression83: "atlstatic_ATL_ExpressionStat", OCL175: "atlstatic_OCL_IfExp", OclExpression: "atlstatic_ATL_Query", OclExpression69: "atlstatic_ATL_Binding", OclExpression85: "atlstatic_ATL_BindingStat", OclExpression65: "atlstatic_ATL_ForEachOutPatternElement", OCL172: "atlstatic_OCL_IfExp", OCL151: "atlstatic_OCL_PropertyCallExp", OclExpression34: "atlstatic_ATL_InPattern", OCL154: "atlstatic_OCL_OperationCallExp", OclExpression101: "atlstatic_ATL_ForStat"):
        self.name = name
        self.TupleTypeAttribute = TupleTypeAttribute
        self.VariableDeclaration219 = VariableDeclaration219
        self.OclContextDefinition = OclContextDefinition
        self.OclExpression201 = OclExpression201
        self.Operation204 = Operation204
        self.MapType = MapType
        self.Attribute209 = Attribute209
        self.MapType212 = MapType212
        self.CollectionType = CollectionType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TupleTypeAttribute(self):
        return self.__TupleTypeAttribute

    @TupleTypeAttribute.setter
    def TupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__TupleTypeAttribute", None)
        self.__TupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL217"):
                opp_val = getattr(old_value, "OCL217", None)
                if opp_val == self:
                    setattr(old_value, "OCL217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL217"):
                opp_val = getattr(value, "OCL217", None)
                setattr(value, "OCL217", self)

    @property
    def Operation204(self):
        return self.__Operation204

    @Operation204.setter
    def Operation204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__Operation204", None)
        self.__Operation204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL205"):
                opp_val = getattr(old_value, "OCL205", None)
                if opp_val == self:
                    setattr(old_value, "OCL205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL205"):
                opp_val = getattr(value, "OCL205", None)
                setattr(value, "OCL205", self)

    @property
    def MapType212(self):
        return self.__MapType212

    @MapType212.setter
    def MapType212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__MapType212", None)
        self.__MapType212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL213"):
                opp_val = getattr(old_value, "OCL213", None)
                if opp_val == self:
                    setattr(old_value, "OCL213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL213"):
                opp_val = getattr(value, "OCL213", None)
                setattr(value, "OCL213", self)

    @property
    def OclExpression201(self):
        return self.__OclExpression201

    @OclExpression201.setter
    def OclExpression201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__OclExpression201", None)
        self.__OclExpression201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL202"):
                opp_val = getattr(old_value, "OCL202", None)
                if opp_val == self:
                    setattr(old_value, "OCL202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL202"):
                opp_val = getattr(value, "OCL202", None)
                setattr(value, "OCL202", self)

    @property
    def OclContextDefinition(self):
        return self.__OclContextDefinition

    @OclContextDefinition.setter
    def OclContextDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__OclContextDefinition", None)
        self.__OclContextDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL199"):
                opp_val = getattr(old_value, "OCL199", None)
                if opp_val == self:
                    setattr(old_value, "OCL199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL199"):
                opp_val = getattr(value, "OCL199", None)
                setattr(value, "OCL199", self)

    @property
    def VariableDeclaration219(self):
        return self.__VariableDeclaration219

    @VariableDeclaration219.setter
    def VariableDeclaration219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__VariableDeclaration219", None)
        self.__VariableDeclaration219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL220"):
                opp_val = getattr(old_value, "OCL220", None)
                if opp_val == self:
                    setattr(old_value, "OCL220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL220"):
                opp_val = getattr(value, "OCL220", None)
                setattr(value, "OCL220", self)

    @property
    def CollectionType(self):
        return self.__CollectionType

    @CollectionType.setter
    def CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__CollectionType", None)
        self.__CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL215"):
                opp_val = getattr(old_value, "OCL215", None)
                if opp_val == self:
                    setattr(old_value, "OCL215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL215"):
                opp_val = getattr(value, "OCL215", None)
                setattr(value, "OCL215", self)

    @property
    def Attribute209(self):
        return self.__Attribute209

    @Attribute209.setter
    def Attribute209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__Attribute209", None)
        self.__Attribute209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL210"):
                opp_val = getattr(old_value, "OCL210", None)
                if opp_val == self:
                    setattr(old_value, "OCL210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL210"):
                opp_val = getattr(value, "OCL210", None)
                setattr(value, "OCL210", self)

    @property
    def MapType(self):
        return self.__MapType

    @MapType.setter
    def MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__MapType", None)
        self.__MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL207"):
                opp_val = getattr(old_value, "OCL207", None)
                if opp_val == self:
                    setattr(old_value, "OCL207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL207"):
                opp_val = getattr(value, "OCL207", None)
                setattr(value, "OCL207", self)

class atlstatic_OCL_IfExp(OclExpression):

    pass
class atlstatic_OCL_VariableExp(OclExpression):

    pass
class Helper:

    pass
class atlstatic_ATL_ContextHelper(Helper):

    pass
class Unit:

    pass
class atlstatic_ATL_Query(Unit):

    pass
class atlstatic_ATL_Module(Unit):

    def __init__(self, isRefining: str, atlstatic_ATL_Module9: set["OclModel"] = None, atlstatic_ATL_Module12: set["ModuleElement"] = None, atlstatic_ATL_Module: set["OclModel"] = None, ATL77: "atlstatic_ATL_LibraryRef"):
        self.isRefining = isRefining
        self.atlstatic_ATL_Module9 = atlstatic_ATL_Module9 if atlstatic_ATL_Module9 is not None else set()
        self.atlstatic_ATL_Module12 = atlstatic_ATL_Module12 if atlstatic_ATL_Module12 is not None else set()
        self.atlstatic_ATL_Module = atlstatic_ATL_Module if atlstatic_ATL_Module is not None else set()
        
    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def atlstatic_ATL_Module9(self):
        return self.__atlstatic_ATL_Module9

    @atlstatic_ATL_Module9.setter
    def atlstatic_ATL_Module9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Module__atlstatic_ATL_Module9", None)
        self.__atlstatic_ATL_Module9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel10"):
                    opp_val = getattr(item, "OclModel10", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel10"):
                    opp_val = getattr(item, "OclModel10", None)
                    
                    setattr(item, "OclModel10", self)
                    

    @property
    def atlstatic_ATL_Module(self):
        return self.__atlstatic_ATL_Module

    @atlstatic_ATL_Module.setter
    def atlstatic_ATL_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Module__atlstatic_ATL_Module", None)
        self.__atlstatic_ATL_Module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel"):
                    opp_val = getattr(item, "OclModel", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel"):
                    opp_val = getattr(item, "OclModel", None)
                    
                    setattr(item, "OclModel", self)
                    

    @property
    def atlstatic_ATL_Module12(self):
        return self.__atlstatic_ATL_Module12

    @atlstatic_ATL_Module12.setter
    def atlstatic_ATL_Module12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Module__atlstatic_ATL_Module12", None)
        self.__atlstatic_ATL_Module12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModuleElement"):
                    opp_val = getattr(item, "ModuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ModuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModuleElement"):
                    opp_val = getattr(item, "ModuleElement", None)
                    
                    setattr(item, "ModuleElement", self)
                    

class atlstatic_ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class LocatedElement:

    pass
class atlstatic_ATL_InPattern(LocatedElement):

    pass
class atlstatic_OCL_OclFeatureDefinition(LocatedElement):

    pass
class atlstatic_ATL_ActionBlock(LocatedElement):

    pass
class atlstatic_ATL_DropPattern(LocatedElement):

    pass
class atlstatic_OCL_OclContextDefinition(LocatedElement):

    pass
class atlstatic_ATL_OutPattern(LocatedElement):

    pass
class atlstatic_OCL_MapElement(LocatedElement):

    pass
class atlstatic_ATL_Statement(LocatedElement):

    pass
class atlstatic_OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, OclType225: "OclType" = None, TupleType: "TupleType" = None):
        self.name = name
        self.OclType225 = OclType225
        self.TupleType = TupleType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TupleType(self):
        return self.__TupleType

    @TupleType.setter
    def TupleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_TupleTypeAttribute__TupleType", None)
        self.__TupleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL228"):
                opp_val = getattr(old_value, "OCL228", None)
                if opp_val == self:
                    setattr(old_value, "OCL228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL228"):
                opp_val = getattr(value, "OCL228", None)
                setattr(value, "OCL228", self)

    @property
    def OclType225(self):
        return self.__OclType225

    @OclType225.setter
    def OclType225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_TupleTypeAttribute__OclType225", None)
        self.__OclType225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL226"):
                opp_val = getattr(old_value, "OCL226", None)
                if opp_val == self:
                    setattr(old_value, "OCL226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL226"):
                opp_val = getattr(value, "OCL226", None)
                setattr(value, "OCL226", self)

class atlstatic_ATL_LibraryRef(LocatedElement):

    def __init__(self, name: str, Unit: "Unit" = None):
        self.name = name
        self.Unit = Unit
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Unit(self):
        return self.__Unit

    @Unit.setter
    def Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_LibraryRef__Unit", None)
        self.__Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL77"):
                opp_val = getattr(old_value, "ATL77", None)
                if opp_val == self:
                    setattr(old_value, "ATL77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL77"):
                opp_val = getattr(value, "ATL77", None)
                setattr(value, "ATL77", self)

class atlstatic_OCL_OclFeature(LocatedElement):

    pass
class atlstatic_OCL_OclExpression(LocatedElement):

    pass
class atlstatic_OCL_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, VariableExp: set["VariableExp"] = None, OclType180: "OclType" = None, OclExpression183: "OclExpression" = None, LetExp186: "LetExp" = None, IterateExp: "IterateExp" = None):
        self.id = id
        self.varName = varName
        self.VariableExp = VariableExp if VariableExp is not None else set()
        self.OclType180 = OclType180
        self.OclExpression183 = OclExpression183
        self.LetExp186 = LetExp186
        self.IterateExp = IterateExp
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def VariableExp(self):
        return self.__VariableExp

    @VariableExp.setter
    def VariableExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__VariableExp", None)
        self.__VariableExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL191"):
                    opp_val = getattr(item, "OCL191", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL191", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL191"):
                    opp_val = getattr(item, "OCL191", None)
                    
                    setattr(item, "OCL191", self)
                    

    @property
    def IterateExp(self):
        return self.__IterateExp

    @IterateExp.setter
    def IterateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__IterateExp", None)
        self.__IterateExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL189"):
                opp_val = getattr(old_value, "OCL189", None)
                if opp_val == self:
                    setattr(old_value, "OCL189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL189"):
                opp_val = getattr(value, "OCL189", None)
                setattr(value, "OCL189", self)

    @property
    def OclExpression183(self):
        return self.__OclExpression183

    @OclExpression183.setter
    def OclExpression183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__OclExpression183", None)
        self.__OclExpression183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL184"):
                opp_val = getattr(old_value, "OCL184", None)
                if opp_val == self:
                    setattr(old_value, "OCL184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL184"):
                opp_val = getattr(value, "OCL184", None)
                setattr(value, "OCL184", self)

    @property
    def OclType180(self):
        return self.__OclType180

    @OclType180.setter
    def OclType180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__OclType180", None)
        self.__OclType180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL181"):
                opp_val = getattr(old_value, "OCL181", None)
                if opp_val == self:
                    setattr(old_value, "OCL181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL181"):
                opp_val = getattr(value, "OCL181", None)
                setattr(value, "OCL181", self)

    @property
    def LetExp186(self):
        return self.__LetExp186

    @LetExp186.setter
    def LetExp186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__LetExp186", None)
        self.__LetExp186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL187"):
                opp_val = getattr(old_value, "OCL187", None)
                if opp_val == self:
                    setattr(old_value, "OCL187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL187"):
                opp_val = getattr(value, "OCL187", None)
                setattr(value, "OCL187", self)

class atlstatic_OCL_OclModel(LocatedElement):

    def __init__(self, name: str, OclModel267: "OclModel" = None, OclModelElement: set["OclModelElement"] = None, OclModel272: set["OclModel"] = None):
        self.name = name
        self.OclModel267 = OclModel267
        self.OclModelElement = OclModelElement if OclModelElement is not None else set()
        self.OclModel272 = OclModel272 if OclModel272 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclModel272(self):
        return self.__OclModel272

    @OclModel272.setter
    def OclModel272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclModel__OclModel272", None)
        self.__OclModel272 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL273"):
                    opp_val = getattr(item, "OCL273", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL273", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL273"):
                    opp_val = getattr(item, "OCL273", None)
                    
                    setattr(item, "OCL273", self)
                    

    @property
    def OclModel267(self):
        return self.__OclModel267

    @OclModel267.setter
    def OclModel267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclModel__OclModel267", None)
        self.__OclModel267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL268"):
                opp_val = getattr(old_value, "OCL268", None)
                if opp_val == self:
                    setattr(old_value, "OCL268", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL268"):
                opp_val = getattr(value, "OCL268", None)
                setattr(value, "OCL268", self)

    @property
    def OclModelElement(self):
        return self.__OclModelElement

    @OclModelElement.setter
    def OclModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclModel__OclModelElement", None)
        self.__OclModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL270"):
                    opp_val = getattr(item, "OCL270", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL270"):
                    opp_val = getattr(item, "OCL270", None)
                    
                    setattr(item, "OCL270", self)
                    

class atlstatic_ATL_Binding(LocatedElement):

    def __init__(self, propertyName: str, isAssignment: str, atlstatic_ATL_Binding: "OclExpression" = None, OutPatternElement71: "OutPatternElement" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlstatic_ATL_Binding = atlstatic_ATL_Binding
        self.OutPatternElement71 = OutPatternElement71
        
    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def isAssignment(self) -> str:
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment

    @property
    def OutPatternElement71(self):
        return self.__OutPatternElement71

    @OutPatternElement71.setter
    def OutPatternElement71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Binding__OutPatternElement71", None)
        self.__OutPatternElement71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL72"):
                opp_val = getattr(old_value, "ATL72", None)
                if opp_val == self:
                    setattr(old_value, "ATL72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL72"):
                opp_val = getattr(value, "ATL72", None)
                setattr(value, "ATL72", self)

    @property
    def atlstatic_ATL_Binding(self):
        return self.__atlstatic_ATL_Binding

    @atlstatic_ATL_Binding.setter
    def atlstatic_ATL_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Binding__atlstatic_ATL_Binding", None)
        self.__atlstatic_ATL_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression69"):
                opp_val = getattr(old_value, "OclExpression69", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression69"):
                opp_val = getattr(value, "OclExpression69", None)
                setattr(value, "OclExpression69", self)

class atlstatic_ATL_Unit(LocatedElement):

    def __init__(self, name: str, LibraryRef: set["LibraryRef"] = None):
        self.name = name
        self.LibraryRef = LibraryRef if LibraryRef is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LibraryRef(self):
        return self.__LibraryRef

    @LibraryRef.setter
    def LibraryRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Unit__LibraryRef", None)
        self.__LibraryRef = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL"):
                    opp_val = getattr(item, "ATL", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL"):
                    opp_val = getattr(item, "ATL", None)
                    
                    setattr(item, "ATL", self)
                    

class Library:

    pass
class Query:

    pass
class ATL_Callable:

    pass
class ATL_ModuleElement:

    pass
class atlstatic_ATL_Helper(ATL_ModuleElement, ATL_Callable):

    pass
class atlstatic_ATL_ModuleElement(LocatedElement):

    pass
class ModuleElement:

    pass
class atlstatic_ATL_Rule(ModuleElement):

    def __init__(self, name: str, OutPattern: "OutPattern" = None, ActionBlock: "ActionBlock" = None, RuleVariableDeclaration: set["RuleVariableDeclaration"] = None, ModuleElement: "atlstatic_ATL_Module"):
        self.name = name
        self.OutPattern = OutPattern
        self.ActionBlock = ActionBlock
        self.RuleVariableDeclaration = RuleVariableDeclaration if RuleVariableDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RuleVariableDeclaration(self):
        return self.__RuleVariableDeclaration

    @RuleVariableDeclaration.setter
    def RuleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Rule__RuleVariableDeclaration", None)
        self.__RuleVariableDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL23"):
                    opp_val = getattr(item, "ATL23", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL23"):
                    opp_val = getattr(item, "ATL23", None)
                    
                    setattr(item, "ATL23", self)
                    

    @property
    def OutPattern(self):
        return self.__OutPattern

    @OutPattern.setter
    def OutPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Rule__OutPattern", None)
        self.__OutPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL19"):
                opp_val = getattr(old_value, "ATL19", None)
                if opp_val == self:
                    setattr(old_value, "ATL19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL19"):
                opp_val = getattr(value, "ATL19", None)
                setattr(value, "ATL19", self)

    @property
    def ActionBlock(self):
        return self.__ActionBlock

    @ActionBlock.setter
    def ActionBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Rule__ActionBlock", None)
        self.__ActionBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL21"):
                opp_val = getattr(old_value, "ATL21", None)
                if opp_val == self:
                    setattr(old_value, "ATL21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL21"):
                opp_val = getattr(value, "ATL21", None)
                setattr(value, "ATL21", self)

class atlstatic_ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter
