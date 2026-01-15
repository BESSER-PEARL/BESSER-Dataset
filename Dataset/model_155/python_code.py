from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinet_PetriNet:

    def __init__(self, name: str, PetriNet8: "petrinet_Arc" = None, PetriNet10: "petrinet_Transition" = None, net: set["petrinet_Place"] = None, net13: set["petrinet_Arc"] = None, PetriNet: "petrinet_Place" = None, net15: set["petrinet_Transition"] = None):
        self.name = name
        self.PetriNet8 = PetriNet8
        self.PetriNet10 = PetriNet10
        self.net = net if net is not None else set()
        self.net13 = net13 if net13 is not None else set()
        self.PetriNet = PetriNet
        self.net15 = net15 if net15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "places"):
                opp_val = getattr(old_value, "places", None)
                if opp_val == self:
                    setattr(old_value, "places", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "places"):
                opp_val = getattr(value, "places", None)
                setattr(value, "places", self)

    @property
    def net13(self):
        return self.__net13

    @net13.setter
    def net13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__net13", None)
        self.__net13 = value if value is not None else set()
        
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
    def PetriNet10(self):
        return self.__PetriNet10

    @PetriNet10.setter
    def PetriNet10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__PetriNet10", None)
        self.__PetriNet10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    @property
    def net15(self):
        return self.__net15

    @net15.setter
    def net15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__net15", None)
        self.__net15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def net(self):
        return self.__net

    @net.setter
    def net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__net", None)
        self.__net = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Place"):
                    opp_val = getattr(item, "Place", None)
                    
                    if opp_val == self:
                        setattr(item, "Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Place"):
                    opp_val = getattr(item, "Place", None)
                    
                    setattr(item, "Place", self)
                    

    @property
    def PetriNet8(self):
        return self.__PetriNet8

    @PetriNet8.setter
    def PetriNet8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__PetriNet8", None)
        self.__PetriNet8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arcs"):
                opp_val = getattr(old_value, "arcs", None)
                if opp_val == self:
                    setattr(old_value, "arcs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arcs"):
                opp_val = getattr(value, "arcs", None)
                setattr(value, "arcs", self)

class petrinet_Transition:

    def __init__(self, name: str, petrinet_Transition3: "petrinet_Arc" = None, transitions: "petrinet_PetriNet" = None, petrinet_Transition: "petrinet_Place" = None, Transition: "petrinet_PetriNet" = None):
        self.name = name
        self.petrinet_Transition3 = petrinet_Transition3
        self.transitions = transitions
        self.petrinet_Transition = petrinet_Transition
        self.Transition = Transition
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "petrinet_Place"):
                opp_val = getattr(old_value, "petrinet_Place", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Place"):
                opp_val = getattr(value, "petrinet_Place", None)
                if opp_val is None:
                    setattr(value, "petrinet_Place", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet10"):
                opp_val = getattr(old_value, "PetriNet10", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet10"):
                opp_val = getattr(value, "PetriNet10", None)
                setattr(value, "PetriNet10", self)

    @property
    def petrinet_Transition3(self):
        return self.__petrinet_Transition3

    @petrinet_Transition3.setter
    def petrinet_Transition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition3", None)
        self.__petrinet_Transition3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc"):
                opp_val = getattr(old_value, "petrinet_Arc", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc"):
                opp_val = getattr(value, "petrinet_Arc", None)
                setattr(value, "petrinet_Arc", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "net15"):
                opp_val = getattr(old_value, "net15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net15"):
                opp_val = getattr(value, "net15", None)
                if opp_val is None:
                    setattr(value, "net15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_Place:

    def __init__(self, token: int, name: str, petrinet_Place6: "petrinet_Arc" = None, Place: "petrinet_PetriNet" = None, petrinet_Place: set["petrinet_Transition"] = None, places: "petrinet_PetriNet" = None):
        self.token = token
        self.name = name
        self.petrinet_Place6 = petrinet_Place6
        self.Place = Place
        self.petrinet_Place = petrinet_Place if petrinet_Place is not None else set()
        self.places = places
        
    @property
    def token(self) -> int:
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__Place", None)
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

    @property
    def petrinet_Place6(self):
        return self.__petrinet_Place6

    @petrinet_Place6.setter
    def petrinet_Place6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place6", None)
        self.__petrinet_Place6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc5"):
                opp_val = getattr(old_value, "petrinet_Arc5", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc5"):
                opp_val = getattr(value, "petrinet_Arc5", None)
                setattr(value, "petrinet_Arc5", self)

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__places", None)
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
    def petrinet_Place(self):
        return self.__petrinet_Place

    @petrinet_Place.setter
    def petrinet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Place__petrinet_Place", None)
        self.__petrinet_Place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Transition"):
                    opp_val = getattr(item, "petrinet_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Transition"):
                    opp_val = getattr(item, "petrinet_Transition", None)
                    
                    setattr(item, "petrinet_Transition", self)
                    

class petrinet_Arc:

    def __init__(self, weight: int, toPlace: bool, petrinet_Arc: "petrinet_Transition" = None, petrinet_Arc5: "petrinet_Place" = None, arcs: "petrinet_PetriNet" = None, Arc: "petrinet_PetriNet" = None):
        self.weight = weight
        self.toPlace = toPlace
        self.petrinet_Arc = petrinet_Arc
        self.petrinet_Arc5 = petrinet_Arc5
        self.arcs = arcs
        self.Arc = Arc
        
    @property
    def toPlace(self) -> bool:
        return self.__toPlace

    @toPlace.setter
    def toPlace(self, toPlace: bool):
        self.__toPlace = toPlace

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def petrinet_Arc5(self):
        return self.__petrinet_Arc5

    @petrinet_Arc5.setter
    def petrinet_Arc5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc5", None)
        self.__petrinet_Arc5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Place6"):
                opp_val = getattr(old_value, "petrinet_Place6", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Place6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Place6"):
                opp_val = getattr(value, "petrinet_Place6", None)
                setattr(value, "petrinet_Place6", self)

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
            if hasattr(old_value, "net13"):
                opp_val = getattr(old_value, "net13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net13"):
                opp_val = getattr(value, "net13", None)
                if opp_val is None:
                    setattr(value, "net13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arcs(self):
        return self.__arcs

    @arcs.setter
    def arcs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__arcs", None)
        self.__arcs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet8"):
                opp_val = getattr(old_value, "PetriNet8", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet8"):
                opp_val = getattr(value, "PetriNet8", None)
                setattr(value, "PetriNet8", self)

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
            if hasattr(old_value, "petrinet_Transition3"):
                opp_val = getattr(old_value, "petrinet_Transition3", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Transition3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition3"):
                opp_val = getattr(value, "petrinet_Transition3", None)
                setattr(value, "petrinet_Transition3", self)
