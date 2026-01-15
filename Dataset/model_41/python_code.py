from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class GenericPlace:

    pass
class extendedPetriNets_InputPort(GenericPlace):

    pass
class extendedPetriNets_Place(GenericPlace):

    pass
class extendedPetriNets_OutputArc:

    def __init__(self, weight: int, extendedPetriNets_OutputArc17: "extendedPetriNets_GenericPlace" = None, extendedPetriNets_OutputArc: "extendedPetriNets_PetriNet" = None, extendedPetriNets_OutputArc14: "extendedPetriNets_Transition" = None):
        self.weight = weight
        self.extendedPetriNets_OutputArc17 = extendedPetriNets_OutputArc17
        self.extendedPetriNets_OutputArc = extendedPetriNets_OutputArc
        self.extendedPetriNets_OutputArc14 = extendedPetriNets_OutputArc14
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def extendedPetriNets_OutputArc14(self):
        return self.__extendedPetriNets_OutputArc14

    @extendedPetriNets_OutputArc14.setter
    def extendedPetriNets_OutputArc14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_OutputArc__extendedPetriNets_OutputArc14", None)
        self.__extendedPetriNets_OutputArc14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_Transition15"):
                opp_val = getattr(old_value, "extendedPetriNets_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_Transition15"):
                opp_val = getattr(value, "extendedPetriNets_Transition15", None)
                setattr(value, "extendedPetriNets_Transition15", self)

    @property
    def extendedPetriNets_OutputArc(self):
        return self.__extendedPetriNets_OutputArc

    @extendedPetriNets_OutputArc.setter
    def extendedPetriNets_OutputArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_OutputArc__extendedPetriNets_OutputArc", None)
        self.__extendedPetriNets_OutputArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_PetriNet6"):
                opp_val = getattr(old_value, "extendedPetriNets_PetriNet6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_PetriNet6"):
                opp_val = getattr(value, "extendedPetriNets_PetriNet6", None)
                if opp_val is None:
                    setattr(value, "extendedPetriNets_PetriNet6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extendedPetriNets_OutputArc17(self):
        return self.__extendedPetriNets_OutputArc17

    @extendedPetriNets_OutputArc17.setter
    def extendedPetriNets_OutputArc17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_OutputArc__extendedPetriNets_OutputArc17", None)
        self.__extendedPetriNets_OutputArc17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_GenericPlace18"):
                opp_val = getattr(old_value, "extendedPetriNets_GenericPlace18", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_GenericPlace18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_GenericPlace18"):
                opp_val = getattr(value, "extendedPetriNets_GenericPlace18", None)
                setattr(value, "extendedPetriNets_GenericPlace18", self)

class extendedPetriNets_OutputPort(GenericPlace):

    pass
class extendedPetriNets_GenericPlace(ABC):

    def __init__(self, name: str, capacity: int, numberOfTokens: int, extendedPetriNets_GenericPlace: "extendedPetriNets_PetriNet" = None, extendedPetriNets_GenericPlace18: "extendedPetriNets_OutputArc" = None, extendedPetriNets_GenericPlace12: "extendedPetriNets_InputArc" = None):
        self.name = name
        self.capacity = capacity
        self.numberOfTokens = numberOfTokens
        self.extendedPetriNets_GenericPlace = extendedPetriNets_GenericPlace
        self.extendedPetriNets_GenericPlace18 = extendedPetriNets_GenericPlace18
        self.extendedPetriNets_GenericPlace12 = extendedPetriNets_GenericPlace12
        
    @property
    def numberOfTokens(self) -> int:
        return self.__numberOfTokens

    @numberOfTokens.setter
    def numberOfTokens(self, numberOfTokens: int):
        self.__numberOfTokens = numberOfTokens

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def extendedPetriNets_GenericPlace(self):
        return self.__extendedPetriNets_GenericPlace

    @extendedPetriNets_GenericPlace.setter
    def extendedPetriNets_GenericPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_GenericPlace__extendedPetriNets_GenericPlace", None)
        self.__extendedPetriNets_GenericPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_PetriNet"):
                opp_val = getattr(old_value, "extendedPetriNets_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_PetriNet"):
                opp_val = getattr(value, "extendedPetriNets_PetriNet", None)
                if opp_val is None:
                    setattr(value, "extendedPetriNets_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extendedPetriNets_GenericPlace18(self):
        return self.__extendedPetriNets_GenericPlace18

    @extendedPetriNets_GenericPlace18.setter
    def extendedPetriNets_GenericPlace18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_GenericPlace__extendedPetriNets_GenericPlace18", None)
        self.__extendedPetriNets_GenericPlace18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_OutputArc17"):
                opp_val = getattr(old_value, "extendedPetriNets_OutputArc17", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_OutputArc17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_OutputArc17"):
                opp_val = getattr(value, "extendedPetriNets_OutputArc17", None)
                setattr(value, "extendedPetriNets_OutputArc17", self)

    @property
    def extendedPetriNets_GenericPlace12(self):
        return self.__extendedPetriNets_GenericPlace12

    @extendedPetriNets_GenericPlace12.setter
    def extendedPetriNets_GenericPlace12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_GenericPlace__extendedPetriNets_GenericPlace12", None)
        self.__extendedPetriNets_GenericPlace12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_InputArc11"):
                opp_val = getattr(old_value, "extendedPetriNets_InputArc11", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_InputArc11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_InputArc11"):
                opp_val = getattr(value, "extendedPetriNets_InputArc11", None)
                setattr(value, "extendedPetriNets_InputArc11", self)

class extendedPetriNets_PetriNet:

    def __init__(self, name: str, extendedPetriNets_PetriNet2: set["extendedPetriNets_Transition"] = None, extendedPetriNets_PetriNet: set["extendedPetriNets_GenericPlace"] = None, extendedPetriNets_PetriNet4: set["extendedPetriNets_InputArc"] = None, extendedPetriNets_PetriNet6: set["extendedPetriNets_OutputArc"] = None):
        self.name = name
        self.extendedPetriNets_PetriNet2 = extendedPetriNets_PetriNet2 if extendedPetriNets_PetriNet2 is not None else set()
        self.extendedPetriNets_PetriNet = extendedPetriNets_PetriNet if extendedPetriNets_PetriNet is not None else set()
        self.extendedPetriNets_PetriNet4 = extendedPetriNets_PetriNet4 if extendedPetriNets_PetriNet4 is not None else set()
        self.extendedPetriNets_PetriNet6 = extendedPetriNets_PetriNet6 if extendedPetriNets_PetriNet6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extendedPetriNets_PetriNet2(self):
        return self.__extendedPetriNets_PetriNet2

    @extendedPetriNets_PetriNet2.setter
    def extendedPetriNets_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_PetriNet__extendedPetriNets_PetriNet2", None)
        self.__extendedPetriNets_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extendedPetriNets_Transition"):
                    opp_val = getattr(item, "extendedPetriNets_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "extendedPetriNets_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extendedPetriNets_Transition"):
                    opp_val = getattr(item, "extendedPetriNets_Transition", None)
                    
                    setattr(item, "extendedPetriNets_Transition", self)
                    

    @property
    def extendedPetriNets_PetriNet(self):
        return self.__extendedPetriNets_PetriNet

    @extendedPetriNets_PetriNet.setter
    def extendedPetriNets_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_PetriNet__extendedPetriNets_PetriNet", None)
        self.__extendedPetriNets_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extendedPetriNets_GenericPlace"):
                    opp_val = getattr(item, "extendedPetriNets_GenericPlace", None)
                    
                    if opp_val == self:
                        setattr(item, "extendedPetriNets_GenericPlace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extendedPetriNets_GenericPlace"):
                    opp_val = getattr(item, "extendedPetriNets_GenericPlace", None)
                    
                    setattr(item, "extendedPetriNets_GenericPlace", self)
                    

    @property
    def extendedPetriNets_PetriNet6(self):
        return self.__extendedPetriNets_PetriNet6

    @extendedPetriNets_PetriNet6.setter
    def extendedPetriNets_PetriNet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_PetriNet__extendedPetriNets_PetriNet6", None)
        self.__extendedPetriNets_PetriNet6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extendedPetriNets_OutputArc"):
                    opp_val = getattr(item, "extendedPetriNets_OutputArc", None)
                    
                    if opp_val == self:
                        setattr(item, "extendedPetriNets_OutputArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extendedPetriNets_OutputArc"):
                    opp_val = getattr(item, "extendedPetriNets_OutputArc", None)
                    
                    setattr(item, "extendedPetriNets_OutputArc", self)
                    

    @property
    def extendedPetriNets_PetriNet4(self):
        return self.__extendedPetriNets_PetriNet4

    @extendedPetriNets_PetriNet4.setter
    def extendedPetriNets_PetriNet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_PetriNet__extendedPetriNets_PetriNet4", None)
        self.__extendedPetriNets_PetriNet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extendedPetriNets_InputArc"):
                    opp_val = getattr(item, "extendedPetriNets_InputArc", None)
                    
                    if opp_val == self:
                        setattr(item, "extendedPetriNets_InputArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extendedPetriNets_InputArc"):
                    opp_val = getattr(item, "extendedPetriNets_InputArc", None)
                    
                    setattr(item, "extendedPetriNets_InputArc", self)
                    

class extendedPetriNets_InputArc:

    def __init__(self, weight: int, extendedPetriNets_InputArc: "extendedPetriNets_PetriNet" = None, extendedPetriNets_InputArc8: "extendedPetriNets_Transition" = None, extendedPetriNets_InputArc11: "extendedPetriNets_GenericPlace" = None):
        self.weight = weight
        self.extendedPetriNets_InputArc = extendedPetriNets_InputArc
        self.extendedPetriNets_InputArc8 = extendedPetriNets_InputArc8
        self.extendedPetriNets_InputArc11 = extendedPetriNets_InputArc11
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def extendedPetriNets_InputArc11(self):
        return self.__extendedPetriNets_InputArc11

    @extendedPetriNets_InputArc11.setter
    def extendedPetriNets_InputArc11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_InputArc__extendedPetriNets_InputArc11", None)
        self.__extendedPetriNets_InputArc11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_GenericPlace12"):
                opp_val = getattr(old_value, "extendedPetriNets_GenericPlace12", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_GenericPlace12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_GenericPlace12"):
                opp_val = getattr(value, "extendedPetriNets_GenericPlace12", None)
                setattr(value, "extendedPetriNets_GenericPlace12", self)

    @property
    def extendedPetriNets_InputArc8(self):
        return self.__extendedPetriNets_InputArc8

    @extendedPetriNets_InputArc8.setter
    def extendedPetriNets_InputArc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_InputArc__extendedPetriNets_InputArc8", None)
        self.__extendedPetriNets_InputArc8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_Transition9"):
                opp_val = getattr(old_value, "extendedPetriNets_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_Transition9"):
                opp_val = getattr(value, "extendedPetriNets_Transition9", None)
                setattr(value, "extendedPetriNets_Transition9", self)

    @property
    def extendedPetriNets_InputArc(self):
        return self.__extendedPetriNets_InputArc

    @extendedPetriNets_InputArc.setter
    def extendedPetriNets_InputArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_InputArc__extendedPetriNets_InputArc", None)
        self.__extendedPetriNets_InputArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_PetriNet4"):
                opp_val = getattr(old_value, "extendedPetriNets_PetriNet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_PetriNet4"):
                opp_val = getattr(value, "extendedPetriNets_PetriNet4", None)
                if opp_val is None:
                    setattr(value, "extendedPetriNets_PetriNet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class extendedPetriNets_Transition:

    def __init__(self, name: str, extendedPetriNets_Transition: "extendedPetriNets_PetriNet" = None, extendedPetriNets_Transition9: "extendedPetriNets_InputArc" = None, extendedPetriNets_Transition15: "extendedPetriNets_OutputArc" = None):
        self.name = name
        self.extendedPetriNets_Transition = extendedPetriNets_Transition
        self.extendedPetriNets_Transition9 = extendedPetriNets_Transition9
        self.extendedPetriNets_Transition15 = extendedPetriNets_Transition15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extendedPetriNets_Transition(self):
        return self.__extendedPetriNets_Transition

    @extendedPetriNets_Transition.setter
    def extendedPetriNets_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_Transition__extendedPetriNets_Transition", None)
        self.__extendedPetriNets_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_PetriNet2"):
                opp_val = getattr(old_value, "extendedPetriNets_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_PetriNet2"):
                opp_val = getattr(value, "extendedPetriNets_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "extendedPetriNets_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extendedPetriNets_Transition9(self):
        return self.__extendedPetriNets_Transition9

    @extendedPetriNets_Transition9.setter
    def extendedPetriNets_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_Transition__extendedPetriNets_Transition9", None)
        self.__extendedPetriNets_Transition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_InputArc8"):
                opp_val = getattr(old_value, "extendedPetriNets_InputArc8", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_InputArc8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_InputArc8"):
                opp_val = getattr(value, "extendedPetriNets_InputArc8", None)
                setattr(value, "extendedPetriNets_InputArc8", self)

    @property
    def extendedPetriNets_Transition15(self):
        return self.__extendedPetriNets_Transition15

    @extendedPetriNets_Transition15.setter
    def extendedPetriNets_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_Transition__extendedPetriNets_Transition15", None)
        self.__extendedPetriNets_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_OutputArc14"):
                opp_val = getattr(old_value, "extendedPetriNets_OutputArc14", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_OutputArc14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_OutputArc14"):
                opp_val = getattr(value, "extendedPetriNets_OutputArc14", None)
                setattr(value, "extendedPetriNets_OutputArc14", self)
