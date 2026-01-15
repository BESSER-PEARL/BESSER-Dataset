from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModelElement:

    pass
class OclFeature:

    pass
class top_OCL_Attribute(OclFeature):

    def __init__(self, name: str, OclType265: "OclType" = None, OclExpression262: "OclExpression" = None, OCL248: "top_OCL_OclFeatureDefinition"):
        self.name = name
        self.OclType265 = OclType265
        self.OclExpression262 = OclExpression262
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclExpression262(self):
        return self.__OclExpression262

    @OclExpression262.setter
    def OclExpression262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_Attribute__OclExpression262", None)
        self.__OclExpression262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL263"):
                opp_val = getattr(old_value, "OCL263", None)
                if opp_val == self:
                    setattr(old_value, "OCL263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL263"):
                opp_val = getattr(value, "OCL263", None)
                setattr(value, "OCL263", self)

    @property
    def OclType265(self):
        return self.__OclType265

    @OclType265.setter
    def OclType265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_Attribute__OclType265", None)
        self.__OclType265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL266"):
                opp_val = getattr(old_value, "OCL266", None)
                if opp_val == self:
                    setattr(old_value, "OCL266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL266"):
                opp_val = getattr(value, "OCL266", None)
                setattr(value, "OCL266", self)

class top_OCL_Operation(OclFeature):

    def __init__(self, name: str, Parameter268: set["Parameter"] = None, OclType271: "OclType" = None, OclExpression274: "OclExpression" = None, OCL248: "top_OCL_OclFeatureDefinition"):
        self.name = name
        self.Parameter268 = Parameter268 if Parameter268 is not None else set()
        self.OclType271 = OclType271
        self.OclExpression274 = OclExpression274
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclType271(self):
        return self.__OclType271

    @OclType271.setter
    def OclType271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_Operation__OclType271", None)
        self.__OclType271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL272"):
                opp_val = getattr(old_value, "OCL272", None)
                if opp_val == self:
                    setattr(old_value, "OCL272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL272"):
                opp_val = getattr(value, "OCL272", None)
                setattr(value, "OCL272", self)

    @property
    def Parameter268(self):
        return self.__Parameter268

    @Parameter268.setter
    def Parameter268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_Operation__Parameter268", None)
        self.__Parameter268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL269"):
                    opp_val = getattr(item, "OCL269", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL269", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL269"):
                    opp_val = getattr(item, "OCL269", None)
                    
                    setattr(item, "OCL269", self)
                    

    @property
    def OclExpression274(self):
        return self.__OclExpression274

    @OclExpression274.setter
    def OclExpression274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_Operation__OclExpression274", None)
        self.__OclExpression274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL275"):
                opp_val = getattr(old_value, "OCL275", None)
                if opp_val == self:
                    setattr(old_value, "OCL275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL275"):
                opp_val = getattr(value, "OCL275", None)
                setattr(value, "OCL275", self)

class NumericType:

    pass
class top_OCL_RealType(NumericType):

    pass
class top_OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class top_OCL_NumericType(Primitive):

    pass
class top_OCL_BooleanType(Primitive):

    pass
class top_OCL_StringType(Primitive):

    pass
class TupleType:

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class top_OCL_SequenceType(CollectionType):

    pass
class top_OCL_BagType(CollectionType):

    pass
class top_OCL_OrderedSetType(CollectionType):

    pass
class top_OCL_SetType(CollectionType):

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class MapExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class TuplePart:

    pass
class PrimitiveExp:

    pass
class top_OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
    @property
    def booleanSymbol(self) -> str:
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol

class top_OCL_StringExp(PrimitiveExp):

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
class Operation:

    pass
class NumericExp:

    pass
class top_OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
    @property
    def integerSymbol(self) -> str:
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol

class top_OCL_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
    @property
    def realSymbol(self) -> str:
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol

class top_OCL_NumericExp(PrimitiveExp):

    pass
class OclType:

    pass
class top_OCL_CollectionType(OclType):

    pass
class top_OCL_OclModelElement(OclType):

    pass
class top_OCL_MapType(OclType):

    pass
class top_OCL_TupleType(OclType):

    pass
