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

class effbd102_ProcessNode(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class effbd102_Item:

    def __init__(self, name: str, effbd102_Item: "effbd102_Flow" = None):
        self.name = name
        self.effbd102_Item = effbd102_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbd102_Item(self):
        return self.__effbd102_Item

    @effbd102_Item.setter
    def effbd102_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_Item__effbd102_Item", None)
        self.__effbd102_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd102_Flow18"):
                opp_val = getattr(old_value, "effbd102_Flow18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd102_Flow18"):
                opp_val = getattr(value, "effbd102_Flow18", None)
                if opp_val is None:
                    setattr(value, "effbd102_Flow18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd102_Port(ABC):

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
class Sequence:

    pass
class effbd102_Iteration(Sequence):

    pass
class effbd102_Start(Sequence):

    pass
class effbd102_LoopExit(Sequence):

    pass
class effbd102_Final(Sequence):

    pass
class effbd102_Or(Sequence):

    pass
class effbd102_Loop(Sequence):

    pass
class effbd102_And(Sequence):

    pass
class effbd102_SequenceNode(ABC):

    def __init__(self, name: str, effbd102_SequenceNode: "effbd102_SequenceNode" = None, effbd102_SequenceNode12: set["effbd102_SequenceNode"] = None):
        self.name = name
        self.effbd102_SequenceNode = effbd102_SequenceNode
        self.effbd102_SequenceNode12 = effbd102_SequenceNode12 if effbd102_SequenceNode12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbd102_SequenceNode12(self):
        return self.__effbd102_SequenceNode12

    @effbd102_SequenceNode12.setter
    def effbd102_SequenceNode12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_SequenceNode__effbd102_SequenceNode12", None)
        self.__effbd102_SequenceNode12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd102_SequenceNode"):
                    opp_val = getattr(item, "effbd102_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd102_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd102_SequenceNode"):
                    opp_val = getattr(item, "effbd102_SequenceNode", None)
                    
                    setattr(item, "effbd102_SequenceNode", self)
                    

    @property
    def effbd102_SequenceNode(self):
        return self.__effbd102_SequenceNode

    @effbd102_SequenceNode.setter
    def effbd102_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_SequenceNode__effbd102_SequenceNode", None)
        self.__effbd102_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd102_SequenceNode12"):
                opp_val = getattr(old_value, "effbd102_SequenceNode12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd102_SequenceNode12"):
                opp_val = getattr(value, "effbd102_SequenceNode12", None)
                if opp_val is None:
                    setattr(value, "effbd102_SequenceNode12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd102_Description:

    def __init__(self, content: str, effbd102_Description: "effbd102_Function" = None):
        self.content = content
        self.effbd102_Description = effbd102_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def effbd102_Description(self):
        return self.__effbd102_Description

    @effbd102_Description.setter
    def effbd102_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_Description__effbd102_Description", None)
        self.__effbd102_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd102_Function11"):
                opp_val = getattr(old_value, "effbd102_Function11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd102_Function11"):
                opp_val = getattr(value, "effbd102_Function11", None)
                if opp_val is None:
                    setattr(value, "effbd102_Function11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd102_InputPort(Port):

    pass
class effbd102_OutputPort(Port):

    pass
class ProcessNode:

    pass
class effbd102_Flow(ProcessNode):

    pass
class SequenceNode:

    pass
class effbd102_Sequence(SequenceNode):

    pass
class effbd102_Function(ProcessNode, SequenceNode):

    def __init__(self, domain: str, minDuration: float, maxDuration: float, effbd102_Function: "effbd102_Function" = None, effbd102_Function0: set["effbd102_Function"] = None, effbd102_Function3: set["effbd102_Sequence"] = None, effbd102_Function5: set["effbd102_Flow"] = None, effbd102_Function7: set["effbd102_OutputPort"] = None, effbd102_Function9: set["effbd102_InputPort"] = None, effbd102_Function11: set["effbd102_Description"] = None):
        self.domain = domain
        self.minDuration = minDuration
        self.maxDuration = maxDuration
        self.effbd102_Function = effbd102_Function
        self.effbd102_Function0 = effbd102_Function0 if effbd102_Function0 is not None else set()
        self.effbd102_Function3 = effbd102_Function3 if effbd102_Function3 is not None else set()
        self.effbd102_Function5 = effbd102_Function5 if effbd102_Function5 is not None else set()
        self.effbd102_Function7 = effbd102_Function7 if effbd102_Function7 is not None else set()
        self.effbd102_Function9 = effbd102_Function9 if effbd102_Function9 is not None else set()
        self.effbd102_Function11 = effbd102_Function11 if effbd102_Function11 is not None else set()
        
    @property
    def minDuration(self) -> float:
        return self.__minDuration

    @minDuration.setter
    def minDuration(self, minDuration: float):
        self.__minDuration = minDuration

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def maxDuration(self) -> float:
        return self.__maxDuration

    @maxDuration.setter
    def maxDuration(self, maxDuration: float):
        self.__maxDuration = maxDuration

    @property
    def effbd102_Function7(self):
        return self.__effbd102_Function7

    @effbd102_Function7.setter
    def effbd102_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_Function__effbd102_Function7", None)
        self.__effbd102_Function7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd102_OutputPort"):
                    opp_val = getattr(item, "effbd102_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd102_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd102_OutputPort"):
                    opp_val = getattr(item, "effbd102_OutputPort", None)
                    
                    setattr(item, "effbd102_OutputPort", self)
                    

    @property
    def effbd102_Function5(self):
        return self.__effbd102_Function5

    @effbd102_Function5.setter
    def effbd102_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_Function__effbd102_Function5", None)
        self.__effbd102_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd102_Flow"):
                    opp_val = getattr(item, "effbd102_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd102_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd102_Flow"):
                    opp_val = getattr(item, "effbd102_Flow", None)
                    
                    setattr(item, "effbd102_Flow", self)
                    

    @property
    def effbd102_Function3(self):
        return self.__effbd102_Function3

    @effbd102_Function3.setter
    def effbd102_Function3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_Function__effbd102_Function3", None)
        self.__effbd102_Function3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd102_Sequence"):
                    opp_val = getattr(item, "effbd102_Sequence", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd102_Sequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd102_Sequence"):
                    opp_val = getattr(item, "effbd102_Sequence", None)
                    
                    setattr(item, "effbd102_Sequence", self)
                    

    @property
    def effbd102_Function11(self):
        return self.__effbd102_Function11

    @effbd102_Function11.setter
    def effbd102_Function11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_Function__effbd102_Function11", None)
        self.__effbd102_Function11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd102_Description"):
                    opp_val = getattr(item, "effbd102_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd102_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd102_Description"):
                    opp_val = getattr(item, "effbd102_Description", None)
                    
                    setattr(item, "effbd102_Description", self)
                    

    @property
    def effbd102_Function(self):
        return self.__effbd102_Function

    @effbd102_Function.setter
    def effbd102_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_Function__effbd102_Function", None)
        self.__effbd102_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd102_Function0"):
                opp_val = getattr(old_value, "effbd102_Function0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd102_Function0"):
                opp_val = getattr(value, "effbd102_Function0", None)
                if opp_val is None:
                    setattr(value, "effbd102_Function0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbd102_Function9(self):
        return self.__effbd102_Function9

    @effbd102_Function9.setter
    def effbd102_Function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_Function__effbd102_Function9", None)
        self.__effbd102_Function9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd102_InputPort"):
                    opp_val = getattr(item, "effbd102_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd102_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd102_InputPort"):
                    opp_val = getattr(item, "effbd102_InputPort", None)
                    
                    setattr(item, "effbd102_InputPort", self)
                    

    @property
    def effbd102_Function0(self):
        return self.__effbd102_Function0

    @effbd102_Function0.setter
    def effbd102_Function0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd102_Function__effbd102_Function0", None)
        self.__effbd102_Function0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd102_Function"):
                    opp_val = getattr(item, "effbd102_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd102_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd102_Function"):
                    opp_val = getattr(item, "effbd102_Function", None)
                    
                    setattr(item, "effbd102_Function", self)
                    
