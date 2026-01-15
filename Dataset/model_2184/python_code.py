from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TreeDsl_Tree:

    def __init__(self, label: str, Tree: "TreeDsl_Tree" = None, parent: set["TreeDsl_Tree"] = None, Tree4: "TreeDsl_Tree" = None, children: "TreeDsl_Tree" = None):
        self.label = label
        self.Tree = Tree
        self.parent = parent if parent is not None else set()
        self.Tree4 = Tree4
        self.children = children
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeDsl_Tree__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tree4"):
                opp_val = getattr(old_value, "Tree4", None)
                if opp_val == self:
                    setattr(old_value, "Tree4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tree4"):
                opp_val = getattr(value, "Tree4", None)
                setattr(value, "Tree4", self)

    @property
    def Tree(self):
        return self.__Tree

    @Tree.setter
    def Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeDsl_Tree__Tree", None)
        self.__Tree = value
        
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
        old_value = getattr(self, f"_TreeDsl_Tree__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tree"):
                    opp_val = getattr(item, "Tree", None)
                    
                    if opp_val == self:
                        setattr(item, "Tree", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tree"):
                    opp_val = getattr(item, "Tree", None)
                    
                    setattr(item, "Tree", self)
                    

    @property
    def Tree4(self):
        return self.__Tree4

    @Tree4.setter
    def Tree4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeDsl_Tree__Tree4", None)
        self.__Tree4 = value
        
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
