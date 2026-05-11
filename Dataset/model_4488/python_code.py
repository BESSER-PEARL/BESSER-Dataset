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
            if hasattr(old_value, "model_Block10"):
                opp_val = getattr(old_value, "model_Block10", None)
                if opp_val == self:
                    setattr(old_value, "model_Block10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Block10"):
                opp_val = getattr(value, "model_Block10", None)
                setattr(value, "model_Block10", self)

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
class model_Ozobot(NamedElement):

    def __init__(self, xposition: float, yposition: float, orientation: float, model_Ozobot: set["model_OzobotProgram"] = None):
        self.xposition = xposition
        self.yposition = yposition
        self.orientation = orientation
        self.model_Ozobot = model_Ozobot if model_Ozobot is not None else set()
        
        pass
    @property
    def xposition(self):
        return self.__xposition

    @xposition.setter
    def xposition(self, xposition: float):
        self.__xposition = xposition


    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: float):
        self.__orientation = orientation


    @property
    def yposition(self):
        return self.__yposition

    @yposition.setter
    def yposition(self, yposition: float):
        self.__yposition = yposition


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
                if hasattr(item, "model_OzobotProgram12"):
                    opp_val = getattr(item, "model_OzobotProgram12", None)
                    
                    if opp_val == self:
                        setattr(item, "model_OzobotProgram12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_OzobotProgram12"):
                    opp_val = getattr(item, "model_OzobotProgram12", None)
                    
                    setattr(item, "model_OzobotProgram12", self)
                    

class model_Transition(NamedElement):

    pass
class model_Command(NamedElement):

    def __init__(self, message: str, model_Command: "model_OzobotProgram" = None, model_Command5: "model_OzobotProgram" = None, source: "model_Transition" = None, target: "model_Transition" = None, model_Command15: "model_Block" = None, Command: "model_Transition" = None, Command20: "model_Transition" = None):
        self.message = message
        self.model_Command = model_Command
        self.model_Command5 = model_Command5
        self.source = source
        self.target = target
        self.model_Command15 = model_Command15
        self.Command = Command
        self.Command20 = Command20
        
        pass
    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__source", None)
        self.__source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition"):
                opp_val = getattr(old_value, "Transition", None)
                if opp_val == self:
                    setattr(old_value, "Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition"):
                opp_val = getattr(value, "Transition", None)
                setattr(value, "Transition", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__target", None)
        self.__target = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition8"):
                opp_val = getattr(old_value, "Transition8", None)
                if opp_val == self:
                    setattr(old_value, "Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition8"):
                opp_val = getattr(value, "Transition8", None)
                setattr(value, "Transition8", self)

    @property
    def Command20(self):
        return self.__Command20

    @Command20.setter
    def Command20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__Command20", None)
        self.__Command20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

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
    def Command(self):
        return self.__Command

    @Command.setter
    def Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__Command", None)
        self.__Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def model_Command15(self):
        return self.__model_Command15

    @model_Command15.setter
    def model_Command15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Command__model_Command15", None)
        self.__model_Command15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Block14"):
                opp_val = getattr(old_value, "model_Block14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Block14"):
                opp_val = getattr(value, "model_Block14", None)
                if opp_val is None:
                    setattr(value, "model_Block14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

