from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class robot_FlotCtrl_Expression(ABC):

    pass
class robot_robot_ProgramUnit:

    pass
class BoolExp:

    pass
class robot_FlotCtrl_NegExp(BoolExp):

    pass
class robot_FlotCtrl_AndExp(BoolExp):

    pass
class robot_Command:

    pass
class FlotCtrl_BoolExp:

    pass
class robot_robot_HasTurnedCmd(robot_Command, FlotCtrl_BoolExp):

    def __init__(self, angle: str):
        self.angle = angle
        
    @property
    def angle(self) -> str:
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle

class robot_robot_ObstacleCmd(robot_Command, FlotCtrl_BoolExp):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class Command:

    pass
class robot_robot_PrintCmd(Command):

    def __init__(self, msg: str, duration: str, line: str, col: str):
        self.msg = msg
        self.duration = duration
        self.line = line
        self.col = col
        
    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def msg(self) -> str:
        return self.__msg

    @msg.setter
    def msg(self, msg: str):
        self.__msg = msg

    @property
    def col(self) -> str:
        return self.__col

    @col.setter
    def col(self, col: str):
        self.__col = col

    @property
    def line(self) -> str:
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line

class robot_robot_Bip(Command):

    def __init__(self, duration: str, power: str, repet: str):
        self.duration = duration
        self.power = power
        self.repet = repet
        
    @property
    def power(self) -> str:
        return self.__power

    @power.setter
    def power(self, power: str):
        self.__power = power

    @property
    def repet(self) -> str:
        return self.__repet

    @repet.setter
    def repet(self, repet: str):
        self.__repet = repet

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

class robot_robot_TurnCmd(Command):

    def __init__(self, power: str, angle: str):
        self.power = power
        self.angle = angle
        
    @property
    def power(self) -> str:
        return self.__power

    @power.setter
    def power(self, power: str):
        self.__power = power

    @property
    def angle(self) -> str:
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle

class robot_robot_StopProgramCmd(Command):

    pass
class robot_robot_SetTurnAngleCmd(Command):

    def __init__(self, angle: str):
        self.angle = angle
        
    @property
    def angle(self) -> str:
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle

class robot_robot_StopEngineCmd(Command):

    pass
class robot_robot_MoveCmd(Command):

    def __init__(self, power: str):
        self.power = power
        
    @property
    def power(self) -> str:
        return self.__power

    @power.setter
    def power(self, power: str):
        self.__power = power

class Expression:

    pass
class robot_FlotCtrl_IfBlock(Expression):

    pass
class robot_FlotCtrl_BoolExp(Expression):

    pass
class robot_FlotCtrl_WhileLoop(Expression):

    pass
class robot_robot_Command(Expression):

    pass