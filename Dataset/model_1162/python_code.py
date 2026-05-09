from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TupleTypeAttribute:

    pass
class CollectionType:

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class OCL_SetType(CollectionType):

    pass
class OCL_SequenceType(CollectionType):

    pass
class IterateExp:

    pass
class OCL_OrderedSetType(CollectionType):

    pass
class VariableExp:

    pass
class MapElement:

    pass
class TupleExp:

    pass
class TuplePart:

    pass
class OclModelElement:

    pass
class OclFeature:

    pass
class OCL_Attribute(OclFeature):

    def __init__(self, name: str, owningAttribute: "OclExpression" = None, attribute: "OclType" = None, OclFeature: "OCL_OclFeatureDefinition" = None):
        self.name = name
        self.owningAttribute = owningAttribute
        self.attribute = attribute
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def owningAttribute(self):
        return self.__owningAttribute

    @owningAttribute.setter
    def owningAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__owningAttribute", None)
        self.__owningAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression196"):
                opp_val = getattr(old_value, "OclExpression196", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression196"):
                opp_val = getattr(value, "OclExpression196", None)
                setattr(value, "OclExpression196", self)

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType198"):
                opp_val = getattr(old_value, "OclType198", None)
                if opp_val == self:
                    setattr(old_value, "OclType198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType198"):
                opp_val = getattr(value, "OclType198", None)
                setattr(value, "OclType198", self)

class TupleType:

    pass
class OCL_Operation(OclFeature):

    def __init__(self, name: str, operation: set["Parameter"] = None, operation202: "OclType" = None, owningOperation: "OclExpression" = None, OclFeature: "OCL_OclFeatureDefinition" = None):
        self.name = name
        self.operation = operation if operation is not None else set()
        self.operation202 = operation202
        self.owningOperation = owningOperation
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def operation202(self):
        return self.__operation202

    @operation202.setter
    def operation202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__operation202", None)
        self.__operation202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType203"):
                opp_val = getattr(old_value, "OclType203", None)
                if opp_val == self:
                    setattr(old_value, "OclType203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType203"):
                opp_val = getattr(value, "OclType203", None)
                setattr(value, "OclType203", self)

    @property
    def owningOperation(self):
        return self.__owningOperation

    @owningOperation.setter
    def owningOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__owningOperation", None)
        self.__owningOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression205"):
                opp_val = getattr(old_value, "OclExpression205", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression205"):
                opp_val = getattr(value, "OclExpression205", None)
                setattr(value, "OclExpression205", self)

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_Operation__operation", None)
        self.__operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter200"):
                    opp_val = getattr(item, "Parameter200", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter200", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter200"):
                    opp_val = getattr(item, "Parameter200", None)
                    
                    setattr(item, "Parameter200", self)
                    

class OCL_BagType(CollectionType):

    pass
class NumericType:

    pass
class OCL_RealType(NumericType):

    pass
class OCL_IntegerType(NumericType):

    pass
class Primitive:

    pass
class OCL_NumericType(Primitive):

    pass
class OCL_BooleanType(Primitive):

    pass
class OCL_StringType(Primitive):

    pass
class NumericExp:

    pass
class OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


class OCL_RealExp(NumericExp):

    def __init__(self, realSymbol: str):
        self.realSymbol = realSymbol
        
        pass
    @property
    def realSymbol(self):
        return self.__realSymbol

    @realSymbol.setter
    def realSymbol(self, realSymbol: str):
        self.__realSymbol = realSymbol


class PrimitiveExp:

    pass
class OCL_NumericExp(PrimitiveExp):

    pass
class OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class OCL_StringExp(PrimitiveExp):

    def __init__(self, stringSymbol: str):
        self.stringSymbol = stringSymbol
        
        pass
    @property
    def stringSymbol(self):
        return self.__stringSymbol

    @stringSymbol.setter
    def stringSymbol(self, stringSymbol: str):
        self.__stringSymbol = stringSymbol


class Attribute:

    pass
class Operation:

    pass
class MapExp:

    pass
class LoopExp:

    pass
class OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, LoopExp150: "OCL_Iterator" = None, LoopExp: "OCL_OclExpression" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class OCL_IterateExp(LoopExp):

    pass
class LetExp:

    pass
class CollectionExp:

    pass
class OCL_SequenceExp(CollectionExp):

    pass
class OCL_OrderedSetExp(CollectionExp):

    pass
class OCL_SetExp(CollectionExp):

    pass
class OCL_BagExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class OCL_LoopExp(PropertyCallExp):

    pass
class OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, parentOperation: set["OclExpression"] = None, PropertyCallExp: "OCL_OclExpression" = None):
        self.operationName = operationName
        self.parentOperation = parentOperation if parentOperation is not None else set()
        
        pass
    @property
    def operationName(self):
        return self.__operationName

    @operationName.setter
    def operationName(self, operationName: str):
        self.__operationName = operationName


    @property
    def parentOperation(self):
        return self.__parentOperation

    @parentOperation.setter
    def parentOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OperationCallExp__parentOperation", None)
        self.__parentOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression123"):
                    opp_val = getattr(item, "OclExpression123", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression123"):
                    opp_val = getattr(item, "OclExpression123", None)
                    
                    setattr(item, "OclExpression123", self)
                    

class OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, PropertyCallExp: "OCL_OclExpression" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class IfExp:

    pass
class OclType:

    pass
class OCL_TupleType(OclType):

    pass
class OCL_OclModelElement(OclType):

    pass
class OCL_MapType(OclType):

    pass
class OCL_Primitive(OclType):

    pass
class OCL_OclAnyType(OclType):

    pass
class OCL_CollectionType(OclType):

    pass
class Statement:

    pass
class ATL_ExpressionStat(Statement):

    pass
class ATL_ForStat(Statement):

    pass
class ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, ATL_BindingStat: "OclExpression" = None, ATL_BindingStat71: "OclExpression" = None, Statement80: "ATL_IfStat" = None, Statement: "ATL_ActionBlock" = None, Statement88: "ATL_ForStat" = None, Statement77: "ATL_IfStat" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.ATL_BindingStat = ATL_BindingStat
        self.ATL_BindingStat71 = ATL_BindingStat71
        
        pass
    @property
    def isAssignment(self):
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment


    @property
    def propertyName(self):
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName


    @property
    def ATL_BindingStat(self):
        return self.__ATL_BindingStat

    @ATL_BindingStat.setter
    def ATL_BindingStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_BindingStat__ATL_BindingStat", None)
        self.__ATL_BindingStat = value
        
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

    @property
    def ATL_BindingStat71(self):
        return self.__ATL_BindingStat71

    @ATL_BindingStat71.setter
    def ATL_BindingStat71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_BindingStat__ATL_BindingStat71", None)
        self.__ATL_BindingStat71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression72"):
                opp_val = getattr(old_value, "OclExpression72", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression72"):
                opp_val = getattr(value, "OclExpression72", None)
                setattr(value, "OclExpression72", self)

class ATL_IfStat(Statement):

    pass
class OperationCallExp:

    pass
class OCL_OperatorCallExp(OperationCallExp):

    pass
class OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class Iterator:

    pass
class Binding:

    pass
class PatternElement:

    pass
class ATL_OutPatternElement(PatternElement):

    pass
class ATL_InPatternElement(PatternElement):

    pass
class VariableDeclaration:

    pass
class OCL_TuplePart(VariableDeclaration):

    pass
class OCL_Iterator(VariableDeclaration):

    pass
class ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class OCL_Parameter(VariableDeclaration):

    pass
class ATL_PatternElement(VariableDeclaration):

    pass
class OutPatternElement:

    pass
class ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class InPatternElement:

    pass
class Parameter:

    pass
class MatchedRule:

    pass
class ATL_LazyMatchedRule(MatchedRule):

    def __init__(self, isUnique: str, MatchedRule: "ATL_MatchedRule" = None, MatchedRule29: "ATL_InPattern" = None, MatchedRule24: "ATL_MatchedRule" = None):
        self.isUnique = isUnique
        
        pass
    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: str):
        self.__isUnique = isUnique


class InPattern:

    pass
class Rule:

    pass
class ATL_CalledRule(Rule):

    def __init__(self, isEntrypoint: str, isEndpoint: str, ATL_CalledRule: set["Parameter"] = None, Rule61: "ATL_RuleVariableDeclaration" = None, Rule: "ATL_OutPattern" = None, Rule64: "ATL_ActionBlock" = None):
        self.isEntrypoint = isEntrypoint
        self.isEndpoint = isEndpoint
        self.ATL_CalledRule = ATL_CalledRule if ATL_CalledRule is not None else set()
        
        pass
    @property
    def isEndpoint(self):
        return self.__isEndpoint

    @isEndpoint.setter
    def isEndpoint(self, isEndpoint: str):
        self.__isEndpoint = isEndpoint


    @property
    def isEntrypoint(self):
        return self.__isEntrypoint

    @isEntrypoint.setter
    def isEntrypoint(self, isEntrypoint: str):
        self.__isEntrypoint = isEntrypoint


    @property
    def ATL_CalledRule(self):
        return self.__ATL_CalledRule

    @ATL_CalledRule.setter
    def ATL_CalledRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_CalledRule__ATL_CalledRule", None)
        self.__ATL_CalledRule = value if value is not None else set()
        
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
                    

class ATL_MatchedRule(Rule):

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, rule21: "InPattern" = None, superRule: set["MatchedRule"] = None, children: "MatchedRule" = None, Rule61: "ATL_RuleVariableDeclaration" = None, Rule: "ATL_OutPattern" = None, Rule64: "ATL_ActionBlock" = None):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.rule21 = rule21
        self.superRule = superRule if superRule is not None else set()
        self.children = children
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def isNoDefault(self):
        return self.__isNoDefault

    @isNoDefault.setter
    def isNoDefault(self, isNoDefault: str):
        self.__isNoDefault = isNoDefault


    @property
    def isRefining(self):
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining


    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_MatchedRule__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MatchedRule24"):
                opp_val = getattr(old_value, "MatchedRule24", None)
                if opp_val == self:
                    setattr(old_value, "MatchedRule24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MatchedRule24"):
                opp_val = getattr(value, "MatchedRule24", None)
                setattr(value, "MatchedRule24", self)

    @property
    def superRule(self):
        return self.__superRule

    @superRule.setter
    def superRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_MatchedRule__superRule", None)
        self.__superRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MatchedRule"):
                    opp_val = getattr(item, "MatchedRule", None)
                    
                    if opp_val == self:
                        setattr(item, "MatchedRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MatchedRule"):
                    opp_val = getattr(item, "MatchedRule", None)
                    
                    setattr(item, "MatchedRule", self)
                    

    @property
    def rule21(self):
        return self.__rule21

    @rule21.setter
    def rule21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_MatchedRule__rule21", None)
        self.__rule21 = value
        
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

class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class ATL_SimpleInPatternElement(InPatternElement):

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
class ATL_Helper(ModuleElement):

    pass
class ATL_Rule(ModuleElement):

    def __init__(self, name: str, rule: "OutPattern" = None, rule17: "ActionBlock" = None, rule19: set["RuleVariableDeclaration"] = None, ModuleElement: "ATL_Module" = None):
        self.name = name
        self.rule = rule
        self.rule17 = rule17
        self.rule19 = rule19 if rule19 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def rule(self):
        return self.__rule

    @rule.setter
    def rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Rule__rule", None)
        self.__rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutPattern"):
                opp_val = getattr(old_value, "OutPattern", None)
                if opp_val == self:
                    setattr(old_value, "OutPattern", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutPattern"):
                opp_val = getattr(value, "OutPattern", None)
                setattr(value, "OutPattern", self)

    @property
    def rule17(self):
        return self.__rule17

    @rule17.setter
    def rule17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Rule__rule17", None)
        self.__rule17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActionBlock"):
                opp_val = getattr(old_value, "ActionBlock", None)
                if opp_val == self:
                    setattr(old_value, "ActionBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActionBlock"):
                opp_val = getattr(value, "ActionBlock", None)
                setattr(value, "ActionBlock", self)

    @property
    def rule19(self):
        return self.__rule19

    @rule19.setter
    def rule19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Rule__rule19", None)
        self.__rule19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RuleVariableDeclaration"):
                    opp_val = getattr(item, "RuleVariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "RuleVariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RuleVariableDeclaration"):
                    opp_val = getattr(item, "RuleVariableDeclaration", None)
                    
                    setattr(item, "RuleVariableDeclaration", self)
                    

class OclModel:

    pass
class OclExpression:

    pass
class OCL_VariableExp(OclExpression):

    pass
class OCL_MapExp(OclExpression):

    pass
class OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression144: "OCL_VariableDeclaration" = None, OclExpression140: "OCL_IfExp" = None, OclExpression69: "ATL_BindingStat" = None, OclExpression196: "OCL_Attribute" = None, OclExpression123: "OCL_OperationCallExp" = None, OclExpression53: "ATL_ForEachOutPatternElement" = None, OclExpression138: "OCL_IfExp" = None, OclExpression72: "ATL_BindingStat" = None, OclExpression85: "ATL_ForStat" = None, OclExpression: "ATL_Query" = None, OclExpression134: "OCL_LetExp" = None, OclExpression51: "ATL_SimpleOutPatternElement" = None, OclExpression157: "OCL_OclType" = None, OclExpression109: "OCL_CollectionExp" = None, OclExpression74: "ATL_IfStat" = None, OclExpression119: "OCL_MapElement" = None, OclExpression116: "OCL_MapElement" = None, OclExpression67: "ATL_ExpressionStat" = None, OclExpression31: "ATL_InPattern" = None, OclExpression136: "OCL_IfExp" = None, OclExpression121: "OCL_PropertyCallExp" = None, OclExpression205: "OCL_Operation" = None, OclExpression57: "ATL_Binding" = None, OclExpression125: "OCL_LoopExp" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class OCL_CollectionExp(OclExpression):

    pass
class OCL_OclUndefinedExp(OclExpression):

    pass
class OCL_OclType(OclExpression):

    def __init__(self, name: str, context_: "OclContextDefinition" = None, type: "OclExpression" = None, returnType: "Operation" = None, valueType: "MapType" = None, type162: "Attribute" = None, keyType: "MapType" = None, elementType: "CollectionType" = None, type168: "TupleTypeAttribute" = None, type170: "VariableDeclaration" = None, OclExpression144: "OCL_VariableDeclaration" = None, OclExpression140: "OCL_IfExp" = None, OclExpression69: "ATL_BindingStat" = None, OclExpression196: "OCL_Attribute" = None, OclExpression123: "OCL_OperationCallExp" = None, OclExpression53: "ATL_ForEachOutPatternElement" = None, OclExpression138: "OCL_IfExp" = None, OclExpression72: "ATL_BindingStat" = None, OclExpression85: "ATL_ForStat" = None, OclExpression: "ATL_Query" = None, OclExpression134: "OCL_LetExp" = None, OclExpression51: "ATL_SimpleOutPatternElement" = None, OclExpression157: "OCL_OclType" = None, OclExpression109: "OCL_CollectionExp" = None, OclExpression74: "ATL_IfStat" = None, OclExpression119: "OCL_MapElement" = None, OclExpression116: "OCL_MapElement" = None, OclExpression67: "ATL_ExpressionStat" = None, OclExpression31: "ATL_InPattern" = None, OclExpression136: "OCL_IfExp" = None, OclExpression121: "OCL_PropertyCallExp" = None, OclExpression205: "OCL_Operation" = None, OclExpression57: "ATL_Binding" = None, OclExpression125: "OCL_LoopExp" = None):
        self.name = name
        self.context_ = context_
        self.type = type
        self.returnType = returnType
        self.valueType = valueType
        self.type162 = type162
        self.keyType = keyType
        self.elementType = elementType
        self.type168 = type168
        self.type170 = type170
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression157"):
                opp_val = getattr(old_value, "OclExpression157", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression157"):
                opp_val = getattr(value, "OclExpression157", None)
                setattr(value, "OclExpression157", self)

    @property
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation159"):
                opp_val = getattr(old_value, "Operation159", None)
                if opp_val == self:
                    setattr(old_value, "Operation159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation159"):
                opp_val = getattr(value, "Operation159", None)
                setattr(value, "Operation159", self)

    @property
    def type170(self):
        return self.__type170

    @type170.setter
    def type170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type170", None)
        self.__type170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration171"):
                opp_val = getattr(old_value, "VariableDeclaration171", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration171"):
                opp_val = getattr(value, "VariableDeclaration171", None)
                setattr(value, "VariableDeclaration171", self)

    @property
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType165"):
                opp_val = getattr(old_value, "MapType165", None)
                if opp_val == self:
                    setattr(old_value, "MapType165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType165"):
                opp_val = getattr(value, "MapType165", None)
                setattr(value, "MapType165", self)

    @property
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__elementType", None)
        self.__elementType = value
        
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
    def type162(self):
        return self.__type162

    @type162.setter
    def type162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type162", None)
        self.__type162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute163"):
                opp_val = getattr(old_value, "Attribute163", None)
                if opp_val == self:
                    setattr(old_value, "Attribute163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute163"):
                opp_val = getattr(value, "Attribute163", None)
                setattr(value, "Attribute163", self)

    @property
    def context_(self):
        return self.__context_

    @context_.setter
    def context_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__context_", None)
        self.__context_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclContextDefinition"):
                opp_val = getattr(old_value, "OclContextDefinition", None)
                if opp_val == self:
                    setattr(old_value, "OclContextDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclContextDefinition"):
                opp_val = getattr(value, "OclContextDefinition", None)
                setattr(value, "OclContextDefinition", self)

    @property
    def valueType(self):
        return self.__valueType

    @valueType.setter
    def valueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__valueType", None)
        self.__valueType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType"):
                opp_val = getattr(old_value, "MapType", None)
                if opp_val == self:
                    setattr(old_value, "MapType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType"):
                opp_val = getattr(value, "MapType", None)
                setattr(value, "MapType", self)

    @property
    def type168(self):
        return self.__type168

    @type168.setter
    def type168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclType__type168", None)
        self.__type168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TupleTypeAttribute"):
                opp_val = getattr(old_value, "TupleTypeAttribute", None)
                if opp_val == self:
                    setattr(old_value, "TupleTypeAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TupleTypeAttribute"):
                opp_val = getattr(value, "TupleTypeAttribute", None)
                setattr(value, "TupleTypeAttribute", self)

class OCL_IfExp(OclExpression):

    pass
class OCL_PropertyCallExp(OclExpression):

    pass
class OCL_PrimitiveExp(OclExpression):

    pass
class OCL_SuperExp(OclExpression):

    pass
class OCL_LetExp(OclExpression):

    pass
class OCL_TupleExp(OclExpression):

    pass
class Helper:

    pass
class Unit:

    pass
class ATL_Query(Unit):

    pass
class ATL_Module(Unit):

    def __init__(self, isRefining: str, ATL_Module: set["OclModel"] = None, ATL_Module7: set["OclModel"] = None, module: set["ModuleElement"] = None, Unit: "ATL_LibraryRef" = None):
        self.isRefining = isRefining
        self.ATL_Module = ATL_Module if ATL_Module is not None else set()
        self.ATL_Module7 = ATL_Module7 if ATL_Module7 is not None else set()
        self.module = module if module is not None else set()
        
        pass
    @property
    def isRefining(self):
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining


    @property
    def ATL_Module7(self):
        return self.__ATL_Module7

    @ATL_Module7.setter
    def ATL_Module7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Module__ATL_Module7", None)
        self.__ATL_Module7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel8"):
                    opp_val = getattr(item, "OclModel8", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel8"):
                    opp_val = getattr(item, "OclModel8", None)
                    
                    setattr(item, "OclModel8", self)
                    

    @property
    def ATL_Module(self):
        return self.__ATL_Module

    @ATL_Module.setter
    def ATL_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Module__ATL_Module", None)
        self.__ATL_Module = value if value is not None else set()
        
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
    def module(self):
        return self.__module

    @module.setter
    def module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Module__module", None)
        self.__module = value if value is not None else set()
        
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
                    

class ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class LocatedElement:

    pass
class ATL_ActionBlock(LocatedElement):

    pass
class ATL_InPattern(LocatedElement):

    pass
class OCL_MapElement(LocatedElement):

    pass
class OCL_OclFeatureDefinition(LocatedElement):

    pass
class ATL_Binding(LocatedElement):

    def __init__(self, propertyName: str, isAssignment: str, ATL_Binding: "OclExpression" = None, bindings: "OutPatternElement" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.ATL_Binding = ATL_Binding
        self.bindings = bindings
        
        pass
    @property
    def propertyName(self):
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName


    @property
    def isAssignment(self):
        return self.__isAssignment

    @isAssignment.setter
    def isAssignment(self, isAssignment: str):
        self.__isAssignment = isAssignment


    @property
    def bindings(self):
        return self.__bindings

    @bindings.setter
    def bindings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Binding__bindings", None)
        self.__bindings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutPatternElement59"):
                opp_val = getattr(old_value, "OutPatternElement59", None)
                if opp_val == self:
                    setattr(old_value, "OutPatternElement59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutPatternElement59"):
                opp_val = getattr(value, "OutPatternElement59", None)
                setattr(value, "OutPatternElement59", self)

    @property
    def ATL_Binding(self):
        return self.__ATL_Binding

    @ATL_Binding.setter
    def ATL_Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Binding__ATL_Binding", None)
        self.__ATL_Binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression57"):
                opp_val = getattr(old_value, "OclExpression57", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression57"):
                opp_val = getattr(value, "OclExpression57", None)
                setattr(value, "OclExpression57", self)

class ATL_Statement(LocatedElement):

    pass
class OCL_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, result: "IterateExp" = None, referredVariable: set["VariableExp"] = None, variableDeclaration: "OclType" = None, initializedVariable: "OclExpression" = None, variable: "LetExp" = None):
        self.id = id
        self.varName = varName
        self.result = result
        self.referredVariable = referredVariable if referredVariable is not None else set()
        self.variableDeclaration = variableDeclaration
        self.initializedVariable = initializedVariable
        self.variable = variable
        
        pass
    @property
    def varName(self):
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def referredVariable(self):
        return self.__referredVariable

    @referredVariable.setter
    def referredVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__referredVariable", None)
        self.__referredVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableExp"):
                    opp_val = getattr(item, "VariableExp", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableExp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableExp"):
                    opp_val = getattr(item, "VariableExp", None)
                    
                    setattr(item, "VariableExp", self)
                    

    @property
    def variableDeclaration(self):
        return self.__variableDeclaration

    @variableDeclaration.setter
    def variableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType142"):
                opp_val = getattr(old_value, "OclType142", None)
                if opp_val == self:
                    setattr(old_value, "OclType142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType142"):
                opp_val = getattr(value, "OclType142", None)
                setattr(value, "OclType142", self)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__result", None)
        self.__result = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IterateExp"):
                opp_val = getattr(old_value, "IterateExp", None)
                if opp_val == self:
                    setattr(old_value, "IterateExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IterateExp"):
                opp_val = getattr(value, "IterateExp", None)
                setattr(value, "IterateExp", self)

    @property
    def initializedVariable(self):
        return self.__initializedVariable

    @initializedVariable.setter
    def initializedVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__initializedVariable", None)
        self.__initializedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression144"):
                opp_val = getattr(old_value, "OclExpression144", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression144"):
                opp_val = getattr(value, "OclExpression144", None)
                setattr(value, "OclExpression144", self)

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_VariableDeclaration__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp146"):
                opp_val = getattr(old_value, "LetExp146", None)
                if opp_val == self:
                    setattr(old_value, "LetExp146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp146"):
                opp_val = getattr(value, "LetExp146", None)
                setattr(value, "LetExp146", self)

class OCL_OclFeature(LocatedElement):

    pass
class ATL_OutPattern(LocatedElement):

    pass
class OCL_TupleTypeAttribute(LocatedElement):

    def __init__(self, name: str, tupleTypeAttribute: "OclType" = None, attributes: "TupleType" = None):
        self.name = name
        self.tupleTypeAttribute = tupleTypeAttribute
        self.attributes = attributes
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def tupleTypeAttribute(self):
        return self.__tupleTypeAttribute

    @tupleTypeAttribute.setter
    def tupleTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__tupleTypeAttribute", None)
        self.__tupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType175"):
                opp_val = getattr(old_value, "OclType175", None)
                if opp_val == self:
                    setattr(old_value, "OclType175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType175"):
                opp_val = getattr(value, "OclType175", None)
                setattr(value, "OclType175", self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_TupleTypeAttribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TupleType"):
                opp_val = getattr(old_value, "TupleType", None)
                if opp_val == self:
                    setattr(old_value, "TupleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TupleType"):
                opp_val = getattr(value, "TupleType", None)
                setattr(value, "TupleType", self)

class ATL_ModuleElement(LocatedElement):

    pass
class OCL_OclModel(LocatedElement):

    def __init__(self, name: str, model: "OclModel" = None, model209: set["OclModelElement"] = None, metamodel: set["OclModel"] = None):
        self.name = name
        self.model = model
        self.model209 = model209 if model209 is not None else set()
        self.metamodel = metamodel if metamodel is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__model", None)
        self.__model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclModel207"):
                opp_val = getattr(old_value, "OclModel207", None)
                if opp_val == self:
                    setattr(old_value, "OclModel207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclModel207"):
                opp_val = getattr(value, "OclModel207", None)
                setattr(value, "OclModel207", self)

    @property
    def metamodel(self):
        return self.__metamodel

    @metamodel.setter
    def metamodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__metamodel", None)
        self.__metamodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModel211"):
                    opp_val = getattr(item, "OclModel211", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModel211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModel211"):
                    opp_val = getattr(item, "OclModel211", None)
                    
                    setattr(item, "OclModel211", self)
                    

    @property
    def model209(self):
        return self.__model209

    @model209.setter
    def model209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OCL_OclModel__model209", None)
        self.__model209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclModelElement"):
                    opp_val = getattr(item, "OclModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "OclModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclModelElement"):
                    opp_val = getattr(item, "OclModelElement", None)
                    
                    setattr(item, "OclModelElement", self)
                    

class OCL_OclExpression(LocatedElement):

    pass
class OCL_OclContextDefinition(LocatedElement):

    pass
class ATL_LibraryRef(LocatedElement):

    def __init__(self, name: str, libraries: "Unit" = None):
        self.name = name
        self.libraries = libraries
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def libraries(self):
        return self.__libraries

    @libraries.setter
    def libraries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_LibraryRef__libraries", None)
        self.__libraries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Unit"):
                opp_val = getattr(old_value, "Unit", None)
                if opp_val == self:
                    setattr(old_value, "Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Unit"):
                opp_val = getattr(value, "Unit", None)
                setattr(value, "Unit", self)

class ATL_Unit(LocatedElement):

    def __init__(self, name: str, unit: set["LibraryRef"] = None):
        self.name = name
        self.unit = unit if unit is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATL_Unit__unit", None)
        self.__unit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LibraryRef"):
                    opp_val = getattr(item, "LibraryRef", None)
                    
                    if opp_val == self:
                        setattr(item, "LibraryRef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LibraryRef"):
                    opp_val = getattr(item, "LibraryRef", None)
                    
                    setattr(item, "LibraryRef", self)
                    

class ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore


    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter


class OutPattern:

    pass