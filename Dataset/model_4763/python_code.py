from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class itemflow101_Port(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class itemflow101_Item:

    def __init__(self, name: str, itemflow101_Item: "itemflow101_Flow" = None):
        self.name = name
        self.itemflow101_Item = itemflow101_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def itemflow101_Item(self):
        return self.__itemflow101_Item

    @itemflow101_Item.setter
    def itemflow101_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itemflow101_Item__itemflow101_Item", None)
        self.__itemflow101_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itemflow101_Flow14"):
                opp_val = getattr(old_value, "itemflow101_Flow14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itemflow101_Flow14"):
                opp_val = getattr(value, "itemflow101_Flow14", None)
                if opp_val is None:
                    setattr(value, "itemflow101_Flow14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class itemflow101_Description:

    def __init__(self, content: str, itemflow101_Description: "itemflow101_Function" = None):
        self.content = content
        self.itemflow101_Description = itemflow101_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def itemflow101_Description(self):
        return self.__itemflow101_Description

    @itemflow101_Description.setter
    def itemflow101_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_itemflow101_Description__itemflow101_Description", None)
        self.__itemflow101_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "itemflow101_Function9"):
                opp_val = getattr(old_value, "itemflow101_Function9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "itemflow101_Function9"):
                opp_val = getattr(value, "itemflow101_Function9", None)
                if opp_val is None:
                    setattr(value, "itemflow101_Function9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class itemflow101_ProcessNode(ABC):

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class Port:

    pass
class itemflow101_InputPort(Port):

    pass
class itemflow101_OutputPort(Port):

    pass
class ProcessNode:

    pass
class itemflow101_Flow(ProcessNode):

    pass
class itemflow101_Function(ProcessNode):

    pass