from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArcType(Enum):
    Arc = "Arc"
    ReadArc = "ReadArc"


############################################
# Definition of Classes
############################################

class PetriNet_PetriNet:

    def __init__(self, name: str, PetriNet_PetriNet: set["PetriNet_Arc"] = None, PetriNet_PetriNet7: set["PetriNet_PetriElement"] = None):
        self.name = name
        self.PetriNet_PetriNet = PetriNet_PetriNet if PetriNet_PetriNet is not None else set()
        self.PetriNet_PetriNet7 = PetriNet_PetriNet7 if PetriNet_PetriNet7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_PetriNet7(self):
        return self.__PetriNet_PetriNet7

    @PetriNet_PetriNet7.setter
    def PetriNet_PetriNet7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__PetriNet_PetriNet7", None)
        self.__PetriNet_PetriNet7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_PetriElement8"):
                    opp_val = getattr(item, "PetriNet_PetriElement8", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_PetriElement8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_PetriElement8"):
                    opp_val = getattr(item, "PetriNet_PetriElement8", None)
                    
                    setattr(item, "PetriNet_PetriElement8", self)
                    

    @property
    def PetriNet_PetriNet(self):
        return self.__PetriNet_PetriNet

    @PetriNet_PetriNet.setter
    def PetriNet_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__PetriNet_PetriNet", None)
        self.__PetriNet_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_Arc5"):
                    opp_val = getattr(item, "PetriNet_Arc5", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_Arc5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_Arc5"):
                    opp_val = getattr(item, "PetriNet_Arc5", None)
                    
                    setattr(item, "PetriNet_Arc5", self)
                    

class PetriNet_PetriElement:

    def __init__(self, nom: str, PetriNet_PetriElement: "PetriNet_Arc" = None, PetriNet_PetriElement3: "PetriNet_Arc" = None, PetriNet_PetriElement8: "PetriNet_PetriNet" = None):
        self.nom = nom
        self.PetriNet_PetriElement = PetriNet_PetriElement
        self.PetriNet_PetriElement3 = PetriNet_PetriElement3
        self.PetriNet_PetriElement8 = PetriNet_PetriElement8
        
    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def PetriNet_PetriElement(self):
        return self.__PetriNet_PetriElement

    @PetriNet_PetriElement.setter
    def PetriNet_PetriElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriElement__PetriNet_PetriElement", None)
        self.__PetriNet_PetriElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Arc"):
                opp_val = getattr(old_value, "PetriNet_Arc", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Arc"):
                opp_val = getattr(value, "PetriNet_Arc", None)
                setattr(value, "PetriNet_Arc", self)

    @property
    def PetriNet_PetriElement3(self):
        return self.__PetriNet_PetriElement3

    @PetriNet_PetriElement3.setter
    def PetriNet_PetriElement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriElement__PetriNet_PetriElement3", None)
        self.__PetriNet_PetriElement3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Arc2"):
                opp_val = getattr(old_value, "PetriNet_Arc2", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_Arc2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Arc2"):
                opp_val = getattr(value, "PetriNet_Arc2", None)
                setattr(value, "PetriNet_Arc2", self)

    @property
    def PetriNet_PetriElement8(self):
        return self.__PetriNet_PetriElement8

    @PetriNet_PetriElement8.setter
    def PetriNet_PetriElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriElement__PetriNet_PetriElement8", None)
        self.__PetriNet_PetriElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNet7"):
                opp_val = getattr(old_value, "PetriNet_PetriNet7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNet7"):
                opp_val = getattr(value, "PetriNet_PetriNet7", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNet7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNet_Arc:

    def __init__(self, poids: int, arcType: str, PetriNet_Arc: "PetriNet_PetriElement" = None, PetriNet_Arc2: "PetriNet_PetriElement" = None, PetriNet_Arc5: "PetriNet_PetriNet" = None):
        self.poids = poids
        self.arcType = arcType
        self.PetriNet_Arc = PetriNet_Arc
        self.PetriNet_Arc2 = PetriNet_Arc2
        self.PetriNet_Arc5 = PetriNet_Arc5
        
    @property
    def arcType(self) -> str:
        return self.__arcType

    @arcType.setter
    def arcType(self, arcType: str):
        self.__arcType = arcType

    @property
    def poids(self) -> int:
        return self.__poids

    @poids.setter
    def poids(self, poids: int):
        self.__poids = poids

    @property
    def PetriNet_Arc2(self):
        return self.__PetriNet_Arc2

    @PetriNet_Arc2.setter
    def PetriNet_Arc2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__PetriNet_Arc2", None)
        self.__PetriNet_Arc2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriElement3"):
                opp_val = getattr(old_value, "PetriNet_PetriElement3", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_PetriElement3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriElement3"):
                opp_val = getattr(value, "PetriNet_PetriElement3", None)
                setattr(value, "PetriNet_PetriElement3", self)

    @property
    def PetriNet_Arc(self):
        return self.__PetriNet_Arc

    @PetriNet_Arc.setter
    def PetriNet_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__PetriNet_Arc", None)
        self.__PetriNet_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriElement"):
                opp_val = getattr(old_value, "PetriNet_PetriElement", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_PetriElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriElement"):
                opp_val = getattr(value, "PetriNet_PetriElement", None)
                setattr(value, "PetriNet_PetriElement", self)

    @property
    def PetriNet_Arc5(self):
        return self.__PetriNet_Arc5

    @PetriNet_Arc5.setter
    def PetriNet_Arc5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__PetriNet_Arc5", None)
        self.__PetriNet_Arc5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNet"):
                opp_val = getattr(old_value, "PetriNet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNet"):
                opp_val = getattr(value, "PetriNet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriElement:

    pass
class PetriNet_Transition(PetriElement):

    pass
class PetriNet_Place(PetriElement):

    def __init__(self, nbJetons: int):
        self.nbJetons = nbJetons
        
    @property
    def nbJetons(self) -> int:
        return self.__nbJetons

    @nbJetons.setter
    def nbJetons(self, nbJetons: int):
        self.__nbJetons = nbJetons
