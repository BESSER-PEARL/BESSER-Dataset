from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class resourcePetriNet_InputArc:

    def __init__(self, weight: int, resourcePetriNet_InputArc8: "resourcePetriNet_GenericPlace" = None, resourcePetriNet_InputArc: "resourcePetriNet_PetriNet" = None, resourcePetriNet_InputArc11: "resourcePetriNet_Transition" = None):
        self.weight = weight
        self.resourcePetriNet_InputArc8 = resourcePetriNet_InputArc8
        self.resourcePetriNet_InputArc = resourcePetriNet_InputArc
        self.resourcePetriNet_InputArc11 = resourcePetriNet_InputArc11
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def resourcePetriNet_InputArc11(self):
        return self.__resourcePetriNet_InputArc11

    @resourcePetriNet_InputArc11.setter
    def resourcePetriNet_InputArc11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_InputArc__resourcePetriNet_InputArc11", None)
        self.__resourcePetriNet_InputArc11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_Transition12"):
                opp_val = getattr(old_value, "resourcePetriNet_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "resourcePetriNet_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_Transition12"):
                opp_val = getattr(value, "resourcePetriNet_Transition12", None)
                setattr(value, "resourcePetriNet_Transition12", self)

    @property
    def resourcePetriNet_InputArc8(self):
        return self.__resourcePetriNet_InputArc8

    @resourcePetriNet_InputArc8.setter
    def resourcePetriNet_InputArc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_InputArc__resourcePetriNet_InputArc8", None)
        self.__resourcePetriNet_InputArc8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_GenericPlace9"):
                opp_val = getattr(old_value, "resourcePetriNet_GenericPlace9", None)
                if opp_val == self:
                    setattr(old_value, "resourcePetriNet_GenericPlace9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_GenericPlace9"):
                opp_val = getattr(value, "resourcePetriNet_GenericPlace9", None)
                setattr(value, "resourcePetriNet_GenericPlace9", self)

    @property
    def resourcePetriNet_InputArc(self):
        return self.__resourcePetriNet_InputArc

    @resourcePetriNet_InputArc.setter
    def resourcePetriNet_InputArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_InputArc__resourcePetriNet_InputArc", None)
        self.__resourcePetriNet_InputArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_PetriNet4"):
                opp_val = getattr(old_value, "resourcePetriNet_PetriNet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_PetriNet4"):
                opp_val = getattr(value, "resourcePetriNet_PetriNet4", None)
                if opp_val is None:
                    setattr(value, "resourcePetriNet_PetriNet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class resourcePetriNet_Transition:

    def __init__(self, name: str, resourcePetriNet_Transition: "resourcePetriNet_PetriNet" = None, resourcePetriNet_Transition12: "resourcePetriNet_InputArc" = None, resourcePetriNet_Transition15: "resourcePetriNet_OutputArc" = None):
        self.name = name
        self.resourcePetriNet_Transition = resourcePetriNet_Transition
        self.resourcePetriNet_Transition12 = resourcePetriNet_Transition12
        self.resourcePetriNet_Transition15 = resourcePetriNet_Transition15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def resourcePetriNet_Transition(self):
        return self.__resourcePetriNet_Transition

    @resourcePetriNet_Transition.setter
    def resourcePetriNet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_Transition__resourcePetriNet_Transition", None)
        self.__resourcePetriNet_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_PetriNet2"):
                opp_val = getattr(old_value, "resourcePetriNet_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_PetriNet2"):
                opp_val = getattr(value, "resourcePetriNet_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "resourcePetriNet_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def resourcePetriNet_Transition12(self):
        return self.__resourcePetriNet_Transition12

    @resourcePetriNet_Transition12.setter
    def resourcePetriNet_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_Transition__resourcePetriNet_Transition12", None)
        self.__resourcePetriNet_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_InputArc11"):
                opp_val = getattr(old_value, "resourcePetriNet_InputArc11", None)
                if opp_val == self:
                    setattr(old_value, "resourcePetriNet_InputArc11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_InputArc11"):
                opp_val = getattr(value, "resourcePetriNet_InputArc11", None)
                setattr(value, "resourcePetriNet_InputArc11", self)

    @property
    def resourcePetriNet_Transition15(self):
        return self.__resourcePetriNet_Transition15

    @resourcePetriNet_Transition15.setter
    def resourcePetriNet_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_Transition__resourcePetriNet_Transition15", None)
        self.__resourcePetriNet_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_OutputArc14"):
                opp_val = getattr(old_value, "resourcePetriNet_OutputArc14", None)
                if opp_val == self:
                    setattr(old_value, "resourcePetriNet_OutputArc14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_OutputArc14"):
                opp_val = getattr(value, "resourcePetriNet_OutputArc14", None)
                setattr(value, "resourcePetriNet_OutputArc14", self)

class resourcePetriNet_GenericPlace(ABC):

    def __init__(self, name: str, numberOfTokens: int, resourcePetriNet_GenericPlace9: "resourcePetriNet_InputArc" = None, resourcePetriNet_GenericPlace: "resourcePetriNet_PetriNet" = None, resourcePetriNet_GenericPlace18: "resourcePetriNet_OutputArc" = None):
        self.name = name
        self.numberOfTokens = numberOfTokens
        self.resourcePetriNet_GenericPlace9 = resourcePetriNet_GenericPlace9
        self.resourcePetriNet_GenericPlace = resourcePetriNet_GenericPlace
        self.resourcePetriNet_GenericPlace18 = resourcePetriNet_GenericPlace18
        
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
    def resourcePetriNet_GenericPlace(self):
        return self.__resourcePetriNet_GenericPlace

    @resourcePetriNet_GenericPlace.setter
    def resourcePetriNet_GenericPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_GenericPlace__resourcePetriNet_GenericPlace", None)
        self.__resourcePetriNet_GenericPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_PetriNet"):
                opp_val = getattr(old_value, "resourcePetriNet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_PetriNet"):
                opp_val = getattr(value, "resourcePetriNet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "resourcePetriNet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def resourcePetriNet_GenericPlace9(self):
        return self.__resourcePetriNet_GenericPlace9

    @resourcePetriNet_GenericPlace9.setter
    def resourcePetriNet_GenericPlace9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_GenericPlace__resourcePetriNet_GenericPlace9", None)
        self.__resourcePetriNet_GenericPlace9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_InputArc8"):
                opp_val = getattr(old_value, "resourcePetriNet_InputArc8", None)
                if opp_val == self:
                    setattr(old_value, "resourcePetriNet_InputArc8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_InputArc8"):
                opp_val = getattr(value, "resourcePetriNet_InputArc8", None)
                setattr(value, "resourcePetriNet_InputArc8", self)

    @property
    def resourcePetriNet_GenericPlace18(self):
        return self.__resourcePetriNet_GenericPlace18

    @resourcePetriNet_GenericPlace18.setter
    def resourcePetriNet_GenericPlace18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_GenericPlace__resourcePetriNet_GenericPlace18", None)
        self.__resourcePetriNet_GenericPlace18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_OutputArc17"):
                opp_val = getattr(old_value, "resourcePetriNet_OutputArc17", None)
                if opp_val == self:
                    setattr(old_value, "resourcePetriNet_OutputArc17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_OutputArc17"):
                opp_val = getattr(value, "resourcePetriNet_OutputArc17", None)
                setattr(value, "resourcePetriNet_OutputArc17", self)

class resourcePetriNet_PetriNet:

    def __init__(self, name: str, resourcePetriNet_PetriNet6: set["resourcePetriNet_OutputArc"] = None, resourcePetriNet_PetriNet: set["resourcePetriNet_GenericPlace"] = None, resourcePetriNet_PetriNet2: set["resourcePetriNet_Transition"] = None, resourcePetriNet_PetriNet4: set["resourcePetriNet_InputArc"] = None):
        self.name = name
        self.resourcePetriNet_PetriNet6 = resourcePetriNet_PetriNet6 if resourcePetriNet_PetriNet6 is not None else set()
        self.resourcePetriNet_PetriNet = resourcePetriNet_PetriNet if resourcePetriNet_PetriNet is not None else set()
        self.resourcePetriNet_PetriNet2 = resourcePetriNet_PetriNet2 if resourcePetriNet_PetriNet2 is not None else set()
        self.resourcePetriNet_PetriNet4 = resourcePetriNet_PetriNet4 if resourcePetriNet_PetriNet4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def resourcePetriNet_PetriNet(self):
        return self.__resourcePetriNet_PetriNet

    @resourcePetriNet_PetriNet.setter
    def resourcePetriNet_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_PetriNet__resourcePetriNet_PetriNet", None)
        self.__resourcePetriNet_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "resourcePetriNet_GenericPlace"):
                    opp_val = getattr(item, "resourcePetriNet_GenericPlace", None)
                    
                    if opp_val == self:
                        setattr(item, "resourcePetriNet_GenericPlace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "resourcePetriNet_GenericPlace"):
                    opp_val = getattr(item, "resourcePetriNet_GenericPlace", None)
                    
                    setattr(item, "resourcePetriNet_GenericPlace", self)
                    

    @property
    def resourcePetriNet_PetriNet2(self):
        return self.__resourcePetriNet_PetriNet2

    @resourcePetriNet_PetriNet2.setter
    def resourcePetriNet_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_PetriNet__resourcePetriNet_PetriNet2", None)
        self.__resourcePetriNet_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "resourcePetriNet_Transition"):
                    opp_val = getattr(item, "resourcePetriNet_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "resourcePetriNet_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "resourcePetriNet_Transition"):
                    opp_val = getattr(item, "resourcePetriNet_Transition", None)
                    
                    setattr(item, "resourcePetriNet_Transition", self)
                    

    @property
    def resourcePetriNet_PetriNet4(self):
        return self.__resourcePetriNet_PetriNet4

    @resourcePetriNet_PetriNet4.setter
    def resourcePetriNet_PetriNet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_PetriNet__resourcePetriNet_PetriNet4", None)
        self.__resourcePetriNet_PetriNet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "resourcePetriNet_InputArc"):
                    opp_val = getattr(item, "resourcePetriNet_InputArc", None)
                    
                    if opp_val == self:
                        setattr(item, "resourcePetriNet_InputArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "resourcePetriNet_InputArc"):
                    opp_val = getattr(item, "resourcePetriNet_InputArc", None)
                    
                    setattr(item, "resourcePetriNet_InputArc", self)
                    

    @property
    def resourcePetriNet_PetriNet6(self):
        return self.__resourcePetriNet_PetriNet6

    @resourcePetriNet_PetriNet6.setter
    def resourcePetriNet_PetriNet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_PetriNet__resourcePetriNet_PetriNet6", None)
        self.__resourcePetriNet_PetriNet6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "resourcePetriNet_OutputArc"):
                    opp_val = getattr(item, "resourcePetriNet_OutputArc", None)
                    
                    if opp_val == self:
                        setattr(item, "resourcePetriNet_OutputArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "resourcePetriNet_OutputArc"):
                    opp_val = getattr(item, "resourcePetriNet_OutputArc", None)
                    
                    setattr(item, "resourcePetriNet_OutputArc", self)
                    

class GenericPlace:

    pass
class resourcePetriNet_Resource(GenericPlace):

    pass
class resourcePetriNet_Place(GenericPlace):

    def __init__(self, capacity: int):
        self.capacity = capacity
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

class resourcePetriNet_OutputArc:

    def __init__(self, weight: int, resourcePetriNet_OutputArc: "resourcePetriNet_PetriNet" = None, resourcePetriNet_OutputArc14: "resourcePetriNet_Transition" = None, resourcePetriNet_OutputArc17: "resourcePetriNet_GenericPlace" = None):
        self.weight = weight
        self.resourcePetriNet_OutputArc = resourcePetriNet_OutputArc
        self.resourcePetriNet_OutputArc14 = resourcePetriNet_OutputArc14
        self.resourcePetriNet_OutputArc17 = resourcePetriNet_OutputArc17
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def resourcePetriNet_OutputArc17(self):
        return self.__resourcePetriNet_OutputArc17

    @resourcePetriNet_OutputArc17.setter
    def resourcePetriNet_OutputArc17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_OutputArc__resourcePetriNet_OutputArc17", None)
        self.__resourcePetriNet_OutputArc17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_GenericPlace18"):
                opp_val = getattr(old_value, "resourcePetriNet_GenericPlace18", None)
                if opp_val == self:
                    setattr(old_value, "resourcePetriNet_GenericPlace18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_GenericPlace18"):
                opp_val = getattr(value, "resourcePetriNet_GenericPlace18", None)
                setattr(value, "resourcePetriNet_GenericPlace18", self)

    @property
    def resourcePetriNet_OutputArc(self):
        return self.__resourcePetriNet_OutputArc

    @resourcePetriNet_OutputArc.setter
    def resourcePetriNet_OutputArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_OutputArc__resourcePetriNet_OutputArc", None)
        self.__resourcePetriNet_OutputArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_PetriNet6"):
                opp_val = getattr(old_value, "resourcePetriNet_PetriNet6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_PetriNet6"):
                opp_val = getattr(value, "resourcePetriNet_PetriNet6", None)
                if opp_val is None:
                    setattr(value, "resourcePetriNet_PetriNet6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def resourcePetriNet_OutputArc14(self):
        return self.__resourcePetriNet_OutputArc14

    @resourcePetriNet_OutputArc14.setter
    def resourcePetriNet_OutputArc14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_resourcePetriNet_OutputArc__resourcePetriNet_OutputArc14", None)
        self.__resourcePetriNet_OutputArc14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resourcePetriNet_Transition15"):
                opp_val = getattr(old_value, "resourcePetriNet_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "resourcePetriNet_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resourcePetriNet_Transition15"):
                opp_val = getattr(value, "resourcePetriNet_Transition15", None)
                setattr(value, "resourcePetriNet_Transition15", self)
