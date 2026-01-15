from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FunctionDomain(Enum):
    time = "time"
    space = "space"
    form = "form"


############################################
# Definition of Classes
############################################

class effbd103_ProcessNode(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class effbd103_Item:

    def __init__(self, name: str, effbd103_Item: "effbd103_Flow" = None):
        self.name = name
        self.effbd103_Item = effbd103_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbd103_Item(self):
        return self.__effbd103_Item

    @effbd103_Item.setter
    def effbd103_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_Item__effbd103_Item", None)
        self.__effbd103_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd103_Flow20"):
                opp_val = getattr(old_value, "effbd103_Flow20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd103_Flow20"):
                opp_val = getattr(value, "effbd103_Flow20", None)
                if opp_val is None:
                    setattr(value, "effbd103_Flow20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd103_Port(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class effbd103_SequenceNode(ABC):

    def __init__(self, tMin: int, tMax: int, name: str, effbd103_SequenceNode: "effbd103_SequenceNode" = None, effbd103_SequenceNode14: set["effbd103_SequenceNode"] = None):
        self.tMin = tMin
        self.tMax = tMax
        self.name = name
        self.effbd103_SequenceNode = effbd103_SequenceNode
        self.effbd103_SequenceNode14 = effbd103_SequenceNode14 if effbd103_SequenceNode14 is not None else set()
        
    @property
    def tMin(self) -> int:
        return self.__tMin

    @tMin.setter
    def tMin(self, tMin: int):
        self.__tMin = tMin

    @property
    def tMax(self) -> int:
        return self.__tMax

    @tMax.setter
    def tMax(self, tMax: int):
        self.__tMax = tMax

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbd103_SequenceNode14(self):
        return self.__effbd103_SequenceNode14

    @effbd103_SequenceNode14.setter
    def effbd103_SequenceNode14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_SequenceNode__effbd103_SequenceNode14", None)
        self.__effbd103_SequenceNode14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd103_SequenceNode"):
                    opp_val = getattr(item, "effbd103_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd103_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd103_SequenceNode"):
                    opp_val = getattr(item, "effbd103_SequenceNode", None)
                    
                    setattr(item, "effbd103_SequenceNode", self)
                    

    @property
    def effbd103_SequenceNode(self):
        return self.__effbd103_SequenceNode

    @effbd103_SequenceNode.setter
    def effbd103_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_SequenceNode__effbd103_SequenceNode", None)
        self.__effbd103_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd103_SequenceNode14"):
                opp_val = getattr(old_value, "effbd103_SequenceNode14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd103_SequenceNode14"):
                opp_val = getattr(value, "effbd103_SequenceNode14", None)
                if opp_val is None:
                    setattr(value, "effbd103_SequenceNode14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd103_Token:

    pass
class effbd103_Description:

    def __init__(self, content: str, effbd103_Description: "effbd103_Function" = None):
        self.content = content
        self.effbd103_Description = effbd103_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def effbd103_Description(self):
        return self.__effbd103_Description

    @effbd103_Description.setter
    def effbd103_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_Description__effbd103_Description", None)
        self.__effbd103_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd103_Function11"):
                opp_val = getattr(old_value, "effbd103_Function11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd103_Function11"):
                opp_val = getattr(value, "effbd103_Function11", None)
                if opp_val is None:
                    setattr(value, "effbd103_Function11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Port:

    pass
class effbd103_InputPort(Port):

    pass
class effbd103_OutputPort(Port):

    pass
class Sequence:

    pass
class effbd103_Start(Sequence):

    pass
class effbd103_Iteration(Sequence):

    pass
class effbd103_Loop(Sequence):

    pass
class effbd103_Final(Sequence):

    pass
class effbd103_LoopExit(Sequence):

    pass
class effbd103_Or(Sequence):

    pass
class effbd103_And(Sequence):

    pass
class ProcessNode:

    pass
class effbd103_Flow(ProcessNode):

    pass
class SequenceNode:

    pass
class effbd103_Sequence(SequenceNode):

    pass
class effbd103_Function(SequenceNode, ProcessNode):

    def __init__(self, domain: str, effbd103_Function: "effbd103_Function" = None, effbd103_Function0: set["effbd103_Function"] = None, effbd103_Function3: set["effbd103_Sequence"] = None, effbd103_Function5: set["effbd103_Flow"] = None, effbd103_Function7: set["effbd103_OutputPort"] = None, effbd103_Function9: set["effbd103_InputPort"] = None, effbd103_Function11: set["effbd103_Description"] = None, effbd103_Function13: set["effbd103_Token"] = None):
        self.domain = domain
        self.effbd103_Function = effbd103_Function
        self.effbd103_Function0 = effbd103_Function0 if effbd103_Function0 is not None else set()
        self.effbd103_Function3 = effbd103_Function3 if effbd103_Function3 is not None else set()
        self.effbd103_Function5 = effbd103_Function5 if effbd103_Function5 is not None else set()
        self.effbd103_Function7 = effbd103_Function7 if effbd103_Function7 is not None else set()
        self.effbd103_Function9 = effbd103_Function9 if effbd103_Function9 is not None else set()
        self.effbd103_Function11 = effbd103_Function11 if effbd103_Function11 is not None else set()
        self.effbd103_Function13 = effbd103_Function13 if effbd103_Function13 is not None else set()
        
    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def effbd103_Function3(self):
        return self.__effbd103_Function3

    @effbd103_Function3.setter
    def effbd103_Function3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_Function__effbd103_Function3", None)
        self.__effbd103_Function3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd103_Sequence"):
                    opp_val = getattr(item, "effbd103_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd103_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd103_Sequence"):
                    opp_val = getattr(item, "effbd103_Sequence", None)
                    
                    setattr(item, "effbd103_Sequence", self)
                    

    @property
    def effbd103_Function5(self):
        return self.__effbd103_Function5

    @effbd103_Function5.setter
    def effbd103_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_Function__effbd103_Function5", None)
        self.__effbd103_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd103_Flow"):
                    opp_val = getattr(item, "effbd103_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd103_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd103_Flow"):
                    opp_val = getattr(item, "effbd103_Flow", None)
                    
                    setattr(item, "effbd103_Flow", self)
                    

    @property
    def effbd103_Function0(self):
        return self.__effbd103_Function0

    @effbd103_Function0.setter
    def effbd103_Function0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_Function__effbd103_Function0", None)
        self.__effbd103_Function0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd103_Function"):
                    opp_val = getattr(item, "effbd103_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd103_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd103_Function"):
                    opp_val = getattr(item, "effbd103_Function", None)
                    
                    setattr(item, "effbd103_Function", self)
                    

    @property
    def effbd103_Function13(self):
        return self.__effbd103_Function13

    @effbd103_Function13.setter
    def effbd103_Function13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_Function__effbd103_Function13", None)
        self.__effbd103_Function13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd103_Token"):
                    opp_val = getattr(item, "effbd103_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd103_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd103_Token"):
                    opp_val = getattr(item, "effbd103_Token", None)
                    
                    setattr(item, "effbd103_Token", self)
                    

    @property
    def effbd103_Function11(self):
        return self.__effbd103_Function11

    @effbd103_Function11.setter
    def effbd103_Function11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_Function__effbd103_Function11", None)
        self.__effbd103_Function11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd103_Description"):
                    opp_val = getattr(item, "effbd103_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd103_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd103_Description"):
                    opp_val = getattr(item, "effbd103_Description", None)
                    
                    setattr(item, "effbd103_Description", self)
                    

    @property
    def effbd103_Function7(self):
        return self.__effbd103_Function7

    @effbd103_Function7.setter
    def effbd103_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_Function__effbd103_Function7", None)
        self.__effbd103_Function7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd103_OutputPort"):
                    opp_val = getattr(item, "effbd103_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd103_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd103_OutputPort"):
                    opp_val = getattr(item, "effbd103_OutputPort", None)
                    
                    setattr(item, "effbd103_OutputPort", self)
                    

    @property
    def effbd103_Function9(self):
        return self.__effbd103_Function9

    @effbd103_Function9.setter
    def effbd103_Function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_Function__effbd103_Function9", None)
        self.__effbd103_Function9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd103_InputPort"):
                    opp_val = getattr(item, "effbd103_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd103_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd103_InputPort"):
                    opp_val = getattr(item, "effbd103_InputPort", None)
                    
                    setattr(item, "effbd103_InputPort", self)
                    

    @property
    def effbd103_Function(self):
        return self.__effbd103_Function

    @effbd103_Function.setter
    def effbd103_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd103_Function__effbd103_Function", None)
        self.__effbd103_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd103_Function0"):
                opp_val = getattr(old_value, "effbd103_Function0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd103_Function0"):
                opp_val = getattr(value, "effbd103_Function0", None)
                if opp_val is None:
                    setattr(value, "effbd103_Function0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
