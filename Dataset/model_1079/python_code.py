from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PetriNets_Token:

    pass
class PetriNets_Place:

    def __init__(self, itokens: int, capacity: int, Place6: "PetriNets_Token" = None, Place: "PetriNets_PetriNet" = None, places: "PetriNets_PetriNet" = None, place: set["PetriNets_Token"] = None, PetriNets_Place: "PetriNets_Transition" = None, PetriNets_Place12: "PetriNets_Transition" = None):
        self.itokens = itokens
        self.capacity = capacity
        self.Place6 = Place6
        self.Place = Place
        self.places = places
        self.place = place if place is not None else set()
        self.PetriNets_Place = PetriNets_Place
        self.PetriNets_Place12 = PetriNets_Place12
        
    @property
    def itokens(self) -> int:
        return self.__itokens

    @itokens.setter
    def itokens(self, itokens: int):
        self.__itokens = itokens

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__places", None)
        self.__places = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet"):
                opp_val = getattr(old_value, "PetriNet", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet"):
                opp_val = getattr(value, "PetriNet", None)
                setattr(value, "PetriNet", self)

    @property
    def PetriNets_Place(self):
        return self.__PetriNets_Place

    @PetriNets_Place.setter
    def PetriNets_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place", None)
        self.__PetriNets_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition"):
                opp_val = getattr(old_value, "PetriNets_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition"):
                opp_val = getattr(value, "PetriNets_Transition", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Place6(self):
        return self.__Place6

    @Place6.setter
    def Place6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__Place6", None)
        self.__Place6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tokens.1"):
                opp_val = getattr(old_value, "tokens.1", None)
                if opp_val == self:
                    setattr(old_value, "tokens.1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tokens.1"):
                opp_val = getattr(value, "tokens.1", None)
                setattr(value, "tokens.1", self)

    @property
    def PetriNets_Place12(self):
        return self.__PetriNets_Place12

    @PetriNets_Place12.setter
    def PetriNets_Place12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place12", None)
        self.__PetriNets_Place12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition11"):
                opp_val = getattr(old_value, "PetriNets_Transition11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition11"):
                opp_val = getattr(value, "PetriNets_Transition11", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__place", None)
        self.__place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Token"):
                    opp_val = getattr(item, "Token", None)
                    
                    if opp_val == self:
                        setattr(item, "Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Token"):
                    opp_val = getattr(item, "Token", None)
                    
                    setattr(item, "Token", self)
                    

    @property
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__Place", None)
        self.__Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "net"):
                opp_val = getattr(old_value, "net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net"):
                opp_val = getattr(value, "net", None)
                if opp_val is None:
                    setattr(value, "net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def tokens(self) -> int:
        # TODO: Implement tokens method
        pass

class PetriNets_PetriNet:

    pass
class PetriNet:

    pass
class PetriNets_Transition(PetriNet):

    pass