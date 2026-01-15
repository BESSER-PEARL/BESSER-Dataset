from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ColorName(Enum):
    RED = "RED"
    WHITE = "WHITE"
    BLACK = "BLACK"
    GREEN = "GREEN"
    BLUE = "BLUE"
class DirectionVal(Enum):
    FORWARD = "FORWARD"
    BACKWARD = "BACKWARD"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class SpeedVal(Enum):
    HIGH = "HIGH"
    MED = "MED"
    LOW = "LOW"
class BoolType(Enum):
    L = "L"
    G = "G"
    AND = "AND"
    OR = "OR"
    TRUE = "TRUE"
    FALSE = "FALSE"
class SensorType(Enum):
    COLOR = "COLOR"
    LEFTLIGHT = "LEFTLIGHT"
    RIGHTLIGHT = "RIGHTLIGHT"
    BACKUS = "BACKUS"
    FRONTUS = "FRONTUS"
    LEFTTOUCH = "LEFTTOUCH"
    RIGHTTOUCH = "RIGHTTOUCH"
    GYRO = "GYRO"
class SoundName(Enum):
    FANFARE = "FANFARE"
    BUZZ = "BUZZ"
class ArmOpType(Enum):
    UP = "UP"
    DOWN = "DOWN"


############################################
# Definition of Classes
############################################

