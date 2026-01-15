from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class HSV2HLS_HSVNode:

    pass
class HSV2HLS_HLSNode:

    pass
class HSV2HLS_HSVNode2HLSNode:

    def __init__(self, rgb: str, name: str, HSV2HLS_HSVNode2HLSNode7: "HSV2HLS_HLSNode" = None, HSVNode2HLSNode: "HSV2HLS_HSVNode2HLSNode" = None, children: "HSV2HLS_HSVNode2HLSNode" = None, HSVNode2HLSNode4: "HSV2HLS_HSVNode2HLSNode" = None, parent: set["HSV2HLS_HSVNode2HLSNode"] = None, HSV2HLS_HSVNode2HLSNode: "HSV2HLS_HSVNode" = None):
        self.rgb = rgb
        self.name = name
        self.HSV2HLS_HSVNode2HLSNode7 = HSV2HLS_HSVNode2HLSNode7
        self.HSVNode2HLSNode = HSVNode2HLSNode
        self.children = children
        self.HSVNode2HLSNode4 = HSVNode2HLSNode4
        self.parent = parent if parent is not None else set()
        self.HSV2HLS_HSVNode2HLSNode = HSV2HLS_HSVNode2HLSNode
        
    @property
    def rgb(self) -> str:
        return self.__rgb

    @rgb.setter
    def rgb(self, rgb: str):
        self.__rgb = rgb

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
        old_value = getattr(self, f"_HSV2HLS_HSVNode2HLSNode__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSVNode2HLSNode"):
                opp_val = getattr(old_value, "HSVNode2HLSNode", None)
                if opp_val == self:
                    setattr(old_value, "HSVNode2HLSNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSVNode2HLSNode"):
                opp_val = getattr(value, "HSVNode2HLSNode", None)
                setattr(value, "HSVNode2HLSNode", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSV2HLS_HSVNode2HLSNode__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HSVNode2HLSNode4"):
                    opp_val = getattr(item, "HSVNode2HLSNode4", None)
                    
                    if opp_val == self:
                        setattr(item, "HSVNode2HLSNode4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HSVNode2HLSNode4"):
                    opp_val = getattr(item, "HSVNode2HLSNode4", None)
                    
                    setattr(item, "HSVNode2HLSNode4", self)
                    

    @property
    def HSV2HLS_HSVNode2HLSNode(self):
        return self.__HSV2HLS_HSVNode2HLSNode

    @HSV2HLS_HSVNode2HLSNode.setter
    def HSV2HLS_HSVNode2HLSNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSV2HLS_HSVNode2HLSNode__HSV2HLS_HSVNode2HLSNode", None)
        self.__HSV2HLS_HSVNode2HLSNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSV2HLS_HSVNode"):
                opp_val = getattr(old_value, "HSV2HLS_HSVNode", None)
                if opp_val == self:
                    setattr(old_value, "HSV2HLS_HSVNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSV2HLS_HSVNode"):
                opp_val = getattr(value, "HSV2HLS_HSVNode", None)
                setattr(value, "HSV2HLS_HSVNode", self)

    @property
    def HSVNode2HLSNode(self):
        return self.__HSVNode2HLSNode

    @HSVNode2HLSNode.setter
    def HSVNode2HLSNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSV2HLS_HSVNode2HLSNode__HSVNode2HLSNode", None)
        self.__HSVNode2HLSNode = value
        
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
    def HSV2HLS_HSVNode2HLSNode7(self):
        return self.__HSV2HLS_HSVNode2HLSNode7

    @HSV2HLS_HSVNode2HLSNode7.setter
    def HSV2HLS_HSVNode2HLSNode7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSV2HLS_HSVNode2HLSNode__HSV2HLS_HSVNode2HLSNode7", None)
        self.__HSV2HLS_HSVNode2HLSNode7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HSV2HLS_HLSNode"):
                opp_val = getattr(old_value, "HSV2HLS_HLSNode", None)
                if opp_val == self:
                    setattr(old_value, "HSV2HLS_HLSNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HSV2HLS_HLSNode"):
                opp_val = getattr(value, "HSV2HLS_HLSNode", None)
                setattr(value, "HSV2HLS_HLSNode", self)

    @property
    def HSVNode2HLSNode4(self):
        return self.__HSVNode2HLSNode4

    @HSVNode2HLSNode4.setter
    def HSVNode2HLSNode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HSV2HLS_HSVNode2HLSNode__HSVNode2HLSNode4", None)
        self.__HSVNode2HLSNode4 = value
        
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
