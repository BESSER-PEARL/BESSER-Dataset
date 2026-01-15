from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petriNet_OutputArc:

    def __init__(self, weight: int, petriNet_OutputArc: "petriNet_PetriNet" = None, petriNet_OutputArc14: "petriNet_Transition" = None, petriNet_OutputArc17: "petriNet_GenericPlace" = None):
        self.weight = weight
        self.petriNet_OutputArc = petriNet_OutputArc
        self.petriNet_OutputArc14 = petriNet_OutputArc14
        self.petriNet_OutputArc17 = petriNet_OutputArc17
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def petriNet_OutputArc17(self):
        return self.__petriNet_OutputArc17

    @petriNet_OutputArc17.setter
    def petriNet_OutputArc17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_OutputArc__petriNet_OutputArc17", None)
        self.__petriNet_OutputArc17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_GenericPlace18"):
                opp_val = getattr(old_value, "petriNet_GenericPlace18", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_GenericPlace18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_GenericPlace18"):
                opp_val = getattr(value, "petriNet_GenericPlace18", None)
                setattr(value, "petriNet_GenericPlace18", self)

    @property
    def petriNet_OutputArc14(self):
        return self.__petriNet_OutputArc14

    @petriNet_OutputArc14.setter
    def petriNet_OutputArc14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_OutputArc__petriNet_OutputArc14", None)
        self.__petriNet_OutputArc14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Transition15"):
                opp_val = getattr(old_value, "petriNet_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Transition15"):
                opp_val = getattr(value, "petriNet_Transition15", None)
                setattr(value, "petriNet_Transition15", self)

    @property
    def petriNet_OutputArc(self):
        return self.__petriNet_OutputArc

    @petriNet_OutputArc.setter
    def petriNet_OutputArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_OutputArc__petriNet_OutputArc", None)
        self.__petriNet_OutputArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_PetriNet6"):
                opp_val = getattr(old_value, "petriNet_PetriNet6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_PetriNet6"):
                opp_val = getattr(value, "petriNet_PetriNet6", None)
                if opp_val is None:
                    setattr(value, "petriNet_PetriNet6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petriNet_InputArc:

    def __init__(self, weight: int, petriNet_InputArc: "petriNet_PetriNet" = None, petriNet_InputArc8: "petriNet_GenericPlace" = None, petriNet_InputArc11: "petriNet_Transition" = None):
        self.weight = weight
        self.petriNet_InputArc = petriNet_InputArc
        self.petriNet_InputArc8 = petriNet_InputArc8
        self.petriNet_InputArc11 = petriNet_InputArc11
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def petriNet_InputArc(self):
        return self.__petriNet_InputArc

    @petriNet_InputArc.setter
    def petriNet_InputArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_InputArc__petriNet_InputArc", None)
        self.__petriNet_InputArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_PetriNet4"):
                opp_val = getattr(old_value, "petriNet_PetriNet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_PetriNet4"):
                opp_val = getattr(value, "petriNet_PetriNet4", None)
                if opp_val is None:
                    setattr(value, "petriNet_PetriNet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petriNet_InputArc8(self):
        return self.__petriNet_InputArc8

    @petriNet_InputArc8.setter
    def petriNet_InputArc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_InputArc__petriNet_InputArc8", None)
        self.__petriNet_InputArc8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_GenericPlace9"):
                opp_val = getattr(old_value, "petriNet_GenericPlace9", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_GenericPlace9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_GenericPlace9"):
                opp_val = getattr(value, "petriNet_GenericPlace9", None)
                setattr(value, "petriNet_GenericPlace9", self)

    @property
    def petriNet_InputArc11(self):
        return self.__petriNet_InputArc11

    @petriNet_InputArc11.setter
    def petriNet_InputArc11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_InputArc__petriNet_InputArc11", None)
        self.__petriNet_InputArc11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_Transition12"):
                opp_val = getattr(old_value, "petriNet_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_Transition12"):
                opp_val = getattr(value, "petriNet_Transition12", None)
                setattr(value, "petriNet_Transition12", self)

class petriNet_Transition:

    def __init__(self, name: str, petriNet_Transition: "petriNet_PetriNet" = None, petriNet_Transition12: "petriNet_InputArc" = None, petriNet_Transition15: "petriNet_OutputArc" = None):
        self.name = name
        self.petriNet_Transition = petriNet_Transition
        self.petriNet_Transition12 = petriNet_Transition12
        self.petriNet_Transition15 = petriNet_Transition15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petriNet_Transition15(self):
        return self.__petriNet_Transition15

    @petriNet_Transition15.setter
    def petriNet_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Transition__petriNet_Transition15", None)
        self.__petriNet_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_OutputArc14"):
                opp_val = getattr(old_value, "petriNet_OutputArc14", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_OutputArc14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_OutputArc14"):
                opp_val = getattr(value, "petriNet_OutputArc14", None)
                setattr(value, "petriNet_OutputArc14", self)

    @property
    def petriNet_Transition12(self):
        return self.__petriNet_Transition12

    @petriNet_Transition12.setter
    def petriNet_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Transition__petriNet_Transition12", None)
        self.__petriNet_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_InputArc11"):
                opp_val = getattr(old_value, "petriNet_InputArc11", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_InputArc11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_InputArc11"):
                opp_val = getattr(value, "petriNet_InputArc11", None)
                setattr(value, "petriNet_InputArc11", self)

    @property
    def petriNet_Transition(self):
        return self.__petriNet_Transition

    @petriNet_Transition.setter
    def petriNet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_Transition__petriNet_Transition", None)
        self.__petriNet_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_PetriNet2"):
                opp_val = getattr(old_value, "petriNet_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_PetriNet2"):
                opp_val = getattr(value, "petriNet_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "petriNet_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petriNet_GenericPlace(ABC):

    def __init__(self, name: str, numberOfTokens: int, petriNet_GenericPlace: "petriNet_PetriNet" = None, petriNet_GenericPlace18: "petriNet_OutputArc" = None, petriNet_GenericPlace9: "petriNet_InputArc" = None):
        self.name = name
        self.numberOfTokens = numberOfTokens
        self.petriNet_GenericPlace = petriNet_GenericPlace
        self.petriNet_GenericPlace18 = petriNet_GenericPlace18
        self.petriNet_GenericPlace9 = petriNet_GenericPlace9
        
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
    def petriNet_GenericPlace18(self):
        return self.__petriNet_GenericPlace18

    @petriNet_GenericPlace18.setter
    def petriNet_GenericPlace18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_GenericPlace__petriNet_GenericPlace18", None)
        self.__petriNet_GenericPlace18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_OutputArc17"):
                opp_val = getattr(old_value, "petriNet_OutputArc17", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_OutputArc17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_OutputArc17"):
                opp_val = getattr(value, "petriNet_OutputArc17", None)
                setattr(value, "petriNet_OutputArc17", self)

    @property
    def petriNet_GenericPlace(self):
        return self.__petriNet_GenericPlace

    @petriNet_GenericPlace.setter
    def petriNet_GenericPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_GenericPlace__petriNet_GenericPlace", None)
        self.__petriNet_GenericPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_PetriNet"):
                opp_val = getattr(old_value, "petriNet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_PetriNet"):
                opp_val = getattr(value, "petriNet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "petriNet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petriNet_GenericPlace9(self):
        return self.__petriNet_GenericPlace9

    @petriNet_GenericPlace9.setter
    def petriNet_GenericPlace9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_GenericPlace__petriNet_GenericPlace9", None)
        self.__petriNet_GenericPlace9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petriNet_InputArc8"):
                opp_val = getattr(old_value, "petriNet_InputArc8", None)
                if opp_val == self:
                    setattr(old_value, "petriNet_InputArc8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petriNet_InputArc8"):
                opp_val = getattr(value, "petriNet_InputArc8", None)
                setattr(value, "petriNet_InputArc8", self)

class petriNet_PetriNet:

    def __init__(self, name: str, petriNet_PetriNet: set["petriNet_GenericPlace"] = None, petriNet_PetriNet2: set["petriNet_Transition"] = None, petriNet_PetriNet4: set["petriNet_InputArc"] = None, petriNet_PetriNet6: set["petriNet_OutputArc"] = None):
        self.name = name
        self.petriNet_PetriNet = petriNet_PetriNet if petriNet_PetriNet is not None else set()
        self.petriNet_PetriNet2 = petriNet_PetriNet2 if petriNet_PetriNet2 is not None else set()
        self.petriNet_PetriNet4 = petriNet_PetriNet4 if petriNet_PetriNet4 is not None else set()
        self.petriNet_PetriNet6 = petriNet_PetriNet6 if petriNet_PetriNet6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petriNet_PetriNet(self):
        return self.__petriNet_PetriNet

    @petriNet_PetriNet.setter
    def petriNet_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_PetriNet__petriNet_PetriNet", None)
        self.__petriNet_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNet_GenericPlace"):
                    opp_val = getattr(item, "petriNet_GenericPlace", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNet_GenericPlace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNet_GenericPlace"):
                    opp_val = getattr(item, "petriNet_GenericPlace", None)
                    
                    setattr(item, "petriNet_GenericPlace", self)
                    

    @property
    def petriNet_PetriNet2(self):
        return self.__petriNet_PetriNet2

    @petriNet_PetriNet2.setter
    def petriNet_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_PetriNet__petriNet_PetriNet2", None)
        self.__petriNet_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNet_Transition"):
                    opp_val = getattr(item, "petriNet_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNet_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNet_Transition"):
                    opp_val = getattr(item, "petriNet_Transition", None)
                    
                    setattr(item, "petriNet_Transition", self)
                    

    @property
    def petriNet_PetriNet4(self):
        return self.__petriNet_PetriNet4

    @petriNet_PetriNet4.setter
    def petriNet_PetriNet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_PetriNet__petriNet_PetriNet4", None)
        self.__petriNet_PetriNet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNet_InputArc"):
                    opp_val = getattr(item, "petriNet_InputArc", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNet_InputArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNet_InputArc"):
                    opp_val = getattr(item, "petriNet_InputArc", None)
                    
                    setattr(item, "petriNet_InputArc", self)
                    

    @property
    def petriNet_PetriNet6(self):
        return self.__petriNet_PetriNet6

    @petriNet_PetriNet6.setter
    def petriNet_PetriNet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petriNet_PetriNet__petriNet_PetriNet6", None)
        self.__petriNet_PetriNet6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petriNet_OutputArc"):
                    opp_val = getattr(item, "petriNet_OutputArc", None)
                    
                    if opp_val == self:
                        setattr(item, "petriNet_OutputArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petriNet_OutputArc"):
                    opp_val = getattr(item, "petriNet_OutputArc", None)
                    
                    setattr(item, "petriNet_OutputArc", self)
                    

class GenericPlace:

    pass
class petriNet_Resource(GenericPlace):

    pass
class petriNet_Place(GenericPlace):

    def __init__(self, capacity: int):
        self.capacity = capacity
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity
