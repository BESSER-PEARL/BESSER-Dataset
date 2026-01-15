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

    pass