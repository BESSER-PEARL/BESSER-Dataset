from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tree2talltree_TallNode:

    pass
class tree2talltree_Node:

    pass
class tree2talltree_Node2TallNode:

    def __init__(self, name: str, Node2TallNode: "tree2talltree_Node2TallNode" = None, parent: set["tree2talltree_Node2TallNode"] = None, Node2TallNode4: "tree2talltree_Node2TallNode" = None, children: "tree2talltree_Node2TallNode" = None, tree2talltree_Node2TallNode: "tree2talltree_Node" = None, tree2talltree_Node2TallNode7: "tree2talltree_TallNode" = None):
        self.name = name
        self.Node2TallNode = Node2TallNode
        self.parent = parent if parent is not None else set()
        self.Node2TallNode4 = Node2TallNode4
        self.children = children
        self.tree2talltree_Node2TallNode = tree2talltree_Node2TallNode
        self.tree2talltree_Node2TallNode7 = tree2talltree_Node2TallNode7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tree2talltree_Node2TallNode7(self):
        return self.__tree2talltree_Node2TallNode7

    @tree2talltree_Node2TallNode7.setter
    def tree2talltree_Node2TallNode7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree2talltree_Node2TallNode__tree2talltree_Node2TallNode7", None)
        self.__tree2talltree_Node2TallNode7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree2talltree_TallNode"):
                opp_val = getattr(old_value, "tree2talltree_TallNode", None)
                if opp_val == self:
                    setattr(old_value, "tree2talltree_TallNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree2talltree_TallNode"):
                opp_val = getattr(value, "tree2talltree_TallNode", None)
                setattr(value, "tree2talltree_TallNode", self)

    @property
    def tree2talltree_Node2TallNode(self):
        return self.__tree2talltree_Node2TallNode

    @tree2talltree_Node2TallNode.setter
    def tree2talltree_Node2TallNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree2talltree_Node2TallNode__tree2talltree_Node2TallNode", None)
        self.__tree2talltree_Node2TallNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree2talltree_Node"):
                opp_val = getattr(old_value, "tree2talltree_Node", None)
                if opp_val == self:
                    setattr(old_value, "tree2talltree_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree2talltree_Node"):
                opp_val = getattr(value, "tree2talltree_Node", None)
                setattr(value, "tree2talltree_Node", self)

    @property
    def Node2TallNode4(self):
        return self.__Node2TallNode4

    @Node2TallNode4.setter
    def Node2TallNode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree2talltree_Node2TallNode__Node2TallNode4", None)
        self.__Node2TallNode4 = value
        
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
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree2talltree_Node2TallNode__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node2TallNode"):
                    opp_val = getattr(item, "Node2TallNode", None)
                    
                    if opp_val == self:
                        setattr(item, "Node2TallNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node2TallNode"):
                    opp_val = getattr(item, "Node2TallNode", None)
                    
                    setattr(item, "Node2TallNode", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree2talltree_Node2TallNode__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node2TallNode4"):
                opp_val = getattr(old_value, "Node2TallNode4", None)
                if opp_val == self:
                    setattr(old_value, "Node2TallNode4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node2TallNode4"):
                opp_val = getattr(value, "Node2TallNode4", None)
                setattr(value, "Node2TallNode4", self)

    @property
    def Node2TallNode(self):
        return self.__Node2TallNode

    @Node2TallNode.setter
    def Node2TallNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree2talltree_Node2TallNode__Node2TallNode", None)
        self.__Node2TallNode = value
        
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
