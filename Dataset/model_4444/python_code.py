from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Signal(Enum):
    HIGH = "HIGH"
    LOW = "LOW"
class Time_unit(Enum):
    ms = "ms"
    s = "s"
    min = "min"
class Compare(Enum):
    inf = "inf"
    einf = "einf"
    equal = "equal"
    esup = "esup"
    sup = "sup"


############################################
# Definition of Classes
############################################

class arduinoML_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Transition:

    pass
class arduinoML_TransitionMode(Transition):

    pass
class Brick:

    pass
class arduinoML_Analog(Brick):

    def __init__(self, debug: bool, arduinoML_Analog: "arduinoML_Transition" = None):
        self.debug = debug
        self.arduinoML_Analog = arduinoML_Analog
        
    @property
    def debug(self) -> bool:
        return self.__debug

    @debug.setter
    def debug(self, debug: bool):
        self.__debug = debug

    @property
    def arduinoML_Analog(self):
        return self.__arduinoML_Analog

    @arduinoML_Analog.setter
    def arduinoML_Analog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Analog__arduinoML_Analog", None)
        self.__arduinoML_Analog = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_Transition12"):
                opp_val = getattr(old_value, "arduinoML_Transition12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_Transition12"):
                opp_val = getattr(value, "arduinoML_Transition12", None)
                if opp_val is None:
                    setattr(value, "arduinoML_Transition12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduinoML_Digital(Brick):

    pass
class arduinoML_Actuator(Brick):

    pass
class NamedElement:

    pass
class arduinoML_Mode(NamedElement):

    pass
class arduinoML_App(NamedElement):

    def __init__(self, monitoring: bool, arduinoML_App2: set["arduinoML_Mode"] = None, arduinoML_App5: set["arduinoML_Brick"] = None, arduinoML_App: "arduinoML_Mode" = None):
        self.monitoring = monitoring
        self.arduinoML_App2 = arduinoML_App2 if arduinoML_App2 is not None else set()
        self.arduinoML_App5 = arduinoML_App5 if arduinoML_App5 is not None else set()
        self.arduinoML_App = arduinoML_App
        
    @property
    def monitoring(self) -> bool:
        return self.__monitoring

    @monitoring.setter
    def monitoring(self, monitoring: bool):
        self.__monitoring = monitoring

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
                if hasattr(item, "arduinoML_Mode3"):
                    opp_val = getattr(item, "arduinoML_Mode3", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoML_Mode3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoML_Mode3"):
                    opp_val = getattr(item, "arduinoML_Mode3", None)
                    
                    setattr(item, "arduinoML_Mode3", self)
                    

    @property
    def arduinoML_App5(self):
        return self.__arduinoML_App5

    @arduinoML_App5.setter
    def arduinoML_App5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_App__arduinoML_App5", None)
        self.__arduinoML_App5 = value if value is not None else set()
        
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
    def arduinoML_App(self):
        return self.__arduinoML_App

    @arduinoML_App.setter
    def arduinoML_App(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_App__arduinoML_App", None)
        self.__arduinoML_App = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_Mode"):
                opp_val = getattr(old_value, "arduinoML_Mode", None)
                if opp_val == self:
                    setattr(old_value, "arduinoML_Mode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_Mode"):
                opp_val = getattr(value, "arduinoML_Mode", None)
                setattr(value, "arduinoML_Mode", self)

class arduinoML_Brick(NamedElement):

    def __init__(self, pin: int, arduinoML_Brick: "arduinoML_App" = None, arduinoML_Brick15: "arduinoML_Mode" = None):
        self.pin = pin
        self.arduinoML_Brick = arduinoML_Brick
        self.arduinoML_Brick15 = arduinoML_Brick15
        
    @property
    def pin(self) -> int:
        return self.__pin

    @pin.setter
    def pin(self, pin: int):
        self.__pin = pin

    @property
    def arduinoML_Brick15(self):
        return self.__arduinoML_Brick15

    @arduinoML_Brick15.setter
    def arduinoML_Brick15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Brick__arduinoML_Brick15", None)
        self.__arduinoML_Brick15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_Mode14"):
                opp_val = getattr(old_value, "arduinoML_Mode14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_Mode14"):
                opp_val = getattr(value, "arduinoML_Mode14", None)
                if opp_val is None:
                    setattr(value, "arduinoML_Mode14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "arduinoML_App5"):
                opp_val = getattr(old_value, "arduinoML_App5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_App5"):
                opp_val = getattr(value, "arduinoML_App5", None)
                if opp_val is None:
                    setattr(value, "arduinoML_App5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduinoML_Transition(ABC):

    def __init__(self, d_values: str, time: int, unit: str, a_values: int, comp: str, arduinoML_Transition: set["arduinoML_Digital"] = None, arduinoML_Transition12: set["arduinoML_Analog"] = None):
        self.d_values = d_values
        self.time = time
        self.unit = unit
        self.a_values = a_values
        self.comp = comp
        self.arduinoML_Transition = arduinoML_Transition if arduinoML_Transition is not None else set()
        self.arduinoML_Transition12 = arduinoML_Transition12 if arduinoML_Transition12 is not None else set()
        
    @property
    def a_values(self) -> int:
        return self.__a_values

    @a_values.setter
    def a_values(self, a_values: int):
        self.__a_values = a_values

    @property
    def d_values(self) -> str:
        return self.__d_values

    @d_values.setter
    def d_values(self, d_values: str):
        self.__d_values = d_values

    @property
    def comp(self) -> str:
        return self.__comp

    @comp.setter
    def comp(self, comp: str):
        self.__comp = comp

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def arduinoML_Transition(self):
        return self.__arduinoML_Transition

    @arduinoML_Transition.setter
    def arduinoML_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Transition__arduinoML_Transition", None)
        self.__arduinoML_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoML_Digital"):
                    opp_val = getattr(item, "arduinoML_Digital", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoML_Digital", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoML_Digital"):
                    opp_val = getattr(item, "arduinoML_Digital", None)
                    
                    setattr(item, "arduinoML_Digital", self)
                    

    @property
    def arduinoML_Transition12(self):
        return self.__arduinoML_Transition12

    @arduinoML_Transition12.setter
    def arduinoML_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Transition__arduinoML_Transition12", None)
        self.__arduinoML_Transition12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoML_Analog"):
                    opp_val = getattr(item, "arduinoML_Analog", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoML_Analog", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoML_Analog"):
                    opp_val = getattr(item, "arduinoML_Analog", None)
                    
                    setattr(item, "arduinoML_Analog", self)
                    

class arduinoML_TransitionState(Transition):

    pass
class arduinoML_Action:

    def __init__(self, value: str, arduinoML_Action: "arduinoML_State" = None, arduinoML_Action9: "arduinoML_Actuator" = None):
        self.value = value
        self.arduinoML_Action = arduinoML_Action
        self.arduinoML_Action9 = arduinoML_Action9
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def arduinoML_Action9(self):
        return self.__arduinoML_Action9

    @arduinoML_Action9.setter
    def arduinoML_Action9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Action__arduinoML_Action9", None)
        self.__arduinoML_Action9 = value
        
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
            if hasattr(old_value, "arduinoML_State"):
                opp_val = getattr(old_value, "arduinoML_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_State"):
                opp_val = getattr(value, "arduinoML_State", None)
                if opp_val is None:
                    setattr(value, "arduinoML_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduinoML_State(NamedElement):

    pass