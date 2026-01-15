from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    AND = "AND"
    OR = "OR"
class Type(Enum):
    analog = "analog"
    digital = "digital"
class Comparator(Enum):
    sup = "sup"
    inf = "inf"
    equ = "equ"
    esup = "esup"
    einf = "einf"
class Signal(Enum):
    HIGH = "HIGH"
    LOW = "LOW"


############################################
# Definition of Classes
############################################

class Condition:

    pass
class arduinoML_Condition(ABC):

    def __init__(self, value: str, analogvalue: int, comparator: str, arduinoML_Condition: "arduinoML_Sensor" = None):
        self.value = value
        self.analogvalue = analogvalue
        self.comparator = comparator
        self.arduinoML_Condition = arduinoML_Condition
        
    @property
    def analogvalue(self) -> int:
        return self.__analogvalue

    @analogvalue.setter
    def analogvalue(self, analogvalue: int):
        self.__analogvalue = analogvalue

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
    def arduinoML_Condition(self):
        return self.__arduinoML_Condition

    @arduinoML_Condition.setter
    def arduinoML_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Condition__arduinoML_Condition", None)
        self.__arduinoML_Condition = value
        
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

class arduinoML_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class arduinoML_BooleanCondition(Condition):

    def __init__(self, operator: str, arduinoML_BooleanCondition: "arduinoML_Transition" = None, arduinoML_BooleanCondition25: "arduinoML_SinkError" = None):
        self.operator = operator
        self.arduinoML_BooleanCondition = arduinoML_BooleanCondition
        self.arduinoML_BooleanCondition25 = arduinoML_BooleanCondition25
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def arduinoML_BooleanCondition(self):
        return self.__arduinoML_BooleanCondition

    @arduinoML_BooleanCondition.setter
    def arduinoML_BooleanCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_BooleanCondition__arduinoML_BooleanCondition", None)
        self.__arduinoML_BooleanCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_Transition19"):
                opp_val = getattr(old_value, "arduinoML_Transition19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_Transition19"):
                opp_val = getattr(value, "arduinoML_Transition19", None)
                if opp_val is None:
                    setattr(value, "arduinoML_Transition19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduinoML_BooleanCondition25(self):
        return self.__arduinoML_BooleanCondition25

    @arduinoML_BooleanCondition25.setter
    def arduinoML_BooleanCondition25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_BooleanCondition__arduinoML_BooleanCondition25", None)
        self.__arduinoML_BooleanCondition25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_SinkError24"):
                opp_val = getattr(old_value, "arduinoML_SinkError24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_SinkError24"):
                opp_val = getattr(value, "arduinoML_SinkError24", None)
                if opp_val is None:
                    setattr(value, "arduinoML_SinkError24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduinoML_SinkError:

    def __init__(self, value: int, SinkError: "arduinoML_State" = None, arduinoML_SinkError: "arduinoML_BaseCondition" = None, arduinoML_SinkError24: set["arduinoML_BooleanCondition"] = None, errors: "arduinoML_State" = None):
        self.value = value
        self.SinkError = SinkError
        self.arduinoML_SinkError = arduinoML_SinkError
        self.arduinoML_SinkError24 = arduinoML_SinkError24 if arduinoML_SinkError24 is not None else set()
        self.errors = errors
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def errors(self):
        return self.__errors

    @errors.setter
    def errors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_SinkError__errors", None)
        self.__errors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State27"):
                opp_val = getattr(old_value, "State27", None)
                if opp_val == self:
                    setattr(old_value, "State27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State27"):
                opp_val = getattr(value, "State27", None)
                setattr(value, "State27", self)

    @property
    def arduinoML_SinkError(self):
        return self.__arduinoML_SinkError

    @arduinoML_SinkError.setter
    def arduinoML_SinkError(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_SinkError__arduinoML_SinkError", None)
        self.__arduinoML_SinkError = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduinoML_BaseCondition22"):
                opp_val = getattr(old_value, "arduinoML_BaseCondition22", None)
                if opp_val == self:
                    setattr(old_value, "arduinoML_BaseCondition22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduinoML_BaseCondition22"):
                opp_val = getattr(value, "arduinoML_BaseCondition22", None)
                setattr(value, "arduinoML_BaseCondition22", self)

    @property
    def arduinoML_SinkError24(self):
        return self.__arduinoML_SinkError24

    @arduinoML_SinkError24.setter
    def arduinoML_SinkError24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_SinkError__arduinoML_SinkError24", None)
        self.__arduinoML_SinkError24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduinoML_BooleanCondition25"):
                    opp_val = getattr(item, "arduinoML_BooleanCondition25", None)
                    
                    if opp_val == self:
                        setattr(item, "arduinoML_BooleanCondition25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduinoML_BooleanCondition25"):
                    opp_val = getattr(item, "arduinoML_BooleanCondition25", None)
                    
                    setattr(item, "arduinoML_BooleanCondition25", self)
                    

    @property
    def SinkError(self):
        return self.__SinkError

    @SinkError.setter
    def SinkError(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_SinkError__SinkError", None)
        self.__SinkError = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state10"):
                opp_val = getattr(old_value, "state10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state10"):
                opp_val = getattr(value, "state10", None)
                if opp_val is None:
                    setattr(value, "state10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduinoML_Transition:

    pass
class arduinoML_Action:

    def __init__(self, analogvalue: int, value: str, arduinoML_Action: "arduinoML_State" = None, arduinoML_Action12: "arduinoML_Actuator" = None):
        self.analogvalue = analogvalue
        self.value = value
        self.arduinoML_Action = arduinoML_Action
        self.arduinoML_Action12 = arduinoML_Action12
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def analogvalue(self) -> int:
        return self.__analogvalue

    @analogvalue.setter
    def analogvalue(self, analogvalue: int):
        self.__analogvalue = analogvalue

    @property
    def arduinoML_Action12(self):
        return self.__arduinoML_Action12

    @arduinoML_Action12.setter
    def arduinoML_Action12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduinoML_Action__arduinoML_Action12", None)
        self.__arduinoML_Action12 = value
        
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

class arduinoML_BaseCondition(Condition):

    pass
class Brick:

    pass
class arduinoML_Sensor(Brick):

    pass
class arduinoML_Actuator(Brick):

    pass
class NamedElement:

    pass
class arduinoML_App(NamedElement):

    pass
class arduinoML_State(NamedElement):

    pass
class arduinoML_Brick(NamedElement):

    def __init__(self, pin: int, type: str, arduinoML_Brick: "arduinoML_App" = None):
        self.pin = pin
        self.type = type
        self.arduinoML_Brick = arduinoML_Brick
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
