from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class JumpType(Enum):
    JUMP_LONG = "JUMP_LONG"
    JUMP_HIGH = "JUMP_HIGH"
    JUMP_MAX = "JUMP_MAX"


############################################
# Definition of Classes
############################################

class Instruction:

    pass
class minidrone_Turn(Instruction):

    def __init__(self, angle: int):
        self.angle = angle
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

class minidrone_Jump(Instruction):

    def __init__(self, jumpType: str):
        self.jumpType = jumpType
        
    @property
    def jumpType(self) -> str:
        return self.__jumpType

    @jumpType.setter
    def jumpType(self, jumpType: str):
        self.__jumpType = jumpType

class minidrone_Go(Instruction):

    def __init__(self, distance: int):
        self.distance = distance
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

class minidrone_Instruction(ABC):

    pass
class minidrone_MiniDroneProgram:

    def __init__(self, name: str, minidrone_MiniDroneProgram: set["minidrone_Instruction"] = None):
        self.name = name
        self.minidrone_MiniDroneProgram = minidrone_MiniDroneProgram if minidrone_MiniDroneProgram is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minidrone_MiniDroneProgram(self):
        return self.__minidrone_MiniDroneProgram

    @minidrone_MiniDroneProgram.setter
    def minidrone_MiniDroneProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minidrone_MiniDroneProgram__minidrone_MiniDroneProgram", None)
        self.__minidrone_MiniDroneProgram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minidrone_Instruction"):
                    opp_val = getattr(item, "minidrone_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "minidrone_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minidrone_Instruction"):
                    opp_val = getattr(item, "minidrone_Instruction", None)
                    
                    setattr(item, "minidrone_Instruction", self)
                    
