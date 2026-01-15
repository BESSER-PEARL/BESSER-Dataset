from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeA_C:

    def __init__(self, name: str, description1: str, description2: str, TypeA_C: "TypeA_A" = None):
        self.name = name
        self.description1 = description1
        self.description2 = description2
        self.TypeA_C = TypeA_C
        
    @property
    def description1(self) -> str:
        return self.__description1

    @description1.setter
    def description1(self, description1: str):
        self.__description1 = description1

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description2(self) -> str:
        return self.__description2

    @description2.setter
    def description2(self, description2: str):
        self.__description2 = description2

    @property
    def TypeA_C(self):
        return self.__TypeA_C

    @TypeA_C.setter
    def TypeA_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_C__TypeA_C", None)
        self.__TypeA_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeA_A2"):
                opp_val = getattr(old_value, "TypeA_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeA_A2"):
                opp_val = getattr(value, "TypeA_A2", None)
                if opp_val is None:
                    setattr(value, "TypeA_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypeA_B:

    def __init__(self, name: str, description1: str, description2: str, description3: str, TypeA_B: "TypeA_A" = None):
        self.name = name
        self.description1 = description1
        self.description2 = description2
        self.description3 = description3
        self.TypeA_B = TypeA_B
        
    @property
    def description1(self) -> str:
        return self.__description1

    @description1.setter
    def description1(self, description1: str):
        self.__description1 = description1

    @property
    def description3(self) -> str:
        return self.__description3

    @description3.setter
    def description3(self, description3: str):
        self.__description3 = description3

    @property
    def description2(self) -> str:
        return self.__description2

    @description2.setter
    def description2(self, description2: str):
        self.__description2 = description2

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    def __init__(self, name: str, TypeA_A: set["TypeA_B"] = None, TypeA_A2: set["TypeA_C"] = None):
        self.name = name
        self.TypeA_A = TypeA_A if TypeA_A is not None else set()
        self.TypeA_A2 = TypeA_A2 if TypeA_A2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def TypeA_A2(self):
        return self.__TypeA_A2

    @TypeA_A2.setter
    def TypeA_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_A__TypeA_A2", None)
        self.__TypeA_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeA_C"):
                    opp_val = getattr(item, "TypeA_C", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeA_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeA_C"):
                    opp_val = getattr(item, "TypeA_C", None)
                    
                    setattr(item, "TypeA_C", self)
                    
