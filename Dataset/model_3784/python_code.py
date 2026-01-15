from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class d_D:

    def __init__(self, name: str, atts: str, d_D: "d_D" = None, d_D0: set["d_D"] = None):
        self.name = name
        self.atts = atts
        self.d_D = d_D
        self.d_D0 = d_D0 if d_D0 is not None else set()
        
    @property
    def atts(self) -> str:
        return self.__atts

    @atts.setter
    def atts(self, atts: str):
        self.__atts = atts

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def d_D0(self):
        return self.__d_D0

    @d_D0.setter
    def d_D0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_d_D__d_D0", None)
        self.__d_D0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "d_D"):
                    opp_val = getattr(item, "d_D", None)
                    
                    if opp_val == self:
                        setattr(item, "d_D", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "d_D"):
                    opp_val = getattr(item, "d_D", None)
                    
                    setattr(item, "d_D", self)
                    

    @property
    def d_D(self):
        return self.__d_D

    @d_D.setter
    def d_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_d_D__d_D", None)
        self.__d_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "d_D0"):
                opp_val = getattr(old_value, "d_D0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "d_D0"):
                opp_val = getattr(value, "d_D0", None)
                if opp_val is None:
                    setattr(value, "d_D0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
