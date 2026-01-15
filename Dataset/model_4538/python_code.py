from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    superior = "superior"
    inferior = "inferior"
    equal = "equal"
    different = "different"


############################################
# Definition of Classes
############################################

class Activator:

    pass
class Sensor:

    pass
class IotComponent:

    pass
class SmartHome_Activator(IotComponent):

    def __init__(self):
        
    def activate(self) -> str:
        # TODO: Implement activate method
        pass

class SmartHome_Sensor(IotComponent):

    pass
class SmartHome_Clock(Sensor):

    pass
class Value:

    pass
class SmartHome_AnalValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class SmartHome_DigitValue(Value):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class SmartHome_Value(ABC):

    pass
class SmartHome_RuleComposant:

    def __init__(self, operator: str, SmartHome_RuleComposant: "SmartHome_Rule" = None, SmartHome_RuleComposant20: "SmartHome_Rule" = None, SmartHome_RuleComposant22: "SmartHome_Value" = None, SmartHome_RuleComposant24: "SmartHome_IotComponent" = None):
        self.operator = operator
        self.SmartHome_RuleComposant = SmartHome_RuleComposant
        self.SmartHome_RuleComposant20 = SmartHome_RuleComposant20
        self.SmartHome_RuleComposant22 = SmartHome_RuleComposant22
        self.SmartHome_RuleComposant24 = SmartHome_RuleComposant24
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def SmartHome_RuleComposant22(self):
        return self.__SmartHome_RuleComposant22

    @SmartHome_RuleComposant22.setter
    def SmartHome_RuleComposant22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHome_RuleComposant__SmartHome_RuleComposant22", None)
        self.__SmartHome_RuleComposant22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHome_Value"):
                opp_val = getattr(old_value, "SmartHome_Value", None)
                if opp_val == self:
                    setattr(old_value, "SmartHome_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHome_Value"):
                opp_val = getattr(value, "SmartHome_Value", None)
                setattr(value, "SmartHome_Value", self)

    @property
    def SmartHome_RuleComposant20(self):
        return self.__SmartHome_RuleComposant20

    @SmartHome_RuleComposant20.setter
    def SmartHome_RuleComposant20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHome_RuleComposant__SmartHome_RuleComposant20", None)
        self.__SmartHome_RuleComposant20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHome_Rule19"):
                opp_val = getattr(old_value, "SmartHome_Rule19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHome_Rule19"):
                opp_val = getattr(value, "SmartHome_Rule19", None)
                if opp_val is None:
                    setattr(value, "SmartHome_Rule19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SmartHome_RuleComposant24(self):
        return self.__SmartHome_RuleComposant24

    @SmartHome_RuleComposant24.setter
    def SmartHome_RuleComposant24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHome_RuleComposant__SmartHome_RuleComposant24", None)
        self.__SmartHome_RuleComposant24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHome_IotComponent"):
                opp_val = getattr(old_value, "SmartHome_IotComponent", None)
                if opp_val == self:
                    setattr(old_value, "SmartHome_IotComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHome_IotComponent"):
                opp_val = getattr(value, "SmartHome_IotComponent", None)
                setattr(value, "SmartHome_IotComponent", self)

    @property
    def SmartHome_RuleComposant(self):
        return self.__SmartHome_RuleComposant

    @SmartHome_RuleComposant.setter
    def SmartHome_RuleComposant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHome_RuleComposant__SmartHome_RuleComposant", None)
        self.__SmartHome_RuleComposant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHome_Rule17"):
                opp_val = getattr(old_value, "SmartHome_Rule17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHome_Rule17"):
                opp_val = getattr(value, "SmartHome_Rule17", None)
                if opp_val is None:
                    setattr(value, "SmartHome_Rule17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SmartHome_Shutter(Activator):

    def __init__(self, stateInit: bool, SmartHome_Shutter: "SmartHome_Room" = None):
        self.stateInit = stateInit
        self.SmartHome_Shutter = SmartHome_Shutter
        
    @property
    def stateInit(self) -> bool:
        return self.__stateInit

    @stateInit.setter
    def stateInit(self, stateInit: bool):
        self.__stateInit = stateInit

    @property
    def SmartHome_Shutter(self):
        return self.__SmartHome_Shutter

    @SmartHome_Shutter.setter
    def SmartHome_Shutter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHome_Shutter__SmartHome_Shutter", None)
        self.__SmartHome_Shutter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHome_Room6"):
                opp_val = getattr(old_value, "SmartHome_Room6", None)
                if opp_val == self:
                    setattr(old_value, "SmartHome_Room6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHome_Room6"):
                opp_val = getattr(value, "SmartHome_Room6", None)
                setattr(value, "SmartHome_Room6", self)

class SmartHome_Light(Activator):

    def __init__(self, intensity: float, stateInit: bool, SmartHome_Light: "SmartHome_Room" = None):
        self.intensity = intensity
        self.stateInit = stateInit
        self.SmartHome_Light = SmartHome_Light
        
    @property
    def intensity(self) -> float:
        return self.__intensity

    @intensity.setter
    def intensity(self, intensity: float):
        self.__intensity = intensity

    @property
    def stateInit(self) -> bool:
        return self.__stateInit

    @stateInit.setter
    def stateInit(self, stateInit: bool):
        self.__stateInit = stateInit

    @property
    def SmartHome_Light(self):
        return self.__SmartHome_Light

    @SmartHome_Light.setter
    def SmartHome_Light(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHome_Light__SmartHome_Light", None)
        self.__SmartHome_Light = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHome_Room2"):
                opp_val = getattr(old_value, "SmartHome_Room2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHome_Room2"):
                opp_val = getattr(value, "SmartHome_Room2", None)
                if opp_val is None:
                    setattr(value, "SmartHome_Room2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SmartHome_LightSensor(Sensor):

    pass
class NamedElement:

    pass
class SmartHome_Rule(NamedElement):

    pass
class SmartHome_IotComponent(NamedElement):

    pass
class SmartHome_PhysicalContext(NamedElement):

    def __init__(self, lightIn: float, lightOut: float, SmartHome_PhysicalContext: "SmartHome_Room" = None):
        self.lightIn = lightIn
        self.lightOut = lightOut
        self.SmartHome_PhysicalContext = SmartHome_PhysicalContext
        
    @property
    def lightOut(self) -> float:
        return self.__lightOut

    @lightOut.setter
    def lightOut(self, lightOut: float):
        self.__lightOut = lightOut

    @property
    def lightIn(self) -> float:
        return self.__lightIn

    @lightIn.setter
    def lightIn(self, lightIn: float):
        self.__lightIn = lightIn

    @property
    def SmartHome_PhysicalContext(self):
        return self.__SmartHome_PhysicalContext

    @SmartHome_PhysicalContext.setter
    def SmartHome_PhysicalContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHome_PhysicalContext__SmartHome_PhysicalContext", None)
        self.__SmartHome_PhysicalContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmartHome_Room4"):
                opp_val = getattr(old_value, "SmartHome_Room4", None)
                if opp_val == self:
                    setattr(old_value, "SmartHome_Room4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmartHome_Room4"):
                opp_val = getattr(value, "SmartHome_Room4", None)
                setattr(value, "SmartHome_Room4", self)

class SmartHome_Home(NamedElement):

    def __init__(self, startDay: float, speed: float, SmartHome_Home: set["SmartHome_Room"] = None, SmartHome_Home14: set["SmartHome_Rule"] = None):
        self.startDay = startDay
        self.speed = speed
        self.SmartHome_Home = SmartHome_Home if SmartHome_Home is not None else set()
        self.SmartHome_Home14 = SmartHome_Home14 if SmartHome_Home14 is not None else set()
        
    @property
    def startDay(self) -> float:
        return self.__startDay

    @startDay.setter
    def startDay(self, startDay: float):
        self.__startDay = startDay

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, speed: float):
        self.__speed = speed

    @property
    def SmartHome_Home14(self):
        return self.__SmartHome_Home14

    @SmartHome_Home14.setter
    def SmartHome_Home14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHome_Home__SmartHome_Home14", None)
        self.__SmartHome_Home14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartHome_Rule15"):
                    opp_val = getattr(item, "SmartHome_Rule15", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartHome_Rule15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartHome_Rule15"):
                    opp_val = getattr(item, "SmartHome_Rule15", None)
                    
                    setattr(item, "SmartHome_Rule15", self)
                    

    @property
    def SmartHome_Home(self):
        return self.__SmartHome_Home

    @SmartHome_Home.setter
    def SmartHome_Home(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SmartHome_Home__SmartHome_Home", None)
        self.__SmartHome_Home = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmartHome_Room12"):
                    opp_val = getattr(item, "SmartHome_Room12", None)
                    
                    if opp_val == self:
                        setattr(item, "SmartHome_Room12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmartHome_Room12"):
                    opp_val = getattr(item, "SmartHome_Room12", None)
                    
                    setattr(item, "SmartHome_Room12", self)
                    

class SmartHome_Room(NamedElement):

    pass
class SmartHome_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
