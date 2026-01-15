from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class petri_PTArc(Arc):

    pass
class petri_TPArc(Arc):

    pass
class Node:

    pass
class petri_Transition(Node):

    pass
class petri_Place(Node):

    def __init__(self, tokens: int, petri_Place: "petri_TPArc" = None, petri_Place7: "petri_PTArc" = None):
        self.tokens = tokens
        self.petri_Place = petri_Place
        self.petri_Place7 = petri_Place7
        
    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def petri_Place7(self):
        return self.__petri_Place7

    @petri_Place7.setter
    def petri_Place7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Place__petri_Place7", None)
        self.__petri_Place7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_PTArc"):
                opp_val = getattr(old_value, "petri_PTArc", None)
                if opp_val == self:
                    setattr(old_value, "petri_PTArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_PTArc"):
                opp_val = getattr(value, "petri_PTArc", None)
                setattr(value, "petri_PTArc", self)

    @property
    def petri_Place(self):
        return self.__petri_Place

    @petri_Place.setter
    def petri_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Place__petri_Place", None)
        self.__petri_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_TPArc5"):
                opp_val = getattr(old_value, "petri_TPArc5", None)
                if opp_val == self:
                    setattr(old_value, "petri_TPArc5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_TPArc5"):
                opp_val = getattr(value, "petri_TPArc5", None)
                setattr(value, "petri_TPArc5", self)

class petri_Arc(ABC):

    pass
class petri_Node(ABC):

    def __init__(self, name: str, petri_Node: "petri_PetriNet" = None):
        self.name = name
        self.petri_Node = petri_Node
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petri_Node(self):
        return self.__petri_Node

    @petri_Node.setter
    def petri_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Node__petri_Node", None)
        self.__petri_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_PetriNet"):
                opp_val = getattr(old_value, "petri_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_PetriNet"):
                opp_val = getattr(value, "petri_PetriNet", None)
                if opp_val is None:
                    setattr(value, "petri_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petri_PetriNet:

    pass