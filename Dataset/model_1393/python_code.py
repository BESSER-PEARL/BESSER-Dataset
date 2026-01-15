from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class IOTypes(Enum):
    local = "local"
    output = "output"
    input = "input"
class DataTypes(Enum):
    int = "int"
    double = "double"
    boolean = "boolean"
class PseudoTypes(Enum):
    join = "join"
    fork = "fork"
    junction = "junction"
    choice = "choice"
    entryPoint = "entryPoint"
    exitPoint = "exitPoint"
    terminate = "terminate"
    initial = "initial"
    deepHistory = "deepHistory"
    shallowHistory = "shallowHistory"
class TriggerTypes(Enum):
    either = "either"
    rising = "rising"
    falling = "falling"
    functionCall = "functionCall"


############################################
# Definition of Classes
############################################

class statemachine_Statechart:

    def __init__(self, name: str, UUID: str, statemachine_Statechart: set["statemachine_DataElement"] = None, statemachine_Statechart10: set["statemachine_Region"] = None, statemachine_Statechart13: set["statemachine_Transition"] = None):
        self.name = name
        self.UUID = UUID
        self.statemachine_Statechart = statemachine_Statechart if statemachine_Statechart is not None else set()
        self.statemachine_Statechart10 = statemachine_Statechart10 if statemachine_Statechart10 is not None else set()
        self.statemachine_Statechart13 = statemachine_Statechart13 if statemachine_Statechart13 is not None else set()
        
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
    def statemachine_Statechart13(self):
        return self.__statemachine_Statechart13

    @statemachine_Statechart13.setter
    def statemachine_Statechart13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statechart__statemachine_Statechart13", None)
        self.__statemachine_Statechart13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Transition14"):
                    opp_val = getattr(item, "statemachine_Transition14", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Transition14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Transition14"):
                    opp_val = getattr(item, "statemachine_Transition14", None)
                    
                    setattr(item, "statemachine_Transition14", self)
                    

    @property
    def statemachine_Statechart(self):
        return self.__statemachine_Statechart

    @statemachine_Statechart.setter
    def statemachine_Statechart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statechart__statemachine_Statechart", None)
        self.__statemachine_Statechart = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_DataElement"):
                    opp_val = getattr(item, "statemachine_DataElement", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_DataElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_DataElement"):
                    opp_val = getattr(item, "statemachine_DataElement", None)
                    
                    setattr(item, "statemachine_DataElement", self)
                    

    @property
    def statemachine_Statechart10(self):
        return self.__statemachine_Statechart10

    @statemachine_Statechart10.setter
    def statemachine_Statechart10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statechart__statemachine_Statechart10", None)
        self.__statemachine_Statechart10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Region11"):
                    opp_val = getattr(item, "statemachine_Region11", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Region11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Region11"):
                    opp_val = getattr(item, "statemachine_Region11", None)
                    
                    setattr(item, "statemachine_Region11", self)
                    

class State:

    pass
class statemachine_FinalState(State):

    pass
class statemachine_DataElement:

    def __init__(self, name: str, ioType: str, port: int, statemachine_DataElement: "statemachine_Statechart" = None):
        self.name = name
        self.ioType = ioType
        self.port = port
        self.statemachine_DataElement = statemachine_DataElement
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioType(self) -> str:
        return self.__ioType

    @ioType.setter
    def ioType(self, ioType: str):
        self.__ioType = ioType

    @property
    def statemachine_DataElement(self):
        return self.__statemachine_DataElement

    @statemachine_DataElement.setter
    def statemachine_DataElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_DataElement__statemachine_DataElement", None)
        self.__statemachine_DataElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statechart"):
                opp_val = getattr(old_value, "statemachine_Statechart", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statechart"):
                opp_val = getattr(value, "statemachine_Statechart", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statechart", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DataElement:

    pass
class statemachine_Event(DataElement):

    def __init__(self, trigger: str):
        self.trigger = trigger
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

class statemachine_Variable(DataElement):

    def __init__(self, dataType: str):
        self.dataType = dataType
        
    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

class statemachine_Transition:

    def __init__(self, expression: str, id: int, priority: int, statemachine_Transition4: "statemachine_Node" = None, statemachine_Transition: "statemachine_Node" = None, statemachine_Transition14: "statemachine_Statechart" = None):
        self.expression = expression
        self.id = id
        self.priority = priority
        self.statemachine_Transition4 = statemachine_Transition4
        self.statemachine_Transition = statemachine_Transition
        self.statemachine_Transition14 = statemachine_Transition14
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def statemachine_Transition(self):
        return self.__statemachine_Transition

    @statemachine_Transition.setter
    def statemachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition", None)
        self.__statemachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Node2"):
                opp_val = getattr(old_value, "statemachine_Node2", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Node2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Node2"):
                opp_val = getattr(value, "statemachine_Node2", None)
                setattr(value, "statemachine_Node2", self)

    @property
    def statemachine_Transition4(self):
        return self.__statemachine_Transition4

    @statemachine_Transition4.setter
    def statemachine_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition4", None)
        self.__statemachine_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Node5"):
                opp_val = getattr(old_value, "statemachine_Node5", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Node5"):
                opp_val = getattr(value, "statemachine_Node5", None)
                setattr(value, "statemachine_Node5", self)

    @property
    def statemachine_Transition14(self):
        return self.__statemachine_Transition14

    @statemachine_Transition14.setter
    def statemachine_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition14", None)
        self.__statemachine_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statechart13"):
                opp_val = getattr(old_value, "statemachine_Statechart13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statechart13"):
                opp_val = getattr(value, "statemachine_Statechart13", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statechart13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Node:

    pass
class statemachine_Pseudostate(Node):

    def __init__(self, pseudoType: str):
        self.pseudoType = pseudoType
        
    @property
    def pseudoType(self) -> str:
        return self.__pseudoType

    @pseudoType.setter
    def pseudoType(self, pseudoType: str):
        self.__pseudoType = pseudoType

class statemachine_State(Node):

    def __init__(self, entry: str, do: str, exit: str, statemachine_State: set["statemachine_Region"] = None):
        self.entry = entry
        self.do = do
        self.exit = exit
        self.statemachine_State = statemachine_State if statemachine_State is not None else set()
        
    @property
    def entry(self) -> str:
        return self.__entry

    @entry.setter
    def entry(self, entry: str):
        self.__entry = entry

    @property
    def exit(self) -> str:
        return self.__exit

    @exit.setter
    def exit(self, exit: str):
        self.__exit = exit

    @property
    def do(self) -> str:
        return self.__do

    @do.setter
    def do(self, do: str):
        self.__do = do

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Region7"):
                    opp_val = getattr(item, "statemachine_Region7", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Region7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Region7"):
                    opp_val = getattr(item, "statemachine_Region7", None)
                    
                    setattr(item, "statemachine_Region7", self)
                    

class statemachine_Node:

    def __init__(self, name: str, id: int, statemachine_Node: "statemachine_Region" = None, statemachine_Node5: "statemachine_Transition" = None, statemachine_Node2: "statemachine_Transition" = None):
        self.name = name
        self.id = id
        self.statemachine_Node = statemachine_Node
        self.statemachine_Node5 = statemachine_Node5
        self.statemachine_Node2 = statemachine_Node2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def statemachine_Node5(self):
        return self.__statemachine_Node5

    @statemachine_Node5.setter
    def statemachine_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Node__statemachine_Node5", None)
        self.__statemachine_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition4"):
                opp_val = getattr(old_value, "statemachine_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition4"):
                opp_val = getattr(value, "statemachine_Transition4", None)
                setattr(value, "statemachine_Transition4", self)

    @property
    def statemachine_Node2(self):
        return self.__statemachine_Node2

    @statemachine_Node2.setter
    def statemachine_Node2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Node__statemachine_Node2", None)
        self.__statemachine_Node2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition"):
                opp_val = getattr(old_value, "statemachine_Transition", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition"):
                opp_val = getattr(value, "statemachine_Transition", None)
                setattr(value, "statemachine_Transition", self)

    @property
    def statemachine_Node(self):
        return self.__statemachine_Node

    @statemachine_Node.setter
    def statemachine_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Node__statemachine_Node", None)
        self.__statemachine_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Region"):
                opp_val = getattr(old_value, "statemachine_Region", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Region"):
                opp_val = getattr(value, "statemachine_Region", None)
                if opp_val is None:
                    setattr(value, "statemachine_Region", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_Region:

    def __init__(self, priority: int, statemachine_Region: set["statemachine_Node"] = None, statemachine_Region7: "statemachine_State" = None, statemachine_Region11: "statemachine_Statechart" = None):
        self.priority = priority
        self.statemachine_Region = statemachine_Region if statemachine_Region is not None else set()
        self.statemachine_Region7 = statemachine_Region7
        self.statemachine_Region11 = statemachine_Region11
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def statemachine_Region(self):
        return self.__statemachine_Region

    @statemachine_Region.setter
    def statemachine_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Region__statemachine_Region", None)
        self.__statemachine_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Node"):
                    opp_val = getattr(item, "statemachine_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Node"):
                    opp_val = getattr(item, "statemachine_Node", None)
                    
                    setattr(item, "statemachine_Node", self)
                    

    @property
    def statemachine_Region11(self):
        return self.__statemachine_Region11

    @statemachine_Region11.setter
    def statemachine_Region11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Region__statemachine_Region11", None)
        self.__statemachine_Region11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statechart10"):
                opp_val = getattr(old_value, "statemachine_Statechart10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statechart10"):
                opp_val = getattr(value, "statemachine_Statechart10", None)
                if opp_val is None:
                    setattr(value, "statemachine_Statechart10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_Region7(self):
        return self.__statemachine_Region7

    @statemachine_Region7.setter
    def statemachine_Region7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Region__statemachine_Region7", None)
        self.__statemachine_Region7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State"):
                opp_val = getattr(old_value, "statemachine_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State"):
                opp_val = getattr(value, "statemachine_State", None)
                if opp_val is None:
                    setattr(value, "statemachine_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
