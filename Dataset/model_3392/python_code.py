from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Topic:

    pass
class mindmap_SubTopic(Topic):

    pass
class mindmap_MainTopic(Topic):

    pass
class mindmap_Topic(ABC):

    def __init__(self, name: str, marker: int):
        self.name = name
        self.marker = marker
        
    @property
    def marker(self) -> int:
        return self.__marker

    @marker.setter
    def marker(self, marker: int):
        self.__marker = marker

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class mindmap_CentralTopic(Topic):

    pass
class mindmap_MindMap:

    def __init__(self, title: str, mindmap_MindMap: "mindmap_CentralTopic" = None):
        self.title = title
        self.mindmap_MindMap = mindmap_MindMap
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def mindmap_MindMap(self):
        return self.__mindmap_MindMap

    @mindmap_MindMap.setter
    def mindmap_MindMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mindmap_MindMap__mindmap_MindMap", None)
        self.__mindmap_MindMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mindmap_CentralTopic"):
                opp_val = getattr(old_value, "mindmap_CentralTopic", None)
                if opp_val == self:
                    setattr(old_value, "mindmap_CentralTopic", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mindmap_CentralTopic"):
                opp_val = getattr(value, "mindmap_CentralTopic", None)
                setattr(value, "mindmap_CentralTopic", self)
