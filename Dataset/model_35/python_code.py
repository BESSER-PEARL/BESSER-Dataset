from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PetriNetModel_ArcTP:

    def __init__(self, inscription: str, PetriNetModel_ArcTP: "PetriNetModel_PetriNet" = None, PetriNetModel_ArcTP12: "PetriNetModel_Transition" = None, PetriNetModel_ArcTP23: "PetriNetModel_Transition" = None, PetriNetModel_ArcTP20: "PetriNetModel_Place" = None, PetriNetModel_ArcTP27: "PetriNetModel_Place" = None):
        self.inscription = inscription
        self.PetriNetModel_ArcTP = PetriNetModel_ArcTP
        self.PetriNetModel_ArcTP12 = PetriNetModel_ArcTP12
        self.PetriNetModel_ArcTP23 = PetriNetModel_ArcTP23
        self.PetriNetModel_ArcTP20 = PetriNetModel_ArcTP20
        self.PetriNetModel_ArcTP27 = PetriNetModel_ArcTP27
        
    @property
    def inscription(self) -> str:
        return self.__inscription

    @inscription.setter
    def inscription(self, inscription: str):
        self.__inscription = inscription

    @property
    def PetriNetModel_ArcTP12(self):
        return self.__PetriNetModel_ArcTP12

    @PetriNetModel_ArcTP12.setter
    def PetriNetModel_ArcTP12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_ArcTP__PetriNetModel_ArcTP12", None)
        self.__PetriNetModel_ArcTP12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_Transition11"):
                opp_val = getattr(old_value, "PetriNetModel_Transition11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_Transition11"):
                opp_val = getattr(value, "PetriNetModel_Transition11", None)
                if opp_val is None:
                    setattr(value, "PetriNetModel_Transition11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNetModel_ArcTP20(self):
        return self.__PetriNetModel_ArcTP20

    @PetriNetModel_ArcTP20.setter
    def PetriNetModel_ArcTP20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_ArcTP__PetriNetModel_ArcTP20", None)
        self.__PetriNetModel_ArcTP20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_Place21"):
                opp_val = getattr(old_value, "PetriNetModel_Place21", None)
                if opp_val == self:
                    setattr(old_value, "PetriNetModel_Place21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_Place21"):
                opp_val = getattr(value, "PetriNetModel_Place21", None)
                setattr(value, "PetriNetModel_Place21", self)

    @property
    def PetriNetModel_ArcTP23(self):
        return self.__PetriNetModel_ArcTP23

    @PetriNetModel_ArcTP23.setter
    def PetriNetModel_ArcTP23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_ArcTP__PetriNetModel_ArcTP23", None)
        self.__PetriNetModel_ArcTP23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_Transition24"):
                opp_val = getattr(old_value, "PetriNetModel_Transition24", None)
                if opp_val == self:
                    setattr(old_value, "PetriNetModel_Transition24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_Transition24"):
                opp_val = getattr(value, "PetriNetModel_Transition24", None)
                setattr(value, "PetriNetModel_Transition24", self)

    @property
    def PetriNetModel_ArcTP(self):
        return self.__PetriNetModel_ArcTP

    @PetriNetModel_ArcTP.setter
    def PetriNetModel_ArcTP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_ArcTP__PetriNetModel_ArcTP", None)
        self.__PetriNetModel_ArcTP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_PetriNet4"):
                opp_val = getattr(old_value, "PetriNetModel_PetriNet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_PetriNet4"):
                opp_val = getattr(value, "PetriNetModel_PetriNet4", None)
                if opp_val is None:
                    setattr(value, "PetriNetModel_PetriNet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNetModel_ArcTP27(self):
        return self.__PetriNetModel_ArcTP27

    @PetriNetModel_ArcTP27.setter
    def PetriNetModel_ArcTP27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_ArcTP__PetriNetModel_ArcTP27", None)
        self.__PetriNetModel_ArcTP27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_Place26"):
                opp_val = getattr(old_value, "PetriNetModel_Place26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_Place26"):
                opp_val = getattr(value, "PetriNetModel_Place26", None)
                if opp_val is None:
                    setattr(value, "PetriNetModel_Place26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNetModel_ArcPT:

    def __init__(self, inscription: str, PetriNetModel_ArcPT: "PetriNetModel_PetriNet" = None, PetriNetModel_ArcPT14: "PetriNetModel_Transition" = None, PetriNetModel_ArcPT9: "PetriNetModel_Transition" = None, PetriNetModel_ArcPT17: "PetriNetModel_Place" = None, PetriNetModel_ArcPT30: "PetriNetModel_Place" = None):
        self.inscription = inscription
        self.PetriNetModel_ArcPT = PetriNetModel_ArcPT
        self.PetriNetModel_ArcPT14 = PetriNetModel_ArcPT14
        self.PetriNetModel_ArcPT9 = PetriNetModel_ArcPT9
        self.PetriNetModel_ArcPT17 = PetriNetModel_ArcPT17
        self.PetriNetModel_ArcPT30 = PetriNetModel_ArcPT30
        
    @property
    def inscription(self) -> str:
        return self.__inscription

    @inscription.setter
    def inscription(self, inscription: str):
        self.__inscription = inscription

    @property
    def PetriNetModel_ArcPT9(self):
        return self.__PetriNetModel_ArcPT9

    @PetriNetModel_ArcPT9.setter
    def PetriNetModel_ArcPT9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_ArcPT__PetriNetModel_ArcPT9", None)
        self.__PetriNetModel_ArcPT9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_Transition8"):
                opp_val = getattr(old_value, "PetriNetModel_Transition8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_Transition8"):
                opp_val = getattr(value, "PetriNetModel_Transition8", None)
                if opp_val is None:
                    setattr(value, "PetriNetModel_Transition8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNetModel_ArcPT17(self):
        return self.__PetriNetModel_ArcPT17

    @PetriNetModel_ArcPT17.setter
    def PetriNetModel_ArcPT17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_ArcPT__PetriNetModel_ArcPT17", None)
        self.__PetriNetModel_ArcPT17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_Place18"):
                opp_val = getattr(old_value, "PetriNetModel_Place18", None)
                if opp_val == self:
                    setattr(old_value, "PetriNetModel_Place18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_Place18"):
                opp_val = getattr(value, "PetriNetModel_Place18", None)
                setattr(value, "PetriNetModel_Place18", self)

    @property
    def PetriNetModel_ArcPT14(self):
        return self.__PetriNetModel_ArcPT14

    @PetriNetModel_ArcPT14.setter
    def PetriNetModel_ArcPT14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_ArcPT__PetriNetModel_ArcPT14", None)
        self.__PetriNetModel_ArcPT14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_Transition15"):
                opp_val = getattr(old_value, "PetriNetModel_Transition15", None)
                if opp_val == self:
                    setattr(old_value, "PetriNetModel_Transition15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_Transition15"):
                opp_val = getattr(value, "PetriNetModel_Transition15", None)
                setattr(value, "PetriNetModel_Transition15", self)

    @property
    def PetriNetModel_ArcPT30(self):
        return self.__PetriNetModel_ArcPT30

    @PetriNetModel_ArcPT30.setter
    def PetriNetModel_ArcPT30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_ArcPT__PetriNetModel_ArcPT30", None)
        self.__PetriNetModel_ArcPT30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_Place29"):
                opp_val = getattr(old_value, "PetriNetModel_Place29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_Place29"):
                opp_val = getattr(value, "PetriNetModel_Place29", None)
                if opp_val is None:
                    setattr(value, "PetriNetModel_Place29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNetModel_ArcPT(self):
        return self.__PetriNetModel_ArcPT

    @PetriNetModel_ArcPT.setter
    def PetriNetModel_ArcPT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_ArcPT__PetriNetModel_ArcPT", None)
        self.__PetriNetModel_ArcPT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_PetriNet2"):
                opp_val = getattr(old_value, "PetriNetModel_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_PetriNet2"):
                opp_val = getattr(value, "PetriNetModel_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "PetriNetModel_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNetModel_Place:

    def __init__(self, name: str, token: str, PetriNetModel_Place: "PetriNetModel_PetriNet" = None, PetriNetModel_Place18: "PetriNetModel_ArcPT" = None, PetriNetModel_Place21: "PetriNetModel_ArcTP" = None, PetriNetModel_Place26: set["PetriNetModel_ArcTP"] = None, PetriNetModel_Place29: set["PetriNetModel_ArcPT"] = None):
        self.name = name
        self.token = token
        self.PetriNetModel_Place = PetriNetModel_Place
        self.PetriNetModel_Place18 = PetriNetModel_Place18
        self.PetriNetModel_Place21 = PetriNetModel_Place21
        self.PetriNetModel_Place26 = PetriNetModel_Place26 if PetriNetModel_Place26 is not None else set()
        self.PetriNetModel_Place29 = PetriNetModel_Place29 if PetriNetModel_Place29 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

    @property
    def PetriNetModel_Place(self):
        return self.__PetriNetModel_Place

    @PetriNetModel_Place.setter
    def PetriNetModel_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Place__PetriNetModel_Place", None)
        self.__PetriNetModel_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_PetriNet6"):
                opp_val = getattr(old_value, "PetriNetModel_PetriNet6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_PetriNet6"):
                opp_val = getattr(value, "PetriNetModel_PetriNet6", None)
                if opp_val is None:
                    setattr(value, "PetriNetModel_PetriNet6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNetModel_Place29(self):
        return self.__PetriNetModel_Place29

    @PetriNetModel_Place29.setter
    def PetriNetModel_Place29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Place__PetriNetModel_Place29", None)
        self.__PetriNetModel_Place29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNetModel_ArcPT30"):
                    opp_val = getattr(item, "PetriNetModel_ArcPT30", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNetModel_ArcPT30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNetModel_ArcPT30"):
                    opp_val = getattr(item, "PetriNetModel_ArcPT30", None)
                    
                    setattr(item, "PetriNetModel_ArcPT30", self)
                    

    @property
    def PetriNetModel_Place18(self):
        return self.__PetriNetModel_Place18

    @PetriNetModel_Place18.setter
    def PetriNetModel_Place18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Place__PetriNetModel_Place18", None)
        self.__PetriNetModel_Place18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_ArcPT17"):
                opp_val = getattr(old_value, "PetriNetModel_ArcPT17", None)
                if opp_val == self:
                    setattr(old_value, "PetriNetModel_ArcPT17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_ArcPT17"):
                opp_val = getattr(value, "PetriNetModel_ArcPT17", None)
                setattr(value, "PetriNetModel_ArcPT17", self)

    @property
    def PetriNetModel_Place21(self):
        return self.__PetriNetModel_Place21

    @PetriNetModel_Place21.setter
    def PetriNetModel_Place21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Place__PetriNetModel_Place21", None)
        self.__PetriNetModel_Place21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_ArcTP20"):
                opp_val = getattr(old_value, "PetriNetModel_ArcTP20", None)
                if opp_val == self:
                    setattr(old_value, "PetriNetModel_ArcTP20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_ArcTP20"):
                opp_val = getattr(value, "PetriNetModel_ArcTP20", None)
                setattr(value, "PetriNetModel_ArcTP20", self)

    @property
    def PetriNetModel_Place26(self):
        return self.__PetriNetModel_Place26

    @PetriNetModel_Place26.setter
    def PetriNetModel_Place26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Place__PetriNetModel_Place26", None)
        self.__PetriNetModel_Place26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNetModel_ArcTP27"):
                    opp_val = getattr(item, "PetriNetModel_ArcTP27", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNetModel_ArcTP27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNetModel_ArcTP27"):
                    opp_val = getattr(item, "PetriNetModel_ArcTP27", None)
                    
                    setattr(item, "PetriNetModel_ArcTP27", self)
                    

class PetriNetModel_PetriNet:

    def __init__(self, name: str, PetriNetModel_PetriNet: set["PetriNetModel_Transition"] = None, PetriNetModel_PetriNet6: set["PetriNetModel_Place"] = None, PetriNetModel_PetriNet2: set["PetriNetModel_ArcPT"] = None, PetriNetModel_PetriNet4: set["PetriNetModel_ArcTP"] = None):
        self.name = name
        self.PetriNetModel_PetriNet = PetriNetModel_PetriNet if PetriNetModel_PetriNet is not None else set()
        self.PetriNetModel_PetriNet6 = PetriNetModel_PetriNet6 if PetriNetModel_PetriNet6 is not None else set()
        self.PetriNetModel_PetriNet2 = PetriNetModel_PetriNet2 if PetriNetModel_PetriNet2 is not None else set()
        self.PetriNetModel_PetriNet4 = PetriNetModel_PetriNet4 if PetriNetModel_PetriNet4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNetModel_PetriNet2(self):
        return self.__PetriNetModel_PetriNet2

    @PetriNetModel_PetriNet2.setter
    def PetriNetModel_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_PetriNet__PetriNetModel_PetriNet2", None)
        self.__PetriNetModel_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNetModel_ArcPT"):
                    opp_val = getattr(item, "PetriNetModel_ArcPT", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNetModel_ArcPT", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNetModel_ArcPT"):
                    opp_val = getattr(item, "PetriNetModel_ArcPT", None)
                    
                    setattr(item, "PetriNetModel_ArcPT", self)
                    

    @property
    def PetriNetModel_PetriNet(self):
        return self.__PetriNetModel_PetriNet

    @PetriNetModel_PetriNet.setter
    def PetriNetModel_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_PetriNet__PetriNetModel_PetriNet", None)
        self.__PetriNetModel_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNetModel_Transition"):
                    opp_val = getattr(item, "PetriNetModel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNetModel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNetModel_Transition"):
                    opp_val = getattr(item, "PetriNetModel_Transition", None)
                    
                    setattr(item, "PetriNetModel_Transition", self)
                    

    @property
    def PetriNetModel_PetriNet6(self):
        return self.__PetriNetModel_PetriNet6

    @PetriNetModel_PetriNet6.setter
    def PetriNetModel_PetriNet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_PetriNet__PetriNetModel_PetriNet6", None)
        self.__PetriNetModel_PetriNet6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNetModel_Place"):
                    opp_val = getattr(item, "PetriNetModel_Place", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNetModel_Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNetModel_Place"):
                    opp_val = getattr(item, "PetriNetModel_Place", None)
                    
                    setattr(item, "PetriNetModel_Place", self)
                    

    @property
    def PetriNetModel_PetriNet4(self):
        return self.__PetriNetModel_PetriNet4

    @PetriNetModel_PetriNet4.setter
    def PetriNetModel_PetriNet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_PetriNet__PetriNetModel_PetriNet4", None)
        self.__PetriNetModel_PetriNet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNetModel_ArcTP"):
                    opp_val = getattr(item, "PetriNetModel_ArcTP", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNetModel_ArcTP", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNetModel_ArcTP"):
                    opp_val = getattr(item, "PetriNetModel_ArcTP", None)
                    
                    setattr(item, "PetriNetModel_ArcTP", self)
                    

class PetriNetModel_Transition:

    def __init__(self, name: str, PetriNetModel_Transition: "PetriNetModel_PetriNet" = None, PetriNetModel_Transition11: set["PetriNetModel_ArcTP"] = None, PetriNetModel_Transition15: "PetriNetModel_ArcPT" = None, PetriNetModel_Transition8: set["PetriNetModel_ArcPT"] = None, PetriNetModel_Transition24: "PetriNetModel_ArcTP" = None):
        self.name = name
        self.PetriNetModel_Transition = PetriNetModel_Transition
        self.PetriNetModel_Transition11 = PetriNetModel_Transition11 if PetriNetModel_Transition11 is not None else set()
        self.PetriNetModel_Transition15 = PetriNetModel_Transition15
        self.PetriNetModel_Transition8 = PetriNetModel_Transition8 if PetriNetModel_Transition8 is not None else set()
        self.PetriNetModel_Transition24 = PetriNetModel_Transition24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNetModel_Transition11(self):
        return self.__PetriNetModel_Transition11

    @PetriNetModel_Transition11.setter
    def PetriNetModel_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Transition__PetriNetModel_Transition11", None)
        self.__PetriNetModel_Transition11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNetModel_ArcTP12"):
                    opp_val = getattr(item, "PetriNetModel_ArcTP12", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNetModel_ArcTP12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNetModel_ArcTP12"):
                    opp_val = getattr(item, "PetriNetModel_ArcTP12", None)
                    
                    setattr(item, "PetriNetModel_ArcTP12", self)
                    

    @property
    def PetriNetModel_Transition15(self):
        return self.__PetriNetModel_Transition15

    @PetriNetModel_Transition15.setter
    def PetriNetModel_Transition15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Transition__PetriNetModel_Transition15", None)
        self.__PetriNetModel_Transition15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_ArcPT14"):
                opp_val = getattr(old_value, "PetriNetModel_ArcPT14", None)
                if opp_val == self:
                    setattr(old_value, "PetriNetModel_ArcPT14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_ArcPT14"):
                opp_val = getattr(value, "PetriNetModel_ArcPT14", None)
                setattr(value, "PetriNetModel_ArcPT14", self)

    @property
    def PetriNetModel_Transition(self):
        return self.__PetriNetModel_Transition

    @PetriNetModel_Transition.setter
    def PetriNetModel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Transition__PetriNetModel_Transition", None)
        self.__PetriNetModel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_PetriNet"):
                opp_val = getattr(old_value, "PetriNetModel_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_PetriNet"):
                opp_val = getattr(value, "PetriNetModel_PetriNet", None)
                if opp_val is None:
                    setattr(value, "PetriNetModel_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNetModel_Transition8(self):
        return self.__PetriNetModel_Transition8

    @PetriNetModel_Transition8.setter
    def PetriNetModel_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Transition__PetriNetModel_Transition8", None)
        self.__PetriNetModel_Transition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNetModel_ArcPT9"):
                    opp_val = getattr(item, "PetriNetModel_ArcPT9", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNetModel_ArcPT9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNetModel_ArcPT9"):
                    opp_val = getattr(item, "PetriNetModel_ArcPT9", None)
                    
                    setattr(item, "PetriNetModel_ArcPT9", self)
                    

    @property
    def PetriNetModel_Transition24(self):
        return self.__PetriNetModel_Transition24

    @PetriNetModel_Transition24.setter
    def PetriNetModel_Transition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNetModel_Transition__PetriNetModel_Transition24", None)
        self.__PetriNetModel_Transition24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetModel_ArcTP23"):
                opp_val = getattr(old_value, "PetriNetModel_ArcTP23", None)
                if opp_val == self:
                    setattr(old_value, "PetriNetModel_ArcTP23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetModel_ArcTP23"):
                opp_val = getattr(value, "PetriNetModel_ArcTP23", None)
                setattr(value, "PetriNetModel_ArcTP23", self)
