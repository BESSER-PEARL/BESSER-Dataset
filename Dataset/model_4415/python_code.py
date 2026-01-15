from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OperatorKind(Enum):
    equal = "equal"
    notEqual = "notEqual"
    upperOrEqual = "upperOrEqual"
    lowerOrEqual = "lowerOrEqual"
class Color(Enum):
    GRAY = "GRAY"
    LIGHT_GRAY = "LIGHT_GRAY"
    DARK_GRAY = "DARK_GRAY"
    CYAN = "CYAN"
    BROWN = "BROWN"
    NONE = "NONE"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    YELLOW = "YELLOW"
    MAGENTA = "MAGENTA"
    ORANGE = "ORANGE"
    WHITE = "WHITE"
    BLACK = "BLACK"
    PINK = "PINK"


############################################
# Definition of Classes
############################################

class Sensor:

    pass
class mindstorms_UltrasonicSensor(Sensor):

    def __init__(self, operator: str, value: float):
        self.operator = operator
        self.value = value
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class mindstorms_ColorSensor(Sensor):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class mindstorms_TouchSensor(Sensor):

    def __init__(self, isPressed: bool):
        self.isPressed = isPressed
        
    @property
    def isPressed(self) -> bool:
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
class Block:

    pass
class mindstorms_Action(Block):

    pass
class ConditionContainer:

    pass
class BlockContainer:

    pass
class mindstorms_Flow(BlockContainer, ConditionContainer, Block):

    pass
class Instruction:

    pass
class mindstorms_ReuseInstruction(Instruction):

    pass
class mindstorms_Arbitrator(Instruction, ConditionContainer):

    pass
class mindstorms_Procedure(BlockContainer, Instruction):

    pass
class mindstorms_Block(Instruction):

    pass
class mindstorms_BlockContainer(ABC):

    pass
class NamedElement:

    pass
class mindstorms_Behavior(BlockContainer, ConditionContainer, NamedElement):

    pass
class mindstorms_Instruction(NamedElement):

    pass
class mindstorms_Main:

    pass
class Action:

    pass
class mindstorms_ReturnToBase(Action):

    pass
class mindstorms_Rotate(Action):

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

class mindstorms_Delay(Action):

    def __init__(self, ms: int):
        self.ms = ms
        
    @property
    def ms(self) -> int:
        return self.__ms

    @ms.setter
    def ms(self, ms: int):
        self.__ms = ms

class mindstorms_GoBackward(Action):

    def __init__(self, cm: int, infinite: bool):
        self.cm = cm
        self.infinite = infinite
        
    @property
    def infinite(self) -> bool:
        return self.__infinite

    @infinite.setter
    def infinite(self, infinite: bool):
        self.__infinite = infinite

    @property
    def cm(self) -> int:
        return self.__cm

    @cm.setter
    def cm(self, cm: int):
        self.__cm = cm

class mindstorms_Grab(Action):

    pass
class mindstorms_GoTo(Action):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

class mindstorms_Release(Action):

    pass
class mindstorms_GoToEnemy(Action):

    pass
class mindstorms_GoForward(Action):

    def __init__(self, cm: int, infinite: bool):
        self.cm = cm
        self.infinite = infinite
        
    @property
    def infinite(self) -> bool:
        return self.__infinite

    @infinite.setter
    def infinite(self, infinite: bool):
        self.__infinite = infinite

    @property
    def cm(self) -> int:
        return self.__cm

    @cm.setter
    def cm(self, cm: int):
        self.__cm = cm

class Flow:

    pass
class mindstorms_While(Flow):

    pass
class mindstorms_If(Flow):

    pass
class mindstorms_Condition(ABC):

    pass
class Condition:

    pass
class mindstorms_Sensor(Condition, NamedElement):

    pass
class mindstorms_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
