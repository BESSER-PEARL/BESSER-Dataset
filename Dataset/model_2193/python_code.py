from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TreeNode:

    pass
class tree_NonTerminal(TreeNode):

    pass
class tree_Leaf(TreeNode):

    pass
class tree_TreeNode(ABC):

    def __init__(self, data: str, tree_TreeNode: "tree_TreeNode" = None, tree_TreeNode0: "tree_TreeNode" = None, tree_TreeNode3: "tree_NonTerminal" = None):
        self.data = data
        self.tree_TreeNode = tree_TreeNode
        self.tree_TreeNode0 = tree_TreeNode0
        self.tree_TreeNode3 = tree_TreeNode3
        
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def tree_TreeNode3(self):
        return self.__tree_TreeNode3

    @tree_TreeNode3.setter
    def tree_TreeNode3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_TreeNode__tree_TreeNode3", None)
        self.__tree_TreeNode3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_NonTerminal"):
                opp_val = getattr(old_value, "tree_NonTerminal", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_NonTerminal"):
                opp_val = getattr(value, "tree_NonTerminal", None)
                if opp_val is None:
                    setattr(value, "tree_NonTerminal", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tree_TreeNode0(self):
        return self.__tree_TreeNode0

    @tree_TreeNode0.setter
    def tree_TreeNode0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_TreeNode__tree_TreeNode0", None)
        self.__tree_TreeNode0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_TreeNode"):
                opp_val = getattr(old_value, "tree_TreeNode", None)
                if opp_val == self:
                    setattr(old_value, "tree_TreeNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_TreeNode"):
                opp_val = getattr(value, "tree_TreeNode", None)
                setattr(value, "tree_TreeNode", self)

    @property
    def tree_TreeNode(self):
        return self.__tree_TreeNode

    @tree_TreeNode.setter
    def tree_TreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_TreeNode__tree_TreeNode", None)
        self.__tree_TreeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_TreeNode0"):
                opp_val = getattr(old_value, "tree_TreeNode0", None)
                if opp_val == self:
                    setattr(old_value, "tree_TreeNode0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_TreeNode0"):
                opp_val = getattr(value, "tree_TreeNode0", None)
                setattr(value, "tree_TreeNode0", self)
