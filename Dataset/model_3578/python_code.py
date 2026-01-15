from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TypeA_PortA:

    def __init__(self, name: str, TypeA_PortA: "TypeA_BlockA" = None, TypeA_PortA3: "TypeA_BlockA" = None):
        self.name = name
        self.TypeA_PortA = TypeA_PortA
        self.TypeA_PortA3 = TypeA_PortA3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TypeA_PortA3(self):
        return self.__TypeA_PortA3

    @TypeA_PortA3.setter
    def TypeA_PortA3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_PortA__TypeA_PortA3", None)
        self.__TypeA_PortA3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeA_BlockA2"):
                opp_val = getattr(old_value, "TypeA_BlockA2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeA_BlockA2"):
                opp_val = getattr(value, "TypeA_BlockA2", None)
                if opp_val is None:
                    setattr(value, "TypeA_BlockA2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TypeA_PortA(self):
        return self.__TypeA_PortA

    @TypeA_PortA.setter
    def TypeA_PortA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TypeA_PortA__TypeA_PortA", None)
        self.__TypeA_PortA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeA_BlockA"):
                opp_val = getattr(old_value, "TypeA_BlockA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeA_BlockA"):
                opp_val = getattr(value, "TypeA_BlockA", None)
                if opp_val is None:
                    setattr(value, "TypeA_BlockA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TypeA_BlockA:

    pass