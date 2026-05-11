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
        
        pass
    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_TurnAction(Action):

    def __init__(self):
        
        pass
    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_StopAction(Action):

    def __init__(self):
        
        pass
    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_TurnDegAction(Action):

    def __init__(self, rcl_TurnDegAction: "rcl_NumberValue" = None):
        self.rcl_TurnDegAction = rcl_TurnDegAction
        
        pass
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
            if hasattr(old_value, "rcl_NumberValue35"):
                opp_val = getattr(old_value, "rcl_NumberValue35", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumberValue35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumberValue35"):
                opp_val = getattr(value, "rcl_NumberValue35", None)
                setattr(value, "rcl_NumberValue35", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_BackwardMinAction(Action):

    def __init__(self, rcl_BackwardMinAction: "rcl_NumberValue" = None):
        self.rcl_BackwardMinAction = rcl_BackwardMinAction
        
        pass
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
            if hasattr(old_value, "rcl_NumberValue33"):
                opp_val = getattr(old_value, "rcl_NumberValue33", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumberValue33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumberValue33"):
                opp_val = getattr(value, "rcl_NumberValue33", None)
                setattr(value, "rcl_NumberValue33", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_BackwardAction(Action):

    def __init__(self):
        
        pass
    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_ForwardMinAction(Action):

    def __init__(self, rcl_ForwardMinAction: "rcl_NumberValue" = None):
        self.rcl_ForwardMinAction = rcl_ForwardMinAction
        
        pass
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
            if hasattr(old_value, "rcl_NumberValue31"):
                opp_val = getattr(old_value, "rcl_NumberValue31", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumberValue31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumberValue31"):
                opp_val = getattr(value, "rcl_NumberValue31", None)
                setattr(value, "rcl_NumberValue31", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_LogAction(Action):

    def __init__(self, message: str):
        self.message = message
        
        pass
    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_ForwardAction(Action):

    def __init__(self):
        
        pass
    def eval(self):
        # TODO: Implement eval method
        pass

class RoverValue:

    pass
class rcl_BooleanValue(RoverValue):

    def __init__(self, bValue: bool, rcl_BooleanValue29: "rcl_BooleanExpression" = None, rcl_BooleanValue: "rcl_BooleanExpression" = None):
        self.bValue = bValue
        self.rcl_BooleanValue29 = rcl_BooleanValue29
        self.rcl_BooleanValue = rcl_BooleanValue
        
        pass
    @property
    def bValue(self):
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
    def rcl_BooleanValue29(self):
        return self.__rcl_BooleanValue29

    @rcl_BooleanValue29.setter
    def rcl_BooleanValue29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_BooleanValue__rcl_BooleanValue29", None)
        self.__rcl_BooleanValue29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_BooleanExpression28"):
                opp_val = getattr(old_value, "rcl_BooleanExpression28", None)
                if opp_val == self:
                    setattr(old_value, "rcl_BooleanExpression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_BooleanExpression28"):
                opp_val = getattr(value, "rcl_BooleanExpression28", None)
                setattr(value, "rcl_BooleanExpression28", self)

    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

class rcl_StringValue(RoverValue):

    def __init__(self, sValue: bool, rcl_StringValue: "rcl_StringExpression" = None, rcl_StringValue25: "rcl_StringExpression" = None):
        self.sValue = sValue
        self.rcl_StringValue = rcl_StringValue
        self.rcl_StringValue25 = rcl_StringValue25
        
        pass
    @property
    def sValue(self):
        return self.__sValue

    @sValue.setter
    def sValue(self, sValue: bool):
        self.__sValue = sValue


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

    @property
    def rcl_StringValue25(self):
        return self.__rcl_StringValue25

    @rcl_StringValue25.setter
    def rcl_StringValue25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_StringValue__rcl_StringValue25", None)
        self.__rcl_StringValue25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_StringExpression24"):
                opp_val = getattr(old_value, "rcl_StringExpression24", None)
                if opp_val == self:
                    setattr(old_value, "rcl_StringExpression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_StringExpression24"):
                opp_val = getattr(value, "rcl_StringExpression24", None)
                setattr(value, "rcl_StringExpression24", self)

    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

class rcl_NumberValue(RoverValue):

    def __init__(self, nValue: str, rcl_NumberValue: "rcl_NumericExpression" = None, rcl_NumberValue21: "rcl_NumericExpression" = None, rcl_NumberValue31: "rcl_ForwardMinAction" = None, rcl_NumberValue33: "rcl_BackwardMinAction" = None, rcl_NumberValue35: "rcl_TurnDegAction" = None):
        self.nValue = nValue
        self.rcl_NumberValue = rcl_NumberValue
        self.rcl_NumberValue21 = rcl_NumberValue21
        self.rcl_NumberValue31 = rcl_NumberValue31
        self.rcl_NumberValue33 = rcl_NumberValue33
        self.rcl_NumberValue35 = rcl_NumberValue35
        
        pass
    @property
    def nValue(self):
        return self.__nValue

    @nValue.setter
    def nValue(self, nValue: str):
        self.__nValue = nValue


    @property
    def rcl_NumberValue35(self):
        return self.__rcl_NumberValue35

    @rcl_NumberValue35.setter
    def rcl_NumberValue35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumberValue__rcl_NumberValue35", None)
        self.__rcl_NumberValue35 = value
        
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
    def rcl_NumberValue21(self):
        return self.__rcl_NumberValue21

    @rcl_NumberValue21.setter
    def rcl_NumberValue21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumberValue__rcl_NumberValue21", None)
        self.__rcl_NumberValue21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_NumericExpression20"):
                opp_val = getattr(old_value, "rcl_NumericExpression20", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumericExpression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumericExpression20"):
                opp_val = getattr(value, "rcl_NumericExpression20", None)
                setattr(value, "rcl_NumericExpression20", self)

    @property
    def rcl_NumberValue31(self):
        return self.__rcl_NumberValue31

    @rcl_NumberValue31.setter
    def rcl_NumberValue31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumberValue__rcl_NumberValue31", None)
        self.__rcl_NumberValue31 = value
        
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
    def rcl_NumberValue33(self):
        return self.__rcl_NumberValue33

    @rcl_NumberValue33.setter
    def rcl_NumberValue33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumberValue__rcl_NumberValue33", None)
        self.__rcl_NumberValue33 = value
        
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

    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class RoverExpression:

    pass
class rcl_StringExpression(RoverExpression):

    def __init__(self, op: bool, rcl_StringExpression: "rcl_StringValue" = None, rcl_StringExpression24: "rcl_StringValue" = None):
        self.op = op
        self.rcl_StringExpression = rcl_StringExpression
        self.rcl_StringExpression24 = rcl_StringExpression24
        
        pass
    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, op: bool):
        self.__op = op


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

    @property
    def rcl_StringExpression24(self):
        return self.__rcl_StringExpression24

    @rcl_StringExpression24.setter
    def rcl_StringExpression24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_StringExpression__rcl_StringExpression24", None)
        self.__rcl_StringExpression24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_StringValue25"):
                opp_val = getattr(old_value, "rcl_StringValue25", None)
                if opp_val == self:
                    setattr(old_value, "rcl_StringValue25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_StringValue25"):
                opp_val = getattr(value, "rcl_StringValue25", None)
                setattr(value, "rcl_StringValue25", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_BooleanExpression(RoverExpression):

    def __init__(self, op: str, rcl_BooleanExpression28: "rcl_BooleanValue" = None, rcl_BooleanExpression: "rcl_BooleanValue" = None):
        self.op = op
        self.rcl_BooleanExpression28 = rcl_BooleanExpression28
        self.rcl_BooleanExpression = rcl_BooleanExpression
        
        pass
    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op


    @property
    def rcl_BooleanExpression28(self):
        return self.__rcl_BooleanExpression28

    @rcl_BooleanExpression28.setter
    def rcl_BooleanExpression28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_BooleanExpression__rcl_BooleanExpression28", None)
        self.__rcl_BooleanExpression28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_BooleanValue29"):
                opp_val = getattr(old_value, "rcl_BooleanValue29", None)
                if opp_val == self:
                    setattr(old_value, "rcl_BooleanValue29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_BooleanValue29"):
                opp_val = getattr(value, "rcl_BooleanValue29", None)
                setattr(value, "rcl_BooleanValue29", self)

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

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_NumericExpression(RoverExpression):

    def __init__(self, op: bool, rcl_NumericExpression: "rcl_NumberValue" = None, rcl_NumericExpression20: "rcl_NumberValue" = None):
        self.op = op
        self.rcl_NumericExpression = rcl_NumericExpression
        self.rcl_NumericExpression20 = rcl_NumericExpression20
        
        pass
    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, op: bool):
        self.__op = op


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

    @property
    def rcl_NumericExpression20(self):
        return self.__rcl_NumericExpression20

    @rcl_NumericExpression20.setter
    def rcl_NumericExpression20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_NumericExpression__rcl_NumericExpression20", None)
        self.__rcl_NumericExpression20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_NumberValue21"):
                opp_val = getattr(old_value, "rcl_NumberValue21", None)
                if opp_val == self:
                    setattr(old_value, "rcl_NumberValue21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_NumberValue21"):
                opp_val = getattr(value, "rcl_NumberValue21", None)
                setattr(value, "rcl_NumberValue21", self)

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
class rcl_HumidityQuery(NumberValue, Query):

    def __init__(self):
        
        pass
    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

class rcl_MessageQuery(Query, StringValue):

    def __init__(self):
        
        pass
    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

class rcl_ObstacleQuery(Query, BooleanValue):

    def __init__(self, front: bool):
        self.front = front
        
        pass
    @property
    def front(self):
        return self.__front

    @front.setter
    def front(self, front: bool):
        self.__front = front


    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

class rcl_TemperatureQuery(NumberValue, Query):

    def __init__(self):
        
        pass
    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

class rcl_Query(ABC):

    pass
class rcl_RoverExpression(ABC):

    def __init__(self, rcl_RoverExpression: "rcl_Conditional" = None, rcl_RoverExpression13: "rcl_Loop" = None):
        self.rcl_RoverExpression = rcl_RoverExpression
        self.rcl_RoverExpression13 = rcl_RoverExpression13
        
        pass
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

    @property
    def rcl_RoverExpression13(self):
        return self.__rcl_RoverExpression13

    @rcl_RoverExpression13.setter
    def rcl_RoverExpression13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RoverExpression__rcl_RoverExpression13", None)
        self.__rcl_RoverExpression13 = value
        
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

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_RoverValue:

    pass
class Statement:

    pass
class rcl_Conditional(Statement):

    def __init__(self, rcl_Conditional: "rcl_RoverExpression" = None, rcl_Conditional7: "rcl_RclBlock" = None, rcl_Conditional10: "rcl_RclBlock" = None):
        self.rcl_Conditional = rcl_Conditional
        self.rcl_Conditional7 = rcl_Conditional7
        self.rcl_Conditional10 = rcl_Conditional10
        
        pass
    @property
    def rcl_Conditional10(self):
        return self.__rcl_Conditional10

    @rcl_Conditional10.setter
    def rcl_Conditional10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Conditional__rcl_Conditional10", None)
        self.__rcl_Conditional10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RclBlock11"):
                opp_val = getattr(old_value, "rcl_RclBlock11", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RclBlock11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RclBlock11"):
                opp_val = getattr(value, "rcl_RclBlock11", None)
                setattr(value, "rcl_RclBlock11", self)

    @property
    def rcl_Conditional7(self):
        return self.__rcl_Conditional7

    @rcl_Conditional7.setter
    def rcl_Conditional7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Conditional__rcl_Conditional7", None)
        self.__rcl_Conditional7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RclBlock8"):
                opp_val = getattr(old_value, "rcl_RclBlock8", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RclBlock8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RclBlock8"):
                opp_val = getattr(value, "rcl_RclBlock8", None)
                setattr(value, "rcl_RclBlock8", self)

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

class rcl_VarAssignment(Statement):

    def __init__(self, name: bool, rcl_VarAssignment: "rcl_RoverValue" = None):
        self.name = name
        self.rcl_VarAssignment = rcl_VarAssignment
        
        pass
    @property
    def name(self):
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

class rcl_Loop(Statement):

    def __init__(self, rcl_Loop: "rcl_RoverExpression" = None, rcl_Loop15: "rcl_RclBlock" = None):
        self.rcl_Loop = rcl_Loop
        self.rcl_Loop15 = rcl_Loop15
        
        pass
    @property
    def rcl_Loop15(self):
        return self.__rcl_Loop15

    @rcl_Loop15.setter
    def rcl_Loop15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Loop__rcl_Loop15", None)
        self.__rcl_Loop15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_RclBlock16"):
                opp_val = getattr(old_value, "rcl_RclBlock16", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RclBlock16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RclBlock16"):
                opp_val = getattr(value, "rcl_RclBlock16", None)
                setattr(value, "rcl_RclBlock16", self)

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
            if hasattr(old_value, "rcl_RoverExpression13"):
                opp_val = getattr(old_value, "rcl_RoverExpression13", None)
                if opp_val == self:
                    setattr(old_value, "rcl_RoverExpression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_RoverExpression13"):
                opp_val = getattr(value, "rcl_RoverExpression13", None)
                setattr(value, "rcl_RoverExpression13", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_Action(Statement):

    pass
class rcl_VarRef(NumberValue, BooleanValue, Statement, StringValue):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_Statement(ABC):

    def __init__(self, Statement: "rcl_RclBlock" = None, stmts: "rcl_RclBlock" = None):
        self.Statement = Statement
        self.stmts = stmts
        
        pass
    @property
    def stmts(self):
        return self.__stmts

    @stmts.setter
    def stmts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Statement__stmts", None)
        self.__stmts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RclBlock"):
                opp_val = getattr(old_value, "RclBlock", None)
                if opp_val == self:
                    setattr(old_value, "RclBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RclBlock"):
                opp_val = getattr(value, "RclBlock", None)
                setattr(value, "RclBlock", self)

    @property
    def Statement(self):
        return self.__Statement

    @Statement.setter
    def Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_Statement__Statement", None)
        self.__Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enclosing"):
                opp_val = getattr(old_value, "enclosing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enclosing"):
                opp_val = getattr(value, "enclosing", None)
                if opp_val is None:
                    setattr(value, "enclosing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eval(self):
        # TODO: Implement eval method
        pass

    def getProgram(self) :
        # TODO: Implement getProgram method
        pass

class rcl_RclBlock(Statement):

    def __init__(self, rcl_RclBlock: "rcl_RoverProgram" = None, rcl_RclBlock8: "rcl_Conditional" = None, rcl_RclBlock11: "rcl_Conditional" = None, rcl_RclBlock16: "rcl_Loop" = None, enclosing: set["rcl_Statement"] = None, RclBlock: "rcl_Statement" = None):
        self.rcl_RclBlock = rcl_RclBlock
        self.rcl_RclBlock8 = rcl_RclBlock8
        self.rcl_RclBlock11 = rcl_RclBlock11
        self.rcl_RclBlock16 = rcl_RclBlock16
        self.enclosing = enclosing if enclosing is not None else set()
        self.RclBlock = RclBlock
        
        pass
    @property
    def rcl_RclBlock11(self):
        return self.__rcl_RclBlock11

    @rcl_RclBlock11.setter
    def rcl_RclBlock11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__rcl_RclBlock11", None)
        self.__rcl_RclBlock11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_Conditional10"):
                opp_val = getattr(old_value, "rcl_Conditional10", None)
                if opp_val == self:
                    setattr(old_value, "rcl_Conditional10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_Conditional10"):
                opp_val = getattr(value, "rcl_Conditional10", None)
                setattr(value, "rcl_Conditional10", self)

    @property
    def rcl_RclBlock16(self):
        return self.__rcl_RclBlock16

    @rcl_RclBlock16.setter
    def rcl_RclBlock16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__rcl_RclBlock16", None)
        self.__rcl_RclBlock16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_Loop15"):
                opp_val = getattr(old_value, "rcl_Loop15", None)
                if opp_val == self:
                    setattr(old_value, "rcl_Loop15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_Loop15"):
                opp_val = getattr(value, "rcl_Loop15", None)
                setattr(value, "rcl_Loop15", self)

    @property
    def RclBlock(self):
        return self.__RclBlock

    @RclBlock.setter
    def RclBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__RclBlock", None)
        self.__RclBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stmts"):
                opp_val = getattr(old_value, "stmts", None)
                if opp_val == self:
                    setattr(old_value, "stmts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stmts"):
                opp_val = getattr(value, "stmts", None)
                setattr(value, "stmts", self)

    @property
    def enclosing(self):
        return self.__enclosing

    @enclosing.setter
    def enclosing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__enclosing", None)
        self.__enclosing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    setattr(item, "Statement", self)
                    

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
    def rcl_RclBlock8(self):
        return self.__rcl_RclBlock8

    @rcl_RclBlock8.setter
    def rcl_RclBlock8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rcl_RclBlock__rcl_RclBlock8", None)
        self.__rcl_RclBlock8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rcl_Conditional7"):
                opp_val = getattr(old_value, "rcl_Conditional7", None)
                if opp_val == self:
                    setattr(old_value, "rcl_Conditional7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rcl_Conditional7"):
                opp_val = getattr(value, "rcl_Conditional7", None)
                setattr(value, "rcl_Conditional7", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class rcl_Param:

    def __init__(self, name: str, rcl_Param: "rcl_RoverProgram" = None):
        self.name = name
        self.rcl_Param = rcl_Param
        
        pass
    @property
    def name(self):
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
        
        pass
    @property
    def name(self):
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

    def bindVar(self, rcl_n, rcl_v):
        # TODO: Implement bindVar method
        pass

    def getVar(self, rcl_n) :
        # TODO: Implement getVar method
        pass

    def run(self):
        # TODO: Implement run method
        pass
