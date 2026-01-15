from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class petrinet_Node(ABC):

    pass
class petrinet_Arc:

    def __init__(self, w: str, petrinet_Arc: "petrinet_PNGraph" = None, petrinet_Arc6: "petrinet_Node" = None, petrinet_Arc8: "petrinet_Node" = None):
        self.w = w
        self.petrinet_Arc = petrinet_Arc
        self.petrinet_Arc6 = petrinet_Arc6
        self.petrinet_Arc8 = petrinet_Arc8
        
    @property
    def w(self) -> str:
        return self.__w

    @w.setter
    def w(self, w: str):
        self.__w = w

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
            if hasattr(old_value, "petrinet_PNGraph4"):
                opp_val = getattr(old_value, "petrinet_PNGraph4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PNGraph4"):
                opp_val = getattr(value, "petrinet_PNGraph4", None)
                if opp_val is None:
                    setattr(value, "petrinet_PNGraph4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Arc8(self):
        return self.__petrinet_Arc8

    @petrinet_Arc8.setter
    def petrinet_Arc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc8", None)
        self.__petrinet_Arc8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Node9"):
                opp_val = getattr(old_value, "petrinet_Node9", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Node9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Node9"):
                opp_val = getattr(value, "petrinet_Node9", None)
                setattr(value, "petrinet_Node9", self)

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
            if hasattr(old_value, "petrinet_Node"):
                opp_val = getattr(old_value, "petrinet_Node", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Node"):
                opp_val = getattr(value, "petrinet_Node", None)
                setattr(value, "petrinet_Node", self)

class petrinet_Place(Node):

    def __init__(self, id: str, markings: str, petrinet_Place: "petrinet_PNGraph" = None):
        self.id = id
        self.markings = markings
        self.petrinet_Place = petrinet_Place
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def markings(self) -> str:
        return self.__markings

    @markings.setter
    def markings(self, markings: str):
        self.__markings = markings

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
            if hasattr(old_value, "petrinet_PNGraph"):
                opp_val = getattr(old_value, "petrinet_PNGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PNGraph"):
                opp_val = getattr(value, "petrinet_PNGraph", None)
                if opp_val is None:
                    setattr(value, "petrinet_PNGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_PNGraph:

    pass
class petrinet_Transition(Node):

    def __init__(self, id: str, petrinet_Transition: "petrinet_PNGraph" = None):
        self.id = id
        self.petrinet_Transition = petrinet_Transition
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def petrinet_Transition(self):
        return self.__petrinet_Transition

    @petrinet_Transition.setter
    def petrinet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition", None)
        self.__petrinet_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PNGraph2"):
                opp_val = getattr(old_value, "petrinet_PNGraph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PNGraph2"):
                opp_val = getattr(value, "petrinet_PNGraph2", None)
                if opp_val is None:
                    setattr(value, "petrinet_PNGraph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
