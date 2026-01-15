from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class drone_EObject:

    pass
class drone_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class drone_RobotMissionContainer:

    pass
class drone_MeasureConversion:

    def __init__(self, rate: float, drone_MeasureConversion: "drone_MeasureDimension" = None, drone_MeasureConversion82: "drone_MeasureDimension" = None):
        self.rate = rate
        self.drone_MeasureConversion = drone_MeasureConversion
        self.drone_MeasureConversion82 = drone_MeasureConversion82
        
    @property
    def rate(self) -> float:
        return self.__rate

    @rate.setter
    def rate(self, rate: float):
        self.__rate = rate

    @property
    def drone_MeasureConversion82(self):
        return self.__drone_MeasureConversion82

    @drone_MeasureConversion82.setter
    def drone_MeasureConversion82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureConversion__drone_MeasureConversion82", None)
        self.__drone_MeasureConversion82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_MeasureDimension81"):
                opp_val = getattr(old_value, "drone_MeasureDimension81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_MeasureDimension81"):
                opp_val = getattr(value, "drone_MeasureDimension81", None)
                if opp_val is None:
                    setattr(value, "drone_MeasureDimension81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def drone_MeasureConversion(self):
        return self.__drone_MeasureConversion

    @drone_MeasureConversion.setter
    def drone_MeasureConversion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureConversion__drone_MeasureConversion", None)
        self.__drone_MeasureConversion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_MeasureDimension79"):
                opp_val = getattr(old_value, "drone_MeasureDimension79", None)
                if opp_val == self:
                    setattr(old_value, "drone_MeasureDimension79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_MeasureDimension79"):
                opp_val = getattr(value, "drone_MeasureDimension79", None)
                setattr(value, "drone_MeasureDimension79", self)

class drone_Battery:

    pass
class drone_PropertyValue(ABC):

    pass
class PropertyValue:

    pass
class drone_StringValue(PropertyValue):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class drone_CapabilityProperties:

    pass
class drone_MeasureValue(PropertyValue):

    def __init__(self, value: float, drone_MeasureValue: "drone_Robot" = None, drone_MeasureValue42: "drone_Robot" = None, drone_MeasureValue51: "drone_Size" = None, drone_MeasureValue77: "drone_MeasureDimension" = None, drone_MeasureValue54: "drone_Size" = None, drone_MeasureValue57: "drone_Size" = None, drone_MeasureValue60: "drone_Battery" = None, drone_MeasureValue63: "drone_Battery" = None, drone_MeasureValue66: "drone_Battery" = None):
        self.value = value
        self.drone_MeasureValue = drone_MeasureValue
        self.drone_MeasureValue42 = drone_MeasureValue42
        self.drone_MeasureValue51 = drone_MeasureValue51
        self.drone_MeasureValue77 = drone_MeasureValue77
        self.drone_MeasureValue54 = drone_MeasureValue54
        self.drone_MeasureValue57 = drone_MeasureValue57
        self.drone_MeasureValue60 = drone_MeasureValue60
        self.drone_MeasureValue63 = drone_MeasureValue63
        self.drone_MeasureValue66 = drone_MeasureValue66
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def drone_MeasureValue57(self):
        return self.__drone_MeasureValue57

    @drone_MeasureValue57.setter
    def drone_MeasureValue57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureValue__drone_MeasureValue57", None)
        self.__drone_MeasureValue57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Size56"):
                opp_val = getattr(old_value, "drone_Size56", None)
                if opp_val == self:
                    setattr(old_value, "drone_Size56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Size56"):
                opp_val = getattr(value, "drone_Size56", None)
                setattr(value, "drone_Size56", self)

    @property
    def drone_MeasureValue66(self):
        return self.__drone_MeasureValue66

    @drone_MeasureValue66.setter
    def drone_MeasureValue66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureValue__drone_MeasureValue66", None)
        self.__drone_MeasureValue66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Battery65"):
                opp_val = getattr(old_value, "drone_Battery65", None)
                if opp_val == self:
                    setattr(old_value, "drone_Battery65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Battery65"):
                opp_val = getattr(value, "drone_Battery65", None)
                setattr(value, "drone_Battery65", self)

    @property
    def drone_MeasureValue42(self):
        return self.__drone_MeasureValue42

    @drone_MeasureValue42.setter
    def drone_MeasureValue42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureValue__drone_MeasureValue42", None)
        self.__drone_MeasureValue42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Robot41"):
                opp_val = getattr(old_value, "drone_Robot41", None)
                if opp_val == self:
                    setattr(old_value, "drone_Robot41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Robot41"):
                opp_val = getattr(value, "drone_Robot41", None)
                setattr(value, "drone_Robot41", self)

    @property
    def drone_MeasureValue(self):
        return self.__drone_MeasureValue

    @drone_MeasureValue.setter
    def drone_MeasureValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureValue__drone_MeasureValue", None)
        self.__drone_MeasureValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Robot39"):
                opp_val = getattr(old_value, "drone_Robot39", None)
                if opp_val == self:
                    setattr(old_value, "drone_Robot39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Robot39"):
                opp_val = getattr(value, "drone_Robot39", None)
                setattr(value, "drone_Robot39", self)

    @property
    def drone_MeasureValue63(self):
        return self.__drone_MeasureValue63

    @drone_MeasureValue63.setter
    def drone_MeasureValue63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureValue__drone_MeasureValue63", None)
        self.__drone_MeasureValue63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Battery62"):
                opp_val = getattr(old_value, "drone_Battery62", None)
                if opp_val == self:
                    setattr(old_value, "drone_Battery62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Battery62"):
                opp_val = getattr(value, "drone_Battery62", None)
                setattr(value, "drone_Battery62", self)

    @property
    def drone_MeasureValue60(self):
        return self.__drone_MeasureValue60

    @drone_MeasureValue60.setter
    def drone_MeasureValue60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureValue__drone_MeasureValue60", None)
        self.__drone_MeasureValue60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Battery59"):
                opp_val = getattr(old_value, "drone_Battery59", None)
                if opp_val == self:
                    setattr(old_value, "drone_Battery59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Battery59"):
                opp_val = getattr(value, "drone_Battery59", None)
                setattr(value, "drone_Battery59", self)

    @property
    def drone_MeasureValue77(self):
        return self.__drone_MeasureValue77

    @drone_MeasureValue77.setter
    def drone_MeasureValue77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureValue__drone_MeasureValue77", None)
        self.__drone_MeasureValue77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_MeasureDimension"):
                opp_val = getattr(old_value, "drone_MeasureDimension", None)
                if opp_val == self:
                    setattr(old_value, "drone_MeasureDimension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_MeasureDimension"):
                opp_val = getattr(value, "drone_MeasureDimension", None)
                setattr(value, "drone_MeasureDimension", self)

    @property
    def drone_MeasureValue51(self):
        return self.__drone_MeasureValue51

    @drone_MeasureValue51.setter
    def drone_MeasureValue51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureValue__drone_MeasureValue51", None)
        self.__drone_MeasureValue51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Size50"):
                opp_val = getattr(old_value, "drone_Size50", None)
                if opp_val == self:
                    setattr(old_value, "drone_Size50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Size50"):
                opp_val = getattr(value, "drone_Size50", None)
                setattr(value, "drone_Size50", self)

    @property
    def drone_MeasureValue54(self):
        return self.__drone_MeasureValue54

    @drone_MeasureValue54.setter
    def drone_MeasureValue54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_MeasureValue__drone_MeasureValue54", None)
        self.__drone_MeasureValue54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Size53"):
                opp_val = getattr(old_value, "drone_Size53", None)
                if opp_val == self:
                    setattr(old_value, "drone_Size53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Size53"):
                opp_val = getattr(value, "drone_Size53", None)
                setattr(value, "drone_Size53", self)

class drone_TaskDescriptor:

    pass
class NamedElement:

    pass
class drone_Task(NamedElement):

    pass
class drone_Equipment(NamedElement):

    pass
class drone_PropertyKey(NamedElement):

    pass
class drone_MeasureDimension(NamedElement):

    pass
class drone_Robot(NamedElement):

    pass
class drone_PropertyKeyContainer(NamedElement):

    pass
class drone_Capability(NamedElement):

    pass
class drone_Mission(NamedElement):

    pass
class drone_Size:

    pass
class drone_Coordinate:

    def __init__(self, latitude: float, longitude: float, altitude: float, drone_Coordinate: "drone_Position" = None):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.drone_Coordinate = drone_Coordinate
        
    @property
    def altitude(self) -> float:
        return self.__altitude

    @altitude.setter
    def altitude(self, altitude: float):
        self.__altitude = altitude

    @property
    def latitude(self) -> float:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: float):
        self.__latitude = latitude

    @property
    def longitude(self) -> float:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: float):
        self.__longitude = longitude

    @property
    def drone_Coordinate(self):
        return self.__drone_Coordinate

    @drone_Coordinate.setter
    def drone_Coordinate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_drone_Coordinate__drone_Coordinate", None)
        self.__drone_Coordinate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "drone_Position"):
                opp_val = getattr(old_value, "drone_Position", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "drone_Position"):
                opp_val = getattr(value, "drone_Position", None)
                if opp_val is None:
                    setattr(value, "drone_Position", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class drone_Position:

    pass
class drone_Property:

    pass
class drone_AreaObject(NamedElement):

    pass