from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class petrinet_Transition(Node):

    pass
class petrinet_Place(Node):

    def __init__(self, nbJetons: int):
        self.nbJetons = nbJetons
        
    @property
    def nbJetons(self) -> int:
        return self.__nbJetons

    @nbJetons.setter
    def nbJetons(self, nbJetons: int):
        self.__nbJetons = nbJetons

class petrinet_Arc:

    def __init__(self, poids: int, readArc: bool, petrinet_Arc: "petrinet_PetriNet" = None, petrinet_Arc4: "petrinet_Node" = None, petrinet_Arc7: "petrinet_Node" = None):
        self.poids = poids
        self.readArc = readArc
        self.petrinet_Arc = petrinet_Arc
        self.petrinet_Arc4 = petrinet_Arc4
        self.petrinet_Arc7 = petrinet_Arc7
        
    @property
    def readArc(self) -> bool:
        return self.__readArc

    @readArc.setter
    def readArc(self, readArc: bool):
        self.__readArc = readArc

    @property
    def poids(self) -> int:
        return self.__poids

    @poids.setter
    def poids(self, poids: int):
        self.__poids = poids

    @property
    def petrinet_Arc4(self):
        return self.__petrinet_Arc4

    @petrinet_Arc4.setter
    def petrinet_Arc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc4", None)
        self.__petrinet_Arc4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Node5"):
                opp_val = getattr(old_value, "petrinet_Node5", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Node5"):
                opp_val = getattr(value, "petrinet_Node5", None)
                setattr(value, "petrinet_Node5", self)

    @property
    def petrinet_Arc7(self):
        return self.__petrinet_Arc7

    @petrinet_Arc7.setter
    def petrinet_Arc7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc7", None)
        self.__petrinet_Arc7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Node8"):
                opp_val = getattr(old_value, "petrinet_Node8", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Node8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Node8"):
                opp_val = getattr(value, "petrinet_Node8", None)
                setattr(value, "petrinet_Node8", self)

    @property
    def petrinet_Arc(self):
        return self.__petrinet_Arc

    @petrinet_Arc.setter
    def petrinet_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc", None)
        self.__petrinet_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNet2"):
                opp_val = getattr(old_value, "petrinet_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet2"):
                opp_val = getattr(value, "petrinet_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_Node(ABC):

    def __init__(self, name: str, petrinet_Node: "petrinet_PetriNet" = None, petrinet_Node5: "petrinet_Arc" = None, petrinet_Node8: "petrinet_Arc" = None):
        self.name = name
        self.petrinet_Node = petrinet_Node
        self.petrinet_Node5 = petrinet_Node5
        self.petrinet_Node8 = petrinet_Node8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Node(self):
        return self.__petrinet_Node

    @petrinet_Node.setter
    def petrinet_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node", None)
        self.__petrinet_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNet"):
                opp_val = getattr(old_value, "petrinet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet"):
                opp_val = getattr(value, "petrinet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Node8(self):
        return self.__petrinet_Node8

    @petrinet_Node8.setter
    def petrinet_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node8", None)
        self.__petrinet_Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc7"):
                opp_val = getattr(old_value, "petrinet_Arc7", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc7"):
                opp_val = getattr(value, "petrinet_Arc7", None)
                setattr(value, "petrinet_Arc7", self)

    @property
    def petrinet_Node5(self):
        return self.__petrinet_Node5

    @petrinet_Node5.setter
    def petrinet_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node5", None)
        self.__petrinet_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc4"):
                opp_val = getattr(old_value, "petrinet_Arc4", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc4"):
                opp_val = getattr(value, "petrinet_Arc4", None)
                setattr(value, "petrinet_Arc4", self)

class petrinet_PetriNet:

    def __init__(self, name: str, petrinet_PetriNet: set["petrinet_Node"] = None, petrinet_PetriNet2: set["petrinet_Arc"] = None):
        self.name = name
        self.petrinet_PetriNet = petrinet_PetriNet if petrinet_PetriNet is not None else set()
        self.petrinet_PetriNet2 = petrinet_PetriNet2 if petrinet_PetriNet2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_PetriNet(self):
        return self.__petrinet_PetriNet

    @petrinet_PetriNet.setter
    def petrinet_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet", None)
        self.__petrinet_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Node"):
                    opp_val = getattr(item, "petrinet_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Node"):
                    opp_val = getattr(item, "petrinet_Node", None)
                    
                    setattr(item, "petrinet_Node", self)
                    

    @property
    def petrinet_PetriNet2(self):
        return self.__petrinet_PetriNet2

    @petrinet_PetriNet2.setter
    def petrinet_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet2", None)
        self.__petrinet_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Arc"):
                    opp_val = getattr(item, "petrinet_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Arc"):
                    opp_val = getattr(item, "petrinet_Arc", None)
                    
                    setattr(item, "petrinet_Arc", self)
                    
