from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DecisionTree_Property:

    pass
class DecisionTree_DecisionTrees:

    def __init__(self, name: str, DecisionTree_DecisionTrees: set["DecisionTree_DecisionTreeForEntity"] = None):
        self.name = name
        self.DecisionTree_DecisionTrees = DecisionTree_DecisionTrees if DecisionTree_DecisionTrees is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DecisionTree_DecisionTrees(self):
        return self.__DecisionTree_DecisionTrees

    @DecisionTree_DecisionTrees.setter
    def DecisionTree_DecisionTrees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DecisionTree_DecisionTrees__DecisionTree_DecisionTrees", None)
        self.__DecisionTree_DecisionTrees = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DecisionTree_DecisionTreeForEntity12"):
                    opp_val = getattr(item, "DecisionTree_DecisionTreeForEntity12", None)
                    
                    if opp_val == self:
                        setattr(item, "DecisionTree_DecisionTreeForEntity12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DecisionTree_DecisionTreeForEntity12"):
                    opp_val = getattr(item, "DecisionTree_DecisionTreeForEntity12", None)
                    
                    setattr(item, "DecisionTree_DecisionTreeForEntity12", self)
                    

class DecisionTree_EntityType:

    pass
class DecisionTree_DecisionTreeForEntity:

    pass
class DecisionTree_PropertySpec2:

    def __init__(self, needsTypeCheck: bool, DecisionTree_PropertySpec2: "DecisionTree_IntermediateNode" = None, DecisionTree_PropertySpec214: "DecisionTree_Property" = None):
        self.needsTypeCheck = needsTypeCheck
        self.DecisionTree_PropertySpec2 = DecisionTree_PropertySpec2
        self.DecisionTree_PropertySpec214 = DecisionTree_PropertySpec214
        
    @property
    def needsTypeCheck(self) -> bool:
        return self.__needsTypeCheck

    @needsTypeCheck.setter
    def needsTypeCheck(self, needsTypeCheck: bool):
        self.__needsTypeCheck = needsTypeCheck

    @property
    def DecisionTree_PropertySpec214(self):
        return self.__DecisionTree_PropertySpec214

    @DecisionTree_PropertySpec214.setter
    def DecisionTree_PropertySpec214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DecisionTree_PropertySpec2__DecisionTree_PropertySpec214", None)
        self.__DecisionTree_PropertySpec214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DecisionTree_Property"):
                opp_val = getattr(old_value, "DecisionTree_Property", None)
                if opp_val == self:
                    setattr(old_value, "DecisionTree_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DecisionTree_Property"):
                opp_val = getattr(value, "DecisionTree_Property", None)
                setattr(value, "DecisionTree_Property", self)

    @property
    def DecisionTree_PropertySpec2(self):
        return self.__DecisionTree_PropertySpec2

    @DecisionTree_PropertySpec2.setter
    def DecisionTree_PropertySpec2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DecisionTree_PropertySpec2__DecisionTree_PropertySpec2", None)
        self.__DecisionTree_PropertySpec2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DecisionTree_IntermediateNode"):
                opp_val = getattr(old_value, "DecisionTree_IntermediateNode", None)
                if opp_val == self:
                    setattr(old_value, "DecisionTree_IntermediateNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DecisionTree_IntermediateNode"):
                opp_val = getattr(value, "DecisionTree_IntermediateNode", None)
                setattr(value, "DecisionTree_IntermediateNode", self)

class DecisionTree_StructuralVariation:

    pass
class DecisionTreeNode:

    pass
class DecisionTree_IntermediateNode(DecisionTreeNode):

    pass
class DecisionTree_LeafNode(DecisionTreeNode):

    pass
class DecisionTree_DecisionTreeNode(ABC):

    pass