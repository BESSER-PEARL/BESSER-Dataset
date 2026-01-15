from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    blue = "blue"
    red = "red"
    yellow = "yellow"


############################################
# Definition of Classes
############################################

class roverDSL_DetectBottle:

    def __init__(self, maxDistance: int, roverDSL_DetectBottle: "roverDSL_Mission" = None):
        self.maxDistance = maxDistance
        self.roverDSL_DetectBottle = roverDSL_DetectBottle
        
    @property
    def maxDistance(self) -> int:
        return self.__maxDistance

    @maxDistance.setter
    def maxDistance(self, maxDistance: int):
        self.__maxDistance = maxDistance

    @property
    def roverDSL_DetectBottle(self):
        return self.__roverDSL_DetectBottle

    @roverDSL_DetectBottle.setter
    def roverDSL_DetectBottle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_DetectBottle__roverDSL_DetectBottle", None)
        self.__roverDSL_DetectBottle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Mission4"):
                opp_val = getattr(old_value, "roverDSL_Mission4", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_Mission4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Mission4"):
                opp_val = getattr(value, "roverDSL_Mission4", None)
                setattr(value, "roverDSL_Mission4", self)

class roverDSL_Colors:

    def __init__(self, color: str, roverDSL_Colors: "roverDSL_Mission" = None, roverDSL_Colors7: "roverDSL_Mission" = None):
        self.color = color
        self.roverDSL_Colors = roverDSL_Colors
        self.roverDSL_Colors7 = roverDSL_Colors7
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def roverDSL_Colors(self):
        return self.__roverDSL_Colors

    @roverDSL_Colors.setter
    def roverDSL_Colors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Colors__roverDSL_Colors", None)
        self.__roverDSL_Colors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Mission2"):
                opp_val = getattr(old_value, "roverDSL_Mission2", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_Mission2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Mission2"):
                opp_val = getattr(value, "roverDSL_Mission2", None)
                setattr(value, "roverDSL_Mission2", self)

    @property
    def roverDSL_Colors7(self):
        return self.__roverDSL_Colors7

    @roverDSL_Colors7.setter
    def roverDSL_Colors7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Colors__roverDSL_Colors7", None)
        self.__roverDSL_Colors7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Mission6"):
                opp_val = getattr(old_value, "roverDSL_Mission6", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_Mission6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Mission6"):
                opp_val = getattr(value, "roverDSL_Mission6", None)
                setattr(value, "roverDSL_Mission6", self)

class roverDSL_Mission:

    def __init__(self, id: str, roverDSL_Mission: "roverDSL_Robot" = None, roverDSL_Mission2: "roverDSL_Colors" = None, roverDSL_Mission4: "roverDSL_DetectBottle" = None, roverDSL_Mission6: "roverDSL_Colors" = None):
        self.id = id
        self.roverDSL_Mission = roverDSL_Mission
        self.roverDSL_Mission2 = roverDSL_Mission2
        self.roverDSL_Mission4 = roverDSL_Mission4
        self.roverDSL_Mission6 = roverDSL_Mission6
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def roverDSL_Mission6(self):
        return self.__roverDSL_Mission6

    @roverDSL_Mission6.setter
    def roverDSL_Mission6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Mission__roverDSL_Mission6", None)
        self.__roverDSL_Mission6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Colors7"):
                opp_val = getattr(old_value, "roverDSL_Colors7", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_Colors7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Colors7"):
                opp_val = getattr(value, "roverDSL_Colors7", None)
                setattr(value, "roverDSL_Colors7", self)

    @property
    def roverDSL_Mission2(self):
        return self.__roverDSL_Mission2

    @roverDSL_Mission2.setter
    def roverDSL_Mission2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Mission__roverDSL_Mission2", None)
        self.__roverDSL_Mission2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Colors"):
                opp_val = getattr(old_value, "roverDSL_Colors", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_Colors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Colors"):
                opp_val = getattr(value, "roverDSL_Colors", None)
                setattr(value, "roverDSL_Colors", self)

    @property
    def roverDSL_Mission4(self):
        return self.__roverDSL_Mission4

    @roverDSL_Mission4.setter
    def roverDSL_Mission4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Mission__roverDSL_Mission4", None)
        self.__roverDSL_Mission4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_DetectBottle"):
                opp_val = getattr(old_value, "roverDSL_DetectBottle", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_DetectBottle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_DetectBottle"):
                opp_val = getattr(value, "roverDSL_DetectBottle", None)
                setattr(value, "roverDSL_DetectBottle", self)

    @property
    def roverDSL_Mission(self):
        return self.__roverDSL_Mission

    @roverDSL_Mission.setter
    def roverDSL_Mission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Mission__roverDSL_Mission", None)
        self.__roverDSL_Mission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Robot"):
                opp_val = getattr(old_value, "roverDSL_Robot", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_Robot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Robot"):
                opp_val = getattr(value, "roverDSL_Robot", None)
                setattr(value, "roverDSL_Robot", self)

class roverDSL_Robot:

    def __init__(self, defaultSpeed: int, slowSpeed: int, minAngle: int, maxAngle: int, roverDSL_Robot: "roverDSL_Mission" = None):
        self.defaultSpeed = defaultSpeed
        self.slowSpeed = slowSpeed
        self.minAngle = minAngle
        self.maxAngle = maxAngle
        self.roverDSL_Robot = roverDSL_Robot
        
    @property
    def defaultSpeed(self) -> int:
        return self.__defaultSpeed

    @defaultSpeed.setter
    def defaultSpeed(self, defaultSpeed: int):
        self.__defaultSpeed = defaultSpeed

    @property
    def minAngle(self) -> int:
        return self.__minAngle

    @minAngle.setter
    def minAngle(self, minAngle: int):
        self.__minAngle = minAngle

    @property
    def maxAngle(self) -> int:
        return self.__maxAngle

    @maxAngle.setter
    def maxAngle(self, maxAngle: int):
        self.__maxAngle = maxAngle

    @property
    def slowSpeed(self) -> int:
        return self.__slowSpeed

    @slowSpeed.setter
    def slowSpeed(self, slowSpeed: int):
        self.__slowSpeed = slowSpeed

    @property
    def roverDSL_Robot(self):
        return self.__roverDSL_Robot

    @roverDSL_Robot.setter
    def roverDSL_Robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverDSL_Robot__roverDSL_Robot", None)
        self.__roverDSL_Robot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverDSL_Mission"):
                opp_val = getattr(old_value, "roverDSL_Mission", None)
                if opp_val == self:
                    setattr(old_value, "roverDSL_Mission", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverDSL_Mission"):
                opp_val = getattr(value, "roverDSL_Mission", None)
                setattr(value, "roverDSL_Mission", self)
