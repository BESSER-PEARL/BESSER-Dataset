from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AngleUnit(Enum):
    radians = "radians"
    degrees = "degrees"
class LengthUnit(Enum):
    millimeters = "millimeters"
    centimeters = "centimeters"
    meters = "meters"
class VelocityUnit(Enum):
    millimeters_per_second = "millimeters_per_second"
    centimeters_per_second = "centimeters_per_second"
class ColorKind(Enum):
    None = "None"
    Red = "Red"
    Green = "Green"
    Blue = "Blue"
    Yellow = "Yellow"
class TimeUnit(Enum):
    nanoseconds = "nanoseconds"
    milliseconds = "milliseconds"
    seconds = "seconds"
    minutes = "minutes"
    hours = "hours"
class Operator(Enum):
    smaller = "smaller"
    greater = "greater"
    equal = "equal"
    unequal = "unequal"


############################################
# Definition of Classes
############################################

class SingleQuantity:

    pass
class Quantity:

    pass
class rover_SingleQuantity(Quantity):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class rover_Velocity(SingleQuantity):

    def __init__(self, velocityUnit: str, rover_Velocity: "rover_Move" = None):
        self.velocityUnit = velocityUnit
        self.rover_Velocity = rover_Velocity
        
    @property
    def velocityUnit(self) -> str:
        return self.__velocityUnit

    @velocityUnit.setter
    def velocityUnit(self, velocityUnit: str):
        self.__velocityUnit = velocityUnit

    @property
    def rover_Velocity(self):
        return self.__rover_Velocity

    @rover_Velocity.setter
    def rover_Velocity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Velocity__rover_Velocity", None)
        self.__rover_Velocity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Move34"):
                opp_val = getattr(old_value, "rover_Move34", None)
                if opp_val == self:
                    setattr(old_value, "rover_Move34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Move34"):
                opp_val = getattr(value, "rover_Move34", None)
                setattr(value, "rover_Move34", self)

class TriggeredTransition:

    pass
class rover_GPSTrigger(TriggeredTransition):

    pass
class rover_CompassTrigger(TriggeredTransition):

    pass
class rover_DistanceSensorTrigger(TriggeredTransition):

    pass
class Transition:

    pass
class rover_NormalTransition(Transition):

    pass
class rover_TriggeredTransition(Transition):

    def __init__(self, Operator: str):
        self.Operator = Operator
        
    @property
    def Operator(self) -> str:
        return self.__Operator

    @Operator.setter
    def Operator(self, Operator: str):
        self.__Operator = Operator

class rover_Angle(SingleQuantity):

    def __init__(self, angleUnit: str, rover_Angle: "rover_Compass" = None, rover_Angle36: "rover_Rotate" = None, rover_Angle58: "rover_CompassTrigger" = None):
        self.angleUnit = angleUnit
        self.rover_Angle = rover_Angle
        self.rover_Angle36 = rover_Angle36
        self.rover_Angle58 = rover_Angle58
        
    @property
    def angleUnit(self) -> str:
        return self.__angleUnit

    @angleUnit.setter
    def angleUnit(self, angleUnit: str):
        self.__angleUnit = angleUnit

    @property
    def rover_Angle36(self):
        return self.__rover_Angle36

    @rover_Angle36.setter
    def rover_Angle36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Angle__rover_Angle36", None)
        self.__rover_Angle36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Rotate"):
                opp_val = getattr(old_value, "rover_Rotate", None)
                if opp_val == self:
                    setattr(old_value, "rover_Rotate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Rotate"):
                opp_val = getattr(value, "rover_Rotate", None)
                setattr(value, "rover_Rotate", self)

    @property
    def rover_Angle58(self):
        return self.__rover_Angle58

    @rover_Angle58.setter
    def rover_Angle58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Angle__rover_Angle58", None)
        self.__rover_Angle58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_CompassTrigger57"):
                opp_val = getattr(old_value, "rover_CompassTrigger57", None)
                if opp_val == self:
                    setattr(old_value, "rover_CompassTrigger57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_CompassTrigger57"):
                opp_val = getattr(value, "rover_CompassTrigger57", None)
                setattr(value, "rover_CompassTrigger57", self)

    @property
    def rover_Angle(self):
        return self.__rover_Angle

    @rover_Angle.setter
    def rover_Angle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Angle__rover_Angle", None)
        self.__rover_Angle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Compass"):
                opp_val = getattr(old_value, "rover_Compass", None)
                if opp_val == self:
                    setattr(old_value, "rover_Compass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Compass"):
                opp_val = getattr(value, "rover_Compass", None)
                setattr(value, "rover_Compass", self)

