from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class bintree_BinTreeNode:

    def __init__(self, data: str, bintree_BinTreeNode: "bintree_BinTreeNode" = None, bintree_BinTreeNode0: "bintree_BinTreeNode" = None, bintree_BinTreeNode4: "bintree_BinTreeNode" = None, bintree_BinTreeNode2: "bintree_BinTreeNode" = None, bintree_BinTreeNode7: "bintree_BinTreeNode" = None, bintree_BinTreeNode5: "bintree_BinTreeNode" = None):
        self.data = data
        self.bintree_BinTreeNode = bintree_BinTreeNode
        self.bintree_BinTreeNode0 = bintree_BinTreeNode0
        self.bintree_BinTreeNode4 = bintree_BinTreeNode4
        self.bintree_BinTreeNode2 = bintree_BinTreeNode2
        self.bintree_BinTreeNode7 = bintree_BinTreeNode7
        self.bintree_BinTreeNode5 = bintree_BinTreeNode5
        
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def bintree_BinTreeNode2(self):
        return self.__bintree_BinTreeNode2

    @bintree_BinTreeNode2.setter
    def bintree_BinTreeNode2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bintree_BinTreeNode__bintree_BinTreeNode2", None)
        self.__bintree_BinTreeNode2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bintree_BinTreeNode4"):
                opp_val = getattr(old_value, "bintree_BinTreeNode4", None)
                if opp_val == self:
                    setattr(old_value, "bintree_BinTreeNode4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bintree_BinTreeNode4"):
                opp_val = getattr(value, "bintree_BinTreeNode4", None)
                setattr(value, "bintree_BinTreeNode4", self)

    @property
    def bintree_BinTreeNode(self):
        return self.__bintree_BinTreeNode

    @bintree_BinTreeNode.setter
    def bintree_BinTreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bintree_BinTreeNode__bintree_BinTreeNode", None)
        self.__bintree_BinTreeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bintree_BinTreeNode0"):
                opp_val = getattr(old_value, "bintree_BinTreeNode0", None)
                if opp_val == self:
                    setattr(old_value, "bintree_BinTreeNode0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bintree_BinTreeNode0"):
                opp_val = getattr(value, "bintree_BinTreeNode0", None)
                setattr(value, "bintree_BinTreeNode0", self)

    @property
    def bintree_BinTreeNode7(self):
        return self.__bintree_BinTreeNode7

    @bintree_BinTreeNode7.setter
    def bintree_BinTreeNode7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bintree_BinTreeNode__bintree_BinTreeNode7", None)
        self.__bintree_BinTreeNode7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bintree_BinTreeNode5"):
                opp_val = getattr(old_value, "bintree_BinTreeNode5", None)
                if opp_val == self:
                    setattr(old_value, "bintree_BinTreeNode5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bintree_BinTreeNode5"):
                opp_val = getattr(value, "bintree_BinTreeNode5", None)
                setattr(value, "bintree_BinTreeNode5", self)

    @property
    def bintree_BinTreeNode0(self):
        return self.__bintree_BinTreeNode0

    @bintree_BinTreeNode0.setter
    def bintree_BinTreeNode0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bintree_BinTreeNode__bintree_BinTreeNode0", None)
        self.__bintree_BinTreeNode0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bintree_BinTreeNode"):
                opp_val = getattr(old_value, "bintree_BinTreeNode", None)
                if opp_val == self:
                    setattr(old_value, "bintree_BinTreeNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bintree_BinTreeNode"):
                opp_val = getattr(value, "bintree_BinTreeNode", None)
                setattr(value, "bintree_BinTreeNode", self)

    @property
    def bintree_BinTreeNode4(self):
        return self.__bintree_BinTreeNode4

    @bintree_BinTreeNode4.setter
    def bintree_BinTreeNode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bintree_BinTreeNode__bintree_BinTreeNode4", None)
        self.__bintree_BinTreeNode4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bintree_BinTreeNode2"):
                opp_val = getattr(old_value, "bintree_BinTreeNode2", None)
                if opp_val == self:
                    setattr(old_value, "bintree_BinTreeNode2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bintree_BinTreeNode2"):
                opp_val = getattr(value, "bintree_BinTreeNode2", None)
                setattr(value, "bintree_BinTreeNode2", self)

    @property
    def bintree_BinTreeNode5(self):
        return self.__bintree_BinTreeNode5

    @bintree_BinTreeNode5.setter
    def bintree_BinTreeNode5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bintree_BinTreeNode__bintree_BinTreeNode5", None)
        self.__bintree_BinTreeNode5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bintree_BinTreeNode7"):
                opp_val = getattr(old_value, "bintree_BinTreeNode7", None)
                if opp_val == self:
                    setattr(old_value, "bintree_BinTreeNode7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bintree_BinTreeNode7"):
                opp_val = getattr(value, "bintree_BinTreeNode7", None)
                setattr(value, "bintree_BinTreeNode7", self)
