from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Action:

    pass
class RobotWork_GoForward(Action):

    def __init__(self, cm: int):
        self.cm = cm
        
    @property
    def cm(self) -> int:
        return self.__cm

    @cm.setter
    def cm(self, cm: int):
        self.__cm = cm

class RobotWork_Rotate(Action):

    def __init__(self, degrees: int, random: bool):
        self.degrees = degrees
        self.random = random
        
    @property
    def random(self) -> bool:
        return self.__random

    @random.setter
    def random(self, random: bool):
        self.__random = random

    @property
    def degrees(self) -> int:
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: int):
        self.__degrees = degrees

class RobotWork_Release(Action):

    pass
class RobotWork_Grab(Action):

    pass
class Instruction:

    pass
class RobotWork_Chrography(Instruction):

    def __init__(self, name: str, RobotWork_Chrography: set["RobotWork_Instruction"] = None):
        self.name = name
        self.RobotWork_Chrography = RobotWork_Chrography if RobotWork_Chrography is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RobotWork_Chrography(self):
        return self.__RobotWork_Chrography

    @RobotWork_Chrography.setter
    def RobotWork_Chrography(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RobotWork_Chrography__RobotWork_Chrography", None)
        self.__RobotWork_Chrography = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RobotWork_Instruction"):
                    opp_val = getattr(item, "RobotWork_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "RobotWork_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RobotWork_Instruction"):
                    opp_val = getattr(item, "RobotWork_Instruction", None)
                    
                    setattr(item, "RobotWork_Instruction", self)
                    

class RobotWork_Action(Instruction):

    pass
class RobotWork_Instruction(ABC):

    pass