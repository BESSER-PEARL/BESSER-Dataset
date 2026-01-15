from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNetElement:

    pass
class petrinet_Arc(PetriNetElement):

    def __init__(self, multiplicity: int, readOnly: bool, linksToSuccessor: "petrinet_Node" = None, linksToPredecessor: "petrinet_Node" = None, Arc: "petrinet_Node" = None, Arc4: "petrinet_Node" = None):
        self.multiplicity = multiplicity
        self.readOnly = readOnly
        self.linksToSuccessor = linksToSuccessor
        self.linksToPredecessor = linksToPredecessor
        self.Arc = Arc
        self.Arc4 = Arc4
        
    @property
    def multiplicity(self) -> int:
        return self.__multiplicity

    @multiplicity.setter
    def multiplicity(self, multiplicity: int):
        self.__multiplicity = multiplicity

    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecessor"):
                opp_val = getattr(old_value, "predecessor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecessor"):
                opp_val = getattr(value, "predecessor", None)
                if opp_val is None:
                    setattr(value, "predecessor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc4(self):
        return self.__Arc4

    @Arc4.setter
    def Arc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__Arc4", None)
        self.__Arc4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successor"):
                opp_val = getattr(old_value, "successor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successor"):
                opp_val = getattr(value, "successor", None)
                if opp_val is None:
                    setattr(value, "successor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linksToSuccessor(self):
        return self.__linksToSuccessor

    @linksToSuccessor.setter
    def linksToSuccessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__linksToSuccessor", None)
        self.__linksToSuccessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def linksToPredecessor(self):
        return self.__linksToPredecessor

    @linksToPredecessor.setter
    def linksToPredecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__linksToPredecessor", None)
        self.__linksToPredecessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node7"):
                opp_val = getattr(old_value, "Node7", None)
                if opp_val == self:
                    setattr(old_value, "Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node7"):
                opp_val = getattr(value, "Node7", None)
                setattr(value, "Node7", self)

class petrinet_Node(PetriNetElement):

    def __init__(self, name: str, Node: "petrinet_Arc" = None, Node7: "petrinet_Arc" = None, predecessor: set["petrinet_Arc"] = None, successor: set["petrinet_Arc"] = None):
        self.name = name
        self.Node = Node
        self.Node7 = Node7
        self.predecessor = predecessor if predecessor is not None else set()
        self.successor = successor if successor is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    setattr(item, "Arc", self)
                    

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__successor", None)
        self.__successor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc4"):
                    opp_val = getattr(item, "Arc4", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc4"):
                    opp_val = getattr(item, "Arc4", None)
                    
                    setattr(item, "Arc4", self)
                    

    @property
    def Node7(self):
        return self.__Node7

    @Node7.setter
    def Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node7", None)
        self.__Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linksToPredecessor"):
                opp_val = getattr(old_value, "linksToPredecessor", None)
                if opp_val == self:
                    setattr(old_value, "linksToPredecessor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linksToPredecessor"):
                opp_val = getattr(value, "linksToPredecessor", None)
                setattr(value, "linksToPredecessor", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linksToSuccessor"):
                opp_val = getattr(old_value, "linksToSuccessor", None)
                if opp_val == self:
                    setattr(old_value, "linksToSuccessor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linksToSuccessor"):
                opp_val = getattr(value, "linksToSuccessor", None)
                setattr(value, "linksToSuccessor", self)

class petrinet_PetriNetElement(ABC):

    pass
class petrinet_PetriNet:

    def __init__(self, name: str, petriNet: set["petrinet_PetriNetElement"] = None, PetriNet: "petrinet_PetriNetElement" = None):
        self.name = name
        self.petriNet = petriNet if petriNet is not None else set()
        self.PetriNet = PetriNet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petriNet(self):
        return self.__petriNet

    @petriNet.setter
    def petriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petriNet", None)
        self.__petriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNetElement"):
                    opp_val = getattr(item, "PetriNetElement", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNetElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNetElement"):
                    opp_val = getattr(item, "PetriNetElement", None)
                    
                    setattr(item, "PetriNetElement", self)
                    

    @property
    def PetriNet(self):
        return self.__PetriNet

    @PetriNet.setter
    def PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__PetriNet", None)
        self.__PetriNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNetElements"):
                opp_val = getattr(old_value, "petriNetElements", None)
                if opp_val == self:
                    setattr(old_value, "petriNetElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNetElements"):
                opp_val = getattr(value, "petriNetElements", None)
                setattr(value, "petriNetElements", self)

class Node:

    pass
class petrinet_Transition(Node):

    pass
class petrinet_Place(Node):

    def __init__(self, marking: int):
        self.marking = marking
        
    @property
    def marking(self) -> int:
        return self.__marking

    @marking.setter
    def marking(self, marking: int):
        self.__marking = marking
