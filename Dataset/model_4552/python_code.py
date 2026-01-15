from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Command:

    pass
class logo_Move(Command):

    def __init__(self, distance: float):
        self.distance = distance
        
    @property
    def distance(self) -> float:
        return self.__distance

    @distance.setter
    def distance(self, distance: float):
        self.__distance = distance

class logo_WhileNoObstacle(Command):

    def __init__(self, distance: float, logo_WhileNoObstacle: set["logo_Command"] = None):
        self.distance = distance
        self.logo_WhileNoObstacle = logo_WhileNoObstacle if logo_WhileNoObstacle is not None else set()
        
    @property
    def distance(self) -> float:
        return self.__distance

    @distance.setter
    def distance(self, distance: float):
        self.__distance = distance

    @property
    def logo_WhileNoObstacle(self):
        return self.__logo_WhileNoObstacle

    @logo_WhileNoObstacle.setter
    def logo_WhileNoObstacle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_logo_WhileNoObstacle__logo_WhileNoObstacle", None)
        self.__logo_WhileNoObstacle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "logo_Command2"):
                    opp_val = getattr(item, "logo_Command2", None)
                    
                    if opp_val == self:
                        setattr(item, "logo_Command2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "logo_Command2"):
                    opp_val = getattr(item, "logo_Command2", None)
                    
                    setattr(item, "logo_Command2", self)
                    

class logo_Turn(Command):

    def __init__(self, angle: float):
        self.angle = angle
        
    @property
    def angle(self) -> float:
        return self.__angle

    @angle.setter
    def angle(self, angle: float):
        self.__angle = angle

class logo_Command(ABC):

    pass
class logo_ProgramUnit:

    pass