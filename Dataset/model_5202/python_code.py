from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeD_BElementName:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class TypeD_AElementName:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class TypeD_C:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class TypeD_B:

    def __init__(self, name: str, TypeD_B: "TypeD_A" = None, TypeD_B2: set["TypeD_A"] = None):
        self.name = name
        self.TypeD_B = TypeD_B
        self.TypeD_B2 = TypeD_B2 if TypeD_B2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TypeD_B2(self):
        return self.__TypeD_B2

    @TypeD_B2.setter
    def TypeD_B2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeD_B__TypeD_B2", None)
        self.__TypeD_B2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeD_A3"):
                    opp_val = getattr(item, "TypeD_A3", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeD_A3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeD_A3"):
                    opp_val = getattr(item, "TypeD_A3", None)
                    
                    setattr(item, "TypeD_A3", self)
                    

    @property
    def TypeD_B(self):
        return self.__TypeD_B

    @TypeD_B.setter
    def TypeD_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeD_B__TypeD_B", None)
        self.__TypeD_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeD_A"):
                opp_val = getattr(old_value, "TypeD_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeD_A"):
                opp_val = getattr(value, "TypeD_A", None)
                if opp_val is None:
                    setattr(value, "TypeD_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypeD_A:

    def __init__(self, name: str, TypeD_A: set["TypeD_B"] = None, TypeD_A3: "TypeD_B" = None):
        self.name = name
        self.TypeD_A = TypeD_A if TypeD_A is not None else set()
        self.TypeD_A3 = TypeD_A3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TypeD_A(self):
        return self.__TypeD_A

    @TypeD_A.setter
    def TypeD_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeD_A__TypeD_A", None)
        self.__TypeD_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeD_B"):
                    opp_val = getattr(item, "TypeD_B", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeD_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeD_B"):
                    opp_val = getattr(item, "TypeD_B", None)
                    
                    setattr(item, "TypeD_B", self)
                    

    @property
    def TypeD_A3(self):
        return self.__TypeD_A3

    @TypeD_A3.setter
    def TypeD_A3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeD_A__TypeD_A3", None)
        self.__TypeD_A3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeD_B2"):
                opp_val = getattr(old_value, "TypeD_B2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeD_B2"):
                opp_val = getattr(value, "TypeD_B2", None)
                if opp_val is None:
                    setattr(value, "TypeD_B2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
