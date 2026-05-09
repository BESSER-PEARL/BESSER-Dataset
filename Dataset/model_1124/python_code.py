from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class TriggerEvent(Enum):
    Rising = "Rising"
    Falling = "Falling"
    Either = "Either"
class SubStateType(Enum):
    EXCLUSIVE = "EXCLUSIVE"
    PARALLEL = "PARALLEL"


############################################
# Definition of Classes
############################################

class BufferFunction:

    pass
class simulink_buffer_SharedDequeue(BufferFunction):

    pass
class simulink_buffer_CheckQueue(BufferFunction):

    pass
class simulink_buffer_Dequeue(BufferFunction):

    pass
class simulink_buffer_SharedEnqueue(BufferFunction):

    pass
class simulink_buffer_SharedCheckQueue(BufferFunction):

    pass
class simulink_buffer_Enqueue(BufferFunction):

    pass
class Action:

    pass
class EmbeddedFunction:

    pass
class simulink_buffer_BufferFunction(EmbeddedFunction):

    def __init__(self, bufferSize: int, EmbeddedFunction: "simulink_stateflow_State" = None):
        self.bufferSize = bufferSize
        
        pass
    @property
    def bufferSize(self):
        return self.__bufferSize

    @bufferSize.setter
    def bufferSize(self, bufferSize: int):
        self.__bufferSize = bufferSize


class Event:

    pass
class Transition:

    pass
class Node:

    pass
class simulink_stateflow_Junction(Node):

    pass
class simulink_stateflow_History(Node):

    pass
class simulink_stateflow_State(Node):

    def __init__(self, subStateType: str, name: str, priority: int, initial: bool, parent59: set["Node"] = None, simulink_stateflow_State: set["Transition"] = None, simulink_stateflow_State62: set["Event"] = None, simulink_stateflow_State64: set["EmbeddedFunction"] = None, simulink_stateflow_State66: set["Action"] = None, simulink_stateflow_State68: set["Action"] = None, simulink_stateflow_State71: set["Action"] = None, simulink_stateflow_State74: set["Data"] = None, simulink_stateflow_State77: set["Data"] = None, simulink_stateflow_State80: set["Action"] = None, Node: "simulink_stateflow_State" = None, Node83: "simulink_stateflow_Transition" = None, Node85: "simulink_stateflow_Transition" = None):
        self.subStateType = subStateType
        self.name = name
        self.priority = priority
        self.initial = initial
        self.parent59 = parent59 if parent59 is not None else set()
        self.simulink_stateflow_State = simulink_stateflow_State if simulink_stateflow_State is not None else set()
        self.simulink_stateflow_State62 = simulink_stateflow_State62 if simulink_stateflow_State62 is not None else set()
        self.simulink_stateflow_State64 = simulink_stateflow_State64 if simulink_stateflow_State64 is not None else set()
        self.simulink_stateflow_State66 = simulink_stateflow_State66 if simulink_stateflow_State66 is not None else set()
        self.simulink_stateflow_State68 = simulink_stateflow_State68 if simulink_stateflow_State68 is not None else set()
        self.simulink_stateflow_State71 = simulink_stateflow_State71 if simulink_stateflow_State71 is not None else set()
        self.simulink_stateflow_State74 = simulink_stateflow_State74 if simulink_stateflow_State74 is not None else set()
        self.simulink_stateflow_State77 = simulink_stateflow_State77 if simulink_stateflow_State77 is not None else set()
        self.simulink_stateflow_State80 = simulink_stateflow_State80 if simulink_stateflow_State80 is not None else set()
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def subStateType(self):
        return self.__subStateType

    @subStateType.setter
    def subStateType(self, subStateType: str):
        self.__subStateType = subStateType


    @property
    def initial(self):
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial


    @property
    def simulink_stateflow_State74(self):
        return self.__simulink_stateflow_State74

    @simulink_stateflow_State74.setter
    def simulink_stateflow_State74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State74", None)
        self.__simulink_stateflow_State74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data75"):
                    opp_val = getattr(item, "Data75", None)
                    
                    if opp_val == self:
                        setattr(item, "Data75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data75"):
                    opp_val = getattr(item, "Data75", None)
                    
                    setattr(item, "Data75", self)
                    

    @property
    def simulink_stateflow_State62(self):
        return self.__simulink_stateflow_State62

    @simulink_stateflow_State62.setter
    def simulink_stateflow_State62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State62", None)
        self.__simulink_stateflow_State62 = value if value is not None else set()
        
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
                    

    @property
    def parent59(self):
        return self.__parent59

    @parent59.setter
    def parent59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__parent59", None)
        self.__parent59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

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
    def simulink_stateflow_State77(self):
        return self.__simulink_stateflow_State77

    @simulink_stateflow_State77.setter
    def simulink_stateflow_State77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State77", None)
        self.__simulink_stateflow_State77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data78"):
                    opp_val = getattr(item, "Data78", None)
                    
                    if opp_val == self:
                        setattr(item, "Data78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data78"):
                    opp_val = getattr(item, "Data78", None)
                    
                    setattr(item, "Data78", self)
                    

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
                if hasattr(item, "Action69"):
                    opp_val = getattr(item, "Action69", None)
                    
                    if opp_val == self:
                        setattr(item, "Action69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action69"):
                    opp_val = getattr(item, "Action69", None)
                    
                    setattr(item, "Action69", self)
                    

    @property
    def simulink_stateflow_State71(self):
        return self.__simulink_stateflow_State71

    @simulink_stateflow_State71.setter
    def simulink_stateflow_State71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State71", None)
        self.__simulink_stateflow_State71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action72"):
                    opp_val = getattr(item, "Action72", None)
                    
                    if opp_val == self:
                        setattr(item, "Action72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action72"):
                    opp_val = getattr(item, "Action72", None)
                    
                    setattr(item, "Action72", self)
                    

    @property
    def simulink_stateflow_State80(self):
        return self.__simulink_stateflow_State80

    @simulink_stateflow_State80.setter
    def simulink_stateflow_State80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_State__simulink_stateflow_State80", None)
        self.__simulink_stateflow_State80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action81"):
                    opp_val = getattr(item, "Action81", None)
                    
                    if opp_val == self:
                        setattr(item, "Action81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action81"):
                    opp_val = getattr(item, "Action81", None)
                    
                    setattr(item, "Action81", self)
                    

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
                    

    def getSubState(self, simulink_name) :
        # TODO: Implement getSubState method
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
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


