from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RefTokens:

    pass
class petrinet_Token(RefTokens):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class petrinet_RefTokens(ABC):

    pass
class Node:

    pass
class petrinet_Place(Node):

    pass
class petrinet_Transition(Node):

    pass
class petrinet_RefPetriNets(ABC):

    pass
class petrinet_RefArcs(ABC):

    pass
class petrinet_RefNodes(ABC):

    pass
class RefPetriNets:

    pass
class petrinet_PetriNet(RefPetriNets):

    def __init__(self, name: str, petrinet_PetriNet: set["petrinet_RefNodes"] = None, petrinet_PetriNet2: set["petrinet_RefArcs"] = None):
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
                if hasattr(item, "petrinet_RefArcs"):
                    opp_val = getattr(item, "petrinet_RefArcs", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_RefArcs", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_RefArcs"):
                    opp_val = getattr(item, "petrinet_RefArcs", None)
                    
                    setattr(item, "petrinet_RefArcs", self)
                    

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
                if hasattr(item, "petrinet_RefNodes"):
                    opp_val = getattr(item, "petrinet_RefNodes", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_RefNodes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_RefNodes"):
                    opp_val = getattr(item, "petrinet_RefNodes", None)
                    
                    setattr(item, "petrinet_RefNodes", self)
                    

class RefArcs:

    pass
class petrinet_Arc(RefArcs):

    def __init__(self, name: str, petrinet_Arc: "petrinet_RefNodes" = None, petrinet_Arc6: "petrinet_RefNodes" = None):
        self.name = name
        self.petrinet_Arc = petrinet_Arc
        self.petrinet_Arc6 = petrinet_Arc6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "petrinet_RefNodes4"):
                opp_val = getattr(old_value, "petrinet_RefNodes4", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_RefNodes4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_RefNodes4"):
                opp_val = getattr(value, "petrinet_RefNodes4", None)
                setattr(value, "petrinet_RefNodes4", self)

    @property
    def petrinet_Arc6(self):
        return self.__petrinet_Arc6

    @petrinet_Arc6.setter
    def petrinet_Arc6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc6", None)
        self.__petrinet_Arc6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_RefNodes7"):
                opp_val = getattr(old_value, "petrinet_RefNodes7", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_RefNodes7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_RefNodes7"):
                opp_val = getattr(value, "petrinet_RefNodes7", None)
                setattr(value, "petrinet_RefNodes7", self)

class RefNodes:

    pass
class petrinet_Node(RefNodes):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
