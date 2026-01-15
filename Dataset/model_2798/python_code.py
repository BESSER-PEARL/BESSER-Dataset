from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Tree_Node:

    def __init__(self, value: int, Tree_Node: "Tree_Storage" = None, Tree_Node3: "Tree_Node" = None, Tree_Node1: set["Tree_Node"] = None):
        self.value = value
        self.Tree_Node = Tree_Node
        self.Tree_Node3 = Tree_Node3
        self.Tree_Node1 = Tree_Node1 if Tree_Node1 is not None else set()
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def Tree_Node3(self):
        return self.__Tree_Node3

    @Tree_Node3.setter
    def Tree_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tree_Node__Tree_Node3", None)
        self.__Tree_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tree_Node1"):
                opp_val = getattr(old_value, "Tree_Node1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tree_Node1"):
                opp_val = getattr(value, "Tree_Node1", None)
                if opp_val is None:
                    setattr(value, "Tree_Node1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Tree_Node(self):
        return self.__Tree_Node

    @Tree_Node.setter
    def Tree_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tree_Node__Tree_Node", None)
        self.__Tree_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tree_Storage"):
                opp_val = getattr(old_value, "Tree_Storage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tree_Storage"):
                opp_val = getattr(value, "Tree_Storage", None)
                if opp_val is None:
                    setattr(value, "Tree_Storage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Tree_Node1(self):
        return self.__Tree_Node1

    @Tree_Node1.setter
    def Tree_Node1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tree_Node__Tree_Node1", None)
        self.__Tree_Node1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tree_Node3"):
                    opp_val = getattr(item, "Tree_Node3", None)
                    
                    if opp_val == self:
                        setattr(item, "Tree_Node3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tree_Node3"):
                    opp_val = getattr(item, "Tree_Node3", None)
                    
                    setattr(item, "Tree_Node3", self)
                    

class Tree_Storage:

    pass