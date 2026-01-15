from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class standardPetriNets_PetriNet:

    def __init__(self, name: str, standardPetriNets_PetriNet11: set["standardPetriNets_Transition"] = None, standardPetriNets_PetriNet14: set["standardPetriNets_InputArc"] = None, standardPetriNets_PetriNet17: set["standardPetriNets_OutputArc"] = None, standardPetriNets_PetriNet: set["standardPetriNets_Place"] = None):
        self.name = name
        self.standardPetriNets_PetriNet11 = standardPetriNets_PetriNet11 if standardPetriNets_PetriNet11 is not None else set()
        self.standardPetriNets_PetriNet14 = standardPetriNets_PetriNet14 if standardPetriNets_PetriNet14 is not None else set()
        self.standardPetriNets_PetriNet17 = standardPetriNets_PetriNet17 if standardPetriNets_PetriNet17 is not None else set()
        self.standardPetriNets_PetriNet = standardPetriNets_PetriNet if standardPetriNets_PetriNet is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def standardPetriNets_PetriNet17(self):
        return self.__standardPetriNets_PetriNet17

    @standardPetriNets_PetriNet17.setter
    def standardPetriNets_PetriNet17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_PetriNet__standardPetriNets_PetriNet17", None)
        self.__standardPetriNets_PetriNet17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "standardPetriNets_OutputArc18"):
                    opp_val = getattr(item, "standardPetriNets_OutputArc18", None)
                    
                    if opp_val == self:
                        setattr(item, "standardPetriNets_OutputArc18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "standardPetriNets_OutputArc18"):
                    opp_val = getattr(item, "standardPetriNets_OutputArc18", None)
                    
                    setattr(item, "standardPetriNets_OutputArc18", self)
                    

    @property
    def standardPetriNets_PetriNet14(self):
        return self.__standardPetriNets_PetriNet14

    @standardPetriNets_PetriNet14.setter
    def standardPetriNets_PetriNet14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_PetriNet__standardPetriNets_PetriNet14", None)
        self.__standardPetriNets_PetriNet14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "standardPetriNets_InputArc15"):
                    opp_val = getattr(item, "standardPetriNets_InputArc15", None)
                    
                    if opp_val == self:
                        setattr(item, "standardPetriNets_InputArc15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "standardPetriNets_InputArc15"):
                    opp_val = getattr(item, "standardPetriNets_InputArc15", None)
                    
                    setattr(item, "standardPetriNets_InputArc15", self)
                    

    @property
    def standardPetriNets_PetriNet(self):
        return self.__standardPetriNets_PetriNet

    @standardPetriNets_PetriNet.setter
    def standardPetriNets_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_PetriNet__standardPetriNets_PetriNet", None)
        self.__standardPetriNets_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "standardPetriNets_Place9"):
                    opp_val = getattr(item, "standardPetriNets_Place9", None)
                    
                    if opp_val == self:
                        setattr(item, "standardPetriNets_Place9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "standardPetriNets_Place9"):
                    opp_val = getattr(item, "standardPetriNets_Place9", None)
                    
                    setattr(item, "standardPetriNets_Place9", self)
                    

    @property
    def standardPetriNets_PetriNet11(self):
        return self.__standardPetriNets_PetriNet11

    @standardPetriNets_PetriNet11.setter
    def standardPetriNets_PetriNet11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_PetriNet__standardPetriNets_PetriNet11", None)
        self.__standardPetriNets_PetriNet11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "standardPetriNets_Transition12"):
                    opp_val = getattr(item, "standardPetriNets_Transition12", None)
                    
                    if opp_val == self:
                        setattr(item, "standardPetriNets_Transition12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "standardPetriNets_Transition12"):
                    opp_val = getattr(item, "standardPetriNets_Transition12", None)
                    
                    setattr(item, "standardPetriNets_Transition12", self)
                    

class standardPetriNets_OutputArc:

    def __init__(self, weight: int, standardPetriNets_OutputArc18: "standardPetriNets_PetriNet" = None, standardPetriNets_OutputArc: "standardPetriNets_Transition" = None, standardPetriNets_OutputArc6: "standardPetriNets_Place" = None):
        self.weight = weight
        self.standardPetriNets_OutputArc18 = standardPetriNets_OutputArc18
        self.standardPetriNets_OutputArc = standardPetriNets_OutputArc
        self.standardPetriNets_OutputArc6 = standardPetriNets_OutputArc6
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def standardPetriNets_OutputArc(self):
        return self.__standardPetriNets_OutputArc

    @standardPetriNets_OutputArc.setter
    def standardPetriNets_OutputArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_OutputArc__standardPetriNets_OutputArc", None)
        self.__standardPetriNets_OutputArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_Transition4"):
                opp_val = getattr(old_value, "standardPetriNets_Transition4", None)
                if opp_val == self:
                    setattr(old_value, "standardPetriNets_Transition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_Transition4"):
                opp_val = getattr(value, "standardPetriNets_Transition4", None)
                setattr(value, "standardPetriNets_Transition4", self)

    @property
    def standardPetriNets_OutputArc6(self):
        return self.__standardPetriNets_OutputArc6

    @standardPetriNets_OutputArc6.setter
    def standardPetriNets_OutputArc6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_OutputArc__standardPetriNets_OutputArc6", None)
        self.__standardPetriNets_OutputArc6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_Place7"):
                opp_val = getattr(old_value, "standardPetriNets_Place7", None)
                if opp_val == self:
                    setattr(old_value, "standardPetriNets_Place7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_Place7"):
                opp_val = getattr(value, "standardPetriNets_Place7", None)
                setattr(value, "standardPetriNets_Place7", self)

    @property
    def standardPetriNets_OutputArc18(self):
        return self.__standardPetriNets_OutputArc18

    @standardPetriNets_OutputArc18.setter
    def standardPetriNets_OutputArc18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_OutputArc__standardPetriNets_OutputArc18", None)
        self.__standardPetriNets_OutputArc18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_PetriNet17"):
                opp_val = getattr(old_value, "standardPetriNets_PetriNet17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_PetriNet17"):
                opp_val = getattr(value, "standardPetriNets_PetriNet17", None)
                if opp_val is None:
                    setattr(value, "standardPetriNets_PetriNet17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class standardPetriNets_Place:

    def __init__(self, numOfTokens: int, capacity: int, name: str, standardPetriNets_Place: "standardPetriNets_InputArc" = None, standardPetriNets_Place7: "standardPetriNets_OutputArc" = None, standardPetriNets_Place9: "standardPetriNets_PetriNet" = None):
        self.numOfTokens = numOfTokens
        self.capacity = capacity
        self.name = name
        self.standardPetriNets_Place = standardPetriNets_Place
        self.standardPetriNets_Place7 = standardPetriNets_Place7
        self.standardPetriNets_Place9 = standardPetriNets_Place9
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def numOfTokens(self) -> int:
        return self.__numOfTokens

    @numOfTokens.setter
    def numOfTokens(self, numOfTokens: int):
        self.__numOfTokens = numOfTokens

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def standardPetriNets_Place(self):
        return self.__standardPetriNets_Place

    @standardPetriNets_Place.setter
    def standardPetriNets_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_Place__standardPetriNets_Place", None)
        self.__standardPetriNets_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_InputArc"):
                opp_val = getattr(old_value, "standardPetriNets_InputArc", None)
                if opp_val == self:
                    setattr(old_value, "standardPetriNets_InputArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_InputArc"):
                opp_val = getattr(value, "standardPetriNets_InputArc", None)
                setattr(value, "standardPetriNets_InputArc", self)

    @property
    def standardPetriNets_Place9(self):
        return self.__standardPetriNets_Place9

    @standardPetriNets_Place9.setter
    def standardPetriNets_Place9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_Place__standardPetriNets_Place9", None)
        self.__standardPetriNets_Place9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_PetriNet"):
                opp_val = getattr(old_value, "standardPetriNets_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_PetriNet"):
                opp_val = getattr(value, "standardPetriNets_PetriNet", None)
                if opp_val is None:
                    setattr(value, "standardPetriNets_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def standardPetriNets_Place7(self):
        return self.__standardPetriNets_Place7

    @standardPetriNets_Place7.setter
    def standardPetriNets_Place7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_Place__standardPetriNets_Place7", None)
        self.__standardPetriNets_Place7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_OutputArc6"):
                opp_val = getattr(old_value, "standardPetriNets_OutputArc6", None)
                if opp_val == self:
                    setattr(old_value, "standardPetriNets_OutputArc6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_OutputArc6"):
                opp_val = getattr(value, "standardPetriNets_OutputArc6", None)
                setattr(value, "standardPetriNets_OutputArc6", self)

class standardPetriNets_InputArc:

    def __init__(self, weight: int, standardPetriNets_InputArc: "standardPetriNets_Place" = None, standardPetriNets_InputArc15: "standardPetriNets_PetriNet" = None, standardPetriNets_InputArc2: "standardPetriNets_Transition" = None):
        self.weight = weight
        self.standardPetriNets_InputArc = standardPetriNets_InputArc
        self.standardPetriNets_InputArc15 = standardPetriNets_InputArc15
        self.standardPetriNets_InputArc2 = standardPetriNets_InputArc2
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def standardPetriNets_InputArc(self):
        return self.__standardPetriNets_InputArc

    @standardPetriNets_InputArc.setter
    def standardPetriNets_InputArc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_InputArc__standardPetriNets_InputArc", None)
        self.__standardPetriNets_InputArc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_Place"):
                opp_val = getattr(old_value, "standardPetriNets_Place", None)
                if opp_val == self:
                    setattr(old_value, "standardPetriNets_Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_Place"):
                opp_val = getattr(value, "standardPetriNets_Place", None)
                setattr(value, "standardPetriNets_Place", self)

    @property
    def standardPetriNets_InputArc15(self):
        return self.__standardPetriNets_InputArc15

    @standardPetriNets_InputArc15.setter
    def standardPetriNets_InputArc15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_InputArc__standardPetriNets_InputArc15", None)
        self.__standardPetriNets_InputArc15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_PetriNet14"):
                opp_val = getattr(old_value, "standardPetriNets_PetriNet14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_PetriNet14"):
                opp_val = getattr(value, "standardPetriNets_PetriNet14", None)
                if opp_val is None:
                    setattr(value, "standardPetriNets_PetriNet14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def standardPetriNets_InputArc2(self):
        return self.__standardPetriNets_InputArc2

    @standardPetriNets_InputArc2.setter
    def standardPetriNets_InputArc2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_InputArc__standardPetriNets_InputArc2", None)
        self.__standardPetriNets_InputArc2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_Transition"):
                opp_val = getattr(old_value, "standardPetriNets_Transition", None)
                if opp_val == self:
                    setattr(old_value, "standardPetriNets_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_Transition"):
                opp_val = getattr(value, "standardPetriNets_Transition", None)
                setattr(value, "standardPetriNets_Transition", self)

class standardPetriNets_Transition:

    def __init__(self, name: str, standardPetriNets_Transition12: "standardPetriNets_PetriNet" = None, standardPetriNets_Transition: "standardPetriNets_InputArc" = None, standardPetriNets_Transition4: "standardPetriNets_OutputArc" = None):
        self.name = name
        self.standardPetriNets_Transition12 = standardPetriNets_Transition12
        self.standardPetriNets_Transition = standardPetriNets_Transition
        self.standardPetriNets_Transition4 = standardPetriNets_Transition4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def standardPetriNets_Transition(self):
        return self.__standardPetriNets_Transition

    @standardPetriNets_Transition.setter
    def standardPetriNets_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_Transition__standardPetriNets_Transition", None)
        self.__standardPetriNets_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_InputArc2"):
                opp_val = getattr(old_value, "standardPetriNets_InputArc2", None)
                if opp_val == self:
                    setattr(old_value, "standardPetriNets_InputArc2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_InputArc2"):
                opp_val = getattr(value, "standardPetriNets_InputArc2", None)
                setattr(value, "standardPetriNets_InputArc2", self)

    @property
    def standardPetriNets_Transition12(self):
        return self.__standardPetriNets_Transition12

    @standardPetriNets_Transition12.setter
    def standardPetriNets_Transition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_Transition__standardPetriNets_Transition12", None)
        self.__standardPetriNets_Transition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_PetriNet11"):
                opp_val = getattr(old_value, "standardPetriNets_PetriNet11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_PetriNet11"):
                opp_val = getattr(value, "standardPetriNets_PetriNet11", None)
                if opp_val is None:
                    setattr(value, "standardPetriNets_PetriNet11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def standardPetriNets_Transition4(self):
        return self.__standardPetriNets_Transition4

    @standardPetriNets_Transition4.setter
    def standardPetriNets_Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standardPetriNets_Transition__standardPetriNets_Transition4", None)
        self.__standardPetriNets_Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standardPetriNets_OutputArc"):
                opp_val = getattr(old_value, "standardPetriNets_OutputArc", None)
                if opp_val == self:
                    setattr(old_value, "standardPetriNets_OutputArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standardPetriNets_OutputArc"):
                opp_val = getattr(value, "standardPetriNets_OutputArc", None)
                setattr(value, "standardPetriNets_OutputArc", self)
