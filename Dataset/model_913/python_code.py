from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet_PetriElement(ABC):

    pass
class PetriNet_ReseauPetri:

    def __init__(self, name: str, PetriNet_ReseauPetri: set["PetriNet_PetriElement"] = None, PetriNet_ReseauPetri6: "PetriNet_PetriElement" = None):
        self.name = name
        self.PetriNet_ReseauPetri = PetriNet_ReseauPetri if PetriNet_ReseauPetri is not None else set()
        self.PetriNet_ReseauPetri6 = PetriNet_ReseauPetri6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_ReseauPetri6(self):
        return self.__PetriNet_ReseauPetri6

    @PetriNet_ReseauPetri6.setter
    def PetriNet_ReseauPetri6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_ReseauPetri__PetriNet_ReseauPetri6", None)
        self.__PetriNet_ReseauPetri6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriElement5"):
                opp_val = getattr(old_value, "PetriNet_PetriElement5", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_PetriElement5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriElement5"):
                opp_val = getattr(value, "PetriNet_PetriElement5", None)
                setattr(value, "PetriNet_PetriElement5", self)

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
                if hasattr(item, "PetriNet_PetriElement"):
                    opp_val = getattr(item, "PetriNet_PetriElement", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_PetriElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_PetriElement"):
                    opp_val = getattr(item, "PetriNet_PetriElement", None)
                    
                    setattr(item, "PetriNet_PetriElement", self)
                    

class PetriElement:

    pass
class PetriNet_Noeud(PetriElement):

    def __init__(self, name: str, successor: set["PetriNet_Arc"] = None, predecessor: set["PetriNet_Arc"] = None, Noeud: "PetriNet_Arc" = None, Noeud2: "PetriNet_Arc" = None):
        self.name = name
        self.successor = successor if successor is not None else set()
        self.predecessor = predecessor if predecessor is not None else set()
        self.Noeud = Noeud
        self.Noeud2 = Noeud2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Noeud(self):
        return self.__Noeud

    @Noeud.setter
    def Noeud(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Noeud__Noeud", None)
        self.__Noeud = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linksToPredecessors"):
                opp_val = getattr(old_value, "linksToPredecessors", None)
                if opp_val == self:
                    setattr(old_value, "linksToPredecessors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linksToPredecessors"):
                opp_val = getattr(value, "linksToPredecessors", None)
                setattr(value, "linksToPredecessors", self)

    @property
    def Noeud2(self):
        return self.__Noeud2

    @Noeud2.setter
    def Noeud2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Noeud__Noeud2", None)
        self.__Noeud2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LinksToSuccessors"):
                opp_val = getattr(old_value, "LinksToSuccessors", None)
                if opp_val == self:
                    setattr(old_value, "LinksToSuccessors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LinksToSuccessors"):
                opp_val = getattr(value, "LinksToSuccessors", None)
                setattr(value, "LinksToSuccessors", self)

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Noeud__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc9"):
                    opp_val = getattr(item, "Arc9", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc9"):
                    opp_val = getattr(item, "Arc9", None)
                    
                    setattr(item, "Arc9", self)
                    

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Noeud__successor", None)
        self.__successor = value if value is not None else set()
        
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
                    

class PetriNet_Arc(PetriElement):

    def __init__(self, isReadArc: bool, poids: int, Arc: "PetriNet_Noeud" = None, Arc9: "PetriNet_Noeud" = None, linksToPredecessors: "PetriNet_Noeud" = None, LinksToSuccessors: "PetriNet_Noeud" = None):
        self.isReadArc = isReadArc
        self.poids = poids
        self.Arc = Arc
        self.Arc9 = Arc9
        self.linksToPredecessors = linksToPredecessors
        self.LinksToSuccessors = LinksToSuccessors
        
    @property
    def poids(self) -> int:
        return self.__poids

    @poids.setter
    def poids(self, poids: int):
        self.__poids = poids

    @property
    def isReadArc(self) -> bool:
        return self.__isReadArc

    @isReadArc.setter
    def isReadArc(self, isReadArc: bool):
        self.__isReadArc = isReadArc

    @property
    def LinksToSuccessors(self):
        return self.__LinksToSuccessors

    @LinksToSuccessors.setter
    def LinksToSuccessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__LinksToSuccessors", None)
        self.__LinksToSuccessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Noeud2"):
                opp_val = getattr(old_value, "Noeud2", None)
                if opp_val == self:
                    setattr(old_value, "Noeud2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Noeud2"):
                opp_val = getattr(value, "Noeud2", None)
                setattr(value, "Noeud2", self)

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successor"):
                opp_val = getattr(old_value, "successor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successor"):
                opp_val = getattr(value, "successor", None)
                if opp_val is None:
                    setattr(value, "successor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc9(self):
        return self.__Arc9

    @Arc9.setter
    def Arc9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__Arc9", None)
        self.__Arc9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecessor"):
                opp_val = getattr(old_value, "predecessor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecessor"):
                opp_val = getattr(value, "predecessor", None)
                if opp_val is None:
                    setattr(value, "predecessor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linksToPredecessors(self):
        return self.__linksToPredecessors

    @linksToPredecessors.setter
    def linksToPredecessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__linksToPredecessors", None)
        self.__linksToPredecessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Noeud"):
                opp_val = getattr(old_value, "Noeud", None)
                if opp_val == self:
                    setattr(old_value, "Noeud", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Noeud"):
                opp_val = getattr(value, "Noeud", None)
                setattr(value, "Noeud", self)

class Noeud:

    pass
class PetriNet_Transition(Noeud):

    pass
class PetriNet_Place(Noeud):

    def __init__(self, jeton: int):
        self.jeton = jeton
        
    @property
    def jeton(self) -> int:
        return self.__jeton

    @jeton.setter
    def jeton(self, jeton: int):
        self.__jeton = jeton
