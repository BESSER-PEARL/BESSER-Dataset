from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class petri_net_Place(Node):

    pass
class petri_net_Transition(Node):

    pass
class petri_net_Arc:

    def __init__(self, name: str, petri_net_Arc4: "petri_net_Node" = None, petri_net_Arc7: "petri_net_Node" = None, petri_net_Arc: "petri_net_PetriNet" = None):
        self.name = name
        self.petri_net_Arc4 = petri_net_Arc4
        self.petri_net_Arc7 = petri_net_Arc7
        self.petri_net_Arc = petri_net_Arc
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petri_net_Arc4(self):
        return self.__petri_net_Arc4

    @petri_net_Arc4.setter
    def petri_net_Arc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_net_Arc__petri_net_Arc4", None)
        self.__petri_net_Arc4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_net_Node5"):
                opp_val = getattr(old_value, "petri_net_Node5", None)
                if opp_val == self:
                    setattr(old_value, "petri_net_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_net_Node5"):
                opp_val = getattr(value, "petri_net_Node5", None)
                setattr(value, "petri_net_Node5", self)

    @property
    def petri_net_Arc7(self):
        return self.__petri_net_Arc7

    @petri_net_Arc7.setter
    def petri_net_Arc7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_net_Arc__petri_net_Arc7", None)
        self.__petri_net_Arc7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_net_Node8"):
                opp_val = getattr(old_value, "petri_net_Node8", None)
                if opp_val == self:
                    setattr(old_value, "petri_net_Node8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_net_Node8"):
                opp_val = getattr(value, "petri_net_Node8", None)
                setattr(value, "petri_net_Node8", self)

    @property
    def petri_net_Arc(self):
        return self.__petri_net_Arc

    @petri_net_Arc.setter
    def petri_net_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_net_Arc__petri_net_Arc", None)
        self.__petri_net_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_net_PetriNet2"):
                opp_val = getattr(old_value, "petri_net_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_net_PetriNet2"):
                opp_val = getattr(value, "petri_net_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "petri_net_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petri_net_PetriNet:

    def __init__(self, name: str, petri_net_PetriNet: set["petri_net_Node"] = None, petri_net_PetriNet2: set["petri_net_Arc"] = None):
        self.name = name
        self.petri_net_PetriNet = petri_net_PetriNet if petri_net_PetriNet is not None else set()
        self.petri_net_PetriNet2 = petri_net_PetriNet2 if petri_net_PetriNet2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petri_net_PetriNet2(self):
        return self.__petri_net_PetriNet2

    @petri_net_PetriNet2.setter
    def petri_net_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_net_PetriNet__petri_net_PetriNet2", None)
        self.__petri_net_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petri_net_Arc"):
                    opp_val = getattr(item, "petri_net_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "petri_net_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petri_net_Arc"):
                    opp_val = getattr(item, "petri_net_Arc", None)
                    
                    setattr(item, "petri_net_Arc", self)
                    

    @property
    def petri_net_PetriNet(self):
        return self.__petri_net_PetriNet

    @petri_net_PetriNet.setter
    def petri_net_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_net_PetriNet__petri_net_PetriNet", None)
        self.__petri_net_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petri_net_Node"):
                    opp_val = getattr(item, "petri_net_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "petri_net_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petri_net_Node"):
                    opp_val = getattr(item, "petri_net_Node", None)
                    
                    setattr(item, "petri_net_Node", self)
                    

class petri_net_Node(ABC):

    def __init__(self, name: str, petri_net_Node5: "petri_net_Arc" = None, petri_net_Node8: "petri_net_Arc" = None, petri_net_Node: "petri_net_PetriNet" = None):
        self.name = name
        self.petri_net_Node5 = petri_net_Node5
        self.petri_net_Node8 = petri_net_Node8
        self.petri_net_Node = petri_net_Node
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petri_net_Node5(self):
        return self.__petri_net_Node5

    @petri_net_Node5.setter
    def petri_net_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_net_Node__petri_net_Node5", None)
        self.__petri_net_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_net_Arc4"):
                opp_val = getattr(old_value, "petri_net_Arc4", None)
                if opp_val == self:
                    setattr(old_value, "petri_net_Arc4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_net_Arc4"):
                opp_val = getattr(value, "petri_net_Arc4", None)
                setattr(value, "petri_net_Arc4", self)

    @property
    def petri_net_Node(self):
        return self.__petri_net_Node

    @petri_net_Node.setter
    def petri_net_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_net_Node__petri_net_Node", None)
        self.__petri_net_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_net_PetriNet"):
                opp_val = getattr(old_value, "petri_net_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_net_PetriNet"):
                opp_val = getattr(value, "petri_net_PetriNet", None)
                if opp_val is None:
                    setattr(value, "petri_net_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petri_net_Node8(self):
        return self.__petri_net_Node8

    @petri_net_Node8.setter
    def petri_net_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_net_Node__petri_net_Node8", None)
        self.__petri_net_Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_net_Arc7"):
                opp_val = getattr(old_value, "petri_net_Arc7", None)
                if opp_val == self:
                    setattr(old_value, "petri_net_Arc7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_net_Arc7"):
                opp_val = getattr(value, "petri_net_Arc7", None)
                setattr(value, "petri_net_Arc7", self)
