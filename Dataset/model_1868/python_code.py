from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class statesml_ChangeExpression:

    def __init__(self, fulfilled: bool, statesml_ChangeExpression: "statesml_ChangeEvent" = None, statesml_ChangeExpression59: "statesml_Function" = None, statesml_ChangeExpression62: set["statesml_IncomingParameter"] = None):
        self.fulfilled = fulfilled
        self.statesml_ChangeExpression = statesml_ChangeExpression
        self.statesml_ChangeExpression59 = statesml_ChangeExpression59
        self.statesml_ChangeExpression62 = statesml_ChangeExpression62 if statesml_ChangeExpression62 is not None else set()
        
    @property
    def fulfilled(self) -> bool:
        return self.__fulfilled

    @fulfilled.setter
    def fulfilled(self, fulfilled: bool):
        self.__fulfilled = fulfilled

    @property
    def statesml_ChangeExpression(self):
        return self.__statesml_ChangeExpression

    @statesml_ChangeExpression.setter
    def statesml_ChangeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_ChangeExpression__statesml_ChangeExpression", None)
        self.__statesml_ChangeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_ChangeEvent"):
                opp_val = getattr(old_value, "statesml_ChangeEvent", None)
                if opp_val == self:
                    setattr(old_value, "statesml_ChangeEvent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_ChangeEvent"):
                opp_val = getattr(value, "statesml_ChangeEvent", None)
                setattr(value, "statesml_ChangeEvent", self)

    @property
    def statesml_ChangeExpression62(self):
        return self.__statesml_ChangeExpression62

    @statesml_ChangeExpression62.setter
    def statesml_ChangeExpression62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_ChangeExpression__statesml_ChangeExpression62", None)
        self.__statesml_ChangeExpression62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_IncomingParameter63"):
                    opp_val = getattr(item, "statesml_IncomingParameter63", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_IncomingParameter63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_IncomingParameter63"):
                    opp_val = getattr(item, "statesml_IncomingParameter63", None)
                    
                    setattr(item, "statesml_IncomingParameter63", self)
                    

    @property
    def statesml_ChangeExpression59(self):
        return self.__statesml_ChangeExpression59

    @statesml_ChangeExpression59.setter
    def statesml_ChangeExpression59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_ChangeExpression__statesml_ChangeExpression59", None)
        self.__statesml_ChangeExpression59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Function60"):
                opp_val = getattr(old_value, "statesml_Function60", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Function60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Function60"):
                opp_val = getattr(value, "statesml_Function60", None)
                setattr(value, "statesml_Function60", self)

class Event:

    pass
class statesml_ChangeEvent(Event):

    pass
class Parameter:

    pass
class State:

    pass
class statesml_TerminalState(State):

    pass
class statesml_MiddleState(State):

    pass
class statesml_InitialState(State):

    pass
class DataType:

    pass
class statesml_Boolean(DataType):

    pass
class statesml_Integer(DataType):

    pass
class statesml_String(DataType):

    pass
class statesml_ParameterValue:

    pass
class statesml_Trigger:

    pass
class statesml_FunctionCall:

    pass
class Node:

    pass
class statesml_SelectionConvergence(Node):

    pass
class statesml_SelectionDivergence(Node):

    pass
class statesml_Transition(Node):

    pass
class statesml_State(Node):

    pass
class statesml_StateSystem:

    pass
class statesml_Event(ABC):

    def __init__(self, name: str, statesml_Event: "statesml_StateSystem" = None, statesml_Event48: "statesml_Trigger" = None):
        self.name = name
        self.statesml_Event = statesml_Event
        self.statesml_Event48 = statesml_Event48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_Event(self):
        return self.__statesml_Event

    @statesml_Event.setter
    def statesml_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Event__statesml_Event", None)
        self.__statesml_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StateSystem37"):
                opp_val = getattr(old_value, "statesml_StateSystem37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StateSystem37"):
                opp_val = getattr(value, "statesml_StateSystem37", None)
                if opp_val is None:
                    setattr(value, "statesml_StateSystem37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Event48(self):
        return self.__statesml_Event48

    @statesml_Event48.setter
    def statesml_Event48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Event__statesml_Event48", None)
        self.__statesml_Event48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Trigger47"):
                opp_val = getattr(old_value, "statesml_Trigger47", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Trigger47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Trigger47"):
                opp_val = getattr(value, "statesml_Trigger47", None)
                setattr(value, "statesml_Trigger47", self)

class statesml_Edge:

    def __init__(self, name: str, statesml_Edge: "statesml_StateSystem" = None, Edge: "statesml_Node" = None, Edge40: "statesml_Node" = None, outgoing: "statesml_Node" = None, incoming: "statesml_Node" = None):
        self.name = name
        self.statesml_Edge = statesml_Edge
        self.Edge = Edge
        self.Edge40 = Edge40
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Edge40(self):
        return self.__Edge40

    @Edge40.setter
    def Edge40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Edge__Edge40", None)
        self.__Edge40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Edge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node43"):
                opp_val = getattr(old_value, "Node43", None)
                if opp_val == self:
                    setattr(old_value, "Node43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node43"):
                opp_val = getattr(value, "Node43", None)
                setattr(value, "Node43", self)

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Edge__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def statesml_Edge(self):
        return self.__statesml_Edge

    @statesml_Edge.setter
    def statesml_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Edge__statesml_Edge", None)
        self.__statesml_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StateSystem32"):
                opp_val = getattr(old_value, "statesml_StateSystem32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StateSystem32"):
                opp_val = getattr(value, "statesml_StateSystem32", None)
                if opp_val is None:
                    setattr(value, "statesml_StateSystem32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_Node(ABC):

    def __init__(self, name: str, statesml_Node: "statesml_StateSystem" = None, source: set["statesml_Edge"] = None, target: set["statesml_Edge"] = None, Node: "statesml_Edge" = None, Node43: "statesml_Edge" = None):
        self.name = name
        self.statesml_Node = statesml_Node
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.Node = Node
        self.Node43 = Node43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    setattr(item, "Edge", self)
                    

    @property
    def Node43(self):
        return self.__Node43

    @Node43.setter
    def Node43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Node__Node43", None)
        self.__Node43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def statesml_Node(self):
        return self.__statesml_Node

    @statesml_Node.setter
    def statesml_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Node__statesml_Node", None)
        self.__statesml_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StateSystem30"):
                opp_val = getattr(old_value, "statesml_StateSystem30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StateSystem30"):
                opp_val = getattr(value, "statesml_StateSystem30", None)
                if opp_val is None:
                    setattr(value, "statesml_StateSystem30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge40"):
                    opp_val = getattr(item, "Edge40", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge40"):
                    opp_val = getattr(item, "Edge40", None)
                    
                    setattr(item, "Edge40", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

class statesml_Parameter(ABC):

    def __init__(self, name: str, statesml_Parameter: "statesml_DataType" = None):
        self.name = name
        self.statesml_Parameter = statesml_Parameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_Parameter(self):
        return self.__statesml_Parameter

    @statesml_Parameter.setter
    def statesml_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Parameter__statesml_Parameter", None)
        self.__statesml_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_DataType26"):
                opp_val = getattr(old_value, "statesml_DataType26", None)
                if opp_val == self:
                    setattr(old_value, "statesml_DataType26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_DataType26"):
                opp_val = getattr(value, "statesml_DataType26", None)
                setattr(value, "statesml_DataType26", self)

class statesml_IncomingParameter(Parameter):

    pass
class statesml_ReturnParameter(Parameter):

    pass
class statesml_SystemUnit:

    def __init__(self, name: str, statesml_SystemUnit: "statesml_SystemUnitLibrary" = None, statesml_SystemUnit11: "statesml_StateSystemModel" = None, statesml_SystemUnit13: set["statesml_Attribute"] = None, statesml_SystemUnit16: set["statesml_Function"] = None):
        self.name = name
        self.statesml_SystemUnit = statesml_SystemUnit
        self.statesml_SystemUnit11 = statesml_SystemUnit11
        self.statesml_SystemUnit13 = statesml_SystemUnit13 if statesml_SystemUnit13 is not None else set()
        self.statesml_SystemUnit16 = statesml_SystemUnit16 if statesml_SystemUnit16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_SystemUnit(self):
        return self.__statesml_SystemUnit

    @statesml_SystemUnit.setter
    def statesml_SystemUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnit__statesml_SystemUnit", None)
        self.__statesml_SystemUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SystemUnitLibrary9"):
                opp_val = getattr(old_value, "statesml_SystemUnitLibrary9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnitLibrary9"):
                opp_val = getattr(value, "statesml_SystemUnitLibrary9", None)
                if opp_val is None:
                    setattr(value, "statesml_SystemUnitLibrary9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_SystemUnit11(self):
        return self.__statesml_SystemUnit11

    @statesml_SystemUnit11.setter
    def statesml_SystemUnit11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnit__statesml_SystemUnit11", None)
        self.__statesml_SystemUnit11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StateSystemModel"):
                opp_val = getattr(old_value, "statesml_StateSystemModel", None)
                if opp_val == self:
                    setattr(old_value, "statesml_StateSystemModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StateSystemModel"):
                opp_val = getattr(value, "statesml_StateSystemModel", None)
                setattr(value, "statesml_StateSystemModel", self)

    @property
    def statesml_SystemUnit16(self):
        return self.__statesml_SystemUnit16

    @statesml_SystemUnit16.setter
    def statesml_SystemUnit16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnit__statesml_SystemUnit16", None)
        self.__statesml_SystemUnit16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_Function17"):
                    opp_val = getattr(item, "statesml_Function17", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_Function17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_Function17"):
                    opp_val = getattr(item, "statesml_Function17", None)
                    
                    setattr(item, "statesml_Function17", self)
                    

    @property
    def statesml_SystemUnit13(self):
        return self.__statesml_SystemUnit13

    @statesml_SystemUnit13.setter
    def statesml_SystemUnit13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnit__statesml_SystemUnit13", None)
        self.__statesml_SystemUnit13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_Attribute14"):
                    opp_val = getattr(item, "statesml_Attribute14", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_Attribute14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_Attribute14"):
                    opp_val = getattr(item, "statesml_Attribute14", None)
                    
                    setattr(item, "statesml_Attribute14", self)
                    

class statesml_Function:

    def __init__(self, name: str, statesml_Function: "statesml_DataType" = None, statesml_Function22: "statesml_ReturnParameter" = None, statesml_Function24: set["statesml_IncomingParameter"] = None, statesml_Function17: "statesml_SystemUnit" = None, statesml_Function54: "statesml_FunctionCall" = None, statesml_Function60: "statesml_ChangeExpression" = None):
        self.name = name
        self.statesml_Function = statesml_Function
        self.statesml_Function22 = statesml_Function22
        self.statesml_Function24 = statesml_Function24 if statesml_Function24 is not None else set()
        self.statesml_Function17 = statesml_Function17
        self.statesml_Function54 = statesml_Function54
        self.statesml_Function60 = statesml_Function60
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_Function22(self):
        return self.__statesml_Function22

    @statesml_Function22.setter
    def statesml_Function22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function22", None)
        self.__statesml_Function22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_ReturnParameter"):
                opp_val = getattr(old_value, "statesml_ReturnParameter", None)
                if opp_val == self:
                    setattr(old_value, "statesml_ReturnParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_ReturnParameter"):
                opp_val = getattr(value, "statesml_ReturnParameter", None)
                setattr(value, "statesml_ReturnParameter", self)

    @property
    def statesml_Function54(self):
        return self.__statesml_Function54

    @statesml_Function54.setter
    def statesml_Function54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function54", None)
        self.__statesml_Function54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_FunctionCall53"):
                opp_val = getattr(old_value, "statesml_FunctionCall53", None)
                if opp_val == self:
                    setattr(old_value, "statesml_FunctionCall53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_FunctionCall53"):
                opp_val = getattr(value, "statesml_FunctionCall53", None)
                setattr(value, "statesml_FunctionCall53", self)

    @property
    def statesml_Function17(self):
        return self.__statesml_Function17

    @statesml_Function17.setter
    def statesml_Function17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function17", None)
        self.__statesml_Function17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SystemUnit16"):
                opp_val = getattr(old_value, "statesml_SystemUnit16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnit16"):
                opp_val = getattr(value, "statesml_SystemUnit16", None)
                if opp_val is None:
                    setattr(value, "statesml_SystemUnit16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Function60(self):
        return self.__statesml_Function60

    @statesml_Function60.setter
    def statesml_Function60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function60", None)
        self.__statesml_Function60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_ChangeExpression59"):
                opp_val = getattr(old_value, "statesml_ChangeExpression59", None)
                if opp_val == self:
                    setattr(old_value, "statesml_ChangeExpression59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_ChangeExpression59"):
                opp_val = getattr(value, "statesml_ChangeExpression59", None)
                setattr(value, "statesml_ChangeExpression59", self)

    @property
    def statesml_Function24(self):
        return self.__statesml_Function24

    @statesml_Function24.setter
    def statesml_Function24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function24", None)
        self.__statesml_Function24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_IncomingParameter"):
                    opp_val = getattr(item, "statesml_IncomingParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_IncomingParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_IncomingParameter"):
                    opp_val = getattr(item, "statesml_IncomingParameter", None)
                    
                    setattr(item, "statesml_IncomingParameter", self)
                    

    @property
    def statesml_Function(self):
        return self.__statesml_Function

    @statesml_Function.setter
    def statesml_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function", None)
        self.__statesml_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_DataType7"):
                opp_val = getattr(old_value, "statesml_DataType7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_DataType7"):
                opp_val = getattr(value, "statesml_DataType7", None)
                if opp_val is None:
                    setattr(value, "statesml_DataType7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_StateSystemModel:

    def __init__(self, name: str, statesml_StateSystemModel: "statesml_SystemUnit" = None, statesml_StateSystemModel28: "statesml_StateSystem" = None):
        self.name = name
        self.statesml_StateSystemModel = statesml_StateSystemModel
        self.statesml_StateSystemModel28 = statesml_StateSystemModel28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_StateSystemModel28(self):
        return self.__statesml_StateSystemModel28

    @statesml_StateSystemModel28.setter
    def statesml_StateSystemModel28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_StateSystemModel__statesml_StateSystemModel28", None)
        self.__statesml_StateSystemModel28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StateSystem"):
                opp_val = getattr(old_value, "statesml_StateSystem", None)
                if opp_val == self:
                    setattr(old_value, "statesml_StateSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StateSystem"):
                opp_val = getattr(value, "statesml_StateSystem", None)
                setattr(value, "statesml_StateSystem", self)

    @property
    def statesml_StateSystemModel(self):
        return self.__statesml_StateSystemModel

    @statesml_StateSystemModel.setter
    def statesml_StateSystemModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_StateSystemModel__statesml_StateSystemModel", None)
        self.__statesml_StateSystemModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SystemUnit11"):
                opp_val = getattr(old_value, "statesml_SystemUnit11", None)
                if opp_val == self:
                    setattr(old_value, "statesml_SystemUnit11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnit11"):
                opp_val = getattr(value, "statesml_SystemUnit11", None)
                setattr(value, "statesml_SystemUnit11", self)

class statesml_DataType(ABC):

    def __init__(self, name: str, statesml_DataType: "statesml_Attribute" = None, statesml_DataType7: set["statesml_Function"] = None, statesml_DataType26: "statesml_Parameter" = None, statesml_DataType20: "statesml_DataTypeLibrary" = None):
        self.name = name
        self.statesml_DataType = statesml_DataType
        self.statesml_DataType7 = statesml_DataType7 if statesml_DataType7 is not None else set()
        self.statesml_DataType26 = statesml_DataType26
        self.statesml_DataType20 = statesml_DataType20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_DataType20(self):
        return self.__statesml_DataType20

    @statesml_DataType20.setter
    def statesml_DataType20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataType__statesml_DataType20", None)
        self.__statesml_DataType20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_DataTypeLibrary19"):
                opp_val = getattr(old_value, "statesml_DataTypeLibrary19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_DataTypeLibrary19"):
                opp_val = getattr(value, "statesml_DataTypeLibrary19", None)
                if opp_val is None:
                    setattr(value, "statesml_DataTypeLibrary19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_DataType(self):
        return self.__statesml_DataType

    @statesml_DataType.setter
    def statesml_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataType__statesml_DataType", None)
        self.__statesml_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Attribute"):
                opp_val = getattr(old_value, "statesml_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Attribute"):
                opp_val = getattr(value, "statesml_Attribute", None)
                setattr(value, "statesml_Attribute", self)

    @property
    def statesml_DataType7(self):
        return self.__statesml_DataType7

    @statesml_DataType7.setter
    def statesml_DataType7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataType__statesml_DataType7", None)
        self.__statesml_DataType7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_Function"):
                    opp_val = getattr(item, "statesml_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_Function"):
                    opp_val = getattr(item, "statesml_Function", None)
                    
                    setattr(item, "statesml_Function", self)
                    

    @property
    def statesml_DataType26(self):
        return self.__statesml_DataType26

    @statesml_DataType26.setter
    def statesml_DataType26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataType__statesml_DataType26", None)
        self.__statesml_DataType26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Parameter"):
                opp_val = getattr(old_value, "statesml_Parameter", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Parameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Parameter"):
                opp_val = getattr(value, "statesml_Parameter", None)
                setattr(value, "statesml_Parameter", self)

class statesml_Attribute:

    def __init__(self, name: str, statesml_Attribute: "statesml_DataType" = None, statesml_Attribute14: "statesml_SystemUnit" = None, statesml_Attribute35: "statesml_StateSystem" = None, statesml_Attribute51: "statesml_IncomingParameter" = None):
        self.name = name
        self.statesml_Attribute = statesml_Attribute
        self.statesml_Attribute14 = statesml_Attribute14
        self.statesml_Attribute35 = statesml_Attribute35
        self.statesml_Attribute51 = statesml_Attribute51
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_Attribute14(self):
        return self.__statesml_Attribute14

    @statesml_Attribute14.setter
    def statesml_Attribute14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Attribute__statesml_Attribute14", None)
        self.__statesml_Attribute14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SystemUnit13"):
                opp_val = getattr(old_value, "statesml_SystemUnit13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnit13"):
                opp_val = getattr(value, "statesml_SystemUnit13", None)
                if opp_val is None:
                    setattr(value, "statesml_SystemUnit13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Attribute51(self):
        return self.__statesml_Attribute51

    @statesml_Attribute51.setter
    def statesml_Attribute51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Attribute__statesml_Attribute51", None)
        self.__statesml_Attribute51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_IncomingParameter50"):
                opp_val = getattr(old_value, "statesml_IncomingParameter50", None)
                if opp_val == self:
                    setattr(old_value, "statesml_IncomingParameter50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_IncomingParameter50"):
                opp_val = getattr(value, "statesml_IncomingParameter50", None)
                setattr(value, "statesml_IncomingParameter50", self)

    @property
    def statesml_Attribute35(self):
        return self.__statesml_Attribute35

    @statesml_Attribute35.setter
    def statesml_Attribute35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Attribute__statesml_Attribute35", None)
        self.__statesml_Attribute35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StateSystem34"):
                opp_val = getattr(old_value, "statesml_StateSystem34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StateSystem34"):
                opp_val = getattr(value, "statesml_StateSystem34", None)
                if opp_val is None:
                    setattr(value, "statesml_StateSystem34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Attribute(self):
        return self.__statesml_Attribute

    @statesml_Attribute.setter
    def statesml_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Attribute__statesml_Attribute", None)
        self.__statesml_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_DataType"):
                opp_val = getattr(old_value, "statesml_DataType", None)
                if opp_val == self:
                    setattr(old_value, "statesml_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_DataType"):
                opp_val = getattr(value, "statesml_DataType", None)
                setattr(value, "statesml_DataType", self)

class statesml_SystemUnitLibrary:

    def __init__(self, name: str, statesml_SystemUnitLibrary: "statesml_SystemUnitModel" = None, statesml_SystemUnitLibrary9: set["statesml_SystemUnit"] = None):
        self.name = name
        self.statesml_SystemUnitLibrary = statesml_SystemUnitLibrary
        self.statesml_SystemUnitLibrary9 = statesml_SystemUnitLibrary9 if statesml_SystemUnitLibrary9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_SystemUnitLibrary9(self):
        return self.__statesml_SystemUnitLibrary9

    @statesml_SystemUnitLibrary9.setter
    def statesml_SystemUnitLibrary9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnitLibrary__statesml_SystemUnitLibrary9", None)
        self.__statesml_SystemUnitLibrary9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_SystemUnit"):
                    opp_val = getattr(item, "statesml_SystemUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_SystemUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_SystemUnit"):
                    opp_val = getattr(item, "statesml_SystemUnit", None)
                    
                    setattr(item, "statesml_SystemUnit", self)
                    

    @property
    def statesml_SystemUnitLibrary(self):
        return self.__statesml_SystemUnitLibrary

    @statesml_SystemUnitLibrary.setter
    def statesml_SystemUnitLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnitLibrary__statesml_SystemUnitLibrary", None)
        self.__statesml_SystemUnitLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SystemUnitModel5"):
                opp_val = getattr(old_value, "statesml_SystemUnitModel5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnitModel5"):
                opp_val = getattr(value, "statesml_SystemUnitModel5", None)
                if opp_val is None:
                    setattr(value, "statesml_SystemUnitModel5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_DataTypeLibrary:

    def __init__(self, name: str, statesml_DataTypeLibrary: "statesml_SystemUnitModel" = None, statesml_DataTypeLibrary19: set["statesml_DataType"] = None):
        self.name = name
        self.statesml_DataTypeLibrary = statesml_DataTypeLibrary
        self.statesml_DataTypeLibrary19 = statesml_DataTypeLibrary19 if statesml_DataTypeLibrary19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_DataTypeLibrary19(self):
        return self.__statesml_DataTypeLibrary19

    @statesml_DataTypeLibrary19.setter
    def statesml_DataTypeLibrary19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataTypeLibrary__statesml_DataTypeLibrary19", None)
        self.__statesml_DataTypeLibrary19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_DataType20"):
                    opp_val = getattr(item, "statesml_DataType20", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_DataType20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_DataType20"):
                    opp_val = getattr(item, "statesml_DataType20", None)
                    
                    setattr(item, "statesml_DataType20", self)
                    

    @property
    def statesml_DataTypeLibrary(self):
        return self.__statesml_DataTypeLibrary

    @statesml_DataTypeLibrary.setter
    def statesml_DataTypeLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataTypeLibrary__statesml_DataTypeLibrary", None)
        self.__statesml_DataTypeLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SystemUnitModel3"):
                opp_val = getattr(old_value, "statesml_SystemUnitModel3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnitModel3"):
                opp_val = getattr(value, "statesml_SystemUnitModel3", None)
                if opp_val is None:
                    setattr(value, "statesml_SystemUnitModel3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_SystemUnitModel:

    def __init__(self, name: str, statesml_SystemUnitModel: "statesml_StatesModel" = None, statesml_SystemUnitModel3: set["statesml_DataTypeLibrary"] = None, statesml_SystemUnitModel5: set["statesml_SystemUnitLibrary"] = None):
        self.name = name
        self.statesml_SystemUnitModel = statesml_SystemUnitModel
        self.statesml_SystemUnitModel3 = statesml_SystemUnitModel3 if statesml_SystemUnitModel3 is not None else set()
        self.statesml_SystemUnitModel5 = statesml_SystemUnitModel5 if statesml_SystemUnitModel5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_SystemUnitModel(self):
        return self.__statesml_SystemUnitModel

    @statesml_SystemUnitModel.setter
    def statesml_SystemUnitModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnitModel__statesml_SystemUnitModel", None)
        self.__statesml_SystemUnitModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StatesModel"):
                opp_val = getattr(old_value, "statesml_StatesModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesModel"):
                opp_val = getattr(value, "statesml_StatesModel", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_SystemUnitModel5(self):
        return self.__statesml_SystemUnitModel5

    @statesml_SystemUnitModel5.setter
    def statesml_SystemUnitModel5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnitModel__statesml_SystemUnitModel5", None)
        self.__statesml_SystemUnitModel5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_SystemUnitLibrary"):
                    opp_val = getattr(item, "statesml_SystemUnitLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_SystemUnitLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_SystemUnitLibrary"):
                    opp_val = getattr(item, "statesml_SystemUnitLibrary", None)
                    
                    setattr(item, "statesml_SystemUnitLibrary", self)
                    

    @property
    def statesml_SystemUnitModel3(self):
        return self.__statesml_SystemUnitModel3

    @statesml_SystemUnitModel3.setter
    def statesml_SystemUnitModel3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnitModel__statesml_SystemUnitModel3", None)
        self.__statesml_SystemUnitModel3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_DataTypeLibrary"):
                    opp_val = getattr(item, "statesml_DataTypeLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_DataTypeLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_DataTypeLibrary"):
                    opp_val = getattr(item, "statesml_DataTypeLibrary", None)
                    
                    setattr(item, "statesml_DataTypeLibrary", self)
                    

class statesml_StatesModel:

    pass