from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    void = "void"
    integer = "integer"
    real = "real"
    boolean = "boolean"
    string = "string"
class MultiplicativeOperator(Enum):
    mul = "mul"
    div = "div"
    mod = "mod"
class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    complement = "complement"
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
class AdditiveOperator(Enum):
    plus = "plus"
    minus = "minus"
class TimeEventType(Enum):
    after = "after"
    every = "every"
class ShiftOperator(Enum):
    left = "left"
    right = "right"
class TimeUnit(Enum):
    second = "second"
    millisecond = "millisecond"
    nanosecond = "nanosecond"
class AssignmentOperator(Enum):
    xorAssign = "xorAssign"
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


############################################
# Definition of Classes
############################################

class Variable:

    pass
class stext_VariableDefinition(Variable):

    def __init__(self, readonly: bool, external: bool, type: str, stext_VariableDefinition: "stext_Expression" = None):
        self.readonly = readonly
        self.external = external
        self.type = type
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
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


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
            if hasattr(old_value, "stext_Expression39"):
                opp_val = getattr(old_value, "stext_Expression39", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression39"):
                opp_val = getattr(value, "stext_Expression39", None)
                setattr(value, "stext_Expression39", self)

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
class stext_Declaration:

    pass
class Expression:

    pass
class stext_BitwiseAndExpression(Expression):

    pass
class stext_ShiftExpression(Expression):

    def __init__(self, operator: str, stext_ShiftExpression: "stext_Expression" = None, stext_ShiftExpression88: "stext_Expression" = None):
        self.operator = operator
        self.stext_ShiftExpression = stext_ShiftExpression
        self.stext_ShiftExpression88 = stext_ShiftExpression88
        
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
            if hasattr(old_value, "stext_Expression86"):
                opp_val = getattr(old_value, "stext_Expression86", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression86"):
                opp_val = getattr(value, "stext_Expression86", None)
                setattr(value, "stext_Expression86", self)

    @property
    def stext_ShiftExpression88(self):
        return self.__stext_ShiftExpression88

    @stext_ShiftExpression88.setter
    def stext_ShiftExpression88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ShiftExpression__stext_ShiftExpression88", None)
        self.__stext_ShiftExpression88 = value
        
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

class stext_ConditionalExpression(Expression):

    pass
class stext_NumericalAddSubtractExpression(Expression):

    def __init__(self, operator: str, stext_NumericalAddSubtractExpression: "stext_Expression" = None, stext_NumericalAddSubtractExpression93: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalAddSubtractExpression = stext_NumericalAddSubtractExpression
        self.stext_NumericalAddSubtractExpression93 = stext_NumericalAddSubtractExpression93
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalAddSubtractExpression93(self):
        return self.__stext_NumericalAddSubtractExpression93

    @stext_NumericalAddSubtractExpression93.setter
    def stext_NumericalAddSubtractExpression93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalAddSubtractExpression__stext_NumericalAddSubtractExpression93", None)
        self.__stext_NumericalAddSubtractExpression93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression94"):
                opp_val = getattr(old_value, "stext_Expression94", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression94"):
                opp_val = getattr(value, "stext_Expression94", None)
                setattr(value, "stext_Expression94", self)

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
            if hasattr(old_value, "stext_Expression91"):
                opp_val = getattr(old_value, "stext_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression91"):
                opp_val = getattr(value, "stext_Expression91", None)
                setattr(value, "stext_Expression91", self)

class stext_PrimitiveValueExpression(Expression):

    pass
class stext_LogicalNotExpression(Expression):

    pass
class stext_OperationCall(Expression):

    pass
class stext_LogicalRelationExpression(Expression):

    def __init__(self, operator: str, stext_LogicalRelationExpression: "stext_Expression" = None, stext_LogicalRelationExpression83: "stext_Expression" = None):
        self.operator = operator
        self.stext_LogicalRelationExpression = stext_LogicalRelationExpression
        self.stext_LogicalRelationExpression83 = stext_LogicalRelationExpression83
        
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
            if hasattr(old_value, "stext_Expression81"):
                opp_val = getattr(old_value, "stext_Expression81", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression81"):
                opp_val = getattr(value, "stext_Expression81", None)
                setattr(value, "stext_Expression81", self)

    @property
    def stext_LogicalRelationExpression83(self):
        return self.__stext_LogicalRelationExpression83

    @stext_LogicalRelationExpression83.setter
    def stext_LogicalRelationExpression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_LogicalRelationExpression__stext_LogicalRelationExpression83", None)
        self.__stext_LogicalRelationExpression83 = value
        
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

class stext_BitwiseOrExpression(Expression):

    pass
class stext_BitwiseXorExpression(Expression):

    pass
class stext_LogicalOrExpression(Expression):

    pass
class stext_EventValueReferenceExpression(Expression):

    pass
class stext_NumericalMultiplyDivideExpression(Expression):

    def __init__(self, operator: str, stext_NumericalMultiplyDivideExpression: "stext_Expression" = None, stext_NumericalMultiplyDivideExpression98: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalMultiplyDivideExpression = stext_NumericalMultiplyDivideExpression
        self.stext_NumericalMultiplyDivideExpression98 = stext_NumericalMultiplyDivideExpression98
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalMultiplyDivideExpression98(self):
        return self.__stext_NumericalMultiplyDivideExpression98

    @stext_NumericalMultiplyDivideExpression98.setter
    def stext_NumericalMultiplyDivideExpression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalMultiplyDivideExpression__stext_NumericalMultiplyDivideExpression98", None)
        self.__stext_NumericalMultiplyDivideExpression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression99"):
                opp_val = getattr(old_value, "stext_Expression99", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression99"):
                opp_val = getattr(value, "stext_Expression99", None)
                setattr(value, "stext_Expression99", self)

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
            if hasattr(old_value, "stext_Expression96"):
                opp_val = getattr(old_value, "stext_Expression96", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression96"):
                opp_val = getattr(value, "stext_Expression96", None)
                setattr(value, "stext_Expression96", self)

class stext_LogicalAndExpression(Expression):

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
            if hasattr(old_value, "stext_Expression101"):
                opp_val = getattr(old_value, "stext_Expression101", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression101"):
                opp_val = getattr(value, "stext_Expression101", None)
                setattr(value, "stext_Expression101", self)

class stext_ElementReferenceExpression(Expression):

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
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


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
            if hasattr(old_value, "stext_EventDerivation37"):
                opp_val = getattr(old_value, "stext_EventDerivation37", None)
                if opp_val == self:
                    setattr(old_value, "stext_EventDerivation37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_EventDerivation37"):
                opp_val = getattr(value, "stext_EventDerivation37", None)
                setattr(value, "stext_EventDerivation37", self)

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


class stext_InternalScope(Scope):

    pass
class stext_SimpleScope(Scope):

    pass
class Literal:

    pass
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
class stext_RegularState:

    pass
class stext_ActiveStateReferenceExpression(Expression):

    pass
class stext_EventRaisedReferenceExpression(Expression):

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

class stext_EventRaising(Statement):

    pass
class ReactionProperty:

    pass
class stext_EntryPointSpec(ReactionProperty):

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
class stext_TransitionReaction(Reaction, TransitionStatement):

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
class stext_LocalReaction(Declaration, Reaction):

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
class stext_Event:

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
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class stext_RegularEventSpec(EventSpec):

    pass
class stext_EventSpec:

    pass
class stext_Exitpoint(Declaration):

    pass
class stext_ExitPointSpec(ReactionProperty):

    pass
class stext_Entrypoint(Declaration):

    pass
class stext_Expression(Statement):

    pass
class stext_EventDerivation:

    pass
class stext_Scope:

    pass
class stext_TransitionStatement:

    pass
class stext_StatechartDefinition:

    def __init__(self, namespace: str, stext_StatechartDefinition: "stext_StatechartRoot" = None, stext_StatechartDefinition5: set["stext_Scope"] = None):
        self.namespace = namespace
        self.stext_StatechartDefinition = stext_StatechartDefinition
        self.stext_StatechartDefinition5 = stext_StatechartDefinition5 if stext_StatechartDefinition5 is not None else set()
        
        pass
    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace


    @property
    def stext_StatechartDefinition5(self):
        return self.__stext_StatechartDefinition5

    @stext_StatechartDefinition5.setter
    def stext_StatechartDefinition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_StatechartDefinition__stext_StatechartDefinition5", None)
        self.__stext_StatechartDefinition5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stext_Scope"):
                    opp_val = getattr(item, "stext_Scope", None)
                    
                    if opp_val == self:
                        setattr(item, "stext_Scope", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stext_Scope"):
                    opp_val = getattr(item, "stext_Scope", None)
                    
                    setattr(item, "stext_Scope", self)
                    

    @property
    def stext_StatechartDefinition(self):
        return self.__stext_StatechartDefinition

    @stext_StatechartDefinition.setter
    def stext_StatechartDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_StatechartDefinition__stext_StatechartDefinition", None)
        self.__stext_StatechartDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_StatechartRoot"):
                opp_val = getattr(old_value, "stext_StatechartRoot", None)
                if opp_val == self:
                    setattr(old_value, "stext_StatechartRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_StatechartRoot"):
                opp_val = getattr(value, "stext_StatechartRoot", None)
                setattr(value, "stext_StatechartRoot", self)

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
class stext_StateDeclaration:

    pass