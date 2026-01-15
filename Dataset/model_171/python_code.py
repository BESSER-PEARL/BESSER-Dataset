from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_Node(ABC):

    def __init__(self, name: str, petrinet_Node: "petrinet_PetriNet" = None):
        self.name = name
        self.petrinet_Node = petrinet_Node
        
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
            if hasattr(old_value, "petrinet_PetriNet22"):
                opp_val = getattr(old_value, "petrinet_PetriNet22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet22"):
                opp_val = getattr(value, "petrinet_PetriNet22", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_Arc(ABC):

    def __init__(self, weight: int, petrinet_Arc: "petrinet_PetriNet" = None):
        self.weight = weight
        self.petrinet_Arc = petrinet_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

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
            if hasattr(old_value, "petrinet_PetriNet20"):
                opp_val = getattr(old_value, "petrinet_PetriNet20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet20"):
                opp_val = getattr(value, "petrinet_PetriNet20", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_PetriNet:

    def __init__(self, name: str, petrinet_PetriNet: set["petrinet_Place"] = None, petrinet_PetriNet11: set["petrinet_Transition"] = None, petrinet_PetriNet14: set["petrinet_PlaceTransitionArc"] = None, petrinet_PetriNet17: set["petrinet_TransitionPlaceArc"] = None, petrinet_PetriNet22: set["petrinet_Node"] = None, petrinet_PetriNet20: set["petrinet_Arc"] = None):
        self.name = name
        self.petrinet_PetriNet = petrinet_PetriNet if petrinet_PetriNet is not None else set()
        self.petrinet_PetriNet11 = petrinet_PetriNet11 if petrinet_PetriNet11 is not None else set()
        self.petrinet_PetriNet14 = petrinet_PetriNet14 if petrinet_PetriNet14 is not None else set()
        self.petrinet_PetriNet17 = petrinet_PetriNet17 if petrinet_PetriNet17 is not None else set()
        self.petrinet_PetriNet22 = petrinet_PetriNet22 if petrinet_PetriNet22 is not None else set()
        self.petrinet_PetriNet20 = petrinet_PetriNet20 if petrinet_PetriNet20 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_PetriNet11(self):
        return self.__petrinet_PetriNet11

    @petrinet_PetriNet11.setter
    def petrinet_PetriNet11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet11", None)
        self.__petrinet_PetriNet11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Transition12"):
                    opp_val = getattr(item, "petrinet_Transition12", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Transition12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Transition12"):
                    opp_val = getattr(item, "petrinet_Transition12", None)
                    
                    setattr(item, "petrinet_Transition12", self)
                    

    @property
    def petrinet_PetriNet20(self):
        return self.__petrinet_PetriNet20

    @petrinet_PetriNet20.setter
    def petrinet_PetriNet20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet20", None)
        self.__petrinet_PetriNet20 = value if value is not None else set()
        
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
    def petrinet_PetriNet22(self):
        return self.__petrinet_PetriNet22

    @petrinet_PetriNet22.setter
    def petrinet_PetriNet22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet22", None)
        self.__petrinet_PetriNet22 = value if value is not None else set()
        
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
                if hasattr(item, "petrinet_Place9"):
                    opp_val = getattr(item, "petrinet_Place9", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Place9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Place9"):
                    opp_val = getattr(item, "petrinet_Place9", None)
                    
                    setattr(item, "petrinet_Place9", self)
                    

    @property
    def petrinet_PetriNet17(self):
        return self.__petrinet_PetriNet17

    @petrinet_PetriNet17.setter
    def petrinet_PetriNet17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet17", None)
        self.__petrinet_PetriNet17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_TransitionPlaceArc18"):
                    opp_val = getattr(item, "petrinet_TransitionPlaceArc18", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_TransitionPlaceArc18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_TransitionPlaceArc18"):
                    opp_val = getattr(item, "petrinet_TransitionPlaceArc18", None)
                    
                    setattr(item, "petrinet_TransitionPlaceArc18", self)
                    

    @property
    def petrinet_PetriNet14(self):
        return self.__petrinet_PetriNet14

    @petrinet_PetriNet14.setter
    def petrinet_PetriNet14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet14", None)
        self.__petrinet_PetriNet14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_PlaceTransitionArc15"):
                    opp_val = getattr(item, "petrinet_PlaceTransitionArc15", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_PlaceTransitionArc15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_PlaceTransitionArc15"):
                    opp_val = getattr(item, "petrinet_PlaceTransitionArc15", None)
                    
                    setattr(item, "petrinet_PlaceTransitionArc15", self)
                    

class Arc:

    pass
class petrinet_TransitionPlaceArc(Arc):

    pass
class petrinet_PlaceTransitionArc(Arc):

    pass
class Node:

    pass
class petrinet_Transition(Node):

    pass
class petrinet_Place(Node):

    def __init__(self, tokens: int, capacity: int, petrinet_Place: "petrinet_PlaceTransitionArc" = None, petrinet_Place7: "petrinet_TransitionPlaceArc" = None, petrinet_Place9: "petrinet_PetriNet" = None):
        self.tokens = tokens
        self.capacity = capacity
        self.petrinet_Place = petrinet_Place
        self.petrinet_Place7 = petrinet_Place7
        self.petrinet_Place9 = petrinet_Place9
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def petrinet_Place(self):
        return self.__petrinet_Place

    @petrinet_Place.setter
    def petrinet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place", None)
        self.__petrinet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PlaceTransitionArc"):
                opp_val = getattr(old_value, "petrinet_PlaceTransitionArc", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_PlaceTransitionArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PlaceTransitionArc"):
                opp_val = getattr(value, "petrinet_PlaceTransitionArc", None)
                setattr(value, "petrinet_PlaceTransitionArc", self)

    @property
    def petrinet_Place7(self):
        return self.__petrinet_Place7

    @petrinet_Place7.setter
    def petrinet_Place7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place7", None)
        self.__petrinet_Place7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_TransitionPlaceArc6"):
                opp_val = getattr(old_value, "petrinet_TransitionPlaceArc6", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_TransitionPlaceArc6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_TransitionPlaceArc6"):
                opp_val = getattr(value, "petrinet_TransitionPlaceArc6", None)
                setattr(value, "petrinet_TransitionPlaceArc6", self)

    @property
    def petrinet_Place9(self):
        return self.__petrinet_Place9

    @petrinet_Place9.setter
    def petrinet_Place9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place9", None)
        self.__petrinet_Place9 = value
        
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
