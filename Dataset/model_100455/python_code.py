from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    complement = "complement"
class AdditiveOperator(Enum):
    plus = "plus"
    minus = "minus"
class TimeUnit(Enum):
    second = "second"
    millisecond = "millisecond"
    microsecond = "microsecond"
    nanosecond = "nanosecond"
class AssignmentOperator(Enum):
    orAssign = "orAssign"
    assign = "assign"
    multAssign = "multAssign"
    divAssign = "divAssign"
    modAssign = "modAssign"
    addAssign = "addAssign"
    subAssign = "subAssign"
    leftShiftAssign = "leftShiftAssign"
    rightShiftAssign = "rightShiftAssign"
    andAssign = "andAssign"
    xorAssign = "xorAssign"
class ShiftOperator(Enum):
    left = "left"
    right = "right"
class MultiplicativeOperator(Enum):
    mul = "mul"
    div = "div"
    mod = "mod"
class TimeEventType(Enum):
    after = "after"
    every = "every"
class Direction(Enum):
    LOCAL = "LOCAL"
    IN = "IN"
    OUT = "OUT"
class RelationalOperator(Enum):
    smaller = "smaller"
    smallerEqual = "smallerEqual"
    greater = "greater"
    greaterEqual = "greaterEqual"
    equals = "equals"
    notEquals = "notEquals"


############################################
# Definition of Classes
############################################

class BuiltinEventSpec:

    pass
class stext_ExitEvent(BuiltinEventSpec):

    pass
class stext_AlwaysEvent(BuiltinEventSpec):

    pass
class stext_EntryEvent(BuiltinEventSpec):

    pass
class EventSpec:

    pass
class stext_BuiltinEventSpec(EventSpec):

    pass
