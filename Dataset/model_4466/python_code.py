from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DistanceUnit(Enum):
    CENTIMETERS = "CENTIMETERS"
class AngleUnit(Enum):
    DEGREES = "DEGREES"
class DetectedType(Enum):
    NULL = "NULL"
    BALL = "BALL"
    WALL = "WALL"
class TimeUnit(Enum):
    SECONDS = "SECONDS"
    MILLISECONDS = "MILLISECONDS"


############################################
# Definition of Classes
############################################

class Angle:

    pass
class RobotProjectModel_HomeDirection(Angle):

    pass
class Condition:

    pass
class RobotProjectModel_DetectedObjectIs(Condition):

    def __init__(self, rightOperand: str):
        self.rightOperand = rightOperand
        
    @property
    def rightOperand(self) -> str:
        return self.__rightOperand

    @rightOperand.setter
    def rightOperand(self, rightOperand: str):
        self.__rightOperand = rightOperand

class RobotProjectModel_SensorActivation(Condition):

    pass
class RobotProjectModel_Condition(ABC):

    pass
class RobotProjectModel_Instruction(ABC):

    pass
class Amount:

    pass
class RobotProjectModel_Amount:

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class RobotProjectModel_Angle(Amount):

    def __init__(self, angleUnit: str, RobotProjectModel_Angle: "RobotProjectModel_Turn" = None):
        self.angleUnit = angleUnit
        self.RobotProjectModel_Angle = RobotProjectModel_Angle
        
    @property
    def angleUnit(self) -> str:
        return self.__angleUnit

    @angleUnit.setter
    def angleUnit(self, angleUnit: str):
        self.__angleUnit = angleUnit

    @property
    def RobotProjectModel_Angle(self):
        return self.__RobotProjectModel_Angle

    @RobotProjectModel_Angle.setter
    def RobotProjectModel_Angle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RobotProjectModel_Angle__RobotProjectModel_Angle", None)
        self.__RobotProjectModel_Angle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RobotProjectModel_Turn"):
                opp_val = getattr(old_value, "RobotProjectModel_Turn", None)
                if opp_val == self:
                    setattr(old_value, "RobotProjectModel_Turn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RobotProjectModel_Turn"):
                opp_val = getattr(value, "RobotProjectModel_Turn", None)
                setattr(value, "RobotProjectModel_Turn", self)

class RobotProjectModel_Duration(Amount):

    def __init__(self, timeUnit: str, RobotProjectModel_Duration: "RobotProjectModel_TimedInstruction" = None):
        self.timeUnit = timeUnit
        self.RobotProjectModel_Duration = RobotProjectModel_Duration
        
    @property
    def timeUnit(self) -> str:
        return self.__timeUnit

    @timeUnit.setter
    def timeUnit(self, timeUnit: str):
        self.__timeUnit = timeUnit

    @property
    def RobotProjectModel_Duration(self):
        return self.__RobotProjectModel_Duration

    @RobotProjectModel_Duration.setter
    def RobotProjectModel_Duration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RobotProjectModel_Duration__RobotProjectModel_Duration", None)
        self.__RobotProjectModel_Duration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RobotProjectModel_TimedInstruction"):
                opp_val = getattr(old_value, "RobotProjectModel_TimedInstruction", None)
                if opp_val == self:
                    setattr(old_value, "RobotProjectModel_TimedInstruction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RobotProjectModel_TimedInstruction"):
                opp_val = getattr(value, "RobotProjectModel_TimedInstruction", None)
                setattr(value, "RobotProjectModel_TimedInstruction", self)

class Instruction:

    pass
class RobotProjectModel_Print(Instruction):

    def __init__(self, string: str):
        self.string = string
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

class RobotProjectModel_InstructionBlock(Instruction):

    pass
class RobotProjectModel_Release(Instruction):

    pass
class RobotProjectModel_If(Instruction):

    pass
class RobotProjectModel_Function(Instruction):

    def __init__(self, name: str, RobotProjectModel_Function: "RobotProjectModel_InstructionBlock" = None, RobotProjectModel_Function6: "RobotProjectModel_Call" = None):
        self.name = name
        self.RobotProjectModel_Function = RobotProjectModel_Function
        self.RobotProjectModel_Function6 = RobotProjectModel_Function6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RobotProjectModel_Function(self):
        return self.__RobotProjectModel_Function

    @RobotProjectModel_Function.setter
    def RobotProjectModel_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RobotProjectModel_Function__RobotProjectModel_Function", None)
        self.__RobotProjectModel_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RobotProjectModel_InstructionBlock"):
                opp_val = getattr(old_value, "RobotProjectModel_InstructionBlock", None)
                if opp_val == self:
                    setattr(old_value, "RobotProjectModel_InstructionBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RobotProjectModel_InstructionBlock"):
                opp_val = getattr(value, "RobotProjectModel_InstructionBlock", None)
                setattr(value, "RobotProjectModel_InstructionBlock", self)

    @property
    def RobotProjectModel_Function6(self):
        return self.__RobotProjectModel_Function6

    @RobotProjectModel_Function6.setter
    def RobotProjectModel_Function6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RobotProjectModel_Function__RobotProjectModel_Function6", None)
        self.__RobotProjectModel_Function6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RobotProjectModel_Call"):
                opp_val = getattr(old_value, "RobotProjectModel_Call", None)
                if opp_val == self:
                    setattr(old_value, "RobotProjectModel_Call", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RobotProjectModel_Call"):
                opp_val = getattr(value, "RobotProjectModel_Call", None)
                setattr(value, "RobotProjectModel_Call", self)

class RobotProjectModel_Call(Instruction):

    pass
class RobotProjectModel_Grab(Instruction):

    pass
class RobotProjectModel_TimedInstruction(Instruction):

    pass
class RobotProjectModel_Robot:

    pass
class RobotProjectModel_Distance(Amount):

    def __init__(self, distanceUnit: str, RobotProjectModel_Distance: "RobotProjectModel_MoveStraight" = None):
        self.distanceUnit = distanceUnit
        self.RobotProjectModel_Distance = RobotProjectModel_Distance
        
    @property
    def distanceUnit(self) -> str:
        return self.__distanceUnit

    @distanceUnit.setter
    def distanceUnit(self, distanceUnit: str):
        self.__distanceUnit = distanceUnit

    @property
    def RobotProjectModel_Distance(self):
        return self.__RobotProjectModel_Distance

    @RobotProjectModel_Distance.setter
    def RobotProjectModel_Distance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RobotProjectModel_Distance__RobotProjectModel_Distance", None)
        self.__RobotProjectModel_Distance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RobotProjectModel_MoveStraight"):
                opp_val = getattr(old_value, "RobotProjectModel_MoveStraight", None)
                if opp_val == self:
                    setattr(old_value, "RobotProjectModel_MoveStraight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RobotProjectModel_MoveStraight"):
                opp_val = getattr(value, "RobotProjectModel_MoveStraight", None)
                setattr(value, "RobotProjectModel_MoveStraight", self)

class TimedInstruction:

    pass
class RobotProjectModel_Turn(TimedInstruction):

    pass
class RobotProjectModel_Wait(TimedInstruction):

    pass
class RobotProjectModel_MoveStraight(TimedInstruction):

    pass