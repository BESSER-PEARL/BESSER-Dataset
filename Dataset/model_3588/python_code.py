from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeA_B:

    def __init__(self, nameB: str, TypeA_B2: set["TypeA_A"] = None, TypeA_B: "TypeA_A" = None):
        self.nameB = nameB
        self.TypeA_B2 = TypeA_B2 if TypeA_B2 is not None else set()
        self.TypeA_B = TypeA_B
        
    @property
    def nameB(self) -> str:
        return self.__nameB

    @nameB.setter
    def nameB(self, nameB: str):
        self.__nameB = nameB

    @property
    def TypeA_B2(self):
        return self.__TypeA_B2

    @TypeA_B2.setter
    def TypeA_B2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_B__TypeA_B2", None)
        self.__TypeA_B2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeA_A3"):
                    opp_val = getattr(item, "TypeA_A3", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeA_A3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeA_A3"):
                    opp_val = getattr(item, "TypeA_A3", None)
                    
                    setattr(item, "TypeA_A3", self)
                    

    @property
    def TypeA_B(self):
        return self.__TypeA_B

    @TypeA_B.setter
    def TypeA_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_B__TypeA_B", None)
        self.__TypeA_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeA_A"):
                opp_val = getattr(old_value, "TypeA_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeA_A"):
                opp_val = getattr(value, "TypeA_A", None)
                if opp_val is None:
                    setattr(value, "TypeA_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypeA_A:

    def __init__(self, nameA: str, TypeA_A3: "TypeA_B" = None, TypeA_A: set["TypeA_B"] = None):
        self.nameA = nameA
        self.TypeA_A3 = TypeA_A3
        self.TypeA_A = TypeA_A if TypeA_A is not None else set()
        
    @property
    def nameA(self) -> str:
        return self.__nameA

    @nameA.setter
    def nameA(self, nameA: str):
        self.__nameA = nameA

    @property
    def TypeA_A(self):
        return self.__TypeA_A

    @TypeA_A.setter
    def TypeA_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_A__TypeA_A", None)
        self.__TypeA_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeA_B"):
                    opp_val = getattr(item, "TypeA_B", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeA_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeA_B"):
                    opp_val = getattr(item, "TypeA_B", None)
                    
                    setattr(item, "TypeA_B", self)
                    

    @property
    def TypeA_A3(self):
        return self.__TypeA_A3

    @TypeA_A3.setter
    def TypeA_A3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_A__TypeA_A3", None)
        self.__TypeA_A3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeA_B2"):
                opp_val = getattr(old_value, "TypeA_B2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeA_B2"):
                opp_val = getattr(value, "TypeA_B2", None)
                if opp_val is None:
                    setattr(value, "TypeA_B2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
