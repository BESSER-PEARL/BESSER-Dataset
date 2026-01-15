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
class Ending:

    pass
class model_StartOver(Ending):

    pass
class model_Wait(Ending):

    pass
class model_Repeat(Ending):

    pass
class RandomAction:

    pass
class ContinuosAction:

    pass
class model_Stop(ContinuosAction):

    pass
class RotorAction:

    pass
class model_Turn(ContinuosAction, RandomAction, RotorAction):

    def __init__(self, degrees: float, direction: str):
        self.degrees = degrees
        self.direction = direction
        
    @property
    def degrees(self) -> float:
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: float):
        self.__degrees = degrees

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class model_Move(ContinuosAction, RandomAction, RotorAction):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class Action:

    pass
class model_RandomAction(Action):

    def __init__(self, isRandom: bool):
        self.isRandom = isRandom
        
    @property
    def isRandom(self) -> bool:
        return self.__isRandom

    @isRandom.setter
    def isRandom(self, isRandom: bool):
        self.__isRandom = isRandom

class model_ContinuosAction(Action):

    def __init__(self, duration: float):
        self.duration = duration
        
    @property
    def duration(self) -> float:
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