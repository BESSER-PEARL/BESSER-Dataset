from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TriggerEvent(Enum):
    Rising = "Rising"
    Falling = "Falling"
    Either = "Either"
class DataType(Enum):
    INHERIT = "INHERIT"
    DOUBLE = "DOUBLE"
    SINGLE = "SINGLE"
    INT32 = "INT32"
    INT16 = "INT16"
    INT8 = "INT8"
    UINT32 = "UINT32"
    UINT16 = "UINT16"
    UINT8 = "UINT8"
    BOOLEAN = "BOOLEAN"
    BUS = "BUS"
class SubStateType(Enum):
    EXCLUSIVE = "EXCLUSIVE"
    PARALLEL = "PARALLEL"


############################################
# Definition of Classes
############################################

class BufferFunction:

    pass
class simulink_buffer_CheckQueue(BufferFunction):

    pass
class simulink_buffer_SharedEnqueue(BufferFunction):

    pass
class simulink_buffer_Dequeue(BufferFunction):

    pass
class simulink_buffer_SharedCheckQueue(BufferFunction):

    pass
class simulink_buffer_SharedDequeue(BufferFunction):

    pass
class simulink_buffer_Enqueue(BufferFunction):

    pass
class Event:

    pass
class Action:

    pass
class EmbeddedFunction:

    pass
class simulink_buffer_BufferFunction(EmbeddedFunction):

    def __init__(self, bufferSize: int, EmbeddedFunction: "simulink_stateflow_State"):
        self.bufferSize = bufferSize
        
    @property
    def bufferSize(self) -> int:
        return self.__bufferSize

    @bufferSize.setter
    def bufferSize(self, bufferSize: int):
        self.__bufferSize = bufferSize

class Transition:

    pass
class Node:

    pass
class simulink_stateflow_History(Node):

    pass
class simulink_stateflow_Junction(Node):

    pass
