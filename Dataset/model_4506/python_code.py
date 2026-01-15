from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DurationUnit(Enum):
    SECOND = "SECOND"
    MINUTE = "MINUTE"
class IntegerOperator(Enum):
    INFERIOR = "INFERIOR"
    SUPERIOR = "SUPERIOR"
    EQUALS = "EQUALS"
class BooleanOperator(Enum):
    IS = "IS"
    IS_NOT = "IS_NOT"


############################################
# Definition of Classes
############################################

class Condition:

    pass
class smartHome_IntegerCondition(Condition):

    def __init__(self, operand: int, operator: str, smartHome_IntegerCondition: "smartHome_IntegerSensor" = None):
        self.operand = operand
        self.operator = operator
        self.smartHome_IntegerCondition = smartHome_IntegerCondition
        
    @property
    def operand(self) -> int:
        return self.__operand

    @operand.setter
    def operand(self, operand: int):
        self.__operand = operand

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def smartHome_IntegerCondition(self):
        return self.__smartHome_IntegerCondition

    @smartHome_IntegerCondition.setter
    def smartHome_IntegerCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_IntegerCondition__smartHome_IntegerCondition", None)
        self.__smartHome_IntegerCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_IntegerSensor"):
                opp_val = getattr(old_value, "smartHome_IntegerSensor", None)
                if opp_val == self:
                    setattr(old_value, "smartHome_IntegerSensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_IntegerSensor"):
                opp_val = getattr(value, "smartHome_IntegerSensor", None)
                setattr(value, "smartHome_IntegerSensor", self)

class smartHome_BooleanCondition(Condition):

    def __init__(self, operand: bool, operator: str, smartHome_BooleanCondition: "smartHome_BooleanSensor" = None):
        self.operand = operand
        self.operator = operator
        self.smartHome_BooleanCondition = smartHome_BooleanCondition
        
    @property
    def operand(self) -> bool:
        return self.__operand

    @operand.setter
    def operand(self, operand: bool):
        self.__operand = operand

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def smartHome_BooleanCondition(self):
        return self.__smartHome_BooleanCondition

    @smartHome_BooleanCondition.setter
    def smartHome_BooleanCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_BooleanCondition__smartHome_BooleanCondition", None)
        self.__smartHome_BooleanCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_BooleanSensor"):
                opp_val = getattr(old_value, "smartHome_BooleanSensor", None)
                if opp_val == self:
                    setattr(old_value, "smartHome_BooleanSensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_BooleanSensor"):
                opp_val = getattr(value, "smartHome_BooleanSensor", None)
                setattr(value, "smartHome_BooleanSensor", self)

class smartHome_Duration:

    def __init__(self, unit: str, value: int, smartHome_Duration: "smartHome_Rule" = None):
        self.unit = unit
        self.value = value
        self.smartHome_Duration = smartHome_Duration
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def smartHome_Duration(self):
        return self.__smartHome_Duration

    @smartHome_Duration.setter
    def smartHome_Duration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_Duration__smartHome_Duration", None)
        self.__smartHome_Duration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_Rule15"):
                opp_val = getattr(old_value, "smartHome_Rule15", None)
                if opp_val == self:
                    setattr(old_value, "smartHome_Rule15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_Rule15"):
                opp_val = getattr(value, "smartHome_Rule15", None)
                setattr(value, "smartHome_Rule15", self)

class smartHome_Event:

    def __init__(self, description: str, smartHome_Event: "smartHome_Rule" = None):
        self.description = description
        self.smartHome_Event = smartHome_Event
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def smartHome_Event(self):
        return self.__smartHome_Event

    @smartHome_Event.setter
    def smartHome_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_Event__smartHome_Event", None)
        self.__smartHome_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_Rule13"):
                opp_val = getattr(old_value, "smartHome_Rule13", None)
                if opp_val == self:
                    setattr(old_value, "smartHome_Rule13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_Rule13"):
                opp_val = getattr(value, "smartHome_Rule13", None)
                setattr(value, "smartHome_Rule13", self)

class smartHome_Condition(ABC):

    pass
class smartHome_Rule:

    pass
class smartHome_SmartHome:

    pass
class SensorType:

    pass
class smartHome_BooleanSensorType(SensorType):

    pass
class smartHome_AnalogSensorType(SensorType):

    pass
