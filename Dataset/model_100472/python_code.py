from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ShiftOperator(Enum):
    right = "right"
    left = "left"
class RelationalOperator(Enum):
    smaller = "smaller"
    smallerEqual = "smallerEqual"
    greater = "greater"
    greaterEqual = "greaterEqual"
    equals = "equals"
    notEquals = "notEquals"
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
class TimeEventType(Enum):
    after = "after"
    every = "every"
class TimeUnit(Enum):
    second = "second"
    millisecond = "millisecond"
    microsend = "microsend"
    nanosecond = "nanosecond"
class Direction(Enum):
    LOCAL = "LOCAL"
    IN = "IN"
    OUT = "OUT"
class UnaryOperator(Enum):
    positive = "positive"
    negative = "negative"
    complement = "complement"
class AdditiveOperator(Enum):
    plus = "plus"
    minus = "minus"
class MultiplicativeOperator(Enum):
    mul = "mul"
    div = "div"
    mod = "mod"


############################################
# Definition of Classes
############################################

class BuiltinEventSpec:

    pass
class stext_DefaultEvent(BuiltinEventSpec):

    pass
class stext_ExitEvent(BuiltinEventSpec):

    pass
class stext_AlwaysEvent(BuiltinEventSpec):

    pass
class stext_OnCycleEvent(BuiltinEventSpec):

    pass
class stext_EntryEvent(BuiltinEventSpec):

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
class Declaration:

    pass
class stext_Entrypoint(Declaration):

    pass
class stext_Exitpoint(Declaration):

    pass
class stext_LocalReaction(Reaction, Declaration):

    pass
class stext_EventDerivation:

    pass
class stext_TransitionReaction(Reaction):

    pass
class stext_Event:

    pass
class EventSpec:

    pass
class stext_TimeEventSpec(EventSpec):

    def __init__(self, type: str, value: int, unit: str):
        self.type = type
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


class stext_BuiltinEventSpec(EventSpec):

    pass
class stext_RegularEventSpec(EventSpec):

    pass
class stext_EventSpec:

    pass
class stext_StatechartSpecification:

    def __init__(self, namespace: str, stext_StatechartSpecification5: set["stext_Scope"] = None, stext_StatechartSpecification: "stext_StatechartRoot" = None):
        self.namespace = namespace
        self.stext_StatechartSpecification5 = stext_StatechartSpecification5 if stext_StatechartSpecification5 is not None else set()
        self.stext_StatechartSpecification = stext_StatechartSpecification
        
        pass
    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace


    @property
    def stext_StatechartSpecification(self):
        return self.__stext_StatechartSpecification

    @stext_StatechartSpecification.setter
    def stext_StatechartSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_StatechartSpecification__stext_StatechartSpecification", None)
        self.__stext_StatechartSpecification = value
        
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

    @property
    def stext_StatechartSpecification5(self):
        return self.__stext_StatechartSpecification5

    @stext_StatechartSpecification5.setter
    def stext_StatechartSpecification5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_StatechartSpecification__stext_StatechartSpecification5", None)
        self.__stext_StatechartSpecification5 = value if value is not None else set()
        
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
                    

class DefRoot:

    pass
class stext_StateRoot(DefRoot):

    pass
class stext_StatechartRoot(DefRoot):

    pass
class stext_DefRoot:

    pass
class stext_Root:

    pass
class stext_Scope:

    pass
class stext_TransitionSpecification:

    pass
class stext_TransitionRoot(DefRoot):

    pass
class stext_StateSpecification:

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
class stext_Operation(Declaration):

    pass
class Scope:

    pass
class stext_InternalScope(Scope):

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
class stext_Declaration:

    pass
class Expression:

    pass
class stext_ConditionalExpression(Expression):

    pass
