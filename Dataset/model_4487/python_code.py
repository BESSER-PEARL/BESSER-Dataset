from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class Direction(Enum):
    left = "left"
    right = "right"


############################################
# Definition of Classes
############################################

class Command:

    pass
class model_Repeat(Command):

    def __init__(self, count: int, model_Repeat: "model_Block" = None):
        self.count = count
        self.model_Repeat = model_Repeat
        
        pass
    @property
    def count(self):
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
            if hasattr(old_value, "model_Block7"):
                opp_val = getattr(old_value, "model_Block7", None)
                if opp_val == self:
                    setattr(old_value, "model_Block7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Block7"):
                opp_val = getattr(value, "model_Block7", None)
                setattr(value, "model_Block7", self)

class model_Rotate(Command):

    def __init__(self, direction: str, velocity: str, angle: float):
        self.direction = direction
        self.velocity = velocity
        self.angle = angle
        
        pass
    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: str):
        self.__velocity = velocity


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: float):
        self.__angle = angle


class model_Light(Command):

    def __init__(self, color: str):
        self.color = color
        
        pass
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


class model_Wait(Command):

    def __init__(self, time: int):
        self.time = time
        
        pass
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time


class model_Move(Command):

    def __init__(self, distance: int, velocity: str):
        self.distance = distance
        self.velocity = velocity
        
        pass
    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: str):
        self.__velocity = velocity


    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance


class NamedElement:

    pass
class model_Transition(NamedElement):

    pass
class model_Command(NamedElement):

    pass
class model_Ozobot(NamedElement):

    pass
class model_Block(NamedElement):

    pass
class model_OzobotProgram(NamedElement):

    pass
class model_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

