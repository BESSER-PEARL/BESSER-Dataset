from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MemoryType(Enum):
    VOLATILE = "VOLATILE"
    STORAGE = "STORAGE"
class LaunchType(Enum):
    VTOL = "VTOL"
    HTOL = "HTOL"
    OTHER = "OTHER"


############################################
# Definition of Classes
############################################

class drone_Parameter:

    def __init__(self, key: str, description: str, drone_Parameter: "drone_Action" = None):
        self.key = key
        self.description = description
        self.drone_Parameter = drone_Parameter
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def drone_Parameter(self):
        return self.__drone_Parameter

    @drone_Parameter.setter
    def drone_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Parameter__drone_Parameter", None)
        self.__drone_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Action18"):
                opp_val = getattr(old_value, "drone_Action18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Action18"):
                opp_val = getattr(value, "drone_Action18", None)
                if opp_val is None:
                    setattr(value, "drone_Action18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drone_FlightPerformance:

    def __init__(self, launchType: str, minSpeed: int, maxSpeed: int, minAcceleration: int, maxAcceleration: int, maxAltitude: int, maxTurnRate: float, minTurnRate: float, maxClimbRate: float, maxDescendRate: float, positionHold: float, maxPayload: int, maxFlightTime: int, maxFlightTimeWithMaxPayload: int, minOperatingTemperature: float, maxOperatingTemperature: float, drone_FlightPerformance: "drone_Drone" = None):
        self.launchType = launchType
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed
        self.minAcceleration = minAcceleration
        self.maxAcceleration = maxAcceleration
        self.maxAltitude = maxAltitude
        self.maxTurnRate = maxTurnRate
        self.minTurnRate = minTurnRate
        self.maxClimbRate = maxClimbRate
        self.maxDescendRate = maxDescendRate
        self.positionHold = positionHold
        self.maxPayload = maxPayload
        self.maxFlightTime = maxFlightTime
        self.maxFlightTimeWithMaxPayload = maxFlightTimeWithMaxPayload
        self.minOperatingTemperature = minOperatingTemperature
        self.maxOperatingTemperature = maxOperatingTemperature
        self.drone_FlightPerformance = drone_FlightPerformance
        
    @property
    def maxTurnRate(self) -> float:
        return self.__maxTurnRate

    @maxTurnRate.setter
    def maxTurnRate(self, maxTurnRate: float):
        self.__maxTurnRate = maxTurnRate

    @property
    def maxOperatingTemperature(self) -> float:
        return self.__maxOperatingTemperature

    @maxOperatingTemperature.setter
    def maxOperatingTemperature(self, maxOperatingTemperature: float):
        self.__maxOperatingTemperature = maxOperatingTemperature

    @property
    def maxFlightTime(self) -> int:
        return self.__maxFlightTime

    @maxFlightTime.setter
    def maxFlightTime(self, maxFlightTime: int):
        self.__maxFlightTime = maxFlightTime

    @property
    def maxFlightTimeWithMaxPayload(self) -> int:
        return self.__maxFlightTimeWithMaxPayload

    @maxFlightTimeWithMaxPayload.setter
    def maxFlightTimeWithMaxPayload(self, maxFlightTimeWithMaxPayload: int):
        self.__maxFlightTimeWithMaxPayload = maxFlightTimeWithMaxPayload

    @property
    def maxPayload(self) -> int:
        return self.__maxPayload

    @maxPayload.setter
    def maxPayload(self, maxPayload: int):
        self.__maxPayload = maxPayload

    @property
    def maxAltitude(self) -> int:
        return self.__maxAltitude

    @maxAltitude.setter
    def maxAltitude(self, maxAltitude: int):
        self.__maxAltitude = maxAltitude

    @property
    def maxDescendRate(self) -> float:
        return self.__maxDescendRate

    @maxDescendRate.setter
    def maxDescendRate(self, maxDescendRate: float):
        self.__maxDescendRate = maxDescendRate

    @property
    def minSpeed(self) -> int:
        return self.__minSpeed

    @minSpeed.setter
    def minSpeed(self, minSpeed: int):
        self.__minSpeed = minSpeed

    @property
    def maxClimbRate(self) -> float:
        return self.__maxClimbRate

    @maxClimbRate.setter
    def maxClimbRate(self, maxClimbRate: float):
        self.__maxClimbRate = maxClimbRate

    @property
    def minOperatingTemperature(self) -> float:
        return self.__minOperatingTemperature

    @minOperatingTemperature.setter
    def minOperatingTemperature(self, minOperatingTemperature: float):
        self.__minOperatingTemperature = minOperatingTemperature

    @property
    def positionHold(self) -> float:
        return self.__positionHold

    @positionHold.setter
    def positionHold(self, positionHold: float):
        self.__positionHold = positionHold

    @property
    def maxSpeed(self) -> int:
        return self.__maxSpeed

    @maxSpeed.setter
    def maxSpeed(self, maxSpeed: int):
        self.__maxSpeed = maxSpeed

    @property
    def launchType(self) -> str:
        return self.__launchType

    @launchType.setter
    def launchType(self, launchType: str):
        self.__launchType = launchType

    @property
    def maxAcceleration(self) -> int:
        return self.__maxAcceleration

    @maxAcceleration.setter
    def maxAcceleration(self, maxAcceleration: int):
        self.__maxAcceleration = maxAcceleration

    @property
    def minTurnRate(self) -> float:
        return self.__minTurnRate

    @minTurnRate.setter
    def minTurnRate(self, minTurnRate: float):
        self.__minTurnRate = minTurnRate

    @property
    def minAcceleration(self) -> int:
        return self.__minAcceleration

    @minAcceleration.setter
    def minAcceleration(self, minAcceleration: int):
        self.__minAcceleration = minAcceleration

    @property
    def drone_FlightPerformance(self):
        return self.__drone_FlightPerformance

    @drone_FlightPerformance.setter
    def drone_FlightPerformance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_FlightPerformance__drone_FlightPerformance", None)
        self.__drone_FlightPerformance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Drone2"):
                opp_val = getattr(old_value, "drone_Drone2", None)
                if opp_val == self:
                    setattr(old_value, "drone_Drone2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Drone2"):
                opp_val = getattr(value, "drone_Drone2", None)
                setattr(value, "drone_Drone2", self)

class drone_Size:

    def __init__(self, width: float, length: float, height: float, weight: float, propellers: int, propellerSize: float, drone_Size: "drone_Drone" = None):
        self.width = width
        self.length = length
        self.height = height
        self.weight = weight
        self.propellers = propellers
        self.propellerSize = propellerSize
        self.drone_Size = drone_Size
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def propellerSize(self) -> float:
        return self.__propellerSize

    @propellerSize.setter
    def propellerSize(self, propellerSize: float):
        self.__propellerSize = propellerSize

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def propellers(self) -> int:
        return self.__propellers

    @propellers.setter
    def propellers(self, propellers: int):
        self.__propellers = propellers

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length

    @property
    def drone_Size(self):
        return self.__drone_Size

    @drone_Size.setter
    def drone_Size(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Size__drone_Size", None)
        self.__drone_Size = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Drone"):
                opp_val = getattr(old_value, "drone_Drone", None)
                if opp_val == self:
                    setattr(old_value, "drone_Drone", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Drone"):
                opp_val = getattr(value, "drone_Drone", None)
                setattr(value, "drone_Drone", self)

class NamedElement:

    pass
class drone_Device(NamedElement):

    pass
class drone_Memory(NamedElement):

    def __init__(self, type: str, subType: str, size: int, drone_Memory: "drone_Drone" = None):
        self.type = type
        self.subType = subType
        self.size = size
        self.drone_Memory = drone_Memory
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def subType(self) -> str:
        return self.__subType

    @subType.setter
    def subType(self, subType: str):
        self.__subType = subType

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def drone_Memory(self):
        return self.__drone_Memory

    @drone_Memory.setter
    def drone_Memory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Memory__drone_Memory", None)
        self.__drone_Memory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Drone8"):
                opp_val = getattr(old_value, "drone_Drone8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Drone8"):
                opp_val = getattr(value, "drone_Drone8", None)
                if opp_val is None:
                    setattr(value, "drone_Drone8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drone_Property(NamedElement):

    def __init__(self, value: str, drone_Property: "drone_Device" = None):
        self.value = value
        self.drone_Property = drone_Property
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def drone_Property(self):
        return self.__drone_Property

    @drone_Property.setter
    def drone_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Property__drone_Property", None)
        self.__drone_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Device16"):
                opp_val = getattr(old_value, "drone_Device16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Device16"):
                opp_val = getattr(value, "drone_Device16", None)
                if opp_val is None:
                    setattr(value, "drone_Device16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drone_ROSDriver(NamedElement):

    def __init__(self, version: str, url: str, drone_ROSDriver: "drone_Drone" = None):
        self.version = version
        self.url = url
        self.drone_ROSDriver = drone_ROSDriver
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def drone_ROSDriver(self):
        return self.__drone_ROSDriver

    @drone_ROSDriver.setter
    def drone_ROSDriver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_ROSDriver__drone_ROSDriver", None)
        self.__drone_ROSDriver = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Drone12"):
                opp_val = getattr(old_value, "drone_Drone12", None)
                if opp_val == self:
                    setattr(old_value, "drone_Drone12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Drone12"):
                opp_val = getattr(value, "drone_Drone12", None)
                setattr(value, "drone_Drone12", self)

class drone_Action(NamedElement):

    pass
class drone_Processor(NamedElement):

    def __init__(self, architecture: str, frequency: int, drone_Processor: "drone_Drone" = None):
        self.architecture = architecture
        self.frequency = frequency
        self.drone_Processor = drone_Processor
        
    @property
    def frequency(self) -> int:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: int):
        self.__frequency = frequency

    @property
    def architecture(self) -> str:
        return self.__architecture

    @architecture.setter
    def architecture(self, architecture: str):
        self.__architecture = architecture

    @property
    def drone_Processor(self):
        return self.__drone_Processor

    @drone_Processor.setter
    def drone_Processor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Processor__drone_Processor", None)
        self.__drone_Processor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Drone6"):
                opp_val = getattr(old_value, "drone_Drone6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Drone6"):
                opp_val = getattr(value, "drone_Drone6", None)
                if opp_val is None:
                    setattr(value, "drone_Drone6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drone_Battery(NamedElement):

    def __init__(self, cellType: str, capacity: int, voltage: float, rechargeTime: int, drone_Battery: "drone_Drone" = None):
        self.cellType = cellType
        self.capacity = capacity
        self.voltage = voltage
        self.rechargeTime = rechargeTime
        self.drone_Battery = drone_Battery
        
    @property
    def cellType(self) -> str:
        return self.__cellType

    @cellType.setter
    def cellType(self, cellType: str):
        self.__cellType = cellType

    @property
    def voltage(self) -> float:
        return self.__voltage

    @voltage.setter
    def voltage(self, voltage: float):
        self.__voltage = voltage

    @property
    def rechargeTime(self) -> int:
        return self.__rechargeTime

    @rechargeTime.setter
    def rechargeTime(self, rechargeTime: int):
        self.__rechargeTime = rechargeTime

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def drone_Battery(self):
        return self.__drone_Battery

    @drone_Battery.setter
    def drone_Battery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Battery__drone_Battery", None)
        self.__drone_Battery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Drone4"):
                opp_val = getattr(old_value, "drone_Drone4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Drone4"):
                opp_val = getattr(value, "drone_Drone4", None)
                if opp_val is None:
                    setattr(value, "drone_Drone4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drone_Drone(NamedElement):

    def __init__(self, onBoardObstacleAvoidance: bool, minVoltage: float, maxVoltage: float, maxPowerConsumption: float, giro: bool, gps: bool, accelerometer: bool, magnetometer: bool, barometer: bool, communicationRange: float, dataRate: int, radioFrequency: int, drone_Drone: "drone_Size" = None, drone_Drone2: "drone_FlightPerformance" = None, drone_Drone4: set["drone_Battery"] = None, drone_Drone6: set["drone_Processor"] = None, drone_Drone8: set["drone_Memory"] = None, drone_Drone10: set["drone_Device"] = None, drone_Drone12: "drone_ROSDriver" = None):
        self.onBoardObstacleAvoidance = onBoardObstacleAvoidance
        self.minVoltage = minVoltage
        self.maxVoltage = maxVoltage
        self.maxPowerConsumption = maxPowerConsumption
        self.giro = giro
        self.gps = gps
        self.accelerometer = accelerometer
        self.magnetometer = magnetometer
        self.barometer = barometer
        self.communicationRange = communicationRange
        self.dataRate = dataRate
        self.radioFrequency = radioFrequency
        self.drone_Drone = drone_Drone
        self.drone_Drone2 = drone_Drone2
        self.drone_Drone4 = drone_Drone4 if drone_Drone4 is not None else set()
        self.drone_Drone6 = drone_Drone6 if drone_Drone6 is not None else set()
        self.drone_Drone8 = drone_Drone8 if drone_Drone8 is not None else set()
        self.drone_Drone10 = drone_Drone10 if drone_Drone10 is not None else set()
        self.drone_Drone12 = drone_Drone12
        
    @property
    def onBoardObstacleAvoidance(self) -> bool:
        return self.__onBoardObstacleAvoidance

    @onBoardObstacleAvoidance.setter
    def onBoardObstacleAvoidance(self, onBoardObstacleAvoidance: bool):
        self.__onBoardObstacleAvoidance = onBoardObstacleAvoidance

    @property
    def accelerometer(self) -> bool:
        return self.__accelerometer

    @accelerometer.setter
    def accelerometer(self, accelerometer: bool):
        self.__accelerometer = accelerometer

    @property
    def maxVoltage(self) -> float:
        return self.__maxVoltage

    @maxVoltage.setter
    def maxVoltage(self, maxVoltage: float):
        self.__maxVoltage = maxVoltage

    @property
    def barometer(self) -> bool:
        return self.__barometer

    @barometer.setter
    def barometer(self, barometer: bool):
        self.__barometer = barometer

    @property
    def minVoltage(self) -> float:
        return self.__minVoltage

    @minVoltage.setter
    def minVoltage(self, minVoltage: float):
        self.__minVoltage = minVoltage

    @property
    def giro(self) -> bool:
        return self.__giro

    @giro.setter
    def giro(self, giro: bool):
        self.__giro = giro

    @property
    def maxPowerConsumption(self) -> float:
        return self.__maxPowerConsumption

    @maxPowerConsumption.setter
    def maxPowerConsumption(self, maxPowerConsumption: float):
        self.__maxPowerConsumption = maxPowerConsumption

    @property
    def communicationRange(self) -> float:
        return self.__communicationRange

    @communicationRange.setter
    def communicationRange(self, communicationRange: float):
        self.__communicationRange = communicationRange

    @property
    def radioFrequency(self) -> int:
        return self.__radioFrequency

    @radioFrequency.setter
    def radioFrequency(self, radioFrequency: int):
        self.__radioFrequency = radioFrequency

    @property
    def gps(self) -> bool:
        return self.__gps

    @gps.setter
    def gps(self, gps: bool):
        self.__gps = gps

    @property
    def magnetometer(self) -> bool:
        return self.__magnetometer

    @magnetometer.setter
    def magnetometer(self, magnetometer: bool):
        self.__magnetometer = magnetometer

    @property
    def dataRate(self) -> int:
        return self.__dataRate

    @dataRate.setter
    def dataRate(self, dataRate: int):
        self.__dataRate = dataRate

    @property
    def drone_Drone4(self):
        return self.__drone_Drone4

    @drone_Drone4.setter
    def drone_Drone4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Drone__drone_Drone4", None)
        self.__drone_Drone4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drone_Battery"):
                    opp_val = getattr(item, "drone_Battery", None)
                    
                    if opp_val == self:
                        setattr(item, "drone_Battery", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drone_Battery"):
                    opp_val = getattr(item, "drone_Battery", None)
                    
                    setattr(item, "drone_Battery", self)
                    

    @property
    def drone_Drone2(self):
        return self.__drone_Drone2

    @drone_Drone2.setter
    def drone_Drone2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Drone__drone_Drone2", None)
        self.__drone_Drone2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_FlightPerformance"):
                opp_val = getattr(old_value, "drone_FlightPerformance", None)
                if opp_val == self:
                    setattr(old_value, "drone_FlightPerformance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_FlightPerformance"):
                opp_val = getattr(value, "drone_FlightPerformance", None)
                setattr(value, "drone_FlightPerformance", self)

    @property
    def drone_Drone10(self):
        return self.__drone_Drone10

    @drone_Drone10.setter
    def drone_Drone10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Drone__drone_Drone10", None)
        self.__drone_Drone10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drone_Device"):
                    opp_val = getattr(item, "drone_Device", None)
                    
                    if opp_val == self:
                        setattr(item, "drone_Device", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drone_Device"):
                    opp_val = getattr(item, "drone_Device", None)
                    
                    setattr(item, "drone_Device", self)
                    

    @property
    def drone_Drone(self):
        return self.__drone_Drone

    @drone_Drone.setter
    def drone_Drone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Drone__drone_Drone", None)
        self.__drone_Drone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Size"):
                opp_val = getattr(old_value, "drone_Size", None)
                if opp_val == self:
                    setattr(old_value, "drone_Size", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Size"):
                opp_val = getattr(value, "drone_Size", None)
                setattr(value, "drone_Size", self)

    @property
    def drone_Drone8(self):
        return self.__drone_Drone8

    @drone_Drone8.setter
    def drone_Drone8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Drone__drone_Drone8", None)
        self.__drone_Drone8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drone_Memory"):
                    opp_val = getattr(item, "drone_Memory", None)
                    
                    if opp_val == self:
                        setattr(item, "drone_Memory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drone_Memory"):
                    opp_val = getattr(item, "drone_Memory", None)
                    
                    setattr(item, "drone_Memory", self)
                    

    @property
    def drone_Drone12(self):
        return self.__drone_Drone12

    @drone_Drone12.setter
    def drone_Drone12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Drone__drone_Drone12", None)
        self.__drone_Drone12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_ROSDriver"):
                opp_val = getattr(old_value, "drone_ROSDriver", None)
                if opp_val == self:
                    setattr(old_value, "drone_ROSDriver", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_ROSDriver"):
                opp_val = getattr(value, "drone_ROSDriver", None)
                setattr(value, "drone_ROSDriver", self)

    @property
    def drone_Drone6(self):
        return self.__drone_Drone6

    @drone_Drone6.setter
    def drone_Drone6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Drone__drone_Drone6", None)
        self.__drone_Drone6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "drone_Processor"):
                    opp_val = getattr(item, "drone_Processor", None)
                    
                    if opp_val == self:
                        setattr(item, "drone_Processor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "drone_Processor"):
                    opp_val = getattr(item, "drone_Processor", None)
                    
                    setattr(item, "drone_Processor", self)
                    

class drone_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