class top_OCL_OclAnyType(OclType):

    pass
class top_OCL_Primitive(OclType):

    pass
class OperationCallExp:

    pass
class top_OCL_OperatorCallExp(OperationCallExp):

    pass
class top_OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class top_OCL_IterateExp(LoopExp):

    pass
class top_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, OCL200: "top_OCL_Iterator", OCL121: "top_OCL_OclExpression"):
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
class top_OCL_OrderedSetExp(CollectionExp):

    pass
class top_OCL_SequenceExp(CollectionExp):

    pass
class top_OCL_BagExp(CollectionExp):

    pass
class top_OCL_SetExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class top_OCL_LoopExp(PropertyCallExp):

    pass
class top_OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, OCL115: "top_OCL_OclExpression"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class top_OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, OclExpression159: set["OclExpression"] = None, OCL115: "top_OCL_OclExpression"):
        self.operationName = operationName
        self.OclExpression159 = OclExpression159 if OclExpression159 is not None else set()
        
    @property
    def operationName(self) -> str:
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName

    @property
    def OclExpression159(self):
        return self.__OclExpression159

    @OclExpression159.setter
    def OclExpression159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OperationCallExp__OclExpression159", None)
        self.__OclExpression159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL160"):
                    opp_val = getattr(item, "OCL160", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL160"):
                    opp_val = getattr(item, "OCL160", None)
                    
                    setattr(item, "OCL160", self)
                    

class IfExp:

    pass
class Statement:

    pass
class top_ATL_ForStat(Statement):

    pass
class top_ATL_ExpressionStat(Statement):

    pass
class top_ATL_IfStat(Statement):

    pass
class top_ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, top_ATL_BindingStat: "OclExpression" = None, top_ATL_BindingStat93: "OclExpression" = None, Statement: "top_ATL_ActionBlock", Statement110: "top_ATL_ForStat", Statement99: "top_ATL_IfStat", Statement102: "top_ATL_IfStat"):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.top_ATL_BindingStat = top_ATL_BindingStat
        self.top_ATL_BindingStat93 = top_ATL_BindingStat93
        
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
    def top_ATL_BindingStat93(self):
        return self.__top_ATL_BindingStat93

    @top_ATL_BindingStat93.setter
    def top_ATL_BindingStat93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_BindingStat__top_ATL_BindingStat93", None)
        self.__top_ATL_BindingStat93 = value
        
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

    @property
    def top_ATL_BindingStat(self):
        return self.__top_ATL_BindingStat

    @top_ATL_BindingStat.setter
    def top_ATL_BindingStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_BindingStat__top_ATL_BindingStat", None)
        self.__top_ATL_BindingStat = value
        
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

class Iterator:

    pass
class Binding:

    pass
class OutPatternElement:

    pass
class top_ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class top_ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class DropPattern:

    pass
class InPatternElement:

    pass
class top_ATL_SimpleInPatternElement(InPatternElement):

    pass
class Parameter:

    pass
class PatternElement:

    pass
class top_ATL_OutPatternElement(PatternElement):

    pass
class top_ATL_InPatternElement(PatternElement):

    pass
class VariableDeclaration:

    pass
class top_OCL_Parameter(VariableDeclaration):

    pass
class top_ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class top_OCL_TuplePart(VariableDeclaration):

    pass
class top_OCL_Iterator(VariableDeclaration):

    pass
class top_ATL_PatternElement(VariableDeclaration):

    pass
class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OutPattern:

    pass
class OclFeatureDefinition:

    pass
class Library:

    pass
class Query:

    pass
class Module:

    pass
class ModuleElement:

    pass
class top_ATL_Helper(ModuleElement):

    pass
