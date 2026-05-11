from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActionKind(Enum):
    SET = "SET"
    ADD = "ADD"
    SUBTRACT = "SUBTRACT"


############################################
# Definition of Classes
############################################

class drones_SizedElement(ABC):

    def __init__(self, length: float, height: float, width: float, x: float, y: float, z: float):
        self.length = length
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.z = z
        
        pass
    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, z: float):
        self.__z = z


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height


class FieldObject:

    pass
class drones_ImmovableObject(FieldObject):

    pass
class drones_MovableObject(FieldObject):

    def __init__(self, weight: float):
        self.weight = weight
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight


class drones_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class ImmovableObject:

    pass
class TemporalContainmentProxy:

    pass
class drones_ChargeStation(ImmovableObject):

    pass
class drones_Battery(TemporalContainmentProxy):

    def __init__(self, lifeTime: float, rechargeRate: float, charge: float, remainingLifeTime: float, drones_Battery: "drones_Drone" = None):
        self.lifeTime = lifeTime
        self.rechargeRate = rechargeRate
        self.charge = charge
        self.remainingLifeTime = remainingLifeTime
        self.drones_Battery = drones_Battery
        
        pass
    @property
    def charge(self):
        return self.__charge

    @charge.setter
    def charge(self, charge: float):
        self.__charge = charge


    @property
    def remainingLifeTime(self):
        return self.__remainingLifeTime

    @remainingLifeTime.setter
    def remainingLifeTime(self, remainingLifeTime: float):
        self.__remainingLifeTime = remainingLifeTime


    @property
    def rechargeRate(self):
        return self.__rechargeRate

    @rechargeRate.setter
    def rechargeRate(self, rechargeRate: float):
        self.__rechargeRate = rechargeRate


    @property
    def lifeTime(self):
        return self.__lifeTime

    @lifeTime.setter
    def lifeTime(self, lifeTime: float):
        self.__lifeTime = lifeTime


    @property
    def drones_Battery(self):
        return self.__drones_Battery

    @drones_Battery.setter
    def drones_Battery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drones_Battery__drones_Battery", None)
        self.__drones_Battery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drones_Drone"):
                opp_val = getattr(old_value, "drones_Drone", None)
                if opp_val == self:
                    setattr(old_value, "drones_Drone", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drones_Drone"):
                opp_val = getattr(value, "drones_Drone", None)
                setattr(value, "drones_Drone", self)

class drones_Parameter(TemporalContainmentProxy):

    def __init__(self, key: str, value: str, drones_Parameter: "drones_FieldObject" = None):
        self.key = key
        self.value = value
        self.drones_Parameter = drones_Parameter
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def drones_Parameter(self):
        return self.__drones_Parameter

    @drones_Parameter.setter
    def drones_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drones_Parameter__drones_Parameter", None)
        self.__drones_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drones_FieldObject"):
                opp_val = getattr(old_value, "drones_FieldObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drones_FieldObject"):
                opp_val = getattr(value, "drones_FieldObject", None)
                if opp_val is None:
                    setattr(value, "drones_FieldObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SizedElement:

    pass
class drones_TemporalContainmentProxy(ABC):

    pass
class NamedElement:

    pass
class drones_Mission(NamedElement):

    pass
class drones_FieldObject(SizedElement, NamedElement):

    pass
class drones_Drone(SizedElement, NamedElement):

    def __init__(self, cpuFrequency: int, memory: int, maxPayload: float, communicationRange: float, minSpeed: float, maxSpeed: float, drones_Drone: "drones_Battery" = None, drones_Drone3: "drones_ChargeStation" = None, drones_Drone5: set["drones_Action"] = None, drones_Drone10: "drones_Mission" = None):
        self.cpuFrequency = cpuFrequency
        self.memory = memory
        self.maxPayload = maxPayload
        self.communicationRange = communicationRange
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed
        self.drones_Drone = drones_Drone
        self.drones_Drone3 = drones_Drone3
        self.drones_Drone5 = drones_Drone5 if drones_Drone5 is not None else set()
        self.drones_Drone10 = drones_Drone10
        
        pass
    @property
    def maxSpeed(self):
        return self.__maxSpeed

    @maxSpeed.setter
    def maxSpeed(self, maxSpeed: float):
        self.__maxSpeed = maxSpeed


    @property
    def maxPayload(self):
        return self.__maxPayload

    @maxPayload.setter
    def maxPayload(self, maxPayload: float):
        self.__maxPayload = maxPayload


    @property
    def minSpeed(self):
        return self.__minSpeed

    @minSpeed.setter
    def minSpeed(self, minSpeed: float):
        self.__minSpeed = minSpeed


    @property
    def communicationRange(self):
        return self.__communicationRange

    @communicationRange.setter
    def communicationRange(self, communicationRange: float):
        self.__communicationRange = communicationRange


    @property
    def cpuFrequency(self):
        return self.__cpuFrequency

    @cpuFrequency.setter
    def cpuFrequency(self, cpuFrequency: int):
        self.__cpuFrequency = cpuFrequency


    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, memory: int):
        self.__memory = memory


    @property
    def drones_Drone3(self):
        return self.__drones_Drone3

    @drones_Drone3.setter
    def drones_Drone3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drones_Drone__drones_Drone3", None)
        self.__drones_Drone3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drones_ChargeStation"):
                opp_val = getattr(old_value, "drones_ChargeStation", None)
                if opp_val == self:
                    setattr(old_value, "drones_ChargeStation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drones_ChargeStation"):
                opp_val = getattr(value, "drones_ChargeStation", None)
                setattr(value, "drones_ChargeStation", self)

    @property
    def drones_Drone(self):
        return self.__drones_Drone

    @drones_Drone.setter
    def drones_Drone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drones_Drone__drones_Drone", None)
        self.__drones_Drone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drones_Battery"):
                opp_val = getattr(old_value, "drones_Battery", None)
                if opp_val == self:
                    setattr(old_value, "drones_Battery", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drones_Battery"):
                opp_val = getattr(value, "drones_Battery", None)
                setattr(value, "drones_Battery", self)

    @property
    def drones_Drone10(self):
        return self.__drones_Drone10

    @drones_Drone10.setter
    def drones_Drone10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drones_Drone__drones_Drone10", None)
        self.__drones_Drone10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drones_Mission9"):
                opp_val = getattr(old_value, "drones_Mission9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drones_Mission9"):
                opp_val = getattr(value, "drones_Mission9", None)
                if opp_val is None:
                    setattr(value, "drones_Mission9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drones_Drone5(self):
        return self.__drones_Drone5

    @drones_Drone5.setter
    def drones_Drone5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drones_Drone__drones_Drone5", None)
        self.__drones_Drone5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drones_Action"):
                    opp_val = getattr(item, "drones_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "drones_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drones_Action"):
                    opp_val = getattr(item, "drones_Action", None)
                    
                    setattr(item, "drones_Action", self)
                    

class drones_Action(NamedElement, TemporalContainmentProxy):

    def __init__(self, operation: str, key: str, value: str, range: float, drones_Action: "drones_Drone" = None, drones_Action15: "drones_Mission" = None):
        self.operation = operation
        self.key = key
        self.value = value
        self.range = range
        self.drones_Action = drones_Action
        self.drones_Action15 = drones_Action15
        
        pass
    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, range: float):
        self.__range = range


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation


    @property
    def drones_Action15(self):
        return self.__drones_Action15

    @drones_Action15.setter
    def drones_Action15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drones_Action__drones_Action15", None)
        self.__drones_Action15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drones_Mission14"):
                opp_val = getattr(old_value, "drones_Mission14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drones_Mission14"):
                opp_val = getattr(value, "drones_Mission14", None)
                if opp_val is None:
                    setattr(value, "drones_Mission14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drones_Action(self):
        return self.__drones_Action

    @drones_Action.setter
    def drones_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drones_Action__drones_Action", None)
        self.__drones_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drones_Drone5"):
                opp_val = getattr(old_value, "drones_Drone5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drones_Drone5"):
                opp_val = getattr(value, "drones_Drone5", None)
                if opp_val is None:
                    setattr(value, "drones_Drone5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
