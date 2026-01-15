from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Node:

    pass
class CST_TNode(Node):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class CST_RNode(Node):

    pass
class CST_Node:

    def __init__(self, kind: str, CST_Node: "CST_Tree" = None, Node: "CST_Node" = None, parent: set["CST_Node"] = None, Node5: "CST_Node" = None, children: "CST_Node" = None):
        self.kind = kind
        self.CST_Node = CST_Node
        self.Node = Node
        self.parent = parent if parent is not None else set()
        self.Node5 = Node5
        self.children = children
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def CST_Node(self):
        return self.__CST_Node

    @CST_Node.setter
    def CST_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CST_Node__CST_Node", None)
        self.__CST_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CST_Tree"):
                opp_val = getattr(old_value, "CST_Tree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CST_Tree"):
                opp_val = getattr(value, "CST_Tree", None)
                if opp_val is None:
                    setattr(value, "CST_Tree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CST_Node__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node5"):
                opp_val = getattr(old_value, "Node5", None)
                if opp_val == self:
                    setattr(old_value, "Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node5"):
                opp_val = getattr(value, "Node5", None)
                setattr(value, "Node5", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CST_Node__Node", None)
        self.__Node = value
        
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
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CST_Node__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

    @property
    def Node5(self):
        return self.__Node5

    @Node5.setter
    def Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CST_Node__Node5", None)
        self.__Node5 = value
        
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

class CST_Tree:

    pass