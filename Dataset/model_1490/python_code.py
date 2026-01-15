from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class GenericPlace:

    pass
class extendedPetriNets_OutputPort(GenericPlace):

    pass
class extendedPetriNets_InputPort(GenericPlace):

    pass
class extendedPetriNets_Place(GenericPlace):

    pass
class extendedPetriNets_OutputArc:

    def __init__(self, weight: int, extendedPetriNets_OutputArc: "extendedPetriNets_PetriNet" = None, extendedPetriNets_OutputArc15: "extendedPetriNets_Transition" = None, extendedPetriNets_OutputArc18: "extendedPetriNets_Place" = None, extendedPetriNets_OutputArc21: "extendedPetriNets_OutputPort" = None):
        self.weight = weight
        self.extendedPetriNets_OutputArc = extendedPetriNets_OutputArc
        self.extendedPetriNets_OutputArc15 = extendedPetriNets_OutputArc15
        self.extendedPetriNets_OutputArc18 = extendedPetriNets_OutputArc18
        self.extendedPetriNets_OutputArc21 = extendedPetriNets_OutputArc21
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

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
    def extendedPetriNets_OutputArc18(self):
        return self.__extendedPetriNets_OutputArc18

    @extendedPetriNets_OutputArc18.setter
    def extendedPetriNets_OutputArc18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_OutputArc__extendedPetriNets_OutputArc18", None)
        self.__extendedPetriNets_OutputArc18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_Place19"):
                opp_val = getattr(old_value, "extendedPetriNets_Place19", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_Place19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_Place19"):
                opp_val = getattr(value, "extendedPetriNets_Place19", None)
                setattr(value, "extendedPetriNets_Place19", self)

    @property
    def extendedPetriNets_OutputArc15(self):
        return self.__extendedPetriNets_OutputArc15

    @extendedPetriNets_OutputArc15.setter
    def extendedPetriNets_OutputArc15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_OutputArc__extendedPetriNets_OutputArc15", None)
        self.__extendedPetriNets_OutputArc15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_Transition16"):
                opp_val = getattr(old_value, "extendedPetriNets_Transition16", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_Transition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_Transition16"):
                opp_val = getattr(value, "extendedPetriNets_Transition16", None)
                setattr(value, "extendedPetriNets_Transition16", self)

    @property
    def extendedPetriNets_OutputArc21(self):
        return self.__extendedPetriNets_OutputArc21

    @extendedPetriNets_OutputArc21.setter
    def extendedPetriNets_OutputArc21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_OutputArc__extendedPetriNets_OutputArc21", None)
        self.__extendedPetriNets_OutputArc21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_OutputPort"):
                opp_val = getattr(old_value, "extendedPetriNets_OutputPort", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_OutputPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_OutputPort"):
                opp_val = getattr(value, "extendedPetriNets_OutputPort", None)
                setattr(value, "extendedPetriNets_OutputPort", self)

class extendedPetriNets_InputArc:

    def __init__(self, weight: int, extendedPetriNets_InputArc: "extendedPetriNets_PetriNet" = None, extendedPetriNets_InputArc8: "extendedPetriNets_Transition" = None, extendedPetriNets_InputArc11: "extendedPetriNets_Place" = None, extendedPetriNets_InputArc13: "extendedPetriNets_InputPort" = None):
        self.weight = weight
        self.extendedPetriNets_InputArc = extendedPetriNets_InputArc
        self.extendedPetriNets_InputArc8 = extendedPetriNets_InputArc8
        self.extendedPetriNets_InputArc11 = extendedPetriNets_InputArc11
        self.extendedPetriNets_InputArc13 = extendedPetriNets_InputArc13
        
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
            if hasattr(old_value, "extendedPetriNets_Place"):
                opp_val = getattr(old_value, "extendedPetriNets_Place", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_Place"):
                opp_val = getattr(value, "extendedPetriNets_Place", None)
                setattr(value, "extendedPetriNets_Place", self)

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

    @property
    def extendedPetriNets_InputArc13(self):
        return self.__extendedPetriNets_InputArc13

    @extendedPetriNets_InputArc13.setter
    def extendedPetriNets_InputArc13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_InputArc__extendedPetriNets_InputArc13", None)
        self.__extendedPetriNets_InputArc13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_InputPort"):
                opp_val = getattr(old_value, "extendedPetriNets_InputPort", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_InputPort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_InputPort"):
                opp_val = getattr(value, "extendedPetriNets_InputPort", None)
                setattr(value, "extendedPetriNets_InputPort", self)

class extendedPetriNets_Transition:

    def __init__(self, name: str, extendedPetriNets_Transition: "extendedPetriNets_PetriNet" = None, extendedPetriNets_Transition9: "extendedPetriNets_InputArc" = None, extendedPetriNets_Transition16: "extendedPetriNets_OutputArc" = None):
        self.name = name
        self.extendedPetriNets_Transition = extendedPetriNets_Transition
        self.extendedPetriNets_Transition9 = extendedPetriNets_Transition9
        self.extendedPetriNets_Transition16 = extendedPetriNets_Transition16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extendedPetriNets_Transition16(self):
        return self.__extendedPetriNets_Transition16

    @extendedPetriNets_Transition16.setter
    def extendedPetriNets_Transition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedPetriNets_Transition__extendedPetriNets_Transition16", None)
        self.__extendedPetriNets_Transition16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedPetriNets_OutputArc15"):
                opp_val = getattr(old_value, "extendedPetriNets_OutputArc15", None)
                if opp_val == self:
                    setattr(old_value, "extendedPetriNets_OutputArc15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedPetriNets_OutputArc15"):
                opp_val = getattr(value, "extendedPetriNets_OutputArc15", None)
                setattr(value, "extendedPetriNets_OutputArc15", self)

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

class extendedPetriNets_GenericPlace(ABC):

    def __init__(self, name: str, capacity: int, numberOfTokens: int, extendedPetriNets_GenericPlace: "extendedPetriNets_PetriNet" = None):
        self.name = name
        self.capacity = capacity
        self.numberOfTokens = numberOfTokens
        self.extendedPetriNets_GenericPlace = extendedPetriNets_GenericPlace
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numberOfTokens(self) -> int:
        return self.__numberOfTokens

    @numberOfTokens.setter
    def numberOfTokens(self, numberOfTokens: int):
        self.__numberOfTokens = numberOfTokens

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

class extendedPetriNets_PetriNet:

    def __init__(self, name: str, extendedPetriNets_PetriNet: set["extendedPetriNets_GenericPlace"] = None, extendedPetriNets_PetriNet2: set["extendedPetriNets_Transition"] = None, extendedPetriNets_PetriNet4: set["extendedPetriNets_InputArc"] = None, extendedPetriNets_PetriNet6: set["extendedPetriNets_OutputArc"] = None):
        self.name = name
        self.extendedPetriNets_PetriNet = extendedPetriNets_PetriNet if extendedPetriNets_PetriNet is not None else set()
        self.extendedPetriNets_PetriNet2 = extendedPetriNets_PetriNet2 if extendedPetriNets_PetriNet2 is not None else set()
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
                    
