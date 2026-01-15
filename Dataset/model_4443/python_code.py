from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ioT_Destination:

    def __init__(self, name: str, ioT_Destination: "ioT_DestinationType" = None):
        self.name = name
        self.ioT_Destination = ioT_Destination
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_Destination(self):
        return self.__ioT_Destination

    @ioT_Destination.setter
    def ioT_Destination(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Destination__ioT_Destination", None)
        self.__ioT_Destination = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_DestinationType25"):
                opp_val = getattr(old_value, "ioT_DestinationType25", None)
                if opp_val == self:
                    setattr(old_value, "ioT_DestinationType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_DestinationType25"):
                opp_val = getattr(value, "ioT_DestinationType25", None)
                setattr(value, "ioT_DestinationType25", self)

class ioT_FetchDataCondition:

    def __init__(self, condition: str):
        self.condition = condition
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

class ioT_Time:

    def __init__(self, time: int, ioT_Time: "ioT_FetchDataExpression" = None):
        self.time = time
        self.ioT_Time = ioT_Time
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def ioT_Time(self):
        return self.__ioT_Time

    @ioT_Time.setter
    def ioT_Time(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Time__ioT_Time", None)
        self.__ioT_Time = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_FetchDataExpression"):
                opp_val = getattr(old_value, "ioT_FetchDataExpression", None)
                if opp_val == self:
                    setattr(old_value, "ioT_FetchDataExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_FetchDataExpression"):
                opp_val = getattr(value, "ioT_FetchDataExpression", None)
                setattr(value, "ioT_FetchDataExpression", self)

class ioT_FetchDataExpression:

    def __init__(self, timeUnit: str, ioT_FetchDataExpression: "ioT_Time" = None):
        self.timeUnit = timeUnit
        self.ioT_FetchDataExpression = ioT_FetchDataExpression
        
    @property
    def timeUnit(self) -> str:
        return self.__timeUnit

    @timeUnit.setter
    def timeUnit(self, timeUnit: str):
        self.__timeUnit = timeUnit

    @property
    def ioT_FetchDataExpression(self):
        return self.__ioT_FetchDataExpression

    @ioT_FetchDataExpression.setter
    def ioT_FetchDataExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_FetchDataExpression__ioT_FetchDataExpression", None)
        self.__ioT_FetchDataExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Time"):
                opp_val = getattr(old_value, "ioT_Time", None)
                if opp_val == self:
                    setattr(old_value, "ioT_Time", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Time"):
                opp_val = getattr(value, "ioT_Time", None)
                setattr(value, "ioT_Time", self)

class ioT_FetchData:

    pass
class ioT_Sensor:

    def __init__(self, name: str, ioT_Sensor: "ioT_SensorType" = None, ioT_Sensor5: "ioT_SensorGroup" = None):
        self.name = name
        self.ioT_Sensor = ioT_Sensor
        self.ioT_Sensor5 = ioT_Sensor5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_Sensor5(self):
        return self.__ioT_Sensor5

    @ioT_Sensor5.setter
    def ioT_Sensor5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Sensor__ioT_Sensor5", None)
        self.__ioT_Sensor5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_SensorGroup"):
                opp_val = getattr(old_value, "ioT_SensorGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_SensorGroup"):
                opp_val = getattr(value, "ioT_SensorGroup", None)
                if opp_val is None:
                    setattr(value, "ioT_SensorGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_Sensor(self):
        return self.__ioT_Sensor

    @ioT_Sensor.setter
    def ioT_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Sensor__ioT_Sensor", None)
        self.__ioT_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_SensorType3"):
                opp_val = getattr(old_value, "ioT_SensorType3", None)
                if opp_val == self:
                    setattr(old_value, "ioT_SensorType3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_SensorType3"):
                opp_val = getattr(value, "ioT_SensorType3", None)
                setattr(value, "ioT_SensorType3", self)

class ioT_DestinationTypes:

    pass
class ioT_DestinationType:

    def __init__(self, name: str, ioT_DestinationType: "ioT_DestinationTypes" = None, ioT_DestinationType25: "ioT_Destination" = None):
        self.name = name
        self.ioT_DestinationType = ioT_DestinationType
        self.ioT_DestinationType25 = ioT_DestinationType25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_DestinationType25(self):
        return self.__ioT_DestinationType25

    @ioT_DestinationType25.setter
    def ioT_DestinationType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_DestinationType__ioT_DestinationType25", None)
        self.__ioT_DestinationType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Destination"):
                opp_val = getattr(old_value, "ioT_Destination", None)
                if opp_val == self:
                    setattr(old_value, "ioT_Destination", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Destination"):
                opp_val = getattr(value, "ioT_Destination", None)
                setattr(value, "ioT_Destination", self)

    @property
    def ioT_DestinationType(self):
        return self.__ioT_DestinationType

    @ioT_DestinationType.setter
    def ioT_DestinationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_DestinationType__ioT_DestinationType", None)
        self.__ioT_DestinationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_DestinationTypes"):
                opp_val = getattr(old_value, "ioT_DestinationTypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_DestinationTypes"):
                opp_val = getattr(value, "ioT_DestinationTypes", None)
                if opp_val is None:
                    setattr(value, "ioT_DestinationTypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_Portnumber:

    def __init__(self, number: int, ioT_Portnumber: "ioT_Server" = None):
        self.number = number
        self.ioT_Portnumber = ioT_Portnumber
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def ioT_Portnumber(self):
        return self.__ioT_Portnumber

    @ioT_Portnumber.setter
    def ioT_Portnumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Portnumber__ioT_Portnumber", None)
        self.__ioT_Portnumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Server22"):
                opp_val = getattr(old_value, "ioT_Server22", None)
                if opp_val == self:
                    setattr(old_value, "ioT_Server22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Server22"):
                opp_val = getattr(value, "ioT_Server22", None)
                setattr(value, "ioT_Server22", self)

class ioT_Ip:

    def __init__(self, ip: int, ioT_Ip: "ioT_Server" = None):
        self.ip = ip
        self.ioT_Ip = ioT_Ip
        
    @property
    def ip(self) -> int:
        return self.__ip

    @ip.setter
    def ip(self, ip: int):
        self.__ip = ip

    @property
    def ioT_Ip(self):
        return self.__ioT_Ip

    @ioT_Ip.setter
    def ioT_Ip(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Ip__ioT_Ip", None)
        self.__ioT_Ip = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Server20"):
                opp_val = getattr(old_value, "ioT_Server20", None)
                if opp_val == self:
                    setattr(old_value, "ioT_Server20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Server20"):
                opp_val = getattr(value, "ioT_Server20", None)
                setattr(value, "ioT_Server20", self)

class ioT_Server:

    def __init__(self, name: str, ioT_Server: "ioT_ServerType" = None, ioT_Server20: "ioT_Ip" = None, ioT_Server22: "ioT_Portnumber" = None):
        self.name = name
        self.ioT_Server = ioT_Server
        self.ioT_Server20 = ioT_Server20
        self.ioT_Server22 = ioT_Server22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_Server20(self):
        return self.__ioT_Server20

    @ioT_Server20.setter
    def ioT_Server20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Server__ioT_Server20", None)
        self.__ioT_Server20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Ip"):
                opp_val = getattr(old_value, "ioT_Ip", None)
                if opp_val == self:
                    setattr(old_value, "ioT_Ip", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Ip"):
                opp_val = getattr(value, "ioT_Ip", None)
                setattr(value, "ioT_Ip", self)

    @property
    def ioT_Server22(self):
        return self.__ioT_Server22

    @ioT_Server22.setter
    def ioT_Server22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Server__ioT_Server22", None)
        self.__ioT_Server22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Portnumber"):
                opp_val = getattr(old_value, "ioT_Portnumber", None)
                if opp_val == self:
                    setattr(old_value, "ioT_Portnumber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Portnumber"):
                opp_val = getattr(value, "ioT_Portnumber", None)
                setattr(value, "ioT_Portnumber", self)

    @property
    def ioT_Server(self):
        return self.__ioT_Server

    @ioT_Server.setter
    def ioT_Server(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Server__ioT_Server", None)
        self.__ioT_Server = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_ServerType18"):
                opp_val = getattr(old_value, "ioT_ServerType18", None)
                if opp_val == self:
                    setattr(old_value, "ioT_ServerType18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_ServerType18"):
                opp_val = getattr(value, "ioT_ServerType18", None)
                setattr(value, "ioT_ServerType18", self)

class ioT_ServerTypes:

    pass
class ioT_ServerType:

    def __init__(self, name: str, ioT_ServerType: "ioT_ServerTypes" = None, ioT_ServerType18: "ioT_Server" = None):
        self.name = name
        self.ioT_ServerType = ioT_ServerType
        self.ioT_ServerType18 = ioT_ServerType18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_ServerType18(self):
        return self.__ioT_ServerType18

    @ioT_ServerType18.setter
    def ioT_ServerType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_ServerType__ioT_ServerType18", None)
        self.__ioT_ServerType18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Server"):
                opp_val = getattr(old_value, "ioT_Server", None)
                if opp_val == self:
                    setattr(old_value, "ioT_Server", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Server"):
                opp_val = getattr(value, "ioT_Server", None)
                setattr(value, "ioT_Server", self)

    @property
    def ioT_ServerType(self):
        return self.__ioT_ServerType

    @ioT_ServerType.setter
    def ioT_ServerType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_ServerType__ioT_ServerType", None)
        self.__ioT_ServerType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_ServerTypes"):
                opp_val = getattr(old_value, "ioT_ServerTypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_ServerTypes"):
                opp_val = getattr(value, "ioT_ServerTypes", None)
                if opp_val is None:
                    setattr(value, "ioT_ServerTypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_Device:

    def __init__(self, name: str, ioT_Device: "ioT_DeviceType" = None, ioT_Device14: "ioT_EObject" = None):
        self.name = name
        self.ioT_Device = ioT_Device
        self.ioT_Device14 = ioT_Device14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_Device(self):
        return self.__ioT_Device

    @ioT_Device.setter
    def ioT_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Device__ioT_Device", None)
        self.__ioT_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_DeviceType12"):
                opp_val = getattr(old_value, "ioT_DeviceType12", None)
                if opp_val == self:
                    setattr(old_value, "ioT_DeviceType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_DeviceType12"):
                opp_val = getattr(value, "ioT_DeviceType12", None)
                setattr(value, "ioT_DeviceType12", self)

    @property
    def ioT_Device14(self):
        return self.__ioT_Device14

    @ioT_Device14.setter
    def ioT_Device14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Device__ioT_Device14", None)
        self.__ioT_Device14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_EObject15"):
                opp_val = getattr(old_value, "ioT_EObject15", None)
                if opp_val == self:
                    setattr(old_value, "ioT_EObject15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_EObject15"):
                opp_val = getattr(value, "ioT_EObject15", None)
                setattr(value, "ioT_EObject15", self)

class ioT_DeviceTypes:

    pass
class ioT_DeviceType:

    def __init__(self, name: str, ioT_DeviceType: "ioT_DeviceTypes" = None, ioT_DeviceType12: "ioT_Device" = None):
        self.name = name
        self.ioT_DeviceType = ioT_DeviceType
        self.ioT_DeviceType12 = ioT_DeviceType12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_DeviceType12(self):
        return self.__ioT_DeviceType12

    @ioT_DeviceType12.setter
    def ioT_DeviceType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_DeviceType__ioT_DeviceType12", None)
        self.__ioT_DeviceType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Device"):
                opp_val = getattr(old_value, "ioT_Device", None)
                if opp_val == self:
                    setattr(old_value, "ioT_Device", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Device"):
                opp_val = getattr(value, "ioT_Device", None)
                setattr(value, "ioT_Device", self)

    @property
    def ioT_DeviceType(self):
        return self.__ioT_DeviceType

    @ioT_DeviceType.setter
    def ioT_DeviceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_DeviceType__ioT_DeviceType", None)
        self.__ioT_DeviceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_DeviceTypes"):
                opp_val = getattr(old_value, "ioT_DeviceTypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_DeviceTypes"):
                opp_val = getattr(value, "ioT_DeviceTypes", None)
                if opp_val is None:
                    setattr(value, "ioT_DeviceTypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_Method:

    def __init__(self, name: str, parameters: str, ioT_Method: "ioT_SensorGetMethod" = None):
        self.name = name
        self.parameters = parameters
        self.ioT_Method = ioT_Method
        
    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_Method(self):
        return self.__ioT_Method

    @ioT_Method.setter
    def ioT_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Method__ioT_Method", None)
        self.__ioT_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_SensorGetMethod"):
                opp_val = getattr(old_value, "ioT_SensorGetMethod", None)
                if opp_val == self:
                    setattr(old_value, "ioT_SensorGetMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_SensorGetMethod"):
                opp_val = getattr(value, "ioT_SensorGetMethod", None)
                setattr(value, "ioT_SensorGetMethod", self)

class ioT_SensorGetMethod:

    pass
class ioT_SensorGroup:

    def __init__(self, name: str, ioT_SensorGroup: set["ioT_Sensor"] = None):
        self.name = name
        self.ioT_SensorGroup = ioT_SensorGroup if ioT_SensorGroup is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_SensorGroup(self):
        return self.__ioT_SensorGroup

    @ioT_SensorGroup.setter
    def ioT_SensorGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_SensorGroup__ioT_SensorGroup", None)
        self.__ioT_SensorGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_Sensor5"):
                    opp_val = getattr(item, "ioT_Sensor5", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_Sensor5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_Sensor5"):
                    opp_val = getattr(item, "ioT_Sensor5", None)
                    
                    setattr(item, "ioT_Sensor5", self)
                    

class ioT_SensorTypes:

    pass
class ioT_SensorType:

    def __init__(self, name: str, ioT_SensorType: "ioT_SensorTypes" = None, ioT_SensorType9: "ioT_SensorGetMethod" = None, ioT_SensorType3: "ioT_Sensor" = None):
        self.name = name
        self.ioT_SensorType = ioT_SensorType
        self.ioT_SensorType9 = ioT_SensorType9
        self.ioT_SensorType3 = ioT_SensorType3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_SensorType9(self):
        return self.__ioT_SensorType9

    @ioT_SensorType9.setter
    def ioT_SensorType9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_SensorType__ioT_SensorType9", None)
        self.__ioT_SensorType9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_SensorGetMethod8"):
                opp_val = getattr(old_value, "ioT_SensorGetMethod8", None)
                if opp_val == self:
                    setattr(old_value, "ioT_SensorGetMethod8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_SensorGetMethod8"):
                opp_val = getattr(value, "ioT_SensorGetMethod8", None)
                setattr(value, "ioT_SensorGetMethod8", self)

    @property
    def ioT_SensorType(self):
        return self.__ioT_SensorType

    @ioT_SensorType.setter
    def ioT_SensorType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_SensorType__ioT_SensorType", None)
        self.__ioT_SensorType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_SensorTypes"):
                opp_val = getattr(old_value, "ioT_SensorTypes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_SensorTypes"):
                opp_val = getattr(value, "ioT_SensorTypes", None)
                if opp_val is None:
                    setattr(value, "ioT_SensorTypes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_SensorType3(self):
        return self.__ioT_SensorType3

    @ioT_SensorType3.setter
    def ioT_SensorType3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_SensorType__ioT_SensorType3", None)
        self.__ioT_SensorType3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Sensor"):
                opp_val = getattr(old_value, "ioT_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "ioT_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Sensor"):
                opp_val = getattr(value, "ioT_Sensor", None)
                setattr(value, "ioT_Sensor", self)

class ioT_EObject:

    pass
class ioT_System:

    pass