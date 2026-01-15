from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Node:

    pass
class Tree_Tree(Node):

    pass
class Tree_Node:

    def __init__(self, id: str, Node: "Tree_Node" = None, parent: set["Tree_Node"] = None, Node4: "Tree_Node" = None, childs: "Tree_Node" = None):
        self.id = id
        self.Node = Node
        self.parent = parent if parent is not None else set()
        self.Node4 = Node4
        self.childs = childs
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tree_Node__Node", None)
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
    def Node4(self):
        return self.__Node4

    @Node4.setter
    def Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tree_Node__Node4", None)
        self.__Node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childs"):
                opp_val = getattr(old_value, "childs", None)
                if opp_val == self:
                    setattr(old_value, "childs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childs"):
                opp_val = getattr(value, "childs", None)
                setattr(value, "childs", self)

    @property
    def childs(self):
        return self.__childs

    @childs.setter
    def childs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tree_Node__childs", None)
        self.__childs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node4"):
                opp_val = getattr(old_value, "Node4", None)
                if opp_val == self:
                    setattr(old_value, "Node4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node4"):
                opp_val = getattr(value, "Node4", None)
                setattr(value, "Node4", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tree_Node__parent", None)
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
                    
