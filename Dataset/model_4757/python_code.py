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

class effbd106_ProcessNode(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class effbd106_Item:

    def __init__(self, name: str, effbd106_Item: "effbd106_Flow" = None):
        self.name = name
        self.effbd106_Item = effbd106_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbd106_Item(self):
        return self.__effbd106_Item

    @effbd106_Item.setter
    def effbd106_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_Item__effbd106_Item", None)
        self.__effbd106_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd106_Flow20"):
                opp_val = getattr(old_value, "effbd106_Flow20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd106_Flow20"):
                opp_val = getattr(value, "effbd106_Flow20", None)
                if opp_val is None:
                    setattr(value, "effbd106_Flow20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Sequence:

    pass
class effbd106_LoopExit(Sequence):

    pass
class effbd106_Iteration(Sequence):

    pass
class effbd106_And(Sequence):

    pass
class effbd106_SequenceNode(ABC):

    def __init__(self, name: str, tMin: int, tMax: int, effbd106_SequenceNode: "effbd106_SequenceNode" = None, effbd106_SequenceNode14: set["effbd106_SequenceNode"] = None):
        self.name = name
        self.tMin = tMin
        self.tMax = tMax
        self.effbd106_SequenceNode = effbd106_SequenceNode
        self.effbd106_SequenceNode14 = effbd106_SequenceNode14 if effbd106_SequenceNode14 is not None else set()
        
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
    def tMin(self) -> int:
        return self.__tMin

    @tMin.setter
    def tMin(self, tMin: int):
        self.__tMin = tMin

    @property
    def effbd106_SequenceNode14(self):
        return self.__effbd106_SequenceNode14

    @effbd106_SequenceNode14.setter
    def effbd106_SequenceNode14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_SequenceNode__effbd106_SequenceNode14", None)
        self.__effbd106_SequenceNode14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd106_SequenceNode"):
                    opp_val = getattr(item, "effbd106_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd106_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd106_SequenceNode"):
                    opp_val = getattr(item, "effbd106_SequenceNode", None)
                    
                    setattr(item, "effbd106_SequenceNode", self)
                    

    @property
    def effbd106_SequenceNode(self):
        return self.__effbd106_SequenceNode

    @effbd106_SequenceNode.setter
    def effbd106_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_SequenceNode__effbd106_SequenceNode", None)
        self.__effbd106_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd106_SequenceNode14"):
                opp_val = getattr(old_value, "effbd106_SequenceNode14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd106_SequenceNode14"):
                opp_val = getattr(value, "effbd106_SequenceNode14", None)
                if opp_val is None:
                    setattr(value, "effbd106_SequenceNode14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd106_Token:

    pass
class effbd106_Description:

    def __init__(self, content: str, effbd106_Description: "effbd106_Function" = None):
        self.content = content
        self.effbd106_Description = effbd106_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def effbd106_Description(self):
        return self.__effbd106_Description

    @effbd106_Description.setter
    def effbd106_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_Description__effbd106_Description", None)
        self.__effbd106_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd106_Function11"):
                opp_val = getattr(old_value, "effbd106_Function11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd106_Function11"):
                opp_val = getattr(value, "effbd106_Function11", None)
                if opp_val is None:
                    setattr(value, "effbd106_Function11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd106_Port(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class Port:

    pass
class effbd106_InputPort(Port):

    pass
class effbd106_OutputPort(Port):

    pass
class effbd106_Loop(Sequence):

    pass
class effbd106_Final(Sequence):

    pass
class effbd106_Start(Sequence):

    pass
class effbd106_Or(Sequence):

    pass
class ProcessNode:

    pass
class SequenceNode:

    pass
class effbd106_Function(SequenceNode, ProcessNode):

    def __init__(self, domain: str, effbd106_Function: "effbd106_Function" = None, effbd106_Function0: set["effbd106_Function"] = None, effbd106_Function3: set["effbd106_Sequence"] = None, effbd106_Function5: set["effbd106_Flow"] = None, effbd106_Function7: set["effbd106_OutputPort"] = None, effbd106_Function9: set["effbd106_InputPort"] = None, effbd106_Function11: set["effbd106_Description"] = None, effbd106_Function13: set["effbd106_Token"] = None):
        self.domain = domain
        self.effbd106_Function = effbd106_Function
        self.effbd106_Function0 = effbd106_Function0 if effbd106_Function0 is not None else set()
        self.effbd106_Function3 = effbd106_Function3 if effbd106_Function3 is not None else set()
        self.effbd106_Function5 = effbd106_Function5 if effbd106_Function5 is not None else set()
        self.effbd106_Function7 = effbd106_Function7 if effbd106_Function7 is not None else set()
        self.effbd106_Function9 = effbd106_Function9 if effbd106_Function9 is not None else set()
        self.effbd106_Function11 = effbd106_Function11 if effbd106_Function11 is not None else set()
        self.effbd106_Function13 = effbd106_Function13 if effbd106_Function13 is not None else set()
        
    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def effbd106_Function9(self):
        return self.__effbd106_Function9

    @effbd106_Function9.setter
    def effbd106_Function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_Function__effbd106_Function9", None)
        self.__effbd106_Function9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd106_InputPort"):
                    opp_val = getattr(item, "effbd106_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd106_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd106_InputPort"):
                    opp_val = getattr(item, "effbd106_InputPort", None)
                    
                    setattr(item, "effbd106_InputPort", self)
                    

    @property
    def effbd106_Function13(self):
        return self.__effbd106_Function13

    @effbd106_Function13.setter
    def effbd106_Function13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_Function__effbd106_Function13", None)
        self.__effbd106_Function13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd106_Token"):
                    opp_val = getattr(item, "effbd106_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd106_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd106_Token"):
                    opp_val = getattr(item, "effbd106_Token", None)
                    
                    setattr(item, "effbd106_Token", self)
                    

    @property
    def effbd106_Function7(self):
        return self.__effbd106_Function7

    @effbd106_Function7.setter
    def effbd106_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_Function__effbd106_Function7", None)
        self.__effbd106_Function7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd106_OutputPort"):
                    opp_val = getattr(item, "effbd106_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd106_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd106_OutputPort"):
                    opp_val = getattr(item, "effbd106_OutputPort", None)
                    
                    setattr(item, "effbd106_OutputPort", self)
                    

    @property
    def effbd106_Function0(self):
        return self.__effbd106_Function0

    @effbd106_Function0.setter
    def effbd106_Function0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_Function__effbd106_Function0", None)
        self.__effbd106_Function0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd106_Function"):
                    opp_val = getattr(item, "effbd106_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd106_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd106_Function"):
                    opp_val = getattr(item, "effbd106_Function", None)
                    
                    setattr(item, "effbd106_Function", self)
                    

    @property
    def effbd106_Function11(self):
        return self.__effbd106_Function11

    @effbd106_Function11.setter
    def effbd106_Function11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_Function__effbd106_Function11", None)
        self.__effbd106_Function11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd106_Description"):
                    opp_val = getattr(item, "effbd106_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd106_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd106_Description"):
                    opp_val = getattr(item, "effbd106_Description", None)
                    
                    setattr(item, "effbd106_Description", self)
                    

    @property
    def effbd106_Function(self):
        return self.__effbd106_Function

    @effbd106_Function.setter
    def effbd106_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_Function__effbd106_Function", None)
        self.__effbd106_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd106_Function0"):
                opp_val = getattr(old_value, "effbd106_Function0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd106_Function0"):
                opp_val = getattr(value, "effbd106_Function0", None)
                if opp_val is None:
                    setattr(value, "effbd106_Function0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbd106_Function3(self):
        return self.__effbd106_Function3

    @effbd106_Function3.setter
    def effbd106_Function3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_Function__effbd106_Function3", None)
        self.__effbd106_Function3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd106_Sequence"):
                    opp_val = getattr(item, "effbd106_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd106_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd106_Sequence"):
                    opp_val = getattr(item, "effbd106_Sequence", None)
                    
                    setattr(item, "effbd106_Sequence", self)
                    

    @property
    def effbd106_Function5(self):
        return self.__effbd106_Function5

    @effbd106_Function5.setter
    def effbd106_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd106_Function__effbd106_Function5", None)
        self.__effbd106_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd106_Flow"):
                    opp_val = getattr(item, "effbd106_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd106_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd106_Flow"):
                    opp_val = getattr(item, "effbd106_Flow", None)
                    
                    setattr(item, "effbd106_Flow", self)
                    

class effbd106_Flow(ProcessNode):

    pass
class effbd106_Sequence(SequenceNode):

    pass