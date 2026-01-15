from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MissionType(Enum):
    AVOID = "AVOID"
    FIND = "FIND"
    FINDINORDER = "FINDINORDER"
    FINDSIMULTANEOUS = "FINDSIMULTANEOUS"
class Sensor(Enum):
    proximity = "proximity"
    touch = "touch"
    color = "color"
class Color(Enum):
    BLACK = "BLACK"
    BLUE = "BLUE"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"
    WHITE = "WHITE"
    BROWN = "BROWN"
class Relation(Enum):
    EQ = "EQ"
    LT = "LT"
    LE = "LE"
    GT = "GT"
    GE = "GE"
class EV3_ACTION(Enum):
    STOP = "STOP"
    REVERSE = "REVERSE"
    PLAY = "PLAY"
    ROTATE = "ROTATE"
    HALT = "HALT"


############################################
# Definition of Classes
############################################

class missionsDSL_Value:

    def __init__(self, color: str, integer: int, bool: str, missionsDSL_Value: "missionsDSL_Condition" = None):
        self.color = color
        self.integer = integer
        self.bool = bool
        self.missionsDSL_Value = missionsDSL_Value
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def bool(self) -> str:
        return self.__bool

    @bool.setter
    def bool(self, bool: str):
        self.__bool = bool

    @property
    def integer(self) -> int:
        return self.__integer

    @integer.setter
    def integer(self, integer: int):
        self.__integer = integer

    @property
    def missionsDSL_Value(self):
        return self.__missionsDSL_Value

    @missionsDSL_Value.setter
    def missionsDSL_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Value__missionsDSL_Value", None)
        self.__missionsDSL_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "missionsDSL_Condition11"):
                opp_val = getattr(old_value, "missionsDSL_Condition11", None)
                if opp_val == self:
                    setattr(old_value, "missionsDSL_Condition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "missionsDSL_Condition11"):
                opp_val = getattr(value, "missionsDSL_Condition11", None)
                setattr(value, "missionsDSL_Condition11", self)

class missionsDSL_NewMissions:

    pass
class missionsDSL_Action:

    def __init__(self, action: str, value: int, duration: int, missionsDSL_Action: "missionsDSL_Mission" = None, missionsDSL_Action14: "missionsDSL_Condition" = None):
        self.action = action
        self.value = value
        self.duration = duration
        self.missionsDSL_Action = missionsDSL_Action
        self.missionsDSL_Action14 = missionsDSL_Action14
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def missionsDSL_Action(self):
        return self.__missionsDSL_Action

    @missionsDSL_Action.setter
    def missionsDSL_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Action__missionsDSL_Action", None)
        self.__missionsDSL_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "missionsDSL_Mission7"):
                opp_val = getattr(old_value, "missionsDSL_Mission7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "missionsDSL_Mission7"):
                opp_val = getattr(value, "missionsDSL_Mission7", None)
                if opp_val is None:
                    setattr(value, "missionsDSL_Mission7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def missionsDSL_Action14(self):
        return self.__missionsDSL_Action14

    @missionsDSL_Action14.setter
    def missionsDSL_Action14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Action__missionsDSL_Action14", None)
        self.__missionsDSL_Action14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "missionsDSL_Condition13"):
                opp_val = getattr(old_value, "missionsDSL_Condition13", None)
                if opp_val == self:
                    setattr(old_value, "missionsDSL_Condition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "missionsDSL_Condition13"):
                opp_val = getattr(value, "missionsDSL_Condition13", None)
                setattr(value, "missionsDSL_Condition13", self)

class missionsDSL_Condition:

    def __init__(self, sensor: str, relation: str, missionsDSL_Condition: "missionsDSL_Mission" = None, missionsDSL_Condition11: "missionsDSL_Value" = None, missionsDSL_Condition13: "missionsDSL_Action" = None):
        self.sensor = sensor
        self.relation = relation
        self.missionsDSL_Condition = missionsDSL_Condition
        self.missionsDSL_Condition11 = missionsDSL_Condition11
        self.missionsDSL_Condition13 = missionsDSL_Condition13
        
    @property
    def sensor(self) -> str:
        return self.__sensor

    @sensor.setter
    def sensor(self, sensor: str):
        self.__sensor = sensor

    @property
    def relation(self) -> str:
        return self.__relation

    @relation.setter
    def relation(self, relation: str):
        self.__relation = relation

    @property
    def missionsDSL_Condition11(self):
        return self.__missionsDSL_Condition11

    @missionsDSL_Condition11.setter
    def missionsDSL_Condition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Condition__missionsDSL_Condition11", None)
        self.__missionsDSL_Condition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "missionsDSL_Value"):
                opp_val = getattr(old_value, "missionsDSL_Value", None)
                if opp_val == self:
                    setattr(old_value, "missionsDSL_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "missionsDSL_Value"):
                opp_val = getattr(value, "missionsDSL_Value", None)
                setattr(value, "missionsDSL_Value", self)

    @property
    def missionsDSL_Condition(self):
        return self.__missionsDSL_Condition

    @missionsDSL_Condition.setter
    def missionsDSL_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Condition__missionsDSL_Condition", None)
        self.__missionsDSL_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "missionsDSL_Mission5"):
                opp_val = getattr(old_value, "missionsDSL_Mission5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "missionsDSL_Mission5"):
                opp_val = getattr(value, "missionsDSL_Mission5", None)
                if opp_val is None:
                    setattr(value, "missionsDSL_Mission5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def missionsDSL_Condition13(self):
        return self.__missionsDSL_Condition13

    @missionsDSL_Condition13.setter
    def missionsDSL_Condition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Condition__missionsDSL_Condition13", None)
        self.__missionsDSL_Condition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "missionsDSL_Action14"):
                opp_val = getattr(old_value, "missionsDSL_Action14", None)
                if opp_val == self:
                    setattr(old_value, "missionsDSL_Action14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "missionsDSL_Action14"):
                opp_val = getattr(value, "missionsDSL_Action14", None)
                setattr(value, "missionsDSL_Action14", self)

class missionsDSL_Mission:

    def __init__(self, name: str, priority: int, type: str, missionsDSL_Mission: "missionsDSL_Robot" = None, missionsDSL_Mission3: "missionsDSL_Robot" = None, missionsDSL_Mission5: set["missionsDSL_Condition"] = None, missionsDSL_Mission7: set["missionsDSL_Action"] = None, missionsDSL_Mission9: "missionsDSL_NewMissions" = None, missionsDSL_Mission17: "missionsDSL_NewMissions" = None):
        self.name = name
        self.priority = priority
        self.type = type
        self.missionsDSL_Mission = missionsDSL_Mission
        self.missionsDSL_Mission3 = missionsDSL_Mission3
        self.missionsDSL_Mission5 = missionsDSL_Mission5 if missionsDSL_Mission5 is not None else set()
        self.missionsDSL_Mission7 = missionsDSL_Mission7 if missionsDSL_Mission7 is not None else set()
        self.missionsDSL_Mission9 = missionsDSL_Mission9
        self.missionsDSL_Mission17 = missionsDSL_Mission17
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def missionsDSL_Mission9(self):
        return self.__missionsDSL_Mission9

    @missionsDSL_Mission9.setter
    def missionsDSL_Mission9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Mission__missionsDSL_Mission9", None)
        self.__missionsDSL_Mission9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "missionsDSL_NewMissions"):
                opp_val = getattr(old_value, "missionsDSL_NewMissions", None)
                if opp_val == self:
                    setattr(old_value, "missionsDSL_NewMissions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "missionsDSL_NewMissions"):
                opp_val = getattr(value, "missionsDSL_NewMissions", None)
                setattr(value, "missionsDSL_NewMissions", self)

    @property
    def missionsDSL_Mission5(self):
        return self.__missionsDSL_Mission5

    @missionsDSL_Mission5.setter
    def missionsDSL_Mission5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Mission__missionsDSL_Mission5", None)
        self.__missionsDSL_Mission5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "missionsDSL_Condition"):
                    opp_val = getattr(item, "missionsDSL_Condition", None)
                    
                    if opp_val == self:
                        setattr(item, "missionsDSL_Condition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "missionsDSL_Condition"):
                    opp_val = getattr(item, "missionsDSL_Condition", None)
                    
                    setattr(item, "missionsDSL_Condition", self)
                    

    @property
    def missionsDSL_Mission17(self):
        return self.__missionsDSL_Mission17

    @missionsDSL_Mission17.setter
    def missionsDSL_Mission17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Mission__missionsDSL_Mission17", None)
        self.__missionsDSL_Mission17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "missionsDSL_NewMissions16"):
                opp_val = getattr(old_value, "missionsDSL_NewMissions16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "missionsDSL_NewMissions16"):
                opp_val = getattr(value, "missionsDSL_NewMissions16", None)
                if opp_val is None:
                    setattr(value, "missionsDSL_NewMissions16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def missionsDSL_Mission3(self):
        return self.__missionsDSL_Mission3

    @missionsDSL_Mission3.setter
    def missionsDSL_Mission3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Mission__missionsDSL_Mission3", None)
        self.__missionsDSL_Mission3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "missionsDSL_Robot2"):
                opp_val = getattr(old_value, "missionsDSL_Robot2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "missionsDSL_Robot2"):
                opp_val = getattr(value, "missionsDSL_Robot2", None)
                if opp_val is None:
                    setattr(value, "missionsDSL_Robot2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def missionsDSL_Mission7(self):
        return self.__missionsDSL_Mission7

    @missionsDSL_Mission7.setter
    def missionsDSL_Mission7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Mission__missionsDSL_Mission7", None)
        self.__missionsDSL_Mission7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "missionsDSL_Action"):
                    opp_val = getattr(item, "missionsDSL_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "missionsDSL_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "missionsDSL_Action"):
                    opp_val = getattr(item, "missionsDSL_Action", None)
                    
                    setattr(item, "missionsDSL_Action", self)
                    

    @property
    def missionsDSL_Mission(self):
        return self.__missionsDSL_Mission

    @missionsDSL_Mission.setter
    def missionsDSL_Mission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Mission__missionsDSL_Mission", None)
        self.__missionsDSL_Mission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "missionsDSL_Robot"):
                opp_val = getattr(old_value, "missionsDSL_Robot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "missionsDSL_Robot"):
                opp_val = getattr(value, "missionsDSL_Robot", None)
                if opp_val is None:
                    setattr(value, "missionsDSL_Robot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class missionsDSL_Robot:

    def __init__(self, slaveAddress: str, refreshRate: int, defaultSpeed: int, slowSpeed: int, minAngle: int, maxAngle: int, missionsDSL_Robot: set["missionsDSL_Mission"] = None, missionsDSL_Robot2: set["missionsDSL_Mission"] = None):
        self.slaveAddress = slaveAddress
        self.refreshRate = refreshRate
        self.defaultSpeed = defaultSpeed
        self.slowSpeed = slowSpeed
        self.minAngle = minAngle
        self.maxAngle = maxAngle
        self.missionsDSL_Robot = missionsDSL_Robot if missionsDSL_Robot is not None else set()
        self.missionsDSL_Robot2 = missionsDSL_Robot2 if missionsDSL_Robot2 is not None else set()
        
    @property
    def minAngle(self) -> int:
        return self.__minAngle

    @minAngle.setter
    def minAngle(self, minAngle: int):
        self.__minAngle = minAngle

    @property
    def defaultSpeed(self) -> int:
        return self.__defaultSpeed

    @defaultSpeed.setter
    def defaultSpeed(self, defaultSpeed: int):
        self.__defaultSpeed = defaultSpeed

    @property
    def slaveAddress(self) -> str:
        return self.__slaveAddress

    @slaveAddress.setter
    def slaveAddress(self, slaveAddress: str):
        self.__slaveAddress = slaveAddress

    @property
    def slowSpeed(self) -> int:
        return self.__slowSpeed

    @slowSpeed.setter
    def slowSpeed(self, slowSpeed: int):
        self.__slowSpeed = slowSpeed

    @property
    def maxAngle(self) -> int:
        return self.__maxAngle

    @maxAngle.setter
    def maxAngle(self, maxAngle: int):
        self.__maxAngle = maxAngle

    @property
    def refreshRate(self) -> int:
        return self.__refreshRate

    @refreshRate.setter
    def refreshRate(self, refreshRate: int):
        self.__refreshRate = refreshRate

    @property
    def missionsDSL_Robot(self):
        return self.__missionsDSL_Robot

    @missionsDSL_Robot.setter
    def missionsDSL_Robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Robot__missionsDSL_Robot", None)
        self.__missionsDSL_Robot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "missionsDSL_Mission"):
                    opp_val = getattr(item, "missionsDSL_Mission", None)
                    
                    if opp_val == self:
                        setattr(item, "missionsDSL_Mission", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "missionsDSL_Mission"):
                    opp_val = getattr(item, "missionsDSL_Mission", None)
                    
                    setattr(item, "missionsDSL_Mission", self)
                    

    @property
    def missionsDSL_Robot2(self):
        return self.__missionsDSL_Robot2

    @missionsDSL_Robot2.setter
    def missionsDSL_Robot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_missionsDSL_Robot__missionsDSL_Robot2", None)
        self.__missionsDSL_Robot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "missionsDSL_Mission3"):
                    opp_val = getattr(item, "missionsDSL_Mission3", None)
                    
                    if opp_val == self:
                        setattr(item, "missionsDSL_Mission3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "missionsDSL_Mission3"):
                    opp_val = getattr(item, "missionsDSL_Mission3", None)
                    
                    setattr(item, "missionsDSL_Mission3", self)
                    
