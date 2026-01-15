from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class Directions(Enum):
    SW = "SW"
    W = "W"
    NW = "NW"
    N = "N"
    NE = "NE"
    E = "E"
    SE = "SE"
    S = "S"
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
    ANY = "ANY"
class timeUnit(Enum):
    SECONDS = "SECONDS"
    MILISECONDS = "MILISECONDS"
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


############################################
# Definition of Classes
############################################

class dsl_SensorType:

    pass
class dsl_Task:

    def __init__(self, action: str, nrOfTimes: int, time: int, name: str, dsl_Task4: "dsl_Ignorables" = None, dsl_Task6: "dsl_timeUnitValue" = None, dsl_Task: "dsl_Mission" = None, dsl_Task2: "dsl_SensorType" = None):
        self.action = action
        self.nrOfTimes = nrOfTimes
        self.time = time
        self.name = name
        self.dsl_Task4 = dsl_Task4
        self.dsl_Task6 = dsl_Task6
        self.dsl_Task = dsl_Task
        self.dsl_Task2 = dsl_Task2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nrOfTimes(self) -> int:
        return self.__nrOfTimes

    @nrOfTimes.setter
    def nrOfTimes(self, nrOfTimes: int):
        self.__nrOfTimes = nrOfTimes

    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def dsl_Task6(self):
        return self.__dsl_Task6

    @dsl_Task6.setter
    def dsl_Task6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Task__dsl_Task6", None)
        self.__dsl_Task6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_timeUnitValue"):
                opp_val = getattr(old_value, "dsl_timeUnitValue", None)
                if opp_val == self:
                    setattr(old_value, "dsl_timeUnitValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_timeUnitValue"):
                opp_val = getattr(value, "dsl_timeUnitValue", None)
                setattr(value, "dsl_timeUnitValue", self)

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

    @property
    def dsl_Task4(self):
        return self.__dsl_Task4

    @dsl_Task4.setter
    def dsl_Task4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Task__dsl_Task4", None)
        self.__dsl_Task4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Ignorables"):
                opp_val = getattr(old_value, "dsl_Ignorables", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Ignorables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Ignorables"):
                opp_val = getattr(value, "dsl_Ignorables", None)
                setattr(value, "dsl_Ignorables", self)

class dsl_Mission:

    pass
class dsl_ColorValue:

    def __init__(self, color: str, dsl_ColorValue: "dsl_ColorSensor" = None, dsl_ColorValue10: "dsl_ColorSensor" = None):
        self.color = color
        self.dsl_ColorValue = dsl_ColorValue
        self.dsl_ColorValue10 = dsl_ColorValue10
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def dsl_ColorValue10(self):
        return self.__dsl_ColorValue10

    @dsl_ColorValue10.setter
    def dsl_ColorValue10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ColorValue__dsl_ColorValue10", None)
        self.__dsl_ColorValue10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ColorSensor9"):
                opp_val = getattr(old_value, "dsl_ColorSensor9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ColorSensor9"):
                opp_val = getattr(value, "dsl_ColorSensor9", None)
                if opp_val is None:
                    setattr(value, "dsl_ColorSensor9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsl_ColorValue(self):
        return self.__dsl_ColorValue

    @dsl_ColorValue.setter
    def dsl_ColorValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ColorValue__dsl_ColorValue", None)
        self.__dsl_ColorValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ColorSensor"):
                opp_val = getattr(old_value, "dsl_ColorSensor", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ColorSensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ColorSensor"):
                opp_val = getattr(value, "dsl_ColorSensor", None)
                setattr(value, "dsl_ColorSensor", self)

class SensorType:

    pass
class dsl_UltrasonicSensor(SensorType):

    def __init__(self, comparator: str, distance: str):
        self.comparator = comparator
        self.distance = distance
        
    @property
    def comparator(self) -> str:
        return self.__comparator

    @comparator.setter
    def comparator(self, comparator: str):
        self.__comparator = comparator

    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class dsl_TouchSensor(SensorType):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class dsl_ColorSensor(SensorType):

    def __init__(self, distinct: bool, dsl_ColorSensor: "dsl_ColorValue" = None, dsl_ColorSensor9: set["dsl_ColorValue"] = None):
        self.distinct = distinct
        self.dsl_ColorSensor = dsl_ColorSensor
        self.dsl_ColorSensor9 = dsl_ColorSensor9 if dsl_ColorSensor9 is not None else set()
        
    @property
    def distinct(self) -> bool:
        return self.__distinct

    @distinct.setter
    def distinct(self, distinct: bool):
        self.__distinct = distinct

    @property
    def dsl_ColorSensor(self):
        return self.__dsl_ColorSensor

    @dsl_ColorSensor.setter
    def dsl_ColorSensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ColorSensor__dsl_ColorSensor", None)
        self.__dsl_ColorSensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_ColorValue"):
                opp_val = getattr(old_value, "dsl_ColorValue", None)
                if opp_val == self:
                    setattr(old_value, "dsl_ColorValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_ColorValue"):
                opp_val = getattr(value, "dsl_ColorValue", None)
                setattr(value, "dsl_ColorValue", self)

    @property
    def dsl_ColorSensor9(self):
        return self.__dsl_ColorSensor9

    @dsl_ColorSensor9.setter
    def dsl_ColorSensor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_ColorSensor__dsl_ColorSensor9", None)
        self.__dsl_ColorSensor9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsl_ColorValue10"):
                    opp_val = getattr(item, "dsl_ColorValue10", None)
                    
                    if opp_val == self:
                        setattr(item, "dsl_ColorValue10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsl_ColorValue10"):
                    opp_val = getattr(item, "dsl_ColorValue10", None)
                    
                    setattr(item, "dsl_ColorValue10", self)
                    

class dsl_timeUnitValue:

    def __init__(self, unit: str, dsl_timeUnitValue: "dsl_Task" = None):
        self.unit = unit
        self.dsl_timeUnitValue = dsl_timeUnitValue
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def dsl_timeUnitValue(self):
        return self.__dsl_timeUnitValue

    @dsl_timeUnitValue.setter
    def dsl_timeUnitValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_timeUnitValue__dsl_timeUnitValue", None)
        self.__dsl_timeUnitValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Task6"):
                opp_val = getattr(old_value, "dsl_Task6", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Task6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Task6"):
                opp_val = getattr(value, "dsl_Task6", None)
                setattr(value, "dsl_Task6", self)

class dsl_Ignorables:

    def __init__(self, AVOID_OBJECTS: str, dsl_Ignorables: "dsl_Task" = None):
        self.AVOID_OBJECTS = AVOID_OBJECTS
        self.dsl_Ignorables = dsl_Ignorables
        
    @property
    def AVOID_OBJECTS(self) -> str:
        return self.__AVOID_OBJECTS

    @AVOID_OBJECTS.setter
    def AVOID_OBJECTS(self, AVOID_OBJECTS: str):
        self.__AVOID_OBJECTS = AVOID_OBJECTS

    @property
    def dsl_Ignorables(self):
        return self.__dsl_Ignorables

    @dsl_Ignorables.setter
    def dsl_Ignorables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsl_Ignorables__dsl_Ignorables", None)
        self.__dsl_Ignorables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsl_Task4"):
                opp_val = getattr(old_value, "dsl_Task4", None)
                if opp_val == self:
                    setattr(old_value, "dsl_Task4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsl_Task4"):
                opp_val = getattr(value, "dsl_Task4", None)
                setattr(value, "dsl_Task4", self)
