from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class NumericOperator(Enum):
    lt = "lt"
    eq = "eq"
    neq = "neq"
    gt = "gt"
    leq = "leq"
    geq = "geq"
class BooleanOperator(Enum):
    eq = "eq"
    neq = "neq"
class StringOperator(Enum):
    neq = "neq"
    eq = "eq"


############################################
# Definition of Classes
############################################

class Action:

    pass
class rcl_StopAction(Action):

    pass
class rcl_ForwardMinAction(Action):

    pass
class rcl_BackwardMinAction(Action):

    pass
class rcl_TurnAction(Action):

    pass
class rcl_SendAction(Action):

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

class rcl_TurnDegAction(Action):

    pass
class rcl_LogAction(Action):

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

class rcl_BackwardAction(Action):

    pass
class rcl_ForwardAction(Action):

    pass
class NumberValue:

    pass
class Query:

    pass
class rcl_HumidityQuery(NumberValue, Query):

    pass
class rcl_TemperatureQuery(NumberValue, Query):

    pass
class rcl_Query(ABC):

    pass
class RoverValue:

    pass
class rcl_BooleanValue(RoverValue):

    def __init__(self, bValue: bool, rcl_BooleanValue: "rcl_BooleanExpression" = None, rcl_BooleanValue32: "rcl_BooleanExpression" = None):
        self.bValue = bValue
        self.rcl_BooleanValue = rcl_BooleanValue
        self.rcl_BooleanValue32 = rcl_BooleanValue32
        
    @property
    def bValue(self) -> bool:
        return self.__bValue

    @bValue.setter
    def bValue(self, bValue: bool):
        self.__bValue = bValue

    @property
    def rcl_BooleanValue32(self):
        return self.__rcl_BooleanValue32

    @rcl_BooleanValue32.setter
    def rcl_BooleanValue32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_BooleanValue__rcl_BooleanValue32", None)
        self.__rcl_BooleanValue32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_BooleanExpression31"):
                opp_val = getattr(old_value, "rcl_BooleanExpression31", None)
                if opp_val == self:
                    setattr(old_value, "rcl_BooleanExpression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_BooleanExpression31"):
                opp_val = getattr(value, "rcl_BooleanExpression31", None)
                setattr(value, "rcl_BooleanExpression31", self)

    @property
    def rcl_BooleanValue(self):
        return self.__rcl_BooleanValue

    @rcl_BooleanValue.setter
    def rcl_BooleanValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_BooleanValue__rcl_BooleanValue", None)
        self.__rcl_BooleanValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_BooleanExpression"):
                opp_val = getattr(old_value, "rcl_BooleanExpression", None)
                if opp_val == self:
                    setattr(old_value, "rcl_BooleanExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_BooleanExpression"):
                opp_val = getattr(value, "rcl_BooleanExpression", None)
                setattr(value, "rcl_BooleanExpression", self)

class rcl_StringValue(RoverValue):

    def __init__(self, sValue: str, rcl_StringValue: "rcl_StringExpression" = None, rcl_StringValue28: "rcl_StringExpression" = None):
        self.sValue = sValue
        self.rcl_StringValue = rcl_StringValue
        self.rcl_StringValue28 = rcl_StringValue28
        
    @property
    def sValue(self) -> str:
        return self.__sValue

    @sValue.setter
    def sValue(self, sValue: str):
        self.__sValue = sValue

    @property
    def rcl_StringValue28(self):
        return self.__rcl_StringValue28

    @rcl_StringValue28.setter
    def rcl_StringValue28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_StringValue__rcl_StringValue28", None)
        self.__rcl_StringValue28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_StringExpression27"):
                opp_val = getattr(old_value, "rcl_StringExpression27", None)
                if opp_val == self:
                    setattr(old_value, "rcl_StringExpression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_StringExpression27"):
                opp_val = getattr(value, "rcl_StringExpression27", None)
                setattr(value, "rcl_StringExpression27", self)

    @property
    def rcl_StringValue(self):
        return self.__rcl_StringValue

    @rcl_StringValue.setter
    def rcl_StringValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_StringValue__rcl_StringValue", None)
        self.__rcl_StringValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_StringExpression"):
                opp_val = getattr(old_value, "rcl_StringExpression", None)
                if opp_val == self:
                    setattr(old_value, "rcl_StringExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_StringExpression"):
                opp_val = getattr(value, "rcl_StringExpression", None)
                setattr(value, "rcl_StringExpression", self)

