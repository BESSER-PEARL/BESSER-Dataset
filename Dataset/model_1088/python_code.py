from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Element:

    pass
class petriNet_Node(Element):

    pass
class petriNet_Arc(Element):

    pass
class Node:

    pass
class petriNet_Transition(Node):

    pass
class petriNet_Place(Node):

    def __init__(self, noTokens: int, petriNet_Place: "petriNet_Transition" = None):
        self.noTokens = noTokens
        self.petriNet_Place = petriNet_Place
        
    @property
    def noTokens(self) -> int:
        return self.__noTokens

    @noTokens.setter
    def noTokens(self, noTokens: int):
        self.__noTokens = noTokens

    @property
    def petriNet_Place(self):
        return self.__petriNet_Place

    @petriNet_Place.setter
    def petriNet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Place__petriNet_Place", None)
        self.__petriNet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Transition"):
                opp_val = getattr(old_value, "petriNet_Transition", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Transition"):
                opp_val = getattr(value, "petriNet_Transition", None)
                setattr(value, "petriNet_Transition", self)

class petriNet_Element(ABC):

    pass
class petriNet_PetriNet:

    def __init__(self, diagramName: str, diagram: set["petriNet_Element"] = None, PetriNet: "petriNet_Element" = None):
        self.diagramName = diagramName
        self.diagram = diagram if diagram is not None else set()
        self.PetriNet = PetriNet
        
    @property
    def diagramName(self) -> str:
        return self.__diagramName

    @diagramName.setter
    def diagramName(self, diagramName: str):
        self.__diagramName = diagramName

    @property
    def diagram(self):
        return self.__diagram

    @diagram.setter
    def diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_PetriNet__diagram", None)
        self.__diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

    @property
    def PetriNet(self):
        return self.__PetriNet

    @PetriNet.setter
    def PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_PetriNet__PetriNet", None)
        self.__PetriNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements"):
                opp_val = getattr(old_value, "elements", None)
                if opp_val == self:
                    setattr(old_value, "elements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements"):
                opp_val = getattr(value, "elements", None)
                setattr(value, "elements", self)
