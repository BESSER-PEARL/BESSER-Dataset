from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class statesml_Trigger:

    def __init__(self, statesml_Trigger: "statesml_ChangeEvent" = None):
        self.statesml_Trigger = statesml_Trigger
        
    @property
    def statesml_Trigger(self):
        return self.__statesml_Trigger

    @statesml_Trigger.setter
    def statesml_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Trigger__statesml_Trigger", None)
        self.__statesml_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_ChangeEvent55"):
                opp_val = getattr(old_value, "statesml_ChangeEvent55", None)
                if opp_val == self:
                    setattr(old_value, "statesml_ChangeEvent55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_ChangeEvent55"):
                opp_val = getattr(value, "statesml_ChangeEvent55", None)
                setattr(value, "statesml_ChangeEvent55", self)

    def fire(self):
        # TODO: Implement fire method
        pass

    def isActivated(self) -> bool:
        # TODO: Implement isActivated method
        pass

class Event:

    pass
class statesml_Edge:

    def __init__(self, name: str, statesml_Edge: "statesml_StatesML" = None, edge: set["statesml_Node"] = None, Edge: "statesml_Node" = None):
        self.name = name
        self.statesml_Edge = statesml_Edge
        self.edge = edge if edge is not None else set()
        self.Edge = Edge
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def edge(self):
        return self.__edge

    @edge.setter
    def edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Edge__edge", None)
        self.__edge = value if value is not None else set()
        
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
    def statesml_Edge(self):
        return self.__statesml_Edge

    @statesml_Edge.setter
    def statesml_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Edge__statesml_Edge", None)
        self.__statesml_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StatesML45"):
                opp_val = getattr(old_value, "statesml_StatesML45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesML45"):
                opp_val = getattr(value, "statesml_StatesML45", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesML45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                if opp_val is None:
                    setattr(value, "node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_Node(ABC):

    def __init__(self, name: str, statesml_Node: "statesml_StatesML" = None, Node: "statesml_Edge" = None, node: set["statesml_Edge"] = None, statesml_Node52: set["statesml_Function"] = None):
        self.name = name
        self.statesml_Node = statesml_Node
        self.Node = Node
        self.node = node if node is not None else set()
        self.statesml_Node52 = statesml_Node52 if statesml_Node52 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_Node52(self):
        return self.__statesml_Node52

    @statesml_Node52.setter
    def statesml_Node52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Node__statesml_Node52", None)
        self.__statesml_Node52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_Function53"):
                    opp_val = getattr(item, "statesml_Function53", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_Function53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_Function53"):
                    opp_val = getattr(item, "statesml_Function53", None)
                    
                    setattr(item, "statesml_Function53", self)
                    

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
            if hasattr(old_value, "edge"):
                opp_val = getattr(old_value, "edge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edge"):
                opp_val = getattr(value, "edge", None)
                if opp_val is None:
                    setattr(value, "edge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Node__node", None)
        self.__node = value if value is not None else set()
        
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
    def statesml_Node(self):
        return self.__statesml_Node

    @statesml_Node.setter
    def statesml_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Node__statesml_Node", None)
        self.__statesml_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StatesML43"):
                opp_val = getattr(old_value, "statesml_StatesML43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesML43"):
                opp_val = getattr(value, "statesml_StatesML43", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesML43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_ChangeEvent(Event):

    def __init__(self, isFulfilled: bool, statesml_ChangeEvent: "statesml_Transition" = None, statesml_ChangeEvent55: "statesml_Trigger" = None):
        self.isFulfilled = isFulfilled
        self.statesml_ChangeEvent = statesml_ChangeEvent
        self.statesml_ChangeEvent55 = statesml_ChangeEvent55
        
    @property
    def isFulfilled(self) -> bool:
        return self.__isFulfilled

    @isFulfilled.setter
    def isFulfilled(self, isFulfilled: bool):
        self.__isFulfilled = isFulfilled

    @property
    def statesml_ChangeEvent(self):
        return self.__statesml_ChangeEvent

    @statesml_ChangeEvent.setter
    def statesml_ChangeEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_ChangeEvent__statesml_ChangeEvent", None)
        self.__statesml_ChangeEvent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Transition"):
                opp_val = getattr(old_value, "statesml_Transition", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Transition"):
                opp_val = getattr(value, "statesml_Transition", None)
                setattr(value, "statesml_Transition", self)

    @property
    def statesml_ChangeEvent55(self):
        return self.__statesml_ChangeEvent55

    @statesml_ChangeEvent55.setter
    def statesml_ChangeEvent55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_ChangeEvent__statesml_ChangeEvent55", None)
        self.__statesml_ChangeEvent55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Trigger"):
                opp_val = getattr(old_value, "statesml_Trigger", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Trigger"):
                opp_val = getattr(value, "statesml_Trigger", None)
                setattr(value, "statesml_Trigger", self)

class statesml_Event(ABC):

    def __init__(self, name: str, statesml_Event: "statesml_StatesML" = None):
        self.name = name
        self.statesml_Event = statesml_Event
        
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
            if hasattr(old_value, "statesml_StatesML"):
                opp_val = getattr(old_value, "statesml_StatesML", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesML"):
                opp_val = getattr(value, "statesml_StatesML", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesML", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_StatesML:

    pass
class Node:

    pass
class statesml_Transition(Node):

    pass
class statesml_SelectionConvergence(Node):

    pass
class statesml_SelectionDivergence(Node):

    pass
class statesml_State(Node):

    def __init__(self, isInitial: bool, isTerminal: bool, state: "statesml_Transition" = None, statesml_State: "statesml_SelectionDivergence" = None, State: "statesml_Transition" = None, statesml_State31: "statesml_SelectionConvergence" = None):
        self.isInitial = isInitial
        self.isTerminal = isTerminal
        self.state = state
        self.statesml_State = statesml_State
        self.State = State
        self.statesml_State31 = statesml_State31
        
    @property
    def isTerminal(self) -> bool:
        return self.__isTerminal

    @isTerminal.setter
    def isTerminal(self, isTerminal: bool):
        self.__isTerminal = isTerminal

    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition"):
                opp_val = getattr(old_value, "transition", None)
                if opp_val == self:
                    setattr(old_value, "transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition"):
                opp_val = getattr(value, "transition", None)
                setattr(value, "transition", self)

    @property
    def statesml_State31(self):
        return self.__statesml_State31

    @statesml_State31.setter
    def statesml_State31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_State__statesml_State31", None)
        self.__statesml_State31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SelectionConvergence30"):
                opp_val = getattr(old_value, "statesml_SelectionConvergence30", None)
                if opp_val == self:
                    setattr(old_value, "statesml_SelectionConvergence30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SelectionConvergence30"):
                opp_val = getattr(value, "statesml_SelectionConvergence30", None)
                setattr(value, "statesml_SelectionConvergence30", self)

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_State__state", None)
        self.__state = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition"):
                opp_val = getattr(old_value, "Transition", None)
                if opp_val == self:
                    setattr(old_value, "Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition"):
                opp_val = getattr(value, "Transition", None)
                setattr(value, "Transition", self)

    @property
    def statesml_State(self):
        return self.__statesml_State

    @statesml_State.setter
    def statesml_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_State__statesml_State", None)
        self.__statesml_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SelectionDivergence"):
                opp_val = getattr(old_value, "statesml_SelectionDivergence", None)
                if opp_val == self:
                    setattr(old_value, "statesml_SelectionDivergence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SelectionDivergence"):
                opp_val = getattr(value, "statesml_SelectionDivergence", None)
                setattr(value, "statesml_SelectionDivergence", self)

class statesml_DataTypeLibrary:

    def __init__(self, name: str, statesml_DataTypeLibrary: set["statesml_DataType"] = None, statesml_DataTypeLibrary38: "statesml_StatesML" = None):
        self.name = name
        self.statesml_DataTypeLibrary = statesml_DataTypeLibrary if statesml_DataTypeLibrary is not None else set()
        self.statesml_DataTypeLibrary38 = statesml_DataTypeLibrary38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_DataTypeLibrary(self):
        return self.__statesml_DataTypeLibrary

    @statesml_DataTypeLibrary.setter
    def statesml_DataTypeLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataTypeLibrary__statesml_DataTypeLibrary", None)
        self.__statesml_DataTypeLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_DataType19"):
                    opp_val = getattr(item, "statesml_DataType19", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_DataType19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_DataType19"):
                    opp_val = getattr(item, "statesml_DataType19", None)
                    
                    setattr(item, "statesml_DataType19", self)
                    

    @property
    def statesml_DataTypeLibrary38(self):
        return self.__statesml_DataTypeLibrary38

    @statesml_DataTypeLibrary38.setter
    def statesml_DataTypeLibrary38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataTypeLibrary__statesml_DataTypeLibrary38", None)
        self.__statesml_DataTypeLibrary38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StatesML37"):
                opp_val = getattr(old_value, "statesml_StatesML37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesML37"):
                opp_val = getattr(value, "statesml_StatesML37", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesML37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_SystemUnitLibrariy:

    def __init__(self, name: str, statesml_SystemUnitLibrariy: set["statesml_SystemUnits"] = None, statesml_SystemUnitLibrariy41: "statesml_StatesML" = None):
        self.name = name
        self.statesml_SystemUnitLibrariy = statesml_SystemUnitLibrariy if statesml_SystemUnitLibrariy is not None else set()
        self.statesml_SystemUnitLibrariy41 = statesml_SystemUnitLibrariy41
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_SystemUnitLibrariy(self):
        return self.__statesml_SystemUnitLibrariy

    @statesml_SystemUnitLibrariy.setter
    def statesml_SystemUnitLibrariy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnitLibrariy__statesml_SystemUnitLibrariy", None)
        self.__statesml_SystemUnitLibrariy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_SystemUnits17"):
                    opp_val = getattr(item, "statesml_SystemUnits17", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_SystemUnits17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_SystemUnits17"):
                    opp_val = getattr(item, "statesml_SystemUnits17", None)
                    
                    setattr(item, "statesml_SystemUnits17", self)
                    

    @property
    def statesml_SystemUnitLibrariy41(self):
        return self.__statesml_SystemUnitLibrariy41

    @statesml_SystemUnitLibrariy41.setter
    def statesml_SystemUnitLibrariy41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnitLibrariy__statesml_SystemUnitLibrariy41", None)
        self.__statesml_SystemUnitLibrariy41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StatesML40"):
                opp_val = getattr(old_value, "statesml_StatesML40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesML40"):
                opp_val = getattr(value, "statesml_StatesML40", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesML40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_DataType:

    def __init__(self, name: str, statesml_DataType: "statesml_Attribute" = None, statesml_DataType12: "statesml_Parameter" = None, statesml_DataType14: set["statesml_Function"] = None, statesml_DataType19: "statesml_DataTypeLibrary" = None):
        self.name = name
        self.statesml_DataType = statesml_DataType
        self.statesml_DataType12 = statesml_DataType12
        self.statesml_DataType14 = statesml_DataType14 if statesml_DataType14 is not None else set()
        self.statesml_DataType19 = statesml_DataType19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_DataType19(self):
        return self.__statesml_DataType19

    @statesml_DataType19.setter
    def statesml_DataType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataType__statesml_DataType19", None)
        self.__statesml_DataType19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_DataTypeLibrary"):
                opp_val = getattr(old_value, "statesml_DataTypeLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_DataTypeLibrary"):
                opp_val = getattr(value, "statesml_DataTypeLibrary", None)
                if opp_val is None:
                    setattr(value, "statesml_DataTypeLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_DataType12(self):
        return self.__statesml_DataType12

    @statesml_DataType12.setter
    def statesml_DataType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataType__statesml_DataType12", None)
        self.__statesml_DataType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Parameter11"):
                opp_val = getattr(old_value, "statesml_Parameter11", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Parameter11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Parameter11"):
                opp_val = getattr(value, "statesml_Parameter11", None)
                setattr(value, "statesml_Parameter11", self)

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
            if hasattr(old_value, "statesml_Attribute9"):
                opp_val = getattr(old_value, "statesml_Attribute9", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Attribute9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Attribute9"):
                opp_val = getattr(value, "statesml_Attribute9", None)
                setattr(value, "statesml_Attribute9", self)

    @property
    def statesml_DataType14(self):
        return self.__statesml_DataType14

    @statesml_DataType14.setter
    def statesml_DataType14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataType__statesml_DataType14", None)
        self.__statesml_DataType14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_Function15"):
                    opp_val = getattr(item, "statesml_Function15", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_Function15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_Function15"):
                    opp_val = getattr(item, "statesml_Function15", None)
                    
                    setattr(item, "statesml_Function15", self)
                    

class statesml_Parameter:

    def __init__(self, name: str, statesml_Parameter: "statesml_Function" = None, statesml_Parameter7: "statesml_Function" = None, statesml_Parameter11: "statesml_DataType" = None):
        self.name = name
        self.statesml_Parameter = statesml_Parameter
        self.statesml_Parameter7 = statesml_Parameter7
        self.statesml_Parameter11 = statesml_Parameter11
        
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
            if hasattr(old_value, "statesml_Function4"):
                opp_val = getattr(old_value, "statesml_Function4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Function4"):
                opp_val = getattr(value, "statesml_Function4", None)
                if opp_val is None:
                    setattr(value, "statesml_Function4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Parameter11(self):
        return self.__statesml_Parameter11

    @statesml_Parameter11.setter
    def statesml_Parameter11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Parameter__statesml_Parameter11", None)
        self.__statesml_Parameter11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_DataType12"):
                opp_val = getattr(old_value, "statesml_DataType12", None)
                if opp_val == self:
                    setattr(old_value, "statesml_DataType12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_DataType12"):
                opp_val = getattr(value, "statesml_DataType12", None)
                setattr(value, "statesml_DataType12", self)

    @property
    def statesml_Parameter7(self):
        return self.__statesml_Parameter7

    @statesml_Parameter7.setter
    def statesml_Parameter7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Parameter__statesml_Parameter7", None)
        self.__statesml_Parameter7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Function6"):
                opp_val = getattr(old_value, "statesml_Function6", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Function6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Function6"):
                opp_val = getattr(value, "statesml_Function6", None)
                setattr(value, "statesml_Function6", self)

class statesml_Attribute:

    def __init__(self, name: str, statesml_Attribute: "statesml_SystemUnits" = None, statesml_Attribute9: "statesml_DataType" = None, statesml_Attribute48: "statesml_StatesML" = None):
        self.name = name
        self.statesml_Attribute = statesml_Attribute
        self.statesml_Attribute9 = statesml_Attribute9
        self.statesml_Attribute48 = statesml_Attribute48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "statesml_SystemUnits2"):
                opp_val = getattr(old_value, "statesml_SystemUnits2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnits2"):
                opp_val = getattr(value, "statesml_SystemUnits2", None)
                if opp_val is None:
                    setattr(value, "statesml_SystemUnits2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Attribute48(self):
        return self.__statesml_Attribute48

    @statesml_Attribute48.setter
    def statesml_Attribute48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Attribute__statesml_Attribute48", None)
        self.__statesml_Attribute48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StatesML47"):
                opp_val = getattr(old_value, "statesml_StatesML47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesML47"):
                opp_val = getattr(value, "statesml_StatesML47", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesML47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Attribute9(self):
        return self.__statesml_Attribute9

    @statesml_Attribute9.setter
    def statesml_Attribute9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Attribute__statesml_Attribute9", None)
        self.__statesml_Attribute9 = value
        
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

class statesml_Function:

    def __init__(self, name: str, statesml_Function: "statesml_SystemUnits" = None, statesml_Function4: set["statesml_Parameter"] = None, statesml_Function6: "statesml_Parameter" = None, statesml_Function15: "statesml_DataType" = None, statesml_Function53: "statesml_Node" = None):
        self.name = name
        self.statesml_Function = statesml_Function
        self.statesml_Function4 = statesml_Function4 if statesml_Function4 is not None else set()
        self.statesml_Function6 = statesml_Function6
        self.statesml_Function15 = statesml_Function15
        self.statesml_Function53 = statesml_Function53
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_Function53(self):
        return self.__statesml_Function53

    @statesml_Function53.setter
    def statesml_Function53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function53", None)
        self.__statesml_Function53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Node52"):
                opp_val = getattr(old_value, "statesml_Node52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Node52"):
                opp_val = getattr(value, "statesml_Node52", None)
                if opp_val is None:
                    setattr(value, "statesml_Node52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Function15(self):
        return self.__statesml_Function15

    @statesml_Function15.setter
    def statesml_Function15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function15", None)
        self.__statesml_Function15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_DataType14"):
                opp_val = getattr(old_value, "statesml_DataType14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_DataType14"):
                opp_val = getattr(value, "statesml_DataType14", None)
                if opp_val is None:
                    setattr(value, "statesml_DataType14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Function6(self):
        return self.__statesml_Function6

    @statesml_Function6.setter
    def statesml_Function6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function6", None)
        self.__statesml_Function6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Parameter7"):
                opp_val = getattr(old_value, "statesml_Parameter7", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Parameter7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Parameter7"):
                opp_val = getattr(value, "statesml_Parameter7", None)
                setattr(value, "statesml_Parameter7", self)

    @property
    def statesml_Function4(self):
        return self.__statesml_Function4

    @statesml_Function4.setter
    def statesml_Function4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function4", None)
        self.__statesml_Function4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_Parameter"):
                    opp_val = getattr(item, "statesml_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_Parameter"):
                    opp_val = getattr(item, "statesml_Parameter", None)
                    
                    setattr(item, "statesml_Parameter", self)
                    

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
            if hasattr(old_value, "statesml_SystemUnits"):
                opp_val = getattr(old_value, "statesml_SystemUnits", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnits"):
                opp_val = getattr(value, "statesml_SystemUnits", None)
                if opp_val is None:
                    setattr(value, "statesml_SystemUnits", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_SystemUnits:

    def __init__(self, name: str, statesml_SystemUnits: set["statesml_Function"] = None, statesml_SystemUnits2: set["statesml_Attribute"] = None, statesml_SystemUnits17: "statesml_SystemUnitLibrariy" = None, statesml_SystemUnits35: "statesml_StatesML" = None):
        self.name = name
        self.statesml_SystemUnits = statesml_SystemUnits if statesml_SystemUnits is not None else set()
        self.statesml_SystemUnits2 = statesml_SystemUnits2 if statesml_SystemUnits2 is not None else set()
        self.statesml_SystemUnits17 = statesml_SystemUnits17
        self.statesml_SystemUnits35 = statesml_SystemUnits35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_SystemUnits35(self):
        return self.__statesml_SystemUnits35

    @statesml_SystemUnits35.setter
    def statesml_SystemUnits35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnits__statesml_SystemUnits35", None)
        self.__statesml_SystemUnits35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_StatesML34"):
                opp_val = getattr(old_value, "statesml_StatesML34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesML34"):
                opp_val = getattr(value, "statesml_StatesML34", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesML34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_SystemUnits(self):
        return self.__statesml_SystemUnits

    @statesml_SystemUnits.setter
    def statesml_SystemUnits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnits__statesml_SystemUnits", None)
        self.__statesml_SystemUnits = value if value is not None else set()
        
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
    def statesml_SystemUnits17(self):
        return self.__statesml_SystemUnits17

    @statesml_SystemUnits17.setter
    def statesml_SystemUnits17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnits__statesml_SystemUnits17", None)
        self.__statesml_SystemUnits17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SystemUnitLibrariy"):
                opp_val = getattr(old_value, "statesml_SystemUnitLibrariy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnitLibrariy"):
                opp_val = getattr(value, "statesml_SystemUnitLibrariy", None)
                if opp_val is None:
                    setattr(value, "statesml_SystemUnitLibrariy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_SystemUnits2(self):
        return self.__statesml_SystemUnits2

    @statesml_SystemUnits2.setter
    def statesml_SystemUnits2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnits__statesml_SystemUnits2", None)
        self.__statesml_SystemUnits2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_Attribute"):
                    opp_val = getattr(item, "statesml_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_Attribute"):
                    opp_val = getattr(item, "statesml_Attribute", None)
                    
                    setattr(item, "statesml_Attribute", self)
                    
