from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArcDirection(Enum):
    P2T = "P2T"
    T2P = "T2P"


############################################
# Definition of Classes
############################################

class petriNet_PetriNetwork:

    def __init__(self, name: str, petriNet_PetriNetwork: set["petriNet_PetriElement"] = None):
        self.name = name
        self.petriNet_PetriNetwork = petriNet_PetriNetwork if petriNet_PetriNetwork is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petriNet_PetriNetwork(self):
        return self.__petriNet_PetriNetwork

    @petriNet_PetriNetwork.setter
    def petriNet_PetriNetwork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_PetriNetwork__petriNet_PetriNetwork", None)
        self.__petriNet_PetriNetwork = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNet_PetriElement"):
                    opp_val = getattr(item, "petriNet_PetriElement", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNet_PetriElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNet_PetriElement"):
                    opp_val = getattr(item, "petriNet_PetriElement", None)
                    
                    setattr(item, "petriNet_PetriElement", self)
                    

class PetriElement:

    pass
class petriNet_Arc(PetriElement):

    def __init__(self, jetonsTransferes: int, Direction: str, petriNet_Arc5: "petriNet_Place" = None, petriNet_Arc8: "petriNet_Place" = None, petriNet_Arc10: "petriNet_Transition" = None, petriNet_Arc: "petriNet_Transition" = None, petriNet_Arc3: "petriNet_Transition" = None, petriNet_Arc13: "petriNet_Place" = None):
        self.jetonsTransferes = jetonsTransferes
        self.Direction = Direction
        self.petriNet_Arc5 = petriNet_Arc5
        self.petriNet_Arc8 = petriNet_Arc8
        self.petriNet_Arc10 = petriNet_Arc10
        self.petriNet_Arc = petriNet_Arc
        self.petriNet_Arc3 = petriNet_Arc3
        self.petriNet_Arc13 = petriNet_Arc13
        
    @property
    def jetonsTransferes(self) -> int:
        return self.__jetonsTransferes

    @jetonsTransferes.setter
    def jetonsTransferes(self, jetonsTransferes: int):
        self.__jetonsTransferes = jetonsTransferes

    @property
    def Direction(self) -> str:
        return self.__Direction

    @Direction.setter
    def Direction(self, Direction: str):
        self.__Direction = Direction

    @property
    def petriNet_Arc13(self):
        return self.__petriNet_Arc13

    @petriNet_Arc13.setter
    def petriNet_Arc13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Arc__petriNet_Arc13", None)
        self.__petriNet_Arc13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Place14"):
                opp_val = getattr(old_value, "petriNet_Place14", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_Place14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Place14"):
                opp_val = getattr(value, "petriNet_Place14", None)
                setattr(value, "petriNet_Place14", self)

    @property
    def petriNet_Arc10(self):
        return self.__petriNet_Arc10

    @petriNet_Arc10.setter
    def petriNet_Arc10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Arc__petriNet_Arc10", None)
        self.__petriNet_Arc10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Transition11"):
                opp_val = getattr(old_value, "petriNet_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Transition11"):
                opp_val = getattr(value, "petriNet_Transition11", None)
                setattr(value, "petriNet_Transition11", self)

    @property
    def petriNet_Arc8(self):
        return self.__petriNet_Arc8

    @petriNet_Arc8.setter
    def petriNet_Arc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Arc__petriNet_Arc8", None)
        self.__petriNet_Arc8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Place7"):
                opp_val = getattr(old_value, "petriNet_Place7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Place7"):
                opp_val = getattr(value, "petriNet_Place7", None)
                if opp_val is None:
                    setattr(value, "petriNet_Place7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petriNet_Arc5(self):
        return self.__petriNet_Arc5

    @petriNet_Arc5.setter
    def petriNet_Arc5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Arc__petriNet_Arc5", None)
        self.__petriNet_Arc5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Place"):
                opp_val = getattr(old_value, "petriNet_Place", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Place"):
                opp_val = getattr(value, "petriNet_Place", None)
                if opp_val is None:
                    setattr(value, "petriNet_Place", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petriNet_Arc3(self):
        return self.__petriNet_Arc3

    @petriNet_Arc3.setter
    def petriNet_Arc3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Arc__petriNet_Arc3", None)
        self.__petriNet_Arc3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Transition2"):
                opp_val = getattr(old_value, "petriNet_Transition2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Transition2"):
                opp_val = getattr(value, "petriNet_Transition2", None)
                if opp_val is None:
                    setattr(value, "petriNet_Transition2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petriNet_Arc(self):
        return self.__petriNet_Arc

    @petriNet_Arc.setter
    def petriNet_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Arc__petriNet_Arc", None)
        self.__petriNet_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Transition"):
                opp_val = getattr(old_value, "petriNet_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Transition"):
                opp_val = getattr(value, "petriNet_Transition", None)
                if opp_val is None:
                    setattr(value, "petriNet_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petriNet_Transition(PetriElement):

    def __init__(self, petriNet_Transition11: "petriNet_Arc" = None, petriNet_Transition: set["petriNet_Arc"] = None, petriNet_Transition2: set["petriNet_Arc"] = None):
        self.petriNet_Transition11 = petriNet_Transition11
        self.petriNet_Transition = petriNet_Transition if petriNet_Transition is not None else set()
        self.petriNet_Transition2 = petriNet_Transition2 if petriNet_Transition2 is not None else set()
        
    @property
    def petriNet_Transition(self):
        return self.__petriNet_Transition

    @petriNet_Transition.setter
    def petriNet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Transition__petriNet_Transition", None)
        self.__petriNet_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNet_Arc"):
                    opp_val = getattr(item, "petriNet_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNet_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNet_Arc"):
                    opp_val = getattr(item, "petriNet_Arc", None)
                    
                    setattr(item, "petriNet_Arc", self)
                    

    @property
    def petriNet_Transition11(self):
        return self.__petriNet_Transition11

    @petriNet_Transition11.setter
    def petriNet_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Transition__petriNet_Transition11", None)
        self.__petriNet_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Arc10"):
                opp_val = getattr(old_value, "petriNet_Arc10", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_Arc10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Arc10"):
                opp_val = getattr(value, "petriNet_Arc10", None)
                setattr(value, "petriNet_Arc10", self)

    @property
    def petriNet_Transition2(self):
        return self.__petriNet_Transition2

    @petriNet_Transition2.setter
    def petriNet_Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Transition__petriNet_Transition2", None)
        self.__petriNet_Transition2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNet_Arc3"):
                    opp_val = getattr(item, "petriNet_Arc3", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNet_Arc3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNet_Arc3"):
                    opp_val = getattr(item, "petriNet_Arc3", None)
                    
                    setattr(item, "petriNet_Arc3", self)
                    

    def newOperation1(self):
        # TODO: Implement newOperation1 method
        pass

class petriNet_Place(PetriElement):

    def __init__(self, nbJetons: int, petriNet_Place: set["petriNet_Arc"] = None, petriNet_Place7: set["petriNet_Arc"] = None, petriNet_Place14: "petriNet_Arc" = None):
        self.nbJetons = nbJetons
        self.petriNet_Place = petriNet_Place if petriNet_Place is not None else set()
        self.petriNet_Place7 = petriNet_Place7 if petriNet_Place7 is not None else set()
        self.petriNet_Place14 = petriNet_Place14
        
    @property
    def nbJetons(self) -> int:
        return self.__nbJetons

    @nbJetons.setter
    def nbJetons(self, nbJetons: int):
        self.__nbJetons = nbJetons

    @property
    def petriNet_Place7(self):
        return self.__petriNet_Place7

    @petriNet_Place7.setter
    def petriNet_Place7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Place__petriNet_Place7", None)
        self.__petriNet_Place7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNet_Arc8"):
                    opp_val = getattr(item, "petriNet_Arc8", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNet_Arc8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNet_Arc8"):
                    opp_val = getattr(item, "petriNet_Arc8", None)
                    
                    setattr(item, "petriNet_Arc8", self)
                    

    @property
    def petriNet_Place14(self):
        return self.__petriNet_Place14

    @petriNet_Place14.setter
    def petriNet_Place14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Place__petriNet_Place14", None)
        self.__petriNet_Place14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Arc13"):
                opp_val = getattr(old_value, "petriNet_Arc13", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_Arc13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Arc13"):
                opp_val = getattr(value, "petriNet_Arc13", None)
                setattr(value, "petriNet_Arc13", self)

    @property
    def petriNet_Place(self):
        return self.__petriNet_Place

    @petriNet_Place.setter
    def petriNet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Place__petriNet_Place", None)
        self.__petriNet_Place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNet_Arc5"):
                    opp_val = getattr(item, "petriNet_Arc5", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNet_Arc5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNet_Arc5"):
                    opp_val = getattr(item, "petriNet_Arc5", None)
                    
                    setattr(item, "petriNet_Arc5", self)
                    

class petriNet_PetriElement(ABC):

    def __init__(self, name: str, petriNet_PetriElement: "petriNet_PetriNetwork" = None):
        self.name = name
        self.petriNet_PetriElement = petriNet_PetriElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petriNet_PetriElement(self):
        return self.__petriNet_PetriElement

    @petriNet_PetriElement.setter
    def petriNet_PetriElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_PetriElement__petriNet_PetriElement", None)
        self.__petriNet_PetriElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_PetriNetwork"):
                opp_val = getattr(old_value, "petriNet_PetriNetwork", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_PetriNetwork"):
                opp_val = getattr(value, "petriNet_PetriNetwork", None)
                if opp_val is None:
                    setattr(value, "petriNet_PetriNetwork", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
