from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MultiplicativeOperator(Enum):
    mul = "mul"
    div = "div"
    mod = "mod"
class RelationalOperator(Enum):
    smaller = "smaller"
    smallerEqual = "smallerEqual"
    greater = "greater"
    greaterEqual = "greaterEqual"
    equals = "equals"
    notEquals = "notEquals"
class Direction(Enum):
    LOCAL = "LOCAL"
    IN = "IN"
    OUT = "OUT"
class ShiftOperator(Enum):
    left = "left"
    right = "right"
class TimeEventType(Enum):
    after = "after"
    every = "every"
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
class TimeUnit(Enum):
    second = "second"
    millisecond = "millisecond"
    microsecond = "microsecond"
    nanosecond = "nanosecond"
class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    complement = "complement"


############################################
# Definition of Classes
############################################

class stext_State:

    pass
class stext_EObject:

    pass
class Expression:

    pass
class stext_LogicalRelationExpression(Expression):

    def __init__(self, operator: str, stext_LogicalRelationExpression: "stext_Expression" = None, stext_LogicalRelationExpression71: "stext_Expression" = None):
        self.operator = operator
        self.stext_LogicalRelationExpression = stext_LogicalRelationExpression
        self.stext_LogicalRelationExpression71 = stext_LogicalRelationExpression71
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


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
            if hasattr(old_value, "stext_Expression69"):
                opp_val = getattr(old_value, "stext_Expression69", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression69"):
                opp_val = getattr(value, "stext_Expression69", None)
                setattr(value, "stext_Expression69", self)

    @property
    def stext_LogicalRelationExpression71(self):
        return self.__stext_LogicalRelationExpression71

    @stext_LogicalRelationExpression71.setter
    def stext_LogicalRelationExpression71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_LogicalRelationExpression__stext_LogicalRelationExpression71", None)
        self.__stext_LogicalRelationExpression71 = value
        
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

class stext_PrimitiveValueExpression(Expression):

    pass
class stext_BitwiseXorExpression(Expression):

    pass
class stext_NumericalMultiplyDivideExpression(Expression):

    def __init__(self, operator: str, stext_NumericalMultiplyDivideExpression: "stext_Expression" = None, stext_NumericalMultiplyDivideExpression86: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalMultiplyDivideExpression = stext_NumericalMultiplyDivideExpression
        self.stext_NumericalMultiplyDivideExpression86 = stext_NumericalMultiplyDivideExpression86
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalMultiplyDivideExpression86(self):
        return self.__stext_NumericalMultiplyDivideExpression86

    @stext_NumericalMultiplyDivideExpression86.setter
    def stext_NumericalMultiplyDivideExpression86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalMultiplyDivideExpression__stext_NumericalMultiplyDivideExpression86", None)
        self.__stext_NumericalMultiplyDivideExpression86 = value
        
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
            if hasattr(old_value, "stext_Expression84"):
                opp_val = getattr(old_value, "stext_Expression84", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression84"):
                opp_val = getattr(value, "stext_Expression84", None)
                setattr(value, "stext_Expression84", self)

class stext_EventValueReferenceExpression(Expression):

    pass
class stext_NumericalAddSubtractExpression(Expression):

    def __init__(self, operator: str, stext_NumericalAddSubtractExpression: "stext_Expression" = None, stext_NumericalAddSubtractExpression81: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalAddSubtractExpression = stext_NumericalAddSubtractExpression
        self.stext_NumericalAddSubtractExpression81 = stext_NumericalAddSubtractExpression81
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalAddSubtractExpression81(self):
        return self.__stext_NumericalAddSubtractExpression81

    @stext_NumericalAddSubtractExpression81.setter
    def stext_NumericalAddSubtractExpression81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalAddSubtractExpression__stext_NumericalAddSubtractExpression81", None)
        self.__stext_NumericalAddSubtractExpression81 = value
        
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
    def stext_NumericalAddSubtractExpression(self):
        return self.__stext_NumericalAddSubtractExpression

    @stext_NumericalAddSubtractExpression.setter
    def stext_NumericalAddSubtractExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalAddSubtractExpression__stext_NumericalAddSubtractExpression", None)
        self.__stext_NumericalAddSubtractExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression79"):
                opp_val = getattr(old_value, "stext_Expression79", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression79"):
                opp_val = getattr(value, "stext_Expression79", None)
                setattr(value, "stext_Expression79", self)

class stext_FeatureCall(Expression):

    def __init__(self, operationCall: bool, stext_FeatureCall94: "stext_EObject" = None, stext_FeatureCall96: set["stext_Expression"] = None, stext_FeatureCall: "stext_Expression" = None):
        self.operationCall = operationCall
        self.stext_FeatureCall94 = stext_FeatureCall94
        self.stext_FeatureCall96 = stext_FeatureCall96 if stext_FeatureCall96 is not None else set()
        self.stext_FeatureCall = stext_FeatureCall
        
        pass
    @property
    def operationCall(self):
        return self.__operationCall

    @operationCall.setter
    def operationCall(self, operationCall: bool):
        self.__operationCall = operationCall


    @property
    def stext_FeatureCall96(self):
        return self.__stext_FeatureCall96

    @stext_FeatureCall96.setter
    def stext_FeatureCall96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_FeatureCall__stext_FeatureCall96", None)
        self.__stext_FeatureCall96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stext_Expression97"):
                    opp_val = getattr(item, "stext_Expression97", None)
                    
                    if opp_val == self:
                        setattr(item, "stext_Expression97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stext_Expression97"):
                    opp_val = getattr(item, "stext_Expression97", None)
                    
                    setattr(item, "stext_Expression97", self)
                    

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
            if hasattr(old_value, "stext_Expression92"):
                opp_val = getattr(old_value, "stext_Expression92", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression92"):
                opp_val = getattr(value, "stext_Expression92", None)
                setattr(value, "stext_Expression92", self)

    @property
    def stext_FeatureCall94(self):
        return self.__stext_FeatureCall94

    @stext_FeatureCall94.setter
    def stext_FeatureCall94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_FeatureCall__stext_FeatureCall94", None)
        self.__stext_FeatureCall94 = value
        
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

class stext_LogicalAndExpression(Expression):

    pass
class stext_LogicalOrExpression(Expression):

    pass
class stext_AssignmentExpression(Expression):

    def __init__(self, operator: str, stext_AssignmentExpression: "stext_Expression" = None, stext_AssignmentExpression31: "stext_Expression" = None):
        self.operator = operator
        self.stext_AssignmentExpression = stext_AssignmentExpression
        self.stext_AssignmentExpression31 = stext_AssignmentExpression31
        
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
            if hasattr(old_value, "stext_Expression29"):
                opp_val = getattr(old_value, "stext_Expression29", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression29"):
                opp_val = getattr(value, "stext_Expression29", None)
                setattr(value, "stext_Expression29", self)

    @property
    def stext_AssignmentExpression31(self):
        return self.__stext_AssignmentExpression31

    @stext_AssignmentExpression31.setter
    def stext_AssignmentExpression31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_AssignmentExpression__stext_AssignmentExpression31", None)
        self.__stext_AssignmentExpression31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression32"):
                opp_val = getattr(old_value, "stext_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression32"):
                opp_val = getattr(value, "stext_Expression32", None)
                setattr(value, "stext_Expression32", self)

class stext_BitwiseAndExpression(Expression):

    pass
class stext_BitwiseOrExpression(Expression):

    pass
class stext_ShiftExpression(Expression):

    def __init__(self, operator: str, stext_ShiftExpression: "stext_Expression" = None, stext_ShiftExpression76: "stext_Expression" = None):
        self.operator = operator
        self.stext_ShiftExpression = stext_ShiftExpression
        self.stext_ShiftExpression76 = stext_ShiftExpression76
        
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
            if hasattr(old_value, "stext_Expression74"):
                opp_val = getattr(old_value, "stext_Expression74", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression74"):
                opp_val = getattr(value, "stext_Expression74", None)
                setattr(value, "stext_Expression74", self)

    @property
    def stext_ShiftExpression76(self):
        return self.__stext_ShiftExpression76

    @stext_ShiftExpression76.setter
    def stext_ShiftExpression76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ShiftExpression__stext_ShiftExpression76", None)
        self.__stext_ShiftExpression76 = value
        
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

class stext_ActiveStateReferenceExpression(Expression):

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
            if hasattr(old_value, "stext_Expression89"):
                opp_val = getattr(old_value, "stext_Expression89", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression89"):
                opp_val = getattr(value, "stext_Expression89", None)
                setattr(value, "stext_Expression89", self)

class stext_ElementReferenceExpression(Expression):

    def __init__(self, operationCall: bool, stext_ElementReferenceExpression: "stext_EObject" = None, stext_ElementReferenceExpression101: set["stext_Expression"] = None):
        self.operationCall = operationCall
        self.stext_ElementReferenceExpression = stext_ElementReferenceExpression
        self.stext_ElementReferenceExpression101 = stext_ElementReferenceExpression101 if stext_ElementReferenceExpression101 is not None else set()
        
        pass
    @property
    def operationCall(self):
        return self.__operationCall

    @operationCall.setter
    def operationCall(self, operationCall: bool):
        self.__operationCall = operationCall


    @property
    def stext_ElementReferenceExpression101(self):
        return self.__stext_ElementReferenceExpression101

    @stext_ElementReferenceExpression101.setter
    def stext_ElementReferenceExpression101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ElementReferenceExpression__stext_ElementReferenceExpression101", None)
        self.__stext_ElementReferenceExpression101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stext_Expression102"):
                    opp_val = getattr(item, "stext_Expression102", None)
                    
                    if opp_val == self:
                        setattr(item, "stext_Expression102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stext_Expression102"):
                    opp_val = getattr(item, "stext_Expression102", None)
                    
                    setattr(item, "stext_Expression102", self)
                    

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
            if hasattr(old_value, "stext_EObject99"):
                opp_val = getattr(old_value, "stext_EObject99", None)
                if opp_val == self:
                    setattr(old_value, "stext_EObject99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_EObject99"):
                opp_val = getattr(value, "stext_EObject99", None)
                setattr(value, "stext_EObject99", self)

class stext_ConditionalExpression(Expression):

    pass
class stext_EventRaisingExpression(Expression):

    pass
class Effect:

    pass
class stext_ReactionEffect(Effect):

    pass
class stext_LogicalNotExpression(Expression):

    pass
class Trigger:

    pass
class stext_ReactionTrigger(Trigger):

    pass
class Literal:

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
class BuiltinEventSpec:

    pass
class stext_DefaultEvent(BuiltinEventSpec):

    pass
class stext_ExitEvent(BuiltinEventSpec):

    pass
class stext_OnCycleEvent(BuiltinEventSpec):

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

    def __init__(self, type: str, value: int, unit: str):
        self.type = type
        self.value = value
        self.unit = unit
        
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
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class stext_RegularEventSpec(EventSpec):

    pass
class stext_EventSpec:

    pass
class ReactionProperty:

    pass
class stext_ExitPointSpec(ReactionProperty):

    pass
class stext_EntryPointSpec(ReactionProperty):

    pass
class stext_ReactionProperty:

    pass
class stext_ReactionProperties:

    pass
class Reaction:

    pass
class Operation:

    pass
class Declaration:

    pass
class stext_LocalReaction(Declaration, Reaction):

    pass
class stext_Exitpoint(Declaration):

    pass
class stext_OperationDefinition(Operation, Declaration):

    pass
class stext_Expression(Statement):

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
class stext_SimpleScope(Scope):

    pass
class stext_StatechartScope(Scope):

    pass
class stext_TransitionReaction(Reaction):

    pass
class stext_Scope:

    pass
class stext_Entrypoint(Declaration):

    pass
class stext_TransitionSpecification:

    pass
class stext_StateSpecification:

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
class stext_Root:

    pass
class ScopedElement:

    pass
class stext_StatechartSpecification(ScopedElement):

    pass