from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class mindstorms_EdgeInstruction:

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
class Action:

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


class mindstorms_End(Action):

    pass
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


class NamedElement:

    pass
class mindstorms_Instruction(NamedElement):

    pass
class mindstorms_Release(Action):

    pass
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


class mindstorms_Begin(Action):

    pass