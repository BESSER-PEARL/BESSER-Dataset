from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tree_Data:

    def __init__(self, name: str, Data: "tree_Node" = None, data: "tree_Node" = None):
        self.name = name
        self.Data = Data
        self.data = data
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Data(self):
        return self.__Data

    @Data.setter
    def Data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Data__Data", None)
        self.__Data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if opp_val == self:
                    setattr(old_value, "node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                setattr(value, "node", self)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Data__data", None)
        self.__data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node9"):
                opp_val = getattr(old_value, "Node9", None)
                if opp_val == self:
                    setattr(old_value, "Node9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node9"):
                opp_val = getattr(value, "Node9", None)
                setattr(value, "Node9", self)

class tree_Node:

    def __init__(self, name: str, Node: "tree_Node" = None, children: "tree_Node" = None, Node4: "tree_Node" = None, parent: set["tree_Node"] = None, node: "tree_Data" = None, tree_Node6: set["tree_Node"] = None, Node9: "tree_Data" = None, tree_Node: "tree_Node" = None):
        self.name = name
        self.Node = Node
        self.children = children
        self.Node4 = Node4
        self.parent = parent if parent is not None else set()
        self.node = node
        self.tree_Node6 = tree_Node6 if tree_Node6 is not None else set()
        self.Node9 = Node9
        self.tree_Node = tree_Node
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Node9(self):
        return self.__Node9

    @Node9.setter
    def Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__Node9", None)
        self.__Node9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data"):
                opp_val = getattr(old_value, "data", None)
                if opp_val == self:
                    setattr(old_value, "data", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data"):
                opp_val = getattr(value, "data", None)
                setattr(value, "data", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node4"):
                    opp_val = getattr(item, "Node4", None)
                    
                    if opp_val == self:
                        setattr(item, "Node4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node4"):
                    opp_val = getattr(item, "Node4", None)
                    
                    setattr(item, "Node4", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

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
            if hasattr(old_value, "tree_Node6"):
                opp_val = getattr(old_value, "tree_Node6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_Node6"):
                opp_val = getattr(value, "tree_Node6", None)
                if opp_val is None:
                    setattr(value, "tree_Node6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tree_Node6(self):
        return self.__tree_Node6

    @tree_Node6.setter
    def tree_Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__tree_Node6", None)
        self.__tree_Node6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tree_Node"):
                    opp_val = getattr(item, "tree_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "tree_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tree_Node"):
                    opp_val = getattr(item, "tree_Node", None)
                    
                    setattr(item, "tree_Node", self)
                    

    @property
    def Node4(self):
        return self.__Node4

    @Node4.setter
    def Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__Node4", None)
        self.__Node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__node", None)
        self.__node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data"):
                opp_val = getattr(old_value, "Data", None)
                if opp_val == self:
                    setattr(old_value, "Data", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data"):
                opp_val = getattr(value, "Data", None)
                setattr(value, "Data", self)
