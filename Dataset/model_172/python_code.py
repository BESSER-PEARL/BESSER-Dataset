from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Edge:

    pass
class petri_Edge:

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class petri_Place:

    def __init__(self, token: int, petri_Place4: set["petri_EdgeToTransition"] = None, petri_Place: "petri_PetriNet" = None, petri_Place9: "petri_EdgeToPlace" = None):
        self.token = token
        self.petri_Place4 = petri_Place4 if petri_Place4 is not None else set()
        self.petri_Place = petri_Place
        self.petri_Place9 = petri_Place9
        
    @property
    def token(self) -> int:
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token

    @property
    def petri_Place9(self):
        return self.__petri_Place9

    @petri_Place9.setter
    def petri_Place9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Place__petri_Place9", None)
        self.__petri_Place9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_EdgeToPlace8"):
                opp_val = getattr(old_value, "petri_EdgeToPlace8", None)
                if opp_val == self:
                    setattr(old_value, "petri_EdgeToPlace8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_EdgeToPlace8"):
                opp_val = getattr(value, "petri_EdgeToPlace8", None)
                setattr(value, "petri_EdgeToPlace8", self)

    @property
    def petri_Place4(self):
        return self.__petri_Place4

    @petri_Place4.setter
    def petri_Place4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Place__petri_Place4", None)
        self.__petri_Place4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petri_EdgeToTransition"):
                    opp_val = getattr(item, "petri_EdgeToTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "petri_EdgeToTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petri_EdgeToTransition"):
                    opp_val = getattr(item, "petri_EdgeToTransition", None)
                    
                    setattr(item, "petri_EdgeToTransition", self)
                    

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
            if hasattr(old_value, "petri_PetriNet2"):
                opp_val = getattr(old_value, "petri_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_PetriNet2"):
                opp_val = getattr(value, "petri_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "petri_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petri_Transition:

    def __init__(self, token: int, petri_Transition6: set["petri_EdgeToPlace"] = None, petri_Transition: "petri_PetriNet" = None, petri_Transition12: "petri_EdgeToTransition" = None):
        self.token = token
        self.petri_Transition6 = petri_Transition6 if petri_Transition6 is not None else set()
        self.petri_Transition = petri_Transition
        self.petri_Transition12 = petri_Transition12
        
    @property
    def token(self) -> int:
        return self.__token

    @token.setter
    def token(self, token: int):
        self.__token = token

    @property
    def petri_Transition(self):
        return self.__petri_Transition

    @petri_Transition.setter
    def petri_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Transition__petri_Transition", None)
        self.__petri_Transition = value
        
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

    @property
    def petri_Transition12(self):
        return self.__petri_Transition12

    @petri_Transition12.setter
    def petri_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Transition__petri_Transition12", None)
        self.__petri_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_EdgeToTransition11"):
                opp_val = getattr(old_value, "petri_EdgeToTransition11", None)
                if opp_val == self:
                    setattr(old_value, "petri_EdgeToTransition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_EdgeToTransition11"):
                opp_val = getattr(value, "petri_EdgeToTransition11", None)
                setattr(value, "petri_EdgeToTransition11", self)

    @property
    def petri_Transition6(self):
        return self.__petri_Transition6

    @petri_Transition6.setter
    def petri_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Transition__petri_Transition6", None)
        self.__petri_Transition6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petri_EdgeToPlace"):
                    opp_val = getattr(item, "petri_EdgeToPlace", None)
                    
                    if opp_val == self:
                        setattr(item, "petri_EdgeToPlace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petri_EdgeToPlace"):
                    opp_val = getattr(item, "petri_EdgeToPlace", None)
                    
                    setattr(item, "petri_EdgeToPlace", self)
                    

class petri_EdgeToPlace(Edge):

    pass
class petri_EdgeToTransition(Edge):

    pass
class petri_PetriNet:

    pass