class smartHome_Location:

    def __init__(self, name: str, smartHome_Location: set["smartHome_Sensor"] = None, smartHome_Location4: "smartHome_SmartHome" = None):
        self.name = name
        self.smartHome_Location = smartHome_Location if smartHome_Location is not None else set()
        self.smartHome_Location4 = smartHome_Location4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smartHome_Location(self):
        return self.__smartHome_Location

    @smartHome_Location.setter
    def smartHome_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_Location__smartHome_Location", None)
        self.__smartHome_Location = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smartHome_Sensor2"):
                    opp_val = getattr(item, "smartHome_Sensor2", None)
                    
                    if opp_val == self:
                        setattr(item, "smartHome_Sensor2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smartHome_Sensor2"):
                    opp_val = getattr(item, "smartHome_Sensor2", None)
                    
                    setattr(item, "smartHome_Sensor2", self)
                    

    @property
    def smartHome_Location4(self):
        return self.__smartHome_Location4

    @smartHome_Location4.setter
    def smartHome_Location4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_Location__smartHome_Location4", None)
        self.__smartHome_Location4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_SmartHome"):
                opp_val = getattr(old_value, "smartHome_SmartHome", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_SmartHome"):
                opp_val = getattr(value, "smartHome_SmartHome", None)
                if opp_val is None:
                    setattr(value, "smartHome_SmartHome", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Sensor:

    pass
class smartHome_BooleanSensor(Sensor):

    def __init__(self, value: bool, smartHome_BooleanSensor: "smartHome_BooleanCondition" = None):
        self.value = value
        self.smartHome_BooleanSensor = smartHome_BooleanSensor
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def smartHome_BooleanSensor(self):
        return self.__smartHome_BooleanSensor

    @smartHome_BooleanSensor.setter
    def smartHome_BooleanSensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_BooleanSensor__smartHome_BooleanSensor", None)
        self.__smartHome_BooleanSensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_BooleanCondition"):
                opp_val = getattr(old_value, "smartHome_BooleanCondition", None)
                if opp_val == self:
                    setattr(old_value, "smartHome_BooleanCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_BooleanCondition"):
                opp_val = getattr(value, "smartHome_BooleanCondition", None)
                setattr(value, "smartHome_BooleanCondition", self)

class smartHome_IntegerSensor(Sensor):

    def __init__(self, value: int, smartHome_IntegerSensor: "smartHome_IntegerCondition" = None):
        self.value = value
        self.smartHome_IntegerSensor = smartHome_IntegerSensor
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def smartHome_IntegerSensor(self):
        return self.__smartHome_IntegerSensor

    @smartHome_IntegerSensor.setter
    def smartHome_IntegerSensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_IntegerSensor__smartHome_IntegerSensor", None)
        self.__smartHome_IntegerSensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_IntegerCondition"):
                opp_val = getattr(old_value, "smartHome_IntegerCondition", None)
                if opp_val == self:
                    setattr(old_value, "smartHome_IntegerCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_IntegerCondition"):
                opp_val = getattr(value, "smartHome_IntegerCondition", None)
                setattr(value, "smartHome_IntegerCondition", self)

class smartHome_SensorType:

    def __init__(self, name: str, smartHome_SensorType: "smartHome_Sensor" = None, smartHome_SensorType7: "smartHome_SmartHome" = None):
        self.name = name
        self.smartHome_SensorType = smartHome_SensorType
        self.smartHome_SensorType7 = smartHome_SensorType7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smartHome_SensorType7(self):
        return self.__smartHome_SensorType7

    @smartHome_SensorType7.setter
    def smartHome_SensorType7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_SensorType__smartHome_SensorType7", None)
        self.__smartHome_SensorType7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_SmartHome6"):
                opp_val = getattr(old_value, "smartHome_SmartHome6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_SmartHome6"):
                opp_val = getattr(value, "smartHome_SmartHome6", None)
                if opp_val is None:
                    setattr(value, "smartHome_SmartHome6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smartHome_SensorType(self):
        return self.__smartHome_SensorType

    @smartHome_SensorType.setter
    def smartHome_SensorType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_SensorType__smartHome_SensorType", None)
        self.__smartHome_SensorType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_Sensor"):
                opp_val = getattr(old_value, "smartHome_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "smartHome_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_Sensor"):
                opp_val = getattr(value, "smartHome_Sensor", None)
                setattr(value, "smartHome_Sensor", self)

class smartHome_Sensor(ABC):

    def __init__(self, dataFile: str, name: str, smartHome_Sensor: "smartHome_SensorType" = None, smartHome_Sensor2: "smartHome_Location" = None):
        self.dataFile = dataFile
        self.name = name
        self.smartHome_Sensor = smartHome_Sensor
        self.smartHome_Sensor2 = smartHome_Sensor2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dataFile(self) -> str:
        return self.__dataFile

    @dataFile.setter
    def dataFile(self, dataFile: str):
        self.__dataFile = dataFile

    @property
    def smartHome_Sensor2(self):
        return self.__smartHome_Sensor2

    @smartHome_Sensor2.setter
    def smartHome_Sensor2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_Sensor__smartHome_Sensor2", None)
        self.__smartHome_Sensor2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_Location"):
                opp_val = getattr(old_value, "smartHome_Location", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_Location"):
                opp_val = getattr(value, "smartHome_Location", None)
                if opp_val is None:
                    setattr(value, "smartHome_Location", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smartHome_Sensor(self):
        return self.__smartHome_Sensor

    @smartHome_Sensor.setter
    def smartHome_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_Sensor__smartHome_Sensor", None)
        self.__smartHome_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_SensorType"):
                opp_val = getattr(old_value, "smartHome_SensorType", None)
                if opp_val == self:
                    setattr(old_value, "smartHome_SensorType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_SensorType"):
                opp_val = getattr(value, "smartHome_SensorType", None)
                setattr(value, "smartHome_SensorType", self)
