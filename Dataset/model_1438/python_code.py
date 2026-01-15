from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class mention_graph_HashTag(Node):

    def __init__(self, count: int, mention_graph_HashTag: "mention_graph_User" = None):
        self.count = count
        self.mention_graph_HashTag = mention_graph_HashTag
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def mention_graph_HashTag(self):
        return self.__mention_graph_HashTag

    @mention_graph_HashTag.setter
    def mention_graph_HashTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mention_graph_HashTag__mention_graph_HashTag", None)
        self.__mention_graph_HashTag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mention_graph_User"):
                opp_val = getattr(old_value, "mention_graph_User", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mention_graph_User"):
                opp_val = getattr(value, "mention_graph_User", None)
                if opp_val is None:
                    setattr(value, "mention_graph_User", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mention_graph_User(Node):

    pass
class mention_graph_Edge:

    pass
class mention_graph_Node(ABC):

    def __init__(self, value: str, mention_graph_Node: "mention_graph_MentionGraph" = None, mention_graph_Node6: "mention_graph_Edge" = None, mention_graph_Node9: "mention_graph_Edge" = None):
        self.value = value
        self.mention_graph_Node = mention_graph_Node
        self.mention_graph_Node6 = mention_graph_Node6
        self.mention_graph_Node9 = mention_graph_Node9
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def mention_graph_Node9(self):
        return self.__mention_graph_Node9

    @mention_graph_Node9.setter
    def mention_graph_Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mention_graph_Node__mention_graph_Node9", None)
        self.__mention_graph_Node9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mention_graph_Edge8"):
                opp_val = getattr(old_value, "mention_graph_Edge8", None)
                if opp_val == self:
                    setattr(old_value, "mention_graph_Edge8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mention_graph_Edge8"):
                opp_val = getattr(value, "mention_graph_Edge8", None)
                setattr(value, "mention_graph_Edge8", self)

    @property
    def mention_graph_Node6(self):
        return self.__mention_graph_Node6

    @mention_graph_Node6.setter
    def mention_graph_Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mention_graph_Node__mention_graph_Node6", None)
        self.__mention_graph_Node6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mention_graph_Edge5"):
                opp_val = getattr(old_value, "mention_graph_Edge5", None)
                if opp_val == self:
                    setattr(old_value, "mention_graph_Edge5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mention_graph_Edge5"):
                opp_val = getattr(value, "mention_graph_Edge5", None)
                setattr(value, "mention_graph_Edge5", self)

    @property
    def mention_graph_Node(self):
        return self.__mention_graph_Node

    @mention_graph_Node.setter
    def mention_graph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mention_graph_Node__mention_graph_Node", None)
        self.__mention_graph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mention_graph_MentionGraph"):
                opp_val = getattr(old_value, "mention_graph_MentionGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mention_graph_MentionGraph"):
                opp_val = getattr(value, "mention_graph_MentionGraph", None)
                if opp_val is None:
                    setattr(value, "mention_graph_MentionGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mention_graph_MentionGraph:

    pass