class rcl_NumberValue(RoverValue):

    def __init__(self, nValue: int, rcl_NumberValue: "rcl_NumericExpression" = None, rcl_NumberValue24: "rcl_NumericExpression" = None, rcl_NumberValue34: "rcl_ForwardMinAction" = None, rcl_NumberValue36: "rcl_BackwardMinAction" = None, rcl_NumberValue38: "rcl_TurnDegAction" = None):
        self.nValue = nValue
        self.rcl_NumberValue = rcl_NumberValue
        self.rcl_NumberValue24 = rcl_NumberValue24
        self.rcl_NumberValue34 = rcl_NumberValue34
        self.rcl_NumberValue36 = rcl_NumberValue36
        self.rcl_NumberValue38 = rcl_NumberValue38
        
    @property
    def nValue(self) -> int:
        return self.__nValue

    @nValue.setter
    def nValue(self, nValue: int):
        self.__nValue = nValue

    @property
    def rcl_NumberValue36(self):
        return self.__rcl_NumberValue36

    @rcl_NumberValue36.setter
    def rcl_NumberValue36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumberValue__rcl_NumberValue36", None)
        self.__rcl_NumberValue36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_BackwardMinAction"):
                opp_val = getattr(old_value, "rcl_BackwardMinAction", None)
                if opp_val == self:
                    setattr(old_value, "rcl_BackwardMinAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_BackwardMinAction"):
                opp_val = getattr(value, "rcl_BackwardMinAction", None)
                setattr(value, "rcl_BackwardMinAction", self)

    @property
    def rcl_NumberValue(self):
        return self.__rcl_NumberValue

    @rcl_NumberValue.setter
    def rcl_NumberValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumberValue__rcl_NumberValue", None)
        self.__rcl_NumberValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_NumericExpression"):
                opp_val = getattr(old_value, "rcl_NumericExpression", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumericExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumericExpression"):
                opp_val = getattr(value, "rcl_NumericExpression", None)
                setattr(value, "rcl_NumericExpression", self)

    @property
    def rcl_NumberValue24(self):
        return self.__rcl_NumberValue24

    @rcl_NumberValue24.setter
    def rcl_NumberValue24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumberValue__rcl_NumberValue24", None)
        self.__rcl_NumberValue24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_NumericExpression23"):
                opp_val = getattr(old_value, "rcl_NumericExpression23", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumericExpression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumericExpression23"):
                opp_val = getattr(value, "rcl_NumericExpression23", None)
                setattr(value, "rcl_NumericExpression23", self)

    @property
    def rcl_NumberValue34(self):
        return self.__rcl_NumberValue34

    @rcl_NumberValue34.setter
    def rcl_NumberValue34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumberValue__rcl_NumberValue34", None)
        self.__rcl_NumberValue34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_ForwardMinAction"):
                opp_val = getattr(old_value, "rcl_ForwardMinAction", None)
                if opp_val == self:
                    setattr(old_value, "rcl_ForwardMinAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_ForwardMinAction"):
                opp_val = getattr(value, "rcl_ForwardMinAction", None)
                setattr(value, "rcl_ForwardMinAction", self)

    @property
    def rcl_NumberValue38(self):
        return self.__rcl_NumberValue38

    @rcl_NumberValue38.setter
    def rcl_NumberValue38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumberValue__rcl_NumberValue38", None)
        self.__rcl_NumberValue38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_TurnDegAction"):
                opp_val = getattr(old_value, "rcl_TurnDegAction", None)
                if opp_val == self:
                    setattr(old_value, "rcl_TurnDegAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_TurnDegAction"):
                opp_val = getattr(value, "rcl_TurnDegAction", None)
                setattr(value, "rcl_TurnDegAction", self)

class RoverExpression:

    pass
class rcl_StringExpression(RoverExpression):

    def __init__(self, op: str, rcl_StringExpression: "rcl_StringValue" = None, rcl_StringExpression27: "rcl_StringValue" = None):
        self.op = op
        self.rcl_StringExpression = rcl_StringExpression
        self.rcl_StringExpression27 = rcl_StringExpression27
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def rcl_StringExpression27(self):
        return self.__rcl_StringExpression27

    @rcl_StringExpression27.setter
    def rcl_StringExpression27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_StringExpression__rcl_StringExpression27", None)
        self.__rcl_StringExpression27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_StringValue28"):
                opp_val = getattr(old_value, "rcl_StringValue28", None)
                if opp_val == self:
                    setattr(old_value, "rcl_StringValue28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_StringValue28"):
                opp_val = getattr(value, "rcl_StringValue28", None)
                setattr(value, "rcl_StringValue28", self)

    @property
    def rcl_StringExpression(self):
        return self.__rcl_StringExpression

    @rcl_StringExpression.setter
    def rcl_StringExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_StringExpression__rcl_StringExpression", None)
        self.__rcl_StringExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_StringValue"):
                opp_val = getattr(old_value, "rcl_StringValue", None)
                if opp_val == self:
                    setattr(old_value, "rcl_StringValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_StringValue"):
                opp_val = getattr(value, "rcl_StringValue", None)
                setattr(value, "rcl_StringValue", self)

class rcl_BooleanExpression(RoverExpression):

    def __init__(self, op: str, rcl_BooleanExpression: "rcl_BooleanValue" = None, rcl_BooleanExpression31: "rcl_BooleanValue" = None):
        self.op = op
        self.rcl_BooleanExpression = rcl_BooleanExpression
        self.rcl_BooleanExpression31 = rcl_BooleanExpression31
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def rcl_BooleanExpression(self):
        return self.__rcl_BooleanExpression

    @rcl_BooleanExpression.setter
    def rcl_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_BooleanExpression__rcl_BooleanExpression", None)
        self.__rcl_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_BooleanValue"):
                opp_val = getattr(old_value, "rcl_BooleanValue", None)
                if opp_val == self:
                    setattr(old_value, "rcl_BooleanValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_BooleanValue"):
                opp_val = getattr(value, "rcl_BooleanValue", None)
                setattr(value, "rcl_BooleanValue", self)

    @property
    def rcl_BooleanExpression31(self):
        return self.__rcl_BooleanExpression31

    @rcl_BooleanExpression31.setter
    def rcl_BooleanExpression31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_BooleanExpression__rcl_BooleanExpression31", None)
        self.__rcl_BooleanExpression31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_BooleanValue32"):
                opp_val = getattr(old_value, "rcl_BooleanValue32", None)
                if opp_val == self:
                    setattr(old_value, "rcl_BooleanValue32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_BooleanValue32"):
                opp_val = getattr(value, "rcl_BooleanValue32", None)
                setattr(value, "rcl_BooleanValue32", self)

class rcl_NumericExpression(RoverExpression):

    def __init__(self, op: str, rcl_NumericExpression: "rcl_NumberValue" = None, rcl_NumericExpression23: "rcl_NumberValue" = None):
        self.op = op
        self.rcl_NumericExpression = rcl_NumericExpression
        self.rcl_NumericExpression23 = rcl_NumericExpression23
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def rcl_NumericExpression23(self):
        return self.__rcl_NumericExpression23

    @rcl_NumericExpression23.setter
    def rcl_NumericExpression23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumericExpression__rcl_NumericExpression23", None)
        self.__rcl_NumericExpression23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_NumberValue24"):
                opp_val = getattr(old_value, "rcl_NumberValue24", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumberValue24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumberValue24"):
                opp_val = getattr(value, "rcl_NumberValue24", None)
                setattr(value, "rcl_NumberValue24", self)

    @property
    def rcl_NumericExpression(self):
        return self.__rcl_NumericExpression

    @rcl_NumericExpression.setter
    def rcl_NumericExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumericExpression__rcl_NumericExpression", None)
        self.__rcl_NumericExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_NumberValue"):
                opp_val = getattr(old_value, "rcl_NumberValue", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumberValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumberValue"):
                opp_val = getattr(value, "rcl_NumberValue", None)
                setattr(value, "rcl_NumberValue", self)

class BooleanValue:

    pass
class rcl_ObstacleQuery(BooleanValue, Query):

    def __init__(self, front: bool):
        self.front = front
        
    @property
    def front(self) -> bool:
        return self.__front

    @front.setter
    def front(self, front: bool):
        self.__front = front

class StringValue:

    pass
class rcl_MessageQuery(Query, StringValue):

    pass
class rcl_RoverExpression(ABC):

    pass
class rcl_RoverValue(ABC):

    pass
class Statement:

    pass
class rcl_Action(Statement):

    pass
class rcl_Conditional(Statement):

    pass
class rcl_Loop(Statement):

    pass
class rcl_VarRef(NumberValue, BooleanValue, StringValue, Statement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class rcl_VarAssignment(Statement):

    def __init__(self, name: str, rcl_VarAssignment: "rcl_RoverValue" = None):
        self.name = name
        self.rcl_VarAssignment = rcl_VarAssignment
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rcl_VarAssignment(self):
        return self.__rcl_VarAssignment

    @rcl_VarAssignment.setter
    def rcl_VarAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_VarAssignment__rcl_VarAssignment", None)
        self.__rcl_VarAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RoverValue"):
                opp_val = getattr(old_value, "rcl_RoverValue", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RoverValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RoverValue"):
                opp_val = getattr(value, "rcl_RoverValue", None)
                setattr(value, "rcl_RoverValue", self)

class rcl_Statement(ABC):

    pass
class rcl_RclBlock(Statement):

    pass
class rcl_Param:

    def __init__(self, name: str, rcl_Param: "rcl_RoverProgram" = None):
        self.name = name
        self.rcl_Param = rcl_Param
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rcl_Param(self):
        return self.__rcl_Param

    @rcl_Param.setter
    def rcl_Param(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Param__rcl_Param", None)
        self.__rcl_Param = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RoverProgram"):
                opp_val = getattr(old_value, "rcl_RoverProgram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RoverProgram"):
                opp_val = getattr(value, "rcl_RoverProgram", None)
                if opp_val is None:
                    setattr(value, "rcl_RoverProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rcl_RoverProgram:

    def __init__(self, name: str, rcl_RoverProgram: set["rcl_Param"] = None, rcl_RoverProgram2: "rcl_RclBlock" = None):
        self.name = name
        self.rcl_RoverProgram = rcl_RoverProgram if rcl_RoverProgram is not None else set()
        self.rcl_RoverProgram2 = rcl_RoverProgram2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rcl_RoverProgram(self):
        return self.__rcl_RoverProgram

    @rcl_RoverProgram.setter
    def rcl_RoverProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RoverProgram__rcl_RoverProgram", None)
        self.__rcl_RoverProgram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rcl_Param"):
                    opp_val = getattr(item, "rcl_Param", None)
                    
                    if opp_val == self:
                        setattr(item, "rcl_Param", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rcl_Param"):
                    opp_val = getattr(item, "rcl_Param", None)
                    
                    setattr(item, "rcl_Param", self)
                    

    @property
    def rcl_RoverProgram2(self):
        return self.__rcl_RoverProgram2

    @rcl_RoverProgram2.setter
    def rcl_RoverProgram2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RoverProgram__rcl_RoverProgram2", None)
        self.__rcl_RoverProgram2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RclBlock"):
                opp_val = getattr(old_value, "rcl_RclBlock", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RclBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RclBlock"):
                opp_val = getattr(value, "rcl_RclBlock", None)
                setattr(value, "rcl_RclBlock", self)
