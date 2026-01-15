from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class polybot_Instruction(ABC):

    pass
class polybot_Point:

    def __init__(self, x: int, y: int, polybot_Point: "polybot_Bot" = None):
        self.x = x
        self.y = y
        self.polybot_Point = polybot_Point
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def polybot_Point(self):
        return self.__polybot_Point

    @polybot_Point.setter
    def polybot_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_polybot_Point__polybot_Point", None)
        self.__polybot_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "polybot_Bot"):
                opp_val = getattr(old_value, "polybot_Bot", None)
                if opp_val == self:
                    setattr(old_value, "polybot_Bot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "polybot_Bot"):
                opp_val = getattr(value, "polybot_Bot", None)
                setattr(value, "polybot_Bot", self)

class polybot_Bot:

    pass
class Instruction:

    pass
class polybot_IfObstacleDetected(Instruction):

    pass
class polybot_IfObjectDetected(Instruction):

    pass
class polybot_TakeDropObject(Instruction):

    pass
class polybot_While(Instruction):

    def __init__(self, nb: int, polybot_While: set["polybot_Instruction"] = None):
        self.nb = nb
        self.polybot_While = polybot_While if polybot_While is not None else set()
        
    @property
    def nb(self) -> int:
        return self.__nb

    @nb.setter
    def nb(self, nb: int):
        self.__nb = nb

    @property
    def polybot_While(self):
        return self.__polybot_While

    @polybot_While.setter
    def polybot_While(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_polybot_While__polybot_While", None)
        self.__polybot_While = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "polybot_Instruction8"):
                    opp_val = getattr(item, "polybot_Instruction8", None)
                    
                    if opp_val == self:
                        setattr(item, "polybot_Instruction8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "polybot_Instruction8"):
                    opp_val = getattr(item, "polybot_Instruction8", None)
                    
                    setattr(item, "polybot_Instruction8", self)
                    

class polybot_Move(Instruction):

    def __init__(self, speed: int, duration: int):
        self.speed = speed
        self.duration = duration
        
    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

class Move:

    pass
class polybot_Right(Move):

    pass
class polybot_Reverse(Move):

    pass
class polybot_Forward(Move):

    pass
class polybot_Left(Move):

    pass
class polybot_GoTo(Move):

    pass