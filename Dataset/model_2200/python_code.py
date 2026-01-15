from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tree_Node:

    def __init__(self, data: str, label: str, tree_Node: "tree_Tree" = None, tree_Node3: "tree_Node" = None, tree_Node1: set["tree_Node"] = None):
        self.data = data
        self.label = label
        self.tree_Node = tree_Node
        self.tree_Node3 = tree_Node3
        self.tree_Node1 = tree_Node1 if tree_Node1 is not None else set()
        
    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def tree_Node3(self):
        return self.__tree_Node3

    @tree_Node3.setter
    def tree_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__tree_Node3", None)
        self.__tree_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_Node1"):
                opp_val = getattr(old_value, "tree_Node1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_Node1"):
                opp_val = getattr(value, "tree_Node1", None)
                if opp_val is None:
                    setattr(value, "tree_Node1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tree_Node(self):
        return self.__tree_Node

    @tree_Node.setter
    def tree_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__tree_Node", None)
        self.__tree_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_Tree"):
                opp_val = getattr(old_value, "tree_Tree", None)
                if opp_val == self:
                    setattr(old_value, "tree_Tree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_Tree"):
                opp_val = getattr(value, "tree_Tree", None)
                setattr(value, "tree_Tree", self)

    @property
    def tree_Node1(self):
        return self.__tree_Node1

    @tree_Node1.setter
    def tree_Node1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__tree_Node1", None)
        self.__tree_Node1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tree_Node3"):
                    opp_val = getattr(item, "tree_Node3", None)
                    
                    if opp_val == self:
                        setattr(item, "tree_Node3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tree_Node3"):
                    opp_val = getattr(item, "tree_Node3", None)
                    
                    setattr(item, "tree_Node3", self)
                    

class tree_Tree:

    def __init__(self, name: str, tree_Tree: "tree_Node" = None):
        self.name = name
        self.tree_Tree = tree_Tree
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tree_Tree(self):
        return self.__tree_Tree

    @tree_Tree.setter
    def tree_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Tree__tree_Tree", None)
        self.__tree_Tree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_Node"):
                opp_val = getattr(old_value, "tree_Node", None)
                if opp_val == self:
                    setattr(old_value, "tree_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_Node"):
                opp_val = getattr(value, "tree_Node", None)
                setattr(value, "tree_Node", self)