class simulink_stateflow_EmbeddedFunction(StateflowElement):

    def __init__(self, name: str, code: str, simulink_stateflow_EmbeddedFunction: set["Data"] = None, simulink_stateflow_EmbeddedFunction102: set["Data"] = None, simulink_stateflow_EmbeddedFunction105: set["Data"] = None, simulink_stateflow_EmbeddedFunction108: set["Data"] = None):
        self.name = name
        self.code = code
        self.simulink_stateflow_EmbeddedFunction = simulink_stateflow_EmbeddedFunction if simulink_stateflow_EmbeddedFunction is not None else set()
        self.simulink_stateflow_EmbeddedFunction102 = simulink_stateflow_EmbeddedFunction102 if simulink_stateflow_EmbeddedFunction102 is not None else set()
        self.simulink_stateflow_EmbeddedFunction105 = simulink_stateflow_EmbeddedFunction105 if simulink_stateflow_EmbeddedFunction105 is not None else set()
        self.simulink_stateflow_EmbeddedFunction108 = simulink_stateflow_EmbeddedFunction108 if simulink_stateflow_EmbeddedFunction108 is not None else set()
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def simulink_stateflow_EmbeddedFunction108(self):
        return self.__simulink_stateflow_EmbeddedFunction108

    @simulink_stateflow_EmbeddedFunction108.setter
    def simulink_stateflow_EmbeddedFunction108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_EmbeddedFunction__simulink_stateflow_EmbeddedFunction108", None)
        self.__simulink_stateflow_EmbeddedFunction108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data109"):
                    opp_val = getattr(item, "Data109", None)
                    
                    if opp_val == self:
                        setattr(item, "Data109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data109"):
                    opp_val = getattr(item, "Data109", None)
                    
                    setattr(item, "Data109", self)
                    

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
                if hasattr(item, "Data100"):
                    opp_val = getattr(item, "Data100", None)
                    
                    if opp_val == self:
                        setattr(item, "Data100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data100"):
                    opp_val = getattr(item, "Data100", None)
                    
                    setattr(item, "Data100", self)
                    

    @property
    def simulink_stateflow_EmbeddedFunction105(self):
        return self.__simulink_stateflow_EmbeddedFunction105

    @simulink_stateflow_EmbeddedFunction105.setter
    def simulink_stateflow_EmbeddedFunction105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_EmbeddedFunction__simulink_stateflow_EmbeddedFunction105", None)
        self.__simulink_stateflow_EmbeddedFunction105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data106"):
                    opp_val = getattr(item, "Data106", None)
                    
                    if opp_val == self:
                        setattr(item, "Data106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data106"):
                    opp_val = getattr(item, "Data106", None)
                    
                    setattr(item, "Data106", self)
                    

    @property
    def simulink_stateflow_EmbeddedFunction102(self):
        return self.__simulink_stateflow_EmbeddedFunction102

    @simulink_stateflow_EmbeddedFunction102.setter
    def simulink_stateflow_EmbeddedFunction102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_EmbeddedFunction__simulink_stateflow_EmbeddedFunction102", None)
        self.__simulink_stateflow_EmbeddedFunction102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data103"):
                    opp_val = getattr(item, "Data103", None)
                    
                    if opp_val == self:
                        setattr(item, "Data103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data103"):
                    opp_val = getattr(item, "Data103", None)
                    
                    setattr(item, "Data103", self)
                    

