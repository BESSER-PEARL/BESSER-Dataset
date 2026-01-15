from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class coom_Transition:

    def __init__(self, name: str, coom_Transition: "coom_ComponentOnOffManifest" = None, coom_Transition6: "coom_State" = None, coom_Transition9: "coom_State" = None):
        self.name = name
        self.coom_Transition = coom_Transition
        self.coom_Transition6 = coom_Transition6
        self.coom_Transition9 = coom_Transition9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def coom_Transition(self):
        return self.__coom_Transition

    @coom_Transition.setter
    def coom_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coom_Transition__coom_Transition", None)
        self.__coom_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coom_ComponentOnOffManifest4"):
                opp_val = getattr(old_value, "coom_ComponentOnOffManifest4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coom_ComponentOnOffManifest4"):
                opp_val = getattr(value, "coom_ComponentOnOffManifest4", None)
                if opp_val is None:
                    setattr(value, "coom_ComponentOnOffManifest4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coom_Transition9(self):
        return self.__coom_Transition9

    @coom_Transition9.setter
    def coom_Transition9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coom_Transition__coom_Transition9", None)
        self.__coom_Transition9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coom_State10"):
                opp_val = getattr(old_value, "coom_State10", None)
                if opp_val == self:
                    setattr(old_value, "coom_State10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coom_State10"):
                opp_val = getattr(value, "coom_State10", None)
                setattr(value, "coom_State10", self)

    @property
    def coom_Transition6(self):
        return self.__coom_Transition6

    @coom_Transition6.setter
    def coom_Transition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coom_Transition__coom_Transition6", None)
        self.__coom_Transition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coom_State7"):
                opp_val = getattr(old_value, "coom_State7", None)
                if opp_val == self:
                    setattr(old_value, "coom_State7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coom_State7"):
                opp_val = getattr(value, "coom_State7", None)
                setattr(value, "coom_State7", self)

class coom_State:

    def __init__(self, initial: bool, name: str, coom_State: "coom_ComponentOnOffManifest" = None, coom_State7: "coom_Transition" = None, coom_State10: "coom_Transition" = None):
        self.initial = initial
        self.name = name
        self.coom_State = coom_State
        self.coom_State7 = coom_State7
        self.coom_State10 = coom_State10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initial(self) -> bool:
        return self.__initial

    @initial.setter
    def initial(self, initial: bool):
        self.__initial = initial

    @property
    def coom_State10(self):
        return self.__coom_State10

    @coom_State10.setter
    def coom_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coom_State__coom_State10", None)
        self.__coom_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coom_Transition9"):
                opp_val = getattr(old_value, "coom_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "coom_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coom_Transition9"):
                opp_val = getattr(value, "coom_Transition9", None)
                setattr(value, "coom_Transition9", self)

    @property
    def coom_State(self):
        return self.__coom_State

    @coom_State.setter
    def coom_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coom_State__coom_State", None)
        self.__coom_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coom_ComponentOnOffManifest2"):
                opp_val = getattr(old_value, "coom_ComponentOnOffManifest2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coom_ComponentOnOffManifest2"):
                opp_val = getattr(value, "coom_ComponentOnOffManifest2", None)
                if opp_val is None:
                    setattr(value, "coom_ComponentOnOffManifest2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coom_State7(self):
        return self.__coom_State7

    @coom_State7.setter
    def coom_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coom_State__coom_State7", None)
        self.__coom_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coom_Transition6"):
                opp_val = getattr(old_value, "coom_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "coom_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coom_Transition6"):
                opp_val = getattr(value, "coom_Transition6", None)
                setattr(value, "coom_Transition6", self)

class coom_Version:

    def __init__(self, majorMalue: int, minorValue: int, coom_Version: "coom_ComponentOnOffManifest" = None):
        self.majorMalue = majorMalue
        self.minorValue = minorValue
        self.coom_Version = coom_Version
        
    @property
    def minorValue(self) -> int:
        return self.__minorValue

    @minorValue.setter
    def minorValue(self, minorValue: int):
        self.__minorValue = minorValue

    @property
    def majorMalue(self) -> int:
        return self.__majorMalue

    @majorMalue.setter
    def majorMalue(self, majorMalue: int):
        self.__majorMalue = majorMalue

    @property
    def coom_Version(self):
        return self.__coom_Version

    @coom_Version.setter
    def coom_Version(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coom_Version__coom_Version", None)
        self.__coom_Version = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coom_ComponentOnOffManifest"):
                opp_val = getattr(old_value, "coom_ComponentOnOffManifest", None)
                if opp_val == self:
                    setattr(old_value, "coom_ComponentOnOffManifest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coom_ComponentOnOffManifest"):
                opp_val = getattr(value, "coom_ComponentOnOffManifest", None)
                setattr(value, "coom_ComponentOnOffManifest", self)

class coom_ComponentOnOffManifest:

    def __init__(self, name: str, coom_ComponentOnOffManifest: "coom_Version" = None, coom_ComponentOnOffManifest2: set["coom_State"] = None, coom_ComponentOnOffManifest4: set["coom_Transition"] = None):
        self.name = name
        self.coom_ComponentOnOffManifest = coom_ComponentOnOffManifest
        self.coom_ComponentOnOffManifest2 = coom_ComponentOnOffManifest2 if coom_ComponentOnOffManifest2 is not None else set()
        self.coom_ComponentOnOffManifest4 = coom_ComponentOnOffManifest4 if coom_ComponentOnOffManifest4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def coom_ComponentOnOffManifest(self):
        return self.__coom_ComponentOnOffManifest

    @coom_ComponentOnOffManifest.setter
    def coom_ComponentOnOffManifest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coom_ComponentOnOffManifest__coom_ComponentOnOffManifest", None)
        self.__coom_ComponentOnOffManifest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coom_Version"):
                opp_val = getattr(old_value, "coom_Version", None)
                if opp_val == self:
                    setattr(old_value, "coom_Version", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coom_Version"):
                opp_val = getattr(value, "coom_Version", None)
                setattr(value, "coom_Version", self)

    @property
    def coom_ComponentOnOffManifest2(self):
        return self.__coom_ComponentOnOffManifest2

    @coom_ComponentOnOffManifest2.setter
    def coom_ComponentOnOffManifest2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coom_ComponentOnOffManifest__coom_ComponentOnOffManifest2", None)
        self.__coom_ComponentOnOffManifest2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coom_State"):
                    opp_val = getattr(item, "coom_State", None)
                    
                    if opp_val == self:
                        setattr(item, "coom_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coom_State"):
                    opp_val = getattr(item, "coom_State", None)
                    
                    setattr(item, "coom_State", self)
                    

    @property
    def coom_ComponentOnOffManifest4(self):
        return self.__coom_ComponentOnOffManifest4

    @coom_ComponentOnOffManifest4.setter
    def coom_ComponentOnOffManifest4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coom_ComponentOnOffManifest__coom_ComponentOnOffManifest4", None)
        self.__coom_ComponentOnOffManifest4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coom_Transition"):
                    opp_val = getattr(item, "coom_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "coom_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coom_Transition"):
                    opp_val = getattr(item, "coom_Transition", None)
                    
                    setattr(item, "coom_Transition", self)
                    
