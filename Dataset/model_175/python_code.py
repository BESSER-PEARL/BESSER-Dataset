from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinet_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class petrinet_Transition(NamedElement):

    pass
class petrinet_Place(NamedElement):

    def __init__(self, tokens: int, petrinet_Place5: "petrinet_Net" = None, petrinet_Place: "petrinet_Net" = None, petrinet_Place7: "petrinet_Transition" = None, petrinet_Place11: "petrinet_Transition" = None, petrinet_Place14: "petrinet_Transition" = None):
        self.tokens = tokens
        self.petrinet_Place5 = petrinet_Place5
        self.petrinet_Place = petrinet_Place
        self.petrinet_Place7 = petrinet_Place7
        self.petrinet_Place11 = petrinet_Place11
        self.petrinet_Place14 = petrinet_Place14
        
    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def petrinet_Place14(self):
        return self.__petrinet_Place14

    @petrinet_Place14.setter
    def petrinet_Place14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place14", None)
        self.__petrinet_Place14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Transition13"):
                opp_val = getattr(old_value, "petrinet_Transition13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition13"):
                opp_val = getattr(value, "petrinet_Transition13", None)
                if opp_val is None:
                    setattr(value, "petrinet_Transition13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Place5(self):
        return self.__petrinet_Place5

    @petrinet_Place5.setter
    def petrinet_Place5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place5", None)
        self.__petrinet_Place5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Net4"):
                opp_val = getattr(old_value, "petrinet_Net4", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Net4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Net4"):
                opp_val = getattr(value, "petrinet_Net4", None)
                setattr(value, "petrinet_Net4", self)

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
            if hasattr(old_value, "petrinet_Net"):
                opp_val = getattr(old_value, "petrinet_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Net"):
                opp_val = getattr(value, "petrinet_Net", None)
                if opp_val is None:
                    setattr(value, "petrinet_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "petrinet_Transition8"):
                opp_val = getattr(old_value, "petrinet_Transition8", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition8"):
                opp_val = getattr(value, "petrinet_Transition8", None)
                setattr(value, "petrinet_Transition8", self)

    @property
    def petrinet_Place11(self):
        return self.__petrinet_Place11

    @petrinet_Place11.setter
    def petrinet_Place11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place11", None)
        self.__petrinet_Place11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Transition10"):
                opp_val = getattr(old_value, "petrinet_Transition10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition10"):
                opp_val = getattr(value, "petrinet_Transition10", None)
                if opp_val is None:
                    setattr(value, "petrinet_Transition10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_Net(NamedElement):

    pass