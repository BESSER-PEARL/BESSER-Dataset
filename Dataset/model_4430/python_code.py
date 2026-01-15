from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SuccessState(Enum):
    Success = "Success"
    Failure = "Failure"
    Running = "Running"
class BumperKind(Enum):
    Left = "Left"
    Right = "Right"
class FailureState(Enum):
    Failure = "Failure"
    Success = "Success"
    Running = "Running"
class RunningState(Enum):
    Success = "Success"
    Failure = "Failure"
    Running = "Running"
class DistanceKind(Enum):
    Minor = "Minor"
    Major = "Major"
class LightStatus(Enum):
    On = "On"
    Off = "Off"


############################################
# Definition of Classes
############################################

class Actuate:

    pass
class gyro_Servo(Actuate):

    def __init__(self, minimalPosition: int, maximalPosition: int, step: int):
        self.minimalPosition = minimalPosition
        self.maximalPosition = maximalPosition
        self.step = step
        
    @property
    def step(self) -> int:
        return self.__step

    @step.setter
    def step(self, step: int):
        self.__step = step

    @property
    def minimalPosition(self) -> int:
        return self.__minimalPosition

    @minimalPosition.setter
    def minimalPosition(self, minimalPosition: int):
        self.__minimalPosition = minimalPosition

    @property
    def maximalPosition(self) -> int:
        return self.__maximalPosition

    @maximalPosition.setter
    def maximalPosition(self, maximalPosition: int):
        self.__maximalPosition = maximalPosition

class gyro_LED(Actuate):

    def __init__(self, status: str):
        self.status = status
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

class gyro_Motor(Actuate):

    def __init__(self, leftMotor: int, rightMotor: int):
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        
    @property
    def leftMotor(self) -> int:
        return self.__leftMotor

    @leftMotor.setter
    def leftMotor(self, leftMotor: int):
        self.__leftMotor = leftMotor

    @property
    def rightMotor(self) -> int:
        return self.__rightMotor

    @rightMotor.setter
    def rightMotor(self, rightMotor: int):
        self.__rightMotor = rightMotor

class gyro_Sibling:

    pass
class gyro_Child:

    pass
