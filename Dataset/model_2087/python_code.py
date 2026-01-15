from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tree_Node:

    def __init__(self, anAttribute: int, anAttribute2: int, anAttribute3: int, name: str, anAttribute4: int, Node5: "tree_Node" = None, child: "tree_Node" = None, tree_Node: "tree_Tree" = None, Node: "tree_Node" = None, parent: set["tree_Node"] = None, tree_Node8: "tree_Node" = None, tree_Node6: set["tree_Node"] = None):
        self.anAttribute = anAttribute
        self.anAttribute2 = anAttribute2
        self.anAttribute3 = anAttribute3
        self.name = name
        self.anAttribute4 = anAttribute4
        self.Node5 = Node5
        self.child = child
        self.tree_Node = tree_Node
        self.Node = Node
        self.parent = parent if parent is not None else set()
        self.tree_Node8 = tree_Node8
        self.tree_Node6 = tree_Node6 if tree_Node6 is not None else set()
        
    @property
    def anAttribute3(self) -> int:
        return self.__anAttribute3

    @anAttribute3.setter
    def anAttribute3(self, anAttribute3: int):
        self.__anAttribute3 = anAttribute3

    @property
    def anAttribute(self) -> int:
        return self.__anAttribute

    @anAttribute.setter
    def anAttribute(self, anAttribute: int):
        self.__anAttribute = anAttribute

    @property
    def anAttribute2(self) -> int:
        return self.__anAttribute2

    @anAttribute2.setter
    def anAttribute2(self, anAttribute2: int):
        self.__anAttribute2 = anAttribute2

    @property
    def anAttribute4(self) -> int:
        return self.__anAttribute4

    @anAttribute4.setter
    def anAttribute4(self, anAttribute4: int):
        self.__anAttribute4 = anAttribute4

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "tree_Node8"):
                    opp_val = getattr(item, "tree_Node8", None)
                    
                    if opp_val == self:
                        setattr(item, "tree_Node8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tree_Node8"):
                    opp_val = getattr(item, "tree_Node8", None)
                    
                    setattr(item, "tree_Node8", self)
                    

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
    def tree_Node8(self):
        return self.__tree_Node8

    @tree_Node8.setter
    def tree_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__tree_Node8", None)
        self.__tree_Node8 = value
        
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
    def Node5(self):
        return self.__Node5

    @Node5.setter
    def Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__Node5", None)
        self.__Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "child"):
                opp_val = getattr(old_value, "child", None)
                if opp_val == self:
                    setattr(old_value, "child", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "child"):
                opp_val = getattr(value, "child", None)
                setattr(value, "child", self)

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
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_Node__child", None)
        self.__child = value
        
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
