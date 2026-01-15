from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class HSVTree_HSVNode:

    def __init__(self, hsv: str, name: str, HSVNode: "HSVTree_HSVNode" = None, children: "HSVTree_HSVNode" = None, HSVNode4: "HSVTree_HSVNode" = None, parent: set["HSVTree_HSVNode"] = None):
        self.hsv = hsv
        self.name = name
        self.HSVNode = HSVNode
        self.children = children
        self.HSVNode4 = HSVNode4
        self.parent = parent if parent is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hsv(self) -> str:
        return self.__hsv

    @hsv.setter
    def hsv(self, hsv: str):
        self.__hsv = hsv

    @property
    def HSVNode(self):
        return self.__HSVNode

    @HSVNode.setter
    def HSVNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSVTree_HSVNode__HSVNode", None)
        self.__HSVNode = value
        
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
    def HSVNode4(self):
        return self.__HSVNode4

    @HSVNode4.setter
    def HSVNode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSVTree_HSVNode__HSVNode4", None)
        self.__HSVNode4 = value
        
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
        old_value = getattr(self, f"_HSVTree_HSVNode__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HSVNode4"):
                    opp_val = getattr(item, "HSVNode4", None)
                    
                    if opp_val == self:
                        setattr(item, "HSVNode4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HSVNode4"):
                    opp_val = getattr(item, "HSVNode4", None)
                    
                    setattr(item, "HSVNode4", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSVTree_HSVNode__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSVNode"):
                opp_val = getattr(old_value, "HSVNode", None)
                if opp_val == self:
                    setattr(old_value, "HSVNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSVNode"):
                opp_val = getattr(value, "HSVNode", None)
                setattr(value, "HSVNode", self)