class gyro_Node(ABC):

    def __init__(self, name: str, gyro_Node9: "gyro_Child" = None, gyro_Node12: "gyro_Sibling" = None, gyro_Node15: "gyro_Sibling" = None, gyro_Node: "gyro_GyroSpecification" = None):
        self.name = name
        self.gyro_Node9 = gyro_Node9
        self.gyro_Node12 = gyro_Node12
        self.gyro_Node15 = gyro_Node15
        self.gyro_Node = gyro_Node
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gyro_Node9(self):
        return self.__gyro_Node9

    @gyro_Node9.setter
    def gyro_Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gyro_Node__gyro_Node9", None)
        self.__gyro_Node9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gyro_Child8"):
                opp_val = getattr(old_value, "gyro_Child8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gyro_Child8"):
                opp_val = getattr(value, "gyro_Child8", None)
                if opp_val is None:
                    setattr(value, "gyro_Child8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gyro_Node15(self):
        return self.__gyro_Node15

    @gyro_Node15.setter
    def gyro_Node15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gyro_Node__gyro_Node15", None)
        self.__gyro_Node15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gyro_Sibling14"):
                opp_val = getattr(old_value, "gyro_Sibling14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gyro_Sibling14"):
                opp_val = getattr(value, "gyro_Sibling14", None)
                if opp_val is None:
                    setattr(value, "gyro_Sibling14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gyro_Node12(self):
        return self.__gyro_Node12

    @gyro_Node12.setter
    def gyro_Node12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gyro_Node__gyro_Node12", None)
        self.__gyro_Node12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gyro_Sibling11"):
                opp_val = getattr(old_value, "gyro_Sibling11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gyro_Sibling11"):
                opp_val = getattr(value, "gyro_Sibling11", None)
                if opp_val is None:
                    setattr(value, "gyro_Sibling11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gyro_Node(self):
        return self.__gyro_Node

    @gyro_Node.setter
    def gyro_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gyro_Node__gyro_Node", None)
        self.__gyro_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gyro_GyroSpecification"):
                opp_val = getattr(old_value, "gyro_GyroSpecification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gyro_GyroSpecification"):
                opp_val = getattr(value, "gyro_GyroSpecification", None)
                if opp_val is None:
                    setattr(value, "gyro_GyroSpecification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Condition:

    pass
class gyro_Waiting(Condition):

    def __init__(self, time: int):
        self.time = time
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

class gyro_Bumpers(Condition):

    def __init__(self, bumperKind: str):
        self.bumperKind = bumperKind
        
    @property
    def bumperKind(self) -> str:
        return self.__bumperKind

    @bumperKind.setter
    def bumperKind(self, bumperKind: str):
        self.__bumperKind = bumperKind

class gyro_Distance(Condition):

    def __init__(self, value: int, kind: str):
        self.value = value
        self.kind = kind
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Action:

    pass
class gyro_Actuate(Action):

    pass
class gyro_Condition(Action):

    pass
class Behavior:

    pass
class gyro_Sequential(Behavior):

    pass
class gyro_Parallel(Behavior):

    pass
class gyro_StatusChange(Behavior):

    def __init__(self, changeSuccess: str, changeFailure: str, changeRunning: str):
        self.changeSuccess = changeSuccess
        self.changeFailure = changeFailure
        self.changeRunning = changeRunning
        
    @property
    def changeRunning(self) -> str:
        return self.__changeRunning

    @changeRunning.setter
    def changeRunning(self, changeRunning: str):
        self.__changeRunning = changeRunning

    @property
    def changeSuccess(self) -> str:
        return self.__changeSuccess

    @changeSuccess.setter
    def changeSuccess(self, changeSuccess: str):
        self.__changeSuccess = changeSuccess

    @property
    def changeFailure(self) -> str:
        return self.__changeFailure

    @changeFailure.setter
    def changeFailure(self, changeFailure: str):
        self.__changeFailure = changeFailure

class gyro_Priority(Behavior):

    pass
class Node:

    pass
class gyro_Action(Node):

    pass
class gyro_Behavior(Node):

    pass
class gyro_GyroSpecification:

    def __init__(self, name: str, gyro_GyroSpecification: set["gyro_Node"] = None, gyro_GyroSpecification2: set["gyro_Child"] = None, gyro_GyroSpecification4: set["gyro_Sibling"] = None):
        self.name = name
        self.gyro_GyroSpecification = gyro_GyroSpecification if gyro_GyroSpecification is not None else set()
        self.gyro_GyroSpecification2 = gyro_GyroSpecification2 if gyro_GyroSpecification2 is not None else set()
        self.gyro_GyroSpecification4 = gyro_GyroSpecification4 if gyro_GyroSpecification4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gyro_GyroSpecification4(self):
        return self.__gyro_GyroSpecification4

    @gyro_GyroSpecification4.setter
    def gyro_GyroSpecification4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gyro_GyroSpecification__gyro_GyroSpecification4", None)
        self.__gyro_GyroSpecification4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gyro_Sibling"):
                    opp_val = getattr(item, "gyro_Sibling", None)
                    
                    if opp_val == self:
                        setattr(item, "gyro_Sibling", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gyro_Sibling"):
                    opp_val = getattr(item, "gyro_Sibling", None)
                    
                    setattr(item, "gyro_Sibling", self)
                    

    @property
    def gyro_GyroSpecification(self):
        return self.__gyro_GyroSpecification

    @gyro_GyroSpecification.setter
    def gyro_GyroSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gyro_GyroSpecification__gyro_GyroSpecification", None)
        self.__gyro_GyroSpecification = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gyro_Node"):
                    opp_val = getattr(item, "gyro_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "gyro_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gyro_Node"):
                    opp_val = getattr(item, "gyro_Node", None)
                    
                    setattr(item, "gyro_Node", self)
                    

    @property
    def gyro_GyroSpecification2(self):
        return self.__gyro_GyroSpecification2

    @gyro_GyroSpecification2.setter
    def gyro_GyroSpecification2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gyro_GyroSpecification__gyro_GyroSpecification2", None)
        self.__gyro_GyroSpecification2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gyro_Child"):
                    opp_val = getattr(item, "gyro_Child", None)
                    
                    if opp_val == self:
                        setattr(item, "gyro_Child", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gyro_Child"):
                    opp_val = getattr(item, "gyro_Child", None)
                    
                    setattr(item, "gyro_Child", self)
                    