class simulink_stateflow_State(Node):

    def __init__(self, subStateType: str, name: str, priority: int, initial: bool, Node: set["Node"] = None, simulink_stateflow_State: set["Transition"] = None, simulink_stateflow_State66: set["EmbeddedFunction"] = None, simulink_stateflow_State68: set["Action"] = None, simulink_stateflow_State70: set["Action"] = None, simulink_stateflow_State73: set["Action"] = None, simulink_stateflow_State76: set["Data"] = None, simulink_stateflow_State79: set["Data"] = None, simulink_stateflow_State82: set["Action"] = None, simulink_stateflow_State64: set["Event"] = None, stateflow86: "simulink_stateflow_Transition", stateflow89: "simulink_stateflow_Transition", stateflow61: "simulink_stateflow_State"):
        self.subStateType = subStateType
        self.name = name
        self.priority = priority
        self.initial = initial
        self.Node = Node if Node is not None else set()
        self.simulink_stateflow_State = simulink_stateflow_State if simulink_stateflow_State is not None else set()
        self.simulink_stateflow_State66 = simulink_stateflow_State66 if simulink_stateflow_State66 is not None else set()
        self.simulink_stateflow_State68 = simulink_stateflow_State68 if simulink_stateflow_State68 is not None else set()
        self.simulink_stateflow_State70 = simulink_stateflow_State70 if simulink_stateflow_State70 is not None else set()
        self.simulink_stateflow_State73 = simulink_stateflow_State73 if simulink_stateflow_State73 is not None else set()
        self.simulink_stateflow_State76 = simulink_stateflow_State76 if simulink_stateflow_State76 is not None else set()
        self.simulink_stateflow_State79 = simulink_stateflow_State79 if simulink_stateflow_State79 is not None else set()
        self.simulink_stateflow_State82 = simulink_stateflow_State82 if simulink_stateflow_State82 is not None else set()
        self.simulink_stateflow_State64 = simulink_stateflow_State64 if simulink_stateflow_State64 is not None else set()
        
    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def subStateType(self) -> str:
        return self.__subStateType

    @subStateType.setter
    def subStateType(self, subStateType: str):
        self.__subStateType = subStateType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def simulink_stateflow_State70(self):
        return self.__simulink_stateflow_State70

    @simulink_stateflow_State70.setter
    def simulink_stateflow_State70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State70", None)
        self.__simulink_stateflow_State70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action71"):
                    opp_val = getattr(item, "Action71", None)
                    
                    if opp_val == self:
                        setattr(item, "Action71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action71"):
                    opp_val = getattr(item, "Action71", None)
                    
                    setattr(item, "Action71", self)
                    

    @property
    def simulink_stateflow_State68(self):
        return self.__simulink_stateflow_State68

    @simulink_stateflow_State68.setter
    def simulink_stateflow_State68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State68", None)
        self.__simulink_stateflow_State68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    if opp_val == self:
                        setattr(item, "Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    setattr(item, "Action", self)
                    

    @property
    def simulink_stateflow_State66(self):
        return self.__simulink_stateflow_State66

    @simulink_stateflow_State66.setter
    def simulink_stateflow_State66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State66", None)
        self.__simulink_stateflow_State66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EmbeddedFunction"):
                    opp_val = getattr(item, "EmbeddedFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "EmbeddedFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EmbeddedFunction"):
                    opp_val = getattr(item, "EmbeddedFunction", None)
                    
                    setattr(item, "EmbeddedFunction", self)
                    

    @property
    def simulink_stateflow_State82(self):
        return self.__simulink_stateflow_State82

    @simulink_stateflow_State82.setter
    def simulink_stateflow_State82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State82", None)
        self.__simulink_stateflow_State82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action83"):
                    opp_val = getattr(item, "Action83", None)
                    
                    if opp_val == self:
                        setattr(item, "Action83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action83"):
                    opp_val = getattr(item, "Action83", None)
                    
                    setattr(item, "Action83", self)
                    

    @property
    def simulink_stateflow_State79(self):
        return self.__simulink_stateflow_State79

    @simulink_stateflow_State79.setter
    def simulink_stateflow_State79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State79", None)
        self.__simulink_stateflow_State79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data80"):
                    opp_val = getattr(item, "Data80", None)
                    
                    if opp_val == self:
                        setattr(item, "Data80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data80"):
                    opp_val = getattr(item, "Data80", None)
                    
                    setattr(item, "Data80", self)
                    

    @property
    def simulink_stateflow_State73(self):
        return self.__simulink_stateflow_State73

    @simulink_stateflow_State73.setter
    def simulink_stateflow_State73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State73", None)
        self.__simulink_stateflow_State73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action74"):
                    opp_val = getattr(item, "Action74", None)
                    
                    if opp_val == self:
                        setattr(item, "Action74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action74"):
                    opp_val = getattr(item, "Action74", None)
                    
                    setattr(item, "Action74", self)
                    

    @property
    def simulink_stateflow_State(self):
        return self.__simulink_stateflow_State

    @simulink_stateflow_State.setter
    def simulink_stateflow_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State", None)
        self.__simulink_stateflow_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def simulink_stateflow_State76(self):
        return self.__simulink_stateflow_State76

    @simulink_stateflow_State76.setter
    def simulink_stateflow_State76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State76", None)
        self.__simulink_stateflow_State76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data77"):
                    opp_val = getattr(item, "Data77", None)
                    
                    if opp_val == self:
                        setattr(item, "Data77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data77"):
                    opp_val = getattr(item, "Data77", None)
                    
                    setattr(item, "Data77", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__Node", None)
        self.__Node = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stateflow61"):
                    opp_val = getattr(item, "stateflow61", None)
                    
                    if opp_val == self:
                        setattr(item, "stateflow61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stateflow61"):
                    opp_val = getattr(item, "stateflow61", None)
                    
                    setattr(item, "stateflow61", self)
                    

    @property
    def simulink_stateflow_State64(self):
        return self.__simulink_stateflow_State64

    @simulink_stateflow_State64.setter
    def simulink_stateflow_State64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State64", None)
        self.__simulink_stateflow_State64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Event"):
                    opp_val = getattr(item, "Event", None)
                    
                    setattr(item, "Event", self)
                    

    def getSubState(self, name: str) -> str:
        # TODO: Implement getSubState method
        pass

class stateflow_simulink_ChartBlock:

    pass
class Data:

    pass
class State:

    pass
class simulink_stateflow_Chart(State):

    pass
class stateflow_simulink_SimulinkFile:

    pass
class StateflowElement:

    pass
class simulink_stateflow_Action(StateflowElement):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class simulink_stateflow_EmbeddedFunction(StateflowElement):

    def __init__(self, name: str, code: str, simulink_stateflow_EmbeddedFunction: set["Data"] = None, simulink_stateflow_EmbeddedFunction109: set["Data"] = None, simulink_stateflow_EmbeddedFunction112: set["Data"] = None, simulink_stateflow_EmbeddedFunction115: set["Data"] = None):
        self.name = name
        self.code = code
        self.simulink_stateflow_EmbeddedFunction = simulink_stateflow_EmbeddedFunction if simulink_stateflow_EmbeddedFunction is not None else set()
        self.simulink_stateflow_EmbeddedFunction109 = simulink_stateflow_EmbeddedFunction109 if simulink_stateflow_EmbeddedFunction109 is not None else set()
        self.simulink_stateflow_EmbeddedFunction112 = simulink_stateflow_EmbeddedFunction112 if simulink_stateflow_EmbeddedFunction112 is not None else set()
        self.simulink_stateflow_EmbeddedFunction115 = simulink_stateflow_EmbeddedFunction115 if simulink_stateflow_EmbeddedFunction115 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def simulink_stateflow_EmbeddedFunction109(self):
        return self.__simulink_stateflow_EmbeddedFunction109

    @simulink_stateflow_EmbeddedFunction109.setter
    def simulink_stateflow_EmbeddedFunction109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_EmbeddedFunction__simulink_stateflow_EmbeddedFunction109", None)
        self.__simulink_stateflow_EmbeddedFunction109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data110"):
                    opp_val = getattr(item, "Data110", None)
                    
                    if opp_val == self:
                        setattr(item, "Data110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data110"):
                    opp_val = getattr(item, "Data110", None)
                    
                    setattr(item, "Data110", self)
                    

    @property
    def simulink_stateflow_EmbeddedFunction112(self):
        return self.__simulink_stateflow_EmbeddedFunction112

    @simulink_stateflow_EmbeddedFunction112.setter
    def simulink_stateflow_EmbeddedFunction112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_EmbeddedFunction__simulink_stateflow_EmbeddedFunction112", None)
        self.__simulink_stateflow_EmbeddedFunction112 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data113"):
                    opp_val = getattr(item, "Data113", None)
                    
                    if opp_val == self:
                        setattr(item, "Data113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data113"):
                    opp_val = getattr(item, "Data113", None)
                    
                    setattr(item, "Data113", self)
                    

    @property
    def simulink_stateflow_EmbeddedFunction(self):
        return self.__simulink_stateflow_EmbeddedFunction

    @simulink_stateflow_EmbeddedFunction.setter
    def simulink_stateflow_EmbeddedFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_EmbeddedFunction__simulink_stateflow_EmbeddedFunction", None)
        self.__simulink_stateflow_EmbeddedFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data107"):
                    opp_val = getattr(item, "Data107", None)
                    
                    if opp_val == self:
                        setattr(item, "Data107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data107"):
                    opp_val = getattr(item, "Data107", None)
                    
                    setattr(item, "Data107", self)
                    

    @property
    def simulink_stateflow_EmbeddedFunction115(self):
        return self.__simulink_stateflow_EmbeddedFunction115

    @simulink_stateflow_EmbeddedFunction115.setter
    def simulink_stateflow_EmbeddedFunction115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_EmbeddedFunction__simulink_stateflow_EmbeddedFunction115", None)
        self.__simulink_stateflow_EmbeddedFunction115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data116"):
                    opp_val = getattr(item, "Data116", None)
                    
                    if opp_val == self:
                        setattr(item, "Data116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data116"):
                    opp_val = getattr(item, "Data116", None)
                    
                    setattr(item, "Data116", self)
                    

class simulink_stateflow_Event(StateflowElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simulink_stateflow_Transition(StateflowElement):

    def __init__(self, priority: int, Node85: "Node" = None, Node88: "Node" = None, simulink_stateflow_Transition: "Event" = None, simulink_stateflow_Transition93: set["Action"] = None, simulink_stateflow_Transition96: set["Action"] = None):
        self.priority = priority
        self.Node85 = Node85
        self.Node88 = Node88
        self.simulink_stateflow_Transition = simulink_stateflow_Transition
        self.simulink_stateflow_Transition93 = simulink_stateflow_Transition93 if simulink_stateflow_Transition93 is not None else set()
        self.simulink_stateflow_Transition96 = simulink_stateflow_Transition96 if simulink_stateflow_Transition96 is not None else set()
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def Node85(self):
        return self.__Node85

    @Node85.setter
    def Node85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_Transition__Node85", None)
        self.__Node85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateflow86"):
                opp_val = getattr(old_value, "stateflow86", None)
                if opp_val == self:
                    setattr(old_value, "stateflow86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateflow86"):
                opp_val = getattr(value, "stateflow86", None)
                setattr(value, "stateflow86", self)

    @property
    def simulink_stateflow_Transition96(self):
        return self.__simulink_stateflow_Transition96

    @simulink_stateflow_Transition96.setter
    def simulink_stateflow_Transition96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_Transition__simulink_stateflow_Transition96", None)
        self.__simulink_stateflow_Transition96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action97"):
                    opp_val = getattr(item, "Action97", None)
                    
                    if opp_val == self:
                        setattr(item, "Action97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action97"):
                    opp_val = getattr(item, "Action97", None)
                    
                    setattr(item, "Action97", self)
                    

    @property
    def simulink_stateflow_Transition93(self):
        return self.__simulink_stateflow_Transition93

    @simulink_stateflow_Transition93.setter
    def simulink_stateflow_Transition93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_Transition__simulink_stateflow_Transition93", None)
        self.__simulink_stateflow_Transition93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action94"):
                    opp_val = getattr(item, "Action94", None)
                    
                    if opp_val == self:
                        setattr(item, "Action94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action94"):
                    opp_val = getattr(item, "Action94", None)
                    
                    setattr(item, "Action94", self)
                    

    @property
    def simulink_stateflow_Transition(self):
        return self.__simulink_stateflow_Transition

    @simulink_stateflow_Transition.setter
    def simulink_stateflow_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_Transition__simulink_stateflow_Transition", None)
        self.__simulink_stateflow_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Event91"):
                opp_val = getattr(old_value, "Event91", None)
                if opp_val == self:
                    setattr(old_value, "Event91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Event91"):
                opp_val = getattr(value, "Event91", None)
                setattr(value, "Event91", self)

    @property
    def Node88(self):
        return self.__Node88

    @Node88.setter
    def Node88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_Transition__Node88", None)
        self.__Node88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateflow89"):
                opp_val = getattr(old_value, "stateflow89", None)
                if opp_val == self:
                    setattr(old_value, "stateflow89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateflow89"):
                opp_val = getattr(value, "stateflow89", None)
                setattr(value, "stateflow89", self)

class simulink_stateflow_Data(StateflowElement):

    def __init__(self, name: str, type: str, value: str, size: str):
        self.name = name
        self.type = type
        self.value = value
        self.size = size
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

class simulink_stateflow_Node(StateflowElement):

    pass
class simulink_stateflow_StateflowMachine(StateflowElement):

    pass
class InPortBlock:

    pass
class simulink_EnablePort(InPortBlock):

    pass
class simulink_TriggerPort(InPortBlock):

    def __init__(self, triggerInput: str):
        self.triggerInput = triggerInput
        
    @property
    def triggerInput(self) -> str:
        return self.__triggerInput

    @triggerInput.setter
    def triggerInput(self, triggerInput: str):
        self.__triggerInput = triggerInput

class simulink_BusElement:

    def __init__(self, name: str, dimensions: str, type: str, simulink_BusElement: "simulink_Bus" = None, simulink_BusElement46: "simulink_Bus" = None):
        self.name = name
        self.dimensions = dimensions
        self.type = type
        self.simulink_BusElement = simulink_BusElement
        self.simulink_BusElement46 = simulink_BusElement46
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dimensions(self) -> str:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions

    @property
    def simulink_BusElement(self):
        return self.__simulink_BusElement

    @simulink_BusElement.setter
    def simulink_BusElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_BusElement__simulink_BusElement", None)
        self.__simulink_BusElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Bus40"):
                opp_val = getattr(old_value, "simulink_Bus40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Bus40"):
                opp_val = getattr(value, "simulink_Bus40", None)
                if opp_val is None:
                    setattr(value, "simulink_Bus40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simulink_BusElement46(self):
        return self.__simulink_BusElement46

    @simulink_BusElement46.setter
    def simulink_BusElement46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_BusElement__simulink_BusElement46", None)
        self.__simulink_BusElement46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Bus47"):
                opp_val = getattr(old_value, "simulink_Bus47", None)
                if opp_val == self:
                    setattr(old_value, "simulink_Bus47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Bus47"):
                opp_val = getattr(value, "simulink_Bus47", None)
                setattr(value, "simulink_Bus47", self)

class Chart:

    pass
class StateflowMachine:

    pass
class SubSystem:

    pass
class simulink_SimulinkFile(SubSystem):

    pass
class PortBlock:

    pass
class Block:

    pass
class simulink_MiscBlock(Block):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class simulink_reconfiguration_MultiTargetControl(Block):

    pass
class simulink_ChartBlock(Block):

    pass
class simulink_ZeroOrderHold(Block):

    def __init__(self, sampleTime: str):
        self.sampleTime = sampleTime
        
    @property
    def sampleTime(self) -> str:
        return self.__sampleTime

    @sampleTime.setter
    def sampleTime(self, sampleTime: str):
        self.__sampleTime = sampleTime

class simulink_Constant(Block):

    def __init__(self, value: str, type: str):
        self.value = value
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class simulink_reconfiguration_FadingComponent(Block):

    def __init__(self, time: int):
        self.time = time
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

class simulink_BusSelector(Block):

    pass
class simulink_LibraryReference(Block):

    pass
class simulink_reconfiguration_MultiSourceControl(Block):

    pass
class simulink_msglib_LinkLayer(Block):

    def __init__(self, delayMin: str, messageRetransmission: bool, bufferOverflowPossible: bool, bufferSize: int, sourceBufferSize: int, messageMapping: str, delayMax: str, messageLossProbability: int):
        self.delayMin = delayMin
        self.messageRetransmission = messageRetransmission
        self.bufferOverflowPossible = bufferOverflowPossible
        self.bufferSize = bufferSize
        self.sourceBufferSize = sourceBufferSize
        self.messageMapping = messageMapping
        self.delayMax = delayMax
        self.messageLossProbability = messageLossProbability
        
    @property
    def bufferOverflowPossible(self) -> bool:
        return self.__bufferOverflowPossible

    @bufferOverflowPossible.setter
    def bufferOverflowPossible(self, bufferOverflowPossible: bool):
        self.__bufferOverflowPossible = bufferOverflowPossible

    @property
    def messageMapping(self) -> str:
        return self.__messageMapping

    @messageMapping.setter
    def messageMapping(self, messageMapping: str):
        self.__messageMapping = messageMapping

    @property
    def sourceBufferSize(self) -> int:
        return self.__sourceBufferSize

    @sourceBufferSize.setter
    def sourceBufferSize(self, sourceBufferSize: int):
        self.__sourceBufferSize = sourceBufferSize

    @property
    def bufferSize(self) -> int:
        return self.__bufferSize

    @bufferSize.setter
    def bufferSize(self, bufferSize: int):
        self.__bufferSize = bufferSize

    @property
    def delayMin(self) -> str:
        return self.__delayMin

    @delayMin.setter
    def delayMin(self, delayMin: str):
        self.__delayMin = delayMin

    @property
    def delayMax(self) -> str:
        return self.__delayMax

    @delayMax.setter
    def delayMax(self, delayMax: str):
        self.__delayMax = delayMax

    @property
    def messageLossProbability(self) -> int:
        return self.__messageLossProbability

    @messageLossProbability.setter
    def messageLossProbability(self, messageLossProbability: int):
        self.__messageLossProbability = messageLossProbability

    @property
    def messageRetransmission(self) -> bool:
        return self.__messageRetransmission

    @messageRetransmission.setter
    def messageRetransmission(self, messageRetransmission: bool):
        self.__messageRetransmission = messageRetransmission

class simulink_UnitDelay(Block):

    pass
class simulink_PortBlock(Block):

    def __init__(self, dimensions: str, type: str, initialCondition: str):
        self.dimensions = dimensions
        self.type = type
        self.initialCondition = initialCondition
        
    @property
    def initialCondition(self) -> str:
        return self.__initialCondition

    @initialCondition.setter
    def initialCondition(self, initialCondition: str):
        self.__initialCondition = initialCondition

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dimensions(self) -> str:
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions

class simulink_msglib_CommunicationSwitch(Block):

    def __init__(self, debug: int):
        self.debug = debug
        
    @property
    def debug(self) -> int:
        return self.__debug

    @debug.setter
    def debug(self, debug: int):
        self.__debug = debug

class simulink_DigitalClock(Block):

    def __init__(self, sampleTime: float):
        self.sampleTime = sampleTime
        
    @property
    def sampleTime(self) -> float:
        return self.__sampleTime

    @sampleTime.setter
    def sampleTime(self, sampleTime: float):
        self.__sampleTime = sampleTime

class simulink_BusCreator(Block):

    pass
class simulink_EmbeddedMatlabFunction(Block):

    def __init__(self, code: str):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class simulink_Parameter:

    def __init__(self, name: str, value: str, type: str, simulink_Parameter: "simulink_Element" = None):
        self.name = name
        self.value = value
        self.type = type
        self.simulink_Parameter = simulink_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def simulink_Parameter(self):
        return self.__simulink_Parameter

    @simulink_Parameter.setter
    def simulink_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Parameter__simulink_Parameter", None)
        self.__simulink_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Element"):
                opp_val = getattr(old_value, "simulink_Element", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Element"):
                opp_val = getattr(value, "simulink_Element", None)
                if opp_val is None:
                    setattr(value, "simulink_Element", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simulink_Element(ABC):

    def __init__(self, id: str, simulink_Element: set["simulink_Parameter"] = None):
        self.id = id
        self.simulink_Element = simulink_Element if simulink_Element is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def simulink_Element(self):
        return self.__simulink_Element

    @simulink_Element.setter
    def simulink_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Element__simulink_Element", None)
        self.__simulink_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simulink_Parameter"):
                    opp_val = getattr(item, "simulink_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "simulink_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simulink_Parameter"):
                    opp_val = getattr(item, "simulink_Parameter", None)
                    
                    setattr(item, "simulink_Parameter", self)
                    

    def getParameter(self, name: str) -> str:
        # TODO: Implement getParameter method
        pass

class SimulinkFile:

    pass
class simulink_SimulinkLibrary(SimulinkFile):

    pass
class simulink_SimulinkModel(SimulinkFile):

    pass
class simulink_InPortBlock(PortBlock):

    pass
class simulink_OutPortBlock(PortBlock):

    pass
class simulink_SubSystem(Block):

    def __init__(self, SubSystem: "simulink_Block" = None, parent: set["simulink_Block"] = None, simulink_SubSystem23: "simulink_SubSystem" = None, simulink_SubSystem21: set["simulink_SubSystem"] = None, simulink_SubSystem25: set["simulink_Block"] = None, simulink_SubSystem: set["simulink_Line"] = None):
        self.SubSystem = SubSystem
        self.parent = parent if parent is not None else set()
        self.simulink_SubSystem23 = simulink_SubSystem23
        self.simulink_SubSystem21 = simulink_SubSystem21 if simulink_SubSystem21 is not None else set()
        self.simulink_SubSystem25 = simulink_SubSystem25 if simulink_SubSystem25 is not None else set()
        self.simulink_SubSystem = simulink_SubSystem if simulink_SubSystem is not None else set()
        
    @property
    def simulink_SubSystem23(self):
        return self.__simulink_SubSystem23

    @simulink_SubSystem23.setter
    def simulink_SubSystem23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SubSystem__simulink_SubSystem23", None)
        self.__simulink_SubSystem23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_SubSystem21"):
                opp_val = getattr(old_value, "simulink_SubSystem21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_SubSystem21"):
                opp_val = getattr(value, "simulink_SubSystem21", None)
                if opp_val is None:
                    setattr(value, "simulink_SubSystem21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simulink_SubSystem21(self):
        return self.__simulink_SubSystem21

    @simulink_SubSystem21.setter
    def simulink_SubSystem21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SubSystem__simulink_SubSystem21", None)
        self.__simulink_SubSystem21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simulink_SubSystem23"):
                    opp_val = getattr(item, "simulink_SubSystem23", None)
                    
                    if opp_val == self:
                        setattr(item, "simulink_SubSystem23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simulink_SubSystem23"):
                    opp_val = getattr(item, "simulink_SubSystem23", None)
                    
                    setattr(item, "simulink_SubSystem23", self)
                    

    @property
    def SubSystem(self):
        return self.__SubSystem

    @SubSystem.setter
    def SubSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SubSystem__SubSystem", None)
        self.__SubSystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blocks"):
                opp_val = getattr(old_value, "blocks", None)
                if opp_val == self:
                    setattr(old_value, "blocks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blocks"):
                opp_val = getattr(value, "blocks", None)
                setattr(value, "blocks", self)

    @property
    def simulink_SubSystem(self):
        return self.__simulink_SubSystem

    @simulink_SubSystem.setter
    def simulink_SubSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SubSystem__simulink_SubSystem", None)
        self.__simulink_SubSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simulink_Line18"):
                    opp_val = getattr(item, "simulink_Line18", None)
                    
                    if opp_val == self:
                        setattr(item, "simulink_Line18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simulink_Line18"):
                    opp_val = getattr(item, "simulink_Line18", None)
                    
                    setattr(item, "simulink_Line18", self)
                    

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SubSystem__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Block20"):
                    opp_val = getattr(item, "Block20", None)
                    
                    if opp_val == self:
                        setattr(item, "Block20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Block20"):
                    opp_val = getattr(item, "Block20", None)
                    
                    setattr(item, "Block20", self)
                    

    @property
    def simulink_SubSystem25(self):
        return self.__simulink_SubSystem25

    @simulink_SubSystem25.setter
    def simulink_SubSystem25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_SubSystem__simulink_SubSystem25", None)
        self.__simulink_SubSystem25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simulink_Block"):
                    opp_val = getattr(item, "simulink_Block", None)
                    
                    if opp_val == self:
                        setattr(item, "simulink_Block", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simulink_Block"):
                    opp_val = getattr(item, "simulink_Block", None)
                    
                    setattr(item, "simulink_Block", self)
                    

    def getBlockByName(self, name: str) -> Block:
        # TODO: Implement getBlockByName method
        pass

class Element:

    pass
class simulink_Line(Element):

    pass
class simulink_SimulinkContainer(Element):

    pass
class simulink_stateflow_StateflowElement(Element):

    pass
class simulink_Bus(Element):

    def __init__(self, name: str, simulink_Bus: "simulink_Line" = None, simulink_Bus34: "simulink_SimulinkFile" = None, simulink_Bus40: set["simulink_BusElement"] = None, simulink_Bus42: "simulink_BusCreator" = None, simulink_Bus44: "simulink_BusSelector" = None, simulink_Bus47: "simulink_BusElement" = None):
        self.name = name
        self.simulink_Bus = simulink_Bus
        self.simulink_Bus34 = simulink_Bus34
        self.simulink_Bus40 = simulink_Bus40 if simulink_Bus40 is not None else set()
        self.simulink_Bus42 = simulink_Bus42
        self.simulink_Bus44 = simulink_Bus44
        self.simulink_Bus47 = simulink_Bus47
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simulink_Bus44(self):
        return self.__simulink_Bus44

    @simulink_Bus44.setter
    def simulink_Bus44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Bus__simulink_Bus44", None)
        self.__simulink_Bus44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_BusSelector"):
                opp_val = getattr(old_value, "simulink_BusSelector", None)
                if opp_val == self:
                    setattr(old_value, "simulink_BusSelector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_BusSelector"):
                opp_val = getattr(value, "simulink_BusSelector", None)
                setattr(value, "simulink_BusSelector", self)

    @property
    def simulink_Bus40(self):
        return self.__simulink_Bus40

    @simulink_Bus40.setter
    def simulink_Bus40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Bus__simulink_Bus40", None)
        self.__simulink_Bus40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simulink_BusElement"):
                    opp_val = getattr(item, "simulink_BusElement", None)
                    
                    if opp_val == self:
                        setattr(item, "simulink_BusElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simulink_BusElement"):
                    opp_val = getattr(item, "simulink_BusElement", None)
                    
                    setattr(item, "simulink_BusElement", self)
                    

    @property
    def simulink_Bus47(self):
        return self.__simulink_Bus47

    @simulink_Bus47.setter
    def simulink_Bus47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Bus__simulink_Bus47", None)
        self.__simulink_Bus47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_BusElement46"):
                opp_val = getattr(old_value, "simulink_BusElement46", None)
                if opp_val == self:
                    setattr(old_value, "simulink_BusElement46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_BusElement46"):
                opp_val = getattr(value, "simulink_BusElement46", None)
                setattr(value, "simulink_BusElement46", self)

    @property
    def simulink_Bus(self):
        return self.__simulink_Bus

    @simulink_Bus.setter
    def simulink_Bus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Bus__simulink_Bus", None)
        self.__simulink_Bus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_Line16"):
                opp_val = getattr(old_value, "simulink_Line16", None)
                if opp_val == self:
                    setattr(old_value, "simulink_Line16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_Line16"):
                opp_val = getattr(value, "simulink_Line16", None)
                setattr(value, "simulink_Line16", self)

    @property
    def simulink_Bus34(self):
        return self.__simulink_Bus34

    @simulink_Bus34.setter
    def simulink_Bus34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Bus__simulink_Bus34", None)
        self.__simulink_Bus34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_SimulinkFile"):
                opp_val = getattr(old_value, "simulink_SimulinkFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_SimulinkFile"):
                opp_val = getattr(value, "simulink_SimulinkFile", None)
                if opp_val is None:
                    setattr(value, "simulink_SimulinkFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simulink_Bus42(self):
        return self.__simulink_Bus42

    @simulink_Bus42.setter
    def simulink_Bus42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Bus__simulink_Bus42", None)
        self.__simulink_Bus42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_BusCreator"):
                opp_val = getattr(old_value, "simulink_BusCreator", None)
                if opp_val == self:
                    setattr(old_value, "simulink_BusCreator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_BusCreator"):
                opp_val = getattr(value, "simulink_BusCreator", None)
                setattr(value, "simulink_BusCreator", self)

class simulink_Block(Element):

    def __init__(self, name: str, blocks: "simulink_SubSystem" = None, block: set["simulink_OutPortBlock"] = None, targetBlock: set["simulink_Line"] = None, sourceBlock: set["simulink_Line"] = None, Block: "simulink_Line" = None, Block14: "simulink_Line" = None, block3: set["simulink_InPortBlock"] = None, Block20: "simulink_SubSystem" = None, simulink_Block: "simulink_SubSystem" = None, Block27: "simulink_InPortBlock" = None, Block36: "simulink_OutPortBlock" = None, simulink_Block31: "simulink_LibraryReference" = None):
        self.name = name
        self.blocks = blocks
        self.block = block if block is not None else set()
        self.targetBlock = targetBlock if targetBlock is not None else set()
        self.sourceBlock = sourceBlock if sourceBlock is not None else set()
        self.Block = Block
        self.Block14 = Block14
        self.block3 = block3 if block3 is not None else set()
        self.Block20 = Block20
        self.simulink_Block = simulink_Block
        self.Block27 = Block27
        self.Block36 = Block36
        self.simulink_Block31 = simulink_Block31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Block27(self):
        return self.__Block27

    @Block27.setter
    def Block27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__Block27", None)
        self.__Block27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inPorts"):
                opp_val = getattr(old_value, "inPorts", None)
                if opp_val == self:
                    setattr(old_value, "inPorts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inPorts"):
                opp_val = getattr(value, "inPorts", None)
                setattr(value, "inPorts", self)

    @property
    def simulink_Block31(self):
        return self.__simulink_Block31

    @simulink_Block31.setter
    def simulink_Block31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__simulink_Block31", None)
        self.__simulink_Block31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_LibraryReference"):
                opp_val = getattr(old_value, "simulink_LibraryReference", None)
                if opp_val == self:
                    setattr(old_value, "simulink_LibraryReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_LibraryReference"):
                opp_val = getattr(value, "simulink_LibraryReference", None)
                setattr(value, "simulink_LibraryReference", self)

    @property
    def block(self):
        return self.__block

    @block.setter
    def block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__block", None)
        self.__block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OutPortBlock"):
                    opp_val = getattr(item, "OutPortBlock", None)
                    
                    if opp_val == self:
                        setattr(item, "OutPortBlock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OutPortBlock"):
                    opp_val = getattr(item, "OutPortBlock", None)
                    
                    setattr(item, "OutPortBlock", self)
                    

    @property
    def Block(self):
        return self.__Block

    @Block.setter
    def Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__Block", None)
        self.__Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingLines"):
                opp_val = getattr(old_value, "outgoingLines", None)
                if opp_val == self:
                    setattr(old_value, "outgoingLines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingLines"):
                opp_val = getattr(value, "outgoingLines", None)
                setattr(value, "outgoingLines", self)

    @property
    def sourceBlock(self):
        return self.__sourceBlock

    @sourceBlock.setter
    def sourceBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__sourceBlock", None)
        self.__sourceBlock = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Line6"):
                    opp_val = getattr(item, "Line6", None)
                    
                    if opp_val == self:
                        setattr(item, "Line6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Line6"):
                    opp_val = getattr(item, "Line6", None)
                    
                    setattr(item, "Line6", self)
                    

    @property
    def Block20(self):
        return self.__Block20

    @Block20.setter
    def Block20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__Block20", None)
        self.__Block20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simulink_Block(self):
        return self.__simulink_Block

    @simulink_Block.setter
    def simulink_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__simulink_Block", None)
        self.__simulink_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulink_SubSystem25"):
                opp_val = getattr(old_value, "simulink_SubSystem25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulink_SubSystem25"):
                opp_val = getattr(value, "simulink_SubSystem25", None)
                if opp_val is None:
                    setattr(value, "simulink_SubSystem25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def blocks(self):
        return self.__blocks

    @blocks.setter
    def blocks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__blocks", None)
        self.__blocks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SubSystem"):
                opp_val = getattr(old_value, "SubSystem", None)
                if opp_val == self:
                    setattr(old_value, "SubSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SubSystem"):
                opp_val = getattr(value, "SubSystem", None)
                setattr(value, "SubSystem", self)

    @property
    def Block14(self):
        return self.__Block14

    @Block14.setter
    def Block14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__Block14", None)
        self.__Block14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingLines"):
                opp_val = getattr(old_value, "incomingLines", None)
                if opp_val == self:
                    setattr(old_value, "incomingLines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingLines"):
                opp_val = getattr(value, "incomingLines", None)
                setattr(value, "incomingLines", self)

    @property
    def Block36(self):
        return self.__Block36

    @Block36.setter
    def Block36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__Block36", None)
        self.__Block36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outPorts"):
                opp_val = getattr(old_value, "outPorts", None)
                if opp_val == self:
                    setattr(old_value, "outPorts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outPorts"):
                opp_val = getattr(value, "outPorts", None)
                setattr(value, "outPorts", self)

    @property
    def targetBlock(self):
        return self.__targetBlock

    @targetBlock.setter
    def targetBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__targetBlock", None)
        self.__targetBlock = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Line"):
                    opp_val = getattr(item, "Line", None)
                    
                    if opp_val == self:
                        setattr(item, "Line", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Line"):
                    opp_val = getattr(item, "Line", None)
                    
                    setattr(item, "Line", self)
                    

    @property
    def block3(self):
        return self.__block3

    @block3.setter
    def block3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_Block__block3", None)
        self.__block3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InPortBlock"):
                    opp_val = getattr(item, "InPortBlock", None)
                    
                    if opp_val == self:
                        setattr(item, "InPortBlock", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InPortBlock"):
                    opp_val = getattr(item, "InPortBlock", None)
                    
                    setattr(item, "InPortBlock", self)
                    

    def getFullyQualifiedName(self) -> str:
        # TODO: Implement getFullyQualifiedName method
        pass
