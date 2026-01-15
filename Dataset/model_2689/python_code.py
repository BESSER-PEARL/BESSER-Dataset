from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class refac_K:

    pass
class refac_X:

    pass
class refac_N99:

    pass
class refac_M:

    pass
class refac_W:

    def __init__(self, name: str, refac_W: "refac_A" = None, refac_W17: "refac_C" = None):
        self.name = name
        self.refac_W = refac_W
        self.refac_W17 = refac_W17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def refac_W17(self):
        return self.__refac_W17

    @refac_W17.setter
    def refac_W17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_refac_W__refac_W17", None)
        self.__refac_W17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refac_C18"):
                opp_val = getattr(old_value, "refac_C18", None)
                if opp_val == self:
                    setattr(old_value, "refac_C18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refac_C18"):
                opp_val = getattr(value, "refac_C18", None)
                setattr(value, "refac_C18", self)

    @property
    def refac_W(self):
        return self.__refac_W

    @refac_W.setter
    def refac_W(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_refac_W__refac_W", None)
        self.__refac_W = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refac_A4"):
                opp_val = getattr(old_value, "refac_A4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refac_A4"):
                opp_val = getattr(value, "refac_A4", None)
                if opp_val is None:
                    setattr(value, "refac_A4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class refac_C:

    pass
class refac_B:

    pass
class refac_A:

    pass