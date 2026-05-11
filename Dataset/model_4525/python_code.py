from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TURN_DIRECTION(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class MOVE_DIRECTION(Enum):
    FORWARDS = "FORWARDS"
    BACKWARDS = "BACKWARDS"


############################################
# Definition of Classes
############################################

class Event:

    pass
class model_Tapped(Event):

    pass
class model_Obstacle(Event):

    pass
class RandomAction:

    pass
class ContinuosAction:

    pass
class RotorAction:

    pass
class model_Turn(ContinuosAction, RotorAction, RandomAction):

    def __init__(self, degrees: float, direction: str):
        self.degrees = degrees
        self.direction = direction
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def degrees(self):
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: float):
        self.__degrees = degrees


class model_Move(ContinuosAction, RotorAction, RandomAction):

    def __init__(self, direction: str):
        self.direction = direction
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


class Action:

    pass
class model_RandomAction(Action):

    def __init__(self, isRandom: bool):
        self.isRandom = isRandom
        
        pass
    @property
    def isRandom(self):
        return self.__isRandom

    @isRandom.setter
    def isRandom(self, isRandom: bool):
        self.__isRandom = isRandom


class model_ContinuosAction(Action):

    def __init__(self, duration: float):
        self.duration = duration
        
        pass
    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration


class model_RotorAction(Action):

    pass
class model_Ending(ABC):

    pass
class model_Action(ABC):

    pass
class model_ActionsList(ABC):

    pass
class model_Event(ABC):

    pass
class ActionsList:

    pass
class model_EventListener(ActionsList):

    pass
class model_Main(ActionsList):

    pass
class model_RoboProse:

    pass
class model_Root:

    pass
class Ending:

    pass
class model_StartOver(Ending):

    pass
class model_Wait(Ending):

    pass
class model_Repeat(Ending):

    pass
class model_Stop(ContinuosAction):

    pass