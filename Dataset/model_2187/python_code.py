from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TreeMapType(Enum):
    Ordred = "Ordred"
    Quantum = "Quantum"
    Linear = "Linear"


############################################
# Definition of Classes
############################################

class TreeMapItem:

    pass
class TreeMapViewer_TreeMapContainer(TreeMapItem):

    pass
class TreeMapViewer_TreeMapItem:

    def __init__(self, label: str, value: float, TreeMapViewer_TreeMapItem: "TreeMapViewer_TreeMapViewer" = None, TreeMapViewer_TreeMapItem2: "TreeMapViewer_TreeMapViewer" = None, TreeMapViewer_TreeMapItem5: "TreeMapViewer_TreeMapContainer" = None):
        self.label = label
        self.value = value
        self.TreeMapViewer_TreeMapItem = TreeMapViewer_TreeMapItem
        self.TreeMapViewer_TreeMapItem2 = TreeMapViewer_TreeMapItem2
        self.TreeMapViewer_TreeMapItem5 = TreeMapViewer_TreeMapItem5
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def TreeMapViewer_TreeMapItem(self):
        return self.__TreeMapViewer_TreeMapItem

    @TreeMapViewer_TreeMapItem.setter
    def TreeMapViewer_TreeMapItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeMapViewer_TreeMapItem__TreeMapViewer_TreeMapItem", None)
        self.__TreeMapViewer_TreeMapItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeMapViewer_TreeMapViewer"):
                opp_val = getattr(old_value, "TreeMapViewer_TreeMapViewer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeMapViewer_TreeMapViewer"):
                opp_val = getattr(value, "TreeMapViewer_TreeMapViewer", None)
                if opp_val is None:
                    setattr(value, "TreeMapViewer_TreeMapViewer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TreeMapViewer_TreeMapItem5(self):
        return self.__TreeMapViewer_TreeMapItem5

    @TreeMapViewer_TreeMapItem5.setter
    def TreeMapViewer_TreeMapItem5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeMapViewer_TreeMapItem__TreeMapViewer_TreeMapItem5", None)
        self.__TreeMapViewer_TreeMapItem5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeMapViewer_TreeMapContainer"):
                opp_val = getattr(old_value, "TreeMapViewer_TreeMapContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeMapViewer_TreeMapContainer"):
                opp_val = getattr(value, "TreeMapViewer_TreeMapContainer", None)
                if opp_val is None:
                    setattr(value, "TreeMapViewer_TreeMapContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TreeMapViewer_TreeMapItem2(self):
        return self.__TreeMapViewer_TreeMapItem2

    @TreeMapViewer_TreeMapItem2.setter
    def TreeMapViewer_TreeMapItem2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeMapViewer_TreeMapItem__TreeMapViewer_TreeMapItem2", None)
        self.__TreeMapViewer_TreeMapItem2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeMapViewer_TreeMapViewer3"):
                opp_val = getattr(old_value, "TreeMapViewer_TreeMapViewer3", None)
                if opp_val == self:
                    setattr(old_value, "TreeMapViewer_TreeMapViewer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeMapViewer_TreeMapViewer3"):
                opp_val = getattr(value, "TreeMapViewer_TreeMapViewer3", None)
                setattr(value, "TreeMapViewer_TreeMapViewer3", self)

class TreeMapViewer_TreeMapViewer:

    def __init__(self, childLayoutStrategy: str, TreeMapViewer_TreeMapViewer: set["TreeMapViewer_TreeMapItem"] = None, TreeMapViewer_TreeMapViewer3: "TreeMapViewer_TreeMapItem" = None):
        self.childLayoutStrategy = childLayoutStrategy
        self.TreeMapViewer_TreeMapViewer = TreeMapViewer_TreeMapViewer if TreeMapViewer_TreeMapViewer is not None else set()
        self.TreeMapViewer_TreeMapViewer3 = TreeMapViewer_TreeMapViewer3
        
    @property
    def childLayoutStrategy(self) -> str:
        return self.__childLayoutStrategy

    @childLayoutStrategy.setter
    def childLayoutStrategy(self, childLayoutStrategy: str):
        self.__childLayoutStrategy = childLayoutStrategy

    @property
    def TreeMapViewer_TreeMapViewer3(self):
        return self.__TreeMapViewer_TreeMapViewer3

    @TreeMapViewer_TreeMapViewer3.setter
    def TreeMapViewer_TreeMapViewer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeMapViewer_TreeMapViewer__TreeMapViewer_TreeMapViewer3", None)
        self.__TreeMapViewer_TreeMapViewer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeMapViewer_TreeMapItem2"):
                opp_val = getattr(old_value, "TreeMapViewer_TreeMapItem2", None)
                if opp_val == self:
                    setattr(old_value, "TreeMapViewer_TreeMapItem2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeMapViewer_TreeMapItem2"):
                opp_val = getattr(value, "TreeMapViewer_TreeMapItem2", None)
                setattr(value, "TreeMapViewer_TreeMapItem2", self)

    @property
    def TreeMapViewer_TreeMapViewer(self):
        return self.__TreeMapViewer_TreeMapViewer

    @TreeMapViewer_TreeMapViewer.setter
    def TreeMapViewer_TreeMapViewer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreeMapViewer_TreeMapViewer__TreeMapViewer_TreeMapViewer", None)
        self.__TreeMapViewer_TreeMapViewer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreeMapViewer_TreeMapItem"):
                    opp_val = getattr(item, "TreeMapViewer_TreeMapItem", None)
                    
                    if opp_val == self:
                        setattr(item, "TreeMapViewer_TreeMapItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreeMapViewer_TreeMapItem"):
                    opp_val = getattr(item, "TreeMapViewer_TreeMapItem", None)
                    
                    setattr(item, "TreeMapViewer_TreeMapItem", self)
                    
