from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Port:

    pass
class effbd101_ProcessNode(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class effbd101_Item:

    def __init__(self, name: str, effbd101_Item: "effbd101_Flow" = None):
        self.name = name
        self.effbd101_Item = effbd101_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbd101_Item(self):
        return self.__effbd101_Item

    @effbd101_Item.setter
    def effbd101_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd101_Item__effbd101_Item", None)
        self.__effbd101_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd101_Flow18"):
                opp_val = getattr(old_value, "effbd101_Flow18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd101_Flow18"):
                opp_val = getattr(value, "effbd101_Flow18", None)
                if opp_val is None:
                    setattr(value, "effbd101_Flow18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd101_Port(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class Sequence:

    pass
class effbd101_Loop(Sequence):

    pass
class effbd101_Start(Sequence):

    pass
class effbd101_Final(Sequence):

    pass
class effbd101_Or(Sequence):

    pass
class effbd101_And(Sequence):

    pass
class effbd101_SequenceNode(ABC):

    def __init__(self, name: str, effbd101_SequenceNode: "effbd101_SequenceNode" = None, effbd101_SequenceNode12: set["effbd101_SequenceNode"] = None):
        self.name = name
        self.effbd101_SequenceNode = effbd101_SequenceNode
        self.effbd101_SequenceNode12 = effbd101_SequenceNode12 if effbd101_SequenceNode12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def effbd101_SequenceNode(self):
        return self.__effbd101_SequenceNode

    @effbd101_SequenceNode.setter
    def effbd101_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd101_SequenceNode__effbd101_SequenceNode", None)
        self.__effbd101_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd101_SequenceNode12"):
                opp_val = getattr(old_value, "effbd101_SequenceNode12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd101_SequenceNode12"):
                opp_val = getattr(value, "effbd101_SequenceNode12", None)
                if opp_val is None:
                    setattr(value, "effbd101_SequenceNode12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def effbd101_SequenceNode12(self):
        return self.__effbd101_SequenceNode12

    @effbd101_SequenceNode12.setter
    def effbd101_SequenceNode12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd101_SequenceNode__effbd101_SequenceNode12", None)
        self.__effbd101_SequenceNode12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "effbd101_SequenceNode"):
                    opp_val = getattr(item, "effbd101_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "effbd101_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "effbd101_SequenceNode"):
                    opp_val = getattr(item, "effbd101_SequenceNode", None)
                    
                    setattr(item, "effbd101_SequenceNode", self)
                    

class effbd101_Description:

    def __init__(self, content: str, effbd101_Description: "effbd101_Function" = None):
        self.content = content
        self.effbd101_Description = effbd101_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def effbd101_Description(self):
        return self.__effbd101_Description

    @effbd101_Description.setter
    def effbd101_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_effbd101_Description__effbd101_Description", None)
        self.__effbd101_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "effbd101_Function11"):
                opp_val = getattr(old_value, "effbd101_Function11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "effbd101_Function11"):
                opp_val = getattr(value, "effbd101_Function11", None)
                if opp_val is None:
                    setattr(value, "effbd101_Function11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class effbd101_InputPort(Port):

    pass
class effbd101_OutputPort(Port):

    pass
class ProcessNode:

    pass
class effbd101_Flow(ProcessNode):

    pass
class SequenceNode:

    pass
class effbd101_Sequence(SequenceNode):

    pass
class effbd101_Function(SequenceNode, ProcessNode):

    pass