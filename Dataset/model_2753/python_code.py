from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PK461726_A461726:

    def __init__(self, name: str, as: set["PK461726_B461726"] = None, A461726: "PK461726_B461726" = None):
        self.name = name
        self.as = as if as is not None else set()
        self.A461726 = A461726
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def A461726(self):
        return self.__A461726

    @A461726.setter
    def A461726(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PK461726_A461726__A461726", None)
        self.__A461726 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bs"):
                opp_val = getattr(old_value, "bs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bs"):
                opp_val = getattr(value, "bs", None)
                if opp_val is None:
                    setattr(value, "bs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def as(self):
        return self.__as

    @as.setter
    def as(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PK461726_A461726__as", None)
        self.__as = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B461726"):
                    opp_val = getattr(item, "B461726", None)
                    
                    if opp_val == self:
                        setattr(item, "B461726", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B461726"):
                    opp_val = getattr(item, "B461726", None)
                    
                    setattr(item, "B461726", self)
                    

class PK461726_B461726:

    def __init__(self, name: str, B461726: "PK461726_A461726" = None, bs: set["PK461726_A461726"] = None):
        self.name = name
        self.B461726 = B461726
        self.bs = bs if bs is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def B461726(self):
        return self.__B461726

    @B461726.setter
    def B461726(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PK461726_B461726__B461726", None)
        self.__B461726 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "as"):
                opp_val = getattr(old_value, "as", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "as"):
                opp_val = getattr(value, "as", None)
                if opp_val is None:
                    setattr(value, "as", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bs(self):
        return self.__bs

    @bs.setter
    def bs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PK461726_B461726__bs", None)
        self.__bs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "A461726"):
                    opp_val = getattr(item, "A461726", None)
                    
                    if opp_val == self:
                        setattr(item, "A461726", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "A461726"):
                    opp_val = getattr(item, "A461726", None)
                    
                    setattr(item, "A461726", self)
                    
