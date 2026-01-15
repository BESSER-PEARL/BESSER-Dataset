from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EnvironmentConditions(Enum):
    TEMPERATURE = "TEMPERATURE"
    SOUND = "SOUND"
    LIGHT = "LIGHT"
class RelationalOperator(Enum):
    MINOR = "MINOR"
    MINOREQUAL = "MINOREQUAL"
    EQUAL = "EQUAL"
    DIFFERENT = "DIFFERENT"
    MAJOR = "MAJOR"
    MAJOREQUAL = "MAJOREQUAL"
class Actions(Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"


############################################
# Definition of Classes
############################################

class iotsystem_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class iotsystem_Parameter:

    def __init__(self, name: str, value: str, iotsystem_Parameter: "iotsystem_Action" = None):
        self.name = name
        self.value = value
        self.iotsystem_Parameter = iotsystem_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def iotsystem_Parameter(self):
        return self.__iotsystem_Parameter

    @iotsystem_Parameter.setter
    def iotsystem_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotsystem_Parameter__iotsystem_Parameter", None)
        self.__iotsystem_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotsystem_Action10"):
                opp_val = getattr(old_value, "iotsystem_Action10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotsystem_Action10"):
                opp_val = getattr(value, "iotsystem_Action10", None)
                if opp_val is None:
                    setattr(value, "iotsystem_Action10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iotsystem_Condition:

    def __init__(self, expectedValue: float, relationalOperator: str, iotsystem_Condition: "iotsystem_Rule" = None, iotsystem_Condition19: "iotsystem_Sensor" = None):
        self.expectedValue = expectedValue
        self.relationalOperator = relationalOperator
        self.iotsystem_Condition = iotsystem_Condition
        self.iotsystem_Condition19 = iotsystem_Condition19
        
    @property
    def expectedValue(self) -> float:
        return self.__expectedValue

    @expectedValue.setter
    def expectedValue(self, expectedValue: float):
        self.__expectedValue = expectedValue

    @property
    def relationalOperator(self) -> str:
        return self.__relationalOperator

    @relationalOperator.setter
    def relationalOperator(self, relationalOperator: str):
        self.__relationalOperator = relationalOperator

    @property
    def iotsystem_Condition19(self):
        return self.__iotsystem_Condition19

    @iotsystem_Condition19.setter
    def iotsystem_Condition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotsystem_Condition__iotsystem_Condition19", None)
        self.__iotsystem_Condition19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotsystem_Sensor"):
                opp_val = getattr(old_value, "iotsystem_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "iotsystem_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotsystem_Sensor"):
                opp_val = getattr(value, "iotsystem_Sensor", None)
                setattr(value, "iotsystem_Sensor", self)

    @property
    def iotsystem_Condition(self):
        return self.__iotsystem_Condition

    @iotsystem_Condition.setter
    def iotsystem_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotsystem_Condition__iotsystem_Condition", None)
        self.__iotsystem_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotsystem_Rule8"):
                opp_val = getattr(old_value, "iotsystem_Rule8", None)
                if opp_val == self:
                    setattr(old_value, "iotsystem_Rule8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotsystem_Rule8"):
                opp_val = getattr(value, "iotsystem_Rule8", None)
                setattr(value, "iotsystem_Rule8", self)

class iotsystem_Action:

    def __init__(self, action: str, iotsystem_Action: "iotsystem_Rule" = None, iotsystem_Action10: set["iotsystem_Parameter"] = None):
        self.action = action
        self.iotsystem_Action = iotsystem_Action
        self.iotsystem_Action10 = iotsystem_Action10 if iotsystem_Action10 is not None else set()
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def iotsystem_Action(self):
        return self.__iotsystem_Action

    @iotsystem_Action.setter
    def iotsystem_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotsystem_Action__iotsystem_Action", None)
        self.__iotsystem_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotsystem_Rule6"):
                opp_val = getattr(old_value, "iotsystem_Rule6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotsystem_Rule6"):
                opp_val = getattr(value, "iotsystem_Rule6", None)
                if opp_val is None:
                    setattr(value, "iotsystem_Rule6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotsystem_Action10(self):
        return self.__iotsystem_Action10

    @iotsystem_Action10.setter
    def iotsystem_Action10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotsystem_Action__iotsystem_Action10", None)
        self.__iotsystem_Action10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iotsystem_Parameter"):
                    opp_val = getattr(item, "iotsystem_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "iotsystem_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iotsystem_Parameter"):
                    opp_val = getattr(item, "iotsystem_Parameter", None)
                    
                    setattr(item, "iotsystem_Parameter", self)
                    

class iotsystem_Resource:

    def __init__(self, url: str, measurement: str, iotsystem_Resource: "iotsystem_Device" = None, iotsystem_Resource2: "iotsystem_DigitalArtifact" = None):
        self.url = url
        self.measurement = measurement
        self.iotsystem_Resource = iotsystem_Resource
        self.iotsystem_Resource2 = iotsystem_Resource2
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def measurement(self) -> str:
        return self.__measurement

    @measurement.setter
    def measurement(self, measurement: str):
        self.__measurement = measurement

    @property
    def iotsystem_Resource(self):
        return self.__iotsystem_Resource

    @iotsystem_Resource.setter
    def iotsystem_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotsystem_Resource__iotsystem_Resource", None)
        self.__iotsystem_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotsystem_Device"):
                opp_val = getattr(old_value, "iotsystem_Device", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotsystem_Device"):
                opp_val = getattr(value, "iotsystem_Device", None)
                if opp_val is None:
                    setattr(value, "iotsystem_Device", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iotsystem_Resource2(self):
        return self.__iotsystem_Resource2

    @iotsystem_Resource2.setter
    def iotsystem_Resource2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iotsystem_Resource__iotsystem_Resource2", None)
        self.__iotsystem_Resource2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iotsystem_DigitalArtifact"):
                opp_val = getattr(old_value, "iotsystem_DigitalArtifact", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iotsystem_DigitalArtifact"):
                opp_val = getattr(value, "iotsystem_DigitalArtifact", None)
                if opp_val is None:
                    setattr(value, "iotsystem_DigitalArtifact", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class iotsystem_Rule(NamedElement):

    pass
class iotsystem_IotSystem(NamedElement):

    pass
class iotsystem_PhysicalEntity(NamedElement):

    pass
class iotsystem_DigitalArtifact(NamedElement):

    pass
class iotsystem_Device(NamedElement):

    pass
class Device:

    pass
class iotsystem_Sensor(Device):

    pass
class iotsystem_Actuator(Device):

    pass