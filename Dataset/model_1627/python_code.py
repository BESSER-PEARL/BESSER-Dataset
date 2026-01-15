from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NamedElement:

    pass
class petri_Transition(NamedElement):

    pass
class petri_Place(NamedElement):

    def __init__(self, tokens: int, petri_Place: "petri_Transition" = None, petri_Place4: "petri_Transition" = None):
        self.tokens = tokens
        self.petri_Place = petri_Place
        self.petri_Place4 = petri_Place4
        
    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def petri_Place4(self):
        return self.__petri_Place4

    @petri_Place4.setter
    def petri_Place4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_Place__petri_Place4", None)
        self.__petri_Place4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petri_Transition3"):
                opp_val = getattr(old_value, "petri_Transition3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_Transition3"):
                opp_val = getattr(value, "petri_Transition3", None)
                if opp_val is None:
                    setattr(value, "petri_Transition3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "petri_Transition"):
                opp_val = getattr(old_value, "petri_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petri_Transition"):
                opp_val = getattr(value, "petri_Transition", None)
                if opp_val is None:
                    setattr(value, "petri_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petri_NamedElement(ABC):

    def __init__(self, name: str, petri_NamedElement: "petri_PetriNet" = None):
        self.name = name
        self.petri_NamedElement = petri_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petri_NamedElement(self):
        return self.__petri_NamedElement

    @petri_NamedElement.setter
    def petri_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petri_NamedElement__petri_NamedElement", None)
        self.__petri_NamedElement = value
        
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

class petri_PetriNet:

    pass