class stext_ShiftExpression(Expression):

    def __init__(self, operator: str, stext_ShiftExpression: "stext_Expression" = None, stext_ShiftExpression99: "stext_Expression" = None):
        self.operator = operator
        self.stext_ShiftExpression = stext_ShiftExpression
        self.stext_ShiftExpression99 = stext_ShiftExpression99
        
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
            if hasattr(old_value, "stext_Expression97"):
                opp_val = getattr(old_value, "stext_Expression97", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression97"):
                opp_val = getattr(value, "stext_Expression97", None)
                setattr(value, "stext_Expression97", self)

    @property
    def stext_ShiftExpression99(self):
        return self.__stext_ShiftExpression99

    @stext_ShiftExpression99.setter
    def stext_ShiftExpression99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_ShiftExpression__stext_ShiftExpression99", None)
        self.__stext_ShiftExpression99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression100"):
                opp_val = getattr(old_value, "stext_Expression100", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression100"):
                opp_val = getattr(value, "stext_Expression100", None)
                setattr(value, "stext_Expression100", self)

class stext_BitwiseXorExpression(Expression):

    pass
class stext_EventValueReferenceExpression(Expression):

    pass
class stext_LogicalRelationExpression(Expression):

    def __init__(self, operator: str, stext_LogicalRelationExpression: "stext_Expression" = None, stext_LogicalRelationExpression94: "stext_Expression" = None):
        self.operator = operator
        self.stext_LogicalRelationExpression = stext_LogicalRelationExpression
        self.stext_LogicalRelationExpression94 = stext_LogicalRelationExpression94
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_LogicalRelationExpression94(self):
        return self.__stext_LogicalRelationExpression94

    @stext_LogicalRelationExpression94.setter
    def stext_LogicalRelationExpression94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_LogicalRelationExpression__stext_LogicalRelationExpression94", None)
        self.__stext_LogicalRelationExpression94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression95"):
                opp_val = getattr(old_value, "stext_Expression95", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression95"):
                opp_val = getattr(value, "stext_Expression95", None)
                setattr(value, "stext_Expression95", self)

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
            if hasattr(old_value, "stext_Expression92"):
                opp_val = getattr(old_value, "stext_Expression92", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression92"):
                opp_val = getattr(value, "stext_Expression92", None)
                setattr(value, "stext_Expression92", self)

class stext_NumericalAddSubtractExpression(Expression):

    def __init__(self, operator: str, stext_NumericalAddSubtractExpression: "stext_Expression" = None, stext_NumericalAddSubtractExpression104: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalAddSubtractExpression = stext_NumericalAddSubtractExpression
        self.stext_NumericalAddSubtractExpression104 = stext_NumericalAddSubtractExpression104
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_NumericalAddSubtractExpression104(self):
        return self.__stext_NumericalAddSubtractExpression104

    @stext_NumericalAddSubtractExpression104.setter
    def stext_NumericalAddSubtractExpression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalAddSubtractExpression__stext_NumericalAddSubtractExpression104", None)
        self.__stext_NumericalAddSubtractExpression104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression105"):
                opp_val = getattr(old_value, "stext_Expression105", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression105"):
                opp_val = getattr(value, "stext_Expression105", None)
                setattr(value, "stext_Expression105", self)

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
            if hasattr(old_value, "stext_Expression102"):
                opp_val = getattr(old_value, "stext_Expression102", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression102"):
                opp_val = getattr(value, "stext_Expression102", None)
                setattr(value, "stext_Expression102", self)

class stext_PrimitiveValueExpression(Expression):

    pass
class stext_LogicalOrExpression(Expression):

    pass
class stext_NumericalMultiplyDivideExpression(Expression):

    def __init__(self, operator: str, stext_NumericalMultiplyDivideExpression: "stext_Expression" = None, stext_NumericalMultiplyDivideExpression109: "stext_Expression" = None):
        self.operator = operator
        self.stext_NumericalMultiplyDivideExpression = stext_NumericalMultiplyDivideExpression
        self.stext_NumericalMultiplyDivideExpression109 = stext_NumericalMultiplyDivideExpression109
        
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
            if hasattr(old_value, "stext_Expression107"):
                opp_val = getattr(old_value, "stext_Expression107", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression107"):
                opp_val = getattr(value, "stext_Expression107", None)
                setattr(value, "stext_Expression107", self)

    @property
    def stext_NumericalMultiplyDivideExpression109(self):
        return self.__stext_NumericalMultiplyDivideExpression109

    @stext_NumericalMultiplyDivideExpression109.setter
    def stext_NumericalMultiplyDivideExpression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_NumericalMultiplyDivideExpression__stext_NumericalMultiplyDivideExpression109", None)
        self.__stext_NumericalMultiplyDivideExpression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression110"):
                opp_val = getattr(old_value, "stext_Expression110", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression110"):
                opp_val = getattr(value, "stext_Expression110", None)
                setattr(value, "stext_Expression110", self)

class stext_OperationCall(Expression):

    pass
class stext_BitwiseAndExpression(Expression):

    pass
class stext_BitwiseOrExpression(Expression):

    pass
class stext_LogicalAndExpression(Expression):

    pass
class stext_LogicalNotExpression(Expression):

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
            if hasattr(old_value, "stext_Expression112"):
                opp_val = getattr(old_value, "stext_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression112"):
                opp_val = getattr(value, "stext_Expression112", None)
                setattr(value, "stext_Expression112", self)

class stext_ActiveStateReferenceExpression(Expression):

    pass
class stext_ElementReferenceExpression(Expression):

    pass
class Variable:

    pass
class stext_VariableDefinition(Variable):

    def __init__(self, readonly: bool, external: bool, stext_VariableDefinition: "stext_Type" = None, stext_VariableDefinition44: "stext_Expression" = None):
        self.readonly = readonly
        self.external = external
        self.stext_VariableDefinition = stext_VariableDefinition
        self.stext_VariableDefinition44 = stext_VariableDefinition44
        
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
            if hasattr(old_value, "stext_Type42"):
                opp_val = getattr(old_value, "stext_Type42", None)
                if opp_val == self:
                    setattr(old_value, "stext_Type42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Type42"):
                opp_val = getattr(value, "stext_Type42", None)
                setattr(value, "stext_Type42", self)

    @property
    def stext_VariableDefinition44(self):
        return self.__stext_VariableDefinition44

    @stext_VariableDefinition44.setter
    def stext_VariableDefinition44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_VariableDefinition__stext_VariableDefinition44", None)
        self.__stext_VariableDefinition44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_Expression45"):
                opp_val = getattr(old_value, "stext_Expression45", None)
                if opp_val == self:
                    setattr(old_value, "stext_Expression45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Expression45"):
                opp_val = getattr(value, "stext_Expression45", None)
                setattr(value, "stext_Expression45", self)

class stext_Type:

    pass
class Event:

    pass
class stext_EventDefinition(Event):

    def __init__(self, direction: str, stext_EventDefinition: "stext_Type" = None, stext_EventDefinition39: "stext_EventDerivation" = None):
        self.direction = direction
        self.stext_EventDefinition = stext_EventDefinition
        self.stext_EventDefinition39 = stext_EventDefinition39
        
        pass
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
            if hasattr(old_value, "stext_Type"):
                opp_val = getattr(old_value, "stext_Type", None)
                if opp_val == self:
                    setattr(old_value, "stext_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_Type"):
                opp_val = getattr(value, "stext_Type", None)
                setattr(value, "stext_Type", self)

    @property
    def stext_EventDefinition39(self):
        return self.__stext_EventDefinition39

    @stext_EventDefinition39.setter
    def stext_EventDefinition39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_EventDefinition__stext_EventDefinition39", None)
        self.__stext_EventDefinition39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stext_EventDerivation40"):
                opp_val = getattr(old_value, "stext_EventDerivation40", None)
                if opp_val == self:
                    setattr(old_value, "stext_EventDerivation40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stext_EventDerivation40"):
                opp_val = getattr(value, "stext_EventDerivation40", None)
                setattr(value, "stext_EventDerivation40", self)

class stext_Variable:

    pass
class Statement:

    pass
class stext_Expression(Statement):

    pass
class stext_EventRaising(Statement):

    pass
class stext_Assignment(Statement):

    def __init__(self, operator: str, stext_Assignment: "stext_Variable" = None, stext_Assignment26: "stext_Expression" = None):
        self.operator = operator
        self.stext_Assignment = stext_Assignment
        self.stext_Assignment26 = stext_Assignment26
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def stext_Assignment26(self):
        return self.__stext_Assignment26

    @stext_Assignment26.setter
    def stext_Assignment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stext_Assignment__stext_Assignment26", None)
        self.__stext_Assignment26 = value
        
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
