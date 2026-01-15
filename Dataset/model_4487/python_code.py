from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    left = "left"
    right = "right"
class Velocity(Enum):
    very_slow = "very_slow"
    slow = "slow"
    medium = "medium"
    fast = "fast"
    very_fast = "very_fast"
class Color(Enum):
    none = "none"
    red = "red"
    green = "green"
    blue = "blue"
    yellow = "yellow"


############################################
# Definition of Classes
############################################

class Command:

    pass
class model_Rotate(Command):

    def __init__(self, direction: str, velocity: str, angle: float):
        self.direction = direction
        self.velocity = velocity
        self.angle = angle
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def velocity(self) -> str:
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: str):
        self.__velocity = velocity

    @property
    def angle(self) -> float:
        return self.__angle

    @angle.setter
    def angle(self, angle: float):
        self.__angle = angle

class model_Light(Command):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class model_Wait(Command):

    def __init__(self, time: int):
        self.time = time
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

class model_Repeat(Command):

    def __init__(self, count: int, model_Repeat: "model_Block" = None):
        self.count = count
        self.model_Repeat = model_Repeat
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def model_Repeat(self):
        return self.__model_Repeat

    @model_Repeat.setter
    def model_Repeat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Repeat__model_Repeat", None)
        self.__model_Repeat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Block12"):
                opp_val = getattr(old_value, "model_Block12", None)
                if opp_val == self:
                    setattr(old_value, "model_Block12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Block12"):
                opp_val = getattr(value, "model_Block12", None)
                setattr(value, "model_Block12", self)

class model_Move(Command):

    def __init__(self, distance: int, velocity: str):
        self.distance = distance
        self.velocity = velocity
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

    @property
    def velocity(self) -> str:
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: str):
        self.__velocity = velocity

class NamedElement:

    pass
class model_Command(NamedElement):

    def __init__(self, message: str, model_Command: "model_OzobotProgram" = None, model_Command5: "model_OzobotProgram" = None, : "model_Transition" = None, 9: "model_Transition" = None, model_Command17: "model_Block" = None, 22: "model_Transition" = None, 25: "model_Transition" = None):
        self.message = message
        self.model_Command = model_Command
        self.model_Command5 = model_Command5
        self. = 
        self.9 = 9
        self.model_Command17 = model_Command17
        self.22 = 22
        self.25 = 25
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "7"):
                opp_val = getattr(old_value, "7", None)
                if opp_val == self:
                    setattr(old_value, "7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "7"):
                opp_val = getattr(value, "7", None)
                setattr(value, "7", self)

    @property
    def model_Command(self):
        return self.__model_Command

    @model_Command.setter
    def model_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__model_Command", None)
        self.__model_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OzobotProgram2"):
                opp_val = getattr(old_value, "model_OzobotProgram2", None)
                if opp_val == self:
                    setattr(old_value, "model_OzobotProgram2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OzobotProgram2"):
                opp_val = getattr(value, "model_OzobotProgram2", None)
                setattr(value, "model_OzobotProgram2", self)

    @property
    def 25(self):
        return self.__25

    @25.setter
    def 25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__25", None)
        self.__25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "24"):
                opp_val = getattr(old_value, "24", None)
                if opp_val == self:
                    setattr(old_value, "24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "24"):
                opp_val = getattr(value, "24", None)
                setattr(value, "24", self)

    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__9", None)
        self.__9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "10"):
                opp_val = getattr(old_value, "10", None)
                if opp_val == self:
                    setattr(old_value, "10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "10"):
                opp_val = getattr(value, "10", None)
                setattr(value, "10", self)

    @property
    def 22(self):
        return self.__22

    @22.setter
    def 22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__22", None)
        self.__22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "21"):
                opp_val = getattr(old_value, "21", None)
                if opp_val == self:
                    setattr(old_value, "21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "21"):
                opp_val = getattr(value, "21", None)
                setattr(value, "21", self)

    @property
    def model_Command5(self):
        return self.__model_Command5

    @model_Command5.setter
    def model_Command5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__model_Command5", None)
        self.__model_Command5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_OzobotProgram4"):
                opp_val = getattr(old_value, "model_OzobotProgram4", None)
                if opp_val == self:
                    setattr(old_value, "model_OzobotProgram4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_OzobotProgram4"):
                opp_val = getattr(value, "model_OzobotProgram4", None)
                setattr(value, "model_OzobotProgram4", self)

    @property
    def model_Command17(self):
        return self.__model_Command17

    @model_Command17.setter
    def model_Command17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__model_Command17", None)
        self.__model_Command17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Block16"):
                opp_val = getattr(old_value, "model_Block16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Block16"):
                opp_val = getattr(value, "model_Block16", None)
                if opp_val is None:
                    setattr(value, "model_Block16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Transition(NamedElement):

    pass
class model_Block(NamedElement):

    pass
class model_Ozobot(NamedElement):

    def __init__(self, xposition: float, yposition: float, orientation: float, model_Ozobot: set["model_OzobotProgram"] = None):
        self.xposition = xposition
        self.yposition = yposition
        self.orientation = orientation
        self.model_Ozobot = model_Ozobot if model_Ozobot is not None else set()
        
    @property
    def yposition(self) -> float:
        return self.__yposition

    @yposition.setter
    def yposition(self, yposition: float):
        self.__yposition = yposition

    @property
    def orientation(self) -> float:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: float):
        self.__orientation = orientation

    @property
    def xposition(self) -> float:
        return self.__xposition

    @xposition.setter
    def xposition(self, xposition: float):
        self.__xposition = xposition

    @property
    def model_Ozobot(self):
        return self.__model_Ozobot

    @model_Ozobot.setter
    def model_Ozobot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Ozobot__model_Ozobot", None)
        self.__model_Ozobot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_OzobotProgram14"):
                    opp_val = getattr(item, "model_OzobotProgram14", None)
                    
                    if opp_val == self:
                        setattr(item, "model_OzobotProgram14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_OzobotProgram14"):
                    opp_val = getattr(item, "model_OzobotProgram14", None)
                    
                    setattr(item, "model_OzobotProgram14", self)
                    

class model_OzobotProgram(NamedElement):

    pass
class model_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
