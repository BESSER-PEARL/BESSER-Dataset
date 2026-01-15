from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class NewEnum1(Enum):
    LITERAL0 = "LITERAL0"
    LITERAL1 = "LITERAL1"
    LITERAL2 = "LITERAL2"


############################################
# Definition of Classes
############################################

class statesml_DataTypeLibrary(ABC):

    def __init__(self, name: str, statesml_DataTypeLibrary: set["statesml_DataType"] = None):
        self.name = name
        self.statesml_DataTypeLibrary = statesml_DataTypeLibrary if statesml_DataTypeLibrary is not None else set()
        
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
                if hasattr(item, "statesml_DataType41"):
                    opp_val = getattr(item, "statesml_DataType41", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_DataType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_DataType41"):
                    opp_val = getattr(item, "statesml_DataType41", None)
                    
                    setattr(item, "statesml_DataType41", self)
                    

class statesml_SystemUnitLibrary(ABC):

    def __init__(self, name: str, statesml_SystemUnitLibrary: set["statesml_SystemUnit"] = None):
        self.name = name
        self.statesml_SystemUnitLibrary = statesml_SystemUnitLibrary if statesml_SystemUnitLibrary is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_SystemUnitLibrary(self):
        return self.__statesml_SystemUnitLibrary

    @statesml_SystemUnitLibrary.setter
    def statesml_SystemUnitLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnitLibrary__statesml_SystemUnitLibrary", None)
        self.__statesml_SystemUnitLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_SystemUnit39"):
                    opp_val = getattr(item, "statesml_SystemUnit39", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_SystemUnit39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_SystemUnit39"):
                    opp_val = getattr(item, "statesml_SystemUnit39", None)
                    
                    setattr(item, "statesml_SystemUnit39", self)
                    

class statesml_KeyValuePair(ABC):

    def __init__(self, name: str, statesml_KeyValuePair: "statesml_DataType" = None):
        self.name = name
        self.statesml_KeyValuePair = statesml_KeyValuePair
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_KeyValuePair(self):
        return self.__statesml_KeyValuePair

    @statesml_KeyValuePair.setter
    def statesml_KeyValuePair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_KeyValuePair__statesml_KeyValuePair", None)
        self.__statesml_KeyValuePair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_DataType37"):
                opp_val = getattr(old_value, "statesml_DataType37", None)
                if opp_val == self:
                    setattr(old_value, "statesml_DataType37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_DataType37"):
                opp_val = getattr(value, "statesml_DataType37", None)
                setattr(value, "statesml_DataType37", self)

class statesml_DataType(ABC):

    def __init__(self, name: str, statesml_DataType: set["statesml_Function"] = None, statesml_DataType37: "statesml_KeyValuePair" = None, statesml_DataType41: "statesml_DataTypeLibrary" = None):
        self.name = name
        self.statesml_DataType = statesml_DataType if statesml_DataType is not None else set()
        self.statesml_DataType37 = statesml_DataType37
        self.statesml_DataType41 = statesml_DataType41
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_DataType(self):
        return self.__statesml_DataType

    @statesml_DataType.setter
    def statesml_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataType__statesml_DataType", None)
        self.__statesml_DataType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_Function35"):
                    opp_val = getattr(item, "statesml_Function35", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_Function35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_Function35"):
                    opp_val = getattr(item, "statesml_Function35", None)
                    
                    setattr(item, "statesml_Function35", self)
                    

    @property
    def statesml_DataType37(self):
        return self.__statesml_DataType37

    @statesml_DataType37.setter
    def statesml_DataType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataType__statesml_DataType37", None)
        self.__statesml_DataType37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_KeyValuePair"):
                opp_val = getattr(old_value, "statesml_KeyValuePair", None)
                if opp_val == self:
                    setattr(old_value, "statesml_KeyValuePair", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_KeyValuePair"):
                opp_val = getattr(value, "statesml_KeyValuePair", None)
                setattr(value, "statesml_KeyValuePair", self)

    @property
    def statesml_DataType41(self):
        return self.__statesml_DataType41

    @statesml_DataType41.setter
    def statesml_DataType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_DataType__statesml_DataType41", None)
        self.__statesml_DataType41 = value
        
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

class statesml_Function:

    def __init__(self, name: str, statesml_Function28: "statesml_SystemUnit" = None, statesml_Function30: set["statesml_Parameter"] = None, statesml_Function: "statesml_RegularState" = None, statesml_Function35: "statesml_DataType" = None, statesml_Function32: "statesml_Parameter" = None):
        self.name = name
        self.statesml_Function28 = statesml_Function28
        self.statesml_Function30 = statesml_Function30 if statesml_Function30 is not None else set()
        self.statesml_Function = statesml_Function
        self.statesml_Function35 = statesml_Function35
        self.statesml_Function32 = statesml_Function32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "statesml_RegularState"):
                opp_val = getattr(old_value, "statesml_RegularState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_RegularState"):
                opp_val = getattr(value, "statesml_RegularState", None)
                if opp_val is None:
                    setattr(value, "statesml_RegularState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Function32(self):
        return self.__statesml_Function32

    @statesml_Function32.setter
    def statesml_Function32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function32", None)
        self.__statesml_Function32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Parameter33"):
                opp_val = getattr(old_value, "statesml_Parameter33", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Parameter33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Parameter33"):
                opp_val = getattr(value, "statesml_Parameter33", None)
                setattr(value, "statesml_Parameter33", self)

    @property
    def statesml_Function30(self):
        return self.__statesml_Function30

    @statesml_Function30.setter
    def statesml_Function30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function30", None)
        self.__statesml_Function30 = value if value is not None else set()
        
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
    def statesml_Function35(self):
        return self.__statesml_Function35

    @statesml_Function35.setter
    def statesml_Function35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function35", None)
        self.__statesml_Function35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_DataType"):
                opp_val = getattr(old_value, "statesml_DataType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_DataType"):
                opp_val = getattr(value, "statesml_DataType", None)
                if opp_val is None:
                    setattr(value, "statesml_DataType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Function28(self):
        return self.__statesml_Function28

    @statesml_Function28.setter
    def statesml_Function28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Function__statesml_Function28", None)
        self.__statesml_Function28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SystemUnit27"):
                opp_val = getattr(old_value, "statesml_SystemUnit27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnit27"):
                opp_val = getattr(value, "statesml_SystemUnit27", None)
                if opp_val is None:
                    setattr(value, "statesml_SystemUnit27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class KeyValuePair:

    pass
class statesml_Parameter(KeyValuePair):

    pass
class Event:

    pass
class statesml_ChangeEvent(Event):

    pass
class statesml_NewEClass22:

    pass
class statesml_NewEClass21:

    pass
class statesml_Constant:

    pass
class statesml_Event(ABC):

    def __init__(self, name: str, statesml_Event: "statesml_Trigger" = None):
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
            if hasattr(old_value, "statesml_Trigger11"):
                opp_val = getattr(old_value, "statesml_Trigger11", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Trigger11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Trigger11"):
                opp_val = getattr(value, "statesml_Trigger11", None)
                setattr(value, "statesml_Trigger11", self)

    def eventOccured(self):
        # TODO: Implement eventOccured method
        pass

class State:

    pass
class statesml_RegularState(State):

    pass
class statesml_TerminalState(State):

    pass
class statesml_InitialState(State):

    pass
class statesml_Edge:

    def __init__(self, name: str, statesml_Edge: "statesml_StatesMLModel" = None, statesml_Edge17: "statesml_Node" = None, statesml_Edge20: "statesml_Node" = None):
        self.name = name
        self.statesml_Edge = statesml_Edge
        self.statesml_Edge17 = statesml_Edge17
        self.statesml_Edge20 = statesml_Edge20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_Edge17(self):
        return self.__statesml_Edge17

    @statesml_Edge17.setter
    def statesml_Edge17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Edge__statesml_Edge17", None)
        self.__statesml_Edge17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Node18"):
                opp_val = getattr(old_value, "statesml_Node18", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Node18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Node18"):
                opp_val = getattr(value, "statesml_Node18", None)
                setattr(value, "statesml_Node18", self)

    @property
    def statesml_Edge20(self):
        return self.__statesml_Edge20

    @statesml_Edge20.setter
    def statesml_Edge20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Edge__statesml_Edge20", None)
        self.__statesml_Edge20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Node21"):
                opp_val = getattr(old_value, "statesml_Node21", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Node21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Node21"):
                opp_val = getattr(value, "statesml_Node21", None)
                setattr(value, "statesml_Node21", self)

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
            if hasattr(old_value, "statesml_StatesMLModel4"):
                opp_val = getattr(old_value, "statesml_StatesMLModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesMLModel4"):
                opp_val = getattr(value, "statesml_StatesMLModel4", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesMLModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_SystemUnit(ABC):

    def __init__(self, name: str, statesml_SystemUnit: "statesml_StatesMLModel" = None, statesml_SystemUnit24: set["statesml_Attribute"] = None, statesml_SystemUnit27: set["statesml_Function"] = None, statesml_SystemUnit39: "statesml_SystemUnitLibrary" = None):
        self.name = name
        self.statesml_SystemUnit = statesml_SystemUnit
        self.statesml_SystemUnit24 = statesml_SystemUnit24 if statesml_SystemUnit24 is not None else set()
        self.statesml_SystemUnit27 = statesml_SystemUnit27 if statesml_SystemUnit27 is not None else set()
        self.statesml_SystemUnit39 = statesml_SystemUnit39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_SystemUnit27(self):
        return self.__statesml_SystemUnit27

    @statesml_SystemUnit27.setter
    def statesml_SystemUnit27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnit__statesml_SystemUnit27", None)
        self.__statesml_SystemUnit27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_Function28"):
                    opp_val = getattr(item, "statesml_Function28", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_Function28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_Function28"):
                    opp_val = getattr(item, "statesml_Function28", None)
                    
                    setattr(item, "statesml_Function28", self)
                    

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
            if hasattr(old_value, "statesml_StatesMLModel2"):
                opp_val = getattr(old_value, "statesml_StatesMLModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesMLModel2"):
                opp_val = getattr(value, "statesml_StatesMLModel2", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesMLModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_SystemUnit24(self):
        return self.__statesml_SystemUnit24

    @statesml_SystemUnit24.setter
    def statesml_SystemUnit24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnit__statesml_SystemUnit24", None)
        self.__statesml_SystemUnit24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statesml_Attribute25"):
                    opp_val = getattr(item, "statesml_Attribute25", None)
                    
                    if opp_val == self:
                        setattr(item, "statesml_Attribute25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statesml_Attribute25"):
                    opp_val = getattr(item, "statesml_Attribute25", None)
                    
                    setattr(item, "statesml_Attribute25", self)
                    

    @property
    def statesml_SystemUnit39(self):
        return self.__statesml_SystemUnit39

    @statesml_SystemUnit39.setter
    def statesml_SystemUnit39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_SystemUnit__statesml_SystemUnit39", None)
        self.__statesml_SystemUnit39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_SystemUnitLibrary"):
                opp_val = getattr(old_value, "statesml_SystemUnitLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_SystemUnitLibrary"):
                opp_val = getattr(value, "statesml_SystemUnitLibrary", None)
                if opp_val is None:
                    setattr(value, "statesml_SystemUnitLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_Attributes:

    pass
class statesml_Trigger:

    def __init__(self, statesml_Trigger: "statesml_Transition" = None, statesml_Trigger11: "statesml_Event" = None):
        self.statesml_Trigger = statesml_Trigger
        self.statesml_Trigger11 = statesml_Trigger11
        
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
            if hasattr(old_value, "statesml_Transition"):
                opp_val = getattr(old_value, "statesml_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Transition"):
                opp_val = getattr(value, "statesml_Transition", None)
                if opp_val is None:
                    setattr(value, "statesml_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statesml_Trigger11(self):
        return self.__statesml_Trigger11

    @statesml_Trigger11.setter
    def statesml_Trigger11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Trigger__statesml_Trigger11", None)
        self.__statesml_Trigger11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Event"):
                opp_val = getattr(old_value, "statesml_Event", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Event"):
                opp_val = getattr(value, "statesml_Event", None)
                setattr(value, "statesml_Event", self)

    def fire(self, event: str):
        # TODO: Implement fire method
        pass

class Node:

    pass
class statesml_SelectionConvergence(Node):

    pass
class statesml_State(Node):

    pass
class statesml_SelectionDivergence(Node):

    pass
class statesml_Transition(Node):

    pass
class statesml_NewEClass4:

    pass
class statesml_NewEClass3:

    pass
class statesml_Events:

    pass
class statesml_Attribute(KeyValuePair):

    pass
class statesml_Node(ABC):

    def __init__(self, name: str, statesml_Node: "statesml_StatesMLModel" = None, Node: "statesml_Transition" = None, node: set["statesml_Transition"] = None, statesml_Node18: "statesml_Edge" = None, statesml_Node21: "statesml_Edge" = None):
        self.name = name
        self.statesml_Node = statesml_Node
        self.Node = Node
        self.node = node if node is not None else set()
        self.statesml_Node18 = statesml_Node18
        self.statesml_Node21 = statesml_Node21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statesml_Node18(self):
        return self.__statesml_Node18

    @statesml_Node18.setter
    def statesml_Node18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Node__statesml_Node18", None)
        self.__statesml_Node18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Edge17"):
                opp_val = getattr(old_value, "statesml_Edge17", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Edge17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Edge17"):
                opp_val = getattr(value, "statesml_Edge17", None)
                setattr(value, "statesml_Edge17", self)

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
            if hasattr(old_value, "transition"):
                opp_val = getattr(old_value, "transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition"):
                opp_val = getattr(value, "transition", None)
                if opp_val is None:
                    setattr(value, "transition", set([self]))
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
    def statesml_Node21(self):
        return self.__statesml_Node21

    @statesml_Node21.setter
    def statesml_Node21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statesml_Node__statesml_Node21", None)
        self.__statesml_Node21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statesml_Edge20"):
                opp_val = getattr(old_value, "statesml_Edge20", None)
                if opp_val == self:
                    setattr(old_value, "statesml_Edge20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_Edge20"):
                opp_val = getattr(value, "statesml_Edge20", None)
                setattr(value, "statesml_Edge20", self)

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
            if hasattr(old_value, "statesml_StatesMLModel"):
                opp_val = getattr(old_value, "statesml_StatesMLModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statesml_StatesMLModel"):
                opp_val = getattr(value, "statesml_StatesMLModel", None)
                if opp_val is None:
                    setattr(value, "statesml_StatesMLModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statesml_StatesMLModel:

    pass