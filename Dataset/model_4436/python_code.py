from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ComparisonOperator(Enum):
    smaller = "smaller"
    equals = "equals"
    greater = "greater"
    unequal = "unequal"
class Color(Enum):
    none = "none"
    red = "red"
    green = "green"
    blue = "blue"
    yellow = "yellow"
class TimeUnit(Enum):
    ns = "ns"
    ms = "ms"
    s = "s"
    min = "min"
    h = "h"
class AngleUnit(Enum):
    radian = "radian"
    degree = "degree"
class LengthUnit(Enum):
    mm = "mm"
    cm = "cm"
    m = "m"
class VelocityUnit(Enum):
    mm_per_s = "mm_per_s"
    cm_per_s = "cm_per_s"


############################################
# Definition of Classes
############################################

class roverml_GpsTrigger:

    pass
class roverml_DistanceSensorTrigger:

    pass
class roverml_RoverSystem:

    pass
class roverml_Quantity(ABC):

    pass
class roverml_CompassTrigger:

    pass
class SingleQuantity:

    pass
class Quantity:

    pass
class roverml_Position(Quantity):

    pass
class roverml_SingleQuantity(Quantity):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class Component:

    pass
class roverml_Actuator(Component):

    pass
class roverml_Sensor(Component):

    pass
class Actuator:

    pass
class roverml_Motor(Actuator):

    pass
class roverml_Compass:

    pass
class roverml_DistanceSensor:

    pass
class roverml_GPS:

    pass
class Transition:

    pass
class roverml_TriggeredTransition(Transition):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class roverml_Block:

    pass
class NamedElement:

    pass
class roverml_Component(NamedElement):

    def __init__(self, kind: str, roverml_Component: "roverml_Rover" = None):
        self.kind = kind
        self.roverml_Component = roverml_Component
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def roverml_Component(self):
        return self.__roverml_Component

    @roverml_Component.setter
    def roverml_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Component__roverml_Component", None)
        self.__roverml_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Rover14"):
                opp_val = getattr(old_value, "roverml_Rover14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Rover14"):
                opp_val = getattr(value, "roverml_Rover14", None)
                if opp_val is None:
                    setattr(value, "roverml_Rover14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class roverml_Rover(NamedElement):

    pass
class roverml_Transition(NamedElement):

    pass
class roverml_Command(NamedElement):

    pass
class roverml_RoverProgram(NamedElement):

    pass
class Block:

    pass
class roverml_Time(SingleQuantity):

    def __init__(self, timeUnit: str, roverml_Time: "roverml_Wait" = None):
        self.timeUnit = timeUnit
        self.roverml_Time = roverml_Time
        
    @property
    def timeUnit(self) -> str:
        return self.__timeUnit

    @timeUnit.setter
    def timeUnit(self, timeUnit: str):
        self.__timeUnit = timeUnit

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

class roverml_Angle(SingleQuantity):

    def __init__(self, angleUnit: str, roverml_Angle: "roverml_Rotate" = None):
        self.angleUnit = angleUnit
        self.roverml_Angle = roverml_Angle
        
    @property
    def angleUnit(self) -> str:
        return self.__angleUnit

    @angleUnit.setter
    def angleUnit(self, angleUnit: str):
        self.__angleUnit = angleUnit

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

class roverml_Light(Actuator):

    pass
class roverml_Length(SingleQuantity):

    def __init__(self, lengthUnit: str, roverml_Length: "roverml_Move" = None, roverml_Length33: "roverml_Position" = None, roverml_Length36: "roverml_Position" = None):
        self.lengthUnit = lengthUnit
        self.roverml_Length = roverml_Length
        self.roverml_Length33 = roverml_Length33
        self.roverml_Length36 = roverml_Length36
        
    @property
    def lengthUnit(self) -> str:
        return self.__lengthUnit

    @lengthUnit.setter
    def lengthUnit(self, lengthUnit: str):
        self.__lengthUnit = lengthUnit

    @property
    def roverml_Length33(self):
        return self.__roverml_Length33

    @roverml_Length33.setter
    def roverml_Length33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Length__roverml_Length33", None)
        self.__roverml_Length33 = value
        
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
    def roverml_Length36(self):
        return self.__roverml_Length36

    @roverml_Length36.setter
    def roverml_Length36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_Length__roverml_Length36", None)
        self.__roverml_Length36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roverml_Position35"):
                opp_val = getattr(old_value, "roverml_Position35", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Position35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Position35"):
                opp_val = getattr(value, "roverml_Position35", None)
                setattr(value, "roverml_Position35", self)

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
            if hasattr(old_value, "roverml_Move9"):
                opp_val = getattr(old_value, "roverml_Move9", None)
                if opp_val == self:
                    setattr(old_value, "roverml_Move9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roverml_Move9"):
                opp_val = getattr(value, "roverml_Move9", None)
                setattr(value, "roverml_Move9", self)

class roverml_Velocity(SingleQuantity):

    def __init__(self, velocityUnit: str, roverml_Velocity: "roverml_Move" = None):
        self.velocityUnit = velocityUnit
        self.roverml_Velocity = roverml_Velocity
        
    @property
    def velocityUnit(self) -> str:
        return self.__velocityUnit

    @velocityUnit.setter
    def velocityUnit(self, velocityUnit: str):
        self.__velocityUnit = velocityUnit

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

class Command:

    pass
class roverml_Terminate(Command):

    pass
class roverml_Rotate(Command):

    pass
class roverml_Repeat(Block, Command):

    def __init__(self, count: int):
        self.count = count
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

class roverml_Wait(Command):

    pass
class roverml_SetLightColor(Command):

    def __init__(self, color: str, roverml_SetLightColor: set["roverml_Light"] = None):
        self.color = color
        self.roverml_SetLightColor = roverml_SetLightColor if roverml_SetLightColor is not None else set()
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def roverml_SetLightColor(self):
        return self.__roverml_SetLightColor

    @roverml_SetLightColor.setter
    def roverml_SetLightColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_roverml_SetLightColor__roverml_SetLightColor", None)
        self.__roverml_SetLightColor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "roverml_Light"):
                    opp_val = getattr(item, "roverml_Light", None)
                    
                    if opp_val == self:
                        setattr(item, "roverml_Light", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "roverml_Light"):
                    opp_val = getattr(item, "roverml_Light", None)
                    
                    setattr(item, "roverml_Light", self)
                    

class roverml_Move(Command):

    pass
class roverml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
