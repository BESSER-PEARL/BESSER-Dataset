from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanOperator(Enum):
    eq = "eq"
    neq = "neq"
class NumericOperator(Enum):
    lt = "lt"
    eq = "eq"
    neq = "neq"
    gt = "gt"
    leq = "leq"
    geq = "geq"
class StringOperator(Enum):
    eq = "eq"
    neq = "neq"


############################################
# Definition of Classes
############################################

class Action:

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

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_ForwardAction(Action):

    def __init__(self):
        
    def eval(self):
        # TODO: Implement eval method
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

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_StopAction(Action):

    def __init__(self):
        
    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_TurnDegAction(Action):

    def __init__(self, rcl_TurnDegAction: "rcl_NumberValue" = None):
        self.rcl_TurnDegAction = rcl_TurnDegAction
        
    @property
    def rcl_TurnDegAction(self):
        return self.__rcl_TurnDegAction

    @rcl_TurnDegAction.setter
    def rcl_TurnDegAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_TurnDegAction__rcl_TurnDegAction", None)
        self.__rcl_TurnDegAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_NumberValue38"):
                opp_val = getattr(old_value, "rcl_NumberValue38", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumberValue38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumberValue38"):
                opp_val = getattr(value, "rcl_NumberValue38", None)
                setattr(value, "rcl_NumberValue38", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_TurnAction(Action):

    def __init__(self):
        
    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_BackwardMinAction(Action):

    def __init__(self, rcl_BackwardMinAction: "rcl_NumberValue" = None):
        self.rcl_BackwardMinAction = rcl_BackwardMinAction
        
    @property
    def rcl_BackwardMinAction(self):
        return self.__rcl_BackwardMinAction

    @rcl_BackwardMinAction.setter
    def rcl_BackwardMinAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_BackwardMinAction__rcl_BackwardMinAction", None)
        self.__rcl_BackwardMinAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_NumberValue36"):
                opp_val = getattr(old_value, "rcl_NumberValue36", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumberValue36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumberValue36"):
                opp_val = getattr(value, "rcl_NumberValue36", None)
                setattr(value, "rcl_NumberValue36", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_BackwardAction(Action):

    def __init__(self):
        
    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_ForwardMinAction(Action):

    def __init__(self, rcl_ForwardMinAction: "rcl_NumberValue" = None):
        self.rcl_ForwardMinAction = rcl_ForwardMinAction
        
    @property
    def rcl_ForwardMinAction(self):
        return self.__rcl_ForwardMinAction

    @rcl_ForwardMinAction.setter
    def rcl_ForwardMinAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_ForwardMinAction__rcl_ForwardMinAction", None)
        self.__rcl_ForwardMinAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_NumberValue34"):
                opp_val = getattr(old_value, "rcl_NumberValue34", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumberValue34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumberValue34"):
                opp_val = getattr(value, "rcl_NumberValue34", None)
                setattr(value, "rcl_NumberValue34", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class RoverExpression:

    pass
class rcl_StringExpression(RoverExpression):

    def __init__(self, op: bool, rcl_StringExpression27: "rcl_StringValue" = None, rcl_StringExpression: "rcl_StringValue" = None):
        self.op = op
        self.rcl_StringExpression27 = rcl_StringExpression27
        self.rcl_StringExpression = rcl_StringExpression
        
    @property
    def op(self) -> bool:
        return self.__op

    @op.setter
    def op(self, op: bool):
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

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_NumericExpression(RoverExpression):

    def __init__(self, op: bool, rcl_NumericExpression: "rcl_NumberValue" = None, rcl_NumericExpression23: "rcl_NumberValue" = None):
        self.op = op
        self.rcl_NumericExpression = rcl_NumericExpression
        self.rcl_NumericExpression23 = rcl_NumericExpression23
        
    @property
    def op(self) -> bool:
        return self.__op

    @op.setter
    def op(self, op: bool):
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

    def eval(self):
        # TODO: Implement eval method
        pass

class RoverValue:

    pass
class rcl_NumberValue(RoverValue):

    def __init__(self, nValue: str, rcl_NumberValue: "rcl_NumericExpression" = None, rcl_NumberValue24: "rcl_NumericExpression" = None, rcl_NumberValue34: "rcl_ForwardMinAction" = None, rcl_NumberValue36: "rcl_BackwardMinAction" = None, rcl_NumberValue38: "rcl_TurnDegAction" = None):
        self.nValue = nValue
        self.rcl_NumberValue = rcl_NumberValue
        self.rcl_NumberValue24 = rcl_NumberValue24
        self.rcl_NumberValue34 = rcl_NumberValue34
        self.rcl_NumberValue36 = rcl_NumberValue36
        self.rcl_NumberValue38 = rcl_NumberValue38
        
    @property
    def nValue(self) -> str:
        return self.__nValue

    @nValue.setter
    def nValue(self, nValue: str):
        self.__nValue = nValue

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

    def print(self):
        # TODO: Implement print method
        pass

    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

class rcl_StringValue(RoverValue):

    def __init__(self, sValue: bool, rcl_StringValue: "rcl_StringExpression" = None, rcl_StringValue28: "rcl_StringExpression" = None):
        self.sValue = sValue
        self.rcl_StringValue = rcl_StringValue
        self.rcl_StringValue28 = rcl_StringValue28
        
    @property
    def sValue(self) -> bool:
        return self.__sValue

    @sValue.setter
    def sValue(self, sValue: bool):
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

    def getStringValue(self):
        # TODO: Implement getStringValue method
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

    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

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

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_RoverExpression(ABC):

    def __init__(self, rcl_RoverExpression: "rcl_Conditional" = None, rcl_RoverExpression14: "rcl_Loop" = None):
        self.rcl_RoverExpression = rcl_RoverExpression
        self.rcl_RoverExpression14 = rcl_RoverExpression14
        
    @property
    def rcl_RoverExpression14(self):
        return self.__rcl_RoverExpression14

    @rcl_RoverExpression14.setter
    def rcl_RoverExpression14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RoverExpression__rcl_RoverExpression14", None)
        self.__rcl_RoverExpression14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_Loop"):
                opp_val = getattr(old_value, "rcl_Loop", None)
                if opp_val == self:
                    setattr(old_value, "rcl_Loop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_Loop"):
                opp_val = getattr(value, "rcl_Loop", None)
                setattr(value, "rcl_Loop", self)

    @property
    def rcl_RoverExpression(self):
        return self.__rcl_RoverExpression

    @rcl_RoverExpression.setter
    def rcl_RoverExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RoverExpression__rcl_RoverExpression", None)
        self.__rcl_RoverExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_Conditional"):
                opp_val = getattr(old_value, "rcl_Conditional", None)
                if opp_val == self:
                    setattr(old_value, "rcl_Conditional", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_Conditional"):
                opp_val = getattr(value, "rcl_Conditional", None)
                setattr(value, "rcl_Conditional", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class BooleanValue:

    pass
class StringValue:

    pass
class NumberValue:

    pass
class Query:

    pass
class rcl_MessageQuery(StringValue, Query):

    def __init__(self):
        
    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

class rcl_HumidityQuery(NumberValue, Query):

    def __init__(self):
        
    def getIntValue(self):
        # TODO: Implement getIntValue method
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

    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

class rcl_TemperatureQuery(NumberValue, Query):

    def __init__(self):
        
    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

class rcl_Query(ABC):

    pass
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
                    

    def getVar(self, n: str) -> str:
        # TODO: Implement getVar method
        pass

    def run(self):
        # TODO: Implement run method
        pass

    def bindVar(self, v: str, n: str):
        # TODO: Implement bindVar method
        pass

class rcl_RoverValue:

    pass
class Statement:

    pass
class rcl_Action(Statement):

    pass
class rcl_Conditional(Statement):

    def __init__(self, rcl_Conditional: "rcl_RoverExpression" = None, rcl_Conditional8: "rcl_RclBlock" = None, rcl_Conditional11: "rcl_RclBlock" = None):
        self.rcl_Conditional = rcl_Conditional
        self.rcl_Conditional8 = rcl_Conditional8
        self.rcl_Conditional11 = rcl_Conditional11
        
    @property
    def rcl_Conditional8(self):
        return self.__rcl_Conditional8

    @rcl_Conditional8.setter
    def rcl_Conditional8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Conditional__rcl_Conditional8", None)
        self.__rcl_Conditional8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RclBlock9"):
                opp_val = getattr(old_value, "rcl_RclBlock9", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RclBlock9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RclBlock9"):
                opp_val = getattr(value, "rcl_RclBlock9", None)
                setattr(value, "rcl_RclBlock9", self)

    @property
    def rcl_Conditional11(self):
        return self.__rcl_Conditional11

    @rcl_Conditional11.setter
    def rcl_Conditional11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Conditional__rcl_Conditional11", None)
        self.__rcl_Conditional11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RclBlock12"):
                opp_val = getattr(old_value, "rcl_RclBlock12", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RclBlock12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RclBlock12"):
                opp_val = getattr(value, "rcl_RclBlock12", None)
                setattr(value, "rcl_RclBlock12", self)

    @property
    def rcl_Conditional(self):
        return self.__rcl_Conditional

    @rcl_Conditional.setter
    def rcl_Conditional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Conditional__rcl_Conditional", None)
        self.__rcl_Conditional = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RoverExpression"):
                opp_val = getattr(old_value, "rcl_RoverExpression", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RoverExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RoverExpression"):
                opp_val = getattr(value, "rcl_RoverExpression", None)
                setattr(value, "rcl_RoverExpression", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_VarRef(NumberValue, Statement, StringValue, BooleanValue):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

    def eval(self):
        # TODO: Implement eval method
        pass

    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

class rcl_Loop(Statement):

    def __init__(self, rcl_Loop: "rcl_RoverExpression" = None, rcl_Loop16: "rcl_RclBlock" = None):
        self.rcl_Loop = rcl_Loop
        self.rcl_Loop16 = rcl_Loop16
        
    @property
    def rcl_Loop16(self):
        return self.__rcl_Loop16

    @rcl_Loop16.setter
    def rcl_Loop16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Loop__rcl_Loop16", None)
        self.__rcl_Loop16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RclBlock17"):
                opp_val = getattr(old_value, "rcl_RclBlock17", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RclBlock17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RclBlock17"):
                opp_val = getattr(value, "rcl_RclBlock17", None)
                setattr(value, "rcl_RclBlock17", self)

    @property
    def rcl_Loop(self):
        return self.__rcl_Loop

    @rcl_Loop.setter
    def rcl_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Loop__rcl_Loop", None)
        self.__rcl_Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RoverExpression14"):
                opp_val = getattr(old_value, "rcl_RoverExpression14", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RoverExpression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RoverExpression14"):
                opp_val = getattr(value, "rcl_RoverExpression14", None)
                setattr(value, "rcl_RoverExpression14", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_VarAssignment(Statement):

    def __init__(self, name: bool, rcl_VarAssignment: "rcl_RoverValue" = None):
        self.name = name
        self.rcl_VarAssignment = rcl_VarAssignment
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
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

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_Statement(ABC):

    def __init__(self, : "rcl_RclBlock" = None, 20: "rcl_RclBlock" = None):
        self. = 
        self.20 = 20
        
    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Statement__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "4"):
                opp_val = getattr(old_value, "4", None)
                if opp_val == self:
                    setattr(old_value, "4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "4"):
                opp_val = getattr(value, "4", None)
                setattr(value, "4", self)

    @property
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Statement__20", None)
        self.__20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "19"):
                opp_val = getattr(old_value, "19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "19"):
                opp_val = getattr(value, "19", None)
                if opp_val is None:
                    setattr(value, "19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getProgram(self) -> str:
        # TODO: Implement getProgram method
        pass

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_RclBlock(Statement):

    def __init__(self, rcl_RclBlock: "rcl_RoverProgram" = None, 4: "rcl_Statement" = None, 19: set["rcl_Statement"] = None, rcl_RclBlock9: "rcl_Conditional" = None, rcl_RclBlock12: "rcl_Conditional" = None, rcl_RclBlock17: "rcl_Loop" = None):
        self.rcl_RclBlock = rcl_RclBlock
        self.4 = 4
        self.19 = 19 if 19 is not None else set()
        self.rcl_RclBlock9 = rcl_RclBlock9
        self.rcl_RclBlock12 = rcl_RclBlock12
        self.rcl_RclBlock17 = rcl_RclBlock17
        
    @property
    def rcl_RclBlock9(self):
        return self.__rcl_RclBlock9

    @rcl_RclBlock9.setter
    def rcl_RclBlock9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__rcl_RclBlock9", None)
        self.__rcl_RclBlock9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_Conditional8"):
                opp_val = getattr(old_value, "rcl_Conditional8", None)
                if opp_val == self:
                    setattr(old_value, "rcl_Conditional8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_Conditional8"):
                opp_val = getattr(value, "rcl_Conditional8", None)
                setattr(value, "rcl_Conditional8", self)

    @property
    def rcl_RclBlock12(self):
        return self.__rcl_RclBlock12

    @rcl_RclBlock12.setter
    def rcl_RclBlock12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__rcl_RclBlock12", None)
        self.__rcl_RclBlock12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_Conditional11"):
                opp_val = getattr(old_value, "rcl_Conditional11", None)
                if opp_val == self:
                    setattr(old_value, "rcl_Conditional11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_Conditional11"):
                opp_val = getattr(value, "rcl_Conditional11", None)
                setattr(value, "rcl_Conditional11", self)

    @property
    def rcl_RclBlock(self):
        return self.__rcl_RclBlock

    @rcl_RclBlock.setter
    def rcl_RclBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__rcl_RclBlock", None)
        self.__rcl_RclBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RoverProgram2"):
                opp_val = getattr(old_value, "rcl_RoverProgram2", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RoverProgram2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RoverProgram2"):
                opp_val = getattr(value, "rcl_RoverProgram2", None)
                setattr(value, "rcl_RoverProgram2", self)

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    @property
    def rcl_RclBlock17(self):
        return self.__rcl_RclBlock17

    @rcl_RclBlock17.setter
    def rcl_RclBlock17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__rcl_RclBlock17", None)
        self.__rcl_RclBlock17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_Loop16"):
                opp_val = getattr(old_value, "rcl_Loop16", None)
                if opp_val == self:
                    setattr(old_value, "rcl_Loop16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_Loop16"):
                opp_val = getattr(value, "rcl_Loop16", None)
                setattr(value, "rcl_Loop16", self)

    @property
    def 19(self):
        return self.__19

    @19.setter
    def 19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__19", None)
        self.__19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "20"):
                    opp_val = getattr(item, "20", None)
                    
                    if opp_val == self:
                        setattr(item, "20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "20"):
                    opp_val = getattr(item, "20", None)
                    
                    setattr(item, "20", self)
                    

    def eval(self):
        # TODO: Implement eval method
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
