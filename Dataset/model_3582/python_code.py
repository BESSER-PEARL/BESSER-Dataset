from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class typeA_ElementA:

    def __init__(self, name: str, typeA_ElementA: "typeA_RootA" = None):
        self.name = name
        self.typeA_ElementA = typeA_ElementA
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeA_ElementA(self):
        return self.__typeA_ElementA

    @typeA_ElementA.setter
    def typeA_ElementA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeA_ElementA__typeA_ElementA", None)
        self.__typeA_ElementA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeA_RootA"):
                opp_val = getattr(old_value, "typeA_RootA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeA_RootA"):
                opp_val = getattr(value, "typeA_RootA", None)
                if opp_val is None:
                    setattr(value, "typeA_RootA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class typeA_RootA:

    def __init__(self, name: str, typeA_RootA: set["typeA_ElementA"] = None):
        self.name = name
        self.typeA_RootA = typeA_RootA if typeA_RootA is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeA_RootA(self):
        return self.__typeA_RootA

    @typeA_RootA.setter
    def typeA_RootA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeA_RootA__typeA_RootA", None)
        self.__typeA_RootA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "typeA_ElementA"):
                    opp_val = getattr(item, "typeA_ElementA", None)
                    
                    if opp_val == self:
                        setattr(item, "typeA_ElementA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "typeA_ElementA"):
                    opp_val = getattr(item, "typeA_ElementA", None)
                    
                    setattr(item, "typeA_ElementA", self)
                    