class rover_Time(SingleQuantity):

    def __init__(self, timeUnit: str, rover_Time: "rover_Wait" = None):
        self.timeUnit = timeUnit
        self.rover_Time = rover_Time
        
    @property
    def timeUnit(self) -> str:
        return self.__timeUnit

    @timeUnit.setter
    def timeUnit(self, timeUnit: str):
        self.__timeUnit = timeUnit

    @property
    def rover_Time(self):
        return self.__rover_Time

    @rover_Time.setter
    def rover_Time(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Time__rover_Time", None)
        self.__rover_Time = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Wait"):
                opp_val = getattr(old_value, "rover_Wait", None)
                if opp_val == self:
                    setattr(old_value, "rover_Wait", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Wait"):
                opp_val = getattr(value, "rover_Wait", None)
                setattr(value, "rover_Wait", self)

class Command:

    pass
class rover_Terminate(Command):

    pass
class rover_Rotate(Command):

    pass
class rover_Wait(Command):

    pass
class rover_Move(Command):

    pass
class rover_SetLightColor(Command):

    def __init__(self, lightColor: str, rover_SetLightColor: "rover_Light" = None, rover_SetLightColor39: "rover_Repeat" = None):
        self.lightColor = lightColor
        self.rover_SetLightColor = rover_SetLightColor
        self.rover_SetLightColor39 = rover_SetLightColor39
        
    @property
    def lightColor(self) -> str:
        return self.__lightColor

    @lightColor.setter
    def lightColor(self, lightColor: str):
        self.__lightColor = lightColor

    @property
    def rover_SetLightColor(self):
        return self.__rover_SetLightColor

    @rover_SetLightColor.setter
    def rover_SetLightColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_SetLightColor__rover_SetLightColor", None)
        self.__rover_SetLightColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Light"):
                opp_val = getattr(old_value, "rover_Light", None)
                if opp_val == self:
                    setattr(old_value, "rover_Light", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Light"):
                opp_val = getattr(value, "rover_Light", None)
                setattr(value, "rover_Light", self)

    @property
    def rover_SetLightColor39(self):
        return self.__rover_SetLightColor39

    @rover_SetLightColor39.setter
    def rover_SetLightColor39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_SetLightColor__rover_SetLightColor39", None)
        self.__rover_SetLightColor39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Repeat38"):
                opp_val = getattr(old_value, "rover_Repeat38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Repeat38"):
                opp_val = getattr(value, "rover_Repeat38", None)
                if opp_val is None:
                    setattr(value, "rover_Repeat38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rover_Repeat(Command):

    def __init__(self, count: int, rover_Repeat: "rover_Block" = None, rover_Repeat38: set["rover_SetLightColor"] = None, rover_Repeat41: set["rover_Wait"] = None, rover_Repeat44: set["rover_Move"] = None, rover_Repeat47: set["rover_Rotate"] = None):
        self.count = count
        self.rover_Repeat = rover_Repeat
        self.rover_Repeat38 = rover_Repeat38 if rover_Repeat38 is not None else set()
        self.rover_Repeat41 = rover_Repeat41 if rover_Repeat41 is not None else set()
        self.rover_Repeat44 = rover_Repeat44 if rover_Repeat44 is not None else set()
        self.rover_Repeat47 = rover_Repeat47 if rover_Repeat47 is not None else set()
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def rover_Repeat41(self):
        return self.__rover_Repeat41

    @rover_Repeat41.setter
    def rover_Repeat41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Repeat__rover_Repeat41", None)
        self.__rover_Repeat41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rover_Wait42"):
                    opp_val = getattr(item, "rover_Wait42", None)
                    
                    if opp_val == self:
                        setattr(item, "rover_Wait42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rover_Wait42"):
                    opp_val = getattr(item, "rover_Wait42", None)
                    
                    setattr(item, "rover_Wait42", self)
                    

    @property
    def rover_Repeat44(self):
        return self.__rover_Repeat44

    @rover_Repeat44.setter
    def rover_Repeat44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Repeat__rover_Repeat44", None)
        self.__rover_Repeat44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rover_Move45"):
                    opp_val = getattr(item, "rover_Move45", None)
                    
                    if opp_val == self:
                        setattr(item, "rover_Move45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rover_Move45"):
                    opp_val = getattr(item, "rover_Move45", None)
                    
                    setattr(item, "rover_Move45", self)
                    

    @property
    def rover_Repeat47(self):
        return self.__rover_Repeat47

    @rover_Repeat47.setter
    def rover_Repeat47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Repeat__rover_Repeat47", None)
        self.__rover_Repeat47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rover_Rotate48"):
                    opp_val = getattr(item, "rover_Rotate48", None)
                    
                    if opp_val == self:
                        setattr(item, "rover_Rotate48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rover_Rotate48"):
                    opp_val = getattr(item, "rover_Rotate48", None)
                    
                    setattr(item, "rover_Rotate48", self)
                    

    @property
    def rover_Repeat(self):
        return self.__rover_Repeat

    @rover_Repeat.setter
    def rover_Repeat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Repeat__rover_Repeat", None)
        self.__rover_Repeat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Block20"):
                opp_val = getattr(old_value, "rover_Block20", None)
                if opp_val == self:
                    setattr(old_value, "rover_Block20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Block20"):
                opp_val = getattr(value, "rover_Block20", None)
                setattr(value, "rover_Block20", self)

    @property
    def rover_Repeat38(self):
        return self.__rover_Repeat38

    @rover_Repeat38.setter
    def rover_Repeat38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Repeat__rover_Repeat38", None)
        self.__rover_Repeat38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rover_SetLightColor39"):
                    opp_val = getattr(item, "rover_SetLightColor39", None)
                    
                    if opp_val == self:
                        setattr(item, "rover_SetLightColor39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rover_SetLightColor39"):
                    opp_val = getattr(item, "rover_SetLightColor39", None)
                    
                    setattr(item, "rover_SetLightColor39", self)
                    

class rover_Transition(ABC):

    pass
class rover_Command(ABC):

    pass
class rover_Length(SingleQuantity):

    def __init__(self, lengthUnit: str, rover_Length: "rover_Distance" = None, rover_Length53: "rover_DistanceSensorTrigger" = None, rover_Length32: "rover_Move" = None, rover_Length66: "rover_Position" = None, rover_Length69: "rover_Position" = None):
        self.lengthUnit = lengthUnit
        self.rover_Length = rover_Length
        self.rover_Length53 = rover_Length53
        self.rover_Length32 = rover_Length32
        self.rover_Length66 = rover_Length66
        self.rover_Length69 = rover_Length69
        
    @property
    def lengthUnit(self) -> str:
        return self.__lengthUnit

    @lengthUnit.setter
    def lengthUnit(self, lengthUnit: str):
        self.__lengthUnit = lengthUnit

    @property
    def rover_Length32(self):
        return self.__rover_Length32

    @rover_Length32.setter
    def rover_Length32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Length__rover_Length32", None)
        self.__rover_Length32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Move31"):
                opp_val = getattr(old_value, "rover_Move31", None)
                if opp_val == self:
                    setattr(old_value, "rover_Move31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Move31"):
                opp_val = getattr(value, "rover_Move31", None)
                setattr(value, "rover_Move31", self)

    @property
    def rover_Length69(self):
        return self.__rover_Length69

    @rover_Length69.setter
    def rover_Length69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Length__rover_Length69", None)
        self.__rover_Length69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Position68"):
                opp_val = getattr(old_value, "rover_Position68", None)
                if opp_val == self:
                    setattr(old_value, "rover_Position68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Position68"):
                opp_val = getattr(value, "rover_Position68", None)
                setattr(value, "rover_Position68", self)

    @property
    def rover_Length53(self):
        return self.__rover_Length53

    @rover_Length53.setter
    def rover_Length53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Length__rover_Length53", None)
        self.__rover_Length53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_DistanceSensorTrigger52"):
                opp_val = getattr(old_value, "rover_DistanceSensorTrigger52", None)
                if opp_val == self:
                    setattr(old_value, "rover_DistanceSensorTrigger52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_DistanceSensorTrigger52"):
                opp_val = getattr(value, "rover_DistanceSensorTrigger52", None)
                setattr(value, "rover_DistanceSensorTrigger52", self)

    @property
    def rover_Length66(self):
        return self.__rover_Length66

    @rover_Length66.setter
    def rover_Length66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Length__rover_Length66", None)
        self.__rover_Length66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Position65"):
                opp_val = getattr(old_value, "rover_Position65", None)
                if opp_val == self:
                    setattr(old_value, "rover_Position65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Position65"):
                opp_val = getattr(value, "rover_Position65", None)
                setattr(value, "rover_Position65", self)

    @property
    def rover_Length(self):
        return self.__rover_Length

    @rover_Length.setter
    def rover_Length(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Length__rover_Length", None)
        self.__rover_Length = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Distance"):
                opp_val = getattr(old_value, "rover_Distance", None)
                if opp_val == self:
                    setattr(old_value, "rover_Distance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Distance"):
                opp_val = getattr(value, "rover_Distance", None)
                setattr(value, "rover_Distance", self)

class rover_Position(Quantity):

    pass
class Sensor:

    pass
class rover_Compass(Sensor):

    pass
class rover_Distance(Sensor):

    pass
class rover_GPS(Sensor):

    pass
class Actuator:

    pass
class rover_Light(Actuator):

    def __init__(self, color: str, rover_Light: "rover_SetLightColor" = None):
        self.color = color
        self.rover_Light = rover_Light
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def rover_Light(self):
        return self.__rover_Light

    @rover_Light.setter
    def rover_Light(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Light__rover_Light", None)
        self.__rover_Light = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_SetLightColor"):
                opp_val = getattr(old_value, "rover_SetLightColor", None)
                if opp_val == self:
                    setattr(old_value, "rover_SetLightColor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_SetLightColor"):
                opp_val = getattr(value, "rover_SetLightColor", None)
                setattr(value, "rover_SetLightColor", self)

class rover_Motor(Actuator):

    pass
class Component:

    pass
class rover_Sensor(Component):

    pass
class rover_Actuator(Component):

    pass
class rover_Quantity(ABC):

    pass
class rover_Block:

    pass
class rover_Component(ABC):

    def __init__(self, name: str, rover_Component: "rover_Rover" = None):
        self.name = name
        self.rover_Component = rover_Component
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rover_Component(self):
        return self.__rover_Component

    @rover_Component.setter
    def rover_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Component__rover_Component", None)
        self.__rover_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Rover4"):
                opp_val = getattr(old_value, "rover_Rover4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Rover4"):
                opp_val = getattr(value, "rover_Rover4", None)
                if opp_val is None:
                    setattr(value, "rover_Rover4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rover_Program:

    def __init__(self, name: str, rover_Program: "rover_System" = None, rover_Program6: "rover_Rover" = None, rover_Program9: "rover_Block" = None, rover_Program11: set["rover_Quantity"] = None):
        self.name = name
        self.rover_Program = rover_Program
        self.rover_Program6 = rover_Program6
        self.rover_Program9 = rover_Program9
        self.rover_Program11 = rover_Program11 if rover_Program11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rover_Program6(self):
        return self.__rover_Program6

    @rover_Program6.setter
    def rover_Program6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Program__rover_Program6", None)
        self.__rover_Program6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Rover7"):
                opp_val = getattr(old_value, "rover_Rover7", None)
                if opp_val == self:
                    setattr(old_value, "rover_Rover7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Rover7"):
                opp_val = getattr(value, "rover_Rover7", None)
                setattr(value, "rover_Rover7", self)

    @property
    def rover_Program(self):
        return self.__rover_Program

    @rover_Program.setter
    def rover_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Program__rover_Program", None)
        self.__rover_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_System2"):
                opp_val = getattr(old_value, "rover_System2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_System2"):
                opp_val = getattr(value, "rover_System2", None)
                if opp_val is None:
                    setattr(value, "rover_System2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rover_Program9(self):
        return self.__rover_Program9

    @rover_Program9.setter
    def rover_Program9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Program__rover_Program9", None)
        self.__rover_Program9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Block"):
                opp_val = getattr(old_value, "rover_Block", None)
                if opp_val == self:
                    setattr(old_value, "rover_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Block"):
                opp_val = getattr(value, "rover_Block", None)
                setattr(value, "rover_Block", self)

    @property
    def rover_Program11(self):
        return self.__rover_Program11

    @rover_Program11.setter
    def rover_Program11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Program__rover_Program11", None)
        self.__rover_Program11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rover_Quantity"):
                    opp_val = getattr(item, "rover_Quantity", None)
                    
                    if opp_val == self:
                        setattr(item, "rover_Quantity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rover_Quantity"):
                    opp_val = getattr(item, "rover_Quantity", None)
                    
                    setattr(item, "rover_Quantity", self)
                    

class rover_Rover:

    def __init__(self, name: str, rover_Rover: "rover_System" = None, rover_Rover4: set["rover_Component"] = None, rover_Rover7: "rover_Program" = None):
        self.name = name
        self.rover_Rover = rover_Rover
        self.rover_Rover4 = rover_Rover4 if rover_Rover4 is not None else set()
        self.rover_Rover7 = rover_Rover7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rover_Rover(self):
        return self.__rover_Rover

    @rover_Rover.setter
    def rover_Rover(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Rover__rover_Rover", None)
        self.__rover_Rover = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_System"):
                opp_val = getattr(old_value, "rover_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_System"):
                opp_val = getattr(value, "rover_System", None)
                if opp_val is None:
                    setattr(value, "rover_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rover_Rover4(self):
        return self.__rover_Rover4

    @rover_Rover4.setter
    def rover_Rover4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Rover__rover_Rover4", None)
        self.__rover_Rover4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rover_Component"):
                    opp_val = getattr(item, "rover_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "rover_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rover_Component"):
                    opp_val = getattr(item, "rover_Component", None)
                    
                    setattr(item, "rover_Component", self)
                    

    @property
    def rover_Rover7(self):
        return self.__rover_Rover7

    @rover_Rover7.setter
    def rover_Rover7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rover_Rover__rover_Rover7", None)
        self.__rover_Rover7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rover_Program6"):
                opp_val = getattr(old_value, "rover_Program6", None)
                if opp_val == self:
                    setattr(old_value, "rover_Program6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rover_Program6"):
                opp_val = getattr(value, "rover_Program6", None)
                setattr(value, "rover_Program6", self)

class rover_System:

    pass