from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Intensity(Enum):
    C = "C"
    A = "A"
    B = "B"
    D = "D"
    E = "E"
class DurationUnit(Enum):
    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"
    MINUTES = "MINUTES"


############################################
# Definition of Classes
############################################

class roc_LeftRightDirection:

    def __init__(self, right: str, left: str):
        self.right = right
        self.left = left
        
    @property
    def left(self) -> str:
        return self.__left

    @left.setter
    def left(self, left: str):
        self.__left = left

    @property
    def right(self) -> str:
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right

class roc_LeftRightDirectedAction:

    def __init__(self, tiltHead: str):
        self.tiltHead = tiltHead
        
    @property
    def tiltHead(self) -> str:
        return self.__tiltHead

    @tiltHead.setter
    def tiltHead(self, tiltHead: str):
        self.__tiltHead = tiltHead

class roc_DirectedAction:

    pass
class roc_SingleAction:

    def __init__(self, actionName: str):
        self.actionName = actionName
        
    @property
    def actionName(self) -> str:
        return self.__actionName

    @actionName.setter
    def actionName(self, actionName: str):
        self.__actionName = actionName

class roc_CompleteAction:

    def __init__(self, actionName: str):
        self.actionName = actionName
        
    @property
    def actionName(self) -> str:
        return self.__actionName

    @actionName.setter
    def actionName(self, actionName: str):
        self.__actionName = actionName

class roc_EObject:

    pass
class roc_Direction:

    def __init__(self, UP: str, DOWN: str, LEFT: str, RIGHT: str):
        self.UP = UP
        self.DOWN = DOWN
        self.LEFT = LEFT
        self.RIGHT = RIGHT
        
    @property
    def LEFT(self) -> str:
        return self.__LEFT

    @LEFT.setter
    def LEFT(self, LEFT: str):
        self.__LEFT = LEFT

    @property
    def RIGHT(self) -> str:
        return self.__RIGHT

    @RIGHT.setter
    def RIGHT(self, RIGHT: str):
        self.__RIGHT = RIGHT

    @property
    def UP(self) -> str:
        return self.__UP

    @UP.setter
    def UP(self, UP: str):
        self.__UP = UP

    @property
    def DOWN(self) -> str:
        return self.__DOWN

    @DOWN.setter
    def DOWN(self, DOWN: str):
        self.__DOWN = DOWN

class roc_FullDirectedAction:

    def __init__(self, turnHead: str, turnEyes: str):
        self.turnHead = turnHead
        self.turnEyes = turnEyes
        
    @property
    def turnHead(self) -> str:
        return self.__turnHead

    @turnHead.setter
    def turnHead(self, turnHead: str):
        self.__turnHead = turnHead

    @property
    def turnEyes(self) -> str:
        return self.__turnEyes

    @turnEyes.setter
    def turnEyes(self, turnEyes: str):
        self.__turnEyes = turnEyes

class roc_Program:

    pass
class roc_Speed:

    def __init__(self, SLOWEST: str, SLOW: str, NORMAL: str, FAST: str, FULL: str, roc_Speed: "roc_Motion" = None):
        self.SLOWEST = SLOWEST
        self.SLOW = SLOW
        self.NORMAL = NORMAL
        self.FAST = FAST
        self.FULL = FULL
        self.roc_Speed = roc_Speed
        
    @property
    def FULL(self) -> str:
        return self.__FULL

    @FULL.setter
    def FULL(self, FULL: str):
        self.__FULL = FULL

    @property
    def SLOW(self) -> str:
        return self.__SLOW

    @SLOW.setter
    def SLOW(self, SLOW: str):
        self.__SLOW = SLOW

    @property
    def NORMAL(self) -> str:
        return self.__NORMAL

    @NORMAL.setter
    def NORMAL(self, NORMAL: str):
        self.__NORMAL = NORMAL

    @property
    def SLOWEST(self) -> str:
        return self.__SLOWEST

    @SLOWEST.setter
    def SLOWEST(self, SLOWEST: str):
        self.__SLOWEST = SLOWEST

    @property
    def FAST(self) -> str:
        return self.__FAST

    @FAST.setter
    def FAST(self, FAST: str):
        self.__FAST = FAST

    @property
    def roc_Speed(self):
        return self.__roc_Speed

    @roc_Speed.setter
    def roc_Speed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roc_Speed__roc_Speed", None)
        self.__roc_Speed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roc_Motion6"):
                opp_val = getattr(old_value, "roc_Motion6", None)
                if opp_val == self:
                    setattr(old_value, "roc_Motion6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roc_Motion6"):
                opp_val = getattr(value, "roc_Motion6", None)
                setattr(value, "roc_Motion6", self)