class simulink_stateflow_Event(StateflowElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class simulink_stateflow_Data(StateflowElement):

    def __init__(self, name: str, type: str, value: str, size: str):
        self.name = name
        self.type = type
        self.value = value
        self.size = size
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


class simulink_stateflow_Transition(StateflowElement):

    def __init__(self, priority: int, simulink_stateflow_Transition89: set["Action"] = None, simulink_stateflow_Transition92: set["Action"] = None, outgoing: "Node" = None, incoming: "Node" = None, simulink_stateflow_Transition: "Event" = None):
        self.priority = priority
        self.simulink_stateflow_Transition89 = simulink_stateflow_Transition89 if simulink_stateflow_Transition89 is not None else set()
        self.simulink_stateflow_Transition92 = simulink_stateflow_Transition92 if simulink_stateflow_Transition92 is not None else set()
        self.outgoing = outgoing
        self.incoming = incoming
        self.simulink_stateflow_Transition = simulink_stateflow_Transition
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node85"):
                opp_val = getattr(old_value, "Node85", None)
                if opp_val == self:
                    setattr(old_value, "Node85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node85"):
                opp_val = getattr(value, "Node85", None)
                setattr(value, "Node85", self)

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
            if hasattr(old_value, "Event87"):
                opp_val = getattr(old_value, "Event87", None)
                if opp_val == self:
                    setattr(old_value, "Event87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Event87"):
                opp_val = getattr(value, "Event87", None)
                setattr(value, "Event87", self)

    @property
    def simulink_stateflow_Transition92(self):
        return self.__simulink_stateflow_Transition92

    @simulink_stateflow_Transition92.setter
    def simulink_stateflow_Transition92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_Transition__simulink_stateflow_Transition92", None)
        self.__simulink_stateflow_Transition92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action93"):
                    opp_val = getattr(item, "Action93", None)
                    
                    if opp_val == self:
                        setattr(item, "Action93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action93"):
                    opp_val = getattr(item, "Action93", None)
                    
                    setattr(item, "Action93", self)
                    

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node83"):
                opp_val = getattr(old_value, "Node83", None)
                if opp_val == self:
                    setattr(old_value, "Node83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node83"):
                opp_val = getattr(value, "Node83", None)
                setattr(value, "Node83", self)

    @property
    def simulink_stateflow_Transition89(self):
        return self.__simulink_stateflow_Transition89

    @simulink_stateflow_Transition89.setter
    def simulink_stateflow_Transition89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simulink_stateflow_Transition__simulink_stateflow_Transition89", None)
        self.__simulink_stateflow_Transition89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action90"):
                    opp_val = getattr(item, "Action90", None)
                    
                    if opp_val == self:
                        setattr(item, "Action90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action90"):
                    opp_val = getattr(item, "Action90", None)
                    
                    setattr(item, "Action90", self)
                    

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
        
        pass
    @property
    def triggerInput(self):
        return self.__triggerInput

    @triggerInput.setter
    def triggerInput(self, triggerInput: str):
        self.__triggerInput = triggerInput


class stateflow_simulink_ChartBlock:

    pass
class simulink_BusElement:

    def __init__(self, name: str, dimensions: str, type: str, simulink_BusElement: "simulink_Bus" = None, simulink_BusElement46: "simulink_Bus" = None):
        self.name = name
        self.dimensions = dimensions
        self.type = type
        self.simulink_BusElement = simulink_BusElement
        self.simulink_BusElement46 = simulink_BusElement46
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions


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

class Chart:

    pass
class PortBlock:

    pass
class StateflowMachine:

    pass
class SubSystem:

    pass
class simulink_SimulinkFile(SubSystem):

    pass
class Block:

    pass
class simulink_DigitalClock(Block):

    def __init__(self, sampleTime: float):
        self.sampleTime = sampleTime
        
        pass
    @property
    def sampleTime(self):
        return self.__sampleTime

    @sampleTime.setter
    def sampleTime(self, sampleTime: float):
        self.__sampleTime = sampleTime


class simulink_ChartBlock(Block):

    pass
class simulink_reconfiguration_MultiTargetControl(Block):

    pass
class simulink_reconfiguration_FadingComponent(Block):

    def __init__(self, time: int):
        self.time = time
        
        pass
    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time


class simulink_EmbeddedMatlabFunction(Block):

    def __init__(self, code: str):
        self.code = code
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


class simulink_msglib_CommunicationSwitch(Block):

    def __init__(self, debug: int):
        self.debug = debug
        
        pass
    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, debug: int):
        self.__debug = debug


