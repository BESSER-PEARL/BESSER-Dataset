from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    EQ = "EQ"
    NE = "NE"
    GT = "GT"
    GE = "GE"
    LT = "LT"
    LE = "LE"


############################################
# Definition of Classes
############################################

class Item:

    pass
class iot_Controller(Item):

    pass
class iot_Component(Item):

    pass
class iot_RequiredPort:

    def __init__(self, name: str, UUID: str, method: str, args: str, iot_RequiredPort: "iot_Iteration" = None, iot_RequiredPort11: "iot_Sequence" = None, iot_RequiredPort13: "iot_Component" = None, iot_RequiredPort20: "iot_ProvidedPort" = None):
        self.name = name
        self.UUID = UUID
        self.method = method
        self.args = args
        self.iot_RequiredPort = iot_RequiredPort
        self.iot_RequiredPort11 = iot_RequiredPort11
        self.iot_RequiredPort13 = iot_RequiredPort13
        self.iot_RequiredPort20 = iot_RequiredPort20
        
    @property
    def UUID(self) -> str:
        return self.__UUID

    @UUID.setter
    def UUID(self, UUID: str):
        self.__UUID = UUID

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def args(self) -> str:
        return self.__args

    @args.setter
    def args(self, args: str):
        self.__args = args

    @property
    def iot_RequiredPort11(self):
        return self.__iot_RequiredPort11

    @iot_RequiredPort11.setter
    def iot_RequiredPort11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_RequiredPort__iot_RequiredPort11", None)
        self.__iot_RequiredPort11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Sequence"):
                opp_val = getattr(old_value, "iot_Sequence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Sequence"):
                opp_val = getattr(value, "iot_Sequence", None)
                if opp_val is None:
                    setattr(value, "iot_Sequence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot_RequiredPort(self):
        return self.__iot_RequiredPort

    @iot_RequiredPort.setter
    def iot_RequiredPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_RequiredPort__iot_RequiredPort", None)
        self.__iot_RequiredPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Iteration"):
                opp_val = getattr(old_value, "iot_Iteration", None)
                if opp_val == self:
                    setattr(old_value, "iot_Iteration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Iteration"):
                opp_val = getattr(value, "iot_Iteration", None)
                setattr(value, "iot_Iteration", self)

    @property
    def iot_RequiredPort20(self):
        return self.__iot_RequiredPort20

    @iot_RequiredPort20.setter
    def iot_RequiredPort20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_RequiredPort__iot_RequiredPort20", None)
        self.__iot_RequiredPort20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_ProvidedPort21"):
                opp_val = getattr(old_value, "iot_ProvidedPort21", None)
                if opp_val == self:
                    setattr(old_value, "iot_ProvidedPort21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_ProvidedPort21"):
                opp_val = getattr(value, "iot_ProvidedPort21", None)
                setattr(value, "iot_ProvidedPort21", self)

    @property
    def iot_RequiredPort13(self):
        return self.__iot_RequiredPort13

    @iot_RequiredPort13.setter
    def iot_RequiredPort13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_RequiredPort__iot_RequiredPort13", None)
        self.__iot_RequiredPort13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Component"):
                opp_val = getattr(old_value, "iot_Component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Component"):
                opp_val = getattr(value, "iot_Component", None)
                if opp_val is None:
                    setattr(value, "iot_Component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def invoke(self, method: str) -> str:
        # TODO: Implement invoke method
        pass

class Controller:

    pass
class iot_Iteration(Controller):

    pass
class iot_Sequence(Controller):

    pass
class iot_Branching(Controller):

    pass
class iot_ProvidedPort:

    def __init__(self, UUID: str, name: str, iot_ProvidedPort: "iot_Item" = None, iot_ProvidedPort16: "iot_Component" = None, iot_ProvidedPort18: "iot_Controller" = None, iot_ProvidedPort21: "iot_RequiredPort" = None):
        self.UUID = UUID
        self.name = name
        self.iot_ProvidedPort = iot_ProvidedPort
        self.iot_ProvidedPort16 = iot_ProvidedPort16
        self.iot_ProvidedPort18 = iot_ProvidedPort18
        self.iot_ProvidedPort21 = iot_ProvidedPort21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def UUID(self) -> str:
        return self.__UUID

    @UUID.setter
    def UUID(self, UUID: str):
        self.__UUID = UUID

    @property
    def iot_ProvidedPort16(self):
        return self.__iot_ProvidedPort16

    @iot_ProvidedPort16.setter
    def iot_ProvidedPort16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_ProvidedPort__iot_ProvidedPort16", None)
        self.__iot_ProvidedPort16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Component15"):
                opp_val = getattr(old_value, "iot_Component15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Component15"):
                opp_val = getattr(value, "iot_Component15", None)
                if opp_val is None:
                    setattr(value, "iot_Component15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot_ProvidedPort18(self):
        return self.__iot_ProvidedPort18

    @iot_ProvidedPort18.setter
    def iot_ProvidedPort18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_ProvidedPort__iot_ProvidedPort18", None)
        self.__iot_ProvidedPort18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Controller"):
                opp_val = getattr(old_value, "iot_Controller", None)
                if opp_val == self:
                    setattr(old_value, "iot_Controller", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Controller"):
                opp_val = getattr(value, "iot_Controller", None)
                setattr(value, "iot_Controller", self)

    @property
    def iot_ProvidedPort21(self):
        return self.__iot_ProvidedPort21

    @iot_ProvidedPort21.setter
    def iot_ProvidedPort21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_ProvidedPort__iot_ProvidedPort21", None)
        self.__iot_ProvidedPort21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_RequiredPort20"):
                opp_val = getattr(old_value, "iot_RequiredPort20", None)
                if opp_val == self:
                    setattr(old_value, "iot_RequiredPort20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_RequiredPort20"):
                opp_val = getattr(value, "iot_RequiredPort20", None)
                setattr(value, "iot_RequiredPort20", self)

    @property
    def iot_ProvidedPort(self):
        return self.__iot_ProvidedPort

    @iot_ProvidedPort.setter
    def iot_ProvidedPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_ProvidedPort__iot_ProvidedPort", None)
        self.__iot_ProvidedPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Item3"):
                opp_val = getattr(old_value, "iot_Item3", None)
                if opp_val == self:
                    setattr(old_value, "iot_Item3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Item3"):
                opp_val = getattr(value, "iot_Item3", None)
                setattr(value, "iot_Item3", self)

    def invoke(self, method: str) -> str:
        # TODO: Implement invoke method
        pass

    def invoke(self, method: str, args: str) -> str:
        # TODO: Implement invoke method
        pass

class Hardware:

    pass
class iot_Sensor(Hardware):

    def __init__(self, script: str):
        self.script = script
        
    @property
    def script(self) -> str:
        return self.__script

    @script.setter
    def script(self, script: str):
        self.__script = script

    def getData(self) -> str:
        # TODO: Implement getData method
        pass

class iot_Actuator(Hardware):

    def __init__(self, toggle: bool):
        self.toggle = toggle
        
    @property
    def toggle(self) -> bool:
        return self.__toggle

    @toggle.setter
    def toggle(self, toggle: bool):
        self.__toggle = toggle

    def switchOnOff(self, onOff: str) -> str:
        # TODO: Implement switchOnOff method
        pass

    def getStatus(self) -> bool:
        # TODO: Implement getStatus method
        pass

    def toggle(self) -> str:
        # TODO: Implement toggle method
        pass

class RequiredPort:

    pass
class iot_ElsePort(RequiredPort):

    pass
class iot_ConditionPort(RequiredPort):

    pass
class iot_ThenPort(RequiredPort):

    pass
class iot_IfPort(RequiredPort):

    def __init__(self, condition: bool, var: str, operator: str, iot_IfPort: "iot_Branching" = None):
        self.condition = condition
        self.var = var
        self.operator = operator
        self.iot_IfPort = iot_IfPort
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def condition(self) -> bool:
        return self.__condition

    @condition.setter
    def condition(self, condition: bool):
        self.__condition = condition

    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def iot_IfPort(self):
        return self.__iot_IfPort

    @iot_IfPort.setter
    def iot_IfPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_IfPort__iot_IfPort", None)
        self.__iot_IfPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Branching"):
                opp_val = getattr(old_value, "iot_Branching", None)
                if opp_val == self:
                    setattr(old_value, "iot_Branching", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Branching"):
                opp_val = getattr(value, "iot_Branching", None)
                setattr(value, "iot_Branching", self)

class Iteration:

    pass
class iot_IterativeLoop(Iteration):

    def __init__(self, var: str, operator: str, iot_IterativeLoop: "iot_ConditionPort" = None):
        self.var = var
        self.operator = operator
        self.iot_IterativeLoop = iot_IterativeLoop
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def var(self) -> str:
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var

    @property
    def iot_IterativeLoop(self):
        return self.__iot_IterativeLoop

    @iot_IterativeLoop.setter
    def iot_IterativeLoop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_IterativeLoop__iot_IterativeLoop", None)
        self.__iot_IterativeLoop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_ConditionPort"):
                opp_val = getattr(old_value, "iot_ConditionPort", None)
                if opp_val == self:
                    setattr(old_value, "iot_ConditionPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_ConditionPort"):
                opp_val = getattr(value, "iot_ConditionPort", None)
                setattr(value, "iot_ConditionPort", self)

class iot_CounterLoop(Iteration):

    def __init__(self, counter: int):
        self.counter = counter
        
    @property
    def counter(self) -> int:
        return self.__counter

    @counter.setter
    def counter(self, counter: int):
        self.__counter = counter

class iot_Item(ABC):

    def __init__(self, name: str, UUID: str, newThread: bool, iot_Item: "iot_Software" = None, iot_Item3: "iot_ProvidedPort" = None):
        self.name = name
        self.UUID = UUID
        self.newThread = newThread
        self.iot_Item = iot_Item
        self.iot_Item3 = iot_Item3
        
    @property
    def UUID(self) -> str:
        return self.__UUID

    @UUID.setter
    def UUID(self, UUID: str):
        self.__UUID = UUID

    @property
    def newThread(self) -> bool:
        return self.__newThread

    @newThread.setter
    def newThread(self, newThread: bool):
        self.__newThread = newThread

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot_Item3(self):
        return self.__iot_Item3

    @iot_Item3.setter
    def iot_Item3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Item__iot_Item3", None)
        self.__iot_Item3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_ProvidedPort"):
                opp_val = getattr(old_value, "iot_ProvidedPort", None)
                if opp_val == self:
                    setattr(old_value, "iot_ProvidedPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_ProvidedPort"):
                opp_val = getattr(value, "iot_ProvidedPort", None)
                setattr(value, "iot_ProvidedPort", self)

    @property
    def iot_Item(self):
        return self.__iot_Item

    @iot_Item.setter
    def iot_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Item__iot_Item", None)
        self.__iot_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_Software"):
                opp_val = getattr(old_value, "iot_Software", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_Software"):
                opp_val = getattr(value, "iot_Software", None)
                if opp_val is None:
                    setattr(value, "iot_Software", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def invoke(self) -> str:
        # TODO: Implement invoke method
        pass

class Component:

    pass
class iot_Snippet(Component):

    def __init__(self, scriptPath: str):
        self.scriptPath = scriptPath
        
    @property
    def scriptPath(self) -> str:
        return self.__scriptPath

    @scriptPath.setter
    def scriptPath(self, scriptPath: str):
        self.__scriptPath = scriptPath

class iot_Hardware(Component):

    def __init__(self, type: str, pinNumber: int, mode: bool, timeInterval: int):
        self.type = type
        self.pinNumber = pinNumber
        self.mode = mode
        self.timeInterval = timeInterval
        
    @property
    def timeInterval(self) -> int:
        return self.__timeInterval

    @timeInterval.setter
    def timeInterval(self, timeInterval: int):
        self.__timeInterval = timeInterval

    @property
    def pinNumber(self) -> int:
        return self.__pinNumber

    @pinNumber.setter
    def pinNumber(self, pinNumber: int):
        self.__pinNumber = pinNumber

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mode(self) -> bool:
        return self.__mode

    @mode.setter
    def mode(self, mode: bool):
        self.__mode = mode

class iot_Software(Component):

    pass