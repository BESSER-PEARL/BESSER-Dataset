from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArcKindType(Enum):
    normal = "normal"
    read_arc = "read_arc"


############################################
# Definition of Classes
############################################

class Noeud:

    pass
class petrinet_Place(Noeud):

    def __init__(self, marking: int):
        self.marking = marking
        
    @property
    def marking(self) -> int:
        return self.__marking

    @marking.setter
    def marking(self, marking: int):
        self.__marking = marking

class petrinet_Transition(Noeud):

    def __init__(self, minTime: int, maxTime: int):
        self.minTime = minTime
        self.maxTime = maxTime
        
    @property
    def minTime(self) -> int:
        return self.__minTime

    @minTime.setter
    def minTime(self, minTime: int):
        self.__minTime = minTime

    @property
    def maxTime(self) -> int:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: int):
        self.__maxTime = maxTime

class petrinet_Arc:

    def __init__(self, name: str, arcType: str, weight: int, petrinet_Arc: "petrinet_PetriNet" = None, petrinet_Arc4: "petrinet_Noeud" = None, petrinet_Arc7: "petrinet_Noeud" = None):
        self.name = name
        self.arcType = arcType
        self.weight = weight
        self.petrinet_Arc = petrinet_Arc
        self.petrinet_Arc4 = petrinet_Arc4
        self.petrinet_Arc7 = petrinet_Arc7
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arcType(self) -> str:
        return self.__arcType

    @arcType.setter
    def arcType(self, arcType: str):
        self.__arcType = arcType

    @property
    def petrinet_Arc7(self):
        return self.__petrinet_Arc7

    @petrinet_Arc7.setter
    def petrinet_Arc7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc7", None)
        self.__petrinet_Arc7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Noeud8"):
                opp_val = getattr(old_value, "petrinet_Noeud8", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Noeud8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Noeud8"):
                opp_val = getattr(value, "petrinet_Noeud8", None)
                setattr(value, "petrinet_Noeud8", self)

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
            if hasattr(old_value, "petrinet_Noeud5"):
                opp_val = getattr(old_value, "petrinet_Noeud5", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Noeud5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Noeud5"):
                opp_val = getattr(value, "petrinet_Noeud5", None)
                setattr(value, "petrinet_Noeud5", self)

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
            if hasattr(old_value, "petrinet_PetriNet2"):
                opp_val = getattr(old_value, "petrinet_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet2"):
                opp_val = getattr(value, "petrinet_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_Noeud:

    def __init__(self, name: str, petrinet_Noeud: "petrinet_PetriNet" = None, petrinet_Noeud5: "petrinet_Arc" = None, petrinet_Noeud8: "petrinet_Arc" = None):
        self.name = name
        self.petrinet_Noeud = petrinet_Noeud
        self.petrinet_Noeud5 = petrinet_Noeud5
        self.petrinet_Noeud8 = petrinet_Noeud8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Noeud(self):
        return self.__petrinet_Noeud

    @petrinet_Noeud.setter
    def petrinet_Noeud(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Noeud__petrinet_Noeud", None)
        self.__petrinet_Noeud = value
        
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
    def petrinet_Noeud5(self):
        return self.__petrinet_Noeud5

    @petrinet_Noeud5.setter
    def petrinet_Noeud5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Noeud__petrinet_Noeud5", None)
        self.__petrinet_Noeud5 = value
        
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

    @property
    def petrinet_Noeud8(self):
        return self.__petrinet_Noeud8

    @petrinet_Noeud8.setter
    def petrinet_Noeud8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Noeud__petrinet_Noeud8", None)
        self.__petrinet_Noeud8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc7"):
                opp_val = getattr(old_value, "petrinet_Arc7", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc7"):
                opp_val = getattr(value, "petrinet_Arc7", None)
                setattr(value, "petrinet_Arc7", self)

class petrinet_PetriNet:

    def __init__(self, name: str, petrinet_PetriNet: set["petrinet_Noeud"] = None, petrinet_PetriNet2: set["petrinet_Arc"] = None):
        self.name = name
        self.petrinet_PetriNet = petrinet_PetriNet if petrinet_PetriNet is not None else set()
        self.petrinet_PetriNet2 = petrinet_PetriNet2 if petrinet_PetriNet2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_PetriNet2(self):
        return self.__petrinet_PetriNet2

    @petrinet_PetriNet2.setter
    def petrinet_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet2", None)
        self.__petrinet_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Arc"):
                    opp_val = getattr(item, "petrinet_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Arc"):
                    opp_val = getattr(item, "petrinet_Arc", None)
                    
                    setattr(item, "petrinet_Arc", self)
                    

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
                if hasattr(item, "petrinet_Noeud"):
                    opp_val = getattr(item, "petrinet_Noeud", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Noeud", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Noeud"):
                    opp_val = getattr(item, "petrinet_Noeud", None)
                    
                    setattr(item, "petrinet_Noeud", self)
                    
