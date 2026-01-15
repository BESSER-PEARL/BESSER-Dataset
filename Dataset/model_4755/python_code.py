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

class effbd104_ProcessNode(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class effbd104_Item:

    def __init__(self, name: str, effbd104_Item: "effbd104_Flow" = None):
        self.name = name
        self.effbd104_Item = effbd104_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbd104_Item(self):
        return self.__effbd104_Item

    @effbd104_Item.setter
    def effbd104_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_Item__effbd104_Item", None)
        self.__effbd104_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd104_Flow20"):
                opp_val = getattr(old_value, "effbd104_Flow20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd104_Flow20"):
                opp_val = getattr(value, "effbd104_Flow20", None)
                if opp_val is None:
                    setattr(value, "effbd104_Flow20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd104_Port(ABC):

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
class effbd104_SequenceNode(ABC):

    def __init__(self, name: str, tMin: int, tMax: int, effbd104_SequenceNode: "effbd104_SequenceNode" = None, effbd104_SequenceNode14: set["effbd104_SequenceNode"] = None):
        self.name = name
        self.tMin = tMin
        self.tMax = tMax
        self.effbd104_SequenceNode = effbd104_SequenceNode
        self.effbd104_SequenceNode14 = effbd104_SequenceNode14 if effbd104_SequenceNode14 is not None else set()
        
    @property
    def tMin(self) -> int:
        return self.__tMin

    @tMin.setter
    def tMin(self, tMin: int):
        self.__tMin = tMin

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tMax(self) -> int:
        return self.__tMax

    @tMax.setter
    def tMax(self, tMax: int):
        self.__tMax = tMax

    @property
    def effbd104_SequenceNode(self):
        return self.__effbd104_SequenceNode

    @effbd104_SequenceNode.setter
    def effbd104_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_SequenceNode__effbd104_SequenceNode", None)
        self.__effbd104_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd104_SequenceNode14"):
                opp_val = getattr(old_value, "effbd104_SequenceNode14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd104_SequenceNode14"):
                opp_val = getattr(value, "effbd104_SequenceNode14", None)
                if opp_val is None:
                    setattr(value, "effbd104_SequenceNode14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbd104_SequenceNode14(self):
        return self.__effbd104_SequenceNode14

    @effbd104_SequenceNode14.setter
    def effbd104_SequenceNode14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_SequenceNode__effbd104_SequenceNode14", None)
        self.__effbd104_SequenceNode14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd104_SequenceNode"):
                    opp_val = getattr(item, "effbd104_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd104_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd104_SequenceNode"):
                    opp_val = getattr(item, "effbd104_SequenceNode", None)
                    
                    setattr(item, "effbd104_SequenceNode", self)
                    

class effbd104_Token:

    pass
class effbd104_Description:

    def __init__(self, content: str, effbd104_Description: "effbd104_Function" = None):
        self.content = content
        self.effbd104_Description = effbd104_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def effbd104_Description(self):
        return self.__effbd104_Description

    @effbd104_Description.setter
    def effbd104_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_Description__effbd104_Description", None)
        self.__effbd104_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd104_Function11"):
                opp_val = getattr(old_value, "effbd104_Function11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd104_Function11"):
                opp_val = getattr(value, "effbd104_Function11", None)
                if opp_val is None:
                    setattr(value, "effbd104_Function11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd104_InputPort(Port):

    pass
class effbd104_OutputPort(Port):

    pass
class ProcessNode:

    pass
class effbd104_Flow(ProcessNode):

    pass
class SequenceNode:

    pass
class effbd104_Sequence(SequenceNode):

    pass
class effbd104_Function(SequenceNode, ProcessNode):

    def __init__(self, domain: str, effbd104_Function: "effbd104_Function" = None, effbd104_Function0: set["effbd104_Function"] = None, effbd104_Function3: set["effbd104_Sequence"] = None, effbd104_Function5: set["effbd104_Flow"] = None, effbd104_Function7: set["effbd104_OutputPort"] = None, effbd104_Function9: set["effbd104_InputPort"] = None, effbd104_Function11: set["effbd104_Description"] = None, effbd104_Function13: set["effbd104_Token"] = None):
        self.domain = domain
        self.effbd104_Function = effbd104_Function
        self.effbd104_Function0 = effbd104_Function0 if effbd104_Function0 is not None else set()
        self.effbd104_Function3 = effbd104_Function3 if effbd104_Function3 is not None else set()
        self.effbd104_Function5 = effbd104_Function5 if effbd104_Function5 is not None else set()
        self.effbd104_Function7 = effbd104_Function7 if effbd104_Function7 is not None else set()
        self.effbd104_Function9 = effbd104_Function9 if effbd104_Function9 is not None else set()
        self.effbd104_Function11 = effbd104_Function11 if effbd104_Function11 is not None else set()
        self.effbd104_Function13 = effbd104_Function13 if effbd104_Function13 is not None else set()
        
    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def effbd104_Function7(self):
        return self.__effbd104_Function7

    @effbd104_Function7.setter
    def effbd104_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_Function__effbd104_Function7", None)
        self.__effbd104_Function7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd104_OutputPort"):
                    opp_val = getattr(item, "effbd104_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd104_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd104_OutputPort"):
                    opp_val = getattr(item, "effbd104_OutputPort", None)
                    
                    setattr(item, "effbd104_OutputPort", self)
                    

    @property
    def effbd104_Function(self):
        return self.__effbd104_Function

    @effbd104_Function.setter
    def effbd104_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_Function__effbd104_Function", None)
        self.__effbd104_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd104_Function0"):
                opp_val = getattr(old_value, "effbd104_Function0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd104_Function0"):
                opp_val = getattr(value, "effbd104_Function0", None)
                if opp_val is None:
                    setattr(value, "effbd104_Function0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbd104_Function0(self):
        return self.__effbd104_Function0

    @effbd104_Function0.setter
    def effbd104_Function0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_Function__effbd104_Function0", None)
        self.__effbd104_Function0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd104_Function"):
                    opp_val = getattr(item, "effbd104_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd104_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd104_Function"):
                    opp_val = getattr(item, "effbd104_Function", None)
                    
                    setattr(item, "effbd104_Function", self)
                    

    @property
    def effbd104_Function3(self):
        return self.__effbd104_Function3

    @effbd104_Function3.setter
    def effbd104_Function3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_Function__effbd104_Function3", None)
        self.__effbd104_Function3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd104_Sequence"):
                    opp_val = getattr(item, "effbd104_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd104_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd104_Sequence"):
                    opp_val = getattr(item, "effbd104_Sequence", None)
                    
                    setattr(item, "effbd104_Sequence", self)
                    

    @property
    def effbd104_Function13(self):
        return self.__effbd104_Function13

    @effbd104_Function13.setter
    def effbd104_Function13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_Function__effbd104_Function13", None)
        self.__effbd104_Function13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd104_Token"):
                    opp_val = getattr(item, "effbd104_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd104_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd104_Token"):
                    opp_val = getattr(item, "effbd104_Token", None)
                    
                    setattr(item, "effbd104_Token", self)
                    

    @property
    def effbd104_Function9(self):
        return self.__effbd104_Function9

    @effbd104_Function9.setter
    def effbd104_Function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_Function__effbd104_Function9", None)
        self.__effbd104_Function9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd104_InputPort"):
                    opp_val = getattr(item, "effbd104_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd104_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd104_InputPort"):
                    opp_val = getattr(item, "effbd104_InputPort", None)
                    
                    setattr(item, "effbd104_InputPort", self)
                    

    @property
    def effbd104_Function5(self):
        return self.__effbd104_Function5

    @effbd104_Function5.setter
    def effbd104_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_Function__effbd104_Function5", None)
        self.__effbd104_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd104_Flow"):
                    opp_val = getattr(item, "effbd104_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd104_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd104_Flow"):
                    opp_val = getattr(item, "effbd104_Flow", None)
                    
                    setattr(item, "effbd104_Flow", self)
                    

    @property
    def effbd104_Function11(self):
        return self.__effbd104_Function11

    @effbd104_Function11.setter
    def effbd104_Function11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd104_Function__effbd104_Function11", None)
        self.__effbd104_Function11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd104_Description"):
                    opp_val = getattr(item, "effbd104_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd104_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd104_Description"):
                    opp_val = getattr(item, "effbd104_Description", None)
                    
                    setattr(item, "effbd104_Description", self)
                    

class Sequence:

    pass
class effbd104_Loop(Sequence):

    pass
class effbd104_Iteration(Sequence):

    pass
class effbd104_Start(Sequence):

    pass
class effbd104_Final(Sequence):

    pass
class effbd104_LoopExit(Sequence):

    pass
class effbd104_Or(Sequence):

    pass
class effbd104_And(Sequence):

    pass