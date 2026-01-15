from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SIGNAL(Enum):
    HIGH = "HIGH"
    LOW = "LOW"
class COMPARATOR(Enum):
    SUPERIOR = "SUPERIOR"
    INFERIOR = "INFERIOR"
    EQUAL = "EQUAL"
class OPERATOR(Enum):
    and = "and"
    or = "or"


############################################
# Definition of Classes
############################################

class Action:

    pass
class arduinoml_BinaryAction(Action):

    def __init__(self, actionValue: str):
        self.actionValue = actionValue
        
    @property
    def actionValue(self) -> str:
        return self.__actionValue

    @actionValue.setter
    def actionValue(self, actionValue: str):
        self.__actionValue = actionValue

class arduinoml_AnalogAction(Action):

    def __init__(self, actionValue: int):
        self.actionValue = actionValue
        
    @property
    def actionValue(self) -> int:
        return self.__actionValue

    @actionValue.setter
    def actionValue(self, actionValue: int):
        self.__actionValue = actionValue

class Actuator:

    pass
class arduinoml_BinaryActuator(Actuator):

    pass
class arduinoml_AnalogActuator(Actuator):

    pass
class Sensor:

    pass
class arduinoml_AnalogSensor(Sensor):

    pass
class arduinoml_BinarySensor(Sensor):

    pass
class Condition:

    pass
class arduinoml_ValueElementCondition(Condition):

    def __init__(self, value: float, comparator: str, arduinoml_ValueElementCondition: "arduinoml_AnalogSensor" = None):
        self.value = value
        self.comparator = comparator
        self.arduinoml_ValueElementCondition = arduinoml_ValueElementCondition
        
    @property
    def comparator(self) -> str:
        return self.__comparator

    @comparator.setter
    def comparator(self, comparator: str):
        self.__comparator = comparator

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def arduinoml_ValueElementCondition(self):
        return self.__arduinoml_ValueElementCondition

    @arduinoml_ValueElementCondition.setter
    def arduinoml_ValueElementCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_ValueElementCondition__arduinoml_ValueElementCondition", None)
        self.__arduinoml_ValueElementCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_AnalogSensor"):
                opp_val = getattr(old_value, "arduinoml_AnalogSensor", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_AnalogSensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_AnalogSensor"):
                opp_val = getattr(value, "arduinoml_AnalogSensor", None)
                setattr(value, "arduinoml_AnalogSensor", self)

class arduinoml_SingleElementCondition(Condition):

    def __init__(self, value: str, arduinoml_SingleElementCondition: "arduinoml_BinarySensor" = None):
        self.value = value
        self.arduinoml_SingleElementCondition = arduinoml_SingleElementCondition
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def arduinoml_SingleElementCondition(self):
        return self.__arduinoml_SingleElementCondition

    @arduinoml_SingleElementCondition.setter
    def arduinoml_SingleElementCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_SingleElementCondition__arduinoml_SingleElementCondition", None)
        self.__arduinoml_SingleElementCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_BinarySensor"):
                opp_val = getattr(old_value, "arduinoml_BinarySensor", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_BinarySensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_BinarySensor"):
                opp_val = getattr(value, "arduinoml_BinarySensor", None)
                setattr(value, "arduinoml_BinarySensor", self)

class arduinoml_Condition(ABC):

    pass
class Brick:

    pass
class arduinoml_Sensor(Brick):

    pass
class arduinoml_MultipleElementCondition(Condition):

    def __init__(self, operators: str, arduinoml_MultipleElementCondition: "arduinoml_Transition" = None, arduinoml_MultipleElementCondition19: set["arduinoml_Condition"] = None):
        self.operators = operators
        self.arduinoml_MultipleElementCondition = arduinoml_MultipleElementCondition
        self.arduinoml_MultipleElementCondition19 = arduinoml_MultipleElementCondition19 if arduinoml_MultipleElementCondition19 is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def arduinoml_MultipleElementCondition(self):
        return self.__arduinoml_MultipleElementCondition

    @arduinoml_MultipleElementCondition.setter
    def arduinoml_MultipleElementCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_MultipleElementCondition__arduinoml_MultipleElementCondition", None)
        self.__arduinoml_MultipleElementCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Transition16"):
                opp_val = getattr(old_value, "arduinoml_Transition16", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_Transition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Transition16"):
                opp_val = getattr(value, "arduinoml_Transition16", None)
                setattr(value, "arduinoml_Transition16", self)

    @property
    def arduinoml_MultipleElementCondition19(self):
        return self.__arduinoml_MultipleElementCondition19

    @arduinoml_MultipleElementCondition19.setter
    def arduinoml_MultipleElementCondition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_MultipleElementCondition__arduinoml_MultipleElementCondition19", None)
        self.__arduinoml_MultipleElementCondition19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoml_Condition"):
                    opp_val = getattr(item, "arduinoml_Condition", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoml_Condition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoml_Condition"):
                    opp_val = getattr(item, "arduinoml_Condition", None)
                    
                    setattr(item, "arduinoml_Condition", self)
                    

class arduinoml_Actuator(Brick):

    pass
class arduinoml_Transition:

    pass
class arduinoml_Action(ABC):

    pass
class NamedElement:

    pass
class arduinoml_Brick(NamedElement):

    def __init__(self, pin: str, arduinoml_Brick: "arduinoml_App" = None):
        self.pin = pin
        self.arduinoml_Brick = arduinoml_Brick
        
    @property
    def pin(self) -> str:
        return self.__pin

    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def arduinoml_Brick(self):
        return self.__arduinoml_Brick

    @arduinoml_Brick.setter
    def arduinoml_Brick(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_Brick__arduinoml_Brick", None)
        self.__arduinoml_Brick = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_App2"):
                opp_val = getattr(old_value, "arduinoml_App2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_App2"):
                opp_val = getattr(value, "arduinoml_App2", None)
                if opp_val is None:
                    setattr(value, "arduinoml_App2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduinoml_State(NamedElement):

    pass
class arduinoml_App(NamedElement):

    pass
class arduinoml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
