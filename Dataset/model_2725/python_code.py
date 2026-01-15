from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class direction_C:

    pass
class A:

    pass
class direction_B(A):

    pass
class direction_A:

    def __init__(self, name: str, direction_A: "direction_C" = None):
        self.name = name
        self.direction_A = direction_A
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def direction_A(self):
        return self.__direction_A

    @direction_A.setter
    def direction_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_direction_A__direction_A", None)
        self.__direction_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "direction_C"):
                opp_val = getattr(old_value, "direction_C", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "direction_C"):
                opp_val = getattr(value, "direction_C", None)
                if opp_val is None:
                    setattr(value, "direction_C", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
