from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class MMA_Element(ABC):

    def __init__(self, name: str, sources: set["Element"] = None, targets: set["Element"] = None, children: "Root" = None):
        self.name = name
        self.sources = sources if sources is not None else set()
        self.targets = targets if targets is not None else set()
        self.children = children
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sources(self):
        return self.__sources

    @sources.setter
    def sources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMA_Element__sources", None)
        self.__sources = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element2"):
                    opp_val = getattr(item, "Element2", None)
                    
                    if opp_val == self:
                        setattr(item, "Element2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element2"):
                    opp_val = getattr(item, "Element2", None)
                    
                    setattr(item, "Element2", self)
                    

    @property
    def targets(self):
        return self.__targets

    @targets.setter
    def targets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMA_Element__targets", None)
        self.__targets = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element4"):
                    opp_val = getattr(item, "Element4", None)
                    
                    if opp_val == self:
                        setattr(item, "Element4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element4"):
                    opp_val = getattr(item, "Element4", None)
                    
                    setattr(item, "Element4", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMA_Element__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Root"):
                opp_val = getattr(old_value, "Root", None)
                if opp_val == self:
                    setattr(old_value, "Root", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Root"):
                opp_val = getattr(value, "Root", None)
                setattr(value, "Root", self)

class Element:

    pass
class MMA_Root:

    pass
class MMA_B(Element):

    pass
class MMA_A(Element):

    pass
class Root:

    pass