class simulink_BusSelector(Block):

    pass
class simulink_ZeroOrderHold(Block):

    def __init__(self, sampleTime: str):
        self.sampleTime = sampleTime
        
        pass
    @property
    def sampleTime(self):
        return self.__sampleTime

    @sampleTime.setter
    def sampleTime(self, sampleTime: str):
        self.__sampleTime = sampleTime


class simulink_Constant(Block):

    def __init__(self, value: str, type: str):
        self.value = value
        self.type = type
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class simulink_MiscBlock(Block):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class simulink_UnitDelay(Block):

    pass
class simulink_msglib_LinkLayer(Block):

    def __init__(self, delayMin: str, delayMax: str, messageLossProbability: int, messageRetransmission: bool, bufferOverflowPossible: bool, bufferSize: int, sourceBufferSize: int, messageMapping: str):
        self.delayMin = delayMin
        self.delayMax = delayMax
        self.messageLossProbability = messageLossProbability
        self.messageRetransmission = messageRetransmission
        self.bufferOverflowPossible = bufferOverflowPossible
        self.bufferSize = bufferSize
        self.sourceBufferSize = sourceBufferSize
        self.messageMapping = messageMapping
        
        pass
    @property
    def sourceBufferSize(self):
        return self.__sourceBufferSize

    @sourceBufferSize.setter
    def sourceBufferSize(self, sourceBufferSize: int):
        self.__sourceBufferSize = sourceBufferSize


    @property
    def bufferOverflowPossible(self):
        return self.__bufferOverflowPossible

    @bufferOverflowPossible.setter
    def bufferOverflowPossible(self, bufferOverflowPossible: bool):
        self.__bufferOverflowPossible = bufferOverflowPossible


    @property
    def messageLossProbability(self):
        return self.__messageLossProbability

    @messageLossProbability.setter
    def messageLossProbability(self, messageLossProbability: int):
        self.__messageLossProbability = messageLossProbability


    @property
    def bufferSize(self):
        return self.__bufferSize

    @bufferSize.setter
    def bufferSize(self, bufferSize: int):
        self.__bufferSize = bufferSize


    @property
    def messageMapping(self):
        return self.__messageMapping

    @messageMapping.setter
    def messageMapping(self, messageMapping: str):
        self.__messageMapping = messageMapping


    @property
    def delayMin(self):
        return self.__delayMin

    @delayMin.setter
    def delayMin(self, delayMin: str):
        self.__delayMin = delayMin


    @property
    def delayMax(self):
        return self.__delayMax

    @delayMax.setter
    def delayMax(self, delayMax: str):
        self.__delayMax = delayMax


    @property
    def messageRetransmission(self):
        return self.__messageRetransmission

    @messageRetransmission.setter
    def messageRetransmission(self, messageRetransmission: bool):
        self.__messageRetransmission = messageRetransmission


