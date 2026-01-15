from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TriggerType(Enum):
    SIMPLE = "SIMPLE"
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    SYNC = "SYNC"
    EMPTY = "EMPTY"
class VariableModifier(Enum):
    VAR = "VAR"
    CONST = "CONST"


############################################
# Definition of Classes
############################################

class Assignable:

    pass
class robochart_VarRef(Assignable):

    pass
class robochart_ArrayAssignable(Assignable):

    pass
class robochart_VarSelection(Assignable):

    pass
class robochart_NamedExpression(ABC):

    pass
class LambdaExp:

    pass
class robochart_DefiniteDescription(LambdaExp):

    pass
class BinaryExpression:

    pass
class robochart_LessThan(BinaryExpression):

    pass
class robochart_And(BinaryExpression):

    pass
class robochart_Equals(BinaryExpression):

    pass
class robochart_GreaterOrEqual(BinaryExpression):

    pass
class robochart_LessOrEqual(BinaryExpression):

    pass
class robochart_Cat(BinaryExpression):

    pass
class robochart_Mult(BinaryExpression):

    pass
class robochart_Minus(BinaryExpression):

    pass
class robochart_Different(BinaryExpression):

    pass
class robochart_Or(BinaryExpression):

    pass
class robochart_Modulus(BinaryExpression):

    pass
class robochart_Plus(BinaryExpression):

    pass
class robochart_GreaterThan(BinaryExpression):

    pass
class robochart_Implies(BinaryExpression):

    pass
class robochart_Div(BinaryExpression):

    pass
class robochart_Iff(BinaryExpression):

    pass
class Expression:

    pass
class robochart_SetExp(Expression):

    pass
class robochart_IfExpression(Expression):

    pass
class robochart_AsExp(Expression):

    pass
class robochart_QuantifierExpression(Expression):

    pass
class robochart_TupleExp(Expression):

    pass
class robochart_FromExp(Expression):

    pass
class robochart_IsExp(Expression):

    pass
class robochart_EnumExp(Expression):

    pass
class robochart_BooleanExp(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class robochart_IntegerExp(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class robochart_ArrayExp(Expression):

    pass
class robochart_StringExp(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class robochart_ElseExp(Expression):

    pass
class robochart_Selection(Expression):

    pass
class robochart_IdExp(Expression):

    pass
class robochart_VarExp(Expression):

    pass
class robochart_SetRange(Expression):

    pass
class robochart_LetExpression(Expression):

    pass
class robochart_StateClockExp(Expression):

    pass
class robochart_SetComp(Expression):

    pass
class robochart_WaitingConditionRef(Expression):

    pass
class robochart_ParExp(Expression):

    pass
class robochart_Not(Expression):

    pass
class robochart_ToExp(Expression):

    pass
class robochart_RefExp(Expression):

    pass
class robochart_CallExp(Expression):

    pass
class robochart_RangeExp(Expression):

    def __init__(self, rinterval: str, linterval: str, robochart_RangeExp291: "robochart_Expression" = None, robochart_RangeExp: "robochart_Expression" = None):
        self.rinterval = rinterval
        self.linterval = linterval
        self.robochart_RangeExp291 = robochart_RangeExp291
        self.robochart_RangeExp = robochart_RangeExp
        
    @property
    def linterval(self) -> str:
        return self.__linterval

    @linterval.setter
    def linterval(self, linterval: str):
        self.__linterval = linterval

    @property
    def rinterval(self) -> str:
        return self.__rinterval

    @rinterval.setter
    def rinterval(self, rinterval: str):
        self.__rinterval = rinterval

    @property
    def robochart_RangeExp291(self):
        return self.__robochart_RangeExp291

    @robochart_RangeExp291.setter
    def robochart_RangeExp291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_RangeExp__robochart_RangeExp291", None)
        self.__robochart_RangeExp291 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Expression292"):
                opp_val = getattr(old_value, "robochart_Expression292", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Expression292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Expression292"):
                opp_val = getattr(value, "robochart_Expression292", None)
                setattr(value, "robochart_Expression292", self)

    @property
    def robochart_RangeExp(self):
        return self.__robochart_RangeExp

    @robochart_RangeExp.setter
    def robochart_RangeExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_RangeExp__robochart_RangeExp", None)
        self.__robochart_RangeExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Expression289"):
                opp_val = getattr(old_value, "robochart_Expression289", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Expression289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Expression289"):
                opp_val = getattr(value, "robochart_Expression289", None)
                setattr(value, "robochart_Expression289", self)

class robochart_InExp(Expression):

    pass
class robochart_ClockExp(Expression):

    pass
class robochart_BinaryExpression(Expression):

    pass
class robochart_Neg(Expression):

    pass
class robochart_FloatExp(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class robochart_TypeExp(Expression):

    pass
class robochart_SeqExp(Expression):

    pass
class robochart_ResultExp(Expression):

    pass
class robochart_LambdaExp(Expression):

    pass
class QuantifierExpression:

    pass
class robochart_Exists(QuantifierExpression):

    def __init__(self, unique: bool):
        self.unique = unique
        
    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

class robochart_Forall(QuantifierExpression):

    pass
class robochart_Assignable(ABC):

    pass
class Statement:

    pass
class robochart_Assignment(Statement):

    pass
class robochart_Call(Statement):

    pass
class robochart_Skip(Statement):

    pass
class robochart_SendEvent(Statement):

    pass
class robochart_ParStmt(Statement):

    pass
class robochart_Wait(Statement):

    pass
class robochart_SeqStatement(Statement):

    pass
class robochart_IfStmt(Statement):

    pass
class robochart_TimedStatement(Statement):

    pass
class robochart_ConnectionNode(ABC):

    pass
class robochart_Connection:

    def __init__(self, async: bool, bidirec: bool, robochart_Connection143: "robochart_Event" = None, robochart_Connection: "robochart_ControllerDef" = None, robochart_Connection135: "robochart_ConnectionNode" = None, robochart_Connection137: "robochart_ConnectionNode" = None, robochart_Connection140: "robochart_Event" = None, robochart_Connection149: "robochart_RCModule" = None):
        self.async = async
        self.bidirec = bidirec
        self.robochart_Connection143 = robochart_Connection143
        self.robochart_Connection = robochart_Connection
        self.robochart_Connection135 = robochart_Connection135
        self.robochart_Connection137 = robochart_Connection137
        self.robochart_Connection140 = robochart_Connection140
        self.robochart_Connection149 = robochart_Connection149
        
    @property
    def async(self) -> bool:
        return self.__async

    @async.setter
    def async(self, async: bool):
        self.__async = async

    @property
    def bidirec(self) -> bool:
        return self.__bidirec

    @bidirec.setter
    def bidirec(self, bidirec: bool):
        self.__bidirec = bidirec

    @property
    def robochart_Connection135(self):
        return self.__robochart_Connection135

    @robochart_Connection135.setter
    def robochart_Connection135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection135", None)
        self.__robochart_Connection135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_ConnectionNode"):
                opp_val = getattr(old_value, "robochart_ConnectionNode", None)
                if opp_val == self:
                    setattr(old_value, "robochart_ConnectionNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_ConnectionNode"):
                opp_val = getattr(value, "robochart_ConnectionNode", None)
                setattr(value, "robochart_ConnectionNode", self)

    @property
    def robochart_Connection(self):
        return self.__robochart_Connection

    @robochart_Connection.setter
    def robochart_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection", None)
        self.__robochart_Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_ControllerDef133"):
                opp_val = getattr(old_value, "robochart_ControllerDef133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_ControllerDef133"):
                opp_val = getattr(value, "robochart_ControllerDef133", None)
                if opp_val is None:
                    setattr(value, "robochart_ControllerDef133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robochart_Connection143(self):
        return self.__robochart_Connection143

    @robochart_Connection143.setter
    def robochart_Connection143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection143", None)
        self.__robochart_Connection143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Event144"):
                opp_val = getattr(old_value, "robochart_Event144", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Event144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Event144"):
                opp_val = getattr(value, "robochart_Event144", None)
                setattr(value, "robochart_Event144", self)

    @property
    def robochart_Connection137(self):
        return self.__robochart_Connection137

    @robochart_Connection137.setter
    def robochart_Connection137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection137", None)
        self.__robochart_Connection137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_ConnectionNode138"):
                opp_val = getattr(old_value, "robochart_ConnectionNode138", None)
                if opp_val == self:
                    setattr(old_value, "robochart_ConnectionNode138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_ConnectionNode138"):
                opp_val = getattr(value, "robochart_ConnectionNode138", None)
                setattr(value, "robochart_ConnectionNode138", self)

    @property
    def robochart_Connection149(self):
        return self.__robochart_Connection149

    @robochart_Connection149.setter
    def robochart_Connection149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection149", None)
        self.__robochart_Connection149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_RCModule148"):
                opp_val = getattr(old_value, "robochart_RCModule148", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_RCModule148"):
                opp_val = getattr(value, "robochart_RCModule148", None)
                if opp_val is None:
                    setattr(value, "robochart_RCModule148", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robochart_Connection140(self):
        return self.__robochart_Connection140

    @robochart_Connection140.setter
    def robochart_Connection140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection140", None)
        self.__robochart_Connection140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Event141"):
                opp_val = getattr(old_value, "robochart_Event141", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Event141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Event141"):
                opp_val = getattr(value, "robochart_Event141", None)
                setattr(value, "robochart_Event141", self)

class Controller:

    pass
class robochart_ControllerRef(Controller):

    pass
class robochart_ClockReset(Statement):

    pass
class Action:

    pass
class robochart_DuringAction(Action):

    pass
class robochart_ExitAction(Action):

    pass
class robochart_EntryAction(Action):

    pass
class State:

    pass
class robochart_Final(State):

    pass
class robochart_Action(ABC):

    pass
class Junction:

    pass
class robochart_ProbabilisticJunction(Junction):

    pass
class robochart_Initial(Junction):

    pass
class Node:

    pass
class robochart_Junction(Node):

    pass
class robochart_Statement(ABC):

    pass
class robochart_Trigger:

    def __init__(self, _type: str, robochart_Trigger: "robochart_Transition" = None, robochart_Trigger106: "robochart_Event" = None, robochart_Trigger109: "robochart_Variable" = None, robochart_Trigger112: "robochart_Expression" = None, robochart_Trigger115: "robochart_Variable" = None, robochart_Trigger118: "robochart_Expression" = None, robochart_Trigger121: "robochart_Variable" = None, robochart_Trigger124: set["robochart_ClockReset"] = None, robochart_Trigger176: "robochart_SendEvent" = None):
        self._type = _type
        self.robochart_Trigger = robochart_Trigger
        self.robochart_Trigger106 = robochart_Trigger106
        self.robochart_Trigger109 = robochart_Trigger109
        self.robochart_Trigger112 = robochart_Trigger112
        self.robochart_Trigger115 = robochart_Trigger115
        self.robochart_Trigger118 = robochart_Trigger118
        self.robochart_Trigger121 = robochart_Trigger121
        self.robochart_Trigger124 = robochart_Trigger124 if robochart_Trigger124 is not None else set()
        self.robochart_Trigger176 = robochart_Trigger176
        
    @property
    def _type(self) -> str:
        return self.___type

    @_type.setter
    def _type(self, _type: str):
        self.___type = _type

    @property
    def robochart_Trigger176(self):
        return self.__robochart_Trigger176

    @robochart_Trigger176.setter
    def robochart_Trigger176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger176", None)
        self.__robochart_Trigger176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_SendEvent"):
                opp_val = getattr(old_value, "robochart_SendEvent", None)
                if opp_val == self:
                    setattr(old_value, "robochart_SendEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_SendEvent"):
                opp_val = getattr(value, "robochart_SendEvent", None)
                setattr(value, "robochart_SendEvent", self)

    @property
    def robochart_Trigger121(self):
        return self.__robochart_Trigger121

    @robochart_Trigger121.setter
    def robochart_Trigger121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger121", None)
        self.__robochart_Trigger121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Variable122"):
                opp_val = getattr(old_value, "robochart_Variable122", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Variable122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Variable122"):
                opp_val = getattr(value, "robochart_Variable122", None)
                setattr(value, "robochart_Variable122", self)

    @property
    def robochart_Trigger118(self):
        return self.__robochart_Trigger118

    @robochart_Trigger118.setter
    def robochart_Trigger118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger118", None)
        self.__robochart_Trigger118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Expression119"):
                opp_val = getattr(old_value, "robochart_Expression119", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Expression119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Expression119"):
                opp_val = getattr(value, "robochart_Expression119", None)
                setattr(value, "robochart_Expression119", self)

    @property
    def robochart_Trigger115(self):
        return self.__robochart_Trigger115

    @robochart_Trigger115.setter
    def robochart_Trigger115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger115", None)
        self.__robochart_Trigger115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Variable116"):
                opp_val = getattr(old_value, "robochart_Variable116", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Variable116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Variable116"):
                opp_val = getattr(value, "robochart_Variable116", None)
                setattr(value, "robochart_Variable116", self)

    @property
    def robochart_Trigger106(self):
        return self.__robochart_Trigger106

    @robochart_Trigger106.setter
    def robochart_Trigger106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger106", None)
        self.__robochart_Trigger106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Event107"):
                opp_val = getattr(old_value, "robochart_Event107", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Event107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Event107"):
                opp_val = getattr(value, "robochart_Event107", None)
                setattr(value, "robochart_Event107", self)

    @property
    def robochart_Trigger124(self):
        return self.__robochart_Trigger124

    @robochart_Trigger124.setter
    def robochart_Trigger124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger124", None)
        self.__robochart_Trigger124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robochart_ClockReset"):
                    opp_val = getattr(item, "robochart_ClockReset", None)
                    
                    if opp_val == self:
                        setattr(item, "robochart_ClockReset", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robochart_ClockReset"):
                    opp_val = getattr(item, "robochart_ClockReset", None)
                    
                    setattr(item, "robochart_ClockReset", self)
                    

    @property
    def robochart_Trigger109(self):
        return self.__robochart_Trigger109

    @robochart_Trigger109.setter
    def robochart_Trigger109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger109", None)
        self.__robochart_Trigger109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Variable110"):
                opp_val = getattr(old_value, "robochart_Variable110", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Variable110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Variable110"):
                opp_val = getattr(value, "robochart_Variable110", None)
                setattr(value, "robochart_Variable110", self)

    @property
    def robochart_Trigger112(self):
        return self.__robochart_Trigger112

    @robochart_Trigger112.setter
    def robochart_Trigger112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger112", None)
        self.__robochart_Trigger112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Expression113"):
                opp_val = getattr(old_value, "robochart_Expression113", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Expression113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Expression113"):
                opp_val = getattr(value, "robochart_Expression113", None)
                setattr(value, "robochart_Expression113", self)

    @property
    def robochart_Trigger(self):
        return self.__robochart_Trigger

    @robochart_Trigger.setter
    def robochart_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger", None)
        self.__robochart_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Transition93"):
                opp_val = getattr(old_value, "robochart_Transition93", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Transition93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Transition93"):
                opp_val = getattr(value, "robochart_Transition93", None)
                setattr(value, "robochart_Transition93", self)

class StateMachine:

    pass
class robochart_NodeContainer(ABC):

    pass
class NodeContainer:

    pass
class robochart_State(NodeContainer, Node):

    pass
class robochart_BasicContext(ABC):

    pass
class RoboticPlatform:

    pass
class Context:

    pass
class robochart_StateMachineBody(NodeContainer, Context):

    pass
class BasicContext:

    pass
class robochart_Context(BasicContext):

    pass
class Reference:

    pass
class robochart_StateMachineRef(StateMachine, Reference):

    pass
class robochart_RoboticPlatformRef(RoboticPlatform, Reference):

    pass
class robochart_Reference(ABC):

    pass
class StateMachineBody:

    pass
class OperationSig:

    pass
class Operation:

    pass
class robochart_OperationRef(Reference, Operation):

    pass
class ConnectionNode:

    pass
class Variable:

    pass
class robochart_Parameter(Variable):

    pass
class robochart_VariableList:

    def __init__(self, modifier: str, robochart_VariableList: set["robochart_Variable"] = None, robochart_VariableList59: "robochart_BasicContext" = None):
        self.modifier = modifier
        self.robochart_VariableList = robochart_VariableList if robochart_VariableList is not None else set()
        self.robochart_VariableList59 = robochart_VariableList59
        
    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def robochart_VariableList59(self):
        return self.__robochart_VariableList59

    @robochart_VariableList59.setter
    def robochart_VariableList59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_VariableList__robochart_VariableList59", None)
        self.__robochart_VariableList59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_BasicContext"):
                opp_val = getattr(old_value, "robochart_BasicContext", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_BasicContext"):
                opp_val = getattr(value, "robochart_BasicContext", None)
                if opp_val is None:
                    setattr(value, "robochart_BasicContext", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robochart_VariableList(self):
        return self.__robochart_VariableList

    @robochart_VariableList.setter
    def robochart_VariableList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_VariableList__robochart_VariableList", None)
        self.__robochart_VariableList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robochart_Variable"):
                    opp_val = getattr(item, "robochart_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "robochart_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robochart_Variable"):
                    opp_val = getattr(item, "robochart_Variable", None)
                    
                    setattr(item, "robochart_Variable", self)
                    

class SetType:

    pass
class robochart_SeqType(SetType):

    pass
class robochart_Expression(ABC):

    pass
class Type:

    pass
class robochart_AnyType(Type):

    def __init__(self, identifier: str):
        self.identifier = identifier
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

class robochart_TypeRef(Type):

    pass
class robochart_VectorType(Type):

    def __init__(self, size: int, robochart_VectorType: "robochart_Type" = None):
        self.size = size
        self.robochart_VectorType = robochart_VectorType
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def robochart_VectorType(self):
        return self.__robochart_VectorType

    @robochart_VectorType.setter
    def robochart_VectorType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_VectorType__robochart_VectorType", None)
        self.__robochart_VectorType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Type318"):
                opp_val = getattr(old_value, "robochart_Type318", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Type318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Type318"):
                opp_val = getattr(value, "robochart_Type318", None)
                setattr(value, "robochart_Type318", self)

class robochart_MatrixType(Type):

    def __init__(self, rows: int, columns: int, robochart_MatrixType: "robochart_Type" = None):
        self.rows = rows
        self.columns = columns
        self.robochart_MatrixType = robochart_MatrixType
        
    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, rows: int):
        self.__rows = rows

    @property
    def robochart_MatrixType(self):
        return self.__robochart_MatrixType

    @robochart_MatrixType.setter
    def robochart_MatrixType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_MatrixType__robochart_MatrixType", None)
        self.__robochart_MatrixType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Type320"):
                opp_val = getattr(old_value, "robochart_Type320", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Type320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Type320"):
                opp_val = getattr(value, "robochart_Type320", None)
                setattr(value, "robochart_Type320", self)

class robochart_ProductType(Type):

    pass
class robochart_SetType(Type):

    pass
class RelationType:

    pass
class robochart_FunctionType(RelationType):

    pass
class robochart_RelationType(Type):

    pass
class NamedExpression:

    pass
class Member:

    pass
class robochart_Field(Member, NamedExpression):

    pass
class TypeDecl:

    pass
class robochart_NameType(TypeDecl):

    pass
class robochart_RecordType(TypeDecl):

    pass
class robochart_PrimitiveType(TypeDecl):

    pass
class robochart_Literal(TypeDecl, NamedExpression):

    pass
class robochart_Enumeration(TypeDecl):

    pass
class TypedNamedElement:

    pass
class robochart_Variable(Member, NamedExpression, TypedNamedElement):

    def __init__(self, modifier: str, robochart_Variable: "robochart_VariableList" = None, robochart_Variable37: "robochart_Expression" = None, robochart_Variable110: "robochart_Trigger" = None, robochart_Variable116: "robochart_Trigger" = None, robochart_Variable122: "robochart_Trigger" = None, robochart_Variable204: "robochart_QuantifierExpression" = None, robochart_Variable212: "robochart_LambdaExp" = None, robochart_Variable250: "robochart_VarExp" = None, robochart_Variable274: "robochart_SetComp" = None, robochart_Variable309: "robochart_VarRef" = None):
        self.modifier = modifier
        self.robochart_Variable = robochart_Variable
        self.robochart_Variable37 = robochart_Variable37
        self.robochart_Variable110 = robochart_Variable110
        self.robochart_Variable116 = robochart_Variable116
        self.robochart_Variable122 = robochart_Variable122
        self.robochart_Variable204 = robochart_Variable204
        self.robochart_Variable212 = robochart_Variable212
        self.robochart_Variable250 = robochart_Variable250
        self.robochart_Variable274 = robochart_Variable274
        self.robochart_Variable309 = robochart_Variable309
        
    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def robochart_Variable212(self):
        return self.__robochart_Variable212

    @robochart_Variable212.setter
    def robochart_Variable212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable212", None)
        self.__robochart_Variable212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_LambdaExp"):
                opp_val = getattr(old_value, "robochart_LambdaExp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_LambdaExp"):
                opp_val = getattr(value, "robochart_LambdaExp", None)
                if opp_val is None:
                    setattr(value, "robochart_LambdaExp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robochart_Variable122(self):
        return self.__robochart_Variable122

    @robochart_Variable122.setter
    def robochart_Variable122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable122", None)
        self.__robochart_Variable122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Trigger121"):
                opp_val = getattr(old_value, "robochart_Trigger121", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Trigger121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Trigger121"):
                opp_val = getattr(value, "robochart_Trigger121", None)
                setattr(value, "robochart_Trigger121", self)

    @property
    def robochart_Variable110(self):
        return self.__robochart_Variable110

    @robochart_Variable110.setter
    def robochart_Variable110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable110", None)
        self.__robochart_Variable110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Trigger109"):
                opp_val = getattr(old_value, "robochart_Trigger109", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Trigger109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Trigger109"):
                opp_val = getattr(value, "robochart_Trigger109", None)
                setattr(value, "robochart_Trigger109", self)

    @property
    def robochart_Variable204(self):
        return self.__robochart_Variable204

    @robochart_Variable204.setter
    def robochart_Variable204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable204", None)
        self.__robochart_Variable204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_QuantifierExpression"):
                opp_val = getattr(old_value, "robochart_QuantifierExpression", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_QuantifierExpression"):
                opp_val = getattr(value, "robochart_QuantifierExpression", None)
                if opp_val is None:
                    setattr(value, "robochart_QuantifierExpression", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robochart_Variable(self):
        return self.__robochart_Variable

    @robochart_Variable.setter
    def robochart_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable", None)
        self.__robochart_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_VariableList"):
                opp_val = getattr(old_value, "robochart_VariableList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_VariableList"):
                opp_val = getattr(value, "robochart_VariableList", None)
                if opp_val is None:
                    setattr(value, "robochart_VariableList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robochart_Variable274(self):
        return self.__robochart_Variable274

    @robochart_Variable274.setter
    def robochart_Variable274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable274", None)
        self.__robochart_Variable274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_SetComp"):
                opp_val = getattr(old_value, "robochart_SetComp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_SetComp"):
                opp_val = getattr(value, "robochart_SetComp", None)
                if opp_val is None:
                    setattr(value, "robochart_SetComp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robochart_Variable309(self):
        return self.__robochart_Variable309

    @robochart_Variable309.setter
    def robochart_Variable309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable309", None)
        self.__robochart_Variable309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_VarRef"):
                opp_val = getattr(old_value, "robochart_VarRef", None)
                if opp_val == self:
                    setattr(old_value, "robochart_VarRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_VarRef"):
                opp_val = getattr(value, "robochart_VarRef", None)
                setattr(value, "robochart_VarRef", self)

    @property
    def robochart_Variable37(self):
        return self.__robochart_Variable37

    @robochart_Variable37.setter
    def robochart_Variable37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable37", None)
        self.__robochart_Variable37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Expression"):
                opp_val = getattr(old_value, "robochart_Expression", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Expression"):
                opp_val = getattr(value, "robochart_Expression", None)
                setattr(value, "robochart_Expression", self)

    @property
    def robochart_Variable250(self):
        return self.__robochart_Variable250

    @robochart_Variable250.setter
    def robochart_Variable250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable250", None)
        self.__robochart_Variable250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_VarExp"):
                opp_val = getattr(old_value, "robochart_VarExp", None)
                if opp_val == self:
                    setattr(old_value, "robochart_VarExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_VarExp"):
                opp_val = getattr(value, "robochart_VarExp", None)
                setattr(value, "robochart_VarExp", self)

    @property
    def robochart_Variable116(self):
        return self.__robochart_Variable116

    @robochart_Variable116.setter
    def robochart_Variable116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable116", None)
        self.__robochart_Variable116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Trigger115"):
                opp_val = getattr(old_value, "robochart_Trigger115", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Trigger115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Trigger115"):
                opp_val = getattr(value, "robochart_Trigger115", None)
                setattr(value, "robochart_Trigger115", self)

class robochart_Member(TypedNamedElement):

    pass
class robochart_Type(ABC):

    pass
class robochart_OperationDef(StateMachineBody, OperationSig, Operation):

    pass
class robochart_ControllerDef(Context, Controller):

    pass
class robochart_StateMachineDef(StateMachineBody, StateMachine):

    pass
class NamedElement:

    pass
class robochart_OperationSig(NamedElement):

    def __init__(self, terminates: bool, robochart_OperationSig: set["robochart_Parameter"] = None, robochart_OperationSig51: set["robochart_Expression"] = None, robochart_OperationSig54: set["robochart_Expression"] = None, robochart_OperationSig62: "robochart_BasicContext" = None, robochart_OperationSig182: "robochart_Call" = None):
        self.terminates = terminates
        self.robochart_OperationSig = robochart_OperationSig if robochart_OperationSig is not None else set()
        self.robochart_OperationSig51 = robochart_OperationSig51 if robochart_OperationSig51 is not None else set()
        self.robochart_OperationSig54 = robochart_OperationSig54 if robochart_OperationSig54 is not None else set()
        self.robochart_OperationSig62 = robochart_OperationSig62
        self.robochart_OperationSig182 = robochart_OperationSig182
        
    @property
    def terminates(self) -> bool:
        return self.__terminates

    @terminates.setter
    def terminates(self, terminates: bool):
        self.__terminates = terminates

    @property
    def robochart_OperationSig62(self):
        return self.__robochart_OperationSig62

    @robochart_OperationSig62.setter
    def robochart_OperationSig62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_OperationSig__robochart_OperationSig62", None)
        self.__robochart_OperationSig62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_BasicContext61"):
                opp_val = getattr(old_value, "robochart_BasicContext61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_BasicContext61"):
                opp_val = getattr(value, "robochart_BasicContext61", None)
                if opp_val is None:
                    setattr(value, "robochart_BasicContext61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robochart_OperationSig51(self):
        return self.__robochart_OperationSig51

    @robochart_OperationSig51.setter
    def robochart_OperationSig51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_OperationSig__robochart_OperationSig51", None)
        self.__robochart_OperationSig51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robochart_Expression52"):
                    opp_val = getattr(item, "robochart_Expression52", None)
                    
                    if opp_val == self:
                        setattr(item, "robochart_Expression52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robochart_Expression52"):
                    opp_val = getattr(item, "robochart_Expression52", None)
                    
                    setattr(item, "robochart_Expression52", self)
                    

    @property
    def robochart_OperationSig182(self):
        return self.__robochart_OperationSig182

    @robochart_OperationSig182.setter
    def robochart_OperationSig182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_OperationSig__robochart_OperationSig182", None)
        self.__robochart_OperationSig182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Call"):
                opp_val = getattr(old_value, "robochart_Call", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Call", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Call"):
                opp_val = getattr(value, "robochart_Call", None)
                setattr(value, "robochart_Call", self)

    @property
    def robochart_OperationSig(self):
        return self.__robochart_OperationSig

    @robochart_OperationSig.setter
    def robochart_OperationSig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_OperationSig__robochart_OperationSig", None)
        self.__robochart_OperationSig = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robochart_Parameter49"):
                    opp_val = getattr(item, "robochart_Parameter49", None)
                    
                    if opp_val == self:
                        setattr(item, "robochart_Parameter49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robochart_Parameter49"):
                    opp_val = getattr(item, "robochart_Parameter49", None)
                    
                    setattr(item, "robochart_Parameter49", self)
                    

    @property
    def robochart_OperationSig54(self):
        return self.__robochart_OperationSig54

    @robochart_OperationSig54.setter
    def robochart_OperationSig54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_OperationSig__robochart_OperationSig54", None)
        self.__robochart_OperationSig54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robochart_Expression55"):
                    opp_val = getattr(item, "robochart_Expression55", None)
                    
                    if opp_val == self:
                        setattr(item, "robochart_Expression55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robochart_Expression55"):
                    opp_val = getattr(item, "robochart_Expression55", None)
                    
                    setattr(item, "robochart_Expression55", self)
                    

class robochart_Operation(NamedElement, ConnectionNode):

    pass
class robochart_TypedNamedElement(NamedElement):

    pass
class robochart_StateMachine(NamedElement, ConnectionNode):

    pass
class robochart_Clock(NamedElement):

    pass
class robochart_WaitingCondition(NamedElement):

    pass
class robochart_Transition(NamedElement):

    pass
class robochart_RoboticPlatform(NamedElement, ConnectionNode):

    pass
class robochart_Declaration(NamedElement, NamedExpression):

    pass
class robochart_Node(NamedElement):

    pass
class robochart_Controller(NamedElement, ConnectionNode):

    pass
class robochart_Event(NamedElement):

    def __init__(self, broadcast: bool, robochart_Event: "robochart_Type" = None, robochart_Event65: "robochart_BasicContext" = None, robochart_Event107: "robochart_Trigger" = None, robochart_Event144: "robochart_Connection" = None, robochart_Event141: "robochart_Connection" = None):
        self.broadcast = broadcast
        self.robochart_Event = robochart_Event
        self.robochart_Event65 = robochart_Event65
        self.robochart_Event107 = robochart_Event107
        self.robochart_Event144 = robochart_Event144
        self.robochart_Event141 = robochart_Event141
        
    @property
    def broadcast(self) -> bool:
        return self.__broadcast

    @broadcast.setter
    def broadcast(self, broadcast: bool):
        self.__broadcast = broadcast

    @property
    def robochart_Event(self):
        return self.__robochart_Event

    @robochart_Event.setter
    def robochart_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Event__robochart_Event", None)
        self.__robochart_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Type39"):
                opp_val = getattr(old_value, "robochart_Type39", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Type39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Type39"):
                opp_val = getattr(value, "robochart_Type39", None)
                setattr(value, "robochart_Type39", self)

    @property
    def robochart_Event141(self):
        return self.__robochart_Event141

    @robochart_Event141.setter
    def robochart_Event141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Event__robochart_Event141", None)
        self.__robochart_Event141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Connection140"):
                opp_val = getattr(old_value, "robochart_Connection140", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Connection140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Connection140"):
                opp_val = getattr(value, "robochart_Connection140", None)
                setattr(value, "robochart_Connection140", self)

    @property
    def robochart_Event144(self):
        return self.__robochart_Event144

    @robochart_Event144.setter
    def robochart_Event144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Event__robochart_Event144", None)
        self.__robochart_Event144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Connection143"):
                opp_val = getattr(old_value, "robochart_Connection143", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Connection143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Connection143"):
                opp_val = getattr(value, "robochart_Connection143", None)
                setattr(value, "robochart_Connection143", self)

    @property
    def robochart_Event65(self):
        return self.__robochart_Event65

    @robochart_Event65.setter
    def robochart_Event65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Event__robochart_Event65", None)
        self.__robochart_Event65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_BasicContext64"):
                opp_val = getattr(old_value, "robochart_BasicContext64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_BasicContext64"):
                opp_val = getattr(value, "robochart_BasicContext64", None)
                if opp_val is None:
                    setattr(value, "robochart_BasicContext64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robochart_Event107(self):
        return self.__robochart_Event107

    @robochart_Event107.setter
    def robochart_Event107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Event__robochart_Event107", None)
        self.__robochart_Event107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Trigger106"):
                opp_val = getattr(old_value, "robochart_Trigger106", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Trigger106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Trigger106"):
                opp_val = getattr(value, "robochart_Trigger106", None)
                setattr(value, "robochart_Trigger106", self)

class robochart_RCModule(NamedElement):

    pass
class robochart_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class robochart_Function(NamedExpression, TypedNamedElement):

    pass
class robochart_Import:

    def __init__(self, importedNamespace: str, robochart_Import: "robochart_BasicPackage" = None):
        self.importedNamespace = importedNamespace
        self.robochart_Import = robochart_Import
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace

    @property
    def robochart_Import(self):
        return self.__robochart_Import

    @robochart_Import.setter
    def robochart_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Import__robochart_Import", None)
        self.__robochart_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_BasicPackage"):
                opp_val = getattr(old_value, "robochart_BasicPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_BasicPackage"):
                opp_val = getattr(value, "robochart_BasicPackage", None)
                if opp_val is None:
                    setattr(value, "robochart_BasicPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class robochart_BasicPackage:

    def __init__(self, name: str, robochart_BasicPackage: set["robochart_Import"] = None):
        self.name = name
        self.robochart_BasicPackage = robochart_BasicPackage if robochart_BasicPackage is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robochart_BasicPackage(self):
        return self.__robochart_BasicPackage

    @robochart_BasicPackage.setter
    def robochart_BasicPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_BasicPackage__robochart_BasicPackage", None)
        self.__robochart_BasicPackage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robochart_Import"):
                    opp_val = getattr(item, "robochart_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "robochart_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robochart_Import"):
                    opp_val = getattr(item, "robochart_Import", None)
                    
                    setattr(item, "robochart_Import", self)
                    

class robochart_TypeDecl(NamedElement):

    pass
class robochart_RoboticPlatformDef(Context, RoboticPlatform):

    pass
class robochart_Interface(NamedElement, BasicContext):

    pass
class BasicPackage:

    pass
class robochart_RCPackage(BasicPackage):

    pass