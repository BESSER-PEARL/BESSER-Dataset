from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Signal(Enum):
    HIGH = "HIGH"
    LOW = "LOW"


############################################
# Definition of Classes
############################################

class arduinoML_Transition:

    def __init__(self, value: str, arduinoML_Transition: "arduinoML_State" = None, arduinoML_Transition14: "arduinoML_Sensor" = None, transition: "arduinoML_State" = None, Transition: "arduinoML_State" = None):
        self.value = value
        self.arduinoML_Transition = arduinoML_Transition
        self.arduinoML_Transition14 = arduinoML_Transition14
        self.transition = transition
        self.Transition = Transition
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def arduinoML_Transition14(self):
        return self.__arduinoML_Transition14

    @arduinoML_Transition14.setter
    def arduinoML_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Transition__arduinoML_Transition14", None)
        self.__arduinoML_Transition14 = value
        
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

    @property
    def arduinoML_Transition(self):
        return self.__arduinoML_Transition

    @arduinoML_Transition.setter
    def arduinoML_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Transition__arduinoML_Transition", None)
        self.__arduinoML_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_State12"):
                opp_val = getattr(old_value, "arduinoML_State12", None)
                if opp_val == self:
                    setattr(old_value, "arduinoML_State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_State12"):
                opp_val = getattr(value, "arduinoML_State12", None)
                setattr(value, "arduinoML_State12", self)

    @property
    def transition(self):
        return self.__transition

    @transition.setter
    def transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Transition__transition", None)
        self.__transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state"):
                opp_val = getattr(old_value, "state", None)
                if opp_val == self:
                    setattr(old_value, "state", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state"):
                opp_val = getattr(value, "state", None)
                setattr(value, "state", self)

class arduinoML_Action:

    def __init__(self, value: str, arduinoML_Action10: "arduinoML_Actuator" = None, arduinoML_Action: "arduinoML_State" = None):
        self.value = value
        self.arduinoML_Action10 = arduinoML_Action10
        self.arduinoML_Action = arduinoML_Action
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def arduinoML_Action10(self):
        return self.__arduinoML_Action10

    @arduinoML_Action10.setter
    def arduinoML_Action10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Action__arduinoML_Action10", None)
        self.__arduinoML_Action10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_Actuator"):
                opp_val = getattr(old_value, "arduinoML_Actuator", None)
                if opp_val == self:
                    setattr(old_value, "arduinoML_Actuator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_Actuator"):
                opp_val = getattr(value, "arduinoML_Actuator", None)
                setattr(value, "arduinoML_Actuator", self)

    @property
    def arduinoML_Action(self):
        return self.__arduinoML_Action

    @arduinoML_Action.setter
    def arduinoML_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Action__arduinoML_Action", None)
        self.__arduinoML_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_State7"):
                opp_val = getattr(old_value, "arduinoML_State7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_State7"):
                opp_val = getattr(value, "arduinoML_State7", None)
                if opp_val is None:
                    setattr(value, "arduinoML_State7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Brick:

    pass
class arduinoML_Actuator(Brick):

    pass
class arduinoML_Sensor(Brick):

    pass
class NamedElement:

    pass
class arduinoML_State(NamedElement):

    pass
class arduinoML_Brick(NamedElement):

    def __init__(self, pin: int, arduinoML_Brick: "arduinoML_App" = None):
        self.pin = pin
        self.arduinoML_Brick = arduinoML_Brick
        
    @property
    def pin(self) -> int:
        return self.__pin

    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

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

class arduinoML_App(NamedElement):

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
