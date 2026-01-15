from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeB_B:

    def __init__(self, name: str, TypeB_B: "TypeB_A" = None, TypeB_B2: set["TypeB_A"] = None):
        self.name = name
        self.TypeB_B = TypeB_B
        self.TypeB_B2 = TypeB_B2 if TypeB_B2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TypeB_B(self):
        return self.__TypeB_B

    @TypeB_B.setter
    def TypeB_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_B__TypeB_B", None)
        self.__TypeB_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_A"):
                opp_val = getattr(old_value, "TypeB_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_A"):
                opp_val = getattr(value, "TypeB_A", None)
                if opp_val is None:
                    setattr(value, "TypeB_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TypeB_B2(self):
        return self.__TypeB_B2

    @TypeB_B2.setter
    def TypeB_B2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_B__TypeB_B2", None)
        self.__TypeB_B2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeB_A3"):
                    opp_val = getattr(item, "TypeB_A3", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeB_A3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeB_A3"):
                    opp_val = getattr(item, "TypeB_A3", None)
                    
                    setattr(item, "TypeB_A3", self)
                    

class TypeB_A:

    def __init__(self, name: str, TypeB_A: set["TypeB_B"] = None, TypeB_A3: "TypeB_B" = None):
        self.name = name
        self.TypeB_A = TypeB_A if TypeB_A is not None else set()
        self.TypeB_A3 = TypeB_A3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TypeB_A3(self):
        return self.__TypeB_A3

    @TypeB_A3.setter
    def TypeB_A3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_A__TypeB_A3", None)
        self.__TypeB_A3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeB_B2"):
                opp_val = getattr(old_value, "TypeB_B2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeB_B2"):
                opp_val = getattr(value, "TypeB_B2", None)
                if opp_val is None:
                    setattr(value, "TypeB_B2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TypeB_A(self):
        return self.__TypeB_A

    @TypeB_A.setter
    def TypeB_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeB_A__TypeB_A", None)
        self.__TypeB_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeB_B"):
                    opp_val = getattr(item, "TypeB_B", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeB_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeB_B"):
                    opp_val = getattr(item, "TypeB_B", None)
                    
                    setattr(item, "TypeB_B", self)
                    
