from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class mindstorms_EdgeInstruction:

    pass
class Action:

    pass
class mindstorms_GoBackward(Action):

    def __init__(self, infinite: bool, cm: int):
        self.infinite = infinite
        self.cm = cm
        
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

class mindstorms_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mindstorms_End(Action):

    pass
class Instruction:

    pass
class mindstorms_Choreography(Instruction):

    pass
class mindstorms_Block(Instruction):

    pass
class Block:

    pass
class mindstorms_Action(Block):

    pass
class mindstorms_Release(Action):

    pass
class mindstorms_Rotate(Action):

    def __init__(self, degrees: int, random: bool):
        self.degrees = degrees
        self.random = random
        
    @property
    def degrees(self) -> int:
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: int):
        self.__degrees = degrees

    @property
    def random(self) -> bool:
        return self.__random

    @random.setter
    def random(self, random: bool):
        self.__random = random

class mindstorms_Begin(Action):

    pass
class NamedElement:

    pass
class mindstorms_Instruction(NamedElement):

    pass