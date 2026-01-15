from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    RED = "RED"
    BLACK = "BLACK"
class Type(Enum):
    NODE = "NODE"
    LEAF = "LEAF"
    ROOT = "ROOT"


############################################
# Definition of Classes
############################################

class redblacktree2_Node:

    def __init__(self, value: int, redblacktree2_Node: "redblacktree2_Tree" = None, redblacktree2_Node6: "redblacktree2_Node" = None, redblacktree2_Node4: "redblacktree2_Node" = None, redblacktree2_Node9: "redblacktree2_Node" = None, redblacktree2_Node7: "redblacktree2_Node" = None, redblacktree2_Node3: "redblacktree2_Tree" = None):
        self.value = value
        self.redblacktree2_Node = redblacktree2_Node
        self.redblacktree2_Node6 = redblacktree2_Node6
        self.redblacktree2_Node4 = redblacktree2_Node4
        self.redblacktree2_Node9 = redblacktree2_Node9
        self.redblacktree2_Node7 = redblacktree2_Node7
        self.redblacktree2_Node3 = redblacktree2_Node3
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def redblacktree2_Node(self):
        return self.__redblacktree2_Node

    @redblacktree2_Node.setter
    def redblacktree2_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_redblacktree2_Node__redblacktree2_Node", None)
        self.__redblacktree2_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "redblacktree2_Tree"):
                opp_val = getattr(old_value, "redblacktree2_Tree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "redblacktree2_Tree"):
                opp_val = getattr(value, "redblacktree2_Tree", None)
                if opp_val is None:
                    setattr(value, "redblacktree2_Tree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def redblacktree2_Node6(self):
        return self.__redblacktree2_Node6

    @redblacktree2_Node6.setter
    def redblacktree2_Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_redblacktree2_Node__redblacktree2_Node6", None)
        self.__redblacktree2_Node6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "redblacktree2_Node4"):
                opp_val = getattr(old_value, "redblacktree2_Node4", None)
                if opp_val == self:
                    setattr(old_value, "redblacktree2_Node4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "redblacktree2_Node4"):
                opp_val = getattr(value, "redblacktree2_Node4", None)
                setattr(value, "redblacktree2_Node4", self)

    @property
    def redblacktree2_Node7(self):
        return self.__redblacktree2_Node7

    @redblacktree2_Node7.setter
    def redblacktree2_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_redblacktree2_Node__redblacktree2_Node7", None)
        self.__redblacktree2_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "redblacktree2_Node9"):
                opp_val = getattr(old_value, "redblacktree2_Node9", None)
                if opp_val == self:
                    setattr(old_value, "redblacktree2_Node9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "redblacktree2_Node9"):
                opp_val = getattr(value, "redblacktree2_Node9", None)
                setattr(value, "redblacktree2_Node9", self)

    @property
    def redblacktree2_Node9(self):
        return self.__redblacktree2_Node9

    @redblacktree2_Node9.setter
    def redblacktree2_Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_redblacktree2_Node__redblacktree2_Node9", None)
        self.__redblacktree2_Node9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "redblacktree2_Node7"):
                opp_val = getattr(old_value, "redblacktree2_Node7", None)
                if opp_val == self:
                    setattr(old_value, "redblacktree2_Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "redblacktree2_Node7"):
                opp_val = getattr(value, "redblacktree2_Node7", None)
                setattr(value, "redblacktree2_Node7", self)

    @property
    def redblacktree2_Node4(self):
        return self.__redblacktree2_Node4

    @redblacktree2_Node4.setter
    def redblacktree2_Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_redblacktree2_Node__redblacktree2_Node4", None)
        self.__redblacktree2_Node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "redblacktree2_Node6"):
                opp_val = getattr(old_value, "redblacktree2_Node6", None)
                if opp_val == self:
                    setattr(old_value, "redblacktree2_Node6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "redblacktree2_Node6"):
                opp_val = getattr(value, "redblacktree2_Node6", None)
                setattr(value, "redblacktree2_Node6", self)

    @property
    def redblacktree2_Node3(self):
        return self.__redblacktree2_Node3

    @redblacktree2_Node3.setter
    def redblacktree2_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_redblacktree2_Node__redblacktree2_Node3", None)
        self.__redblacktree2_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "redblacktree2_Tree2"):
                opp_val = getattr(old_value, "redblacktree2_Tree2", None)
                if opp_val == self:
                    setattr(old_value, "redblacktree2_Tree2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "redblacktree2_Tree2"):
                opp_val = getattr(value, "redblacktree2_Tree2", None)
                setattr(value, "redblacktree2_Tree2", self)

class redblacktree2_Tree:

    pass