from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Directions(Enum):
    N = "N"
    NE = "NE"
    E = "E"
    SE = "SE"
    S = "S"
    SW = "SW"
    W = "W"
    NW = "NW"
class CompareOperator(Enum):
    EQ = "EQ"
    NEQ = "NEQ"
    GEQ = "GEQ"
    G = "G"
    LEQ = "LEQ"
    L = "L"
class TouchSensorSides(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    BOTH = "BOTH"
class Colors(Enum):
    BLACK = "BLACK"
    BLUE = "BLUE"
    CYAN = "CYAN"
    DARK_GRAY = "DARK_GRAY"
    GRAY = "GRAY"
    GREEN = "GREEN"
    LIGHT_GRAY = "LIGHT_GRAY"
    MAGENTA = "MAGENTA"
    ORANGE = "ORANGE"
    PINK = "PINK"
    RED = "RED"
    WHITE = "WHITE"
    YELLOW = "YELLOW"
class Actions(Enum):
    DRIVE_BACKWARD = "DRIVE_BACKWARD"
    ROTATE_L = "ROTATE_L"
    ROTATE_R = "ROTATE_R"
    DRIVE_FORWARD = "DRIVE_FORWARD"
    STOP_DRIVING = "STOP_DRIVING"
    TURN_AROUND = "TURN_AROUND"
    BEEP = "BEEP"
    MEASURE = "MEASURE"
    DRIVETOEDGE = "DRIVETOEDGE"


############################################
# Definition of Classes
############################################

class SensorType:

    pass
class dsl_TouchSensor(SensorType):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class dsl_UltrasonicSensor(SensorType):

    def __init__(self, comparator: str, distance: str):
        self.comparator = comparator
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

    @property
    def comparator(self) -> str:
        return self.__comparator

    @comparator.setter
    def comparator(self, comparator: str):
        self.__comparator = comparator

class dsl_ColorSensor(SensorType):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class dsl_Ignorables:

    def __init__(self, AVOID_OBJECTS: str):
        self.AVOID_OBJECTS = AVOID_OBJECTS
        
    @property
    def AVOID_OBJECTS(self) -> str:
        return self.__AVOID_OBJECTS

    @AVOID_OBJECTS.setter
    def AVOID_OBJECTS(self, AVOID_OBJECTS: str):
        self.__AVOID_OBJECTS = AVOID_OBJECTS

class dsl_SensorType:

    pass
class dsl_Task:

    def __init__(self, name: str, action: str, ignoreBehavior: bool, dsl_Task: "dsl_Mission" = None, dsl_Task2: "dsl_SensorType" = None):
        self.name = name
        self.action = action
        self.ignoreBehavior = ignoreBehavior
        self.dsl_Task = dsl_Task
        self.dsl_Task2 = dsl_Task2
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def ignoreBehavior(self) -> bool:
        return self.__ignoreBehavior

    @ignoreBehavior.setter
    def ignoreBehavior(self, ignoreBehavior: bool):
        self.__ignoreBehavior = ignoreBehavior

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsl_Task2(self):
        return self.__dsl_Task2

    @dsl_Task2.setter
    def dsl_Task2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Task__dsl_Task2", None)
        self.__dsl_Task2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_SensorType"):
                opp_val = getattr(old_value, "dsl_SensorType", None)
                if opp_val == self:
                    setattr(old_value, "dsl_SensorType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_SensorType"):
                opp_val = getattr(value, "dsl_SensorType", None)
                setattr(value, "dsl_SensorType", self)

    @property
    def dsl_Task(self):
        return self.__dsl_Task

    @dsl_Task.setter
    def dsl_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Task__dsl_Task", None)
        self.__dsl_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Mission"):
                opp_val = getattr(old_value, "dsl_Mission", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Mission"):
                opp_val = getattr(value, "dsl_Mission", None)
                if opp_val is None:
                    setattr(value, "dsl_Mission", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dsl_Mission:

    pass