from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ESensor(Enum):
    distanceFRF = "distanceFRF"
    distanceFRB = "distanceFRB"
    distanceR = "distanceR"
    distanceBR = "distanceBR"
    distanceFLB = "distanceFLB"
    distanceFLF = "distanceFLF"
    lightFRF = "lightFRF"
    lightFRB = "lightFRB"
    lightR = "lightR"
    lightBR = "lightBR"
    lightBL = "lightBL"
    lightL = "lightL"
    lightFLB = "lightFLB"
    lightFLF = "lightFLF"
    distanceBL = "distanceBL"
    distanceL = "distanceL"
class EOperator(Enum):
    GT = "GT"
    LT = "LT"
    EQ = "EQ"
    DIFF = "DIFF"
    GTE = "GTE"
    LTE = "LTE"
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class Condition:

    pass
class robot_Compare(Condition):

    pass
class robot_Value(Condition):

    pass
class Var:

    pass
class robot_Declaration(Var):

    pass
class robot_Affectation(Var):

    pass
class Operator:

    pass
class robot_Different(Operator):

    pass
class robot_Operator:

    def __init__(self, type: str, robot_Operator: "robot_Compare" = None):
        self.type = type
        self.robot_Operator = robot_Operator
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def robot_Operator(self):
        return self.__robot_Operator

    @robot_Operator.setter
    def robot_Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robot_Operator__robot_Operator", None)
        self.__robot_Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robot_Compare"):
                opp_val = getattr(old_value, "robot_Compare", None)
                if opp_val == self:
                    setattr(old_value, "robot_Compare", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robot_Compare"):
                opp_val = getattr(value, "robot_Compare", None)
                setattr(value, "robot_Compare", self)

class Values:

    pass
class robot_Variable(Values):

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class robot_TFloat(Values):

    def __init__(self, Value: str):
        self.Value = Value
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

class robot_TBoolean(Values):

    def __init__(self, Value: str):
        self.Value = Value
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

class robot_TInteger(Values):

    def __init__(self, Value: str):
        self.Value = Value
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

class robot_TString(Values):

    def __init__(self, Value: str):
        self.Value = Value
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

class robot_Sensor(Values):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class robot_Values:

    pass
class robot_Condition:

    pass
class Movement:

    pass
class robot_Sleep(Movement):

    pass
class robot_Backward(Movement):

    pass
class robot_TurnRight(Movement):

    pass
class robot_TurnLeft(Movement):

    pass
class robot_Stop(Movement):

    pass
class robot_Forward(Movement):

    pass
class robot_Operation:

    pass
class Operation:

    pass
class robot_Alternative(Operation):

    pass
class robot_Echo(Operation):

    def __init__(self, param: str):
        self.param = param
        
    @property
    def param(self) -> str:
        return self.__param

    @param.setter
    def param(self, param: str):
        self.__param = param

class robot_Event(Operation):

    pass
class robot_While(Operation):

    pass
class robot_Whenever(Operation):

    pass
class robot_Movement(Operation):

    def __init__(self, duration: float):
        self.duration = duration
        
    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

class robot_Var(Operation):

    def __init__(self, Name: str, robot_Var: "robot_Values" = None):
        self.Name = Name
        self.robot_Var = robot_Var
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def robot_Var(self):
        return self.__robot_Var

    @robot_Var.setter
    def robot_Var(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robot_Var__robot_Var", None)
        self.__robot_Var = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robot_Values"):
                opp_val = getattr(old_value, "robot_Values", None)
                if opp_val == self:
                    setattr(old_value, "robot_Values", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robot_Values"):
                opp_val = getattr(value, "robot_Values", None)
                setattr(value, "robot_Values", self)

class robot_Sequence(Operation):

    pass
class robot_Mission:

    pass