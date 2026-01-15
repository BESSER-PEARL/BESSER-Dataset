from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dgf_DTypedElement(ABC):

    pass
class dgf_Graph:

    pass
class DContainedVertex:

    pass
class DContainedElement:

    pass
class DTypedElement:

    pass
class dgf_DLink(DContainedVertex, DTypedElement):

    pass
class dgf_DContainment(DContainedVertex):

    def __init__(self, compartment: str):
        self.compartment = compartment
        
    @property
    def compartment(self) -> str:
        return self.__compartment

    @compartment.setter
    def compartment(self, compartment: str):
        self.__compartment = compartment

class DVertex:

    pass
class dgf_DContainedVertex(DVertex, DContainedElement):

    pass
class dgf_DReference(DVertex):

    def __init__(self, property: bool):
        self.property = property
        
    @property
    def property(self) -> bool:
        return self.__property

    @property.setter
    def property(self, property: bool):
        self.__property = property

class DGraphElement:

    pass
class dgf_DContainedElement(DGraphElement):

    pass
class dgf_DVertex(DGraphElement):

    pass
class dgf_DGraphElement(ABC):

    def __init__(self, name: str, dgf_DGraphElement: "dgf_Graph" = None):
        self.name = name
        self.dgf_DGraphElement = dgf_DGraphElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dgf_DGraphElement(self):
        return self.__dgf_DGraphElement

    @dgf_DGraphElement.setter
    def dgf_DGraphElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dgf_DGraphElement__dgf_DGraphElement", None)
        self.__dgf_DGraphElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dgf_Graph"):
                opp_val = getattr(old_value, "dgf_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dgf_Graph"):
                opp_val = getattr(value, "dgf_Graph", None)
                if opp_val is None:
                    setattr(value, "dgf_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dgf_DNode(DGraphElement, DTypedElement, DContainedElement):

    def __init__(self, pointOfView: str, dgf_DNode: "dgf_DVertex" = None, dgf_DNode3: "dgf_DVertex" = None, dgf_DNode5: set["dgf_DVertex"] = None, dgf_DNode9: "dgf_DContainedElement" = None):
        self.pointOfView = pointOfView
        self.dgf_DNode = dgf_DNode
        self.dgf_DNode3 = dgf_DNode3
        self.dgf_DNode5 = dgf_DNode5 if dgf_DNode5 is not None else set()
        self.dgf_DNode9 = dgf_DNode9
        
    @property
    def pointOfView(self) -> str:
        return self.__pointOfView

    @pointOfView.setter
    def pointOfView(self, pointOfView: str):
        self.__pointOfView = pointOfView

    @property
    def dgf_DNode9(self):
        return self.__dgf_DNode9

    @dgf_DNode9.setter
    def dgf_DNode9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dgf_DNode__dgf_DNode9", None)
        self.__dgf_DNode9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dgf_DContainedElement"):
                opp_val = getattr(old_value, "dgf_DContainedElement", None)
                if opp_val == self:
                    setattr(old_value, "dgf_DContainedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dgf_DContainedElement"):
                opp_val = getattr(value, "dgf_DContainedElement", None)
                setattr(value, "dgf_DContainedElement", self)

    @property
    def dgf_DNode5(self):
        return self.__dgf_DNode5

    @dgf_DNode5.setter
    def dgf_DNode5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dgf_DNode__dgf_DNode5", None)
        self.__dgf_DNode5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dgf_DVertex6"):
                    opp_val = getattr(item, "dgf_DVertex6", None)
                    
                    if opp_val == self:
                        setattr(item, "dgf_DVertex6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dgf_DVertex6"):
                    opp_val = getattr(item, "dgf_DVertex6", None)
                    
                    setattr(item, "dgf_DVertex6", self)
                    

    @property
    def dgf_DNode(self):
        return self.__dgf_DNode

    @dgf_DNode.setter
    def dgf_DNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dgf_DNode__dgf_DNode", None)
        self.__dgf_DNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dgf_DVertex"):
                opp_val = getattr(old_value, "dgf_DVertex", None)
                if opp_val == self:
                    setattr(old_value, "dgf_DVertex", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dgf_DVertex"):
                opp_val = getattr(value, "dgf_DVertex", None)
                setattr(value, "dgf_DVertex", self)

    @property
    def dgf_DNode3(self):
        return self.__dgf_DNode3

    @dgf_DNode3.setter
    def dgf_DNode3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dgf_DNode__dgf_DNode3", None)
        self.__dgf_DNode3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dgf_DVertex2"):
                opp_val = getattr(old_value, "dgf_DVertex2", None)
                if opp_val == self:
                    setattr(old_value, "dgf_DVertex2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dgf_DVertex2"):
                opp_val = getattr(value, "dgf_DVertex2", None)
                setattr(value, "dgf_DVertex2", self)
