from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_PetriNet:

    pass
class Arc:

    pass
class petrinet_Arc(ABC):

    def __init__(self, weight: int):
        self.weight = weight
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight


class petrinet_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class petrinet_OutArc(Arc):

    pass
class petrinet_InArc(Arc):

    pass
class Named:

    pass
class petrinet_Transition(Named):

    pass
class petrinet_Place(Named):

    def __init__(self, token: int, petrinet_Place: "petrinet_PetriNet" = None, petrinet_Place12: "petrinet_OutArc" = None, petrinet_Place9: "petrinet_InArc" = None):
        self.token = token
        self.petrinet_Place = petrinet_Place
        self.petrinet_Place12 = petrinet_Place12
        self.petrinet_Place9 = petrinet_Place9
        
        pass
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token


    @property
    def petrinet_Place12(self):
        return self.__petrinet_Place12

    @petrinet_Place12.setter
    def petrinet_Place12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place12", None)
        self.__petrinet_Place12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_OutArc11"):
                opp_val = getattr(old_value, "petrinet_OutArc11", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_OutArc11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_OutArc11"):
                opp_val = getattr(value, "petrinet_OutArc11", None)
                setattr(value, "petrinet_OutArc11", self)

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
    def petrinet_Place9(self):
        return self.__petrinet_Place9

    @petrinet_Place9.setter
    def petrinet_Place9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place9", None)
        self.__petrinet_Place9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_InArc8"):
                opp_val = getattr(old_value, "petrinet_InArc8", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_InArc8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_InArc8"):
                opp_val = getattr(value, "petrinet_InArc8", None)
                setattr(value, "petrinet_InArc8", self)
