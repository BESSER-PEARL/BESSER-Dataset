from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TimeComparison(Enum):
    AFTER = "AFTER"
    BEFORE = "BEFORE"
class DigitalState(Enum):
    OFF = "OFF"
    ON = "ON"
class AnalogComparison(Enum):
    GREATER = "GREATER"
    GREATEREQ = "GREATEREQ"
    EQUAL = "EQUAL"
    LOWEREQ = "LOWEREQ"
    LOWER = "LOWER"


############################################
# Definition of Classes
############################################

class AnalogAction:

    pass
class arduinoml_AnalogActionSensor(AnalogAction):

    pass
class arduinoml_AnalogActionValue(AnalogAction):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Action:

    pass
class arduinoml_DigitalAction(Action):

    def __init__(self, dState: str, arduinoml_DigitalAction: "arduinoml_DigitalActuator" = None):
        self.dState = dState
        self.arduinoml_DigitalAction = arduinoml_DigitalAction
        
    @property
    def dState(self) -> str:
        return self.__dState

    @dState.setter
    def dState(self, dState: str):
        self.__dState = dState

    @property
    def arduinoml_DigitalAction(self):
        return self.__arduinoml_DigitalAction

    @arduinoml_DigitalAction.setter
    def arduinoml_DigitalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_DigitalAction__arduinoml_DigitalAction", None)
        self.__arduinoml_DigitalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_DigitalActuator"):
                opp_val = getattr(old_value, "arduinoml_DigitalActuator", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_DigitalActuator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_DigitalActuator"):
                opp_val = getattr(value, "arduinoml_DigitalActuator", None)
                setattr(value, "arduinoml_DigitalActuator", self)

class Condition:

    pass
class arduinoml_DigitalCondition(Condition):

    def __init__(self, dState: str, arduinoml_DigitalCondition: "arduinoml_DigitalSensor" = None):
        self.dState = dState
        self.arduinoml_DigitalCondition = arduinoml_DigitalCondition
        
    @property
    def dState(self) -> str:
        return self.__dState

    @dState.setter
    def dState(self, dState: str):
        self.__dState = dState

    @property
    def arduinoml_DigitalCondition(self):
        return self.__arduinoml_DigitalCondition

    @arduinoml_DigitalCondition.setter
    def arduinoml_DigitalCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_DigitalCondition__arduinoml_DigitalCondition", None)
        self.__arduinoml_DigitalCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_DigitalSensor"):
                opp_val = getattr(old_value, "arduinoml_DigitalSensor", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_DigitalSensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_DigitalSensor"):
                opp_val = getattr(value, "arduinoml_DigitalSensor", None)
                setattr(value, "arduinoml_DigitalSensor", self)

class arduinoml_Condition(ABC):

    pass
class arduinoml_AnalogAction(Action):

    pass
class arduinoml_AnalogCondition(Condition):

    def __init__(self, aComp: str, value: int, arduinoml_AnalogCondition: "arduinoml_AnalogSensor" = None):
        self.aComp = aComp
        self.value = value
        self.arduinoml_AnalogCondition = arduinoml_AnalogCondition
        
    @property
    def aComp(self) -> str:
        return self.__aComp

    @aComp.setter
    def aComp(self, aComp: str):
        self.__aComp = aComp

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def arduinoml_AnalogCondition(self):
        return self.__arduinoml_AnalogCondition

    @arduinoml_AnalogCondition.setter
    def arduinoml_AnalogCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_AnalogCondition__arduinoml_AnalogCondition", None)
        self.__arduinoml_AnalogCondition = value
        
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

class arduinoml_TimeCondition(Condition):

    def __init__(self, time: int, tComp: str):
        self.time = time
        self.tComp = tComp
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def tComp(self) -> str:
        return self.__tComp

    @tComp.setter
    def tComp(self, tComp: str):
        self.__tComp = tComp

class arduinoml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class arduinoml_AMLMachine:

    def __init__(self, frequency: int, arduinoml_AMLMachine2: set["arduinoml_AMLState"] = None, arduinoml_AMLMachine4: "arduinoml_AMLState" = None, arduinoml_AMLMachine: set["arduinoml_Brick"] = None):
        self.frequency = frequency
        self.arduinoml_AMLMachine2 = arduinoml_AMLMachine2 if arduinoml_AMLMachine2 is not None else set()
        self.arduinoml_AMLMachine4 = arduinoml_AMLMachine4
        self.arduinoml_AMLMachine = arduinoml_AMLMachine if arduinoml_AMLMachine is not None else set()
        
    @property
    def frequency(self) -> int:
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency: int):
        self.__frequency = frequency

    @property
    def arduinoml_AMLMachine2(self):
        return self.__arduinoml_AMLMachine2

    @arduinoml_AMLMachine2.setter
    def arduinoml_AMLMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_AMLMachine__arduinoml_AMLMachine2", None)
        self.__arduinoml_AMLMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoml_AMLState"):
                    opp_val = getattr(item, "arduinoml_AMLState", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoml_AMLState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoml_AMLState"):
                    opp_val = getattr(item, "arduinoml_AMLState", None)
                    
                    setattr(item, "arduinoml_AMLState", self)
                    

    @property
    def arduinoml_AMLMachine4(self):
        return self.__arduinoml_AMLMachine4

    @arduinoml_AMLMachine4.setter
    def arduinoml_AMLMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_AMLMachine__arduinoml_AMLMachine4", None)
        self.__arduinoml_AMLMachine4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoml_AMLState5"):
                opp_val = getattr(old_value, "arduinoml_AMLState5", None)
                if opp_val == self:
                    setattr(old_value, "arduinoml_AMLState5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_AMLState5"):
                opp_val = getattr(value, "arduinoml_AMLState5", None)
                setattr(value, "arduinoml_AMLState5", self)

    @property
    def arduinoml_AMLMachine(self):
        return self.__arduinoml_AMLMachine

    @arduinoml_AMLMachine.setter
    def arduinoml_AMLMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoml_AMLMachine__arduinoml_AMLMachine", None)
        self.__arduinoml_AMLMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoml_Brick"):
                    opp_val = getattr(item, "arduinoml_Brick", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoml_Brick", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoml_Brick"):
                    opp_val = getattr(item, "arduinoml_Brick", None)
                    
                    setattr(item, "arduinoml_Brick", self)
                    

class Brick:

    pass
class arduinoml_AnalogActuator(Brick):

    pass
class arduinoml_AnalogSensor(Brick):

    pass
class arduinoml_DigitalActuator(Brick):

    pass
class arduinoml_DigitalSensor(Brick):

    pass
class arduinoml_Action(ABC):

    pass
class arduinoml_Transition:

    pass
class NamedElement:

    pass
class arduinoml_Brick(NamedElement):

    def __init__(self, pin: int, arduinoml_Brick: "arduinoml_AMLMachine" = None):
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
            if hasattr(old_value, "arduinoml_AMLMachine"):
                opp_val = getattr(old_value, "arduinoml_AMLMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoml_AMLMachine"):
                opp_val = getattr(value, "arduinoml_AMLMachine", None)
                if opp_val is None:
                    setattr(value, "arduinoml_AMLMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduinoml_AMLState(NamedElement):

    pass