class top_ATL_Rule(ModuleElement):

    def __init__(self, name: str, OutPattern: "OutPattern" = None, ActionBlock: "ActionBlock" = None, RuleVariableDeclaration: set["RuleVariableDeclaration"] = None, ATL12: "top_ATL_Module"):
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
        old_value = getattr(self, f"_top_ATL_Rule__RuleVariableDeclaration", None)
        self.__RuleVariableDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL25"):
                    opp_val = getattr(item, "ATL25", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL25"):
                    opp_val = getattr(item, "ATL25", None)
                    
                    setattr(item, "ATL25", self)
                    

    @property
    def ActionBlock(self):
        return self.__ActionBlock

    @ActionBlock.setter
    def ActionBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_Rule__ActionBlock", None)
        self.__ActionBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL23"):
                opp_val = getattr(old_value, "ATL23", None)
                if opp_val == self:
                    setattr(old_value, "ATL23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL23"):
                opp_val = getattr(value, "ATL23", None)
                setattr(value, "ATL23", self)

    @property
    def OutPattern(self):
        return self.__OutPattern

    @OutPattern.setter
    def OutPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_Rule__OutPattern", None)
        self.__OutPattern = value
        
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

class MatchedRule:

    pass
class top_ATL_LazyMatchedRule(MatchedRule):

    def __init__(self, isUnique: str, ATL32: "top_ATL_MatchedRule", ATL29: "top_ATL_MatchedRule", ATL38: "top_ATL_InPattern"):
        self.isUnique = isUnique
        
    @property
    def isUnique(self) -> str:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique

class InPattern:

    pass
class Rule:

    pass
class top_ATL_CalledRule(Rule):

    def __init__(self, isEntrypoint: str, isEndpoint: str, top_ATL_CalledRule: set["Parameter"] = None, ATL86: "top_ATL_ActionBlock", ATL81: "top_ATL_RuleVariableDeclaration", ATL42: "top_ATL_OutPattern"):
        self.isEntrypoint = isEntrypoint
        self.isEndpoint = isEndpoint
        self.top_ATL_CalledRule = top_ATL_CalledRule if top_ATL_CalledRule is not None else set()
        
    @property
    def isEntrypoint(self) -> str:
        return self.__isEntrypoint

    @isEntrypoint.setter
    def isEntrypoint(self, isEntrypoint: str):
        self.__isEntrypoint = isEntrypoint

    @property
    def isEndpoint(self) -> str:
        return self.__isEndpoint

    @isEndpoint.setter
    def isEndpoint(self, isEndpoint: str):
        self.__isEndpoint = isEndpoint

    @property
    def top_ATL_CalledRule(self):
        return self.__top_ATL_CalledRule

    @top_ATL_CalledRule.setter
    def top_ATL_CalledRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_CalledRule__top_ATL_CalledRule", None)
        self.__top_ATL_CalledRule = value if value is not None else set()
        
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
                    

class top_ATL_MatchedRule(Rule):

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, InPattern: "InPattern" = None, MatchedRule: set["MatchedRule"] = None, MatchedRule31: "MatchedRule" = None, ATL86: "top_ATL_ActionBlock", ATL81: "top_ATL_RuleVariableDeclaration", ATL42: "top_ATL_OutPattern"):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.InPattern = InPattern
        self.MatchedRule = MatchedRule if MatchedRule is not None else set()
        self.MatchedRule31 = MatchedRule31
        
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
    def InPattern(self):
        return self.__InPattern

    @InPattern.setter
    def InPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_MatchedRule__InPattern", None)
        self.__InPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL27"):
                opp_val = getattr(old_value, "ATL27", None)
                if opp_val == self:
                    setattr(old_value, "ATL27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL27"):
                opp_val = getattr(value, "ATL27", None)
                setattr(value, "ATL27", self)

    @property
    def MatchedRule31(self):
        return self.__MatchedRule31

    @MatchedRule31.setter
    def MatchedRule31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_MatchedRule__MatchedRule31", None)
        self.__MatchedRule31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL32"):
                opp_val = getattr(old_value, "ATL32", None)
                if opp_val == self:
                    setattr(old_value, "ATL32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL32"):
                opp_val = getattr(value, "ATL32", None)
                setattr(value, "ATL32", self)

    @property
    def MatchedRule(self):
        return self.__MatchedRule

    @MatchedRule.setter
    def MatchedRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_MatchedRule__MatchedRule", None)
        self.__MatchedRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL29"):
                    opp_val = getattr(item, "ATL29", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL29"):
                    opp_val = getattr(item, "ATL29", None)
                    
                    setattr(item, "ATL29", self)
                    

class Helper:

    pass
class Unit:

    pass
class top_ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class LocatedElement:

    pass
class top_ATL_InPattern(LocatedElement):

    pass
class top_OCL_MapElement(LocatedElement):

    pass
class top_OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, TupleType: "TupleType" = None, OclType234: "OclType" = None):
        self.name = name
        self.TupleType = TupleType
        self.OclType234 = OclType234
        
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
        old_value = getattr(self, f"_top_OCL_TupleTypeAttribute__TupleType", None)
        self.__TupleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL237"):
                opp_val = getattr(old_value, "OCL237", None)
                if opp_val == self:
                    setattr(old_value, "OCL237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL237"):
                opp_val = getattr(value, "OCL237", None)
                setattr(value, "OCL237", self)

    @property
    def OclType234(self):
        return self.__OclType234

    @OclType234.setter
    def OclType234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_TupleTypeAttribute__OclType234", None)
        self.__OclType234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL235"):
                opp_val = getattr(old_value, "OCL235", None)
                if opp_val == self:
                    setattr(old_value, "OCL235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL235"):
                opp_val = getattr(value, "OCL235", None)
                setattr(value, "OCL235", self)

