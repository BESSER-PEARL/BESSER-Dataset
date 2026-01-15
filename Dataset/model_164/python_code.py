from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Identifiable:

    pass
class PetriNet_Transition(Identifiable):

    def __init__(self, name: str, PetriNet_Transition: set["PetriNet_InputArc"] = None, PetriNet_Transition8: set["PetriNet_OutputArc"] = None, PetriNet_Transition15: "PetriNet_InputArc" = None, PetriNet_Transition21: "PetriNet_OutputArc" = None):
        self.name = name
        self.PetriNet_Transition = PetriNet_Transition if PetriNet_Transition is not None else set()
        self.PetriNet_Transition8 = PetriNet_Transition8 if PetriNet_Transition8 is not None else set()
        self.PetriNet_Transition15 = PetriNet_Transition15
        self.PetriNet_Transition21 = PetriNet_Transition21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_Transition15(self):
        return self.__PetriNet_Transition15

    @PetriNet_Transition15.setter
    def PetriNet_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__PetriNet_Transition15", None)
        self.__PetriNet_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_InputArc14"):
                opp_val = getattr(old_value, "PetriNet_InputArc14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_InputArc14"):
                opp_val = getattr(value, "PetriNet_InputArc14", None)
                if opp_val is None:
                    setattr(value, "PetriNet_InputArc14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNet_Transition(self):
        return self.__PetriNet_Transition

    @PetriNet_Transition.setter
    def PetriNet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__PetriNet_Transition", None)
        self.__PetriNet_Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_InputArc6"):
                    opp_val = getattr(item, "PetriNet_InputArc6", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_InputArc6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_InputArc6"):
                    opp_val = getattr(item, "PetriNet_InputArc6", None)
                    
                    setattr(item, "PetriNet_InputArc6", self)
                    

    @property
    def PetriNet_Transition8(self):
        return self.__PetriNet_Transition8

    @PetriNet_Transition8.setter
    def PetriNet_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__PetriNet_Transition8", None)
        self.__PetriNet_Transition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_OutputArc9"):
                    opp_val = getattr(item, "PetriNet_OutputArc9", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_OutputArc9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_OutputArc9"):
                    opp_val = getattr(item, "PetriNet_OutputArc9", None)
                    
                    setattr(item, "PetriNet_OutputArc9", self)
                    

    @property
    def PetriNet_Transition21(self):
        return self.__PetriNet_Transition21

    @PetriNet_Transition21.setter
    def PetriNet_Transition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Transition__PetriNet_Transition21", None)
        self.__PetriNet_Transition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_OutputArc20"):
                opp_val = getattr(old_value, "PetriNet_OutputArc20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_OutputArc20"):
                opp_val = getattr(value, "PetriNet_OutputArc20", None)
                if opp_val is None:
                    setattr(value, "PetriNet_OutputArc20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNet_InputArc(Identifiable):

    pass
class PetriNet_Token(Identifiable):

    pass
class PetriNet_Net(Identifiable):

    pass
class PetriNet_OutputArc(Identifiable):

    pass
class PetriNet_Place(Identifiable):

    def __init__(self, name: str, PetriNet_Place: set["PetriNet_Token"] = None, PetriNet_Place2: set["PetriNet_InputArc"] = None, PetriNet_Place4: set["PetriNet_OutputArc"] = None, PetriNet_Place23: "PetriNet_Net" = None, PetriNet_Place12: "PetriNet_InputArc" = None, PetriNet_Place18: "PetriNet_OutputArc" = None):
        self.name = name
        self.PetriNet_Place = PetriNet_Place if PetriNet_Place is not None else set()
        self.PetriNet_Place2 = PetriNet_Place2 if PetriNet_Place2 is not None else set()
        self.PetriNet_Place4 = PetriNet_Place4 if PetriNet_Place4 is not None else set()
        self.PetriNet_Place23 = PetriNet_Place23
        self.PetriNet_Place12 = PetriNet_Place12
        self.PetriNet_Place18 = PetriNet_Place18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_Place23(self):
        return self.__PetriNet_Place23

    @PetriNet_Place23.setter
    def PetriNet_Place23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place23", None)
        self.__PetriNet_Place23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Net"):
                opp_val = getattr(old_value, "PetriNet_Net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Net"):
                opp_val = getattr(value, "PetriNet_Net", None)
                if opp_val is None:
                    setattr(value, "PetriNet_Net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNet_Place18(self):
        return self.__PetriNet_Place18

    @PetriNet_Place18.setter
    def PetriNet_Place18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place18", None)
        self.__PetriNet_Place18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_OutputArc17"):
                opp_val = getattr(old_value, "PetriNet_OutputArc17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_OutputArc17"):
                opp_val = getattr(value, "PetriNet_OutputArc17", None)
                if opp_val is None:
                    setattr(value, "PetriNet_OutputArc17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNet_Place(self):
        return self.__PetriNet_Place

    @PetriNet_Place.setter
    def PetriNet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place", None)
        self.__PetriNet_Place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_Token"):
                    opp_val = getattr(item, "PetriNet_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_Token"):
                    opp_val = getattr(item, "PetriNet_Token", None)
                    
                    setattr(item, "PetriNet_Token", self)
                    

    @property
    def PetriNet_Place4(self):
        return self.__PetriNet_Place4

    @PetriNet_Place4.setter
    def PetriNet_Place4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place4", None)
        self.__PetriNet_Place4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_OutputArc"):
                    opp_val = getattr(item, "PetriNet_OutputArc", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_OutputArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_OutputArc"):
                    opp_val = getattr(item, "PetriNet_OutputArc", None)
                    
                    setattr(item, "PetriNet_OutputArc", self)
                    

    @property
    def PetriNet_Place2(self):
        return self.__PetriNet_Place2

    @PetriNet_Place2.setter
    def PetriNet_Place2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place2", None)
        self.__PetriNet_Place2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_InputArc"):
                    opp_val = getattr(item, "PetriNet_InputArc", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_InputArc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_InputArc"):
                    opp_val = getattr(item, "PetriNet_InputArc", None)
                    
                    setattr(item, "PetriNet_InputArc", self)
                    

    @property
    def PetriNet_Place12(self):
        return self.__PetriNet_Place12

    @PetriNet_Place12.setter
    def PetriNet_Place12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place12", None)
        self.__PetriNet_Place12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_InputArc11"):
                opp_val = getattr(old_value, "PetriNet_InputArc11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_InputArc11"):
                opp_val = getattr(value, "PetriNet_InputArc11", None)
                if opp_val is None:
                    setattr(value, "PetriNet_InputArc11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
