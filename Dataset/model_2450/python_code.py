from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Referenced:

    pass
class region_RgTransition(Referenced):

    def __init__(self, message: str, effect: str, event: str, region_RgTransition7: "region_RgState" = None, region_RgTransition: "region_RgInitialPseudostate" = None, region_RgTransition9: "region_RgState" = None):
        self.message = message
        self.effect = effect
        self.event = event
        self.region_RgTransition7 = region_RgTransition7
        self.region_RgTransition = region_RgTransition
        self.region_RgTransition9 = region_RgTransition9
        
    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def region_RgTransition7(self):
        return self.__region_RgTransition7

    @region_RgTransition7.setter
    def region_RgTransition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_region_RgTransition__region_RgTransition7", None)
        self.__region_RgTransition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "region_RgState6"):
                opp_val = getattr(old_value, "region_RgState6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "region_RgState6"):
                opp_val = getattr(value, "region_RgState6", None)
                if opp_val is None:
                    setattr(value, "region_RgState6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def region_RgTransition9(self):
        return self.__region_RgTransition9

    @region_RgTransition9.setter
    def region_RgTransition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_region_RgTransition__region_RgTransition9", None)
        self.__region_RgTransition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "region_RgState10"):
                opp_val = getattr(old_value, "region_RgState10", None)
                if opp_val == self:
                    setattr(old_value, "region_RgState10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "region_RgState10"):
                opp_val = getattr(value, "region_RgState10", None)
                setattr(value, "region_RgState10", self)

    @property
    def region_RgTransition(self):
        return self.__region_RgTransition

    @region_RgTransition.setter
    def region_RgTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_region_RgTransition__region_RgTransition", None)
        self.__region_RgTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "region_RgInitialPseudostate4"):
                opp_val = getattr(old_value, "region_RgInitialPseudostate4", None)
                if opp_val == self:
                    setattr(old_value, "region_RgInitialPseudostate4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "region_RgInitialPseudostate4"):
                opp_val = getattr(value, "region_RgInitialPseudostate4", None)
                setattr(value, "region_RgInitialPseudostate4", self)

class Named:

    pass
class region_RgState(Named):

    def __init__(self, entry: str, exit: str, isFinal: bool, region_RgState6: set["region_RgTransition"] = None, region_RgState: "region_RgRegion" = None, region_RgState10: "region_RgTransition" = None):
        self.entry = entry
        self.exit = exit
        self.isFinal = isFinal
        self.region_RgState6 = region_RgState6 if region_RgState6 is not None else set()
        self.region_RgState = region_RgState
        self.region_RgState10 = region_RgState10
        
    @property
    def entry(self) -> str:
        return self.__entry

    @entry.setter
    def entry(self, entry: str):
        self.__entry = entry

    @property
    def exit(self) -> str:
        return self.__exit

    @exit.setter
    def exit(self, exit: str):
        self.__exit = exit

    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def region_RgState6(self):
        return self.__region_RgState6

    @region_RgState6.setter
    def region_RgState6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_region_RgState__region_RgState6", None)
        self.__region_RgState6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "region_RgTransition7"):
                    opp_val = getattr(item, "region_RgTransition7", None)
                    
                    if opp_val == self:
                        setattr(item, "region_RgTransition7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "region_RgTransition7"):
                    opp_val = getattr(item, "region_RgTransition7", None)
                    
                    setattr(item, "region_RgTransition7", self)
                    

    @property
    def region_RgState(self):
        return self.__region_RgState

    @region_RgState.setter
    def region_RgState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_region_RgState__region_RgState", None)
        self.__region_RgState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "region_RgRegion2"):
                opp_val = getattr(old_value, "region_RgRegion2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "region_RgRegion2"):
                opp_val = getattr(value, "region_RgRegion2", None)
                if opp_val is None:
                    setattr(value, "region_RgRegion2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def region_RgState10(self):
        return self.__region_RgState10

    @region_RgState10.setter
    def region_RgState10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_region_RgState__region_RgState10", None)
        self.__region_RgState10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "region_RgTransition9"):
                opp_val = getattr(old_value, "region_RgTransition9", None)
                if opp_val == self:
                    setattr(old_value, "region_RgTransition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "region_RgTransition9"):
                opp_val = getattr(value, "region_RgTransition9", None)
                setattr(value, "region_RgTransition9", self)

class region_RgInitialPseudostate(Named):

    pass
class ModelRoot:

    pass
class region_RgRegion(ModelRoot):

    def __init__(self, containerClass: str, region_RgRegion: "region_RgInitialPseudostate" = None, region_RgRegion2: set["region_RgState"] = None):
        self.containerClass = containerClass
        self.region_RgRegion = region_RgRegion
        self.region_RgRegion2 = region_RgRegion2 if region_RgRegion2 is not None else set()
        
    @property
    def containerClass(self) -> str:
        return self.__containerClass

    @containerClass.setter
    def containerClass(self, containerClass: str):
        self.__containerClass = containerClass

    @property
    def region_RgRegion2(self):
        return self.__region_RgRegion2

    @region_RgRegion2.setter
    def region_RgRegion2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_region_RgRegion__region_RgRegion2", None)
        self.__region_RgRegion2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "region_RgState"):
                    opp_val = getattr(item, "region_RgState", None)
                    
                    if opp_val == self:
                        setattr(item, "region_RgState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "region_RgState"):
                    opp_val = getattr(item, "region_RgState", None)
                    
                    setattr(item, "region_RgState", self)
                    

    @property
    def region_RgRegion(self):
        return self.__region_RgRegion

    @region_RgRegion.setter
    def region_RgRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_region_RgRegion__region_RgRegion", None)
        self.__region_RgRegion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "region_RgInitialPseudostate"):
                opp_val = getattr(old_value, "region_RgInitialPseudostate", None)
                if opp_val == self:
                    setattr(old_value, "region_RgInitialPseudostate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "region_RgInitialPseudostate"):
                opp_val = getattr(value, "region_RgInitialPseudostate", None)
                setattr(value, "region_RgInitialPseudostate", self)
