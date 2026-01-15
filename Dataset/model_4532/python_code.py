from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class robotG_flow_Expr(ABC):

    pass
class robotG_flow_Programme:

    pass
class OpBinaire:

    pass
class robotG_flow_Or(OpBinaire):

    pass
class robotG_flow_And(OpBinaire):

    pass
class CommandeRobot:

    pass
class robotG_robot_Bip(CommandeRobot):

    def __init__(self, duration: int, power: int, repeat: bool):
        self.duration = duration
        self.power = power
        self.repeat = repeat
        
    @property
    def power(self) -> int:
        return self.__power

    @power.setter
    def power(self, power: int):
        self.__power = power

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def repeat(self) -> bool:
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat: bool):
        self.__repeat = repeat

class robotG_robot_Move(CommandeRobot):

    def __init__(self, power: int):
        self.power = power
        
    @property
    def power(self) -> int:
        return self.__power

    @power.setter
    def power(self, power: int):
        self.__power = power

class OpUnaire:

    pass
class robotG_flow_Not(OpUnaire):

    pass
class ExprBool:

    pass
class robotG_flow_OpBinaire(ExprBool):

    pass
class robotG_flow_OpUnaire(ExprBool):

    pass
class Expr:

    pass
class robotG_flow_While(Expr):

    pass
class robotG_flow_ExprBool(Expr):

    pass
class robotG_flow_If(Expr):

    pass
class robotG_flow_StopProgram(Expr):

    pass
class robotG_robot_CommandeRobot(Expr):

    pass
class robotG_robot_StopEngine(CommandeRobot):

    pass
class robotG_robot_Display(CommandeRobot):

    def __init__(self, msg: str, duration: int, line: int, col: int):
        self.msg = msg
        self.duration = duration
        self.line = line
        self.col = col
        
    @property
    def col(self) -> int:
        return self.__col

    @col.setter
    def col(self, col: int):
        self.__col = col

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def line(self) -> int:
        return self.__line

    @line.setter
    def line(self, line: int):
        self.__line = line

    @property
    def msg(self) -> str:
        return self.__msg

    @msg.setter
    def msg(self, msg: str):
        self.__msg = msg

class robot_CommandeRobot:

    pass
class flow_ExprBool:

    pass
class robotG_robot_Obstacle(flow_ExprBool, robot_CommandeRobot):

    def __init__(self, distance: int):
        self.distance = distance
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

class robotG_robot_HasTurned(flow_ExprBool, robot_CommandeRobot):

    def __init__(self, angle: int):
        self.angle = angle
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

class robotG_robot_SetTurnAngle(CommandeRobot):

    def __init__(self, angle: int):
        self.angle = angle
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

class robotG_robot_Turn(CommandeRobot):

    def __init__(self, power: int, angle: int):
        self.power = power
        self.angle = angle
        
    @property
    def power(self) -> int:
        return self.__power

    @power.setter
    def power(self, power: int):
        self.__power = power

    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle
