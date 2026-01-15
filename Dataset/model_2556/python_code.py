from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class HLSTree_HLSNode:

    def __init__(self, hls: str, name: str, HLSNode: "HLSTree_HLSNode" = None, children: "HLSTree_HLSNode" = None, HLSNode4: "HLSTree_HLSNode" = None, parent: set["HLSTree_HLSNode"] = None):
        self.hls = hls
        self.name = name
        self.HLSNode = HLSNode
        self.children = children
        self.HLSNode4 = HLSNode4
        self.parent = parent if parent is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hls(self) -> str:
        return self.__hls

    @hls.setter
    def hls(self, hls: str):
        self.__hls = hls

    @property
    def HLSNode(self):
        return self.__HLSNode

    @HLSNode.setter
    def HLSNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HLSTree_HLSNode__HLSNode", None)
        self.__HLSNode = value
        
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
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HLSTree_HLSNode__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HLSNode"):
                opp_val = getattr(old_value, "HLSNode", None)
                if opp_val == self:
                    setattr(old_value, "HLSNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HLSNode"):
                opp_val = getattr(value, "HLSNode", None)
                setattr(value, "HLSNode", self)

    @property
    def HLSNode4(self):
        return self.__HLSNode4

    @HLSNode4.setter
    def HLSNode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_HLSTree_HLSNode__HLSNode4", None)
        self.__HLSNode4 = value
        
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
        old_value = getattr(self, f"_HLSTree_HLSNode__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HLSNode4"):
                    opp_val = getattr(item, "HLSNode4", None)
                    
                    if opp_val == self:
                        setattr(item, "HLSNode4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HLSNode4"):
                    opp_val = getattr(item, "HLSNode4", None)
                    
                    setattr(item, "HLSNode4", self)
                    
