from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    complement = "complement"
class TimeEventType(Enum):
    after = "after"
    every = "every"
class MultiplicativeOperator(Enum):
    mul = "mul"
    div = "div"
    mod = "mod"
class AssignmentOperator(Enum):
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
    orAssign = "orAssign"
class AdditiveOperator(Enum):
    plus = "plus"
    minus = "minus"
class RelationalOperator(Enum):
    smaller = "smaller"
    smallerEqual = "smallerEqual"
    greater = "greater"
    greaterEqual = "greaterEqual"
    equals = "equals"
    notEquals = "notEquals"
class ShiftOperator(Enum):
    left = "left"
    right = "right"
class Direction(Enum):
    LOCAL = "LOCAL"
    IN = "IN"
    OUT = "OUT"
class TimeUnit(Enum):
    second = "second"
    millisecond = "millisecond"
    microsecond = "microsecond"
    nanosecond = "nanosecond"


############################################
# Definition of Classes
############################################

class stext_Root:

    pass
class ScopedElement:

    pass
class stext_TransitionSpecification:

    pass
class stext_State:

    pass
class stext_EObject:

    pass
class Expression:

    pass
class stext_BitwiseXorExpression(Expression):

    pass
class stext_ParenthesizedExpression(Expression):

    pass
class stext_ShiftExpression(Expression):

    def __init__(self, operator: str, stext_ShiftExpression: "stext_Expression" = None, stext_ShiftExpression72: "stext_Expression" = None):
        self.operator = operator
        self.stext_ShiftExpression = stext_ShiftExpression
        self.stext_ShiftExpression72 = stext_ShiftExpression72
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


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
    def stext_ShiftExpression72(self):
        return self.__stext_ShiftExpression72

    @stext_ShiftExpression72.setter
    def stext_ShiftExpression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ShiftExpression__stext_ShiftExpression72", None)
        self.__stext_ShiftExpression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression73"):
                opp_val = getattr(old_value, "stext_Expression73", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression73"):
                opp_val = getattr(value, "stext_Expression73", None)
                setattr(value, "stext_Expression73", self)

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
            if hasattr(old_value, "stext_Expression85"):
                opp_val = getattr(old_value, "stext_Expression85", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression85"):
                opp_val = getattr(value, "stext_Expression85", None)
                setattr(value, "stext_Expression85", self)

class stext_FeatureCall(Expression):

    def __init__(self, operationCall: bool, stext_FeatureCall92: set["stext_Expression"] = None, stext_FeatureCall: "stext_Expression" = None, stext_FeatureCall90: "stext_EObject" = None):
        self.operationCall = operationCall
        self.stext_FeatureCall92 = stext_FeatureCall92 if stext_FeatureCall92 is not None else set()
        self.stext_FeatureCall = stext_FeatureCall
        self.stext_FeatureCall90 = stext_FeatureCall90
        
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
        self.__stext_FeatureCall92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stext_Expression93"):
                    opp_val = getattr(item, "stext_Expression93", None)
                    
                    if opp_val == self:
                        setattr(item, "stext_Expression93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stext_Expression93"):
                    opp_val = getattr(item, "stext_Expression93", None)
                    
                    setattr(item, "stext_Expression93", self)
                    

    @property
    def stext_FeatureCall90(self):
        return self.__stext_FeatureCall90

    @stext_FeatureCall90.setter
    def stext_FeatureCall90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_FeatureCall__stext_FeatureCall90", None)
        self.__stext_FeatureCall90 = value
        
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
    def stext_FeatureCall(self):
        return self.__stext_FeatureCall

    @stext_FeatureCall.setter
    def stext_FeatureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_FeatureCall__stext_FeatureCall", None)
        self.__stext_FeatureCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression88"):
                opp_val = getattr(old_value, "stext_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression88"):
                opp_val = getattr(value, "stext_Expression88", None)
                setattr(value, "stext_Expression88", self)

class stext_NumericalMultiplyDivideExpression(Expression):

    def __init__(self, operator: str, stext_NumericalMultiplyDivideExpression82: "stext_Expression" = None, stext_NumericalMultiplyDivideExpression: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalMultiplyDivideExpression82 = stext_NumericalMultiplyDivideExpression82
        self.stext_NumericalMultiplyDivideExpression = stext_NumericalMultiplyDivideExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalMultiplyDivideExpression82(self):
        return self.__stext_NumericalMultiplyDivideExpression82

    @stext_NumericalMultiplyDivideExpression82.setter
    def stext_NumericalMultiplyDivideExpression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalMultiplyDivideExpression__stext_NumericalMultiplyDivideExpression82", None)
        self.__stext_NumericalMultiplyDivideExpression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression83"):
                opp_val = getattr(old_value, "stext_Expression83", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression83"):
                opp_val = getattr(value, "stext_Expression83", None)
                setattr(value, "stext_Expression83", self)

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
            if hasattr(old_value, "stext_Expression80"):
                opp_val = getattr(old_value, "stext_Expression80", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression80"):
                opp_val = getattr(value, "stext_Expression80", None)
                setattr(value, "stext_Expression80", self)

class stext_LogicalNotExpression(Expression):

    pass
class stext_NumericalAddSubtractExpression(Expression):

    def __init__(self, operator: str, stext_NumericalAddSubtractExpression: "stext_Expression" = None, stext_NumericalAddSubtractExpression77: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalAddSubtractExpression = stext_NumericalAddSubtractExpression
        self.stext_NumericalAddSubtractExpression77 = stext_NumericalAddSubtractExpression77
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalAddSubtractExpression77(self):
        return self.__stext_NumericalAddSubtractExpression77

    @stext_NumericalAddSubtractExpression77.setter
    def stext_NumericalAddSubtractExpression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalAddSubtractExpression__stext_NumericalAddSubtractExpression77", None)
        self.__stext_NumericalAddSubtractExpression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression78"):
                opp_val = getattr(old_value, "stext_Expression78", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression78"):
                opp_val = getattr(value, "stext_Expression78", None)
                setattr(value, "stext_Expression78", self)

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
            if hasattr(old_value, "stext_Expression75"):
                opp_val = getattr(old_value, "stext_Expression75", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression75"):
                opp_val = getattr(value, "stext_Expression75", None)
                setattr(value, "stext_Expression75", self)

class stext_AssignmentExpression(Expression):

    def __init__(self, operator: str, stext_AssignmentExpression: "stext_Expression" = None, stext_AssignmentExpression27: "stext_Expression" = None):
        self.operator = operator
        self.stext_AssignmentExpression = stext_AssignmentExpression
        self.stext_AssignmentExpression27 = stext_AssignmentExpression27
        
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
            if hasattr(old_value, "stext_Expression25"):
                opp_val = getattr(old_value, "stext_Expression25", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression25"):
                opp_val = getattr(value, "stext_Expression25", None)
                setattr(value, "stext_Expression25", self)

    @property
    def stext_AssignmentExpression27(self):
        return self.__stext_AssignmentExpression27

    @stext_AssignmentExpression27.setter
    def stext_AssignmentExpression27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_AssignmentExpression__stext_AssignmentExpression27", None)
        self.__stext_AssignmentExpression27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression28"):
                opp_val = getattr(old_value, "stext_Expression28", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression28"):
                opp_val = getattr(value, "stext_Expression28", None)
                setattr(value, "stext_Expression28", self)

class stext_BitwiseAndExpression(Expression):

    pass
class stext_ConditionalExpression(Expression):

    pass
class stext_ActiveStateReferenceExpression(Expression):

    pass
class stext_LogicalRelationExpression(Expression):

    def __init__(self, operator: str, stext_LogicalRelationExpression: "stext_Expression" = None, stext_LogicalRelationExpression67: "stext_Expression" = None):
        self.operator = operator
        self.stext_LogicalRelationExpression = stext_LogicalRelationExpression
        self.stext_LogicalRelationExpression67 = stext_LogicalRelationExpression67
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_LogicalRelationExpression67(self):
        return self.__stext_LogicalRelationExpression67

    @stext_LogicalRelationExpression67.setter
    def stext_LogicalRelationExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_LogicalRelationExpression__stext_LogicalRelationExpression67", None)
        self.__stext_LogicalRelationExpression67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression68"):
                opp_val = getattr(old_value, "stext_Expression68", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression68"):
                opp_val = getattr(value, "stext_Expression68", None)
                setattr(value, "stext_Expression68", self)

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
            if hasattr(old_value, "stext_Expression65"):
                opp_val = getattr(old_value, "stext_Expression65", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression65"):
                opp_val = getattr(value, "stext_Expression65", None)
                setattr(value, "stext_Expression65", self)

class stext_ElementReferenceExpression(Expression):

    def __init__(self, operationCall: bool, stext_ElementReferenceExpression: "stext_EObject" = None, stext_ElementReferenceExpression97: set["stext_Expression"] = None):
        self.operationCall = operationCall
        self.stext_ElementReferenceExpression = stext_ElementReferenceExpression
        self.stext_ElementReferenceExpression97 = stext_ElementReferenceExpression97 if stext_ElementReferenceExpression97 is not None else set()
        
        pass
    @property
    def operationCall(self):
        return self.__operationCall

    @operationCall.setter
    def operationCall(self, operationCall: bool):
        self.__operationCall = operationCall


    @property
    def stext_ElementReferenceExpression97(self):
        return self.__stext_ElementReferenceExpression97

    @stext_ElementReferenceExpression97.setter
    def stext_ElementReferenceExpression97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ElementReferenceExpression__stext_ElementReferenceExpression97", None)
        self.__stext_ElementReferenceExpression97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stext_Expression98"):
                    opp_val = getattr(item, "stext_Expression98", None)
                    
                    if opp_val == self:
                        setattr(item, "stext_Expression98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stext_Expression98"):
                    opp_val = getattr(item, "stext_Expression98", None)
                    
                    setattr(item, "stext_Expression98", self)
                    

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
            if hasattr(old_value, "stext_EObject95"):
                opp_val = getattr(old_value, "stext_EObject95", None)
                if opp_val == self:
                    setattr(old_value, "stext_EObject95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_EObject95"):
                opp_val = getattr(value, "stext_EObject95", None)
                setattr(value, "stext_EObject95", self)

class stext_LogicalAndExpression(Expression):

    pass
class stext_BitwiseOrExpression(Expression):

    pass
class stext_EventValueReferenceExpression(Expression):

    pass
class stext_PrimitiveValueExpression(Expression):

    pass
class stext_EventRaisingExpression(Expression):

    pass
class Effect:

    pass
class stext_ReactionEffect(Effect):

    pass
class stext_LogicalOrExpression(Expression):

    pass
class Trigger:

    pass
class stext_DefaultTrigger(Trigger):

    pass
class stext_ReactionTrigger(Trigger):

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
            if hasattr(old_value, "stext_Expression12"):
                opp_val = getattr(old_value, "stext_Expression12", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression12"):
                opp_val = getattr(value, "stext_Expression12", None)
                setattr(value, "stext_Expression12", self)

class stext_RegularEventSpec(EventSpec):

    pass
class stext_EventSpec:

    pass
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


class Operation:

    pass
class Declaration:

    pass
class stext_OperationDefinition(Operation, Declaration):

    pass
class stext_Expression(Statement):

    pass
class Property:

    pass
class Variable:

    pass
class stext_VariableDefinition(Property, Variable):

    def __init__(self, readonly: bool, external: bool, stext_VariableDefinition: "stext_Expression" = None):
        self.readonly = readonly
        self.external = external
        self.stext_VariableDefinition = stext_VariableDefinition
        
        pass
    @property
    def readonly(self):
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly


    @property
    def external(self):
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external


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
class stext_SimpleScope(Scope):

    pass
class stext_StatechartScope(Scope):

    pass
class stext_Scope:

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


class Reaction:

    pass
class stext_TransitionReaction(Reaction):

    pass
class stext_LocalReaction(Reaction, Declaration):

    pass
class stext_StateSpecification:

    pass
class stext_StatechartSpecification(ScopedElement):

    pass
class DefRoot:

    pass
class stext_StateRoot(DefRoot):

    pass
class stext_TransitionRoot(DefRoot):

    pass
class stext_StatechartRoot(DefRoot):

    pass
class stext_DefRoot:

    pass