from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PetriNets_OutputArc:

    def __init__(self, weight: int, PetriNets_OutputArc: "PetriNets_PetriNet" = None, PetriNets_OutputArc14: "PetriNets_Transition" = None, PetriNets_OutputArc17: "PetriNets_Place" = None):
        self.weight = weight
        self.PetriNets_OutputArc = PetriNets_OutputArc
        self.PetriNets_OutputArc14 = PetriNets_OutputArc14
        self.PetriNets_OutputArc17 = PetriNets_OutputArc17
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def PetriNets_OutputArc14(self):
        return self.__PetriNets_OutputArc14

    @PetriNets_OutputArc14.setter
    def PetriNets_OutputArc14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_OutputArc__PetriNets_OutputArc14", None)
        self.__PetriNets_OutputArc14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition15"):
                opp_val = getattr(old_value, "PetriNets_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition15"):
                opp_val = getattr(value, "PetriNets_Transition15", None)
                setattr(value, "PetriNets_Transition15", self)

    @property
    def PetriNets_OutputArc(self):
        return self.__PetriNets_OutputArc

    @PetriNets_OutputArc.setter
    def PetriNets_OutputArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_OutputArc__PetriNets_OutputArc", None)
        self.__PetriNets_OutputArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_PetriNet6"):
                opp_val = getattr(old_value, "PetriNets_PetriNet6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_PetriNet6"):
                opp_val = getattr(value, "PetriNets_PetriNet6", None)
                if opp_val is None:
                    setattr(value, "PetriNets_PetriNet6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNets_OutputArc17(self):
        return self.__PetriNets_OutputArc17

    @PetriNets_OutputArc17.setter
    def PetriNets_OutputArc17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_OutputArc__PetriNets_OutputArc17", None)
        self.__PetriNets_OutputArc17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Place18"):
                opp_val = getattr(old_value, "PetriNets_Place18", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_Place18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Place18"):
                opp_val = getattr(value, "PetriNets_Place18", None)
                setattr(value, "PetriNets_Place18", self)

class PetriNets_InputArc:

    def __init__(self, weight: int, PetriNets_InputArc: "PetriNets_PetriNet" = None, PetriNets_InputArc8: "PetriNets_Place" = None, PetriNets_InputArc11: "PetriNets_Transition" = None):
        self.weight = weight
        self.PetriNets_InputArc = PetriNets_InputArc
        self.PetriNets_InputArc8 = PetriNets_InputArc8
        self.PetriNets_InputArc11 = PetriNets_InputArc11
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def PetriNets_InputArc11(self):
        return self.__PetriNets_InputArc11

    @PetriNets_InputArc11.setter
    def PetriNets_InputArc11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_InputArc__PetriNets_InputArc11", None)
        self.__PetriNets_InputArc11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition12"):
                opp_val = getattr(old_value, "PetriNets_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition12"):
                opp_val = getattr(value, "PetriNets_Transition12", None)
                setattr(value, "PetriNets_Transition12", self)

    @property
    def PetriNets_InputArc(self):
        return self.__PetriNets_InputArc

    @PetriNets_InputArc.setter
    def PetriNets_InputArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_InputArc__PetriNets_InputArc", None)
        self.__PetriNets_InputArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_PetriNet4"):
                opp_val = getattr(old_value, "PetriNets_PetriNet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_PetriNet4"):
                opp_val = getattr(value, "PetriNets_PetriNet4", None)
                if opp_val is None:
                    setattr(value, "PetriNets_PetriNet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNets_InputArc8(self):
        return self.__PetriNets_InputArc8

    @PetriNets_InputArc8.setter
    def PetriNets_InputArc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_InputArc__PetriNets_InputArc8", None)
        self.__PetriNets_InputArc8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Place9"):
                opp_val = getattr(old_value, "PetriNets_Place9", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_Place9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Place9"):
                opp_val = getattr(value, "PetriNets_Place9", None)
                setattr(value, "PetriNets_Place9", self)

class PetriNets_Transition:

    def __init__(self, name: str, PetriNets_Transition: "PetriNets_PetriNet" = None, PetriNets_Transition12: "PetriNets_InputArc" = None, PetriNets_Transition15: "PetriNets_OutputArc" = None):
        self.name = name
        self.PetriNets_Transition = PetriNets_Transition
        self.PetriNets_Transition12 = PetriNets_Transition12
        self.PetriNets_Transition15 = PetriNets_Transition15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNets_Transition15(self):
        return self.__PetriNets_Transition15

    @PetriNets_Transition15.setter
    def PetriNets_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition15", None)
        self.__PetriNets_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_OutputArc14"):
                opp_val = getattr(old_value, "PetriNets_OutputArc14", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_OutputArc14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_OutputArc14"):
                opp_val = getattr(value, "PetriNets_OutputArc14", None)
                setattr(value, "PetriNets_OutputArc14", self)

    @property
    def PetriNets_Transition12(self):
        return self.__PetriNets_Transition12

    @PetriNets_Transition12.setter
    def PetriNets_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition12", None)
        self.__PetriNets_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_InputArc11"):
                opp_val = getattr(old_value, "PetriNets_InputArc11", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_InputArc11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_InputArc11"):
                opp_val = getattr(value, "PetriNets_InputArc11", None)
                setattr(value, "PetriNets_InputArc11", self)

    @property
    def PetriNets_Transition(self):
        return self.__PetriNets_Transition

    @PetriNets_Transition.setter
    def PetriNets_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Transition__PetriNets_Transition", None)
        self.__PetriNets_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_PetriNet2"):
                opp_val = getattr(old_value, "PetriNets_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_PetriNet2"):
                opp_val = getattr(value, "PetriNets_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "PetriNets_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNets_PetriNet:

    def __init__(self, name: str, PetriNets_PetriNet: set["PetriNets_Place"] = None, PetriNets_PetriNet2: set["PetriNets_Transition"] = None, PetriNets_PetriNet4: set["PetriNets_InputArc"] = None, PetriNets_PetriNet6: set["PetriNets_OutputArc"] = None):
        self.name = name
        self.PetriNets_PetriNet = PetriNets_PetriNet if PetriNets_PetriNet is not None else set()
        self.PetriNets_PetriNet2 = PetriNets_PetriNet2 if PetriNets_PetriNet2 is not None else set()
        self.PetriNets_PetriNet4 = PetriNets_PetriNet4 if PetriNets_PetriNet4 is not None else set()
        self.PetriNets_PetriNet6 = PetriNets_PetriNet6 if PetriNets_PetriNet6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNets_PetriNet4(self):
        return self.__PetriNets_PetriNet4

    @PetriNets_PetriNet4.setter
    def PetriNets_PetriNet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_PetriNet__PetriNets_PetriNet4", None)
        self.__PetriNets_PetriNet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_InputArc"):
                    opp_val = getattr(item, "PetriNets_InputArc", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_InputArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_InputArc"):
                    opp_val = getattr(item, "PetriNets_InputArc", None)
                    
                    setattr(item, "PetriNets_InputArc", self)
                    

    @property
    def PetriNets_PetriNet(self):
        return self.__PetriNets_PetriNet

    @PetriNets_PetriNet.setter
    def PetriNets_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_PetriNet__PetriNets_PetriNet", None)
        self.__PetriNets_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Place"):
                    opp_val = getattr(item, "PetriNets_Place", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Place"):
                    opp_val = getattr(item, "PetriNets_Place", None)
                    
                    setattr(item, "PetriNets_Place", self)
                    

    @property
    def PetriNets_PetriNet2(self):
        return self.__PetriNets_PetriNet2

    @PetriNets_PetriNet2.setter
    def PetriNets_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_PetriNet__PetriNets_PetriNet2", None)
        self.__PetriNets_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Transition"):
                    opp_val = getattr(item, "PetriNets_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Transition"):
                    opp_val = getattr(item, "PetriNets_Transition", None)
                    
                    setattr(item, "PetriNets_Transition", self)
                    

    @property
    def PetriNets_PetriNet6(self):
        return self.__PetriNets_PetriNet6

    @PetriNets_PetriNet6.setter
    def PetriNets_PetriNet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_PetriNet__PetriNets_PetriNet6", None)
        self.__PetriNets_PetriNet6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_OutputArc"):
                    opp_val = getattr(item, "PetriNets_OutputArc", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_OutputArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_OutputArc"):
                    opp_val = getattr(item, "PetriNets_OutputArc", None)
                    
                    setattr(item, "PetriNets_OutputArc", self)
                    

class PetriNets_Place:

    def __init__(self, name: str, capacity: int, numberOfTokens: int, PetriNets_Place: "PetriNets_PetriNet" = None, PetriNets_Place9: "PetriNets_InputArc" = None, PetriNets_Place18: "PetriNets_OutputArc" = None):
        self.name = name
        self.capacity = capacity
        self.numberOfTokens = numberOfTokens
        self.PetriNets_Place = PetriNets_Place
        self.PetriNets_Place9 = PetriNets_Place9
        self.PetriNets_Place18 = PetriNets_Place18
        
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
    def PetriNets_Place9(self):
        return self.__PetriNets_Place9

    @PetriNets_Place9.setter
    def PetriNets_Place9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place9", None)
        self.__PetriNets_Place9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_InputArc8"):
                opp_val = getattr(old_value, "PetriNets_InputArc8", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_InputArc8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_InputArc8"):
                opp_val = getattr(value, "PetriNets_InputArc8", None)
                setattr(value, "PetriNets_InputArc8", self)

    @property
    def PetriNets_Place18(self):
        return self.__PetriNets_Place18

    @PetriNets_Place18.setter
    def PetriNets_Place18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place18", None)
        self.__PetriNets_Place18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_OutputArc17"):
                opp_val = getattr(old_value, "PetriNets_OutputArc17", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_OutputArc17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_OutputArc17"):
                opp_val = getattr(value, "PetriNets_OutputArc17", None)
                setattr(value, "PetriNets_OutputArc17", self)

    @property
    def PetriNets_Place(self):
        return self.__PetriNets_Place

    @PetriNets_Place.setter
    def PetriNets_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place", None)
        self.__PetriNets_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_PetriNet"):
                opp_val = getattr(old_value, "PetriNets_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_PetriNet"):
                opp_val = getattr(value, "PetriNets_PetriNet", None)
                if opp_val is None:
                    setattr(value, "PetriNets_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
