from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class emfdb_C:

    def __init__(self, value: str, key: str, emfdb_C: "emfdb_A" = None):
        self.value = value
        self.key = key
        self.emfdb_C = emfdb_C
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def emfdb_C(self):
        return self.__emfdb_C

    @emfdb_C.setter
    def emfdb_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfdb_C__emfdb_C", None)
        self.__emfdb_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emfdb_A2"):
                opp_val = getattr(old_value, "emfdb_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emfdb_A2"):
                opp_val = getattr(value, "emfdb_A2", None)
                if opp_val is None:
                    setattr(value, "emfdb_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emfdb_B:

    def __init__(self, string: str, emfdb_B: "emfdb_A" = None):
        self.string = string
        self.emfdb_B = emfdb_B
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def emfdb_B(self):
        return self.__emfdb_B

    @emfdb_B.setter
    def emfdb_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfdb_B__emfdb_B", None)
        self.__emfdb_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emfdb_A"):
                opp_val = getattr(old_value, "emfdb_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emfdb_A"):
                opp_val = getattr(value, "emfdb_A", None)
                if opp_val is None:
                    setattr(value, "emfdb_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emfdb_A:

    def __init__(self, string: str, emfdb_A: set["emfdb_B"] = None, emfdb_A2: set["emfdb_C"] = None):
        self.string = string
        self.emfdb_A = emfdb_A if emfdb_A is not None else set()
        self.emfdb_A2 = emfdb_A2 if emfdb_A2 is not None else set()
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def emfdb_A2(self):
        return self.__emfdb_A2

    @emfdb_A2.setter
    def emfdb_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfdb_A__emfdb_A2", None)
        self.__emfdb_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emfdb_C"):
                    opp_val = getattr(item, "emfdb_C", None)
                    
                    if opp_val == self:
                        setattr(item, "emfdb_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emfdb_C"):
                    opp_val = getattr(item, "emfdb_C", None)
                    
                    setattr(item, "emfdb_C", self)
                    

    @property
    def emfdb_A(self):
        return self.__emfdb_A

    @emfdb_A.setter
    def emfdb_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfdb_A__emfdb_A", None)
        self.__emfdb_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emfdb_B"):
                    opp_val = getattr(item, "emfdb_B", None)
                    
                    if opp_val == self:
                        setattr(item, "emfdb_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emfdb_B"):
                    opp_val = getattr(item, "emfdb_B", None)
                    
                    setattr(item, "emfdb_B", self)
                    