class top_OCL_OclFeatureDefinition(LocatedElement):

    pass
class top_ATL_OutPattern(LocatedElement):

    pass
class top_ATL_ActionBlock(LocatedElement):

    pass
class top_OCL_OclExpression(LocatedElement):

    pass
class top_OCL_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, IterateExp: "IterateExp" = None, VariableExp: set["VariableExp"] = None, OclType186: "OclType" = None, OclExpression189: "OclExpression" = None, LetExp192: "LetExp" = None):
        self.id = id
        self.varName = varName
        self.IterateExp = IterateExp
        self.VariableExp = VariableExp if VariableExp is not None else set()
        self.OclType186 = OclType186
        self.OclExpression189 = OclExpression189
        self.LetExp192 = LetExp192
        
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
    def IterateExp(self):
        return self.__IterateExp

    @IterateExp.setter
    def IterateExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_VariableDeclaration__IterateExp", None)
        self.__IterateExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL195"):
                opp_val = getattr(old_value, "OCL195", None)
                if opp_val == self:
                    setattr(old_value, "OCL195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL195"):
                opp_val = getattr(value, "OCL195", None)
                setattr(value, "OCL195", self)

    @property
    def VariableExp(self):
        return self.__VariableExp

    @VariableExp.setter
    def VariableExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_VariableDeclaration__VariableExp", None)
        self.__VariableExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL197"):
                    opp_val = getattr(item, "OCL197", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL197", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL197"):
                    opp_val = getattr(item, "OCL197", None)
                    
                    setattr(item, "OCL197", self)
                    

    @property
    def LetExp192(self):
        return self.__LetExp192

    @LetExp192.setter
    def LetExp192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_VariableDeclaration__LetExp192", None)
        self.__LetExp192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL193"):
                opp_val = getattr(old_value, "OCL193", None)
                if opp_val == self:
                    setattr(old_value, "OCL193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL193"):
                opp_val = getattr(value, "OCL193", None)
                setattr(value, "OCL193", self)

    @property
    def OclType186(self):
        return self.__OclType186

    @OclType186.setter
    def OclType186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_VariableDeclaration__OclType186", None)
        self.__OclType186 = value
        
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

    @property
    def OclExpression189(self):
        return self.__OclExpression189

    @OclExpression189.setter
    def OclExpression189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_VariableDeclaration__OclExpression189", None)
        self.__OclExpression189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL190"):
                opp_val = getattr(old_value, "OCL190", None)
                if opp_val == self:
                    setattr(old_value, "OCL190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL190"):
                opp_val = getattr(value, "OCL190", None)
                setattr(value, "OCL190", self)

class top_OCL_OclContextDefinition(LocatedElement):

    pass
