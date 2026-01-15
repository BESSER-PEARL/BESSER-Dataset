from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    INFERIOR = "INFERIOR"
    SUPERIOR = "SUPERIOR"
    EQUALS = "EQUALS"
class DurationUnit(Enum):
    MINUTE = "MINUTE"
    SECOND = "SECOND"


############################################
# Definition of Classes
############################################

class smartHome_SensorValue:

    pass
class smartHome_Location:

    def __init__(self, name: str, smartHome_Location4: "smartHome_SmartHome" = None, smartHome_Location: set["smartHome_Sensor"] = None):
        self.name = name
        self.smartHome_Location4 = smartHome_Location4
        self.smartHome_Location = smartHome_Location if smartHome_Location is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

class smartHome_SensorType:

    def __init__(self, name: str, smartHome_SensorType7: "smartHome_SmartHome" = None, smartHome_SensorType: "smartHome_Sensor" = None):
        self.name = name
        self.smartHome_SensorType7 = smartHome_SensorType7
        self.smartHome_SensorType = smartHome_SensorType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class smartHome_Sensor:

    def __init__(self, dataFile: str, name: str, value: int, smartHome_Sensor18: "smartHome_Condition" = None, smartHome_Sensor: "smartHome_SensorType" = None, smartHome_Sensor2: "smartHome_Location" = None):
        self.dataFile = dataFile
        self.name = name
        self.value = value
        self.smartHome_Sensor18 = smartHome_Sensor18
        self.smartHome_Sensor = smartHome_Sensor
        self.smartHome_Sensor2 = smartHome_Sensor2
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

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
    def smartHome_Sensor18(self):
        return self.__smartHome_Sensor18

    @smartHome_Sensor18.setter
    def smartHome_Sensor18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_Sensor__smartHome_Sensor18", None)
        self.__smartHome_Sensor18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_Condition17"):
                opp_val = getattr(old_value, "smartHome_Condition17", None)
                if opp_val == self:
                    setattr(old_value, "smartHome_Condition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_Condition17"):
                opp_val = getattr(value, "smartHome_Condition17", None)
                setattr(value, "smartHome_Condition17", self)

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

class smartHome_Condition:

    def __init__(self, operand: int, operator: str, smartHome_Condition: "smartHome_Rule" = None, smartHome_Condition17: "smartHome_Sensor" = None):
        self.operand = operand
        self.operator = operator
        self.smartHome_Condition = smartHome_Condition
        self.smartHome_Condition17 = smartHome_Condition17
        
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
    def smartHome_Condition(self):
        return self.__smartHome_Condition

    @smartHome_Condition.setter
    def smartHome_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_Condition__smartHome_Condition", None)
        self.__smartHome_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_Rule11"):
                opp_val = getattr(old_value, "smartHome_Rule11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_Rule11"):
                opp_val = getattr(value, "smartHome_Rule11", None)
                if opp_val is None:
                    setattr(value, "smartHome_Rule11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smartHome_Condition17(self):
        return self.__smartHome_Condition17

    @smartHome_Condition17.setter
    def smartHome_Condition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smartHome_Condition__smartHome_Condition17", None)
        self.__smartHome_Condition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smartHome_Sensor18"):
                opp_val = getattr(old_value, "smartHome_Sensor18", None)
                if opp_val == self:
                    setattr(old_value, "smartHome_Sensor18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smartHome_Sensor18"):
                opp_val = getattr(value, "smartHome_Sensor18", None)
                setattr(value, "smartHome_Sensor18", self)

class smartHome_Rule:

    pass
class smartHome_SmartHome:

    pass