class stext_TimeEventSpec(EventSpec):

    def __init__(self, type: str, unit: str, stext_TimeEventSpec: "stext_Expression" = None):
        self.type = type
        self.unit = unit
        self.stext_TimeEventSpec = stext_TimeEventSpec
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def stext_TimeEventSpec(self):
        return self.__stext_TimeEventSpec

    @stext_TimeEventSpec.setter
    def stext_TimeEventSpec(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_TimeEventSpec__stext_TimeEventSpec", None)
        self.__stext_TimeEventSpec = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression14"):
                opp_val = getattr(old_value, "stext_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression14"):
                opp_val = getattr(value, "stext_Expression14", None)
                setattr(value, "stext_Expression14", self)

class stext_RegularEventSpec(EventSpec):

    pass
class stext_TransitionSpecification:

    pass
class stext_StateSpecification:

    pass
class DefRoot:

    pass
class stext_TransitionRoot(DefRoot):

    pass
class stext_StateRoot(DefRoot):

    pass
class stext_StatechartRoot(DefRoot):

    pass
class stext_DefRoot:

    pass
class stext_Root:

    pass
class Property:

    pass
class Variable:

    pass
class stext_VariableDefinition(Variable, Property):

    def __init__(self, readonly: bool, external: bool, stext_VariableDefinition: "stext_Expression" = None):
        self.readonly = readonly
        self.external = external
        self.stext_VariableDefinition = stext_VariableDefinition
        
        pass
    @property
    def external(self):
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external


    @property
    def readonly(self):
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly


    @property
    def stext_VariableDefinition(self):
        return self.__stext_VariableDefinition

    @stext_VariableDefinition.setter
    def stext_VariableDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_VariableDefinition__stext_VariableDefinition", None)
        self.__stext_VariableDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression"):
                opp_val = getattr(old_value, "stext_Expression", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression"):
                opp_val = getattr(value, "stext_Expression", None)
                setattr(value, "stext_Expression", self)

class Event:

    pass
class stext_EventDefinition(Event):

    def __init__(self, direction: str):
        self.direction = direction
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


class NamedElement:

    pass
class StatechartScope:

    pass
class stext_InternalScope(StatechartScope):

    pass
class stext_InterfaceScope(NamedElement, StatechartScope):

    pass
class Scope:

    pass
class stext_StatechartScope(Scope):

    pass
class stext_Scope:

    pass
class ScopedElement:

    pass
class stext_StatechartSpecification(ScopedElement):

    pass
class stext_EObject:

    pass
class stext_State:

    pass
class Expression:

    pass
class stext_NumericalUnaryExpression(Expression):

    def __init__(self, operator: str, stext_NumericalUnaryExpression: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalUnaryExpression = stext_NumericalUnaryExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalUnaryExpression(self):
        return self.__stext_NumericalUnaryExpression

    @stext_NumericalUnaryExpression.setter
    def stext_NumericalUnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalUnaryExpression__stext_NumericalUnaryExpression", None)
        self.__stext_NumericalUnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression87"):
                opp_val = getattr(old_value, "stext_Expression87", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression87"):
                opp_val = getattr(value, "stext_Expression87", None)
                setattr(value, "stext_Expression87", self)

class stext_BitwiseXorExpression(Expression):

    pass
class stext_FeatureCall(Expression):

    def __init__(self, operationCall: bool, stext_FeatureCall: "stext_Expression" = None, stext_FeatureCall92: "stext_EObject" = None, stext_FeatureCall94: set["stext_Expression"] = None):
        self.operationCall = operationCall
        self.stext_FeatureCall = stext_FeatureCall
        self.stext_FeatureCall92 = stext_FeatureCall92
        self.stext_FeatureCall94 = stext_FeatureCall94 if stext_FeatureCall94 is not None else set()
        
        pass
    @property
    def operationCall(self):
        return self.__operationCall

    @operationCall.setter
    def operationCall(self, operationCall: bool):
        self.__operationCall = operationCall


    @property
    def stext_FeatureCall92(self):
        return self.__stext_FeatureCall92

    @stext_FeatureCall92.setter
    def stext_FeatureCall92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_FeatureCall__stext_FeatureCall92", None)
        self.__stext_FeatureCall92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_EObject"):
                opp_val = getattr(old_value, "stext_EObject", None)
                if opp_val == self:
                    setattr(old_value, "stext_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_EObject"):
                opp_val = getattr(value, "stext_EObject", None)
                setattr(value, "stext_EObject", self)

    @property
    def stext_FeatureCall94(self):
        return self.__stext_FeatureCall94

    @stext_FeatureCall94.setter
    def stext_FeatureCall94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_FeatureCall__stext_FeatureCall94", None)
        self.__stext_FeatureCall94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stext_Expression95"):
                    opp_val = getattr(item, "stext_Expression95", None)
                    
                    if opp_val == self:
                        setattr(item, "stext_Expression95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stext_Expression95"):
                    opp_val = getattr(item, "stext_Expression95", None)
                    
                    setattr(item, "stext_Expression95", self)
                    

    @property
    def stext_FeatureCall(self):
        return self.__stext_FeatureCall

    @stext_FeatureCall.setter
    def stext_FeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_FeatureCall__stext_FeatureCall", None)
        self.__stext_FeatureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression90"):
                opp_val = getattr(old_value, "stext_Expression90", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression90"):
                opp_val = getattr(value, "stext_Expression90", None)
                setattr(value, "stext_Expression90", self)

class stext_ActiveStateReferenceExpression(Expression):

    pass
class stext_BitwiseAndExpression(Expression):

    pass
class stext_LogicalAndExpression(Expression):

    pass
class stext_EventValueReferenceExpression(Expression):

    pass
class stext_NumericalMultiplyDivideExpression(Expression):

    def __init__(self, operator: str, stext_NumericalMultiplyDivideExpression: "stext_Expression" = None, stext_NumericalMultiplyDivideExpression84: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalMultiplyDivideExpression = stext_NumericalMultiplyDivideExpression
        self.stext_NumericalMultiplyDivideExpression84 = stext_NumericalMultiplyDivideExpression84
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalMultiplyDivideExpression(self):
        return self.__stext_NumericalMultiplyDivideExpression

    @stext_NumericalMultiplyDivideExpression.setter
    def stext_NumericalMultiplyDivideExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalMultiplyDivideExpression__stext_NumericalMultiplyDivideExpression", None)
        self.__stext_NumericalMultiplyDivideExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression82"):
                opp_val = getattr(old_value, "stext_Expression82", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression82"):
                opp_val = getattr(value, "stext_Expression82", None)
                setattr(value, "stext_Expression82", self)

    @property
    def stext_NumericalMultiplyDivideExpression84(self):
        return self.__stext_NumericalMultiplyDivideExpression84

    @stext_NumericalMultiplyDivideExpression84.setter
    def stext_NumericalMultiplyDivideExpression84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalMultiplyDivideExpression__stext_NumericalMultiplyDivideExpression84", None)
        self.__stext_NumericalMultiplyDivideExpression84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression85"):
                opp_val = getattr(old_value, "stext_Expression85", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression85"):
                opp_val = getattr(value, "stext_Expression85", None)
                setattr(value, "stext_Expression85", self)

class stext_ParenthesizedExpression(Expression):

    pass
class stext_PrimitiveValueExpression(Expression):

    pass
class stext_LogicalRelationExpression(Expression):

    def __init__(self, operator: str, stext_LogicalRelationExpression69: "stext_Expression" = None, stext_LogicalRelationExpression: "stext_Expression" = None):
        self.operator = operator
        self.stext_LogicalRelationExpression69 = stext_LogicalRelationExpression69
        self.stext_LogicalRelationExpression = stext_LogicalRelationExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_LogicalRelationExpression69(self):
        return self.__stext_LogicalRelationExpression69

    @stext_LogicalRelationExpression69.setter
    def stext_LogicalRelationExpression69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_LogicalRelationExpression__stext_LogicalRelationExpression69", None)
        self.__stext_LogicalRelationExpression69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression70"):
                opp_val = getattr(old_value, "stext_Expression70", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression70"):
                opp_val = getattr(value, "stext_Expression70", None)
                setattr(value, "stext_Expression70", self)

    @property
    def stext_LogicalRelationExpression(self):
        return self.__stext_LogicalRelationExpression

    @stext_LogicalRelationExpression.setter
    def stext_LogicalRelationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_LogicalRelationExpression__stext_LogicalRelationExpression", None)
        self.__stext_LogicalRelationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression67"):
                opp_val = getattr(old_value, "stext_Expression67", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression67"):
                opp_val = getattr(value, "stext_Expression67", None)
                setattr(value, "stext_Expression67", self)

class stext_ElementReferenceExpression(Expression):

    def __init__(self, operationCall: bool, stext_ElementReferenceExpression: "stext_EObject" = None, stext_ElementReferenceExpression99: set["stext_Expression"] = None):
        self.operationCall = operationCall
        self.stext_ElementReferenceExpression = stext_ElementReferenceExpression
        self.stext_ElementReferenceExpression99 = stext_ElementReferenceExpression99 if stext_ElementReferenceExpression99 is not None else set()
        
        pass
    @property
    def operationCall(self):
        return self.__operationCall

    @operationCall.setter
    def operationCall(self, operationCall: bool):
        self.__operationCall = operationCall


    @property
    def stext_ElementReferenceExpression99(self):
        return self.__stext_ElementReferenceExpression99

    @stext_ElementReferenceExpression99.setter
    def stext_ElementReferenceExpression99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ElementReferenceExpression__stext_ElementReferenceExpression99", None)
        self.__stext_ElementReferenceExpression99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stext_Expression100"):
                    opp_val = getattr(item, "stext_Expression100", None)
                    
                    if opp_val == self:
                        setattr(item, "stext_Expression100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stext_Expression100"):
                    opp_val = getattr(item, "stext_Expression100", None)
                    
                    setattr(item, "stext_Expression100", self)
                    

    @property
    def stext_ElementReferenceExpression(self):
        return self.__stext_ElementReferenceExpression

    @stext_ElementReferenceExpression.setter
    def stext_ElementReferenceExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ElementReferenceExpression__stext_ElementReferenceExpression", None)
        self.__stext_ElementReferenceExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_EObject97"):
                opp_val = getattr(old_value, "stext_EObject97", None)
                if opp_val == self:
                    setattr(old_value, "stext_EObject97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_EObject97"):
                opp_val = getattr(value, "stext_EObject97", None)
                setattr(value, "stext_EObject97", self)

class stext_BitwiseOrExpression(Expression):

    pass
class stext_LogicalNotExpression(Expression):

    pass
class stext_NumericalAddSubtractExpression(Expression):

    def __init__(self, operator: str, stext_NumericalAddSubtractExpression: "stext_Expression" = None, stext_NumericalAddSubtractExpression79: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalAddSubtractExpression = stext_NumericalAddSubtractExpression
        self.stext_NumericalAddSubtractExpression79 = stext_NumericalAddSubtractExpression79
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalAddSubtractExpression79(self):
        return self.__stext_NumericalAddSubtractExpression79

    @stext_NumericalAddSubtractExpression79.setter
    def stext_NumericalAddSubtractExpression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalAddSubtractExpression__stext_NumericalAddSubtractExpression79", None)
        self.__stext_NumericalAddSubtractExpression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression80"):
                opp_val = getattr(old_value, "stext_Expression80", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression80"):
                opp_val = getattr(value, "stext_Expression80", None)
                setattr(value, "stext_Expression80", self)

    @property
    def stext_NumericalAddSubtractExpression(self):
        return self.__stext_NumericalAddSubtractExpression

    @stext_NumericalAddSubtractExpression.setter
    def stext_NumericalAddSubtractExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalAddSubtractExpression__stext_NumericalAddSubtractExpression", None)
        self.__stext_NumericalAddSubtractExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression77"):
                opp_val = getattr(old_value, "stext_Expression77", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression77"):
                opp_val = getattr(value, "stext_Expression77", None)
                setattr(value, "stext_Expression77", self)

class stext_ShiftExpression(Expression):

    def __init__(self, operator: str, stext_ShiftExpression: "stext_Expression" = None, stext_ShiftExpression74: "stext_Expression" = None):
        self.operator = operator
        self.stext_ShiftExpression = stext_ShiftExpression
        self.stext_ShiftExpression74 = stext_ShiftExpression74
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_ShiftExpression74(self):
        return self.__stext_ShiftExpression74

    @stext_ShiftExpression74.setter
    def stext_ShiftExpression74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ShiftExpression__stext_ShiftExpression74", None)
        self.__stext_ShiftExpression74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression75"):
                opp_val = getattr(old_value, "stext_Expression75", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression75"):
                opp_val = getattr(value, "stext_Expression75", None)
                setattr(value, "stext_Expression75", self)

    @property
    def stext_ShiftExpression(self):
        return self.__stext_ShiftExpression

    @stext_ShiftExpression.setter
    def stext_ShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ShiftExpression__stext_ShiftExpression", None)
        self.__stext_ShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression72"):
                opp_val = getattr(old_value, "stext_Expression72", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression72"):
                opp_val = getattr(value, "stext_Expression72", None)
                setattr(value, "stext_Expression72", self)

class stext_EventRaisingExpression(Expression):

    pass
class Effect:

    pass
class stext_ReactionEffect(Effect):

    pass
class Trigger:

    pass
class stext_DefaultTrigger(Trigger):

    pass
class stext_ReactionTrigger(Trigger):

    pass
class stext_SimpleScope(Scope):

    pass
class stext_LogicalOrExpression(Expression):

    pass
class stext_ConditionalExpression(Expression):

    pass
class stext_AssignmentExpression(Expression):

    def __init__(self, operator: str, stext_AssignmentExpression: "stext_Expression" = None, stext_AssignmentExpression29: "stext_Expression" = None):
        self.operator = operator
        self.stext_AssignmentExpression = stext_AssignmentExpression
        self.stext_AssignmentExpression29 = stext_AssignmentExpression29
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_AssignmentExpression(self):
        return self.__stext_AssignmentExpression

    @stext_AssignmentExpression.setter
    def stext_AssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_AssignmentExpression__stext_AssignmentExpression", None)
        self.__stext_AssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression27"):
                opp_val = getattr(old_value, "stext_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression27"):
                opp_val = getattr(value, "stext_Expression27", None)
                setattr(value, "stext_Expression27", self)

    @property
    def stext_AssignmentExpression29(self):
        return self.__stext_AssignmentExpression29

    @stext_AssignmentExpression29.setter
    def stext_AssignmentExpression29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_AssignmentExpression__stext_AssignmentExpression29", None)
        self.__stext_AssignmentExpression29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression30"):
                opp_val = getattr(old_value, "stext_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression30"):
                opp_val = getattr(value, "stext_Expression30", None)
                setattr(value, "stext_Expression30", self)

class stext_EventSpec:

    pass
class ReactionProperty:

    pass
class stext_ExitPointSpec(ReactionProperty):

    def __init__(self, exitpoint: str):
        self.exitpoint = exitpoint
        
        pass
    @property
    def exitpoint(self):
        return self.__exitpoint

    @exitpoint.setter
    def exitpoint(self, exitpoint: str):
        self.__exitpoint = exitpoint


class stext_EntryPointSpec(ReactionProperty):

    def __init__(self, entrypoint: str):
        self.entrypoint = entrypoint
        
        pass
    @property
    def entrypoint(self):
        return self.__entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint: str):
        self.__entrypoint = entrypoint


class stext_Guard:

    pass
class Reaction:

    pass
class stext_TransitionReaction(Reaction):

    pass
class Operation:

    pass
class Declaration:

    pass
class stext_LocalReaction(Declaration, Reaction):

    pass
class stext_OperationDefinition(Declaration, Operation):

    pass
class Literal:

    pass
class stext_RealLiteral(Literal):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class stext_IntLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class stext_StringLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class stext_HexLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class stext_BoolLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class stext_Literal:

    pass
class Statement:

    pass
class stext_Expression(Statement):

    pass