from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BrickType(Enum):
    DIGITAL = "DIGITAL"
    ANALOGICAL = "ANALOGICAL"
class COMPARATOR(Enum):
    EQUALS = "EQUALS"
    NON_EQUALS = "NON_EQUALS"
    SUPERIOR = "SUPERIOR"
    INFERIOR = "INFERIOR"
    SUPERIOR_OR_EQUALS = "SUPERIOR_OR_EQUALS"
    INFERIOR_OR_EQUALS = "INFERIOR_OR_EQUALS"
class OPERATOR(Enum):
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class Condition:

    pass
class arduinoml_MultipleCondition(Condition):

    def __init__(self, operators: str, arduinoml_MultipleCondition: set["arduinoml_SimpleCondition"] = None):
        self.operators = operators
        self.arduinoml_MultipleCondition = arduinoml_MultipleCondition if arduinoml_MultipleCondition is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def arduinoml_MultipleCondition(self):
        return self.__arduinoml_MultipleCondition

    @arduinoml_MultipleCondition.setter
    def arduinoml_MultipleCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_MultipleCondition__arduinoml_MultipleCondition", None)
        self.__arduinoml_MultipleCondition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoml_SimpleCondition25"):
                    opp_val = getattr(item, "arduinoml_SimpleCondition25", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoml_SimpleCondition25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoml_SimpleCondition25"):
                    opp_val = getattr(item, "arduinoml_SimpleCondition25", None)
                    
                    setattr(item, "arduinoml_SimpleCondition25", self)
                    

class arduinoml_SimpleCondition(Condition):

    def __init__(self, value: str, comparator: str, arduinoml_SimpleCondition: "arduinoml_Sensor" = None, arduinoml_SimpleCondition25: "arduinoml_MultipleCondition" = None):
        self.value = value
        self.comparator = comparator
        self.arduinoml_SimpleCondition = arduinoml_SimpleCondition
        self.arduinoml_SimpleCondition25 = arduinoml_SimpleCondition25
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def comparator(self) -> str:
        return self.__comparator

    @comparator.setter
    def comparator(self, comparator: str):
        self.__comparator = comparator

    @property
    def arduinoml_SimpleCondition25(self):
        return self.__arduinoml_SimpleCondition25

    @arduinoml_SimpleCondition25.setter
    def arduinoml_SimpleCondition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_SimpleCondition__arduinoml_SimpleCondition25", None)
        self.__arduinoml_SimpleCondition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_MultipleCondition"):
                opp_val = getattr(old_value, "arduinoml_MultipleCondition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_MultipleCondition"):
                opp_val = getattr(value, "arduinoml_MultipleCondition", None)
                if opp_val is None:
                    setattr(value, "arduinoml_MultipleCondition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduinoml_SimpleCondition(self):
        return self.__arduinoml_SimpleCondition

    @arduinoml_SimpleCondition.setter
    def arduinoml_SimpleCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_SimpleCondition__arduinoml_SimpleCondition", None)
        self.__arduinoml_SimpleCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Sensor"):
                opp_val = getattr(old_value, "arduinoml_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Sensor"):
                opp_val = getattr(value, "arduinoml_Sensor", None)
                setattr(value, "arduinoml_Sensor", self)

class NamedElement:

    pass
class arduinoml_Action(NamedElement):

    def __init__(self, value: str, arduinoml_Action22: "arduinoml_Actuator" = None, arduinoml_Action: "arduinoml_State" = None):
        self.value = value
        self.arduinoml_Action22 = arduinoml_Action22
        self.arduinoml_Action = arduinoml_Action
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def arduinoml_Action(self):
        return self.__arduinoml_Action

    @arduinoml_Action.setter
    def arduinoml_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_Action__arduinoml_Action", None)
        self.__arduinoml_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_State17"):
                opp_val = getattr(old_value, "arduinoml_State17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_State17"):
                opp_val = getattr(value, "arduinoml_State17", None)
                if opp_val is None:
                    setattr(value, "arduinoml_State17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduinoml_Action22(self):
        return self.__arduinoml_Action22

    @arduinoml_Action22.setter
    def arduinoml_Action22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_Action__arduinoml_Action22", None)
        self.__arduinoml_Action22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Actuator"):
                opp_val = getattr(old_value, "arduinoml_Actuator", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_Actuator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Actuator"):
                opp_val = getattr(value, "arduinoml_Actuator", None)
                setattr(value, "arduinoml_Actuator", self)

class arduinoml_Brick(NamedElement):

    def __init__(self, pin: int, type: str, arduinoml_Brick: "arduinoml_App" = None):
        self.pin = pin
        self.type = type
        self.arduinoml_Brick = arduinoml_Brick
        
    @property
    def pin(self) -> int:
        return self.__pin

    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
            if hasattr(old_value, "arduinoml_App"):
                opp_val = getattr(old_value, "arduinoml_App", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_App"):
                opp_val = getattr(value, "arduinoml_App", None)
                if opp_val is None:
                    setattr(value, "arduinoml_App", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class Brick:

    pass
class arduinoml_Actuator(Brick):

    pass
class arduinoml_Sensor(Brick):

    pass
class arduinoml_Transition:

    pass
class arduinoml_Condition(NamedElement):

    pass
class arduinoml_State(NamedElement):

    pass