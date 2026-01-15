from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class petrinet_Transition(Node):

    def __init__(self, seconds: float):
        self.seconds = seconds
        
    @property
    def seconds(self) -> float:
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: float):
        self.__seconds = seconds

class petrinet_Token:

    pass
class petrinet_Place(Node):

    pass
class petrinet_Arc:

    pass
class petrinet_Node(ABC):

    def __init__(self, name: str, petrinet_Node: "petrinet_PetriNet" = None, petrinet_Node8: "petrinet_Arc" = None, petrinet_Node11: "petrinet_Arc" = None, petrinet_Node13: "petrinet_PetriNet" = None, petrinet_Node16: set["petrinet_Arc"] = None, petrinet_Node19: set["petrinet_Arc"] = None):
        self.name = name
        self.petrinet_Node = petrinet_Node
        self.petrinet_Node8 = petrinet_Node8
        self.petrinet_Node11 = petrinet_Node11
        self.petrinet_Node13 = petrinet_Node13
        self.petrinet_Node16 = petrinet_Node16 if petrinet_Node16 is not None else set()
        self.petrinet_Node19 = petrinet_Node19 if petrinet_Node19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def petrinet_Node13(self):
        return self.__petrinet_Node13

    @petrinet_Node13.setter
    def petrinet_Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node13", None)
        self.__petrinet_Node13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNet14"):
                opp_val = getattr(old_value, "petrinet_PetriNet14", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_PetriNet14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet14"):
                opp_val = getattr(value, "petrinet_PetriNet14", None)
                setattr(value, "petrinet_PetriNet14", self)

    @property
    def petrinet_Node19(self):
        return self.__petrinet_Node19

    @petrinet_Node19.setter
    def petrinet_Node19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node19", None)
        self.__petrinet_Node19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Arc20"):
                    opp_val = getattr(item, "petrinet_Arc20", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Arc20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Arc20"):
                    opp_val = getattr(item, "petrinet_Arc20", None)
                    
                    setattr(item, "petrinet_Arc20", self)
                    

    @property
    def petrinet_Node11(self):
        return self.__petrinet_Node11

    @petrinet_Node11.setter
    def petrinet_Node11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node11", None)
        self.__petrinet_Node11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc10"):
                opp_val = getattr(old_value, "petrinet_Arc10", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc10"):
                opp_val = getattr(value, "petrinet_Arc10", None)
                setattr(value, "petrinet_Arc10", self)

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
    def petrinet_Node16(self):
        return self.__petrinet_Node16

    @petrinet_Node16.setter
    def petrinet_Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node16", None)
        self.__petrinet_Node16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Arc17"):
                    opp_val = getattr(item, "petrinet_Arc17", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Arc17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Arc17"):
                    opp_val = getattr(item, "petrinet_Arc17", None)
                    
                    setattr(item, "petrinet_Arc17", self)
                    

class petrinet_PetriNet:

    def __init__(self, name: str, petrinet_PetriNet: set["petrinet_Node"] = None, petrinet_PetriNet2: set["petrinet_Arc"] = None, petrinet_PetriNet5: "petrinet_Arc" = None, petrinet_PetriNet14: "petrinet_Node" = None):
        self.name = name
        self.petrinet_PetriNet = petrinet_PetriNet if petrinet_PetriNet is not None else set()
        self.petrinet_PetriNet2 = petrinet_PetriNet2 if petrinet_PetriNet2 is not None else set()
        self.petrinet_PetriNet5 = petrinet_PetriNet5
        self.petrinet_PetriNet14 = petrinet_PetriNet14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_PetriNet5(self):
        return self.__petrinet_PetriNet5

    @petrinet_PetriNet5.setter
    def petrinet_PetriNet5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet5", None)
        self.__petrinet_PetriNet5 = value
        
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

    @property
    def petrinet_PetriNet14(self):
        return self.__petrinet_PetriNet14

    @petrinet_PetriNet14.setter
    def petrinet_PetriNet14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet14", None)
        self.__petrinet_PetriNet14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Node13"):
                opp_val = getattr(old_value, "petrinet_Node13", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Node13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Node13"):
                opp_val = getattr(value, "petrinet_Node13", None)
                setattr(value, "petrinet_Node13", self)

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
                    
