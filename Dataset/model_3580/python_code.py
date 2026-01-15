from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class typeA_PortA:

    def __init__(self, name: str, typeA_PortA: "typeA_BlockA" = None, typeA_PortA3: "typeA_BlockA" = None):
        self.name = name
        self.typeA_PortA = typeA_PortA
        self.typeA_PortA3 = typeA_PortA3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def typeA_PortA(self):
        return self.__typeA_PortA

    @typeA_PortA.setter
    def typeA_PortA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeA_PortA__typeA_PortA", None)
        self.__typeA_PortA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeA_BlockA"):
                opp_val = getattr(old_value, "typeA_BlockA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeA_BlockA"):
                opp_val = getattr(value, "typeA_BlockA", None)
                if opp_val is None:
                    setattr(value, "typeA_BlockA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def typeA_PortA3(self):
        return self.__typeA_PortA3

    @typeA_PortA3.setter
    def typeA_PortA3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_typeA_PortA__typeA_PortA3", None)
        self.__typeA_PortA3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "typeA_BlockA2"):
                opp_val = getattr(old_value, "typeA_BlockA2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "typeA_BlockA2"):
                opp_val = getattr(value, "typeA_BlockA2", None)
                if opp_val is None:
                    setattr(value, "typeA_BlockA2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class typeA_BlockA:

    pass