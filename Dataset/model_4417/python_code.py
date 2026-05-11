from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    YELLOW = "YELLOW"
    MAGENTA = "MAGENTA"
    ORANGE = "ORANGE"
    WHITE = "WHITE"
    BLACK = "BLACK"
    PINK = "PINK"
    GRAY = "GRAY"
    LIGHT_GRAY = "LIGHT_GRAY"
    DARK_GRAY = "DARK_GRAY"
    CYAN = "CYAN"
    BROWN = "BROWN"
    NONE = "NONE"
class OperatorKind(Enum):
    equal = "equal"
    notEqual = "notEqual"
    upperOrEqual = "upperOrEqual"
    lowerOrEqual = "lowerOrEqual"


############################################
# Definition of Classes
############################################

class Sensor:

    pass
class mindstorms_UltrasonicSensor(Sensor):

    def __init__(self, operator: str, value: float):
        self.operator = operator
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


class mindstorms_ColorSensor(Sensor):

    def __init__(self, color: str):
        self.color = color
        
        pass
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


class mindstorms_TouchSensor(Sensor):

    def __init__(self, isPressed: bool):
        self.isPressed = isPressed
        
        pass
    @property
    def isPressed(self):
        return self.__isPressed

    @isPressed.setter
    def isPressed(self, isPressed: bool):
        self.__isPressed = isPressed


class Action:

    pass
class mindstorms_GoBackward(Action):

    def __init__(self, cm: int, infinite: bool):
        self.cm = cm
        self.infinite = infinite
        
        pass
    @property
    def infinite(self):
        return self.__infinite

    @infinite.setter
    def infinite(self, infinite: bool):
        self.__infinite = infinite


    @property
    def cm(self):
        return self.__cm

    @cm.setter
    def cm(self, cm: int):
        self.__cm = cm


class mindstorms_Rotate(Action):

    def __init__(self, degrees: int, random: bool):
        self.degrees = degrees
        self.random = random
        
        pass
    @property
    def degrees(self):
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: int):
        self.__degrees = degrees


    @property
    def random(self):
        return self.__random

    @random.setter
    def random(self, random: bool):
        self.__random = random


class mindstorms_GoTo(Action):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        pass
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


class mindstorms_Release(Action):

    pass
class mindstorms_Grab(Action):

    pass
class mindstorms_Delay(Action):

    def __init__(self, ms: int):
        self.ms = ms
        
        pass
    @property
    def ms(self):
        return self.__ms

    @ms.setter
    def ms(self, ms: int):
        self.__ms = ms


class mindstorms_ReturnToBase(Action):

    pass
class mindstorms_GoForward(Action):

    def __init__(self, cm: int, infinite: bool):
        self.cm = cm
        self.infinite = infinite
        
        pass
    @property
    def infinite(self):
        return self.__infinite

    @infinite.setter
    def infinite(self, infinite: bool):
        self.__infinite = infinite


    @property
    def cm(self):
        return self.__cm

    @cm.setter
    def cm(self, cm: int):
        self.__cm = cm


class ConditionalFlow:

    pass
class mindstorms_While(ConditionalFlow):

    pass
class mindstorms_If(ConditionalFlow):

    pass
class Condition:

    pass
class mindstorms_Sensor(Condition):

    pass
class mindstorms_Condition(ABC):

    pass
class Flow:

    pass
class mindstorms_ConditionalFlow(Flow):

    pass
class mindstorms_Choregraphy(Flow):

    def __init__(self, name: str, mindstorms_Choregraphy: "mindstorms_Reuse" = None):
        self.name = name
        self.mindstorms_Choregraphy = mindstorms_Choregraphy
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def mindstorms_Choregraphy(self):
        return self.__mindstorms_Choregraphy

    @mindstorms_Choregraphy.setter
    def mindstorms_Choregraphy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mindstorms_Choregraphy__mindstorms_Choregraphy", None)
        self.__mindstorms_Choregraphy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mindstorms_Reuse"):
                opp_val = getattr(old_value, "mindstorms_Reuse", None)
                if opp_val == self:
                    setattr(old_value, "mindstorms_Reuse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mindstorms_Reuse"):
                opp_val = getattr(value, "mindstorms_Reuse", None)
                setattr(value, "mindstorms_Reuse", self)

class Instruction:

    pass
class mindstorms_Reuse(Instruction):

    pass
class mindstorms_Action(Instruction):

    pass
class mindstorms_Flow(Instruction):

    pass
class mindstorms_Instruction(ABC):

    pass