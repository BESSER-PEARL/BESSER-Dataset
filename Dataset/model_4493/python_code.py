from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"


############################################
# Definition of Classes
############################################

class dSL_Action:

    def __init__(self, showLakes: bool, driveDirection: bool, direction: str, driveDistance: bool, steer: bool, probeLake: bool, blinkLights: bool, dSL_Action15: "dSL_Distance" = None, dSL_Action18: "dSL_Angle" = None, dSL_Action: "dSL_ActionList" = None):
        self.showLakes = showLakes
        self.driveDirection = driveDirection
        self.direction = direction
        self.driveDistance = driveDistance
        self.steer = steer
        self.probeLake = probeLake
        self.blinkLights = blinkLights
        self.dSL_Action15 = dSL_Action15
        self.dSL_Action18 = dSL_Action18
        self.dSL_Action = dSL_Action
        
    @property
    def driveDirection(self) -> bool:
        return self.__driveDirection

    @driveDirection.setter
    def driveDirection(self, driveDirection: bool):
        self.__driveDirection = driveDirection

    @property
    def driveDistance(self) -> bool:
        return self.__driveDistance

    @driveDistance.setter
    def driveDistance(self, driveDistance: bool):
        self.__driveDistance = driveDistance

    @property
    def steer(self) -> bool:
        return self.__steer

    @steer.setter
    def steer(self, steer: bool):
        self.__steer = steer

    @property
    def blinkLights(self) -> bool:
        return self.__blinkLights

    @blinkLights.setter
    def blinkLights(self, blinkLights: bool):
        self.__blinkLights = blinkLights

    @property
    def probeLake(self) -> bool:
        return self.__probeLake

    @probeLake.setter
    def probeLake(self, probeLake: bool):
        self.__probeLake = probeLake

    @property
    def showLakes(self) -> bool:
        return self.__showLakes

    @showLakes.setter
    def showLakes(self, showLakes: bool):
        self.__showLakes = showLakes

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def dSL_Action15(self):
        return self.__dSL_Action15

    @dSL_Action15.setter
    def dSL_Action15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Action__dSL_Action15", None)
        self.__dSL_Action15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_Distance16"):
                opp_val = getattr(old_value, "dSL_Distance16", None)
                if opp_val == self:
                    setattr(old_value, "dSL_Distance16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_Distance16"):
                opp_val = getattr(value, "dSL_Distance16", None)
                setattr(value, "dSL_Distance16", self)

    @property
    def dSL_Action(self):
        return self.__dSL_Action

    @dSL_Action.setter
    def dSL_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Action__dSL_Action", None)
        self.__dSL_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_ActionList13"):
                opp_val = getattr(old_value, "dSL_ActionList13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_ActionList13"):
                opp_val = getattr(value, "dSL_ActionList13", None)
                if opp_val is None:
                    setattr(value, "dSL_ActionList13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dSL_Action18(self):
        return self.__dSL_Action18

    @dSL_Action18.setter
    def dSL_Action18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Action__dSL_Action18", None)
        self.__dSL_Action18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_Angle"):
                opp_val = getattr(old_value, "dSL_Angle", None)
                if opp_val == self:
                    setattr(old_value, "dSL_Angle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_Angle"):
                opp_val = getattr(value, "dSL_Angle", None)
                setattr(value, "dSL_Angle", self)

class dSL_Distance:

    def __init__(self, value: int, dSL_Distance16: "dSL_Action" = None, dSL_Distance: "dSL_Condition" = None):
        self.value = value
        self.dSL_Distance16 = dSL_Distance16
        self.dSL_Distance = dSL_Distance
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def dSL_Distance(self):
        return self.__dSL_Distance

    @dSL_Distance.setter
    def dSL_Distance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Distance__dSL_Distance", None)
        self.__dSL_Distance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_Condition11"):
                opp_val = getattr(old_value, "dSL_Condition11", None)
                if opp_val == self:
                    setattr(old_value, "dSL_Condition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_Condition11"):
                opp_val = getattr(value, "dSL_Condition11", None)
                setattr(value, "dSL_Condition11", self)

    @property
    def dSL_Distance16(self):
        return self.__dSL_Distance16

    @dSL_Distance16.setter
    def dSL_Distance16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Distance__dSL_Distance16", None)
        self.__dSL_Distance16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_Action15"):
                opp_val = getattr(old_value, "dSL_Action15", None)
                if opp_val == self:
                    setattr(old_value, "dSL_Action15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_Action15"):
                opp_val = getattr(value, "dSL_Action15", None)
                setattr(value, "dSL_Action15", self)

class dSL_Condition:

    def __init__(self, not: bool, allLakes: bool, collision: bool, atLake: bool, isProbed: bool, dSL_Condition: "dSL_ConditionList" = None, dSL_Condition9: "dSL_Condition" = None, dSL_Condition7: "dSL_Condition" = None, dSL_Condition11: "dSL_Distance" = None):
        self.not = not
        self.allLakes = allLakes
        self.collision = collision
        self.atLake = atLake
        self.isProbed = isProbed
        self.dSL_Condition = dSL_Condition
        self.dSL_Condition9 = dSL_Condition9
        self.dSL_Condition7 = dSL_Condition7
        self.dSL_Condition11 = dSL_Condition11
        
    @property
    def atLake(self) -> bool:
        return self.__atLake

    @atLake.setter
    def atLake(self, atLake: bool):
        self.__atLake = atLake

    @property
    def isProbed(self) -> bool:
        return self.__isProbed

    @isProbed.setter
    def isProbed(self, isProbed: bool):
        self.__isProbed = isProbed

    @property
    def collision(self) -> bool:
        return self.__collision

    @collision.setter
    def collision(self, collision: bool):
        self.__collision = collision

    @property
    def allLakes(self) -> bool:
        return self.__allLakes

    @allLakes.setter
    def allLakes(self, allLakes: bool):
        self.__allLakes = allLakes

    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

    @property
    def dSL_Condition11(self):
        return self.__dSL_Condition11

    @dSL_Condition11.setter
    def dSL_Condition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Condition__dSL_Condition11", None)
        self.__dSL_Condition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_Distance"):
                opp_val = getattr(old_value, "dSL_Distance", None)
                if opp_val == self:
                    setattr(old_value, "dSL_Distance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_Distance"):
                opp_val = getattr(value, "dSL_Distance", None)
                setattr(value, "dSL_Distance", self)

    @property
    def dSL_Condition7(self):
        return self.__dSL_Condition7

    @dSL_Condition7.setter
    def dSL_Condition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Condition__dSL_Condition7", None)
        self.__dSL_Condition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_Condition9"):
                opp_val = getattr(old_value, "dSL_Condition9", None)
                if opp_val == self:
                    setattr(old_value, "dSL_Condition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_Condition9"):
                opp_val = getattr(value, "dSL_Condition9", None)
                setattr(value, "dSL_Condition9", self)

    @property
    def dSL_Condition(self):
        return self.__dSL_Condition

    @dSL_Condition.setter
    def dSL_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Condition__dSL_Condition", None)
        self.__dSL_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_ConditionList6"):
                opp_val = getattr(old_value, "dSL_ConditionList6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_ConditionList6"):
                opp_val = getattr(value, "dSL_ConditionList6", None)
                if opp_val is None:
                    setattr(value, "dSL_ConditionList6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dSL_Condition9(self):
        return self.__dSL_Condition9

    @dSL_Condition9.setter
    def dSL_Condition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Condition__dSL_Condition9", None)
        self.__dSL_Condition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_Condition7"):
                opp_val = getattr(old_value, "dSL_Condition7", None)
                if opp_val == self:
                    setattr(old_value, "dSL_Condition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_Condition7"):
                opp_val = getattr(value, "dSL_Condition7", None)
                setattr(value, "dSL_Condition7", self)

class dSL_Angle:

    def __init__(self, value: int, away: bool, dSL_Angle: "dSL_Action" = None):
        self.value = value
        self.away = away
        self.dSL_Angle = dSL_Angle
        
    @property
    def away(self) -> bool:
        return self.__away

    @away.setter
    def away(self, away: bool):
        self.__away = away

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def dSL_Angle(self):
        return self.__dSL_Angle

    @dSL_Angle.setter
    def dSL_Angle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dSL_Angle__dSL_Angle", None)
        self.__dSL_Angle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dSL_Action18"):
                opp_val = getattr(old_value, "dSL_Action18", None)
                if opp_val == self:
                    setattr(old_value, "dSL_Action18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dSL_Action18"):
                opp_val = getattr(value, "dSL_Action18", None)
                setattr(value, "dSL_Action18", self)

class dSL_ActionList:

    pass
class dSL_ConditionList:

    pass
class dSL_Rule:

    pass
class dSL_Specification:

    pass