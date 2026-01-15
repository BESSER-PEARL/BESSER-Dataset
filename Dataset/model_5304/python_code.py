from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class typeB_ElementB:

    def __init__(self, name: str, typeB_ElementB: "typeB_RootB" = None):
        self.name = name
        self.typeB_ElementB = typeB_ElementB
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeB_ElementB(self):
        return self.__typeB_ElementB

    @typeB_ElementB.setter
    def typeB_ElementB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeB_ElementB__typeB_ElementB", None)
        self.__typeB_ElementB = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeB_RootB"):
                opp_val = getattr(old_value, "typeB_RootB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeB_RootB"):
                opp_val = getattr(value, "typeB_RootB", None)
                if opp_val is None:
                    setattr(value, "typeB_RootB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class typeB_RootB:

    pass