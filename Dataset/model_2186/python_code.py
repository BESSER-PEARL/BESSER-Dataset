from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    red = "red"
    green = "green"
    blue = "blue"


############################################
# Definition of Classes
############################################

class coloredTree_HueTree:

    def __init__(self, label: str, color: str, HueTree: "coloredTree_HueTree" = None, parent: set["coloredTree_HueTree"] = None, HueTree4: "coloredTree_HueTree" = None, children: "coloredTree_HueTree" = None):
        self.label = label
        self.color = color
        self.HueTree = HueTree
        self.parent = parent if parent is not None else set()
        self.HueTree4 = HueTree4
        self.children = children
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def HueTree4(self):
        return self.__HueTree4

    @HueTree4.setter
    def HueTree4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coloredTree_HueTree__HueTree4", None)
        self.__HueTree4 = value
        
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
        old_value = getattr(self, f"_coloredTree_HueTree__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "HueTree4"):
                opp_val = getattr(old_value, "HueTree4", None)
                if opp_val == self:
                    setattr(old_value, "HueTree4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "HueTree4"):
                opp_val = getattr(value, "HueTree4", None)
                setattr(value, "HueTree4", self)

    @property
    def HueTree(self):
        return self.__HueTree

    @HueTree.setter
    def HueTree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coloredTree_HueTree__HueTree", None)
        self.__HueTree = value
        
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
        old_value = getattr(self, f"_coloredTree_HueTree__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "HueTree"):
                    opp_val = getattr(item, "HueTree", None)
                    
                    if opp_val == self:
                        setattr(item, "HueTree", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "HueTree"):
                    opp_val = getattr(item, "HueTree", None)
                    
                    setattr(item, "HueTree", self)
                    
