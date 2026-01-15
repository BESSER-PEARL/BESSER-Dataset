from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    AND = "AND"
    OR = "OR"
    NONE = "NONE"
class DigitalSignalEnum(Enum):
    HIGH = "HIGH"
    LOW = "LOW"


############################################
# Definition of Classes
############################################

class Sensor:

    pass
class arduinoML_KeyboardSensor(Sensor):

    pass
class Signal:

    pass
class arduinoML_StringSignal(Signal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class arduinoML_DigitalSignal(Signal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Actuator:

    pass
class arduinoML_LCDScreenActuator(Actuator):

    pass
class arduinoML_Signal(ABC):

    pass
class arduinoML_Transition:

    pass
class arduinoML_Action:

    pass
class arduinoML_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class arduinoML_App:

    def __init__(self, name: str, arduinoML_App: set["arduinoML_Brick"] = None, arduinoML_App2: set["arduinoML_State"] = None, arduinoML_App4: "arduinoML_State" = None):
        self.name = name
        self.arduinoML_App = arduinoML_App if arduinoML_App is not None else set()
        self.arduinoML_App2 = arduinoML_App2 if arduinoML_App2 is not None else set()
        self.arduinoML_App4 = arduinoML_App4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduinoML_App4(self):
        return self.__arduinoML_App4

    @arduinoML_App4.setter
    def arduinoML_App4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_App__arduinoML_App4", None)
        self.__arduinoML_App4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_State5"):
                opp_val = getattr(old_value, "arduinoML_State5", None)
                if opp_val == self:
                    setattr(old_value, "arduinoML_State5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_State5"):
                opp_val = getattr(value, "arduinoML_State5", None)
                setattr(value, "arduinoML_State5", self)

    @property
    def arduinoML_App(self):
        return self.__arduinoML_App

    @arduinoML_App.setter
    def arduinoML_App(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_App__arduinoML_App", None)
        self.__arduinoML_App = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoML_Brick"):
                    opp_val = getattr(item, "arduinoML_Brick", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoML_Brick", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoML_Brick"):
                    opp_val = getattr(item, "arduinoML_Brick", None)
                    
                    setattr(item, "arduinoML_Brick", self)
                    

    @property
    def arduinoML_App2(self):
        return self.__arduinoML_App2

    @arduinoML_App2.setter
    def arduinoML_App2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_App__arduinoML_App2", None)
        self.__arduinoML_App2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoML_State"):
                    opp_val = getattr(item, "arduinoML_State", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoML_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoML_State"):
                    opp_val = getattr(item, "arduinoML_State", None)
                    
                    setattr(item, "arduinoML_State", self)
                    

class Brick:

    pass
class arduinoML_Sensor(Brick):

    pass
class arduinoML_Actuator(Brick):

    pass
class NamedElement:

    pass
class arduinoML_Condition(NamedElement):

    def __init__(self, operator: str, arduinoML_Condition22: "arduinoML_Signal" = None, arduinoML_Condition: "arduinoML_Transition" = None, arduinoML_Condition20: "arduinoML_Sensor" = None):
        self.operator = operator
        self.arduinoML_Condition22 = arduinoML_Condition22
        self.arduinoML_Condition = arduinoML_Condition
        self.arduinoML_Condition20 = arduinoML_Condition20
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def arduinoML_Condition22(self):
        return self.__arduinoML_Condition22

    @arduinoML_Condition22.setter
    def arduinoML_Condition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Condition__arduinoML_Condition22", None)
        self.__arduinoML_Condition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_Signal23"):
                opp_val = getattr(old_value, "arduinoML_Signal23", None)
                if opp_val == self:
                    setattr(old_value, "arduinoML_Signal23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_Signal23"):
                opp_val = getattr(value, "arduinoML_Signal23", None)
                setattr(value, "arduinoML_Signal23", self)

    @property
    def arduinoML_Condition(self):
        return self.__arduinoML_Condition

    @arduinoML_Condition.setter
    def arduinoML_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Condition__arduinoML_Condition", None)
        self.__arduinoML_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_Transition18"):
                opp_val = getattr(old_value, "arduinoML_Transition18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_Transition18"):
                opp_val = getattr(value, "arduinoML_Transition18", None)
                if opp_val is None:
                    setattr(value, "arduinoML_Transition18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduinoML_Condition20(self):
        return self.__arduinoML_Condition20

    @arduinoML_Condition20.setter
    def arduinoML_Condition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Condition__arduinoML_Condition20", None)
        self.__arduinoML_Condition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_Sensor"):
                opp_val = getattr(old_value, "arduinoML_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "arduinoML_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_Sensor"):
                opp_val = getattr(value, "arduinoML_Sensor", None)
                setattr(value, "arduinoML_Sensor", self)

class arduinoML_State(NamedElement):

    pass
class arduinoML_Brick(NamedElement):

    def __init__(self, pins: int, arduinoML_Brick: "arduinoML_App" = None):
        self.pins = pins
        self.arduinoML_Brick = arduinoML_Brick
        
    @property
    def pins(self) -> int:
        return self.__pins

    @pins.setter
    def pins(self, pins: int):
        self.__pins = pins

    @property
    def arduinoML_Brick(self):
        return self.__arduinoML_Brick

    @arduinoML_Brick.setter
    def arduinoML_Brick(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Brick__arduinoML_Brick", None)
        self.__arduinoML_Brick = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_App"):
                opp_val = getattr(old_value, "arduinoML_App", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_App"):
                opp_val = getattr(value, "arduinoML_App", None)
                if opp_val is None:
                    setattr(value, "arduinoML_App", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
