from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class robot_ExpBool(ABC):

    pass
class ExpBool:

    pass
class robot_If(ExpBool):

    pass
class robot_Not(ExpBool):

    pass
class robot_While(ExpBool):

    pass
class robot_Obstacle(ExpBool):

    pass
class Instruction:

    pass
class robot_SetTurnAngle(Instruction):

    pass
class robot_Turn(Instruction):

    pass
class robot_StopEngine(Instruction):

    pass
class robot_StopProgram(Instruction):

    pass
class robot_Move(Instruction):

    pass
class robot_Bip(Instruction):

    pass
class robot_Instruction(ABC):

    pass
class robot_Program:

    pass
class robot_And(ExpBool):

    pass
class robot_HasTurned(ExpBool):

    pass