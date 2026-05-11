from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariableModifier(Enum):
    VAR = "VAR"
    CONST = "CONST"
class TriggerType(Enum):
    SIMPLE = "SIMPLE"
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    SYNC = "SYNC"
    EMPTY = "EMPTY"


############################################
# Definition of Classes
############################################

class robochart_ConnectionNode(ABC):

    pass
class robochart_Connection:

    def __init__(self, async_: bool, bidirec: bool, robochart_Connection141: "robochart_Event" = None, robochart_Connection144: "robochart_Event" = None, robochart_Connection150: "robochart_RCModule" = None, robochart_Connection: "robochart_ControllerDef" = None, robochart_Connection136: "robochart_ConnectionNode" = None, robochart_Connection138: "robochart_ConnectionNode" = None):
        self.async_ = async_
        self.bidirec = bidirec
        self.robochart_Connection141 = robochart_Connection141
        self.robochart_Connection144 = robochart_Connection144
        self.robochart_Connection150 = robochart_Connection150
        self.robochart_Connection = robochart_Connection
        self.robochart_Connection136 = robochart_Connection136
        self.robochart_Connection138 = robochart_Connection138
        
        pass
    @property
    def bidirec(self):
        return self.__bidirec

    @bidirec.setter
    def bidirec(self, bidirec: bool):
        self.__bidirec = bidirec


    @property
    def async_(self):
        return self.__async_

    @async_.setter
    def async_(self, async_: bool):
        self.__async_ = async_


    @property
    def robochart_Connection144(self):
        return self.__robochart_Connection144

    @robochart_Connection144.setter
    def robochart_Connection144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection144", None)
        self.__robochart_Connection144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Event145"):
                opp_val = getattr(old_value, "robochart_Event145", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Event145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Event145"):
                opp_val = getattr(value, "robochart_Event145", None)
                setattr(value, "robochart_Event145", self)

    @property
    def robochart_Connection138(self):
        return self.__robochart_Connection138

    @robochart_Connection138.setter
    def robochart_Connection138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection138", None)
        self.__robochart_Connection138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_ConnectionNode139"):
                opp_val = getattr(old_value, "robochart_ConnectionNode139", None)
                if opp_val == self:
                    setattr(old_value, "robochart_ConnectionNode139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_ConnectionNode139"):
                opp_val = getattr(value, "robochart_ConnectionNode139", None)
                setattr(value, "robochart_ConnectionNode139", self)

    @property
    def robochart_Connection141(self):
        return self.__robochart_Connection141

    @robochart_Connection141.setter
    def robochart_Connection141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection141", None)
        self.__robochart_Connection141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Event142"):
                opp_val = getattr(old_value, "robochart_Event142", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Event142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Event142"):
                opp_val = getattr(value, "robochart_Event142", None)
                setattr(value, "robochart_Event142", self)

    @property
    def robochart_Connection136(self):
        return self.__robochart_Connection136

    @robochart_Connection136.setter
    def robochart_Connection136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection136", None)
        self.__robochart_Connection136 = value
        
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
    def robochart_Connection150(self):
        return self.__robochart_Connection150

    @robochart_Connection150.setter
    def robochart_Connection150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Connection__robochart_Connection150", None)
        self.__robochart_Connection150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_RCModule149"):
                opp_val = getattr(old_value, "robochart_RCModule149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_RCModule149"):
                opp_val = getattr(value, "robochart_RCModule149", None)
                if opp_val is None:
                    setattr(value, "robochart_RCModule149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "robochart_ControllerDef134"):
                opp_val = getattr(old_value, "robochart_ControllerDef134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_ControllerDef134"):
                opp_val = getattr(value, "robochart_ControllerDef134", None)
                if opp_val is None:
                    setattr(value, "robochart_ControllerDef134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Controller:

    pass
class Statement:

    pass
class robochart_Wait(Statement):

    pass
class robochart_Call(Statement):

    pass
class robochart_ParStmt(Statement):

    pass
class robochart_SeqStatement(Statement):

    pass
class robochart_TimedStatement(Statement):

    pass
class robochart_ControllerRef(Controller):

    pass
class robochart_Statement(ABC):

    pass
class robochart_Trigger:

    def __init__(self, _type: str, robochart_Trigger107: "robochart_Event" = None, robochart_Trigger110: "robochart_Variable" = None, robochart_Trigger113: "robochart_Expression" = None, robochart_Trigger116: "robochart_Variable" = None, robochart_Trigger119: "robochart_Expression" = None, robochart_Trigger122: "robochart_Variable" = None, robochart_Trigger125: set["robochart_ClockReset"] = None, robochart_Trigger: "robochart_Transition" = None, robochart_Trigger177: "robochart_SendEvent" = None):
        self._type = _type
        self.robochart_Trigger107 = robochart_Trigger107
        self.robochart_Trigger110 = robochart_Trigger110
        self.robochart_Trigger113 = robochart_Trigger113
        self.robochart_Trigger116 = robochart_Trigger116
        self.robochart_Trigger119 = robochart_Trigger119
        self.robochart_Trigger122 = robochart_Trigger122
        self.robochart_Trigger125 = robochart_Trigger125 if robochart_Trigger125 is not None else set()
        self.robochart_Trigger = robochart_Trigger
        self.robochart_Trigger177 = robochart_Trigger177
        
        pass
    @property
    def _type(self):
        return self.___type

    @_type.setter
    def _type(self, _type: str):
        self.___type = _type


    @property
    def robochart_Trigger122(self):
        return self.__robochart_Trigger122

    @robochart_Trigger122.setter
    def robochart_Trigger122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger122", None)
        self.__robochart_Trigger122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Variable123"):
                opp_val = getattr(old_value, "robochart_Variable123", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Variable123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Variable123"):
                opp_val = getattr(value, "robochart_Variable123", None)
                setattr(value, "robochart_Variable123", self)

    @property
    def robochart_Trigger107(self):
        return self.__robochart_Trigger107

    @robochart_Trigger107.setter
    def robochart_Trigger107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger107", None)
        self.__robochart_Trigger107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Event108"):
                opp_val = getattr(old_value, "robochart_Event108", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Event108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Event108"):
                opp_val = getattr(value, "robochart_Event108", None)
                setattr(value, "robochart_Event108", self)

    @property
    def robochart_Trigger125(self):
        return self.__robochart_Trigger125

    @robochart_Trigger125.setter
    def robochart_Trigger125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger125", None)
        self.__robochart_Trigger125 = value if value is not None else set()
        
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
    def robochart_Trigger113(self):
        return self.__robochart_Trigger113

    @robochart_Trigger113.setter
    def robochart_Trigger113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger113", None)
        self.__robochart_Trigger113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Expression114"):
                opp_val = getattr(old_value, "robochart_Expression114", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Expression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Expression114"):
                opp_val = getattr(value, "robochart_Expression114", None)
                setattr(value, "robochart_Expression114", self)

    @property
    def robochart_Trigger119(self):
        return self.__robochart_Trigger119

    @robochart_Trigger119.setter
    def robochart_Trigger119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger119", None)
        self.__robochart_Trigger119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Expression120"):
                opp_val = getattr(old_value, "robochart_Expression120", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Expression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Expression120"):
                opp_val = getattr(value, "robochart_Expression120", None)
                setattr(value, "robochart_Expression120", self)

    @property
    def robochart_Trigger177(self):
        return self.__robochart_Trigger177

    @robochart_Trigger177.setter
    def robochart_Trigger177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger177", None)
        self.__robochart_Trigger177 = value
        
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
    def robochart_Trigger110(self):
        return self.__robochart_Trigger110

    @robochart_Trigger110.setter
    def robochart_Trigger110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger110", None)
        self.__robochart_Trigger110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Variable111"):
                opp_val = getattr(old_value, "robochart_Variable111", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Variable111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Variable111"):
                opp_val = getattr(value, "robochart_Variable111", None)
                setattr(value, "robochart_Variable111", self)

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
            if hasattr(old_value, "robochart_Transition94"):
                opp_val = getattr(old_value, "robochart_Transition94", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Transition94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Transition94"):
                opp_val = getattr(value, "robochart_Transition94", None)
                setattr(value, "robochart_Transition94", self)

    @property
    def robochart_Trigger116(self):
        return self.__robochart_Trigger116

    @robochart_Trigger116.setter
    def robochart_Trigger116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Trigger__robochart_Trigger116", None)
        self.__robochart_Trigger116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Variable117"):
                opp_val = getattr(old_value, "robochart_Variable117", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Variable117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Variable117"):
                opp_val = getattr(value, "robochart_Variable117", None)
                setattr(value, "robochart_Variable117", self)

class State:

    pass
class robochart_Final(State):

    pass
class Action:

    pass
class robochart_DuringAction(Action):

    pass
class robochart_ExitAction(Action):

    pass
class robochart_EntryAction(Action):

    pass
class robochart_ClockReset(Statement):

    pass
class RoboticPlatform:

    pass
class Context:

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
class robochart_NodeContainer(ABC):

    pass
class NodeContainer:

    pass
class robochart_State(NodeContainer, Node):

    pass
class robochart_StateMachineBody(NodeContainer, Context):

    pass
class StateMachine:

    pass
class Variable:

    pass
class robochart_Parameter(Variable):

    pass
class robochart_BasicContext(ABC):

    pass
class BasicContext:

    pass
class robochart_Context(BasicContext):

    pass
class Reference:

    pass
class robochart_RoboticPlatformRef(RoboticPlatform, Reference):

    pass
class robochart_StateMachineRef(Reference, StateMachine):

    pass
class robochart_Reference(ABC):

    pass
class StateMachineBody:

    pass
class OperationSig:

    pass
class Operation:

    pass
class robochart_OperationRef(Operation, Reference):

    pass
class ConnectionNode:

    pass
class Type:

    pass
class robochart_RelationType(Type):

    pass
class robochart_ProductType(Type):

    pass
class robochart_Expression(ABC):

    pass
class robochart_VariableList:

    def __init__(self, modifier: str, robochart_VariableList: set["robochart_Variable"] = None, robochart_VariableList59: "robochart_BasicContext" = None):
        self.modifier = modifier
        self.robochart_VariableList = robochart_VariableList if robochart_VariableList is not None else set()
        self.robochart_VariableList59 = robochart_VariableList59
        
        pass
    @property
    def modifier(self):
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
                    

class robochart_AnyType(Type):

    def __init__(self, identifier: str):
        self.identifier = identifier
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


class robochart_TypeRef(Type):

    pass
class SetType:

    pass
class robochart_SeqType(SetType):

    pass
class robochart_SetType(Type):

    pass
class robochart_VectorType(Type):

    def __init__(self, size: int, robochart_VectorType: "robochart_Type" = None):
        self.size = size
        self.robochart_VectorType = robochart_VectorType
        
        pass
    @property
    def size(self):
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
            if hasattr(old_value, "robochart_Type319"):
                opp_val = getattr(old_value, "robochart_Type319", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Type319", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Type319"):
                opp_val = getattr(value, "robochart_Type319", None)
                setattr(value, "robochart_Type319", self)

class robochart_MatrixType(Type):

    def __init__(self, rows: int, columns: int, robochart_MatrixType: "robochart_Type" = None):
        self.rows = rows
        self.columns = columns
        self.robochart_MatrixType = robochart_MatrixType
        
        pass
    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns


    @property
    def rows(self):
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
            if hasattr(old_value, "robochart_Type321"):
                opp_val = getattr(old_value, "robochart_Type321", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Type321", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Type321"):
                opp_val = getattr(value, "robochart_Type321", None)
                setattr(value, "robochart_Type321", self)

class Assignable:

    pass
class robochart_ArrayAssignable(Assignable):

    pass
class robochart_VarRef(Assignable):

    pass
class robochart_VarSelection(Assignable):

    pass
class robochart_NamedExpression(ABC):

    pass
class BinaryExpression:

    pass
class robochart_LessOrEqual(BinaryExpression):

    pass
class robochart_GreaterThan(BinaryExpression):

    pass
class robochart_Equals(BinaryExpression):

    pass
class robochart_Or(BinaryExpression):

    pass
class robochart_Plus(BinaryExpression):

    pass
class robochart_LessThan(BinaryExpression):

    pass
class robochart_Mult(BinaryExpression):

    pass
class robochart_Different(BinaryExpression):

    pass
class robochart_Modulus(BinaryExpression):

    pass
class robochart_Cat(BinaryExpression):

    pass
class robochart_Minus(BinaryExpression):

    pass
class robochart_Div(BinaryExpression):

    pass
class robochart_GreaterOrEqual(BinaryExpression):

    pass
class robochart_Implies(BinaryExpression):

    pass
class robochart_And(BinaryExpression):

    pass
class robochart_Iff(BinaryExpression):

    pass
class LambdaExp:

    pass
class robochart_DefiniteDescription(LambdaExp):

    pass
class QuantifierExpression:

    pass
class robochart_Exists(QuantifierExpression):

    def __init__(self, unique: bool):
        self.unique = unique
        
        pass
    @property
    def unique(self):
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique


class robochart_Forall(QuantifierExpression):

    pass
class robochart_SendEvent(Statement):

    pass
class robochart_Assignable(ABC):

    pass
class robochart_Assignment(Statement):

    pass
class robochart_IfStmt(Statement):

    pass
class robochart_Skip(Statement):

    pass
class Expression:

    pass
class robochart_IfExpression(Expression):

    pass
class robochart_ElseExp(Expression):

    pass
class robochart_Not(Expression):

    pass
class robochart_IdExp(Expression):

    pass
class robochart_VarExp(Expression):

    pass
class robochart_IsExp(Expression):

    pass
class robochart_SetRange(Expression):

    pass
class robochart_ArrayExp(Expression):

    pass
class robochart_BooleanExp(Expression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class robochart_FloatExp(Expression):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class robochart_TupleExp(Expression):

    pass
class robochart_SetExp(Expression):

    pass
class robochart_WaitingConditionRef(Expression):

    pass
class robochart_LetExpression(Expression):

    pass
class robochart_InExp(Expression):

    pass
class robochart_AsExp(Expression):

    pass
class robochart_ResultExp(Expression):

    pass
class robochart_SeqExp(Expression):

    pass
class robochart_FromExp(Expression):

    pass
class robochart_Selection(Expression):

    pass
class robochart_BinaryExpression(Expression):

    pass
class robochart_RefExp(Expression):

    pass
class robochart_StringExp(Expression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class robochart_Neg(Expression):

    pass
class robochart_IntegerExp(Expression):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class robochart_QuantifierExpression(Expression):

    pass
class robochart_CallExp(Expression):

    pass
class robochart_TypeExp(Expression):

    pass
class robochart_ToExp(Expression):

    pass
class robochart_ClockExp(Expression):

    pass
class robochart_StateClockExp(Expression):

    pass
class robochart_EnumExp(Expression):

    pass
class robochart_RangeExp(Expression):

    def __init__(self, linterval: str, rinterval: str, robochart_RangeExp: "robochart_Expression" = None, robochart_RangeExp292: "robochart_Expression" = None):
        self.linterval = linterval
        self.rinterval = rinterval
        self.robochart_RangeExp = robochart_RangeExp
        self.robochart_RangeExp292 = robochart_RangeExp292
        
        pass
    @property
    def rinterval(self):
        return self.__rinterval

    @rinterval.setter
    def rinterval(self, rinterval: str):
        self.__rinterval = rinterval


    @property
    def linterval(self):
        return self.__linterval

    @linterval.setter
    def linterval(self, linterval: str):
        self.__linterval = linterval


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
            if hasattr(old_value, "robochart_Expression290"):
                opp_val = getattr(old_value, "robochart_Expression290", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Expression290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Expression290"):
                opp_val = getattr(value, "robochart_Expression290", None)
                setattr(value, "robochart_Expression290", self)

    @property
    def robochart_RangeExp292(self):
        return self.__robochart_RangeExp292

    @robochart_RangeExp292.setter
    def robochart_RangeExp292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_RangeExp__robochart_RangeExp292", None)
        self.__robochart_RangeExp292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Expression293"):
                opp_val = getattr(old_value, "robochart_Expression293", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Expression293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Expression293"):
                opp_val = getattr(value, "robochart_Expression293", None)
                setattr(value, "robochart_Expression293", self)

class robochart_ParExp(Expression):

    pass
class robochart_LambdaExp(Expression):

    pass
class robochart_SetComp(Expression):

    pass
class RelationType:

    pass
class robochart_FunctionType(RelationType):

    pass
class NamedElement:

    pass
class robochart_Controller(ConnectionNode, NamedElement):

    pass
class robochart_Clock(NamedElement):

    pass
class robochart_Transition(NamedElement):

    pass
class robochart_Event(NamedElement):

    def __init__(self, broadcast: bool, robochart_Event65: "robochart_BasicContext" = None, robochart_Event108: "robochart_Trigger" = None, robochart_Event142: "robochart_Connection" = None, robochart_Event145: "robochart_Connection" = None, robochart_Event: "robochart_Type" = None):
        self.broadcast = broadcast
        self.robochart_Event65 = robochart_Event65
        self.robochart_Event108 = robochart_Event108
        self.robochart_Event142 = robochart_Event142
        self.robochart_Event145 = robochart_Event145
        self.robochart_Event = robochart_Event
        
        pass
    @property
    def broadcast(self):
        return self.__broadcast

    @broadcast.setter
    def broadcast(self, broadcast: bool):
        self.__broadcast = broadcast


    @property
    def robochart_Event142(self):
        return self.__robochart_Event142

    @robochart_Event142.setter
    def robochart_Event142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Event__robochart_Event142", None)
        self.__robochart_Event142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Connection141"):
                opp_val = getattr(old_value, "robochart_Connection141", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Connection141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Connection141"):
                opp_val = getattr(value, "robochart_Connection141", None)
                setattr(value, "robochart_Connection141", self)

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
    def robochart_Event108(self):
        return self.__robochart_Event108

    @robochart_Event108.setter
    def robochart_Event108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Event__robochart_Event108", None)
        self.__robochart_Event108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Trigger107"):
                opp_val = getattr(old_value, "robochart_Trigger107", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Trigger107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Trigger107"):
                opp_val = getattr(value, "robochart_Trigger107", None)
                setattr(value, "robochart_Trigger107", self)

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
    def robochart_Event145(self):
        return self.__robochart_Event145

    @robochart_Event145.setter
    def robochart_Event145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Event__robochart_Event145", None)
        self.__robochart_Event145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Connection144"):
                opp_val = getattr(old_value, "robochart_Connection144", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Connection144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Connection144"):
                opp_val = getattr(value, "robochart_Connection144", None)
                setattr(value, "robochart_Connection144", self)

class robochart_WaitingCondition(NamedElement):

    pass
class robochart_Node(NamedElement):

    pass
class robochart_Operation(ConnectionNode, NamedElement):

    pass
class robochart_StateMachine(ConnectionNode, NamedElement):

    pass
class robochart_OperationSig(NamedElement):

    def __init__(self, terminates: bool, robochart_OperationSig: set["robochart_Parameter"] = None, robochart_OperationSig51: set["robochart_Expression"] = None, robochart_OperationSig54: set["robochart_Expression"] = None, robochart_OperationSig62: "robochart_BasicContext" = None, robochart_OperationSig183: "robochart_Call" = None):
        self.terminates = terminates
        self.robochart_OperationSig = robochart_OperationSig if robochart_OperationSig is not None else set()
        self.robochart_OperationSig51 = robochart_OperationSig51 if robochart_OperationSig51 is not None else set()
        self.robochart_OperationSig54 = robochart_OperationSig54 if robochart_OperationSig54 is not None else set()
        self.robochart_OperationSig62 = robochart_OperationSig62
        self.robochart_OperationSig183 = robochart_OperationSig183
        
        pass
    @property
    def terminates(self):
        return self.__terminates

    @terminates.setter
    def terminates(self, terminates: bool):
        self.__terminates = terminates


    @property
    def robochart_OperationSig183(self):
        return self.__robochart_OperationSig183

    @robochart_OperationSig183.setter
    def robochart_OperationSig183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_OperationSig__robochart_OperationSig183", None)
        self.__robochart_OperationSig183 = value
        
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
                    

class robochart_RoboticPlatform(NamedElement, ConnectionNode):

    pass
class robochart_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class TypedNamedElement:

    pass
class robochart_Member(TypedNamedElement):

    pass
class robochart_Type(ABC):

    pass
class robochart_TypedNamedElement(NamedElement):

    pass
class NamedExpression:

    pass
class robochart_Declaration(NamedElement, NamedExpression):

    pass
class Member:

    pass
class robochart_Variable(TypedNamedElement, Member, NamedExpression):

    def __init__(self, modifier: str, robochart_Variable: "robochart_VariableList" = None, robochart_Variable37: "robochart_Expression" = None, robochart_Variable111: "robochart_Trigger" = None, robochart_Variable117: "robochart_Trigger" = None, robochart_Variable123: "robochart_Trigger" = None, robochart_Variable213: "robochart_LambdaExp" = None, robochart_Variable205: "robochart_QuantifierExpression" = None, robochart_Variable310: "robochart_VarRef" = None, robochart_Variable251: "robochart_VarExp" = None, robochart_Variable275: "robochart_SetComp" = None):
        self.modifier = modifier
        self.robochart_Variable = robochart_Variable
        self.robochart_Variable37 = robochart_Variable37
        self.robochart_Variable111 = robochart_Variable111
        self.robochart_Variable117 = robochart_Variable117
        self.robochart_Variable123 = robochart_Variable123
        self.robochart_Variable213 = robochart_Variable213
        self.robochart_Variable205 = robochart_Variable205
        self.robochart_Variable310 = robochart_Variable310
        self.robochart_Variable251 = robochart_Variable251
        self.robochart_Variable275 = robochart_Variable275
        
        pass
    @property
    def modifier(self):
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier


    @property
    def robochart_Variable117(self):
        return self.__robochart_Variable117

    @robochart_Variable117.setter
    def robochart_Variable117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable117", None)
        self.__robochart_Variable117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Trigger116"):
                opp_val = getattr(old_value, "robochart_Trigger116", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Trigger116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Trigger116"):
                opp_val = getattr(value, "robochart_Trigger116", None)
                setattr(value, "robochart_Trigger116", self)

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
    def robochart_Variable123(self):
        return self.__robochart_Variable123

    @robochart_Variable123.setter
    def robochart_Variable123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable123", None)
        self.__robochart_Variable123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Trigger122"):
                opp_val = getattr(old_value, "robochart_Trigger122", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Trigger122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Trigger122"):
                opp_val = getattr(value, "robochart_Trigger122", None)
                setattr(value, "robochart_Trigger122", self)

    @property
    def robochart_Variable213(self):
        return self.__robochart_Variable213

    @robochart_Variable213.setter
    def robochart_Variable213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable213", None)
        self.__robochart_Variable213 = value
        
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
    def robochart_Variable205(self):
        return self.__robochart_Variable205

    @robochart_Variable205.setter
    def robochart_Variable205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable205", None)
        self.__robochart_Variable205 = value
        
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
    def robochart_Variable251(self):
        return self.__robochart_Variable251

    @robochart_Variable251.setter
    def robochart_Variable251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable251", None)
        self.__robochart_Variable251 = value
        
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
    def robochart_Variable275(self):
        return self.__robochart_Variable275

    @robochart_Variable275.setter
    def robochart_Variable275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable275", None)
        self.__robochart_Variable275 = value
        
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
    def robochart_Variable310(self):
        return self.__robochart_Variable310

    @robochart_Variable310.setter
    def robochart_Variable310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable310", None)
        self.__robochart_Variable310 = value
        
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
    def robochart_Variable111(self):
        return self.__robochart_Variable111

    @robochart_Variable111.setter
    def robochart_Variable111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robochart_Variable__robochart_Variable111", None)
        self.__robochart_Variable111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robochart_Trigger110"):
                opp_val = getattr(old_value, "robochart_Trigger110", None)
                if opp_val == self:
                    setattr(old_value, "robochart_Trigger110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robochart_Trigger110"):
                opp_val = getattr(value, "robochart_Trigger110", None)
                setattr(value, "robochart_Trigger110", self)

class robochart_Field(Member, NamedExpression):

    pass
class TypeDecl:

    pass
class robochart_RecordType(TypeDecl):

    pass
class robochart_NameType(TypeDecl):

    pass
class robochart_Enumeration(TypeDecl):

    pass
class robochart_Literal(TypeDecl, NamedExpression):

    pass
class robochart_PrimitiveType(TypeDecl):

    pass
class BasicPackage:

    pass
class robochart_RCPackage(BasicPackage):

    pass
class robochart_Import:

    def __init__(self, importedNamespace: str, robochart_Import: "robochart_BasicPackage" = None):
        self.importedNamespace = importedNamespace
        self.robochart_Import = robochart_Import
        
        pass
    @property
    def importedNamespace(self):
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
        
        pass
    @property
    def name(self):
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
                    

class robochart_Function(TypedNamedElement, NamedExpression):

    pass
class robochart_OperationDef(Operation, OperationSig, StateMachineBody):

    pass
class robochart_RCModule(NamedElement):

    pass
class robochart_ControllerDef(Controller, Context):

    pass
class robochart_StateMachineDef(StateMachine, StateMachineBody):

    pass
class robochart_TypeDecl(NamedElement):

    pass
class robochart_RoboticPlatformDef(RoboticPlatform, Context):

    pass
class robochart_Interface(NamedElement, BasicContext):

    pass