from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    IN = "IN"
    OUT = "OUT"
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
class Type(Enum):
    void = "void"
    integer = "integer"
    real = "real"
    boolean = "boolean"
    string = "string"
class TimeUnit(Enum):
    second = "second"
    millisecond = "millisecond"
    nanosecond = "nanosecond"
class ShiftOperator(Enum):
    left = "left"
    right = "right"
class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    complement = "complement"
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


############################################
# Definition of Classes
############################################

class stext_Declaration:

    pass
class Expression:

    pass
class stext_LogicalOrExpression(Expression):

    pass
class stext_BitwiseAndExpression(Expression):

    pass
class stext_LogicalRelationExpression(Expression):

    def __init__(self, operator: str, stext_LogicalRelationExpression: "stext_Expression" = None, stext_LogicalRelationExpression75: "stext_Expression" = None):
        self.operator = operator
        self.stext_LogicalRelationExpression = stext_LogicalRelationExpression
        self.stext_LogicalRelationExpression75 = stext_LogicalRelationExpression75
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_LogicalRelationExpression75(self):
        return self.__stext_LogicalRelationExpression75

    @stext_LogicalRelationExpression75.setter
    def stext_LogicalRelationExpression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_LogicalRelationExpression__stext_LogicalRelationExpression75", None)
        self.__stext_LogicalRelationExpression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression76"):
                opp_val = getattr(old_value, "stext_Expression76", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression76"):
                opp_val = getattr(value, "stext_Expression76", None)
                setattr(value, "stext_Expression76", self)

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
            if hasattr(old_value, "stext_Expression73"):
                opp_val = getattr(old_value, "stext_Expression73", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression73"):
                opp_val = getattr(value, "stext_Expression73", None)
                setattr(value, "stext_Expression73", self)

class stext_NumericalAddSubtractExpression(Expression):

    def __init__(self, operator: str, stext_NumericalAddSubtractExpression: "stext_Expression" = None, stext_NumericalAddSubtractExpression85: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalAddSubtractExpression = stext_NumericalAddSubtractExpression
        self.stext_NumericalAddSubtractExpression85 = stext_NumericalAddSubtractExpression85
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


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
    def stext_NumericalAddSubtractExpression85(self):
        return self.__stext_NumericalAddSubtractExpression85

    @stext_NumericalAddSubtractExpression85.setter
    def stext_NumericalAddSubtractExpression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalAddSubtractExpression__stext_NumericalAddSubtractExpression85", None)
        self.__stext_NumericalAddSubtractExpression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression86"):
                opp_val = getattr(old_value, "stext_Expression86", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression86"):
                opp_val = getattr(value, "stext_Expression86", None)
                setattr(value, "stext_Expression86", self)

class stext_OperationCall(Expression):

    pass
class stext_LogicalAndExpression(Expression):

    pass
class stext_ElementReferenceExpression(Expression):

    pass
class stext_LogicalNotExpression(Expression):

    pass
class stext_BitwiseOrExpression(Expression):

    pass
class stext_PrimitiveValueExpression(Expression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class stext_ShiftExpression(Expression):

    def __init__(self, operator: str, stext_ShiftExpression: "stext_Expression" = None, stext_ShiftExpression80: "stext_Expression" = None):
        self.operator = operator
        self.stext_ShiftExpression = stext_ShiftExpression
        self.stext_ShiftExpression80 = stext_ShiftExpression80
        
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
    def stext_ShiftExpression80(self):
        return self.__stext_ShiftExpression80

    @stext_ShiftExpression80.setter
    def stext_ShiftExpression80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ShiftExpression__stext_ShiftExpression80", None)
        self.__stext_ShiftExpression80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression81"):
                opp_val = getattr(old_value, "stext_Expression81", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression81"):
                opp_val = getattr(value, "stext_Expression81", None)
                setattr(value, "stext_Expression81", self)

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
            if hasattr(old_value, "stext_Expression93"):
                opp_val = getattr(old_value, "stext_Expression93", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression93"):
                opp_val = getattr(value, "stext_Expression93", None)
                setattr(value, "stext_Expression93", self)

class stext_NumericalMultiplyDivideExpression(Expression):

    def __init__(self, operator: str, stext_NumericalMultiplyDivideExpression: "stext_Expression" = None, stext_NumericalMultiplyDivideExpression90: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalMultiplyDivideExpression = stext_NumericalMultiplyDivideExpression
        self.stext_NumericalMultiplyDivideExpression90 = stext_NumericalMultiplyDivideExpression90
        
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
            if hasattr(old_value, "stext_Expression88"):
                opp_val = getattr(old_value, "stext_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression88"):
                opp_val = getattr(value, "stext_Expression88", None)
                setattr(value, "stext_Expression88", self)

    @property
    def stext_NumericalMultiplyDivideExpression90(self):
        return self.__stext_NumericalMultiplyDivideExpression90

    @stext_NumericalMultiplyDivideExpression90.setter
    def stext_NumericalMultiplyDivideExpression90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalMultiplyDivideExpression__stext_NumericalMultiplyDivideExpression90", None)
        self.__stext_NumericalMultiplyDivideExpression90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression91"):
                opp_val = getattr(old_value, "stext_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression91"):
                opp_val = getattr(value, "stext_Expression91", None)
                setattr(value, "stext_Expression91", self)

class stext_BitwiseXorExpression(Expression):

    pass
class stext_ConditionalExpression(Expression):

    pass
class stext_Statement:

    pass
class Effect:

    pass
class stext_ReactionEffect(Effect):

    pass
class Trigger:

    pass
class stext_ReactionTrigger(Trigger):

    pass
class Variable:

    pass
class stext_VariableDefinition(Variable):

    def __init__(self, readonly: bool, external: bool, type: str, initialValue: str):
        self.readonly = readonly
        self.external = external
        self.type = type
        self.initialValue = initialValue
        
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
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def initialValue(self):
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: str):
        self.__initialValue = initialValue


class Scope:

    pass
class stext_InterfaceScope(Scope):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class stext_SimpleScope(Scope):

    pass
class Event:

    pass
class stext_EventDefinition(Event):

    def __init__(self, direction: str, type: str, stext_EventDefinition: "stext_EventDerivation" = None):
        self.direction = direction
        self.type = type
        self.stext_EventDefinition = stext_EventDefinition
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def stext_EventDefinition(self):
        return self.__stext_EventDefinition

    @stext_EventDefinition.setter
    def stext_EventDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_EventDefinition__stext_EventDefinition", None)
        self.__stext_EventDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_EventDerivation31"):
                opp_val = getattr(old_value, "stext_EventDerivation31", None)
                if opp_val == self:
                    setattr(old_value, "stext_EventDerivation31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_EventDerivation31"):
                opp_val = getattr(value, "stext_EventDerivation31", None)
                setattr(value, "stext_EventDerivation31", self)

class stext_InternalScope(Scope):

    pass
class stext_Variable:

    pass
class Statement:

    pass
class stext_Assignment(Statement):

    def __init__(self, operator: str, stext_Assignment: "stext_Variable" = None, stext_Assignment23: "stext_Expression" = None):
        self.operator = operator
        self.stext_Assignment = stext_Assignment
        self.stext_Assignment23 = stext_Assignment23
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_Assignment(self):
        return self.__stext_Assignment

    @stext_Assignment.setter
    def stext_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_Assignment__stext_Assignment", None)
        self.__stext_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Variable"):
                opp_val = getattr(old_value, "stext_Variable", None)
                if opp_val == self:
                    setattr(old_value, "stext_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Variable"):
                opp_val = getattr(value, "stext_Variable", None)
                setattr(value, "stext_Variable", self)

    @property
    def stext_Assignment23(self):
        return self.__stext_Assignment23

    @stext_Assignment23.setter
    def stext_Assignment23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_Assignment__stext_Assignment23", None)
        self.__stext_Assignment23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression24"):
                opp_val = getattr(old_value, "stext_Expression24", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression24"):
                opp_val = getattr(value, "stext_Expression24", None)
                setattr(value, "stext_Expression24", self)

class BuiltinEventSpec:

    pass
class stext_ExitEvent(BuiltinEventSpec):

    pass
class stext_OnCycleEvent(BuiltinEventSpec):

    pass
class stext_AlwaysEvent(BuiltinEventSpec):

    pass
class stext_EntryEvent(BuiltinEventSpec):

    pass
class stext_Event:

    pass
class stext_EventRaising(Statement):

    pass
class ReactionProperty:

    pass
class stext_EntryPointSpec(ReactionProperty):

    pass
class stext_ExitPointSpec(ReactionProperty):

    pass
class stext_ReactionPriority(ReactionProperty):

    def __init__(self, priority: int):
        self.priority = priority
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


class stext_ReactionProperty:

    pass
class TransitionStatement:

    pass
class stext_ReactionProperties:

    pass
class Reaction:

    pass
class stext_TransitionReaction(TransitionStatement, Reaction):

    pass
class Declaration:

    pass
class stext_Operation(Declaration):

    def __init__(self, paramTypes: str, type: str, stext_Operation: "stext_OperationCall" = None):
        self.paramTypes = paramTypes
        self.type = type
        self.stext_Operation = stext_Operation
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def paramTypes(self):
        return self.__paramTypes

    @paramTypes.setter
    def paramTypes(self, paramTypes: str):
        self.__paramTypes = paramTypes


    @property
    def stext_Operation(self):
        return self.__stext_Operation

    @stext_Operation.setter
    def stext_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_Operation__stext_Operation", None)
        self.__stext_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_OperationCall"):
                opp_val = getattr(old_value, "stext_OperationCall", None)
                if opp_val == self:
                    setattr(old_value, "stext_OperationCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_OperationCall"):
                opp_val = getattr(value, "stext_OperationCall", None)
                setattr(value, "stext_OperationCall", self)

class stext_Clock(Declaration):

    pass
class stext_Entrypoint(Declaration):

    pass
class stext_LocalReaction(Declaration, Reaction):

    pass
class stext_Expression(Statement):

    pass
class stext_EventDerivation:

    pass
class EventSpec:

    pass
class stext_BuiltinEventSpec(EventSpec):

    pass
class stext_TimeEventSpec(EventSpec):

    def __init__(self, value: int, unit: str):
        self.value = value
        self.unit = unit
        
        pass
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
class stext_Exitpoint(Declaration):

    pass
class stext_Scope:

    pass
class stext_TransitionStatement:

    pass
class stext_StateDeclaration:

    pass
class stext_StatechartDefinition:

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