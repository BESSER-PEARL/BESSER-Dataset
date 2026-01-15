from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class petrinet_PetriNet:

    def __init__(self, name: str, petrinet_PetriNet: set["petrinet_Place"] = None, petrinet_PetriNet9: set["petrinet_Arc"] = None, petrinet_PetriNet12: set["petrinet_Transition"] = None):
        self.name = name
        self.petrinet_PetriNet = petrinet_PetriNet if petrinet_PetriNet is not None else set()
        self.petrinet_PetriNet9 = petrinet_PetriNet9 if petrinet_PetriNet9 is not None else set()
        self.petrinet_PetriNet12 = petrinet_PetriNet12 if petrinet_PetriNet12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "petrinet_Place7"):
                    opp_val = getattr(item, "petrinet_Place7", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Place7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Place7"):
                    opp_val = getattr(item, "petrinet_Place7", None)
                    
                    setattr(item, "petrinet_Place7", self)
                    

    @property
    def petrinet_PetriNet12(self):
        return self.__petrinet_PetriNet12

    @petrinet_PetriNet12.setter
    def petrinet_PetriNet12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet12", None)
        self.__petrinet_PetriNet12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Transition13"):
                    opp_val = getattr(item, "petrinet_Transition13", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Transition13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Transition13"):
                    opp_val = getattr(item, "petrinet_Transition13", None)
                    
                    setattr(item, "petrinet_Transition13", self)
                    

    @property
    def petrinet_PetriNet9(self):
        return self.__petrinet_PetriNet9

    @petrinet_PetriNet9.setter
    def petrinet_PetriNet9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet9", None)
        self.__petrinet_PetriNet9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Arc10"):
                    opp_val = getattr(item, "petrinet_Arc10", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Arc10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Arc10"):
                    opp_val = getattr(item, "petrinet_Arc10", None)
                    
                    setattr(item, "petrinet_Arc10", self)
                    

class petrinet_Arc:

    def __init__(self, weight: int, toPlace: bool, petrinet_Arc: "petrinet_Transition" = None, petrinet_Arc4: "petrinet_Place" = None, petrinet_Arc10: "petrinet_PetriNet" = None):
        self.weight = weight
        self.toPlace = toPlace
        self.petrinet_Arc = petrinet_Arc
        self.petrinet_Arc4 = petrinet_Arc4
        self.petrinet_Arc10 = petrinet_Arc10
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def toPlace(self) -> bool:
        return self.__toPlace

    @toPlace.setter
    def toPlace(self, toPlace: bool):
        self.__toPlace = toPlace

    @property
    def petrinet_Arc10(self):
        return self.__petrinet_Arc10

    @petrinet_Arc10.setter
    def petrinet_Arc10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc10", None)
        self.__petrinet_Arc10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNet9"):
                opp_val = getattr(old_value, "petrinet_PetriNet9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet9"):
                opp_val = getattr(value, "petrinet_PetriNet9", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Arc4(self):
        return self.__petrinet_Arc4

    @petrinet_Arc4.setter
    def petrinet_Arc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc4", None)
        self.__petrinet_Arc4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Place5"):
                opp_val = getattr(old_value, "petrinet_Place5", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Place5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Place5"):
                opp_val = getattr(value, "petrinet_Place5", None)
                setattr(value, "petrinet_Place5", self)

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
            if hasattr(old_value, "petrinet_Transition2"):
                opp_val = getattr(old_value, "petrinet_Transition2", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Transition2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Transition2"):
                opp_val = getattr(value, "petrinet_Transition2", None)
                setattr(value, "petrinet_Transition2", self)

class petrinet_Transition:

    def __init__(self, name: str, petrinet_Transition: "petrinet_Place" = None, petrinet_Transition2: "petrinet_Arc" = None, petrinet_Transition13: "petrinet_PetriNet" = None):
        self.name = name
        self.petrinet_Transition = petrinet_Transition
        self.petrinet_Transition2 = petrinet_Transition2
        self.petrinet_Transition13 = petrinet_Transition13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Transition13(self):
        return self.__petrinet_Transition13

    @petrinet_Transition13.setter
    def petrinet_Transition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition13", None)
        self.__petrinet_Transition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNet12"):
                opp_val = getattr(old_value, "petrinet_PetriNet12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet12"):
                opp_val = getattr(value, "petrinet_PetriNet12", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Transition2(self):
        return self.__petrinet_Transition2

    @petrinet_Transition2.setter
    def petrinet_Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition2", None)
        self.__petrinet_Transition2 = value
        
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

class petrinet_Place:

    def __init__(self, token: int, name: str, petrinet_Place: set["petrinet_Transition"] = None, petrinet_Place5: "petrinet_Arc" = None, petrinet_Place7: "petrinet_PetriNet" = None):
        self.token = token
        self.name = name
        self.petrinet_Place = petrinet_Place if petrinet_Place is not None else set()
        self.petrinet_Place5 = petrinet_Place5
        self.petrinet_Place7 = petrinet_Place7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def token(self) -> int:
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token

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
            if hasattr(old_value, "petrinet_Arc4"):
                opp_val = getattr(old_value, "petrinet_Arc4", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc4"):
                opp_val = getattr(value, "petrinet_Arc4", None)
                setattr(value, "petrinet_Arc4", self)
