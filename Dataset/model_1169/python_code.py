from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OclModelElement:

    pass
class OclFeature:

    pass
class TupleType:

    pass
class atlstatic_OCL_Operation(OclFeature):

    def __init__(self, name: str, atlstatic_OCL_Operation: set["Parameter"] = None, operation: "OclType" = None, owningOperation: "OclExpression" = None, OclFeature: "atlstatic_OCL_OclFeatureDefinition" = None):
        self.name = name
        self.atlstatic_OCL_Operation = atlstatic_OCL_Operation if atlstatic_OCL_Operation is not None else set()
        self.operation = operation
        self.owningOperation = owningOperation
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Operation__operation", None)
        self.__operation = value
        
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
        old_value = getattr(self, f"_atlstatic_OCL_Operation__owningOperation", None)
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
                if hasattr(item, "Parameter201"):
                    opp_val = getattr(item, "Parameter201", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter201"):
                    opp_val = getattr(item, "Parameter201", None)
                    
                    setattr(item, "Parameter201", self)
                    

class atlstatic_OCL_Attribute(OclFeature):

    def __init__(self, name: str, owningAttribute: "OclExpression" = None, attribute: "OclType" = None, OclFeature: "atlstatic_OCL_OclFeatureDefinition" = None):
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
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType199"):
                opp_val = getattr(old_value, "OclType199", None)
                if opp_val == self:
                    setattr(old_value, "OclType199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType199"):
                opp_val = getattr(value, "OclType199", None)
                setattr(value, "OclType199", self)

    @property
    def owningAttribute(self):
        return self.__owningAttribute

    @owningAttribute.setter
    def owningAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_Attribute__owningAttribute", None)
        self.__owningAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression197"):
                opp_val = getattr(old_value, "OclExpression197", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression197"):
                opp_val = getattr(value, "OclExpression197", None)
                setattr(value, "OclExpression197", self)

class CollectionType:

    pass
class atlstatic_OCL_SequenceType(CollectionType):

    pass
class atlstatic_OCL_SetType(CollectionType):

    pass
class MapType:

    pass
class OclContextDefinition:

    pass
class VariableExp:

    pass
class IterateExp:

    pass
class atlstatic_OCL_OrderedSetType(CollectionType):

    pass
class atlstatic_OCL_BagType(CollectionType):

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
class TupleTypeAttribute:

    pass
class NumericExp:

    pass
class atlstatic_OCL_IntegerExp(NumericExp):

    def __init__(self, integerSymbol: str):
        self.integerSymbol = integerSymbol
        
        pass
    @property
    def integerSymbol(self):
        return self.__integerSymbol

    @integerSymbol.setter
    def integerSymbol(self, integerSymbol: str):
        self.__integerSymbol = integerSymbol


class atlstatic_OCL_RealExp(NumericExp):

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
class atlstatic_OCL_BooleanExp(PrimitiveExp):

    def __init__(self, booleanSymbol: str):
        self.booleanSymbol = booleanSymbol
        
        pass
    @property
    def booleanSymbol(self):
        return self.__booleanSymbol

    @booleanSymbol.setter
    def booleanSymbol(self, booleanSymbol: str):
        self.__booleanSymbol = booleanSymbol


class atlstatic_OCL_NumericExp(PrimitiveExp):

    pass
class atlstatic_OCL_StringExp(PrimitiveExp):

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
class MapElement:

    pass
class TupleExp:

    pass
class TuplePart:

    pass
class IfExp:

    pass
class OclType:

    pass
class atlstatic_OCL_OclAnyType(OclType):

    pass
class atlstatic_OCL_Primitive(OclType):

    pass
class atlstatic_OCL_MapType(OclType):

    pass
class atlstatic_OCL_CollectionType(OclType):

    pass
class atlstatic_OCL_OclModelElement(OclType):

    pass
class atlstatic_OCL_TupleType(OclType):

    pass
class OperationCallExp:

    pass
class atlstatic_OCL_OperatorCallExp(OperationCallExp):

    pass
class atlstatic_OCL_CollectionOperationCallExp(OperationCallExp):

    pass
class LoopExp:

    pass
class atlstatic_OCL_IteratorExp(LoopExp):

    def __init__(self, name: str, LoopExp153: "atlstatic_OCL_Iterator" = None, LoopExp: "atlstatic_OCL_OclExpression" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atlstatic_OCL_IterateExp(LoopExp):

    pass
class LetExp:

    pass
class CollectionExp:

    pass
class atlstatic_OCL_BagExp(CollectionExp):

    pass
class atlstatic_OCL_OrderedSetExp(CollectionExp):

    pass
class atlstatic_OCL_SequenceExp(CollectionExp):

    pass
class atlstatic_OCL_SetExp(CollectionExp):

    pass
class PropertyCallExp:

    pass
class atlstatic_OCL_OperationCallExp(PropertyCallExp):

    def __init__(self, operationName: str, parentOperation: set["OclExpression"] = None, PropertyCallExp: "atlstatic_OCL_OclExpression" = None):
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
        old_value = getattr(self, f"_atlstatic_OCL_OperationCallExp__parentOperation", None)
        self.__parentOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclExpression126"):
                    opp_val = getattr(item, "OclExpression126", None)
                    
                    if opp_val == self:
                        setattr(item, "OclExpression126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclExpression126"):
                    opp_val = getattr(item, "OclExpression126", None)
                    
                    setattr(item, "OclExpression126", self)
                    

class atlstatic_OCL_NavigationOrAttributeCallExp(PropertyCallExp):

    def __init__(self, name: str, PropertyCallExp: "atlstatic_OCL_OclExpression" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atlstatic_OCL_LoopExp(PropertyCallExp):

    pass
class Iterator:

    pass
class Binding:

    pass
class PatternElement:

    pass
class atlstatic_ATL_OutPatternElement(PatternElement):

    pass
class Statement:

    pass
class atlstatic_ATL_ForStat(Statement):

    pass
class atlstatic_ATL_ExpressionStat(Statement):

    pass
class atlstatic_ATL_IfStat(Statement):

    pass
class atlstatic_ATL_BindingStat(Statement):

    def __init__(self, propertyName: str, isAssignment: str, atlstatic_ATL_BindingStat: "OclExpression" = None, atlstatic_ATL_BindingStat74: "OclExpression" = None, Statement83: "atlstatic_ATL_IfStat" = None, Statement80: "atlstatic_ATL_IfStat" = None, Statement91: "atlstatic_ATL_ForStat" = None, Statement: "atlstatic_ATL_ActionBlock" = None):
        self.propertyName = propertyName
        self.isAssignment = isAssignment
        self.atlstatic_ATL_BindingStat = atlstatic_ATL_BindingStat
        self.atlstatic_ATL_BindingStat74 = atlstatic_ATL_BindingStat74
        
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
    def atlstatic_ATL_BindingStat74(self):
        return self.__atlstatic_ATL_BindingStat74

    @atlstatic_ATL_BindingStat74.setter
    def atlstatic_ATL_BindingStat74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_BindingStat__atlstatic_ATL_BindingStat74", None)
        self.__atlstatic_ATL_BindingStat74 = value
        
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
            if hasattr(old_value, "OclExpression72"):
                opp_val = getattr(old_value, "OclExpression72", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression72"):
                opp_val = getattr(value, "OclExpression72", None)
                setattr(value, "OclExpression72", self)

class InPatternElement:

    pass
class atlstatic_ATL_SimpleInPatternElement(InPatternElement):

    pass
class Parameter:

    pass
class MatchedRule:

    pass
class atlstatic_ATL_LazyMatchedRule(MatchedRule):

    def __init__(self, isUnique: str, MatchedRule29: "atlstatic_ATL_InPattern" = None, MatchedRule24: "atlstatic_ATL_MatchedRule" = None, MatchedRule: "atlstatic_ATL_MatchedRule" = None):
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
class atlstatic_ATL_CalledRule(Rule):

    def __init__(self, isEntrypoint: str, isEndpoint: str, atlstatic_ATL_CalledRule: set["Parameter"] = None, Rule67: "atlstatic_ATL_ActionBlock" = None, Rule64: "atlstatic_ATL_RuleVariableDeclaration" = None, Rule: "atlstatic_ATL_OutPattern" = None):
        self.isEntrypoint = isEntrypoint
        self.isEndpoint = isEndpoint
        self.atlstatic_ATL_CalledRule = atlstatic_ATL_CalledRule if atlstatic_ATL_CalledRule is not None else set()
        
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
                    

class atlstatic_ATL_MatchedRule(Rule):

    def __init__(self, isAbstract: str, isRefining: str, isNoDefault: str, rule21: "InPattern" = None, superRule: set["MatchedRule"] = None, children: "MatchedRule" = None, Rule67: "atlstatic_ATL_ActionBlock" = None, Rule64: "atlstatic_ATL_RuleVariableDeclaration" = None, Rule: "atlstatic_ATL_OutPattern" = None):
        self.isAbstract = isAbstract
        self.isRefining = isRefining
        self.isNoDefault = isNoDefault
        self.rule21 = rule21
        self.superRule = superRule if superRule is not None else set()
        self.children = children
        
        pass
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
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_MatchedRule__children", None)
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
    def rule21(self):
        return self.__rule21

    @rule21.setter
    def rule21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_MatchedRule__rule21", None)
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

    @property
    def superRule(self):
        return self.__superRule

    @superRule.setter
    def superRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_MatchedRule__superRule", None)
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
                    

class RuleVariableDeclaration:

    pass
class ActionBlock:

    pass
class OutPattern:

    pass
class atlstatic_ATL_InPatternElement(PatternElement):

    pass
class VariableDeclaration:

    pass
class atlstatic_ATL_RuleVariableDeclaration(VariableDeclaration):

    pass
class atlstatic_OCL_Parameter(VariableDeclaration):

    pass
class atlstatic_OCL_Iterator(VariableDeclaration):

    pass
class atlstatic_OCL_TuplePart(VariableDeclaration):

    pass
class atlstatic_ATL_PatternElement(VariableDeclaration):

    pass
class OutPatternElement:

    pass
class atlstatic_ATL_ForEachOutPatternElement(OutPatternElement):

    pass
class atlstatic_ATL_SimpleOutPatternElement(OutPatternElement):

    pass
class DropPattern:

    pass
class OclModel:

    pass
class OclExpression:

    pass
class atlstatic_OCL_VariableExp(OclExpression):

    pass
class atlstatic_OCL_OclType(OclExpression):

    def __init__(self, name: str, returnType: "Operation" = None, valueType: "MapType" = None, type163: "Attribute" = None, keyType: "MapType" = None, elementType: "CollectionType" = None, type169: "TupleTypeAttribute" = None, type171: "VariableDeclaration" = None, context_: "OclContextDefinition" = None, type: "OclExpression" = None, OclExpression77: "atlstatic_ATL_IfStat" = None, OclExpression75: "atlstatic_ATL_BindingStat" = None, OclExpression31: "atlstatic_ATL_InPattern" = None, OclExpression137: "atlstatic_OCL_LetExp" = None, OclExpression88: "atlstatic_ATL_ForStat" = None, OclExpression139: "atlstatic_OCL_IfExp" = None, OclExpression126: "atlstatic_OCL_OperationCallExp" = None, OclExpression128: "atlstatic_OCL_LoopExp" = None, OclExpression122: "atlstatic_OCL_MapElement" = None, OclExpression70: "atlstatic_ATL_ExpressionStat" = None, OclExpression60: "atlstatic_ATL_Binding" = None, OclExpression112: "atlstatic_OCL_CollectionExp" = None, OclExpression143: "atlstatic_OCL_IfExp" = None, OclExpression124: "atlstatic_OCL_PropertyCallExp" = None, OclExpression: "atlstatic_ATL_Query" = None, OclExpression141: "atlstatic_OCL_IfExp" = None, OclExpression119: "atlstatic_OCL_MapElement" = None, OclExpression72: "atlstatic_ATL_BindingStat" = None, OclExpression197: "atlstatic_OCL_Attribute" = None, OclExpression54: "atlstatic_ATL_SimpleOutPatternElement" = None, OclExpression56: "atlstatic_ATL_ForEachOutPatternElement" = None, OclExpression147: "atlstatic_OCL_VariableDeclaration" = None, OclExpression205: "atlstatic_OCL_Operation" = None, OclExpression158: "atlstatic_OCL_OclType" = None):
        self.name = name
        self.returnType = returnType
        self.valueType = valueType
        self.type163 = type163
        self.keyType = keyType
        self.elementType = elementType
        self.type169 = type169
        self.type171 = type171
        self.context_ = context_
        self.type = type
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type163(self):
        return self.__type163

    @type163.setter
    def type163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__type163", None)
        self.__type163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute164"):
                opp_val = getattr(old_value, "Attribute164", None)
                if opp_val == self:
                    setattr(old_value, "Attribute164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute164"):
                opp_val = getattr(value, "Attribute164", None)
                setattr(value, "Attribute164", self)

    @property
    def type171(self):
        return self.__type171

    @type171.setter
    def type171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__type171", None)
        self.__type171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariableDeclaration172"):
                opp_val = getattr(old_value, "VariableDeclaration172", None)
                if opp_val == self:
                    setattr(old_value, "VariableDeclaration172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariableDeclaration172"):
                opp_val = getattr(value, "VariableDeclaration172", None)
                setattr(value, "VariableDeclaration172", self)

    @property
    def context_(self):
        return self.__context_

    @context_.setter
    def context_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__context_", None)
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
    def returnType(self):
        return self.__returnType

    @returnType.setter
    def returnType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__returnType", None)
        self.__returnType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation160"):
                opp_val = getattr(old_value, "Operation160", None)
                if opp_val == self:
                    setattr(old_value, "Operation160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation160"):
                opp_val = getattr(value, "Operation160", None)
                setattr(value, "Operation160", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__type", None)
        self.__type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression158"):
                opp_val = getattr(old_value, "OclExpression158", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression158"):
                opp_val = getattr(value, "OclExpression158", None)
                setattr(value, "OclExpression158", self)

    @property
    def keyType(self):
        return self.__keyType

    @keyType.setter
    def keyType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__keyType", None)
        self.__keyType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MapType166"):
                opp_val = getattr(old_value, "MapType166", None)
                if opp_val == self:
                    setattr(old_value, "MapType166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MapType166"):
                opp_val = getattr(value, "MapType166", None)
                setattr(value, "MapType166", self)

    @property
    def valueType(self):
        return self.__valueType

    @valueType.setter
    def valueType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__valueType", None)
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
    def type169(self):
        return self.__type169

    @type169.setter
    def type169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__type169", None)
        self.__type169 = value
        
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

    @property
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_OclType__elementType", None)
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

class atlstatic_OCL_TupleExp(OclExpression):

    pass
class atlstatic_OCL_MapExp(OclExpression):

    pass
class atlstatic_OCL_CollectionExp(OclExpression):

    pass
class atlstatic_OCL_EnumLiteralExp(OclExpression):

    def __init__(self, name: str, OclExpression77: "atlstatic_ATL_IfStat" = None, OclExpression75: "atlstatic_ATL_BindingStat" = None, OclExpression31: "atlstatic_ATL_InPattern" = None, OclExpression137: "atlstatic_OCL_LetExp" = None, OclExpression88: "atlstatic_ATL_ForStat" = None, OclExpression139: "atlstatic_OCL_IfExp" = None, OclExpression126: "atlstatic_OCL_OperationCallExp" = None, OclExpression128: "atlstatic_OCL_LoopExp" = None, OclExpression122: "atlstatic_OCL_MapElement" = None, OclExpression70: "atlstatic_ATL_ExpressionStat" = None, OclExpression60: "atlstatic_ATL_Binding" = None, OclExpression112: "atlstatic_OCL_CollectionExp" = None, OclExpression143: "atlstatic_OCL_IfExp" = None, OclExpression124: "atlstatic_OCL_PropertyCallExp" = None, OclExpression: "atlstatic_ATL_Query" = None, OclExpression141: "atlstatic_OCL_IfExp" = None, OclExpression119: "atlstatic_OCL_MapElement" = None, OclExpression72: "atlstatic_ATL_BindingStat" = None, OclExpression197: "atlstatic_OCL_Attribute" = None, OclExpression54: "atlstatic_ATL_SimpleOutPatternElement" = None, OclExpression56: "atlstatic_ATL_ForEachOutPatternElement" = None, OclExpression147: "atlstatic_OCL_VariableDeclaration" = None, OclExpression205: "atlstatic_OCL_Operation" = None, OclExpression158: "atlstatic_OCL_OclType" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class atlstatic_OCL_PropertyCallExp(OclExpression):

    pass
class atlstatic_OCL_PrimitiveExp(OclExpression):

    pass
class atlstatic_OCL_IfExp(OclExpression):

    pass
class atlstatic_OCL_LetExp(OclExpression):

    pass
class atlstatic_OCL_OclUndefinedExp(OclExpression):

    pass
class atlstatic_OCL_SuperExp(OclExpression):

    pass
class Helper:

    pass
class Unit:

    pass
class atlstatic_ATL_Query(Unit):

    pass
class atlstatic_ATL_Module(Unit):

    def __init__(self, isRefining: str, atlstatic_ATL_Module7: set["OclModel"] = None, atlstatic_ATL_Module10: set["ModuleElement"] = None, atlstatic_ATL_Module: set["OclModel"] = None, Unit: "atlstatic_ATL_LibraryRef" = None):
        self.isRefining = isRefining
        self.atlstatic_ATL_Module7 = atlstatic_ATL_Module7 if atlstatic_ATL_Module7 is not None else set()
        self.atlstatic_ATL_Module10 = atlstatic_ATL_Module10 if atlstatic_ATL_Module10 is not None else set()
        self.atlstatic_ATL_Module = atlstatic_ATL_Module if atlstatic_ATL_Module is not None else set()
        
        pass
    @property
    def isRefining(self):
        return self.__isRefining

    @isRefining.setter
    def isRefining(self, isRefining: str):
        self.__isRefining = isRefining


    @property
    def atlstatic_ATL_Module10(self):
        return self.__atlstatic_ATL_Module10

    @atlstatic_ATL_Module10.setter
    def atlstatic_ATL_Module10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Module__atlstatic_ATL_Module10", None)
        self.__atlstatic_ATL_Module10 = value if value is not None else set()
        
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
    def atlstatic_ATL_Module7(self):
        return self.__atlstatic_ATL_Module7

    @atlstatic_ATL_Module7.setter
    def atlstatic_ATL_Module7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Module__atlstatic_ATL_Module7", None)
        self.__atlstatic_ATL_Module7 = value if value is not None else set()
        
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
                    

class atlstatic_ATL_Library(Unit):

    pass
class LibraryRef:

    pass
class LocatedElement:

    pass
class atlstatic_OCL_TupleTypeAttribute(LocatedElement):

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
        old_value = getattr(self, f"_atlstatic_OCL_TupleTypeAttribute__tupleTypeAttribute", None)
        self.__tupleTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType176"):
                opp_val = getattr(old_value, "OclType176", None)
                if opp_val == self:
                    setattr(old_value, "OclType176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType176"):
                opp_val = getattr(value, "OclType176", None)
                setattr(value, "OclType176", self)

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_TupleTypeAttribute__attributes", None)
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

class atlstatic_ATL_ActionBlock(LocatedElement):

    pass
class atlstatic_OCL_OclFeature(LocatedElement):

    pass
class atlstatic_ATL_DropPattern(LocatedElement):

    pass
class atlstatic_OCL_OclContextDefinition(LocatedElement):

    pass
class atlstatic_ATL_InPattern(LocatedElement):

    pass
class atlstatic_ATL_Binding(LocatedElement):

    def __init__(self, isAssignment: str, propertyName: str, atlstatic_ATL_Binding: "OclExpression" = None, bindings: "OutPatternElement" = None):
        self.isAssignment = isAssignment
        self.propertyName = propertyName
        self.atlstatic_ATL_Binding = atlstatic_ATL_Binding
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
        old_value = getattr(self, f"_atlstatic_ATL_Binding__bindings", None)
        self.__bindings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutPatternElement62"):
                opp_val = getattr(old_value, "OutPatternElement62", None)
                if opp_val == self:
                    setattr(old_value, "OutPatternElement62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutPatternElement62"):
                opp_val = getattr(value, "OutPatternElement62", None)
                setattr(value, "OutPatternElement62", self)

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
            if hasattr(old_value, "OclExpression60"):
                opp_val = getattr(old_value, "OclExpression60", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression60"):
                opp_val = getattr(value, "OclExpression60", None)
                setattr(value, "OclExpression60", self)

class atlstatic_ATL_OutPattern(LocatedElement):

    pass
class atlstatic_OCL_VariableDeclaration(LocatedElement):

    def __init__(self, id: str, varName: str, variableDeclaration: "OclType" = None, initializedVariable: "OclExpression" = None, variable: "LetExp" = None, result: "IterateExp" = None, referredVariable: set["VariableExp"] = None):
        self.id = id
        self.varName = varName
        self.variableDeclaration = variableDeclaration
        self.initializedVariable = initializedVariable
        self.variable = variable
        self.result = result
        self.referredVariable = referredVariable if referredVariable is not None else set()
        
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
    def variableDeclaration(self):
        return self.__variableDeclaration

    @variableDeclaration.setter
    def variableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__variableDeclaration", None)
        self.__variableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclType145"):
                opp_val = getattr(old_value, "OclType145", None)
                if opp_val == self:
                    setattr(old_value, "OclType145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclType145"):
                opp_val = getattr(value, "OclType145", None)
                setattr(value, "OclType145", self)

    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__variable", None)
        self.__variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LetExp149"):
                opp_val = getattr(old_value, "LetExp149", None)
                if opp_val == self:
                    setattr(old_value, "LetExp149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LetExp149"):
                opp_val = getattr(value, "LetExp149", None)
                setattr(value, "LetExp149", self)

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__result", None)
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
    def referredVariable(self):
        return self.__referredVariable

    @referredVariable.setter
    def referredVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__referredVariable", None)
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
    def initializedVariable(self):
        return self.__initializedVariable

    @initializedVariable.setter
    def initializedVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_OCL_VariableDeclaration__initializedVariable", None)
        self.__initializedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclExpression147"):
                opp_val = getattr(old_value, "OclExpression147", None)
                if opp_val == self:
                    setattr(old_value, "OclExpression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclExpression147"):
                opp_val = getattr(value, "OclExpression147", None)
                setattr(value, "OclExpression147", self)

class atlstatic_OCL_MapElement(LocatedElement):

    pass
class atlstatic_OCL_OclFeatureDefinition(LocatedElement):

    pass
class atlstatic_ATL_LibraryRef(LocatedElement):

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
        old_value = getattr(self, f"_atlstatic_ATL_LibraryRef__libraries", None)
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

class atlstatic_ATL_Statement(LocatedElement):

    pass
class atlstatic_OCL_OclExpression(LocatedElement):

    pass
class atlstatic_OCL_OclModel(LocatedElement):

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
        old_value = getattr(self, f"_atlstatic_OCL_OclModel__model", None)
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
        old_value = getattr(self, f"_atlstatic_OCL_OclModel__metamodel", None)
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
        old_value = getattr(self, f"_atlstatic_OCL_OclModel__model209", None)
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
                    

class atlstatic_ATL_Unit(LocatedElement):

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
        old_value = getattr(self, f"_atlstatic_ATL_Unit__unit", None)
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
                    

class atlstatic_ATL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
        pass
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


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class OclFeatureDefinition:

    pass
class Library:

    pass
class Query:

    pass
class atlstatic_ATL_ModuleElement(LocatedElement):

    pass
class ModuleElement:

    pass
class atlstatic_ATL_Rule(ModuleElement):

    def __init__(self, name: str, rule: "OutPattern" = None, rule17: "ActionBlock" = None, rule19: set["RuleVariableDeclaration"] = None, ModuleElement: "atlstatic_ATL_Module" = None):
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
    def rule19(self):
        return self.__rule19

    @rule19.setter
    def rule19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Rule__rule19", None)
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
                    

    @property
    def rule17(self):
        return self.__rule17

    @rule17.setter
    def rule17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Rule__rule17", None)
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
    def rule(self):
        return self.__rule

    @rule.setter
    def rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_atlstatic_ATL_Rule__rule", None)
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

class atlstatic_ATL_Helper(ModuleElement):

    pass