class roc_Action:

    def __init__(self, intensity: str, roc_Action: "roc_Motion" = None, roc_Action8: "roc_EObject" = None):
        self.intensity = intensity
        self.roc_Action = roc_Action
        self.roc_Action8 = roc_Action8
        
    @property
    def intensity(self) -> str:
        return self.__intensity

    @intensity.setter
    def intensity(self, intensity: str):
        self.__intensity = intensity

    @property
    def roc_Action(self):
        return self.__roc_Action

    @roc_Action.setter
    def roc_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roc_Action__roc_Action", None)
        self.__roc_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roc_Motion4"):
                opp_val = getattr(old_value, "roc_Motion4", None)
                if opp_val == self:
                    setattr(old_value, "roc_Motion4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roc_Motion4"):
                opp_val = getattr(value, "roc_Motion4", None)
                setattr(value, "roc_Motion4", self)

    @property
    def roc_Action8(self):
        return self.__roc_Action8

    @roc_Action8.setter
    def roc_Action8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roc_Action__roc_Action8", None)
        self.__roc_Action8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roc_EObject"):
                opp_val = getattr(old_value, "roc_EObject", None)
                if opp_val == self:
                    setattr(old_value, "roc_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roc_EObject"):
                opp_val = getattr(value, "roc_EObject", None)
                setattr(value, "roc_EObject", self)

class roc_Motion:

    def __init__(self, duration: str, durationUnit: str, roc_Motion: "roc_Movement" = None, roc_Motion4: "roc_Action" = None, roc_Motion6: "roc_Speed" = None):
        self.duration = duration
        self.durationUnit = durationUnit
        self.roc_Motion = roc_Motion
        self.roc_Motion4 = roc_Motion4
        self.roc_Motion6 = roc_Motion6
        
    @property
    def durationUnit(self) -> str:
        return self.__durationUnit

    @durationUnit.setter
    def durationUnit(self, durationUnit: str):
        self.__durationUnit = durationUnit

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def roc_Motion(self):
        return self.__roc_Motion

    @roc_Motion.setter
    def roc_Motion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roc_Motion__roc_Motion", None)
        self.__roc_Motion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roc_Movement2"):
                opp_val = getattr(old_value, "roc_Movement2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roc_Movement2"):
                opp_val = getattr(value, "roc_Movement2", None)
                if opp_val is None:
                    setattr(value, "roc_Movement2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def roc_Motion4(self):
        return self.__roc_Motion4

    @roc_Motion4.setter
    def roc_Motion4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roc_Motion__roc_Motion4", None)
        self.__roc_Motion4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roc_Action"):
                opp_val = getattr(old_value, "roc_Action", None)
                if opp_val == self:
                    setattr(old_value, "roc_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roc_Action"):
                opp_val = getattr(value, "roc_Action", None)
                setattr(value, "roc_Action", self)

    @property
    def roc_Motion6(self):
        return self.__roc_Motion6

    @roc_Motion6.setter
    def roc_Motion6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roc_Motion__roc_Motion6", None)
        self.__roc_Motion6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roc_Speed"):
                opp_val = getattr(old_value, "roc_Speed", None)
                if opp_val == self:
                    setattr(old_value, "roc_Speed", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roc_Speed"):
                opp_val = getattr(value, "roc_Speed", None)
                setattr(value, "roc_Speed", self)

class roc_Movement:

    pass