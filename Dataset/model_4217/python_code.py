from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class talltree_TallNode:

    def __init__(self, height: int, name: str, TallNode: "talltree_TallNode" = None, parent: set["talltree_TallNode"] = None, TallNode4: "talltree_TallNode" = None, children: "talltree_TallNode" = None):
        self.height = height
        self.name = name
        self.TallNode = TallNode
        self.parent = parent if parent is not None else set()
        self.TallNode4 = TallNode4
        self.children = children
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_talltree_TallNode__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TallNode4"):
                opp_val = getattr(old_value, "TallNode4", None)
                if opp_val == self:
                    setattr(old_value, "TallNode4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TallNode4"):
                opp_val = getattr(value, "TallNode4", None)
                setattr(value, "TallNode4", self)

    @property
    def TallNode4(self):
        return self.__TallNode4

    @TallNode4.setter
    def TallNode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_talltree_TallNode__TallNode4", None)
        self.__TallNode4 = value
        
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
    def TallNode(self):
        return self.__TallNode

    @TallNode.setter
    def TallNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_talltree_TallNode__TallNode", None)
        self.__TallNode = value
        
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
        old_value = getattr(self, f"_talltree_TallNode__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TallNode"):
                    opp_val = getattr(item, "TallNode", None)
                    
                    if opp_val == self:
                        setattr(item, "TallNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TallNode"):
                    opp_val = getattr(item, "TallNode", None)
                    
                    setattr(item, "TallNode", self)
                    
