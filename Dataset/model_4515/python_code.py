from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Activity(Enum):
    standing = "standing"
    laying = "laying"
    sitting = "sitting"
class Precision(Enum):
    ms = "ms"
    s = "s"
    m = "m"
class Operator(Enum):
    superior = "superior"
    inferior = "inferior"
    equal = "equal"


############################################
# Definition of Classes
############################################

class smarthome_Mode:

    pass
class smarthome_Duration:

    def __init__(self, time: int, precision: str, smarthome_Duration: "smarthome_Rule" = None):
        self.time = time
        self.precision = precision
        self.smarthome_Duration = smarthome_Duration
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

    @property
    def smarthome_Duration(self):
        return self.__smarthome_Duration

    @smarthome_Duration.setter
    def smarthome_Duration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Duration__smarthome_Duration", None)
        self.__smarthome_Duration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_Rule14"):
                opp_val = getattr(old_value, "smarthome_Rule14", None)
                if opp_val == self:
                    setattr(old_value, "smarthome_Rule14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_Rule14"):
                opp_val = getattr(value, "smarthome_Rule14", None)
                setattr(value, "smarthome_Rule14", self)

class smarthome_Predicate(ABC):

    pass
class smarthome_Rule:

    pass
class smarthome_CSVSensor:

    def __init__(self, file: str):
        self.file = file
        
    @property
    def file(self) -> str:
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file

class Sensor:

    pass
class smarthome_DigitalSensor(Sensor):

    pass
class smarthome_AnalogSensor(Sensor):

    pass
class Predicate:

    pass
class smarthome_PersonPredicate(Predicate):

    def __init__(self, activity: str, smarthome_PersonPredicate: "smarthome_Person" = None):
        self.activity = activity
        self.smarthome_PersonPredicate = smarthome_PersonPredicate
        
    @property
    def activity(self) -> str:
        return self.__activity

    @activity.setter
    def activity(self, activity: str):
        self.__activity = activity

    @property
    def smarthome_PersonPredicate(self):
        return self.__smarthome_PersonPredicate

    @smarthome_PersonPredicate.setter
    def smarthome_PersonPredicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_PersonPredicate__smarthome_PersonPredicate", None)
        self.__smarthome_PersonPredicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_Person29"):
                opp_val = getattr(old_value, "smarthome_Person29", None)
                if opp_val == self:
                    setattr(old_value, "smarthome_Person29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_Person29"):
                opp_val = getattr(value, "smarthome_Person29", None)
                setattr(value, "smarthome_Person29", self)

class smarthome_SensorPredicate(Predicate):

    def __init__(self, operator: str, value: float, smarthome_SensorPredicate: "smarthome_Sensor" = None):
        self.operator = operator
        self.value = value
        self.smarthome_SensorPredicate = smarthome_SensorPredicate
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def smarthome_SensorPredicate(self):
        return self.__smarthome_SensorPredicate

    @smarthome_SensorPredicate.setter
    def smarthome_SensorPredicate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_SensorPredicate__smarthome_SensorPredicate", None)
        self.__smarthome_SensorPredicate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_Sensor27"):
                opp_val = getattr(old_value, "smarthome_Sensor27", None)
                if opp_val == self:
                    setattr(old_value, "smarthome_Sensor27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_Sensor27"):
                opp_val = getattr(value, "smarthome_Sensor27", None)
                setattr(value, "smarthome_Sensor27", self)

class smarthome_Home:

    def __init__(self, fileEvents: str, smarthome_Home2: set["smarthome_Person"] = None, smarthome_Home4: set["smarthome_Pattern"] = None, smarthome_Home6: set["smarthome_NamedEntity"] = None, smarthome_Home: set["smarthome_Room"] = None):
        self.fileEvents = fileEvents
        self.smarthome_Home2 = smarthome_Home2 if smarthome_Home2 is not None else set()
        self.smarthome_Home4 = smarthome_Home4 if smarthome_Home4 is not None else set()
        self.smarthome_Home6 = smarthome_Home6 if smarthome_Home6 is not None else set()
        self.smarthome_Home = smarthome_Home if smarthome_Home is not None else set()
        
    @property
    def fileEvents(self) -> str:
        return self.__fileEvents

    @fileEvents.setter
    def fileEvents(self, fileEvents: str):
        self.__fileEvents = fileEvents

    @property
    def smarthome_Home(self):
        return self.__smarthome_Home

    @smarthome_Home.setter
    def smarthome_Home(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Home__smarthome_Home", None)
        self.__smarthome_Home = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smarthome_Room"):
                    opp_val = getattr(item, "smarthome_Room", None)
                    
                    if opp_val == self:
                        setattr(item, "smarthome_Room", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smarthome_Room"):
                    opp_val = getattr(item, "smarthome_Room", None)
                    
                    setattr(item, "smarthome_Room", self)
                    

    @property
    def smarthome_Home2(self):
        return self.__smarthome_Home2

    @smarthome_Home2.setter
    def smarthome_Home2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Home__smarthome_Home2", None)
        self.__smarthome_Home2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smarthome_Person"):
                    opp_val = getattr(item, "smarthome_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "smarthome_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smarthome_Person"):
                    opp_val = getattr(item, "smarthome_Person", None)
                    
                    setattr(item, "smarthome_Person", self)
                    

    @property
    def smarthome_Home6(self):
        return self.__smarthome_Home6

    @smarthome_Home6.setter
    def smarthome_Home6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Home__smarthome_Home6", None)
        self.__smarthome_Home6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smarthome_NamedEntity"):
                    opp_val = getattr(item, "smarthome_NamedEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "smarthome_NamedEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smarthome_NamedEntity"):
                    opp_val = getattr(item, "smarthome_NamedEntity", None)
                    
                    setattr(item, "smarthome_NamedEntity", self)
                    

    @property
    def smarthome_Home4(self):
        return self.__smarthome_Home4

    @smarthome_Home4.setter
    def smarthome_Home4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_Home__smarthome_Home4", None)
        self.__smarthome_Home4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smarthome_Pattern"):
                    opp_val = getattr(item, "smarthome_Pattern", None)
                    
                    if opp_val == self:
                        setattr(item, "smarthome_Pattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smarthome_Pattern"):
                    opp_val = getattr(item, "smarthome_Pattern", None)
                    
                    setattr(item, "smarthome_Pattern", self)
                    

class NamedEntity:

    pass
class smarthome_Room(NamedEntity):

    pass
class smarthome_Tag(NamedEntity):

    pass
class smarthome_Sensor(NamedEntity):

    pass
class smarthome_NamedEntity(ABC):

    def __init__(self, name: str, smarthome_NamedEntity: "smarthome_Home" = None):
        self.name = name
        self.smarthome_NamedEntity = smarthome_NamedEntity
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smarthome_NamedEntity(self):
        return self.__smarthome_NamedEntity

    @smarthome_NamedEntity.setter
    def smarthome_NamedEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smarthome_NamedEntity__smarthome_NamedEntity", None)
        self.__smarthome_NamedEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smarthome_Home6"):
                opp_val = getattr(old_value, "smarthome_Home6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smarthome_Home6"):
                opp_val = getattr(value, "smarthome_Home6", None)
                if opp_val is None:
                    setattr(value, "smarthome_Home6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smarthome_Pattern(NamedEntity):

    pass
class smarthome_Person(NamedEntity):

    pass