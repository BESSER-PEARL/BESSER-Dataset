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

class effbd201_ProcessNode(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class effbd201_Item:

    def __init__(self, name: str, effbd201_Item: "effbd201_Flow" = None):
        self.name = name
        self.effbd201_Item = effbd201_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbd201_Item(self):
        return self.__effbd201_Item

    @effbd201_Item.setter
    def effbd201_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Item__effbd201_Item", None)
        self.__effbd201_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd201_Flow22"):
                opp_val = getattr(old_value, "effbd201_Flow22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd201_Flow22"):
                opp_val = getattr(value, "effbd201_Flow22", None)
                if opp_val is None:
                    setattr(value, "effbd201_Flow22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd201_Port(ABC):

    def __init__(self, id: str, effbd201_Port: set["effbd201_Flow"] = None, effbd201_Port20: "effbd201_Flow" = None):
        self.id = id
        self.effbd201_Port = effbd201_Port if effbd201_Port is not None else set()
        self.effbd201_Port20 = effbd201_Port20
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def effbd201_Port(self):
        return self.__effbd201_Port

    @effbd201_Port.setter
    def effbd201_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Port__effbd201_Port", None)
        self.__effbd201_Port = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd201_Flow17"):
                    opp_val = getattr(item, "effbd201_Flow17", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd201_Flow17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd201_Flow17"):
                    opp_val = getattr(item, "effbd201_Flow17", None)
                    
                    setattr(item, "effbd201_Flow17", self)
                    

    @property
    def effbd201_Port20(self):
        return self.__effbd201_Port20

    @effbd201_Port20.setter
    def effbd201_Port20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Port__effbd201_Port20", None)
        self.__effbd201_Port20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd201_Flow19"):
                opp_val = getattr(old_value, "effbd201_Flow19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd201_Flow19"):
                opp_val = getattr(value, "effbd201_Flow19", None)
                if opp_val is None:
                    setattr(value, "effbd201_Flow19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Port:

    pass
class effbd201_SequenceNode(ABC):

    def __init__(self, tMax: int, name: str, tMin: int, effbd201_SequenceNode: "effbd201_SequenceNode" = None, effbd201_SequenceNode14: set["effbd201_SequenceNode"] = None):
        self.tMax = tMax
        self.name = name
        self.tMin = tMin
        self.effbd201_SequenceNode = effbd201_SequenceNode
        self.effbd201_SequenceNode14 = effbd201_SequenceNode14 if effbd201_SequenceNode14 is not None else set()
        
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
    def effbd201_SequenceNode(self):
        return self.__effbd201_SequenceNode

    @effbd201_SequenceNode.setter
    def effbd201_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_SequenceNode__effbd201_SequenceNode", None)
        self.__effbd201_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd201_SequenceNode14"):
                opp_val = getattr(old_value, "effbd201_SequenceNode14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd201_SequenceNode14"):
                opp_val = getattr(value, "effbd201_SequenceNode14", None)
                if opp_val is None:
                    setattr(value, "effbd201_SequenceNode14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbd201_SequenceNode14(self):
        return self.__effbd201_SequenceNode14

    @effbd201_SequenceNode14.setter
    def effbd201_SequenceNode14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_SequenceNode__effbd201_SequenceNode14", None)
        self.__effbd201_SequenceNode14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd201_SequenceNode"):
                    opp_val = getattr(item, "effbd201_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd201_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd201_SequenceNode"):
                    opp_val = getattr(item, "effbd201_SequenceNode", None)
                    
                    setattr(item, "effbd201_SequenceNode", self)
                    

class effbd201_Token:

    pass
class effbd201_Description:

    def __init__(self, content: str, effbd201_Description: "effbd201_Function" = None):
        self.content = content
        self.effbd201_Description = effbd201_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def effbd201_Description(self):
        return self.__effbd201_Description

    @effbd201_Description.setter
    def effbd201_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Description__effbd201_Description", None)
        self.__effbd201_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd201_Function11"):
                opp_val = getattr(old_value, "effbd201_Function11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd201_Function11"):
                opp_val = getattr(value, "effbd201_Function11", None)
                if opp_val is None:
                    setattr(value, "effbd201_Function11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd201_InputPort(Port):

    pass
class effbd201_OutputPort(Port):

    pass
class Sequence:

    pass
class effbd201_Loop(Sequence):

    pass
class effbd201_Start(Sequence):

    pass
class effbd201_LoopExit(Sequence):

    pass
class effbd201_Final(Sequence):

    pass
class effbd201_Or(Sequence):

    pass
class effbd201_Iteration(Sequence):

    pass
class effbd201_And(Sequence):

    pass
class ProcessNode:

    pass
class effbd201_Flow(ProcessNode):

    pass
class SequenceNode:

    pass
class effbd201_Sequence(SequenceNode):

    pass
class effbd201_Function(ProcessNode, SequenceNode):

    def __init__(self, domain: str, effbd201_Function: "effbd201_Function" = None, effbd201_Function0: set["effbd201_Function"] = None, effbd201_Function3: set["effbd201_Sequence"] = None, effbd201_Function5: set["effbd201_Flow"] = None, effbd201_Function7: set["effbd201_OutputPort"] = None, effbd201_Function9: set["effbd201_InputPort"] = None, effbd201_Function11: set["effbd201_Description"] = None, effbd201_Function13: set["effbd201_Token"] = None):
        self.domain = domain
        self.effbd201_Function = effbd201_Function
        self.effbd201_Function0 = effbd201_Function0 if effbd201_Function0 is not None else set()
        self.effbd201_Function3 = effbd201_Function3 if effbd201_Function3 is not None else set()
        self.effbd201_Function5 = effbd201_Function5 if effbd201_Function5 is not None else set()
        self.effbd201_Function7 = effbd201_Function7 if effbd201_Function7 is not None else set()
        self.effbd201_Function9 = effbd201_Function9 if effbd201_Function9 is not None else set()
        self.effbd201_Function11 = effbd201_Function11 if effbd201_Function11 is not None else set()
        self.effbd201_Function13 = effbd201_Function13 if effbd201_Function13 is not None else set()
        
    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def effbd201_Function9(self):
        return self.__effbd201_Function9

    @effbd201_Function9.setter
    def effbd201_Function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Function__effbd201_Function9", None)
        self.__effbd201_Function9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd201_InputPort"):
                    opp_val = getattr(item, "effbd201_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd201_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd201_InputPort"):
                    opp_val = getattr(item, "effbd201_InputPort", None)
                    
                    setattr(item, "effbd201_InputPort", self)
                    

    @property
    def effbd201_Function13(self):
        return self.__effbd201_Function13

    @effbd201_Function13.setter
    def effbd201_Function13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Function__effbd201_Function13", None)
        self.__effbd201_Function13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd201_Token"):
                    opp_val = getattr(item, "effbd201_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd201_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd201_Token"):
                    opp_val = getattr(item, "effbd201_Token", None)
                    
                    setattr(item, "effbd201_Token", self)
                    

    @property
    def effbd201_Function7(self):
        return self.__effbd201_Function7

    @effbd201_Function7.setter
    def effbd201_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Function__effbd201_Function7", None)
        self.__effbd201_Function7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd201_OutputPort"):
                    opp_val = getattr(item, "effbd201_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd201_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd201_OutputPort"):
                    opp_val = getattr(item, "effbd201_OutputPort", None)
                    
                    setattr(item, "effbd201_OutputPort", self)
                    

    @property
    def effbd201_Function0(self):
        return self.__effbd201_Function0

    @effbd201_Function0.setter
    def effbd201_Function0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Function__effbd201_Function0", None)
        self.__effbd201_Function0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd201_Function"):
                    opp_val = getattr(item, "effbd201_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd201_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd201_Function"):
                    opp_val = getattr(item, "effbd201_Function", None)
                    
                    setattr(item, "effbd201_Function", self)
                    

    @property
    def effbd201_Function5(self):
        return self.__effbd201_Function5

    @effbd201_Function5.setter
    def effbd201_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Function__effbd201_Function5", None)
        self.__effbd201_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd201_Flow"):
                    opp_val = getattr(item, "effbd201_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd201_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd201_Flow"):
                    opp_val = getattr(item, "effbd201_Flow", None)
                    
                    setattr(item, "effbd201_Flow", self)
                    

    @property
    def effbd201_Function(self):
        return self.__effbd201_Function

    @effbd201_Function.setter
    def effbd201_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Function__effbd201_Function", None)
        self.__effbd201_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd201_Function0"):
                opp_val = getattr(old_value, "effbd201_Function0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd201_Function0"):
                opp_val = getattr(value, "effbd201_Function0", None)
                if opp_val is None:
                    setattr(value, "effbd201_Function0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbd201_Function11(self):
        return self.__effbd201_Function11

    @effbd201_Function11.setter
    def effbd201_Function11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Function__effbd201_Function11", None)
        self.__effbd201_Function11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd201_Description"):
                    opp_val = getattr(item, "effbd201_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd201_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd201_Description"):
                    opp_val = getattr(item, "effbd201_Description", None)
                    
                    setattr(item, "effbd201_Description", self)
                    

    @property
    def effbd201_Function3(self):
        return self.__effbd201_Function3

    @effbd201_Function3.setter
    def effbd201_Function3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd201_Function__effbd201_Function3", None)
        self.__effbd201_Function3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd201_Sequence"):
                    opp_val = getattr(item, "effbd201_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd201_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd201_Sequence"):
                    opp_val = getattr(item, "effbd201_Sequence", None)
                    
                    setattr(item, "effbd201_Sequence", self)
                    