class top_ATL_Binding(LocatedElement):

    def __init__(self, propertyName: str, isAssignment: str, OutPatternElement77: "OutPatternElement" = None, top_ATL_Binding: "OclExpression" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.OutPatternElement77 = OutPatternElement77
        self.top_ATL_Binding = top_ATL_Binding
        
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
    def OutPatternElement77(self):
        return self.__OutPatternElement77

    @OutPatternElement77.setter
    def OutPatternElement77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_Binding__OutPatternElement77", None)
        self.__OutPatternElement77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL78"):
                opp_val = getattr(old_value, "ATL78", None)
                if opp_val == self:
                    setattr(old_value, "ATL78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL78"):
                opp_val = getattr(value, "ATL78", None)
                setattr(value, "ATL78", self)

    @property
    def top_ATL_Binding(self):
        return self.__top_ATL_Binding

    @top_ATL_Binding.setter
    def top_ATL_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_Binding__top_ATL_Binding", None)
        self.__top_ATL_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression75"):
                opp_val = getattr(old_value, "OclExpression75", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression75"):
                opp_val = getattr(value, "OclExpression75", None)
                setattr(value, "OclExpression75", self)

class top_ATL_Statement(LocatedElement):

    pass
class top_ATL_DropPattern(LocatedElement):

    pass
class top_ATL_ModuleElement(LocatedElement):

    pass
class top_OCL_OclFeature(LocatedElement):

    pass
class top_OCL_OclModel(LocatedElement):

    def __init__(self, name: str, OclModel277: "OclModel" = None, OclModelElement: set["OclModelElement"] = None, OclModel282: set["OclModel"] = None):
        self.name = name
        self.OclModel277 = OclModel277
        self.OclModelElement = OclModelElement if OclModelElement is not None else set()
        self.OclModel282 = OclModel282 if OclModel282 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def OclModel277(self):
        return self.__OclModel277

    @OclModel277.setter
    def OclModel277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclModel__OclModel277", None)
        self.__OclModel277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL278"):
                opp_val = getattr(old_value, "OCL278", None)
                if opp_val == self:
                    setattr(old_value, "OCL278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL278"):
                opp_val = getattr(value, "OCL278", None)
                setattr(value, "OCL278", self)

    @property
    def OclModel282(self):
        return self.__OclModel282

    @OclModel282.setter
    def OclModel282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclModel__OclModel282", None)
        self.__OclModel282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL283"):
                    opp_val = getattr(item, "OCL283", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL283"):
                    opp_val = getattr(item, "OCL283", None)
                    
                    setattr(item, "OCL283", self)
                    

    @property
    def OclModelElement(self):
        return self.__OclModelElement

    @OclModelElement.setter
    def OclModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclModel__OclModelElement", None)
        self.__OclModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OCL280"):
                    opp_val = getattr(item, "OCL280", None)
                    
                    if opp_val == self:
                        setattr(item, "OCL280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OCL280"):
                    opp_val = getattr(item, "OCL280", None)
                    
                    setattr(item, "OCL280", self)
                    

class top_ATL_LibraryRef(LocatedElement):

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
        old_value = getattr(self, f"_top_ATL_LibraryRef__Unit", None)
        self.__Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATL83"):
                opp_val = getattr(old_value, "ATL83", None)
                if opp_val == self:
                    setattr(old_value, "ATL83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATL83"):
                opp_val = getattr(value, "ATL83", None)
                setattr(value, "ATL83", self)

class top_ATL_Unit(LocatedElement):

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
        old_value = getattr(self, f"_top_ATL_Unit__LibraryRef", None)
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
                    

class top_ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class OclModel:

    pass
class top_ATL_Module(Unit):

    def __init__(self, isRefining: str, top_ATL_Module: set["OclModel"] = None, top_ATL_Module9: set["OclModel"] = None, ModuleElement: set["ModuleElement"] = None, ATL83: "top_ATL_LibraryRef"):
        self.isRefining = isRefining
        self.top_ATL_Module = top_ATL_Module if top_ATL_Module is not None else set()
        self.top_ATL_Module9 = top_ATL_Module9 if top_ATL_Module9 is not None else set()
        self.ModuleElement = ModuleElement if ModuleElement is not None else set()
        
    @property
    def isRefining(self) -> str:
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining

    @property
    def ModuleElement(self):
        return self.__ModuleElement

    @ModuleElement.setter
    def ModuleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_Module__ModuleElement", None)
        self.__ModuleElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ATL12"):
                    opp_val = getattr(item, "ATL12", None)
                    
                    if opp_val == self:
                        setattr(item, "ATL12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ATL12"):
                    opp_val = getattr(item, "ATL12", None)
                    
                    setattr(item, "ATL12", self)
                    

    @property
    def top_ATL_Module9(self):
        return self.__top_ATL_Module9

    @top_ATL_Module9.setter
    def top_ATL_Module9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_Module__top_ATL_Module9", None)
        self.__top_ATL_Module9 = value if value is not None else set()
        
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
    def top_ATL_Module(self):
        return self.__top_ATL_Module

    @top_ATL_Module.setter
    def top_ATL_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_ATL_Module__top_ATL_Module", None)
        self.__top_ATL_Module = value if value is not None else set()
        
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
                    

class OclExpression:

    pass
class top_OCL_PropertyCallExp(OclExpression):

    pass
class top_OCL_IfExp(OclExpression):

    pass
class top_OCL_PrimitiveExp(OclExpression):

    pass
class top_OCL_OclUndefinedExp(OclExpression):

    pass
class top_OCL_MapExp(OclExpression):

    pass
class top_OCL_SuperExp(OclExpression):

    pass
class top_OCL_LetExp(OclExpression):

    pass
class top_OCL_TupleExp(OclExpression):

    pass
class top_OCL_CollectionExp(OclExpression):

    pass
class top_OCL_OclType(OclExpression):

    def __init__(self, name: str, CollectionType: "CollectionType" = None, TupleTypeAttribute: "TupleTypeAttribute" = None, VariableDeclaration228: "VariableDeclaration" = None, OclContextDefinition: "OclContextDefinition" = None, OclExpression210: "OclExpression" = None, Operation213: "Operation" = None, MapType: "MapType" = None, Attribute218: "Attribute" = None, MapType221: "MapType" = None, OclExpression40: "top_ATL_InPattern", OclExpression69: "top_ATL_SimpleOutPatternElement", OCL190: "top_OCL_VariableDeclaration", OCL181: "top_OCL_IfExp", OCL157: "top_OCL_PropertyCallExp", OCL163: "top_OCL_LoopExp", OCL175: "top_OCL_LetExp", OCL141: "top_OCL_CollectionExp", OclExpression107: "top_ATL_ForStat", OCL178: "top_OCL_IfExp", OCL211: "top_OCL_OclType", OCL263: "top_OCL_Attribute", OclExpression154: "top_OCL_MapElement", OCL160: "top_OCL_OperationCallExp", OclExpression94: "top_ATL_BindingStat", OCL184: "top_OCL_IfExp", OclExpression75: "top_ATL_Binding", OclExpression151: "top_OCL_MapElement", OclExpression71: "top_ATL_ForEachOutPatternElement", OCL275: "top_OCL_Operation", OclExpression91: "top_ATL_BindingStat", OclExpression: "top_ATL_Query", OclExpression96: "top_ATL_IfStat", OclExpression89: "top_ATL_ExpressionStat"):
        self.name = name
        self.CollectionType = CollectionType
        self.TupleTypeAttribute = TupleTypeAttribute
        self.VariableDeclaration228 = VariableDeclaration228
        self.OclContextDefinition = OclContextDefinition
        self.OclExpression210 = OclExpression210
        self.Operation213 = Operation213
        self.MapType = MapType
        self.Attribute218 = Attribute218
        self.MapType221 = MapType221
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MapType(self):
        return self.__MapType

    @MapType.setter
    def MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclType__MapType", None)
        self.__MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL216"):
                opp_val = getattr(old_value, "OCL216", None)
                if opp_val == self:
                    setattr(old_value, "OCL216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL216"):
                opp_val = getattr(value, "OCL216", None)
                setattr(value, "OCL216", self)

    @property
    def VariableDeclaration228(self):
        return self.__VariableDeclaration228

    @VariableDeclaration228.setter
    def VariableDeclaration228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclType__VariableDeclaration228", None)
        self.__VariableDeclaration228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL229"):
                opp_val = getattr(old_value, "OCL229", None)
                if opp_val == self:
                    setattr(old_value, "OCL229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL229"):
                opp_val = getattr(value, "OCL229", None)
                setattr(value, "OCL229", self)

    @property
    def Attribute218(self):
        return self.__Attribute218

    @Attribute218.setter
    def Attribute218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclType__Attribute218", None)
        self.__Attribute218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL219"):
                opp_val = getattr(old_value, "OCL219", None)
                if opp_val == self:
                    setattr(old_value, "OCL219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL219"):
                opp_val = getattr(value, "OCL219", None)
                setattr(value, "OCL219", self)

    @property
    def OclExpression210(self):
        return self.__OclExpression210

    @OclExpression210.setter
    def OclExpression210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclType__OclExpression210", None)
        self.__OclExpression210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL211"):
                opp_val = getattr(old_value, "OCL211", None)
                if opp_val == self:
                    setattr(old_value, "OCL211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL211"):
                opp_val = getattr(value, "OCL211", None)
                setattr(value, "OCL211", self)

    @property
    def TupleTypeAttribute(self):
        return self.__TupleTypeAttribute

    @TupleTypeAttribute.setter
    def TupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclType__TupleTypeAttribute", None)
        self.__TupleTypeAttribute = value
        
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

    @property
    def Operation213(self):
        return self.__Operation213

    @Operation213.setter
    def Operation213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclType__Operation213", None)
        self.__Operation213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL214"):
                opp_val = getattr(old_value, "OCL214", None)
                if opp_val == self:
                    setattr(old_value, "OCL214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL214"):
                opp_val = getattr(value, "OCL214", None)
                setattr(value, "OCL214", self)

    @property
    def OclContextDefinition(self):
        return self.__OclContextDefinition

    @OclContextDefinition.setter
    def OclContextDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclType__OclContextDefinition", None)
        self.__OclContextDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL208"):
                opp_val = getattr(old_value, "OCL208", None)
                if opp_val == self:
                    setattr(old_value, "OCL208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL208"):
                opp_val = getattr(value, "OCL208", None)
                setattr(value, "OCL208", self)

    @property
    def MapType221(self):
        return self.__MapType221

    @MapType221.setter
    def MapType221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclType__MapType221", None)
        self.__MapType221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL222"):
                opp_val = getattr(old_value, "OCL222", None)
                if opp_val == self:
                    setattr(old_value, "OCL222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL222"):
                opp_val = getattr(value, "OCL222", None)
                setattr(value, "OCL222", self)

    @property
    def CollectionType(self):
        return self.__CollectionType

    @CollectionType.setter
    def CollectionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_top_OCL_OclType__CollectionType", None)
        self.__CollectionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OCL224"):
                opp_val = getattr(old_value, "OCL224", None)
                if opp_val == self:
                    setattr(old_value, "OCL224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OCL224"):
                opp_val = getattr(value, "OCL224", None)
                setattr(value, "OCL224", self)

class top_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression40: "top_ATL_InPattern", OclExpression69: "top_ATL_SimpleOutPatternElement", OCL190: "top_OCL_VariableDeclaration", OCL181: "top_OCL_IfExp", OCL157: "top_OCL_PropertyCallExp", OCL163: "top_OCL_LoopExp", OCL175: "top_OCL_LetExp", OCL141: "top_OCL_CollectionExp", OclExpression107: "top_ATL_ForStat", OCL178: "top_OCL_IfExp", OCL211: "top_OCL_OclType", OCL263: "top_OCL_Attribute", OclExpression154: "top_OCL_MapElement", OCL160: "top_OCL_OperationCallExp", OclExpression94: "top_ATL_BindingStat", OCL184: "top_OCL_IfExp", OclExpression75: "top_ATL_Binding", OclExpression151: "top_OCL_MapElement", OclExpression71: "top_ATL_ForEachOutPatternElement", OCL275: "top_OCL_Operation", OclExpression91: "top_ATL_BindingStat", OclExpression: "top_ATL_Query", OclExpression96: "top_ATL_IfStat", OclExpression89: "top_ATL_ExpressionStat"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class top_OCL_VariableExp(OclExpression):

    pass
class top_ATL_Query(Unit):

    pass