class simulink_reconfiguration_MultiSourceControl(Block):

    pass
class simulink_BusCreator(Block):

    pass
class simulink_PortBlock(Block):

    def __init__(self, dimensions: str, type: str, initialCondition: str):
        self.dimensions = dimensions
        self.type = type
        self.initialCondition = initialCondition
        
        pass
    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions: str):
        self.__dimensions = dimensions


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def initialCondition(self):
        return self.__initialCondition

    @initialCondition.setter
    def initialCondition(self, initialCondition: str):
        self.__initialCondition = initialCondition


class simulink_LibraryReference(Block):

    pass
class simulink_Parameter:

    def __init__(self, name: str, value: str, type: str, simulink_Parameter: "simulink_Element" = None):
        self.name = name
        self.value = value
        self.type = type
        self.simulink_Parameter = simulink_Parameter
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def type(self):
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
        
        pass
    @property
    def id(self):
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
                    

    def getParameter(self, simulink_name) :
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
class Element:

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
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

class simulink_SimulinkContainer(Element):

    pass
class simulink_Line(Element):

    pass
class simulink_Block(Element):

    def __init__(self, name: str, Block: "simulink_Line" = None, Block14: "simulink_Line" = None, Block20: "simulink_SubSystem" = None, simulink_Block: "simulink_SubSystem" = None, Block27: "simulink_InPortBlock" = None, simulink_Block31: "simulink_LibraryReference" = None, blocks: "simulink_SubSystem" = None, block: set["simulink_OutPortBlock"] = None, block3: set["simulink_InPortBlock"] = None, targetBlock: set["simulink_Line"] = None, sourceBlock: set["simulink_Line"] = None, Block36: "simulink_OutPortBlock" = None):
        self.name = name
        self.Block = Block
        self.Block14 = Block14
        self.Block20 = Block20
        self.simulink_Block = simulink_Block
        self.Block27 = Block27
        self.simulink_Block31 = simulink_Block31
        self.blocks = blocks
        self.block = block if block is not None else set()
        self.block3 = block3 if block3 is not None else set()
        self.targetBlock = targetBlock if targetBlock is not None else set()
        self.sourceBlock = sourceBlock if sourceBlock is not None else set()
        self.Block36 = Block36
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

    def getFullyQualifiedName(self) :
        # TODO: Implement getFullyQualifiedName method
        pass

class simulink_SubSystem(Block):

    def __init__(self, simulink_SubSystem: set["simulink_Line"] = None, parent: set["simulink_Block"] = None, simulink_SubSystem23: "simulink_SubSystem" = None, simulink_SubSystem21: set["simulink_SubSystem"] = None, simulink_SubSystem25: set["simulink_Block"] = None, SubSystem: "simulink_Block" = None):
        self.simulink_SubSystem = simulink_SubSystem if simulink_SubSystem is not None else set()
        self.parent = parent if parent is not None else set()
        self.simulink_SubSystem23 = simulink_SubSystem23
        self.simulink_SubSystem21 = simulink_SubSystem21 if simulink_SubSystem21 is not None else set()
        self.simulink_SubSystem25 = simulink_SubSystem25 if simulink_SubSystem25 is not None else set()
        self.SubSystem = SubSystem
        
        pass
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
                    

    def getBlockByName(self, simulink_name) :
        # TODO: Implement getBlockByName method
        pass
