from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArcType(Enum):
    Normal = "Normal"
    Read_arc = "Read_arc"


############################################
# Definition of Classes
############################################

class PetriNet_ReseauPetri:

    def __init__(self, name: str, PetriNet_ReseauPetri7: set["PetriNet_Arc"] = None, PetriNet_ReseauPetri: set["PetriNet_PetriElement"] = None):
        self.name = name
        self.PetriNet_ReseauPetri7 = PetriNet_ReseauPetri7 if PetriNet_ReseauPetri7 is not None else set()
        self.PetriNet_ReseauPetri = PetriNet_ReseauPetri if PetriNet_ReseauPetri is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_ReseauPetri7(self):
        return self.__PetriNet_ReseauPetri7

    @PetriNet_ReseauPetri7.setter
    def PetriNet_ReseauPetri7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_ReseauPetri__PetriNet_ReseauPetri7", None)
        self.__PetriNet_ReseauPetri7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_Arc8"):
                    opp_val = getattr(item, "PetriNet_Arc8", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_Arc8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_Arc8"):
                    opp_val = getattr(item, "PetriNet_Arc8", None)
                    
                    setattr(item, "PetriNet_Arc8", self)
                    

    @property
    def PetriNet_ReseauPetri(self):
        return self.__PetriNet_ReseauPetri

    @PetriNet_ReseauPetri.setter
    def PetriNet_ReseauPetri(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_ReseauPetri__PetriNet_ReseauPetri", None)
        self.__PetriNet_ReseauPetri = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_PetriElement5"):
                    opp_val = getattr(item, "PetriNet_PetriElement5", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_PetriElement5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_PetriElement5"):
                    opp_val = getattr(item, "PetriNet_PetriElement5", None)
                    
                    setattr(item, "PetriNet_PetriElement5", self)
                    

class PetriNet_PetriElement:

    def __init__(self, name: str, PetriNet_PetriElement3: "PetriNet_Arc" = None, PetriNet_PetriElement: "PetriNet_Arc" = None, PetriNet_PetriElement5: "PetriNet_ReseauPetri" = None):
        self.name = name
        self.PetriNet_PetriElement3 = PetriNet_PetriElement3
        self.PetriNet_PetriElement = PetriNet_PetriElement
        self.PetriNet_PetriElement5 = PetriNet_PetriElement5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def PetriNet_PetriElement5(self):
        return self.__PetriNet_PetriElement5

    @PetriNet_PetriElement5.setter
    def PetriNet_PetriElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriElement__PetriNet_PetriElement5", None)
        self.__PetriNet_PetriElement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_ReseauPetri"):
                opp_val = getattr(old_value, "PetriNet_ReseauPetri", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_ReseauPetri"):
                opp_val = getattr(value, "PetriNet_ReseauPetri", None)
                if opp_val is None:
                    setattr(value, "PetriNet_ReseauPetri", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class PetriNet_Arc:

    def __init__(self, type: str, poids: str, PetriNet_Arc2: "PetriNet_PetriElement" = None, PetriNet_Arc: "PetriNet_PetriElement" = None, PetriNet_Arc8: "PetriNet_ReseauPetri" = None):
        self.type = type
        self.poids = poids
        self.PetriNet_Arc2 = PetriNet_Arc2
        self.PetriNet_Arc = PetriNet_Arc
        self.PetriNet_Arc8 = PetriNet_Arc8
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def poids(self) -> str:
        return self.__poids

    @poids.setter
    def poids(self, poids: str):
        self.__poids = poids

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
    def PetriNet_Arc8(self):
        return self.__PetriNet_Arc8

    @PetriNet_Arc8.setter
    def PetriNet_Arc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__PetriNet_Arc8", None)
        self.__PetriNet_Arc8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_ReseauPetri7"):
                opp_val = getattr(old_value, "PetriNet_ReseauPetri7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_ReseauPetri7"):
                opp_val = getattr(value, "PetriNet_ReseauPetri7", None)
                if opp_val is None:
                    setattr(value, "PetriNet_ReseauPetri7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class PetriElement:

    pass
class PetriNet_Transition(PetriElement):

    pass
class PetriNet_Place(PetriElement):

    def __init__(self, borne: str, nbJeton: str):
        self.borne = borne
        self.nbJeton = nbJeton
        
    @property
    def nbJeton(self) -> str:
        return self.__nbJeton

    @nbJeton.setter
    def nbJeton(self, nbJeton: str):
        self.__nbJeton = nbJeton

    @property
    def borne(self) -> str:
        return self.__borne

    @borne.setter
    def borne(self, borne: str):
        self.__borne = borne
