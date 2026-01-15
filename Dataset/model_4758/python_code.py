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

class effbd902_ProcessNode(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class Sequence:

    pass
class effbd902_LoopExit(Sequence):

    pass
class effbd902_Iteration(Sequence):

    pass
class effbd902_And(Sequence):

    pass
class effbd902_SequenceNode(ABC):

    def __init__(self, name: str, tMin: int, tMax: int, effbd902_SequenceNode: "effbd902_SequenceNode" = None, effbd902_SequenceNode13: set["effbd902_SequenceNode"] = None):
        self.name = name
        self.tMin = tMin
        self.tMax = tMax
        self.effbd902_SequenceNode = effbd902_SequenceNode
        self.effbd902_SequenceNode13 = effbd902_SequenceNode13 if effbd902_SequenceNode13 is not None else set()
        
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
    def effbd902_SequenceNode(self):
        return self.__effbd902_SequenceNode

    @effbd902_SequenceNode.setter
    def effbd902_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_SequenceNode__effbd902_SequenceNode", None)
        self.__effbd902_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd902_SequenceNode13"):
                opp_val = getattr(old_value, "effbd902_SequenceNode13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd902_SequenceNode13"):
                opp_val = getattr(value, "effbd902_SequenceNode13", None)
                if opp_val is None:
                    setattr(value, "effbd902_SequenceNode13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbd902_SequenceNode13(self):
        return self.__effbd902_SequenceNode13

    @effbd902_SequenceNode13.setter
    def effbd902_SequenceNode13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_SequenceNode__effbd902_SequenceNode13", None)
        self.__effbd902_SequenceNode13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd902_SequenceNode"):
                    opp_val = getattr(item, "effbd902_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd902_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd902_SequenceNode"):
                    opp_val = getattr(item, "effbd902_SequenceNode", None)
                    
                    setattr(item, "effbd902_SequenceNode", self)
                    

class effbd902_Token:

    pass
class effbd902_Description:

    def __init__(self, content: str, effbd902_Description: "effbd902_Function" = None):
        self.content = content
        self.effbd902_Description = effbd902_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def effbd902_Description(self):
        return self.__effbd902_Description

    @effbd902_Description.setter
    def effbd902_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_Description__effbd902_Description", None)
        self.__effbd902_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd902_Function10"):
                opp_val = getattr(old_value, "effbd902_Function10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd902_Function10"):
                opp_val = getattr(value, "effbd902_Function10", None)
                if opp_val is None:
                    setattr(value, "effbd902_Function10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd902_Item:

    def __init__(self, name: str, effbd902_Item: "effbd902_Flow" = None):
        self.name = name
        self.effbd902_Item = effbd902_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbd902_Item(self):
        return self.__effbd902_Item

    @effbd902_Item.setter
    def effbd902_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_Item__effbd902_Item", None)
        self.__effbd902_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd902_Flow19"):
                opp_val = getattr(old_value, "effbd902_Flow19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd902_Flow19"):
                opp_val = getattr(value, "effbd902_Flow19", None)
                if opp_val is None:
                    setattr(value, "effbd902_Flow19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd902_Port(ABC):

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
class effbd902_Loop(Sequence):

    pass
class effbd902_Final(Sequence):

    pass
class effbd902_Start(Sequence):

    pass
class effbd902_Or(Sequence):

    pass
class effbd902_InputPort(Port):

    pass
class effbd902_OutputPort(Port):

    pass
class effbd902_AbstractFunction(ABC):

    def __init__(self, id: str, effbd902_AbstractFunction: "effbd902_Function" = None):
        self.id = id
        self.effbd902_AbstractFunction = effbd902_AbstractFunction
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def effbd902_AbstractFunction(self):
        return self.__effbd902_AbstractFunction

    @effbd902_AbstractFunction.setter
    def effbd902_AbstractFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_AbstractFunction__effbd902_AbstractFunction", None)
        self.__effbd902_AbstractFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd902_Function"):
                opp_val = getattr(old_value, "effbd902_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd902_Function"):
                opp_val = getattr(value, "effbd902_Function", None)
                if opp_val is None:
                    setattr(value, "effbd902_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractFunction:

    pass
class ProcessNode:

    pass
class effbd902_Flow(ProcessNode):

    pass
class SequenceNode:

    pass
class effbd902_Sequence(SequenceNode):

    pass
class effbd902_Function(SequenceNode, AbstractFunction, ProcessNode):

    def __init__(self, domain: str, effbd902_Function: set["effbd902_AbstractFunction"] = None, effbd902_Function2: set["effbd902_Sequence"] = None, effbd902_Function4: set["effbd902_Flow"] = None, effbd902_Function6: set["effbd902_OutputPort"] = None, effbd902_Function8: set["effbd902_InputPort"] = None, effbd902_Function10: set["effbd902_Description"] = None, effbd902_Function12: set["effbd902_Token"] = None):
        self.domain = domain
        self.effbd902_Function = effbd902_Function if effbd902_Function is not None else set()
        self.effbd902_Function2 = effbd902_Function2 if effbd902_Function2 is not None else set()
        self.effbd902_Function4 = effbd902_Function4 if effbd902_Function4 is not None else set()
        self.effbd902_Function6 = effbd902_Function6 if effbd902_Function6 is not None else set()
        self.effbd902_Function8 = effbd902_Function8 if effbd902_Function8 is not None else set()
        self.effbd902_Function10 = effbd902_Function10 if effbd902_Function10 is not None else set()
        self.effbd902_Function12 = effbd902_Function12 if effbd902_Function12 is not None else set()
        
    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def effbd902_Function(self):
        return self.__effbd902_Function

    @effbd902_Function.setter
    def effbd902_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_Function__effbd902_Function", None)
        self.__effbd902_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd902_AbstractFunction"):
                    opp_val = getattr(item, "effbd902_AbstractFunction", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd902_AbstractFunction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd902_AbstractFunction"):
                    opp_val = getattr(item, "effbd902_AbstractFunction", None)
                    
                    setattr(item, "effbd902_AbstractFunction", self)
                    

    @property
    def effbd902_Function10(self):
        return self.__effbd902_Function10

    @effbd902_Function10.setter
    def effbd902_Function10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_Function__effbd902_Function10", None)
        self.__effbd902_Function10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd902_Description"):
                    opp_val = getattr(item, "effbd902_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd902_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd902_Description"):
                    opp_val = getattr(item, "effbd902_Description", None)
                    
                    setattr(item, "effbd902_Description", self)
                    

    @property
    def effbd902_Function4(self):
        return self.__effbd902_Function4

    @effbd902_Function4.setter
    def effbd902_Function4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_Function__effbd902_Function4", None)
        self.__effbd902_Function4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd902_Flow"):
                    opp_val = getattr(item, "effbd902_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd902_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd902_Flow"):
                    opp_val = getattr(item, "effbd902_Flow", None)
                    
                    setattr(item, "effbd902_Flow", self)
                    

    @property
    def effbd902_Function2(self):
        return self.__effbd902_Function2

    @effbd902_Function2.setter
    def effbd902_Function2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_Function__effbd902_Function2", None)
        self.__effbd902_Function2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd902_Sequence"):
                    opp_val = getattr(item, "effbd902_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd902_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd902_Sequence"):
                    opp_val = getattr(item, "effbd902_Sequence", None)
                    
                    setattr(item, "effbd902_Sequence", self)
                    

    @property
    def effbd902_Function6(self):
        return self.__effbd902_Function6

    @effbd902_Function6.setter
    def effbd902_Function6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_Function__effbd902_Function6", None)
        self.__effbd902_Function6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd902_OutputPort"):
                    opp_val = getattr(item, "effbd902_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd902_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd902_OutputPort"):
                    opp_val = getattr(item, "effbd902_OutputPort", None)
                    
                    setattr(item, "effbd902_OutputPort", self)
                    

    @property
    def effbd902_Function12(self):
        return self.__effbd902_Function12

    @effbd902_Function12.setter
    def effbd902_Function12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_Function__effbd902_Function12", None)
        self.__effbd902_Function12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd902_Token"):
                    opp_val = getattr(item, "effbd902_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd902_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd902_Token"):
                    opp_val = getattr(item, "effbd902_Token", None)
                    
                    setattr(item, "effbd902_Token", self)
                    

    @property
    def effbd902_Function8(self):
        return self.__effbd902_Function8

    @effbd902_Function8.setter
    def effbd902_Function8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd902_Function__effbd902_Function8", None)
        self.__effbd902_Function8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd902_InputPort"):
                    opp_val = getattr(item, "effbd902_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd902_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd902_InputPort"):
                    opp_val = getattr(item, "effbd902_InputPort", None)
                    
                    setattr(item, "effbd902_InputPort", self)
                    
