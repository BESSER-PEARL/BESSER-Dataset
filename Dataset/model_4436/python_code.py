from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CompareOperator(Enum):
    EQ = "EQ"
    NEQ = "NEQ"
    GEQ = "GEQ"
    G = "G"
    LEQ = "LEQ"
    L = "L"
class Actions(Enum):
    ROTATE_L = "ROTATE_L"
    ROTATE_R = "ROTATE_R"
    DRIVE_FORWARD = "DRIVE_FORWARD"
    DRIVE_BACKWARD = "DRIVE_BACKWARD"
    STOP_DRIVING = "STOP_DRIVING"
    TURN_AROUND = "TURN_AROUND"
    BEEP = "BEEP"
    MEASURE = "MEASURE"
    DRIVETOEDGE = "DRIVETOEDGE"
class TouchSensorSides(Enum):
    RIGHT = "RIGHT"
    BOTH = "BOTH"
    LEFT = "LEFT"
class Directions(Enum):
    E = "E"
    SE = "SE"
    S = "S"
    SW = "SW"
    W = "W"
    NW = "NW"
    N = "N"
    NE = "NE"
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
    WHITE = "WHITE"
    YELLOW = "YELLOW"
    PINK = "PINK"
    RED = "RED"


############################################
# Definition of Classes
############################################

class SensorType:

    pass
class dsl_UltrasonicSensor(SensorType):

    def __init__(self, comparator: str, distance: str):
        self.comparator = comparator
        self.distance = distance
        
        pass
    @property
    def comparator(self):
        return self.__comparator

    @comparator.setter
    def comparator(self, comparator: str):
        self.__comparator = comparator


    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance


class dsl_TouchSensor(SensorType):

    def __init__(self, key: str):
        self.key = key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class dsl_ColorSensor(SensorType):

    def __init__(self, key: str):
        self.key = key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class dsl_Ignorables:

    def __init__(self, AVOID_OBJECTS: str):
        self.AVOID_OBJECTS = AVOID_OBJECTS
        
        pass
    @property
    def AVOID_OBJECTS(self):
        return self.__AVOID_OBJECTS

    @AVOID_OBJECTS.setter
    def AVOID_OBJECTS(self, AVOID_OBJECTS: str):
        self.__AVOID_OBJECTS = AVOID_OBJECTS


class dsl_SensorType:

    pass
class dsl_Task:

    def __init__(self, action: str, ignoreBehavior: bool, name: str, dsl_Task: "dsl_Mission" = None, dsl_Task2: "dsl_SensorType" = None):
        self.action = action
        self.ignoreBehavior = ignoreBehavior
        self.name = name
        self.dsl_Task = dsl_Task
        self.dsl_Task2 = dsl_Task2
        
        pass
    @property
    def ignoreBehavior(self):
        return self.__ignoreBehavior

    @ignoreBehavior.setter
    def ignoreBehavior(self, ignoreBehavior: bool):
        self.__ignoreBehavior = ignoreBehavior


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


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

class dsl_Mission:

    pass