from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fSM_Transition:

    pass
class fSM_EnumerationLiteral:

    def __init__(self, name: str, fSM_EnumerationLiteral: "fSM_State" = None, fSM_EnumerationLiteral17: "fSM_EnumerationType" = None):
        self.name = name
        self.fSM_EnumerationLiteral = fSM_EnumerationLiteral
        self.fSM_EnumerationLiteral17 = fSM_EnumerationLiteral17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fSM_EnumerationLiteral17(self):
        return self.__fSM_EnumerationLiteral17

    @fSM_EnumerationLiteral17.setter
    def fSM_EnumerationLiteral17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fSM_EnumerationLiteral__fSM_EnumerationLiteral17", None)
        self.__fSM_EnumerationLiteral17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fSM_EnumerationType16"):
                opp_val = getattr(old_value, "fSM_EnumerationType16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fSM_EnumerationType16"):
                opp_val = getattr(value, "fSM_EnumerationType16", None)
                if opp_val is None:
                    setattr(value, "fSM_EnumerationType16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fSM_EnumerationLiteral(self):
        return self.__fSM_EnumerationLiteral

    @fSM_EnumerationLiteral.setter
    def fSM_EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fSM_EnumerationLiteral__fSM_EnumerationLiteral", None)
        self.__fSM_EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fSM_State9"):
                opp_val = getattr(old_value, "fSM_State9", None)
                if opp_val == self:
                    setattr(old_value, "fSM_State9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fSM_State9"):
                opp_val = getattr(value, "fSM_State9", None)
                setattr(value, "fSM_State9", self)

class fSM_State:

    pass
class fSM_FSM:

    pass
class fSM_EnumerationType:

    def __init__(self, name: str, fSM_EnumerationType: "fSM_Model" = None, fSM_EnumerationType5: "fSM_FSM" = None, fSM_EnumerationType16: set["fSM_EnumerationLiteral"] = None):
        self.name = name
        self.fSM_EnumerationType = fSM_EnumerationType
        self.fSM_EnumerationType5 = fSM_EnumerationType5
        self.fSM_EnumerationType16 = fSM_EnumerationType16 if fSM_EnumerationType16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fSM_EnumerationType(self):
        return self.__fSM_EnumerationType

    @fSM_EnumerationType.setter
    def fSM_EnumerationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fSM_EnumerationType__fSM_EnumerationType", None)
        self.__fSM_EnumerationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fSM_Model"):
                opp_val = getattr(old_value, "fSM_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fSM_Model"):
                opp_val = getattr(value, "fSM_Model", None)
                if opp_val is None:
                    setattr(value, "fSM_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fSM_EnumerationType5(self):
        return self.__fSM_EnumerationType5

    @fSM_EnumerationType5.setter
    def fSM_EnumerationType5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fSM_EnumerationType__fSM_EnumerationType5", None)
        self.__fSM_EnumerationType5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fSM_FSM4"):
                opp_val = getattr(old_value, "fSM_FSM4", None)
                if opp_val == self:
                    setattr(old_value, "fSM_FSM4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fSM_FSM4"):
                opp_val = getattr(value, "fSM_FSM4", None)
                setattr(value, "fSM_FSM4", self)

    @property
    def fSM_EnumerationType16(self):
        return self.__fSM_EnumerationType16

    @fSM_EnumerationType16.setter
    def fSM_EnumerationType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fSM_EnumerationType__fSM_EnumerationType16", None)
        self.__fSM_EnumerationType16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fSM_EnumerationLiteral17"):
                    opp_val = getattr(item, "fSM_EnumerationLiteral17", None)
                    
                    if opp_val == self:
                        setattr(item, "fSM_EnumerationLiteral17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fSM_EnumerationLiteral17"):
                    opp_val = getattr(item, "fSM_EnumerationLiteral17", None)
                    
                    setattr(item, "fSM_EnumerationLiteral17", self)
                    

class fSM_Model:

    pass