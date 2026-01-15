from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DigitalValue(Enum):
    ON = "ON"
    OFF = "OFF"


############################################
# Definition of Classes
############################################

class arduinoml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class arduinoml_Trigger:

    def __init__(self, value: str, arduinoml_Trigger: "arduinoml_Transition" = None, arduinoml_Trigger17: set["arduinoml_Sensor"] = None):
        self.value = value
        self.arduinoml_Trigger = arduinoml_Trigger
        self.arduinoml_Trigger17 = arduinoml_Trigger17 if arduinoml_Trigger17 is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def arduinoml_Trigger(self):
        return self.__arduinoml_Trigger

    @arduinoml_Trigger.setter
    def arduinoml_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_Trigger__arduinoml_Trigger", None)
        self.__arduinoml_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_Transition12"):
                opp_val = getattr(old_value, "arduinoml_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Transition12"):
                opp_val = getattr(value, "arduinoml_Transition12", None)
                setattr(value, "arduinoml_Transition12", self)

    @property
    def arduinoml_Trigger17(self):
        return self.__arduinoml_Trigger17

    @arduinoml_Trigger17.setter
    def arduinoml_Trigger17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_Trigger__arduinoml_Trigger17", None)
        self.__arduinoml_Trigger17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoml_Sensor"):
                    opp_val = getattr(item, "arduinoml_Sensor", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoml_Sensor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoml_Sensor"):
                    opp_val = getattr(item, "arduinoml_Sensor", None)
                    
                    setattr(item, "arduinoml_Sensor", self)
                    

class Brick:

    pass
class arduinoml_Actuator(Brick):

    pass
class arduinoml_Sensor(Brick):

    pass
class arduinoml_Action(ABC):

    pass
class NamedElement:

    pass
class arduinoml_Transition(NamedElement):

    pass
class arduinoml_Brick(NamedElement):

    def __init__(self, pin: int, arduinoml_Brick: "arduinoml_Board" = None):
        self.pin = pin
        self.arduinoml_Brick = arduinoml_Brick
        
    @property
    def pin(self) -> int:
        return self.__pin

    @pin.setter
    def pin(self, pin: int):
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
            if hasattr(old_value, "arduinoml_Board5"):
                opp_val = getattr(old_value, "arduinoml_Board5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_Board5"):
                opp_val = getattr(value, "arduinoml_Board5", None)
                if opp_val is None:
                    setattr(value, "arduinoml_Board5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduinoml_State(NamedElement):

    pass
class arduinoml_Board:

    pass
class Action:

    pass
class arduinoml_On(Action):

    pass
class arduinoml_Wait(Action):

    def __init__(self, waitingTime: int):
        self.waitingTime = waitingTime
        
    @property
    def waitingTime(self) -> int:
        return self.__waitingTime

    @waitingTime.setter
    def waitingTime(self, waitingTime: int):
        self.__waitingTime = waitingTime

class arduinoml_Off(Action):

    pass