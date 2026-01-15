from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Colours(Enum):
    NONE = "NONE"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    YELLOW = "YELLOW"
class TimeUnits(Enum):
    NANOSECONDS = "NANOSECONDS"
    MILLISECONDS = "MILLISECONDS"
    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
class VelocityUnits(Enum):
    MILLIMETERS_PER_SECOND = "MILLIMETERS_PER_SECOND"
    CENTIMETERS_PER_SECOND = "CENTIMETERS_PER_SECOND"
class LengthUnits(Enum):
    MILLIMETERS = "MILLIMETERS"
    CENTIMETERS = "CENTIMETERS"
    METERS = "METERS"
class AngleUnits(Enum):
    RADIANS = "RADIANS"
    DEGREES = "DEGREES"


############################################
# Definition of Classes
############################################

class SingleQuantity:

    pass
class Quantity:

    pass
class roverml_SingleQuantity(Quantity):

    pass
class roverml_Quantity:

    pass
class Triggered:

    pass
class roverml_CompassTrigger(Triggered):

    def __init__(self, angle: int, roverml_CompassTrigger37: "roverml_Compass" = None, roverml_CompassTrigger: "roverml_Angle" = None):
        self.angle = angle
        self.roverml_CompassTrigger37 = roverml_CompassTrigger37
        self.roverml_CompassTrigger = roverml_CompassTrigger
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

    @property
    def roverml_CompassTrigger(self):
        return self.__roverml_CompassTrigger

    @roverml_CompassTrigger.setter
    def roverml_CompassTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_CompassTrigger__roverml_CompassTrigger", None)
        self.__roverml_CompassTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Angle35"):
                opp_val = getattr(old_value, "roverml_Angle35", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Angle35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Angle35"):
                opp_val = getattr(value, "roverml_Angle35", None)
                setattr(value, "roverml_Angle35", self)

    @property
    def roverml_CompassTrigger37(self):
        return self.__roverml_CompassTrigger37

    @roverml_CompassTrigger37.setter
    def roverml_CompassTrigger37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_CompassTrigger__roverml_CompassTrigger37", None)
        self.__roverml_CompassTrigger37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Compass"):
                opp_val = getattr(old_value, "roverml_Compass", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Compass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Compass"):
                opp_val = getattr(value, "roverml_Compass", None)
                setattr(value, "roverml_Compass", self)

class roverml_DistanceSensorTrigger(Triggered):

    def __init__(self, dist: float, roverml_DistanceSensorTrigger: "roverml_Length" = None, roverml_DistanceSensorTrigger33: "roverml_DistanceSensor" = None):
        self.dist = dist
        self.roverml_DistanceSensorTrigger = roverml_DistanceSensorTrigger
        self.roverml_DistanceSensorTrigger33 = roverml_DistanceSensorTrigger33
        
    @property
    def dist(self) -> float:
        return self.__dist

    @dist.setter
    def dist(self, dist: float):
        self.__dist = dist

    @property
    def roverml_DistanceSensorTrigger33(self):
        return self.__roverml_DistanceSensorTrigger33

    @roverml_DistanceSensorTrigger33.setter
    def roverml_DistanceSensorTrigger33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_DistanceSensorTrigger__roverml_DistanceSensorTrigger33", None)
        self.__roverml_DistanceSensorTrigger33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_DistanceSensor"):
                opp_val = getattr(old_value, "roverml_DistanceSensor", None)
                if opp_val == self:
                    setattr(old_value, "roverml_DistanceSensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_DistanceSensor"):
                opp_val = getattr(value, "roverml_DistanceSensor", None)
                setattr(value, "roverml_DistanceSensor", self)

    @property
    def roverml_DistanceSensorTrigger(self):
        return self.__roverml_DistanceSensorTrigger

    @roverml_DistanceSensorTrigger.setter
    def roverml_DistanceSensorTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_DistanceSensorTrigger__roverml_DistanceSensorTrigger", None)
        self.__roverml_DistanceSensorTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Length31"):
                opp_val = getattr(old_value, "roverml_Length31", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Length31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Length31"):
                opp_val = getattr(value, "roverml_Length31", None)
                setattr(value, "roverml_Length31", self)

class Transition:

    pass
class roverml_Regular(Transition):

    pass
class roverml_Triggered(Transition):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class roverml_Angle(SingleQuantity):

    def __init__(self, units: str, roverml_Angle: "roverml_Rotate" = None, roverml_Angle35: "roverml_CompassTrigger" = None):
        self.units = units
        self.roverml_Angle = roverml_Angle
        self.roverml_Angle35 = roverml_Angle35
        
    @property
    def units(self) -> str:
        return self.__units

    @units.setter
    def units(self, units: str):
        self.__units = units

    @property
    def roverml_Angle(self):
        return self.__roverml_Angle

    @roverml_Angle.setter
    def roverml_Angle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Angle__roverml_Angle", None)
        self.__roverml_Angle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Rotate"):
                opp_val = getattr(old_value, "roverml_Rotate", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Rotate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Rotate"):
                opp_val = getattr(value, "roverml_Rotate", None)
                setattr(value, "roverml_Rotate", self)

    @property
    def roverml_Angle35(self):
        return self.__roverml_Angle35

    @roverml_Angle35.setter
    def roverml_Angle35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Angle__roverml_Angle35", None)
        self.__roverml_Angle35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_CompassTrigger"):
                opp_val = getattr(old_value, "roverml_CompassTrigger", None)
                if opp_val == self:
                    setattr(old_value, "roverml_CompassTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_CompassTrigger"):
                opp_val = getattr(value, "roverml_CompassTrigger", None)
                setattr(value, "roverml_CompassTrigger", self)

class roverml_Length(SingleQuantity):

    def __init__(self, units: str, roverml_Length: "roverml_Move" = None, roverml_Length31: "roverml_DistanceSensorTrigger" = None):
        self.units = units
        self.roverml_Length = roverml_Length
        self.roverml_Length31 = roverml_Length31
        
    @property
    def units(self) -> str:
        return self.__units

    @units.setter
    def units(self, units: str):
        self.__units = units

    @property
    def roverml_Length31(self):
        return self.__roverml_Length31

    @roverml_Length31.setter
    def roverml_Length31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Length__roverml_Length31", None)
        self.__roverml_Length31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_DistanceSensorTrigger"):
                opp_val = getattr(old_value, "roverml_DistanceSensorTrigger", None)
                if opp_val == self:
                    setattr(old_value, "roverml_DistanceSensorTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_DistanceSensorTrigger"):
                opp_val = getattr(value, "roverml_DistanceSensorTrigger", None)
                setattr(value, "roverml_DistanceSensorTrigger", self)

    @property
    def roverml_Length(self):
        return self.__roverml_Length

    @roverml_Length.setter
    def roverml_Length(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Length__roverml_Length", None)
        self.__roverml_Length = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Move26"):
                opp_val = getattr(old_value, "roverml_Move26", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Move26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Move26"):
                opp_val = getattr(value, "roverml_Move26", None)
                setattr(value, "roverml_Move26", self)

class roverml_Velocity(SingleQuantity):

    def __init__(self, units: str, roverml_Velocity: "roverml_Move" = None):
        self.units = units
        self.roverml_Velocity = roverml_Velocity
        
    @property
    def units(self) -> str:
        return self.__units

    @units.setter
    def units(self, units: str):
        self.__units = units

    @property
    def roverml_Velocity(self):
        return self.__roverml_Velocity

    @roverml_Velocity.setter
    def roverml_Velocity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Velocity__roverml_Velocity", None)
        self.__roverml_Velocity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Move"):
                opp_val = getattr(old_value, "roverml_Move", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Move", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Move"):
                opp_val = getattr(value, "roverml_Move", None)
                setattr(value, "roverml_Move", self)

class roverml_Position(Quantity):

    def __init__(self, x: float, y: float, roverml_Position: "roverml_GPSTrigger" = None):
        self.x = x
        self.y = y
        self.roverml_Position = roverml_Position
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def roverml_Position(self):
        return self.__roverml_Position

    @roverml_Position.setter
    def roverml_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Position__roverml_Position", None)
        self.__roverml_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_GPSTrigger"):
                opp_val = getattr(old_value, "roverml_GPSTrigger", None)
                if opp_val == self:
                    setattr(old_value, "roverml_GPSTrigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_GPSTrigger"):
                opp_val = getattr(value, "roverml_GPSTrigger", None)
                setattr(value, "roverml_GPSTrigger", self)

class roverml_GPSTrigger(Triggered):

    def __init__(self, x: float, y: float, roverml_GPSTrigger: "roverml_Position" = None, roverml_GPSTrigger40: "roverml_GPS" = None):
        self.x = x
        self.y = y
        self.roverml_GPSTrigger = roverml_GPSTrigger
        self.roverml_GPSTrigger40 = roverml_GPSTrigger40
        
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def roverml_GPSTrigger(self):
        return self.__roverml_GPSTrigger

    @roverml_GPSTrigger.setter
    def roverml_GPSTrigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_GPSTrigger__roverml_GPSTrigger", None)
        self.__roverml_GPSTrigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Position"):
                opp_val = getattr(old_value, "roverml_Position", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Position"):
                opp_val = getattr(value, "roverml_Position", None)
                setattr(value, "roverml_Position", self)

    @property
    def roverml_GPSTrigger40(self):
        return self.__roverml_GPSTrigger40

    @roverml_GPSTrigger40.setter
    def roverml_GPSTrigger40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_GPSTrigger__roverml_GPSTrigger40", None)
        self.__roverml_GPSTrigger40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_GPS"):
                opp_val = getattr(old_value, "roverml_GPS", None)
                if opp_val == self:
                    setattr(old_value, "roverml_GPS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_GPS"):
                opp_val = getattr(value, "roverml_GPS", None)
                setattr(value, "roverml_GPS", self)

class Command:

    pass
class roverml_Wait(Command):

    def __init__(self, time: int, roverml_Wait: "roverml_Time" = None):
        self.time = time
        self.roverml_Wait = roverml_Wait
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def roverml_Wait(self):
        return self.__roverml_Wait

    @roverml_Wait.setter
    def roverml_Wait(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Wait__roverml_Wait", None)
        self.__roverml_Wait = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Time"):
                opp_val = getattr(old_value, "roverml_Time", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Time", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Time"):
                opp_val = getattr(value, "roverml_Time", None)
                setattr(value, "roverml_Time", self)

class roverml_Rotate(Command):

    def __init__(self, angle: int, roverml_Rotate: "roverml_Angle" = None):
        self.angle = angle
        self.roverml_Rotate = roverml_Rotate
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

    @property
    def roverml_Rotate(self):
        return self.__roverml_Rotate

    @roverml_Rotate.setter
    def roverml_Rotate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Rotate__roverml_Rotate", None)
        self.__roverml_Rotate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Angle"):
                opp_val = getattr(old_value, "roverml_Angle", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Angle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Angle"):
                opp_val = getattr(value, "roverml_Angle", None)
                setattr(value, "roverml_Angle", self)

class roverml_Terminate(Command):

    pass
class roverml_Repeat(Command):

    def __init__(self, numberOfReps: int, roverml_Repeat: set["roverml_Command"] = None):
        self.numberOfReps = numberOfReps
        self.roverml_Repeat = roverml_Repeat if roverml_Repeat is not None else set()
        
    @property
    def numberOfReps(self) -> int:
        return self.__numberOfReps

    @numberOfReps.setter
    def numberOfReps(self, numberOfReps: int):
        self.__numberOfReps = numberOfReps

    @property
    def roverml_Repeat(self):
        return self.__roverml_Repeat

    @roverml_Repeat.setter
    def roverml_Repeat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Repeat__roverml_Repeat", None)
        self.__roverml_Repeat = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "roverml_Command29"):
                    opp_val = getattr(item, "roverml_Command29", None)
                    
                    if opp_val == self:
                        setattr(item, "roverml_Command29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "roverml_Command29"):
                    opp_val = getattr(item, "roverml_Command29", None)
                    
                    setattr(item, "roverml_Command29", self)
                    

class roverml_SetLightColor(Command):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class roverml_Command:

    pass
class roverml_Transition:

    pass
class Actuator:

    pass
class roverml_Light(Actuator):

    pass
class roverml_Motor(Actuator):

    pass
class roverml_Move(Command):

    def __init__(self, length: float, velocity: float, roverml_Move: "roverml_Velocity" = None, roverml_Move26: "roverml_Length" = None):
        self.length = length
        self.velocity = velocity
        self.roverml_Move = roverml_Move
        self.roverml_Move26 = roverml_Move26
        
    @property
    def velocity(self) -> float:
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: float):
        self.__velocity = velocity

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length

    @property
    def roverml_Move26(self):
        return self.__roverml_Move26

    @roverml_Move26.setter
    def roverml_Move26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Move__roverml_Move26", None)
        self.__roverml_Move26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Length"):
                opp_val = getattr(old_value, "roverml_Length", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Length", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Length"):
                opp_val = getattr(value, "roverml_Length", None)
                setattr(value, "roverml_Length", self)

    @property
    def roverml_Move(self):
        return self.__roverml_Move

    @roverml_Move.setter
    def roverml_Move(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Move__roverml_Move", None)
        self.__roverml_Move = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Velocity"):
                opp_val = getattr(old_value, "roverml_Velocity", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Velocity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Velocity"):
                opp_val = getattr(value, "roverml_Velocity", None)
                setattr(value, "roverml_Velocity", self)

class roverml_Time(SingleQuantity):

    def __init__(self, units: str, roverml_Time: "roverml_Wait" = None):
        self.units = units
        self.roverml_Time = roverml_Time
        
    @property
    def units(self) -> str:
        return self.__units

    @units.setter
    def units(self, units: str):
        self.__units = units

    @property
    def roverml_Time(self):
        return self.__roverml_Time

    @roverml_Time.setter
    def roverml_Time(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Time__roverml_Time", None)
        self.__roverml_Time = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Wait"):
                opp_val = getattr(old_value, "roverml_Wait", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Wait", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Wait"):
                opp_val = getattr(value, "roverml_Wait", None)
                setattr(value, "roverml_Wait", self)

class roverml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class roverml_Block:

    pass
class Sensor:

    pass
class roverml_DistanceSensor(Sensor):

    def __init__(self, distance: float, roverml_DistanceSensor: "roverml_DistanceSensorTrigger" = None):
        self.distance = distance
        self.roverml_DistanceSensor = roverml_DistanceSensor
        
    @property
    def distance(self) -> float:
        return self.__distance

    @distance.setter
    def distance(self, distance: float):
        self.__distance = distance

    @property
    def roverml_DistanceSensor(self):
        return self.__roverml_DistanceSensor

    @roverml_DistanceSensor.setter
    def roverml_DistanceSensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_DistanceSensor__roverml_DistanceSensor", None)
        self.__roverml_DistanceSensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_DistanceSensorTrigger33"):
                opp_val = getattr(old_value, "roverml_DistanceSensorTrigger33", None)
                if opp_val == self:
                    setattr(old_value, "roverml_DistanceSensorTrigger33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_DistanceSensorTrigger33"):
                opp_val = getattr(value, "roverml_DistanceSensorTrigger33", None)
                setattr(value, "roverml_DistanceSensorTrigger33", self)

class roverml_Compass(Sensor):

    def __init__(self, angle: int, roverml_Compass: "roverml_CompassTrigger" = None):
        self.angle = angle
        self.roverml_Compass = roverml_Compass
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

    @property
    def roverml_Compass(self):
        return self.__roverml_Compass

    @roverml_Compass.setter
    def roverml_Compass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Compass__roverml_Compass", None)
        self.__roverml_Compass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_CompassTrigger37"):
                opp_val = getattr(old_value, "roverml_CompassTrigger37", None)
                if opp_val == self:
                    setattr(old_value, "roverml_CompassTrigger37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_CompassTrigger37"):
                opp_val = getattr(value, "roverml_CompassTrigger37", None)
                setattr(value, "roverml_CompassTrigger37", self)

class roverml_GPS(Sensor):

    def __init__(self, x: float, y: float, roverml_GPS: "roverml_GPSTrigger" = None):
        self.x = x
        self.y = y
        self.roverml_GPS = roverml_GPS
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def roverml_GPS(self):
        return self.__roverml_GPS

    @roverml_GPS.setter
    def roverml_GPS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_GPS__roverml_GPS", None)
        self.__roverml_GPS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_GPSTrigger40"):
                opp_val = getattr(old_value, "roverml_GPSTrigger40", None)
                if opp_val == self:
                    setattr(old_value, "roverml_GPSTrigger40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_GPSTrigger40"):
                opp_val = getattr(value, "roverml_GPSTrigger40", None)
                setattr(value, "roverml_GPSTrigger40", self)

class Component:

    pass
class roverml_Actuator(Component):

    pass
class roverml_Sensor(Component):

    pass
class NamedElement:

    pass
class roverml_Rover(NamedElement):

    pass
class roverml_Program(NamedElement):

    pass
class roverml_Component(NamedElement):

    pass
class roverml_System(NamedElement):

    pass