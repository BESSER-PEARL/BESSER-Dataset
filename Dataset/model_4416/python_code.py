from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
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
    RED = "RED"
    GREEN = "GREEN"
class OperatorKind(Enum):
    equal = "equal"
    notEqual = "notEqual"
    upperOrEqual = "upperOrEqual"
    lowerOrEqual = "lowerOrEqual"


############################################
# Definition of Classes
############################################

class Condition:

    pass
class Block:

    pass
class mindstorms_Action(Block):

    pass
class mindstorms_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Sensor:

    pass
class mindstorms_UltrasonicSensor(Sensor):

    def __init__(self, operator: str, value: float):
        self.operator = operator
        self.value = value
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


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


class Behavior:

    pass
class mindstorms_ExploreForward(Behavior):

    pass
class mindstorms_ReturnBottleToBase(Behavior):

    pass
class mindstorms_AvoidObstacle(Behavior):

    pass
class mindstorms_ConditionContainer(ABC):

    pass
class ConditionContainer:

    pass
class BlockContainer:

    pass
class mindstorms_Flow(BlockContainer, ConditionContainer, Block):

    pass
class Instruction:

    pass
class mindstorms_Arbitrator(Instruction, ConditionContainer):

    pass
class mindstorms_ReuseInstruction(Instruction):

    pass
class mindstorms_Procedure(Instruction, BlockContainer):

    pass
class mindstorms_Block(Instruction):

    pass
class mindstorms_BlockContainer(ABC):

    pass
class NamedElement:

    pass
class mindstorms_Behavior(BlockContainer, ConditionContainer, NamedElement):

    pass
class mindstorms_Sensor(NamedElement, Condition):

    pass
class mindstorms_Instruction(NamedElement):

    pass
class mindstorms_Main:

    pass
class Action:

    pass
class mindstorms_ReturnToBase(Action):

    pass
class mindstorms_Grab(Action):

    pass
class mindstorms_GoBackward(Action):

    def __init__(self, cm: int, infinite: bool):
        self.cm = cm
        self.infinite = infinite
        
        pass
    @property
    def cm(self):
        return self.__cm

    @cm.setter
    def cm(self, cm: int):
        self.__cm = cm


    @property
    def infinite(self):
        return self.__infinite

    @infinite.setter
    def infinite(self, infinite: bool):
        self.__infinite = infinite


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


class mindstorms_GoToEnemy(Action):

    pass
class mindstorms_GoTo(Action):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


class mindstorms_Release(Action):

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


class mindstorms_GoForward(Action):

    def __init__(self, cm: int, infinite: bool):
        self.cm = cm
        self.infinite = infinite
        
        pass
    @property
    def cm(self):
        return self.__cm

    @cm.setter
    def cm(self, cm: int):
        self.__cm = cm


    @property
    def infinite(self):
        return self.__infinite

    @infinite.setter
    def infinite(self, infinite: bool):
        self.__infinite = infinite


class Flow:

    pass
class mindstorms_While(Flow):

    pass
class mindstorms_If(Flow):

    pass
class mindstorms_Condition(ABC):

    pass