class robotDSL_Sound:

    def __init__(self, soundName: str, robotDSL_Sound: "robotDSL_Action" = None):
        self.soundName = soundName
        self.robotDSL_Sound = robotDSL_Sound
        
    @property
    def soundName(self) -> str:
        return self.__soundName

    @soundName.setter
    def soundName(self, soundName: str):
        self.__soundName = soundName

    @property
    def robotDSL_Sound(self):
        return self.__robotDSL_Sound

    @robotDSL_Sound.setter
    def robotDSL_Sound(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Sound__robotDSL_Sound", None)
        self.__robotDSL_Sound = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Action32"):
                opp_val = getattr(old_value, "robotDSL_Action32", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Action32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Action32"):
                opp_val = getattr(value, "robotDSL_Action32", None)
                setattr(value, "robotDSL_Action32", self)

class robotDSL_ArmOp:

    def __init__(self, opType: str, robotDSL_ArmOp: "robotDSL_Action" = None):
        self.opType = opType
        self.robotDSL_ArmOp = robotDSL_ArmOp
        
    @property
    def opType(self) -> str:
        return self.__opType

    @opType.setter
    def opType(self, opType: str):
        self.__opType = opType

    @property
    def robotDSL_ArmOp(self):
        return self.__robotDSL_ArmOp

    @robotDSL_ArmOp.setter
    def robotDSL_ArmOp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_ArmOp__robotDSL_ArmOp", None)
        self.__robotDSL_ArmOp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Action30"):
                opp_val = getattr(old_value, "robotDSL_Action30", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Action30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Action30"):
                opp_val = getattr(value, "robotDSL_Action30", None)
                setattr(value, "robotDSL_Action30", self)

class robotDSL_Speed:

    def __init__(self, speed: str, robotDSL_Speed: "robotDSL_Action" = None):
        self.speed = speed
        self.robotDSL_Speed = robotDSL_Speed
        
    @property
    def speed(self) -> str:
        return self.__speed

    @speed.setter
    def speed(self, speed: str):
        self.__speed = speed

    @property
    def robotDSL_Speed(self):
        return self.__robotDSL_Speed

    @robotDSL_Speed.setter
    def robotDSL_Speed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Speed__robotDSL_Speed", None)
        self.__robotDSL_Speed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Action22"):
                opp_val = getattr(old_value, "robotDSL_Action22", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Action22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Action22"):
                opp_val = getattr(value, "robotDSL_Action22", None)
                setattr(value, "robotDSL_Action22", self)

class robotDSL_Distance:

    def __init__(self, distance: int, robotDSL_Distance: "robotDSL_Trigger" = None, robotDSL_Distance53: "robotDSL_Bool" = None):
        self.distance = distance
        self.robotDSL_Distance = robotDSL_Distance
        self.robotDSL_Distance53 = robotDSL_Distance53
        
    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

    @property
    def robotDSL_Distance53(self):
        return self.__robotDSL_Distance53

    @robotDSL_Distance53.setter
    def robotDSL_Distance53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Distance__robotDSL_Distance53", None)
        self.__robotDSL_Distance53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Bool54"):
                opp_val = getattr(old_value, "robotDSL_Bool54", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Bool54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Bool54"):
                opp_val = getattr(value, "robotDSL_Bool54", None)
                setattr(value, "robotDSL_Bool54", self)

    @property
    def robotDSL_Distance(self):
        return self.__robotDSL_Distance

    @robotDSL_Distance.setter
    def robotDSL_Distance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Distance__robotDSL_Distance", None)
        self.__robotDSL_Distance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Trigger51"):
                opp_val = getattr(old_value, "robotDSL_Trigger51", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Trigger51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Trigger51"):
                opp_val = getattr(value, "robotDSL_Trigger51", None)
                setattr(value, "robotDSL_Trigger51", self)

class robotDSL_Color:

    def __init__(self, colorName: str, robotDSL_Color: "robotDSL_Trigger" = None):
        self.colorName = colorName
        self.robotDSL_Color = robotDSL_Color
        
    @property
    def colorName(self) -> str:
        return self.__colorName

    @colorName.setter
    def colorName(self, colorName: str):
        self.__colorName = colorName

    @property
    def robotDSL_Color(self):
        return self.__robotDSL_Color

    @robotDSL_Color.setter
    def robotDSL_Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Color__robotDSL_Color", None)
        self.__robotDSL_Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Trigger49"):
                opp_val = getattr(old_value, "robotDSL_Trigger49", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Trigger49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Trigger49"):
                opp_val = getattr(value, "robotDSL_Trigger49", None)
                setattr(value, "robotDSL_Trigger49", self)

class robotDSL_Sensor:

    def __init__(self, sensorType: str, robotDSL_Sensor: "robotDSL_Trigger" = None):
        self.sensorType = sensorType
        self.robotDSL_Sensor = robotDSL_Sensor
        
    @property
    def sensorType(self) -> str:
        return self.__sensorType

    @sensorType.setter
    def sensorType(self, sensorType: str):
        self.__sensorType = sensorType

    @property
    def robotDSL_Sensor(self):
        return self.__robotDSL_Sensor

    @robotDSL_Sensor.setter
    def robotDSL_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Sensor__robotDSL_Sensor", None)
        self.__robotDSL_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Trigger47"):
                opp_val = getattr(old_value, "robotDSL_Trigger47", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Trigger47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Trigger47"):
                opp_val = getattr(value, "robotDSL_Trigger47", None)
                setattr(value, "robotDSL_Trigger47", self)

class robotDSL_Negation:

    def __init__(self, NOT: str, robotDSL_Negation: "robotDSL_Trigger" = None):
        self.NOT = NOT
        self.robotDSL_Negation = robotDSL_Negation
        
    @property
    def NOT(self) -> str:
        return self.__NOT

    @NOT.setter
    def NOT(self, NOT: str):
        self.__NOT = NOT

    @property
    def robotDSL_Negation(self):
        return self.__robotDSL_Negation

    @robotDSL_Negation.setter
    def robotDSL_Negation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Negation__robotDSL_Negation", None)
        self.__robotDSL_Negation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Trigger42"):
                opp_val = getattr(old_value, "robotDSL_Trigger42", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Trigger42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Trigger42"):
                opp_val = getattr(value, "robotDSL_Trigger42", None)
                setattr(value, "robotDSL_Trigger42", self)

class robotDSL_Bool:

    def __init__(self, boolType: str, robotDSL_Bool: "robotDSL_Action" = None, robotDSL_Bool40: "robotDSL_Trigger" = None, robotDSL_Bool54: "robotDSL_Distance" = None):
        self.boolType = boolType
        self.robotDSL_Bool = robotDSL_Bool
        self.robotDSL_Bool40 = robotDSL_Bool40
        self.robotDSL_Bool54 = robotDSL_Bool54
        
    @property
    def boolType(self) -> str:
        return self.__boolType

    @boolType.setter
    def boolType(self, boolType: str):
        self.__boolType = boolType

    @property
    def robotDSL_Bool(self):
        return self.__robotDSL_Bool

    @robotDSL_Bool.setter
    def robotDSL_Bool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Bool__robotDSL_Bool", None)
        self.__robotDSL_Bool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Action37"):
                opp_val = getattr(old_value, "robotDSL_Action37", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Action37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Action37"):
                opp_val = getattr(value, "robotDSL_Action37", None)
                setattr(value, "robotDSL_Action37", self)

    @property
    def robotDSL_Bool54(self):
        return self.__robotDSL_Bool54

    @robotDSL_Bool54.setter
    def robotDSL_Bool54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Bool__robotDSL_Bool54", None)
        self.__robotDSL_Bool54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Distance53"):
                opp_val = getattr(old_value, "robotDSL_Distance53", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Distance53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Distance53"):
                opp_val = getattr(value, "robotDSL_Distance53", None)
                setattr(value, "robotDSL_Distance53", self)

    @property
    def robotDSL_Bool40(self):
        return self.__robotDSL_Bool40

    @robotDSL_Bool40.setter
    def robotDSL_Bool40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Bool__robotDSL_Bool40", None)
        self.__robotDSL_Bool40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Trigger39"):
                opp_val = getattr(old_value, "robotDSL_Trigger39", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Trigger39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Trigger39"):
                opp_val = getattr(value, "robotDSL_Trigger39", None)
                setattr(value, "robotDSL_Trigger39", self)

class robotDSL_Missions:

    def __init__(self, name: str, robotDSL_Missions: set["robotDSL_Mission"] = None):
        self.name = name
        self.robotDSL_Missions = robotDSL_Missions if robotDSL_Missions is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robotDSL_Missions(self):
        return self.__robotDSL_Missions

    @robotDSL_Missions.setter
    def robotDSL_Missions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Missions__robotDSL_Missions", None)
        self.__robotDSL_Missions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotDSL_Mission"):
                    opp_val = getattr(item, "robotDSL_Mission", None)
                    
                    if opp_val == self:
                        setattr(item, "robotDSL_Mission", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotDSL_Mission"):
                    opp_val = getattr(item, "robotDSL_Mission", None)
                    
                    setattr(item, "robotDSL_Mission", self)
                    

class robotDSL_Direction:

    def __init__(self, dir: str, robotDSL_Direction: "robotDSL_Action" = None, robotDSL_Direction25: "robotDSL_Action" = None):
        self.dir = dir
        self.robotDSL_Direction = robotDSL_Direction
        self.robotDSL_Direction25 = robotDSL_Direction25
        
    @property
    def dir(self) -> str:
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir

    @property
    def robotDSL_Direction(self):
        return self.__robotDSL_Direction

    @robotDSL_Direction.setter
    def robotDSL_Direction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Direction__robotDSL_Direction", None)
        self.__robotDSL_Direction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Action20"):
                opp_val = getattr(old_value, "robotDSL_Action20", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Action20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Action20"):
                opp_val = getattr(value, "robotDSL_Action20", None)
                setattr(value, "robotDSL_Action20", self)

    @property
    def robotDSL_Direction25(self):
        return self.__robotDSL_Direction25

    @robotDSL_Direction25.setter
    def robotDSL_Direction25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Direction__robotDSL_Direction25", None)
        self.__robotDSL_Direction25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Action24"):
                opp_val = getattr(old_value, "robotDSL_Action24", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Action24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Action24"):
                opp_val = getattr(value, "robotDSL_Action24", None)
                setattr(value, "robotDSL_Action24", self)

class robotDSL_Action:

    def __init__(self, duration: int, cent: str, degr: int, robotDSL_Action: "robotDSL_Goal" = None, robotDSL_Action18: "robotDSL_Task" = None, robotDSL_Action20: "robotDSL_Direction" = None, robotDSL_Action37: "robotDSL_Bool" = None, robotDSL_Action22: "robotDSL_Speed" = None, robotDSL_Action24: "robotDSL_Direction" = None, robotDSL_Action27: set["robotDSL_Trigger"] = None, robotDSL_Action30: "robotDSL_ArmOp" = None, robotDSL_Action32: "robotDSL_Sound" = None, robotDSL_Action34: "robotDSL_Flag" = None):
        self.duration = duration
        self.cent = cent
        self.degr = degr
        self.robotDSL_Action = robotDSL_Action
        self.robotDSL_Action18 = robotDSL_Action18
        self.robotDSL_Action20 = robotDSL_Action20
        self.robotDSL_Action37 = robotDSL_Action37
        self.robotDSL_Action22 = robotDSL_Action22
        self.robotDSL_Action24 = robotDSL_Action24
        self.robotDSL_Action27 = robotDSL_Action27 if robotDSL_Action27 is not None else set()
        self.robotDSL_Action30 = robotDSL_Action30
        self.robotDSL_Action32 = robotDSL_Action32
        self.robotDSL_Action34 = robotDSL_Action34
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def degr(self) -> int:
        return self.__degr

    @degr.setter
    def degr(self, degr: int):
        self.__degr = degr

    @property
    def cent(self) -> str:
        return self.__cent

    @cent.setter
    def cent(self, cent: str):
        self.__cent = cent

    @property
    def robotDSL_Action24(self):
        return self.__robotDSL_Action24

    @robotDSL_Action24.setter
    def robotDSL_Action24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Action__robotDSL_Action24", None)
        self.__robotDSL_Action24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Direction25"):
                opp_val = getattr(old_value, "robotDSL_Direction25", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Direction25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Direction25"):
                opp_val = getattr(value, "robotDSL_Direction25", None)
                setattr(value, "robotDSL_Direction25", self)

    @property
    def robotDSL_Action30(self):
        return self.__robotDSL_Action30

    @robotDSL_Action30.setter
    def robotDSL_Action30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Action__robotDSL_Action30", None)
        self.__robotDSL_Action30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_ArmOp"):
                opp_val = getattr(old_value, "robotDSL_ArmOp", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_ArmOp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_ArmOp"):
                opp_val = getattr(value, "robotDSL_ArmOp", None)
                setattr(value, "robotDSL_ArmOp", self)

    @property
    def robotDSL_Action27(self):
        return self.__robotDSL_Action27

    @robotDSL_Action27.setter
    def robotDSL_Action27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Action__robotDSL_Action27", None)
        self.__robotDSL_Action27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotDSL_Trigger28"):
                    opp_val = getattr(item, "robotDSL_Trigger28", None)
                    
                    if opp_val == self:
                        setattr(item, "robotDSL_Trigger28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotDSL_Trigger28"):
                    opp_val = getattr(item, "robotDSL_Trigger28", None)
                    
                    setattr(item, "robotDSL_Trigger28", self)
                    

    @property
    def robotDSL_Action18(self):
        return self.__robotDSL_Action18

    @robotDSL_Action18.setter
    def robotDSL_Action18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Action__robotDSL_Action18", None)
        self.__robotDSL_Action18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Task17"):
                opp_val = getattr(old_value, "robotDSL_Task17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Task17"):
                opp_val = getattr(value, "robotDSL_Task17", None)
                if opp_val is None:
                    setattr(value, "robotDSL_Task17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotDSL_Action(self):
        return self.__robotDSL_Action

    @robotDSL_Action.setter
    def robotDSL_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Action__robotDSL_Action", None)
        self.__robotDSL_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Goal12"):
                opp_val = getattr(old_value, "robotDSL_Goal12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Goal12"):
                opp_val = getattr(value, "robotDSL_Goal12", None)
                if opp_val is None:
                    setattr(value, "robotDSL_Goal12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotDSL_Action22(self):
        return self.__robotDSL_Action22

    @robotDSL_Action22.setter
    def robotDSL_Action22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Action__robotDSL_Action22", None)
        self.__robotDSL_Action22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Speed"):
                opp_val = getattr(old_value, "robotDSL_Speed", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Speed", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Speed"):
                opp_val = getattr(value, "robotDSL_Speed", None)
                setattr(value, "robotDSL_Speed", self)

    @property
    def robotDSL_Action32(self):
        return self.__robotDSL_Action32

    @robotDSL_Action32.setter
    def robotDSL_Action32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Action__robotDSL_Action32", None)
        self.__robotDSL_Action32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Sound"):
                opp_val = getattr(old_value, "robotDSL_Sound", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Sound", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Sound"):
                opp_val = getattr(value, "robotDSL_Sound", None)
                setattr(value, "robotDSL_Sound", self)

    @property
    def robotDSL_Action37(self):
        return self.__robotDSL_Action37

    @robotDSL_Action37.setter
    def robotDSL_Action37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Action__robotDSL_Action37", None)
        self.__robotDSL_Action37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Bool"):
                opp_val = getattr(old_value, "robotDSL_Bool", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Bool", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Bool"):
                opp_val = getattr(value, "robotDSL_Bool", None)
                setattr(value, "robotDSL_Bool", self)

    @property
    def robotDSL_Action20(self):
        return self.__robotDSL_Action20

    @robotDSL_Action20.setter
    def robotDSL_Action20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Action__robotDSL_Action20", None)
        self.__robotDSL_Action20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Direction"):
                opp_val = getattr(old_value, "robotDSL_Direction", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Direction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Direction"):
                opp_val = getattr(value, "robotDSL_Direction", None)
                setattr(value, "robotDSL_Direction", self)

    @property
    def robotDSL_Action34(self):
        return self.__robotDSL_Action34

    @robotDSL_Action34.setter
    def robotDSL_Action34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Action__robotDSL_Action34", None)
        self.__robotDSL_Action34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Flag35"):
                opp_val = getattr(old_value, "robotDSL_Flag35", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Flag35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Flag35"):
                opp_val = getattr(value, "robotDSL_Flag35", None)
                setattr(value, "robotDSL_Flag35", self)

class robotDSL_Time:

    def __init__(self, sec: int, robotDSL_Time: "robotDSL_Goal" = None):
        self.sec = sec
        self.robotDSL_Time = robotDSL_Time
        
    @property
    def sec(self) -> int:
        return self.__sec

    @sec.setter
    def sec(self, sec: int):
        self.__sec = sec

    @property
    def robotDSL_Time(self):
        return self.__robotDSL_Time

    @robotDSL_Time.setter
    def robotDSL_Time(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Time__robotDSL_Time", None)
        self.__robotDSL_Time = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Goal10"):
                opp_val = getattr(old_value, "robotDSL_Goal10", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Goal10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Goal10"):
                opp_val = getattr(value, "robotDSL_Goal10", None)
                setattr(value, "robotDSL_Goal10", self)

class robotDSL_Trigger:

    def __init__(self, touching: str, degrees: int, robotDSL_Trigger: "robotDSL_Goal" = None, robotDSL_Trigger15: "robotDSL_Task" = None, robotDSL_Trigger39: "robotDSL_Bool" = None, robotDSL_Trigger42: "robotDSL_Negation" = None, robotDSL_Trigger44: "robotDSL_Flag" = None, robotDSL_Trigger47: "robotDSL_Sensor" = None, robotDSL_Trigger49: "robotDSL_Color" = None, robotDSL_Trigger51: "robotDSL_Distance" = None, robotDSL_Trigger28: "robotDSL_Action" = None):
        self.touching = touching
        self.degrees = degrees
        self.robotDSL_Trigger = robotDSL_Trigger
        self.robotDSL_Trigger15 = robotDSL_Trigger15
        self.robotDSL_Trigger39 = robotDSL_Trigger39
        self.robotDSL_Trigger42 = robotDSL_Trigger42
        self.robotDSL_Trigger44 = robotDSL_Trigger44
        self.robotDSL_Trigger47 = robotDSL_Trigger47
        self.robotDSL_Trigger49 = robotDSL_Trigger49
        self.robotDSL_Trigger51 = robotDSL_Trigger51
        self.robotDSL_Trigger28 = robotDSL_Trigger28
        
    @property
    def degrees(self) -> int:
        return self.__degrees

    @degrees.setter
    def degrees(self, degrees: int):
        self.__degrees = degrees

    @property
    def touching(self) -> str:
        return self.__touching

    @touching.setter
    def touching(self, touching: str):
        self.__touching = touching

    @property
    def robotDSL_Trigger42(self):
        return self.__robotDSL_Trigger42

    @robotDSL_Trigger42.setter
    def robotDSL_Trigger42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Trigger__robotDSL_Trigger42", None)
        self.__robotDSL_Trigger42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Negation"):
                opp_val = getattr(old_value, "robotDSL_Negation", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Negation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Negation"):
                opp_val = getattr(value, "robotDSL_Negation", None)
                setattr(value, "robotDSL_Negation", self)

    @property
    def robotDSL_Trigger51(self):
        return self.__robotDSL_Trigger51

    @robotDSL_Trigger51.setter
    def robotDSL_Trigger51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Trigger__robotDSL_Trigger51", None)
        self.__robotDSL_Trigger51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Distance"):
                opp_val = getattr(old_value, "robotDSL_Distance", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Distance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Distance"):
                opp_val = getattr(value, "robotDSL_Distance", None)
                setattr(value, "robotDSL_Distance", self)

    @property
    def robotDSL_Trigger47(self):
        return self.__robotDSL_Trigger47

    @robotDSL_Trigger47.setter
    def robotDSL_Trigger47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Trigger__robotDSL_Trigger47", None)
        self.__robotDSL_Trigger47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Sensor"):
                opp_val = getattr(old_value, "robotDSL_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Sensor"):
                opp_val = getattr(value, "robotDSL_Sensor", None)
                setattr(value, "robotDSL_Sensor", self)

    @property
    def robotDSL_Trigger(self):
        return self.__robotDSL_Trigger

    @robotDSL_Trigger.setter
    def robotDSL_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Trigger__robotDSL_Trigger", None)
        self.__robotDSL_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Goal8"):
                opp_val = getattr(old_value, "robotDSL_Goal8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Goal8"):
                opp_val = getattr(value, "robotDSL_Goal8", None)
                if opp_val is None:
                    setattr(value, "robotDSL_Goal8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotDSL_Trigger39(self):
        return self.__robotDSL_Trigger39

    @robotDSL_Trigger39.setter
    def robotDSL_Trigger39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Trigger__robotDSL_Trigger39", None)
        self.__robotDSL_Trigger39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Bool40"):
                opp_val = getattr(old_value, "robotDSL_Bool40", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Bool40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Bool40"):
                opp_val = getattr(value, "robotDSL_Bool40", None)
                setattr(value, "robotDSL_Bool40", self)

    @property
    def robotDSL_Trigger44(self):
        return self.__robotDSL_Trigger44

    @robotDSL_Trigger44.setter
    def robotDSL_Trigger44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Trigger__robotDSL_Trigger44", None)
        self.__robotDSL_Trigger44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Flag45"):
                opp_val = getattr(old_value, "robotDSL_Flag45", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Flag45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Flag45"):
                opp_val = getattr(value, "robotDSL_Flag45", None)
                setattr(value, "robotDSL_Flag45", self)

    @property
    def robotDSL_Trigger49(self):
        return self.__robotDSL_Trigger49

    @robotDSL_Trigger49.setter
    def robotDSL_Trigger49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Trigger__robotDSL_Trigger49", None)
        self.__robotDSL_Trigger49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Color"):
                opp_val = getattr(old_value, "robotDSL_Color", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Color"):
                opp_val = getattr(value, "robotDSL_Color", None)
                setattr(value, "robotDSL_Color", self)

    @property
    def robotDSL_Trigger28(self):
        return self.__robotDSL_Trigger28

    @robotDSL_Trigger28.setter
    def robotDSL_Trigger28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Trigger__robotDSL_Trigger28", None)
        self.__robotDSL_Trigger28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Action27"):
                opp_val = getattr(old_value, "robotDSL_Action27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Action27"):
                opp_val = getattr(value, "robotDSL_Action27", None)
                if opp_val is None:
                    setattr(value, "robotDSL_Action27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotDSL_Trigger15(self):
        return self.__robotDSL_Trigger15

    @robotDSL_Trigger15.setter
    def robotDSL_Trigger15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Trigger__robotDSL_Trigger15", None)
        self.__robotDSL_Trigger15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Task14"):
                opp_val = getattr(old_value, "robotDSL_Task14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Task14"):
                opp_val = getattr(value, "robotDSL_Task14", None)
                if opp_val is None:
                    setattr(value, "robotDSL_Task14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class robotDSL_Goal:

    pass
class robotDSL_Task:

    def __init__(self, name: str, prio: int, robotDSL_Task: "robotDSL_Mission" = None, robotDSL_Task14: set["robotDSL_Trigger"] = None, robotDSL_Task17: set["robotDSL_Action"] = None):
        self.name = name
        self.prio = prio
        self.robotDSL_Task = robotDSL_Task
        self.robotDSL_Task14 = robotDSL_Task14 if robotDSL_Task14 is not None else set()
        self.robotDSL_Task17 = robotDSL_Task17 if robotDSL_Task17 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def prio(self) -> int:
        return self.__prio

    @prio.setter
    def prio(self, prio: int):
        self.__prio = prio

    @property
    def robotDSL_Task17(self):
        return self.__robotDSL_Task17

    @robotDSL_Task17.setter
    def robotDSL_Task17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Task__robotDSL_Task17", None)
        self.__robotDSL_Task17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotDSL_Action18"):
                    opp_val = getattr(item, "robotDSL_Action18", None)
                    
                    if opp_val == self:
                        setattr(item, "robotDSL_Action18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotDSL_Action18"):
                    opp_val = getattr(item, "robotDSL_Action18", None)
                    
                    setattr(item, "robotDSL_Action18", self)
                    

    @property
    def robotDSL_Task14(self):
        return self.__robotDSL_Task14

    @robotDSL_Task14.setter
    def robotDSL_Task14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Task__robotDSL_Task14", None)
        self.__robotDSL_Task14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotDSL_Trigger15"):
                    opp_val = getattr(item, "robotDSL_Trigger15", None)
                    
                    if opp_val == self:
                        setattr(item, "robotDSL_Trigger15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotDSL_Trigger15"):
                    opp_val = getattr(item, "robotDSL_Trigger15", None)
                    
                    setattr(item, "robotDSL_Trigger15", self)
                    

    @property
    def robotDSL_Task(self):
        return self.__robotDSL_Task

    @robotDSL_Task.setter
    def robotDSL_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Task__robotDSL_Task", None)
        self.__robotDSL_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Mission4"):
                opp_val = getattr(old_value, "robotDSL_Mission4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Mission4"):
                opp_val = getattr(value, "robotDSL_Mission4", None)
                if opp_val is None:
                    setattr(value, "robotDSL_Mission4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class robotDSL_Flag:

    def __init__(self, name: str, robotDSL_Flag: "robotDSL_Mission" = None, robotDSL_Flag45: "robotDSL_Trigger" = None, robotDSL_Flag35: "robotDSL_Action" = None):
        self.name = name
        self.robotDSL_Flag = robotDSL_Flag
        self.robotDSL_Flag45 = robotDSL_Flag45
        self.robotDSL_Flag35 = robotDSL_Flag35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robotDSL_Flag35(self):
        return self.__robotDSL_Flag35

    @robotDSL_Flag35.setter
    def robotDSL_Flag35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Flag__robotDSL_Flag35", None)
        self.__robotDSL_Flag35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Action34"):
                opp_val = getattr(old_value, "robotDSL_Action34", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Action34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Action34"):
                opp_val = getattr(value, "robotDSL_Action34", None)
                setattr(value, "robotDSL_Action34", self)

    @property
    def robotDSL_Flag(self):
        return self.__robotDSL_Flag

    @robotDSL_Flag.setter
    def robotDSL_Flag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Flag__robotDSL_Flag", None)
        self.__robotDSL_Flag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Mission2"):
                opp_val = getattr(old_value, "robotDSL_Mission2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Mission2"):
                opp_val = getattr(value, "robotDSL_Mission2", None)
                if opp_val is None:
                    setattr(value, "robotDSL_Mission2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotDSL_Flag45(self):
        return self.__robotDSL_Flag45

    @robotDSL_Flag45.setter
    def robotDSL_Flag45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Flag__robotDSL_Flag45", None)
        self.__robotDSL_Flag45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Trigger44"):
                opp_val = getattr(old_value, "robotDSL_Trigger44", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Trigger44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Trigger44"):
                opp_val = getattr(value, "robotDSL_Trigger44", None)
                setattr(value, "robotDSL_Trigger44", self)

class robotDSL_Mission:

    def __init__(self, name: str, robotDSL_Mission: "robotDSL_Missions" = None, robotDSL_Mission2: set["robotDSL_Flag"] = None, robotDSL_Mission4: set["robotDSL_Task"] = None, robotDSL_Mission6: "robotDSL_Goal" = None):
        self.name = name
        self.robotDSL_Mission = robotDSL_Mission
        self.robotDSL_Mission2 = robotDSL_Mission2 if robotDSL_Mission2 is not None else set()
        self.robotDSL_Mission4 = robotDSL_Mission4 if robotDSL_Mission4 is not None else set()
        self.robotDSL_Mission6 = robotDSL_Mission6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def robotDSL_Mission6(self):
        return self.__robotDSL_Mission6

    @robotDSL_Mission6.setter
    def robotDSL_Mission6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Mission__robotDSL_Mission6", None)
        self.__robotDSL_Mission6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Goal"):
                opp_val = getattr(old_value, "robotDSL_Goal", None)
                if opp_val == self:
                    setattr(old_value, "robotDSL_Goal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Goal"):
                opp_val = getattr(value, "robotDSL_Goal", None)
                setattr(value, "robotDSL_Goal", self)

    @property
    def robotDSL_Mission(self):
        return self.__robotDSL_Mission

    @robotDSL_Mission.setter
    def robotDSL_Mission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Mission__robotDSL_Mission", None)
        self.__robotDSL_Mission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "robotDSL_Missions"):
                opp_val = getattr(old_value, "robotDSL_Missions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "robotDSL_Missions"):
                opp_val = getattr(value, "robotDSL_Missions", None)
                if opp_val is None:
                    setattr(value, "robotDSL_Missions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def robotDSL_Mission4(self):
        return self.__robotDSL_Mission4

    @robotDSL_Mission4.setter
    def robotDSL_Mission4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Mission__robotDSL_Mission4", None)
        self.__robotDSL_Mission4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotDSL_Task"):
                    opp_val = getattr(item, "robotDSL_Task", None)
                    
                    if opp_val == self:
                        setattr(item, "robotDSL_Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotDSL_Task"):
                    opp_val = getattr(item, "robotDSL_Task", None)
                    
                    setattr(item, "robotDSL_Task", self)
                    

    @property
    def robotDSL_Mission2(self):
        return self.__robotDSL_Mission2

    @robotDSL_Mission2.setter
    def robotDSL_Mission2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_robotDSL_Mission__robotDSL_Mission2", None)
        self.__robotDSL_Mission2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "robotDSL_Flag"):
                    opp_val = getattr(item, "robotDSL_Flag", None)
                    
                    if opp_val == self:
                        setattr(item, "robotDSL_Flag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "robotDSL_Flag"):
                    opp_val = getattr(item, "robotDSL_Flag", None)
                    
                    setattr(item, "robotDSL_Flag", self)
                    
